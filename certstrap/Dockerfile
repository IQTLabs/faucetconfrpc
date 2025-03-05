FROM golang:1.24-alpine AS build

ENV GO111MODULE="on"
RUN go install github.com/square/certstrap@latest

WORKDIR /
COPY gen_faucetconfrpc_keys.sh gen_faucetconfrpc_keys.sh

FROM alpine:3.21

COPY --from=build /gen_faucetconfrpc_keys.sh /gen_faucetconfrpc_keys.sh
COPY --from=build /go/bin/certstrap /usr/bin/certstrap

WORKDIR /

ENTRYPOINT ["sh", "gen_faucetconfrpc_keys.sh"]
