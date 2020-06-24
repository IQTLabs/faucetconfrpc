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
from faucetconfrpc.faucetconfrpc_client_lib import FaucetConfRpcClient


def test_faucetconfrpc():  # pylint: disable=too-many-locals,disable=too-many-statements
    """Test faucetconfrpc RPCs."""

    def wait_for_port(host, port, timeout=10):
        for _ in range(timeout):
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                if sock.connect_ex((host, port)) == 0:
                    return  # pytype: disable=not-callable
            time.sleep(1)
        assert False

    host = 'localhost'
    port = 59999
    certstrap = shutil.which('certstrap')
    assert certstrap

    with tempfile.TemporaryDirectory() as tmpdir:
        for cmd in (
                ['init', '--common-name', 'ca', '--passphrase', ''],
                ['request-cert', '--common-name', 'client', '--passphrase', ''],
                ['sign', 'client', '--CA', 'ca'],
                ['request-cert', '--common-name', host, '--passphrase', ''],
                ['sign', host, '--CA', 'ca']):
            subprocess.check_call([certstrap, '--depot-path', tmpdir] + cmd)
        client_key = os.path.join(tmpdir, 'client.key')
        client_cert = os.path.join(tmpdir, 'client.crt')
        server_key = os.path.join(tmpdir, '%s.key' % host)
        server_cert = os.path.join(tmpdir, '%s.crt' % host)
        ca_cert = os.path.join(tmpdir, 'ca.crt')

        test_yaml = yaml.safe_load(
            '{dps: {ovs: {dp_id: 1, hardware: Open vSwitch, interfaces: '
            '{1: {native_vlan: 100, acls_in: []}, 2: {native_vlan: 100}, '
            '3: {output_only: true, mirror: [1]}}}},'
            'acls: {test: [{rule: {actions: {allow: 0}}}]}}')
        test_yaml_str = yaml.dump(test_yaml)
        default_config = 'test.yaml'

        with open(os.path.join(tmpdir, default_config), 'w') as test_yaml_file:
            test_yaml_file.write(test_yaml_str)  # pytype: disable=wrong-arg-types
        server = subprocess.Popen(
            ['timeout',
             '10s',
             './faucetconfrpc/faucetconfrpc_server.py',
             '--config_dir=%s' % tmpdir,
             '--default_config=%s' % default_config,
             '--port=%u' % port,
             '--host=%s' % host,
             '--key=%s' % server_key,
             '--cert=%s' % server_cert,
             '--cacert=%s' % ca_cert,
             ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        wait_for_port(host, port)
        server_addr = '%s:%u' % (host, port)
        client = FaucetConfRpcClient(client_key, client_cert, ca_cert, server_addr)

        # Get of non-existent file.
        response = client.get_config_file(config_filename='nosuchfile.yaml')
        assert response is None
        # Get existing file
        response = client.get_config_file(config_filename=default_config)
        assert response == yaml.safe_load(test_yaml_str)

        # Remove item from list.
        response = client.del_config_from_file(
            ['dps', 'ovs', 'interfaces', 3, 'mirror', 1], config_filename=default_config)
        assert response is not None
        del_test_yaml = yaml.safe_load(
            '{dps: {ovs: {dp_id: 1, hardware: Open vSwitch, interfaces: '
            '{1: {native_vlan: 100, acls_in: []}, 2: {native_vlan: 100}, '
            '3: {output_only: true, mirror: []}}}},'
            'acls: {test: [{rule: {actions: {allow: 0}}}]}}')
        assert del_test_yaml == client.get_config_file(config_filename=default_config)
        # Remove entire key
        response = client.del_config_from_file(
            ['dps', 'ovs', 'interfaces', 3, 'mirror'], config_filename=default_config)
        assert response is not None
        del_test_yaml = yaml.safe_load(
            '{dps: {ovs: {dp_id: 1, hardware: Open vSwitch, interfaces: '
            '{1: {native_vlan: 100, acls_in: []}, 2: {native_vlan: 100}, 3: {output_only: true}}}},'
            'acls: {test: [{rule: {actions: {allow: 0}}}]}}')
        assert del_test_yaml == client.get_config_file(config_filename=default_config)

        # Replace existing file with new content
        response = client.set_config_file(
            test_yaml_str, config_filename=default_config, merge=False)
        assert response is not None
        assert test_yaml == client.get_config_file(default_config)

        # Replace existing file with broken content
        response = client.set_config_file(
            '{dps: {ovs: {dp_id: NO, hardware: xyz vSwitch, interfaces: {1: {blah: 100}}}}}',
            config_filename=default_config, merge=False)
        assert response is None
        # File didn't change.
        assert test_yaml == client.get_config_file(default_config)

        # Merge new content into existing file
        response = client.set_config_file(
            test_yaml_str, config_filename=default_config, merge=True)
        assert response is not None
        assert test_yaml == client.get_config_file(config_filename=default_config)
        new_test_yaml = yaml.safe_load('{dps: {ovs: {interfaces: {3: {description: test}}}}}')
        response = client.set_config_file(
            new_test_yaml, config_filename=default_config, merge=True)
        assert response is not None
        new_test_yaml = yaml.safe_load(
            '{dps: {ovs: {dp_id: 1, hardware: Open vSwitch, interfaces: '
            '{1: {native_vlan: 100, acls_in: []}, 2: {native_vlan: 100}, '
            '3: {output_only: true, mirror: [1], description: test}}}},'
            'acls: {test: [{rule: {actions: {allow: 0}}}]}}')
        assert new_test_yaml == client.get_config_file(config_filename=default_config)

        # Add and remove port mirroring.
        response = client.add_port_mirror('ovs', 2, 3)
        assert response is not None
        assert new_test_yaml != client.get_config_file(config_filename=default_config)
        response = client.remove_port_mirror('ovs', 2, 3)
        assert response is not None
        assert new_test_yaml == client.get_config_file(config_filename=default_config)

        # Add and remove port ACLs
        response = client.add_port_acl('ovs', 1, 'test')
        assert response is not None
        assert new_test_yaml != client.get_config_file(config_filename=default_config)
        response = client.remove_port_acl('ovs', 1, 'test')
        assert response is not None
        assert new_test_yaml == client.get_config_file(config_filename=default_config)

        server.terminate()
        server.wait()
