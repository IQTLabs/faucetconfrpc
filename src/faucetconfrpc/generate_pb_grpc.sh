#!/bin/bash
set -e

# TODO: remove old ../../faucetconfrpc protobufs in favor of ../../faucetconfserv path once dovesnap updated.
protoc protos/faucetconfrpc/faucetconfrpc.proto --go-grpc_out=. --go_out=.
python3 -m grpc_tools.protoc -Iprotos protos/faucetconfrpc/faucetconfrpc.proto --python_out=.. --grpc_python_out=..
