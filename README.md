# faucetconfrpc

An RPC server/client for Faucet YAML config Files


### Example usage

In one terminal, having already created keys for client and server, start the server with an example config file:

```cat<<EOD
$ cat<<EOD>faucet.yaml
 dps:
   ovs:
     dp_id: 0x1
     hardware: Open vSwitch
     interfaces:
       1:
          native_vlan: 100
EOD
$ ./faucetconfrpc_server.py --config_dir=.
```

In another terminal:

```
$ ./faucetconfrpc_client.py get_config_file config_filename='faucet.yaml'
{'dps': {'ovs': {'dp_id': 1, 'hardware': 'Open vSwitch', 'interfaces': {1: {'native_vlan': 100}}}}}
$ ./faucetconfrpc_client.py set_config_file config_filename='faucet.yaml' config_yaml='{dps: {ovs: {interfaces: {1: {native_vlan: 200}}}}}' merge=true

$ ./faucetconfrpc_client.py get_config_file config_filename='faucet.yaml'
{'dps': {'ovs': {'dp_id': 1, 'hardware': 'Open vSwitch', 'interfaces': {1: {'native_vlan': 200}}}}}

$ ./faucetconfrpc_client.py set_config_file config_filename='faucet.yaml' config_yaml='{dps: {ovs: {interfaces: {2: {native_vlan: 100}}}}}' merge=true

$ ./faucetconfrpc_client.py get_config_file config_filename='faucet.yaml'
{'dps': {'ovs': {'dp_id': 1, 'hardware': 'Open vSwitch', 'interfaces': {1: {'native_vlan': 200}, 2: {'native_vlan': 100}}}}}
$ ./faucetconfrpc_client.py del_config_from_file config_filename='faucet.yaml' config_yaml_keys='[dps, ovs, interfaces, 1]'

$ ./faucetconfrpc_client.py get_config_file config_filename='faucet.yaml'
{'dps': {'ovs': {'dp_id': 1, 'hardware': 'Open vSwitch', 'interfaces': {2: {'native_vlan': 100}}}}}
```
