#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from easyconfig import Config, json_mapping, yaml_mapping

cur_path = os.path.abspath(os.path.dirname(__file__))


class MappingsTest(unittest.TestCase):

    def test_json_mapping(self):
        config = Config()
        json_filename = os.path.join(cur_path, 'configs/default_config.json')
        config.from_mapping(json_mapping(json_filename))
        self.assertEqual(config.DEBUG, True)
        self.assertEqual(config.PORT, 5000)
        self.assertEqual(config.SECRET_KEY, '123***456')

    def test_yaml_mapping(self):
        config = Config()
        yaml_filename = os.path.join(cur_path, 'configs/default_config.yml')
        config.from_mapping(yaml_mapping(yaml_filename))
        self.assertEqual(config.DEBUG, True)
        self.assertEqual(config.PORT, 5000)
        self.assertEqual(config.SECRET_KEY, '123***456')


if __name__ == '__main__':
    unittest.main()
