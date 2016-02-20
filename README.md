EasyConfig
==========

A simple library for loading configurations easily in Python, inspired by `flask.config`.


Installation
------------

Install `EasyConfig` with `pip`:

    $ pip install python-easyconfig

Install development version from `GitHub`:

    $ git clone https://github.com/RussellLuo/easyconfig.git
    $ cd easyconfig
    $ python setup.py install


Getting Started
---------------

### 1. load default configurations from a dictionary (or an object)

```python
    # from a dictionary
    from easyconfig import Config
    config = Config({'DEBUG': True})
    assert config.DEBUG == True

    # from an object
    from easyconfig import Config
    from yourapplication import default_config
    config = Config(default_config)
    assert config.DEBUG == True
```

### 2. load/update configurations from a dictionary

```python
    from easyconfig import Config
    config = Config()
    config.load({'PORT': 5000})
```

### 3. load/update configurations from an object

```python
    from easyconfig import Config
    from yourapplication import default_config
    config = Config()
    config.load(default_config)
```

### 4. load configurations from environment variables

```python
    import os
    os.environ.setdefault('SECRET_KEY', '123***456')

    from easyconfig import Config
    config = Config(datasrc=os.environ)
    assert config.SECRET_KEY == '123***456'
```

### 5. load/update configurations from a string pointing to an object

```python
    from easyconfig import Config, str_object
    config = Config()
    config.load(str_object('yourapplication.default_config'))
    assert config.SECRET_KEY == '123***456'
```

### 6. load/update configurations from an environment variable pointing to an object

```python
    import os
    os.environ.setdefault('EASY_CONFIG', 'yourapplication.default_config')

    from easyconfig import Config, str_object
    config = Config()
    config.load(str_object('EASY_CONFIG', is_envvar=True))
    assert config.SECRET_KEY == '123***456'
```

### 7. load/update configurations from a JSON file

```python
    from easyconfig import Config, json_mapping
    config = Config()
    config.load(json_mapping('/data/configs/default_config.json'))
    assert config.SECRET_KEY == '123***456'
```

### 8. load/update configurations from an environment variable pointing to a JSON file

```python
    import os
    os.environ.setdefault('EASY_CONFIG', '/data/configs/default_config.json')

    from easyconfig import Config, json_mapping
    config = Config()
    config.load(json_mapping('EASY_CONFIG', is_envvar=True))
    assert config.SECRET_KEY == '123***456'
```

### 9. load/update configurations from a YAML file

```python
    from easyconfig import Config, yaml_mapping
    config = Config()
    config.load(yaml_mapping('/data/configs/default_config.yml'))
    assert config.SECRET_KEY == '123***456'
```

### 10. load/update configurations from an environment variable pointing to a YAML file

```python
    import os
    os.environ.setdefault('EASY_CONFIG', '/data/configs/default_config.yml')

    from easyconfig import Config, yaml_mapping
    config = Config()
    config.load(yaml_mapping('EASY_CONFIG', is_envvar=True))
    assert config.SECRET_KEY == '123***456'
```
