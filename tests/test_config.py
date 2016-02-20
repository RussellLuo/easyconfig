# -*- coding: utf-8 -*-

import os

import pytest

from easyconfig import Config


class AppConfig(object):

    SECRET_KEY = '123***456'


class TestConfig(object):

    def test_cant_set_lowercase_item(self):
        config = Config()
        with pytest.raises(ValueError):
            config['debug'] = True

    def test_can_set_uppercase_item(self):
        config = Config()
        config['DEBUG'] = True
        assert config['DEBUG']

    def test_can_set_lowercase_attribute_as_attribute(self):
        config = Config()
        config.debug = True
        # seems like an attribute
        assert hasattr(config, 'debug')
        # actually is an attribute
        assert 'debug' in config.__dict__

    def test_cant_set_uppercase_attribute_as_attribute(self):
        config = Config()
        config.DEBUG = True
        # seems like an attribute
        assert hasattr(config, 'DEBUG')
        # actually is not an attribute
        assert 'DEBUG' not in config.__dict__

    def test_uppercase_items_are_also_attributes(self):
        config = Config()
        config.DEBUG = True
        assert config['DEBUG']

        config['PORT'] = 5000
        assert config.PORT == 5000

    def test_cant_load_lowercase_keys(self):
        config = Config({'debug': True})
        assert 'debug' not in config
        assert not hasattr(config, 'debug')

    def test_can_load_defaults_from_mapping(self):
        config = Config({'DEBUG': True})
        assert config.DEBUG

    def test_can_load_defaults_from_object(self):
        config = Config(AppConfig)
        assert config.SECRET_KEY == '123***456'

    def test_load_from_mapping(self):
        config = Config()
        config.from_mapping({'PORT': 5000})
        assert config.PORT == 5000

    def test_load_from_object(self):
        config = Config()
        config.from_object(AppConfig)
        assert config.SECRET_KEY == '123***456'

    def test_load_from_none_object(self):
        config = Config()
        config.from_object(None)
        uppercase_attrs = [attr for attr in dir(config) if attr.isupper()]
        assert not uppercase_attrs

    def test_load_from_envvar(self):
        config = Config(datasrc=os.environ)
        assert 'SECRET_KEY' not in config

        os.environ.setdefault('SECRET_KEY', '123***456')
        assert config.SECRET_KEY == '123***456'

        os.environ['SECRET_KEY'] = 'xxx***yyy'
        assert config.SECRET_KEY == 'xxx***yyy'

    def test_load_from_empty_envvar(self):
        config = Config(datasrc=os.environ)
        assert not hasattr(config, 'NULL_KEY')

    def test_load_from_either_mapping_or_object(self):
        config1 = Config()
        config1.load({'DEBUG': True})
        assert config1.DEBUG

        config2 = Config()
        config2.load(AppConfig)
        assert config2.SECRET_KEY == '123***456'
