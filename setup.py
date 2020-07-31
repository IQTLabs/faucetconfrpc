"""package setup."""

from setuptools import setup

setup(
    name='faucetconfrpc',
    version=open('VERSION', 'r').read().strip(),
    include_package_data=True,
    install_requires=open('requirements.txt', 'r').read().splitlines(),
    license='Apache License 2.0',
    description='utility to manage FAUCET config files via RPC',
    url='https://github.com/IQTLabs/faucetconfrpc',
    packages=['faucetconfrpc'],
    scripts=['faucetconfrpc/faucetconfrpc_server.py', 'faucetconfrpc/faucetconfrpc_client.py'],
)
