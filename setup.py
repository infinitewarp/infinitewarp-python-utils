#!/usr/bin/env python
"""Setup module for infinitewarp_utils."""
from datetime import datetime

from setuptools import find_packages, setup

build_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')

setup(
    name='infinitewarp_utils',
    version='1.0.{}'.format(build_time),
    description='infinitewarp_utils is a collection of Python helper modules '
                'for infinitewarp.',
    url='https://github.com/infinitewarp/infinitewarp-python-utils',
    author='Brad Smith',
    author_email='bradster@infinitewarp.com',
    license='MIT',
    packages=find_packages(exclude=['docs', 'tests', 'tests.*']),
    install_requires=[],
    dependency_links=[],
    zip_safe=True,
)
