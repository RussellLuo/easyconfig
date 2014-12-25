#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import yaml


def load_from_file(load_func, filename, silent=False):
    """Get a configuration mapping from a file."""
    try:
        with open(filename) as fp:
            obj = load_func(fp)
            if not isinstance(obj, dict):
                raise RuntimeError(
                    'The configuration file %r is invalid' % filename
                )
    except IOError as e:
        if not silent:
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise
        else:
            obj = {}

    return obj


def json_mapping(filename, silent=False):
    """Get a configuration mapping from a JSON file."""
    load_func = lambda fp: json.load(fp)
    return load_from_file(load_func, filename, silent)


def yaml_mapping(filename, silent=False):
    """Get a configuration mapping from a YAML file."""
    load_func = lambda fp: yaml.load(fp)
    return load_from_file(load_func, filename, silent)
