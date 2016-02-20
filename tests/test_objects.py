#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from easyconfig import str_object, envvar_object


class ObjectsTest(unittest.TestCase):

    def test_valid_str_object(self):
        obj = str_object('configs.default_config')
        self.assertEqual(obj.DEBUG, True)
        self.assertEqual(obj.PORT, 5000)
        self.assertEqual(obj.SECRET_KEY, '123***456')

    def test_invalid_str_object(self):
        self.assertRaisesRegexp(ValueError, 'Empty module name',
                                str_object, '')

    def test_invalid_str_object_in_silent(self):
        obj = str_object('', silent=True)
        self.assertIsNone(obj)

    def test_valid_str_object_from_envvar(self):
        os.environ['EASY_CONFIG'] = 'configs.default_config'
        obj = str_object('EASY_CONFIG', is_envvar=True)
        self.assertEqual(obj.DEBUG, True)
        self.assertEqual(obj.PORT, 5000)
        self.assertEqual(obj.SECRET_KEY, '123***456')

    def test_nonexistent_str_object_from_envvar(self):
        os.environ.pop('EASY_CONFIG', None)
        self.assertRaisesRegexp(
            RuntimeError,
            "The environment variable 'EMPTY_CONFIG' is not set "
            "and as such configuration could not be "
            "loaded. Set this variable and make it "
            "point to a configuration file",
            str_object, 'EMPTY_CONFIG', False, True
        )

    def test_nonexistent_str_object_from_envvar_in_silent(self):
        os.environ.pop('EASY_CONFIG', None)
        obj = str_object('EASY_CONFIG', silent=True, is_envvar=True)
        self.assertIsNone(obj)

    def test_empty_str_object_from_envvar(self):
        os.environ['EASY_CONFIG'] = ''
        self.assertRaisesRegexp(ValueError, 'Empty module name',
                                str_object, 'EASY_CONFIG', False, True)

    def test_empty_str_object_from_envvar_in_silent(self):
        os.environ['EASY_CONFIG'] = ''
        obj = str_object('EASY_CONFIG', silent=True, is_envvar=True)
        self.assertIsNone(obj)

    def test_valid_envvar_object(self):
        os.environ['EASY_CONFIG'] = 'configs.default_config'
        obj = envvar_object('EASY_CONFIG')
        self.assertEqual(obj.DEBUG, True)
        self.assertEqual(obj.PORT, 5000)
        self.assertEqual(obj.SECRET_KEY, '123***456')


if __name__ == '__main__':
    unittest.main()
