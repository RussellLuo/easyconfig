import sys
from importlib import import_module

from six import reraise


def import_string(import_path):
    """Import a module path and return the module/attribute designated by
    the last name in the path. Raise ImportError if the import failed.
    """
    # The destination object is a module
    try:
        module = import_module(import_path)
    except ImportError:
        if '.' not in import_path:
            raise
    else:
        return module

    # The destination object is an attribute
    module_path, attr_name = import_path.rsplit('.', 1)
    module = import_module(module_path)
    try:
        return getattr(module, attr_name)
    except AttributeError:
        msg = 'Module "%s" does not define a "%s" attribute' % (
            module_path, attr_name
        )
        reraise(ImportError, ImportError(msg), sys.exc_info()[2])
