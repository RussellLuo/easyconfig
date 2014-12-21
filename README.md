EasyConfig
==========

A simple library for loading configurations easily in Python, inspired by `flask.config`.


Getting Started
---------------

### 1. load configurations from a dict (as default)

    from easyconfig import Config
    config = Config({'DEBUG': True})
    assert config['DEBUG'] == True
    assert config.DEBUG == True

### 2. load/update configurations from a dict

    from easyconfig import Config
    config = Config()
    config.from_mapping({'PORT': 5000})

### 3. load/update configurations from an object

    from easyconfig import Config
    from yourapplication import default_config
    config = Config()
    config.from_object(default_config)

### 4. load configurations from environment variables

    import os
    from easyconfig import Config
    config = Config(datasrc=os.environ)
    os.environ.setdefault('SECRET_KEY', '123***456')
    assert config.SECRET_KEY == '123***456'

### 5. load/update configurations from a string pointing to an object

    import os
    from easyconfig import Config, str_object
    config = Config()
    config.from_object(str_object('default_config'))
    assert config.SECRET_KEY == '123***456'

### 6. load/update configurations from an environment variable pointing to an object

    import os
    from easyconfig import Config, envvar_object
    config = Config()
    os.environ.setdefault('EASY_CONFIG', 'default_config')
    config.from_object(envvar_object('EASY_CONFIG'))
    assert config.SECRET_KEY == '123***456'
