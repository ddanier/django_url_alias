from django.core.urlresolvers import get_script_prefix
from django.utils import six
from django.utils.importlib import import_module
from .aliases import default_url_alias_modules


def resolve_rewrite(path, url_alias_modules=None):
    if url_alias_modules is None:
        url_alias_modules = default_url_alias_modules
    for url_alias_module in url_alias_modules:
        new_path = getattr(url_alias_module, 'resolve', lambda path: None)(path)
        if not new_path is None:
            path = new_path
            break  # first module wins
    return path


def reverse_rewrite(path, url_alias_modules=None):
    if url_alias_modules is None:
        url_alias_modules = default_url_alias_modules
    prepend_prefix = False
    prefix = get_script_prefix()
    if path.startswith(prefix):
        path = path[len(prefix):]
        prepend_prefix = True
    for url_alias_module in url_alias_modules:
        new_path = getattr(url_alias_module, 'reverse', lambda path: None)(path)
        if not new_path is None:
            path = new_path  # first module wins
            break
    if prepend_prefix:
        path = prefix + path
    return path


def aliased_urls(urlconf_module):
    from .resolver import AliasedURLResolver
    if isinstance(urlconf_module, six.string_types):
        urlconf_module = import_module(urlconf_module)
    return AliasedURLResolver(urlconf_module)
