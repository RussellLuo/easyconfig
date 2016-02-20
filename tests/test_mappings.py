# -*- coding: utf-8 -*-

import os

import pytest

from easyconfig import json_mapping, yaml_mapping

cur_path = os.path.abspath(os.path.dirname(__file__))
json_filename = os.path.join(cur_path, 'configs/default_config.json')
yaml_filename = os.path.join(cur_path, 'configs/default_config.yml')


class TestMappings(object):

    def test_valid_json_mapping(self):
        mapping = json_mapping(json_filename)
        assert mapping['DEBUG']
        assert mapping['PORT'] == 5000
        assert mapping['SECRET_KEY'] == '123***456'

    def test_empty_json_mapping(self):
        with pytest.raises(IOError) as exc:
            json_mapping('')
        assert str(exc.value) == (
            "[Errno 2] Unable to load configuration file "
            "(No such file or directory): ''"
        )

    def test_empty_json_mapping_in_silent(self):
        mapping = json_mapping('', silent=True)
        assert not mapping

    def test_valid_json_mapping_from_envvar(self):
        os.environ['EASY_CONFIG'] = json_filename
        mapping = json_mapping('EASY_CONFIG', is_envvar=True)
        assert mapping['DEBUG']
        assert mapping['PORT'] == 5000
        assert mapping['SECRET_KEY'] == '123***456'

    def test_nonexistent_json_object_from_envvar(self):
        os.environ.pop('EASY_CONFIG', None)
        with pytest.raises(RuntimeError) as exc:
            json_mapping('EASY_CONFIG', silent=False, is_envvar=True)
        assert str(exc.value) == (
            "The environment variable 'EASY_CONFIG' is not set "
            "and as such configuration could not be "
            "loaded. Set this variable and make it "
            "point to a configuration file"
        )

    def test_nonexistent_json_object_from_envvar_in_silent(self):
        os.environ.pop('EASY_CONFIG', None)
        mapping = json_mapping('EASY_CONFIG', silent=True, is_envvar=True)
        assert not mapping

    def test_empty_json_mapping_from_envvar(self):
        os.environ['EASY_CONFIG'] = ''
        with pytest.raises(IOError) as exc:
            json_mapping('EASY_CONFIG', silent=False, is_envvar=True)
        assert str(exc.value) == (
            "[Errno 2] Unable to load configuration file "
            "(No such file or directory): ''"
        )

    def test_empty_json_mapping_from_envvar_in_silent(self):
        os.environ['EASY_CONFIG'] = ''
        mapping = json_mapping('EASY_CONFIG', silent=True, is_envvar=True)
        assert not mapping

    def test_valid_yaml_mapping(self):
        mapping = yaml_mapping(yaml_filename)
        assert mapping['DEBUG']
        assert mapping['PORT'] == 5000
        assert mapping['SECRET_KEY'] == '123***456'

    def test_empty_yaml_mapping(self):
        with pytest.raises(IOError) as exc:
            yaml_mapping('')
        assert str(exc.value) == (
            "[Errno 2] Unable to load configuration file "
            "(No such file or directory): ''"
        )

    def test_empty_yaml_mapping_in_silent(self):
        mapping = json_mapping('', silent=True)
        assert not mapping

    def test_valid_yaml_mapping_from_envvar(self):
        os.environ['EASY_CONFIG'] = yaml_filename
        mapping = yaml_mapping('EASY_CONFIG', is_envvar=True)
        assert mapping['DEBUG']
        assert mapping['PORT'] == 5000
        assert mapping['SECRET_KEY'] == '123***456'

    def test_nonexistent_yaml_object_from_envvar(self):
        os.environ.pop('EASY_CONFIG', None)
        with pytest.raises(RuntimeError) as exc:
            yaml_mapping('EASY_CONFIG', silent=False, is_envvar=True)
        assert str(exc.value) == (
            "The environment variable 'EASY_CONFIG' is not set "
            "and as such configuration could not be "
            "loaded. Set this variable and make it "
            "point to a configuration file"
        )

    def test_nonexistent_yaml_object_from_envvar_in_silent(self):
        os.environ.pop('EASY_CONFIG', None)
        mapping = yaml_mapping('EASY_CONFIG', silent=True, is_envvar=True)
        assert not mapping

    def test_empty_yaml_mapping_from_envvar(self):
        os.environ['EASY_CONFIG'] = ''
        with pytest.raises(IOError) as exc:
            yaml_mapping('EASY_CONFIG', silent=False, is_envvar=True)
        assert str(exc.value) == (
            "[Errno 2] Unable to load configuration file "
            "(No such file or directory): ''"
        )

    def test_empty_yaml_mapping_from_envvar_in_silent(self):
        os.environ['EASY_CONFIG'] = ''
        mapping = yaml_mapping('EASY_CONFIG', silent=True, is_envvar=True)
        assert not mapping
