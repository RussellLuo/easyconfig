#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

description = 'A simple library for loading configurations easily in Python, inspired by `flask.config`.'

install_requires = [
    'Werkzeug>=0.7',
],

setup(
    name='EasyConfig',
    version='0.0.1',
    author='RussellLuo',
    author_email='luopeng.he@gmail.com',
    description=description,
    license='MIT',
    long_description=description,
    packages=find_packages(),
    url='https://github.com/RussellLuo/easyconfig',
    install_requires=install_requires,
)
