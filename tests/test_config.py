#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from easyconfig import Config


class AppConfig(object):

    SECRET_KEY = '123***456'


class ConfigTest(unittest.TestCase):

    def test_cant_set_lowercase_item(self):
        config = Config()
        with self.assertRaises(ValueError):
            config['debug'] = True

    def test_can_set_uppercase_item(self):
        config = Config()
        config['DEBUG'] = True
        self.assertEqual(config['DEBUG'], True)

    def test_can_set_lowercase_attribute_as_attribute(self):
        config = Config()
        config.debug = True
        # seems like an attribute
        self.assertTrue(hasattr(config, 'debug'))
        # actually is an attribute
        self.assertTrue('debug' in config.__dict__)

    def test_cant_set_uppercase_attribute_as_attribute(self):
        config = Config()
        config.DEBUG = True
        # seems like an attribute
        self.assertTrue(hasattr(config, 'DEBUG'))
        # actually is not an attribute
        self.assertFalse('DEBUG' in config.__dict__)

    def test_uppercase_items_are_also_attributes(self):
        config = Config()
        config.DEBUG = True
        self.assertEqual(config['DEBUG'], True)

        config['PORT'] = 5000
        self.assertEqual(config.PORT, 5000)

    def test_cant_load_lowercase_keys(self):
        config = Config({'debug': True})
        self.assertFalse('debug' in config)
        self.assertFalse(hasattr(config, 'debug'))

    def test_can_load_defaults_from_mapping(self):
        config = Config({'DEBUG': True})
        self.assertEqual(config.DEBUG, True)

    def test_can_load_defaults_from_object(self):
        config = Config(AppConfig)
        self.assertEqual(config.SECRET_KEY, '123***456')

    def test_load_from_mapping(self):
        config = Config()
        config.from_mapping({'PORT': 5000})
        self.assertEqual(config.PORT, 5000)

    def test_load_from_object(self):
        config = Config()
        config.from_object(AppConfig)
        self.assertEqual(config.SECRET_KEY, '123***456')

    def test_load_from_none_object(self):
        config = Config()
        config.from_object(None)
        uppercase_attrs = [attr for attr in dir(config) if attr.isupper()]
        self.assertFalse(uppercase_attrs)

    def test_load_from_envvar(self):
        config = Config(datasrc=os.environ)
        self.assertTrue('SECRET_KEY' not in config)

        os.environ.setdefault('SECRET_KEY', '123***456')
        self.assertEqual(config.SECRET_KEY, '123***456')

        os.environ['SECRET_KEY'] = 'xxx***yyy'
        self.assertEqual(config.SECRET_KEY, 'xxx***yyy')

    def test_load_from_empty_envvar(self):
        config = Config(datasrc=os.environ)
        self.assertFalse(hasattr(config, 'NULL_KEY'))

    def test_load_from_either_mapping_or_object(self):
        config1 = Config()
        config1.load({'DEBUG': True})
        self.assertEqual(config1.DEBUG, True)

        config2 = Config()
        config2.load(AppConfig)
        self.assertEqual(config2.SECRET_KEY, '123***456')


if __name__ == '__main__':
    unittest.main()
