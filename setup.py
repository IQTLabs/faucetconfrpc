"""package setup."""

from setuptools import setup
from urllib.request import urlopen, Request

def parse_requirements(path):
    required = open(path, 'r').read().splitlines()
    parsed_required = []
    for requirement in required:
        if '+' in requirement:
            if '=' in requirement:
                name = requirement.rsplit('=')[-1]
            else:
                name = requirement.rsplit('.', 1)[0].split('/')[-1]
            parsed_required.append(f'{name} @ {requirement}')
        elif requirement.startswith('-r'):
            url = requirement.split()[1]
            req = Request(url)
            data = urlopen(req).read().decode("utf-8")
            deps = data.split('\n')
            for dep in deps:
                if '+' in dep:
                    if '=' in dep:
                        name = dep.rsplit('=')[-1]
                    else:
                        name = dep.rsplit('.', 1)[0].split('/')[-1]
                    parsed_required.append(f'{name} @ {dep}')
                else:
                    parsed_required.append(dep)
        else:
            parsed_required.append(requirement)
    return parsed_required

setup(
    name='faucetconfrpc',
    version=open('VERSION', 'r').read().strip(),
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    license='Apache License 2.0',
    description='utility to manage FAUCET config files via RPC',
    url='https://github.com/IQTLabs/faucetconfrpc',
    packages=['faucetconfrpc'],
    scripts=['faucetconfrpc/faucetconfrpc_server.py', 'faucetconfrpc/faucetconfrpc_client.py'],
)
