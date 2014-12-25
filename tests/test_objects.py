#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from easyconfig import Config, str_object, envvar_object


class ObjectsTest(unittest.TestCase):

    def test_valid_str_object(self):
        config = Config()
        config.from_object(str_object('configs.default_config'))
        self.assertEqual(config.DEBUG, True)
        self.assertEqual(config.PORT, 5000)
        self.assertEqual(config.SECRET_KEY, '123***456')

    def test_invalid_str_object(self):
        self.assertRaisesRegexp(ValueError, 'Empty module name',
                                str_object, '')

    def test_valid_envvar_object(self):
        config = Config()
        os.environ.setdefault('EASY_CONFIG', 'configs.default_config')
        config.from_object(envvar_object('EASY_CONFIG'))
        self.assertEqual(config.DEBUG, True)
        self.assertEqual(config.PORT, 5000)
        self.assertEqual(config.SECRET_KEY, '123***456')

    def test_invalid_envvar_object(self):
        self.assertRaisesRegexp(
            RuntimeError,
            "The environment variable 'EMPTY_CONFIG' is not set "
            "and as such configuration could not be "
            "loaded. Set this variable and make it "
            "point to a configuration file",
            envvar_object, 'EMPTY_CONFIG'
        )

    def test_invalid_envvar_object_in_silent(self):
        obj = envvar_object('EMPTY_CONFIG', True)
        self.assertIsNone(obj)


if __name__ == '__main__':
    unittest.main()
