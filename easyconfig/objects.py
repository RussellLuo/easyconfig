#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from werkzeug.utils import import_string


def str_object(obj_name):
    """Get configuration object from string."""
    return import_string(obj_name)


def envvar_object(var_name, silent=False):
    """Configuration object from an environment variable."""
    obj_name = os.environ.get(var_name)
    if not obj_name and not silent:
        raise RuntimeError(
            'The environment variable %r is not set '
            'and as such configuration could not be '
            'loaded.  Set this variable and make it '
            'point to a configuration file' % var_name
        )
    return str_object(obj_name)
