from django.core.urlresolvers import RegexURLResolver, reverse
from django.utils.functional import lazy
from .utils import resolve_rewrite, reverse_rewrite


class AliasedURLResolver(RegexURLResolver):
    def __init__(self, urlconf_module):
        super(AliasedURLResolver, self).__init__(r'', urlconf_module)

    def resolve(self, path):
        path = resolve_rewrite(path)
        return super(AliasedURLResolver, self).resolve(path)

    def _reverse_with_prefix(self, lookup_view, _prefix, *args, **kwargs):
        path = super(AliasedURLResolver, self)._reverse_with_prefix(lookup_view, _prefix, *args, **kwargs)
        return reverse_rewrite(path)


def aliased_reverse(viewname, urlconf=None, args=None, kwargs=None, prefix=None, current_app=None):
    path = reverse(viewname, urlconf=None, args=None, kwargs=None, prefix=None, current_app=None)
    return reverse_rewrite(path)

aliased_reverse_lazy = lazy(aliased_reverse, str)
