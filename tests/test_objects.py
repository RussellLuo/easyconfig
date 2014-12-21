#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from easyconfig import Config, str_object, envvar_object


class ObjectsTest(unittest.TestCase):

    def test_str_object(self):
        config = Config()
        config.from_object(str_object('default_config'))
        self.assertEqual(config.DEBUG, True)
        self.assertEqual(config.PORT, 5000)
        self.assertEqual(config.SECRET_KEY, '123***456')

    def test_envvar_object(self):
        config = Config()
        os.environ.setdefault('EASY_CONFIG', 'default_config')
        config.from_object(envvar_object('EASY_CONFIG'))
        self.assertEqual(config.DEBUG, True)
        self.assertEqual(config.PORT, 5000)
        self.assertEqual(config.SECRET_KEY, '123***456')


if __name__ == '__main__':
    unittest.main()
