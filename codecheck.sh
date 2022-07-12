#!/bin/sh

set -e

# https://github.com/google/pytype/issues/764 (disable pyi-error for protobuf)
PYTHONPATH=$pwd/src/faucetconfrpc:$PYTHONPATH pytype --disable=pyi-error --exclude=src/faucetconfrpc/faucetconfrpc_pb2_grpc.py --exclude=src/faucetconfrpc/faucetconfrpc_pb2.py src/faucetconfrpc/*py
pylint --ignore=faucetconfrpc_pb2_grpc.py,faucetconfrpc_pb2.py src/faucetconfrpc/*py
