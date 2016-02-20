# -*- coding: utf-8 -*-

import pytest

from easyconfig.utils import import_string


class TestUtils(object):

    def test_import_a_config_module(self):
        config_module = import_string('configs.default_config')
        assert config_module.__name__ == 'configs.default_config'
        assert config_module.DEBUG is True
        assert config_module.PORT == 5000
        assert config_module.SECRET_KEY == '123***456'

    def test_import_a_nonexistent_config_module(self):
        with pytest.raises(ImportError) as exc:
            import_string('configs.dummy_config_module')
        assert str(exc.value) == (
            'No module named "configs.dummy_config_module", nor does a '
            'module named "configs" define a "dummy_config_module" attribute'
        )

    def test_import_a_config_class(self):
        config_class = import_string('configs.default_config_in_class.Config')
        assert config_class.__name__ == 'Config'
        assert config_class.DEBUG is True
        assert config_class.PORT == 5000
        assert config_class.SECRET_KEY == '123***456'

    def test_import_a_nonexistent_config_class(self):
        with pytest.raises(ImportError) as exc:
            import_string('configs.default_config_in_class.dummy_class')
        assert str(exc.value) == (
            'No module named "configs.default_config_in_class.dummy_class", '
            'nor does a module named "configs.default_config_in_class" '
            'define a "dummy_class" attribute'
        )
