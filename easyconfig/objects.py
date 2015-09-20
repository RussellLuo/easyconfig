#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from .utils import import_string


def str_object(obj_name):
    """Get a configuration object from a string."""
    return import_string(obj_name)


def envvar_object(var_name, silent=False):
    """Get a configuration object from an environment variable."""
    obj_name = os.environ.get(var_name)
    if not obj_name:
        if not silent:
            raise RuntimeError(
                'The environment variable %r is not set '
                'and as such configuration could not be '
                'loaded. Set this variable and make it '
                'point to a configuration file' % var_name
            )
        else:
            return None
    return str_object(obj_name)
