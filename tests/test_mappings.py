#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from easyconfig import json_mapping, yaml_mapping

cur_path = os.path.abspath(os.path.dirname(__file__))
json_filename = os.path.join(cur_path, 'configs/default_config.json')
yaml_filename = os.path.join(cur_path, 'configs/default_config.yml')


class MappingsTest(unittest.TestCase):

    def test_valid_json_mapping(self):
        mapping = json_mapping(json_filename)
        self.assertEqual(mapping['DEBUG'], True)
        self.assertEqual(mapping['PORT'], 5000)
        self.assertEqual(mapping['SECRET_KEY'], '123***456')

    def test_empty_json_mapping(self):
        self.assertRaisesRegexp(
            IOError,
            "\[Errno 2\] Unable to load configuration file "
            "\(No such file or directory\): ''",
            json_mapping, ''
        )

    def test_empty_json_mapping_in_silent(self):
        mapping = json_mapping('', silent=True)
        self.assertFalse(mapping)

    def test_valid_json_mapping_from_envvar(self):
        os.environ['EASY_CONFIG'] = json_filename
        mapping = json_mapping('EASY_CONFIG', is_envvar=True)
        self.assertEqual(mapping['DEBUG'], True)
        self.assertEqual(mapping['PORT'], 5000)
        self.assertEqual(mapping['SECRET_KEY'], '123***456')

    def test_nonexistent_json_object_from_envvar(self):
        os.environ.pop('EASY_CONFIG', None)
        self.assertRaisesRegexp(
            RuntimeError,
            "The environment variable 'EASY_CONFIG' is not set "
            "and as such configuration could not be "
            "loaded. Set this variable and make it "
            "point to a configuration file",
            json_mapping, 'EASY_CONFIG', False, True
        )

    def test_nonexistent_json_object_from_envvar_in_silent(self):
        os.environ.pop('EASY_CONFIG', None)
        mapping = json_mapping('EASY_CONFIG', silent=True, is_envvar=True)
        self.assertFalse(mapping)

    def test_empty_json_mapping_from_envvar(self):
        os.environ['EASY_CONFIG'] = ''
        self.assertRaisesRegexp(
            IOError,
            "\[Errno 2\] Unable to load configuration file "
            "\(No such file or directory\): ''",
            json_mapping, 'EASY_CONFIG', False, True
        )

    def test_empty_json_mapping_from_envvar_in_silent(self):
        os.environ['EASY_CONFIG'] = ''
        mapping = json_mapping('EASY_CONFIG', silent=True, is_envvar=True)
        self.assertFalse(mapping)

    def test_valid_yaml_mapping(self):
        mapping = yaml_mapping(yaml_filename)
        self.assertEqual(mapping['DEBUG'], True)
        self.assertEqual(mapping['PORT'], 5000)
        self.assertEqual(mapping['SECRET_KEY'], '123***456')

    def test_empty_yaml_mapping(self):
        self.assertRaisesRegexp(
            IOError,
            "\[Errno 2\] Unable to load configuration file "
            "\(No such file or directory\): ''",
            json_mapping, ''
        )

    def test_empty_yaml_mapping_in_silent(self):
        mapping = json_mapping('', silent=True)
        self.assertFalse(mapping)

    def test_valid_yaml_mapping_from_envvar(self):
        os.environ['EASY_CONFIG'] = yaml_filename
        mapping = yaml_mapping('EASY_CONFIG', is_envvar=True)
        self.assertEqual(mapping['DEBUG'], True)
        self.assertEqual(mapping['PORT'], 5000)
        self.assertEqual(mapping['SECRET_KEY'], '123***456')

    def test_nonexistent_yaml_object_from_envvar(self):
        os.environ.pop('EASY_CONFIG', None)
        self.assertRaisesRegexp(
            RuntimeError,
            "The environment variable 'EASY_CONFIG' is not set "
            "and as such configuration could not be "
            "loaded. Set this variable and make it "
            "point to a configuration file",
            yaml_mapping, 'EASY_CONFIG', False, True
        )

    def test_nonexistent_yaml_object_from_envvar_in_silent(self):
        os.environ.pop('EASY_CONFIG', None)
        mapping = yaml_mapping('EASY_CONFIG', silent=True, is_envvar=True)
        self.assertFalse(mapping)

    def test_empty_yaml_mapping_from_envvar(self):
        os.environ['EASY_CONFIG'] = ''
        self.assertRaisesRegexp(
            IOError,
            "\[Errno 2\] Unable to load configuration file "
            "\(No such file or directory\): ''",
            yaml_mapping, 'EASY_CONFIG', False, True
        )

    def test_empty_yaml_mapping_from_envvar_in_silent(self):
        os.environ['EASY_CONFIG'] = ''
        mapping = yaml_mapping('EASY_CONFIG', silent=True, is_envvar=True)
        self.assertFalse(mapping)


if __name__ == '__main__':
    unittest.main()
