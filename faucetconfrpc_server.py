"""Manage FAUCET config files via RPC."""

from concurrent import futures  # pytype: disable=pyi-error

import logging

import grpc

from protos import faucetconfrpc_pb2
from protos import faucetconfrpc_pb2_grpc


class Server(faucetconfrpc_pb2_grpc.FaucetConfServer):

    def Placeholder(self, request, _context):
        return faucetconfrpc_pb2.PlaceholderReply(message='OK')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    faucetconfrpc_pb2_grpc.add_FaucetConfServerServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:59999')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
