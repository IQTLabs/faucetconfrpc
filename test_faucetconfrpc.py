#!/usr/bin/python3

"""Tests for faucetconfrpc."""

from contextlib import closing
import shutil
import socket
import subprocess
import tempfile
import time
import os
import yaml
import unittest
from faucetconfrpc.faucetconfrpc_client_lib import FaucetConfRpcClient
from faucetconfrpc.faucetconfrpc_server import Server, _ServerError


class ServerMethodTests(unittest.TestCase):

    def test_merge(self):
        server = Server('.', None)
        existing_yaml = {'dps': {
            'switch1': {
                'interfaces': {
                    1: {'native_vlan': 100}}}}}
        dpid_yaml = {'dps': {'switch1': {'dp_id': 1}}}
        merged_yaml = server._yaml_merge(existing_yaml, dpid_yaml)
        # dp_id is set.
        assert (merged_yaml ==
            {'dps': {
                'switch1': {
                    'dp_id': 1,
                    'interfaces': {
                        1: {'native_vlan': 100}}}}})
        existing_yaml = {'dps': {
            'switch1': {
                'interfaces': {
                    1: {'native_vlan': 100}}}}}
        # add new switch and stacking link.
        new_yaml = {'dps': {
            'switch1': {
                'stack': {'priority': 1},
                'interfaces': {
                     9: {'stack': {'dp': 'switch2', 'port': 999}}}},
            'switch2': {
                'dp_id': 2,
                'interfaces': {
                    999: {'stack': {'dp': 'switch1', 'port': 9}}}}}}
        merged_yaml = server._yaml_merge(existing_yaml, new_yaml)
        assert (merged_yaml ==
            {'dps': {
                'switch1': {
                    'stack': {'priority': 1},
                    'interfaces': {
                        1: {'native_vlan': 100},
                        9: {'stack': {'dp': 'switch2', 'port': 999}}}},
                'switch2': {
                    'dp_id': 2,
                    'interfaces': {
                        999: {'stack': {'dp': 'switch1', 'port': 9}}}}}})

    def test_parse(self):
        server = Server('.', None)
        with self.assertRaises(_ServerError):
            server._yaml_parse('{missing')
        with self.assertRaises(_ServerError):
            server._yaml_parse('{{unhashable}: 1}')

