from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from .settings import URL_ALIAS_MODULES


def get_url_alias_modules(collect=None):
    if collect is None:
        collect = URL_ALIAS_MODULES
    alias_modules = []
    for path in collect:
        i = path.rfind('.')
        module, attr = path[:i], path[i+1:]
        try:
            mod = import_module(module)
        except ImportError, e:
            raise ImproperlyConfigured('Error importing url alias module %s: "%s"' % (module, e))
        try:
            klass = getattr(mod, attr)
        except AttributeError:
            raise ImproperlyConfigured('Module "%s" does not define a "%s" url alias class' % (module, attr))
        alias_modules.append(klass())
    return alias_modules


default_url_alias_modules = get_url_alias_modules()

