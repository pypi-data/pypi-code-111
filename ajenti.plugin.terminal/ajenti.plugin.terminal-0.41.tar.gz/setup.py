#!/usr/bin/env python3
from setuptools import setup, find_packages

import os

__requires = [dep.split('#')[0].strip() for dep in filter(None, open('requirements.txt').read().splitlines())] 

setup(
    name='ajenti.plugin.terminal',
    version='0.41',
    python_requires='>=3',
    install_requires=__requires,
    description='Terminal',
    long_description='A Terminal plugin for Ajenti panel',
    author='Ajenti project',
    author_email='e@ajenti.org',
    url='https://ajenti.org',
    packages=find_packages(),
    include_package_data=True,
)