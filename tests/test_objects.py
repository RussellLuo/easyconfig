# -*- coding: utf-8 -*-

import os

import pytest

from easyconfig import str_object, envvar_object


class TestObjects(object):

    def test_valid_str_object(self):
        obj = str_object('configs.default_config')
        assert obj.DEBUG
        assert obj.PORT == 5000
        assert obj.SECRET_KEY == '123***456'

    def test_invalid_str_object(self):
        with pytest.raises(ValueError) as exc:
            str_object('')
        assert str(exc.value) == 'Empty module name'

    def test_invalid_str_object_in_silent(self):
        obj = str_object('', silent=True)
        assert obj is None

    def test_valid_str_object_from_envvar(self):
        os.environ['EASY_CONFIG'] = 'configs.default_config'
        obj = str_object('EASY_CONFIG', is_envvar=True)
        assert obj.DEBUG
        assert obj.PORT == 5000
        assert obj.SECRET_KEY == '123***456'

    def test_nonexistent_str_object_from_envvar(self):
        os.environ.pop('EASY_CONFIG', None)
        with pytest.raises(RuntimeError) as exc:
            str_object('EASY_CONFIG', silent=False, is_envvar=True)
        assert str(exc.value) == (
            "The environment variable 'EASY_CONFIG' is not set "
            "and as such configuration could not be "
            "loaded. Set this variable and make it "
            "point to a configuration file"
        )

    def test_nonexistent_str_object_from_envvar_in_silent(self):
        os.environ.pop('EASY_CONFIG', None)
        obj = str_object('EASY_CONFIG', silent=True, is_envvar=True)
        assert obj is None

    def test_empty_str_object_from_envvar(self):
        os.environ['EASY_CONFIG'] = ''
        with pytest.raises(ValueError) as exc:
            str_object('EASY_CONFIG', silent=False, is_envvar=True)
        assert str(exc.value) == 'Empty module name'

    def test_empty_str_object_from_envvar_in_silent(self):
        os.environ['EASY_CONFIG'] = ''
        obj = str_object('EASY_CONFIG', silent=True, is_envvar=True)
        assert obj is None

    def test_valid_envvar_object(self):
        os.environ['EASY_CONFIG'] = 'configs.default_config'
        obj = envvar_object('EASY_CONFIG')
        assert obj.DEBUG
        assert obj.PORT == 5000
        assert obj.SECRET_KEY == '123***456'
