#!/usr/bin/python3
"""Manage FAUCET config files via RPC."""

from concurrent import futures  # pytype: disable=pyi-error

import argparse
import os
import tempfile
import threading
import yaml

import grpc

import faucetconfrpc_pb2
import faucetconfrpc_pb2_grpc


class Server(faucetconfrpc_pb2_grpc.FaucetConfServerServicer):  # pylint: disable=too-few-public-methods
    """Serve config management requests."""

    def __init__(self, config_dir):
        self.config_dir = config_dir
        self.lock = threading.Lock()
        os.chdir(self.config_dir)

    def GetConfigFile(self, request, _context):  # pylint: disable=invalid-name
        """Return existing file contents as YAML string."""
        with self.lock:
            try:
                with open(os.path.basename(request.config_filename)) as config_file:
                    config_yaml = yaml.safe_load(config_file.read())
                    return faucetconfrpc_pb2.GetConfigFileReply(
                        success=True, error_text='', config_yaml=yaml.dump(config_yaml))
            except (FileNotFoundError, PermissionError) as err:
                return faucetconfrpc_pb2.GetConfigFileReply(
                    success=False, error_text=str(err), config_yaml='')

    def SetConfigFile(self, request, _context):  # pylint: disable=invalid-name
        """Overwrite existing config file contents with provided YAML."""
        with self.lock:
            try:
                config_filename = os.path.basename(request.config_filename)
                if not (os.path.exists(config_filename) and os.path.isfile(config_filename)):
                    return faucetconfrpc_pb2.SetConfigFileReply(
                        success=False, error_text='%s is not an existing file' % config_filename)

                new_file = tempfile.NamedTemporaryFile(mode='wt', dir=self.config_dir, delete=False)
                new_file_name = new_file.name
                new_file.write(yaml.dump(yaml.safe_load(request.config_yaml)))
                new_file.close()
                os.rename(new_file_name, os.path.basename(config_filename))
                return faucetconfrpc_pb2.SetConfigFileReply(
                    success=True, error_text='')
            except (FileNotFoundError, PermissionError) as err:
                return faucetconfrpc_pb2.SetConfigFileReply(
                    success=False, error_text=str(err))

def serve():
    """Start server and serve requests."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--config_dir', help='directory to serve config', action='store',
        default='/tmp/')
    parser.add_argument(
        '--port', help='port to serve rpc requests', action='store',
        default=59999, type=int)
    args = parser.parse_args()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    faucetconfrpc_pb2_grpc.add_FaucetConfServerServicer_to_server(
        Server(args.config_dir), server)
    server.add_insecure_port('[::]:%u' % args.port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
