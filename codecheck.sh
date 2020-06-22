#!/bin/sh

pytype --exclude=faucetconfrpc_pb2_grpc.py --exclude=faucetconfrpc_pb2.py . && \
pylint --ignore=faucetconfrpc_pb2_grpc.py,faucetconfrpc_pb2.py *py
