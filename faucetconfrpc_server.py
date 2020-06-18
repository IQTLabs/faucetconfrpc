from concurrent import futures
import logging

import grpc

import faucetconfrpc_pb2
import faucetconfrpc_pb2_grpc


class Server(faucetconfrpc_pb2_grpc.FaucetConfServer):

    def Placeholder(self, request, context):
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
