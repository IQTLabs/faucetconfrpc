#!/bin/sh

set -e

PYTHONPATH=$pwd/src/faucetconfrpc:$PYTHONPATH python3 -m pytype --exclude=src/faucetconfrpc/faucetconfrpc_pb2_grpc.py --exclude=src/faucetconfrpc/faucetconfrpc_pb2.py src/faucetconfrpc/*py
python3 -m pylint --ignore=faucetconfrpc_pb2_grpc.py,faucetconfrpc_pb2.py src/faucetconfrpc/*py
