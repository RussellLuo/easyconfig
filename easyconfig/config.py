#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config(dict):
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
        self._datasrc = datasrc or {}
        self.from_mapping(defaults or {})

    def __getitem__(self, key):
        """Override to take `self._datasrc` into account."""
        if key in self:
            return dict.__getitem__(self, key)
        else:
            return object.__getattribute__(self, '_datasrc')[key]

    def __setitem__(self, key, value):
        """Override to only allow uppercase `key` to be set."""
        if key.isupper():
            dict.__setitem__(self, key, value)
        object.__setattr__(self, key, value)

    # make accessing dict keys like attributes possible
    __getattr__ = __getitem__
    __setattr__ = __setitem__

    def from_mapping(self, mapping):
        for key, value in mapping.iteritems():
            if key.isupper():
                self[key] = value

    def from_object(self, obj):
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)
