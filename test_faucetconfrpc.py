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
from faucetconfrpc_client_lib import FaucetConfRpcClient


def test_faucetconfrpc():  # pylint: disable=too-many-locals
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

        test_yaml_str = '{key1: [1, 2, 3], key2: [4, 5, 6]}'
        with open(os.path.join(tmpdir, 'test.yaml'), 'w') as test_yaml_file:
            test_yaml_file.write(test_yaml_str)  # pytype: disable=wrong-arg-types
        server = subprocess.Popen(
            ['timeout',
             '10s',
             './faucetconfrpc_server.py',
             '--config_dir=%s' % tmpdir,
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
        response = client.get_config_file('nosuchfile.yaml')
        assert response is None
        # Get existing file
        response = client.get_config_file('test.yaml')
        assert response == yaml.safe_load(test_yaml_str)

        # Remove item from list.
        response = client.del_config_from_file('test.yaml', ['key2', 5])
        assert response is not None
        del_test_yaml = yaml.safe_load('{key1: [1, 2, 3], key2: [4, 6]}')
        assert del_test_yaml == client.get_config_file('test.yaml')
        # Remove entire key
        response = client.del_config_from_file('test.yaml', ['key2'])
        assert response is not None
        del_test_yaml = yaml.safe_load('{key1: [1, 2, 3]}')
        assert del_test_yaml == client.get_config_file('test.yaml')

        # Replace existing file with new content
        new_test_yaml = yaml.safe_load('{key1: [a, b, c], key2: [4, 5, 6]}')
        response = client.set_config_file('test.yaml', new_test_yaml, merge=False)
        assert response is not None
        assert new_test_yaml == client.get_config_file('test.yaml')

        # Merge new content into existing file
        response = client.set_config_file('test.yaml', new_test_yaml, merge=True)
        assert response is not None
        assert new_test_yaml == client.get_config_file('test.yaml')
        new_test_yaml = yaml.safe_load('{key2: [4, 5, 6, 7]}')
        response = client.set_config_file('test.yaml', new_test_yaml, merge=True)
        assert response is not None
        new_test_yaml = yaml.safe_load('{key1: [a, b, c], key2: [4, 5, 6, 7]}')
        assert new_test_yaml == client.get_config_file('test.yaml')
        server.terminate()
        server.wait()
