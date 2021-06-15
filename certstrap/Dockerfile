FROM golang:1.16-alpine as build

ENV GO111MODULE="on"
RUN go get github.com/square/certstrap

WORKDIR /
COPY gen_faucetconfrpc_keys.sh gen_faucetconfrpc_keys.sh

FROM alpine:3.14

COPY --from=build /gen_faucetconfrpc_keys.sh /gen_faucetconfrpc_keys.sh
COPY --from=build /go/bin/certstrap /usr/bin/certstrap

WORKDIR /

ENTRYPOINT ["sh", "gen_faucetconfrpc_keys.sh"]
