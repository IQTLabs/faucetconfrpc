# faucetconfrpc

An RPC server/client for Faucet YAML config files.

## Overview

The Faucet SDN controller obtains its configuration from at least one YAML file,
generally /etc/faucet/faucet.yaml (which may include others).  Faucet can be
configured to notice a change in those configuration files itself, or upon
receiving a HUP signal.  An operator, an automated process, or a combination
of both must provide the entire configuration and make it self-consistent.

However, an application relying on Faucet may just want to make simple changes - such
as to mirror a port to another port, or to an apply an ACL - and not have to
understand/parse/be responsible for the entire configuration.  faucetconfrpc
provides such high level RPCs and will probably provide more ongoing.  Applications
may also use faucetconfrpc to manage entire configuration files at once,
so can serve both high level and low level needs.

faucetconfrpc therefore provides a similar role for Faucet, to that provided by
ovsdb-server for OVS (providing RPC access, and some common high and low level
operations at the command line).  Again like ovsdb-server, only one faucetconfrpc
process can manage one set of Faucet configuration files at once.

faucetconfrpc requires mutual client-server certificate based authentication,
using gRPC.  RPC calls are authenticated and all clients operate at the same
level of privilege.  faucetconfrpc can be restarted at any time without
disturbing running Faucets.  faucetconfrpc validates all configuration changes
using Faucet's own configuration parser library before submitting them.

## Example usage

In one terminal, having already created keys for client and server in `/tmp/keydir`, start the server with an example config file:

```cat<<EOD
$ mkdir -p /tmp/conf_dir
$ cat<<EOD>/tmp/conf_dir/faucet.yaml
 dps:
   ovs:
     dp_id: 0x1
     hardware: Open vSwitch
     interfaces:
       1:
          native_vlan: 100
EOD
$ docker build -f Dockerfile.server . -t iqtlabs/faucetconfrpc
$ docker run -v /tmp/keydir:/keydir -v /tmp/conf_dir:/conf_dir -p 59999:59999/tcp iqtlabs/faucetconfrpc:latest --key=/keydir/localhost.key --cert=/keydir/localhost.crt --cacert=/keydir/ca.crt --host=0.0.0.0 --config_dir=/conf_dir
```

In another terminal, having run `pip3 install faucetconfrpc`:

```
$ faucetconfrpc_client.py get_config_file --key=/tmp/keydir/client.key --cert=/tmp/keydir/client.crt --cacert=/tmp/keydir/ca.crt
{'dps': {'ovs': {'dp_id': 1, 'hardware': 'Open vSwitch', 'interfaces': {1: {'native_vlan': 100}}}}}
$ faucetconfrpc_client.py set_config_file config_yaml='{dps: {ovs: {interfaces: {1: {native_vlan: 200}}}}}' merge=true --key=/tmp/keydir/client.key --cert=/tmp/keydir/client.crt --cacert=/tmp/keydir/ca.crt

$ faucetconfrpc_client.py get_config_file --key=/tmp/keydir/client.key --cert=/tmp/keydir/client.crt --cacert=/tmp/keydir/ca.crt
{'dps': {'ovs': {'dp_id': 1, 'hardware': 'Open vSwitch', 'interfaces': {1: {'native_vlan': 200}}}}}

$ faucetconfrpc_client.py set_config_file config_yaml='{dps: {ovs: {interfaces: {2: {native_vlan: 100}}}}}' merge=true --key=/tmp/keydir/client.key --cert=/tmp/keydir/client.crt --cacert=/tmp/keydir/ca.crt

$ faucetconfrpc_client.py get_config_file config_filename='faucet.yaml' --key=/tmp/keydir/client.key --cert=/tmp/keydir/client.crt --cacert=/tmp/keydir/ca.crt
{'dps': {'ovs': {'dp_id': 1, 'hardware': 'Open vSwitch', 'interfaces': {1: {'native_vlan': 200}, 2: {'native_vlan': 100}}}}}
$ faucetconfrpc_client.py del_config_from_file config_filename='faucet.yaml' config_yaml_keys='[dps, ovs, interfaces, 1]' --key=/tmp/keydir/client.key --cert=/tmp/keydir/client.crt --cacert=/tmp/keydir/ca.crt

$ faucetconfrpc_client.py get_config_file config_filename='faucet.yaml' --key=/tmp/keydir/client.key --cert=/tmp/keydir/client.crt --cacert=/tmp/keydir/ca.crt
{'dps': {'ovs': {'dp_id': 1, 'hardware': 'Open vSwitch', 'interfaces': {2: {'native_vlan': 100}}}}}
```
