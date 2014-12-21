#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DictProxy(object):
    """Access (get/set) attributes via an inner dictionary."""

    def __init__(self, inner_dict):
        self._inner_dict = inner_dict

    def __getattr__(self, name):
        _inner_dict = object.__getattribute__(self, '_inner_dict')
        if name in _inner_dict:
            return _inner_dict[name]
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        _inner_dict = getattr(self, '_inner_dict', None)
        if _inner_dict and name in _inner_dict:
            _inner_dict[name] = value
        else:
            object.__setattr__(self, name, value)
