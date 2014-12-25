#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from easyconfig import Config


class ConfigTest(unittest.TestCase):

    def test_cant_load_lowercase(self):
        config = Config({'debug': True})
        self.assertFalse('debug' in config)
        self.assertFalse(hasattr(config, 'debug'))

    def test_can_load_uppercase(self):
        config = Config({'DEBUG': True})
        self.assertEqual(config['DEBUG'], True)
        self.assertEqual(config.DEBUG, True)

    def test_load_from_mapping(self):
        config = Config()
        config.from_mapping({'PORT': 5000})
        self.assertEqual(config.PORT, 5000)

    def test_load_from_object(self):
        class AppConfig(object):
            def __init__(self):
                self.SECRET_KEY = '123***456'
        app_config = AppConfig()

        config = Config()
        config.from_object(app_config)
        self.assertEqual(config.SECRET_KEY, '123***456')

    def test_load_from_none_object(self):
        config = Config()
        config.from_object(None)
        uppercase_attrs = filter(lambda attr: attr.isupper(), dir(config))
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


if __name__ == '__main__':
    unittest.main()
