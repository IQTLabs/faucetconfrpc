#!/bin/sh

set -e

# https://github.com/google/pytype/issues/764 (disable pyi-error for protobuf)
PYTHONPATH=$pwd/faucetconfrpc:$PYTHONPATH pytype --disable=pyi-error --exclude=faucetconfrpc/faucetconfrpc_pb2_grpc.py --exclude=faucetconfrpc/faucetconfrpc_pb2.py faucetconfrpc/*py
pylint --ignore=faucetconfrpc_pb2_grpc.py,faucetconfrpc_pb2.py faucetconfrpc/*py
