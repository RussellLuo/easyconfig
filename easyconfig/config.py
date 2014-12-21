#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .dictproxy import DictProxy


class Config(DictProxy, dict):
    """The core configuration class.

    Example usage:

        # load configurations from a dict (as default)
        config = Config({'DEBUG': True})
        assert config['DEBUG'] == True
        assert config.DEBUG == True

        # load/update configurations from a dict
        config.from_mapping({'PORT': 5000})

        # load/update configurations from an object
        from yourapplication import default_config
        config.from_object(default_config)

        # load configurations from environment variables
        import os
        config = Config(datasrc=os.environ)
        assert 'DEBUG' not in config
        os.environ.setdefault('SECRET_KEY', '123***456')
        assert config.SECRET_KEY == '123***456'

    Note: only uppercase keys will be added as config.
    """

    def __init__(self, defaults=None, datasrc=None):
        # `self._datasrc` must be set before `DictProxy.__init__` is called
        # reason:
        #     1. `DictProxy.__init__` will set `self._inner_dict`
        #     2. then, every set behaviour will trigger `self.__contains__`
        #     3. then, `self._datasrc` will be accessed
        #     4. if `self._datasrc` is not set yet, then go to `self.__getattr__`
        #     5. then, `self.__contains__` is triggered again
        #     6. an infinite recursive loop occurs...
        self._datasrc = datasrc or {}
        DictProxy.__init__(self, self)

        self.from_mapping(defaults or {})

    def __contains__(self, item):
        """Override to take `self._datasrc` into account."""
        exists = dict.__contains__(self, item)
        if not exists:
            exists = item in self._datasrc
        return exists

    def __missing__(self, key):
        """Override to try to get `key` from `self._datasrc`."""
        return self._datasrc[key]

    def from_mapping(self, mapping):
        for key, value in mapping.iteritems():
            if key.isupper():
                self[key] = value

    def from_object(self, obj):
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)
