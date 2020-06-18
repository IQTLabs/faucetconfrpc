#!/usr/bin/python3

"""Tests for faucetconfrpc."""

from contextlib import closing
import socket
import subprocess
import tempfile
import time
import os
import yaml

import grpc

import faucetconfrpc_pb2
import faucetconfrpc_pb2_grpc


def test_faucetconfrpc():
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

    with tempfile.TemporaryDirectory() as tmpdir:
        test_yaml_str = 'yamlkey: [1, 2, 3]'
        with open(os.path.join(tmpdir, 'test.yaml'), 'w') as test_yaml_file:
            test_yaml_file.write(test_yaml_str)  # pytype: disable=wrong-arg-types
        server = subprocess.Popen(
            ['./faucetconfrpc_server.py', '--config_dir=%s' % tmpdir,
             '--port=%u' % port], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        wait_for_port(host, port)
        with grpc.insecure_channel('%s:%u' % (host, port)) as channel:
            stub = faucetconfrpc_pb2_grpc.FaucetConfServerStub(channel)
            response = stub.GetConfigFile(faucetconfrpc_pb2.GetConfigFileRequest(
                config_filename='nosuchfile.yaml'))
            assert not response.success
            assert response.error_text == "[Errno 2] No such file or directory: \'nosuchfile.yaml\'"
            response = stub.GetConfigFile(faucetconfrpc_pb2.GetConfigFileRequest(
                config_filename='test.yaml'))
            assert response.success, response.error_text
            assert yaml.safe_load(response.config_yaml) == yaml.safe_load(test_yaml_str)
            new_test_yaml_str = 'yamlkey: [a, b, c]'
            response = stub.SetConfigFile(faucetconfrpc_pb2.SetConfigFileRequest(
                config_filename='test.yaml',
                config_yaml=yaml.dump(yaml.safe_load(new_test_yaml_str))))
            assert response.success, response.error_text
            response = stub.GetConfigFile(faucetconfrpc_pb2.GetConfigFileRequest(
                config_filename='test.yaml'))
            assert response.success
            assert yaml.safe_load(new_test_yaml_str) == yaml.safe_load(response.config_yaml)
        server.terminate()
        server.wait()
