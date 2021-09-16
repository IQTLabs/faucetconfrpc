#!/usr/bin/python3

"""Manage FAUCET config files via RPC (client)."""

import argparse
import inspect
from faucetconfrpc.faucetconfrpc_client_lib import FaucetConfRpcClient
from faucetconfrpc.faucetconfrpc_server import yaml_load, yaml_dump


class ClientError(Exception):
    """Exceptions for client."""


def get_attributes(cls):
    """Get available RPCs via attrs"""
    boring = dir(type('dummy', (object,), {}))
    return [item for item in inspect.getmembers(cls) if item[0] not in boring]


def yaml_sanity():
    """Ensure YAML libraries present."""
    test_dict = {'test': 'value'}
    test_yaml = yaml_dump(test_dict)
    assert yaml_load(test_yaml) == test_dict


def main():
    """Instantiate client and call it."""
    yaml_sanity()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--key', help='client private key', action='store',
        default='client.key')
    parser.add_argument(
        '--cert', help='client public cert', action='store',
        default='client.crt')
    parser.add_argument(
        '--cacert', help='CA public cert', action='store',
        default='ca.crt')
    parser.add_argument(
        '--port', help='port of rpc server', action='store',
        default=59999, type=int)
    parser.add_argument(
        '--host', help='host address of rpc server',
        default='localhost')
    parser.add_argument(
        'commands', type=str, nargs='+',
        help='rpc commands')
    args = parser.parse_args()
    server_addr = f'{args.host}:{args.port}'
    client = FaucetConfRpcClient(args.key, args.cert, args.cacert, server_addr)

    if args.commands[0] == 'list_rpcs':
        attributes = get_attributes(client)
        for attribute in attributes:
            if not attribute[0].startswith('_'):
                print(attribute[0])
        return

    command = getattr(client, args.commands[0], None)
    if not command:
        raise ClientError(f'no such rpc: {args.commands[0]}')
    command_args = {}
    for args in args.commands[1:]:
        arg, val = args.split('=')
        if val.lower() == 'true':
            val = True
        elif val.lower() == 'false':
            val = False
        command_args[arg] = val
    print(command(**command_args))


if __name__ == '__main__':
    main()
