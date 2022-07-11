#!/bin/sh

PYTHONPATH=$pwd/src/faucetconfrpc:$PYTHONPATH pytype --exclude=src/faucetconfrpc/faucetconfrpc_pb2_grpc.py --exclude=src/faucetconfrpc/faucetconfrpc_pb2.py src/faucetconfrpc/*py
pylint --ignore=faucetconfrpc_pb2_grpc.py,faucetconfrpc_pb2.py src/faucetconfrpc/*py
