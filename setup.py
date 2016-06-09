# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='redmon',
    packages = ['redmon'],
    version='0.1.0',
    description='Monitor a Redis key',
    long_description=readme,
    author='Swaathi Kakarla',
    author_email='swaathi@skcript.com',
    url = 'https://github.com/swaathi/redmon',
    download_url = 'https://github.com/swaathi/redmon/tarball/0.1.0',
    license=license,
    entry_points={
        'console_scripts': [
            'redmon = redmon.cli:main',
        ],
    },
    install_requires=(
    	['redis'], ['click'], ['pytest'], ['termcolor']
    )
)