class ServerIntTests(unittest.TestCase):

    default_test_yaml_str = """
        {dps: {ovs: {
            dp_id: 1,
            hardware: Open vSwitch,
            interfaces: {
                1: {native_vlan: 100, acls_in: []},
                2: {native_vlan: 100},
                3: {output_only: true, mirror: [1]}}}},
         acls: {test: [{rule: {actions: {allow: 0}}}]}}
    """

    def _wait_for_port(self, host, port, timeout=10):
        for _ in range(timeout):
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                if sock.connect_ex((host, port)) == 0:
                    return  # pytype: disable=not-callable
            time.sleep(1)
        self.fail('server did not start')

    @classmethod
    def tearDownClass(cls):
        cls.server.terminate()
        cls.server.wait()
        shutil.rmtree(cls.tmpdir)

    @classmethod
    def setUpClass(cls):
        cls.tmpdir = tempfile.mkdtemp()
        cls.default_test_yaml = yaml.safe_load(cls.default_test_yaml_str)
        cls.default_config = 'test.yaml'
        with open(os.path.join(cls.tmpdir, cls.default_config), 'w') as test_yaml_file:
            test_yaml_file.write(cls.default_test_yaml_str)  # pytype: disable=wrong-arg-types

        host = 'localhost'
        port = 59999
        certstrap = shutil.which('certstrap')
        cls.assertTrue(certstrap, 'certstrap not found')
        for cmd in (
                ['init', '--common-name', 'ca', '--passphrase', ''],
                ['request-cert', '--common-name', 'client', '--passphrase', ''],
                ['sign', 'client', '--CA', 'ca'],
                ['request-cert', '--common-name', host, '--passphrase', ''],
                ['sign', host, '--CA', 'ca']):
            subprocess.check_call([certstrap, '--depot-path', cls.tmpdir] + cmd)
        client_key = os.path.join(cls.tmpdir, 'client.key')
        client_cert = os.path.join(cls.tmpdir, 'client.crt')
        server_key = os.path.join(cls.tmpdir, '%s.key' % host)
        server_cert = os.path.join(cls.tmpdir, '%s.crt' % host)
        ca_cert = os.path.join(cls.tmpdir, 'ca.crt')

        cls.server = subprocess.Popen(
            ['timeout',
             '10s',
             './faucetconfrpc/faucetconfrpc_server.py',
             '--config_dir=%s' % cls.tmpdir,
             '--default_config=%s' % cls.default_config,
             '--port=%u' % port,
             '--host=%s' % host,
             '--key=%s' % server_key,
             '--cert=%s' % server_cert,
             '--cacert=%s' % ca_cert,
             ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        cls._wait_for_port(cls, host, port)
        server_addr = '%s:%u' % (host, port)
        cls.client = FaucetConfRpcClient(client_key, client_cert, ca_cert, server_addr)

    def setUp(self):
        self.default_test_yaml = yaml.safe_load(self.default_test_yaml_str)
        assert self.client.set_config_file(
            self.default_test_yaml_str, config_filename=self.default_config, merge=False)

    def test_del_dps(self):
        three_dps_yaml = {
            'dps': {
                'ovs1': {
                    'dp_id': 1,
                    'hardware': 'Open vSwitch',
                    'stack': {'priority': 1},
                    'interfaces': {
                        1: {'native_vlan': 100},
                        2: {'stack': {'dp': 'ovs2', 'port': 2}}}},
                'ovs2': {
                    'dp_id': 2,
                    'hardware': 'Open vSwitch',
                    'interfaces': {
                        1: {'native_vlan': 100},
                        2: {'stack': {'dp': 'ovs1', 'port': 2}}}},
                'ovs3': {
                    'dp_id': 3,
                    'hardware': 'Open vSwitch',
                    'interfaces': {
                        1: {'native_vlan': 100}}}}}
        assert self.client.set_config_file(
            yaml.dump(three_dps_yaml), config_filename=self.default_config, merge=False)
        response = self.client.del_dps(['ovs2'])
        assert response is not None
        assert self.client.del_dp_interfaces([('ovs3', [1])], delete_empty_dp=True) is not None
        del three_dps_yaml['dps']['ovs3']
        del three_dps_yaml['dps']['ovs2']
        del three_dps_yaml['dps']['ovs1']['interfaces'][2]
        result = self.client.get_config_file(config_filename=self.default_config)
        assert three_dps_yaml == result

    def test_del_interfaces(self):
        response = self.client.del_dp_interfaces(
            [('ovs', [2])])
        assert response is not None
        del_test_yaml = {
            'dps': {
                'ovs': {
                    'dp_id': 1,
                    'hardware': 'Open vSwitch',
                    'interfaces': {
                        1: {'native_vlan': 100, 'acls_in': []},
                        3: {'output_only': True, 'mirror': [1]}}}},
            'acls': {
                'test': [{'rule': {'actions': {'allow': 0}}}]}}
        assert del_test_yaml == self.client.get_config_file(config_filename=self.default_config)

    def test_set_interfaces(self):
        response = self.client.set_dp_interfaces(
            [('ovs', {
                # 2 is replaced.
                2: '{output_only: true}',
                # 4 is new.
                4: '{output_only: true}'})])
        assert response is not None
        set_test_yaml = {
            'dps': {
                'ovs': {
                    'dp_id': 1,
                    'hardware': 'Open vSwitch',
                    'interfaces': {
                        1: {'native_vlan': 100, 'acls_in': []},
                        2: {'output_only': True},
                        3: {'output_only': True, 'mirror': [1]},
                        4: {'output_only': True}}}},
            'acls': {
                'test': [{'rule': {'actions': {'allow': 0}}}]}}
        assert set_test_yaml == self.client.get_config_file(config_filename=self.default_config)

    def test_dpinfo(self):
        # All DP info returned.
        response = self.client.get_dp_info()
        assert len(response.dps) == 1
        dp = response.dps[0]
        assert dp.name == 'ovs'
        assert len(dp.interfaces) == 3

        # Only one DP info returned.
        response = self.client.get_dp_info(dp_name='ovs')
        assert len(response.dps) == 1
        dp = response.dps[0]
        assert dp.name == 'ovs'
        assert len(dp.interfaces) == 3

        # Empty list when no such DP
        response = self.client.get_dp_info(dp_name='nosuchdp')
        assert len(response.dps) == 0

    def test_get(self):
        # Get of non-existent file.
        response = self.client.get_config_file(config_filename='nosuchfile.yaml')
        assert response is None
        # Get existing file
        response = self.client.get_config_file(config_filename=self.default_config)
        assert response == yaml.safe_load(self.default_test_yaml_str)

    def test_remove(self):
        # Remove item from list.
        response = self.client.del_config_from_file(
            ['dps', 'ovs', 'interfaces', 3, 'mirror', 1],
            config_filename=self.default_config)
        assert response is not None
        del_test_yaml = {
            'dps': {
                'ovs': {
                    'dp_id': 1,
                    'hardware': 'Open vSwitch',
                    'interfaces': {
                        1: {'native_vlan': 100, 'acls_in': []},
                        2: {'native_vlan': 100},
                        3: {'output_only': True, 'mirror': []}}}},
            'acls': {
                'test': [{'rule': {'actions': {'allow': 0}}}]}}
        assert del_test_yaml == self.client.get_config_file(config_filename=self.default_config)
        # Remove entire key (mirror)
        response = self.client.del_config_from_file(
            ['dps', 'ovs', 'interfaces', 3, 'mirror'],
            config_filename=self.default_config)
        assert response is not None
        del_test_yaml = {
            'dps': {
                'ovs': {
                    'dp_id': 1,
                    'hardware': 'Open vSwitch',
                    'interfaces': {
                        1: {'native_vlan': 100, 'acls_in': []},
                        2: {'native_vlan': 100},
                        3: {'output_only': True}}}},
            'acls': {
                'test': [{'rule': {'actions': {'allow': 0}}}]}}
        assert del_test_yaml == self.client.get_config_file(config_filename=self.default_config)

    def test_set(self):
        # Replace existing file with new content
        response = self.client.set_config_file(
            self.default_test_yaml_str, config_filename=self.default_config, merge=False)
        assert response is not None
        assert self.default_test_yaml == self.client.get_config_file(self.default_config)
        # Replace existing file with broken content
        response = self.client.set_config_file(
            '{dps: {ovs: {dp_id: NO, hardware: xyz vSwitch, interfaces: {1: {blah: 100}}}}}',
            config_filename=self.default_config, merge=False)
        assert response is None
        # File didn't change.
        assert self.default_test_yaml == self.client.get_config_file(self.default_config)

        # Merge new content into existing file
        response = self.client.set_config_file(
            self.default_test_yaml_str, config_filename=self.default_config, merge=True)
        assert response is not None
        assert self.default_test_yaml == self.client.get_config_file(config_filename=self.default_config)
        new_test_yaml = yaml.safe_load('{dps: {ovs: {interfaces: {3: {description: test}}}}}')
        response = self.client.set_config_file(
            new_test_yaml, config_filename=self.default_config, merge=True)
        assert response is not None
        new_test_yaml = {
            'dps': {
                'ovs': {
                    'dp_id': 1,
                    'hardware': 'Open vSwitch',
                    'interfaces': {
                        1: {'native_vlan': 100, 'acls_in': []},
                        2: {'native_vlan': 100},
                        3: {'output_only': True, 'description': 'test', 'mirror': [1]}}}},
            'acls': {
                'test': [{'rule': {'actions': {'allow': 0}}}]}}
        assert new_test_yaml == self.client.get_config_file(config_filename=self.default_config)

        # Test replace operation.
        new_test_yaml = yaml.safe_load(
            '{dps: {ovs: {interfaces: {3: {description: replaced, output_only: true}}}}}')
        del_config_yaml_keys = '[dps, ovs, interfaces, 3]'
        response = self.client.set_config_file(
            new_test_yaml, config_filename=self.default_config, merge=True,
            del_config_yaml_keys=del_config_yaml_keys)
        assert response is not None
        assert (new_test_yaml['dps']['ovs']['interfaces'][3] ==
                self.client.get_config_file(
                    config_filename=self.default_config)['dps']['ovs']['interfaces'][3])

    def test_mirror(self):
        # Add and remove port mirroring.
        mirror_test_yaml_str = """
        {dps: {ovs: {
            dp_id: 1,
            hardware: Open vSwitch,
            interfaces: {
                1: {native_vlan: 100},
                2: {native_vlan: 100},
                3: {output_only: true, mirror: []}}}}}
        """
        mirror_test_yaml = yaml.safe_load(mirror_test_yaml_str)
        response = self.client.set_config_file(
            yaml.safe_load(mirror_test_yaml_str),
            config_filename=self.default_config, merge=False)
        assert response is not None
        response = self.client.add_port_mirror('ovs', 2, 3)
        assert response is not None
        assert mirror_test_yaml != self.client.get_config_file(
            config_filename=self.default_config)
        response = self.client.remove_port_mirror('ovs', 2, 3)
        assert response is not None
        assert mirror_test_yaml == self.client.get_config_file(
            config_filename=self.default_config)
        response = self.client.add_port_mirror('ovs', 2, 3)
        assert response is not None
        response = self.client.clear_port_mirror('ovs', 3)
        assert response is not None
        assert mirror_test_yaml == self.client.get_config_file(
            config_filename=self.default_config)

    def test_remote_mirror_port(self):
        stack_dps_yaml = {
            'dps': {
                'ovs1': {
                    'dp_id': 1,
                    'hardware': 'Open vSwitch',
                    'stack': {'priority': 1},
                    'interfaces': {
                        1: {'native_vlan': 100},
                        2: {'stack': {'dp': 'ovs2', 'port': 2}}}},
                'ovs2': {
                    'dp_id': 2,
                    'hardware': 'Open vSwitch',
                    'interfaces': {
                        1: {'native_vlan': 100},
                        2: {'stack': {'dp': 'ovs1', 'port': 2}}}}}}
        assert self.client.set_config_file(
            yaml.dump(stack_dps_yaml), config_filename=self.default_config, merge=False)
        response = self.client.set_remote_mirror_port('ovs2', 3, 999, 'ovs1', 1)
        assert response is not None
        response = self.client.get_config_file(config_filename=self.default_config)
        assert (response['dps']['ovs2']['interfaces'][3] == {
            'acls_in': ['remote-mirror-999-ovs1-1'], 'coprocessor': {'strategy': 'vlan_vid'}, 'description': 'loopback'})

    def test_acls(self):
        # Add and remove port ACLs
        response = self.client.add_port_acl('ovs', 1, 'test')
        assert response is not None
        assert self.default_test_yaml != self.client.get_config_file(
            config_filename=self.default_config)
        response = self.client.set_port_acls('ovs', 1, 'test')
        assert response is not None
        assert self.default_test_yaml != self.client.get_config_file(
            config_filename=self.default_config)
        response = self.client.remove_port_acl('ovs', 1, 'test')
        assert response is not None
        assert self.default_test_yaml == self.client.get_config_file(
            config_filename=self.default_config)
        response = self.client.remove_port_acl('ovs', 1)
        assert response is not None
        assert self.default_test_yaml == self.client.get_config_file(
            config_filename=self.default_config)
