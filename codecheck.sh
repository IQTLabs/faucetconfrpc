#!/bin/sh

pytype --exclude=faucetconfrpc/faucetconfrpc_pb2_grpc.py --exclude=faucetconfrpc/faucetconfrpc_pb2.py faucetconfrpc/*py && \
pylint --ignore=faucetconfrpc_pb2_grpc.py,faucetconfrpc_pb2.py faucetconfrpc/*py
