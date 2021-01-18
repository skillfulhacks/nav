#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

NAME = "xv"
URL = "https://github.com/skillfulhacks/xv"
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name=NAME,
    version='0.0.1a1',
    description='none',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['code'],
    author='NAV',
    author_email='skillfulhacks@gmail.com',
    url=URL
)
