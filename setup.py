#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

description = 'A simple library for loading configurations easily in Python, inspired by `flask.config`.'

install_requires = [
    'six',
    'PyYAML',
],

setup(
    name='Python-EasyConfig',
    version='0.1.7',
    author='RussellLuo',
    author_email='luopeng.he@gmail.com',
    maintainer='RussellLuo',
    maintainer_email='luopeng.he@gmail.com',
    keywords='Configuration, Python',
    description=description,
    license='MIT',
    long_description=description,
    packages=find_packages(),
    url='https://github.com/RussellLuo/easyconfig',
    install_requires=install_requires,
)
