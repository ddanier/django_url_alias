from django.core.urlresolvers import RegexURLResolver, reverse as base_reverse
from django.utils.functional import lazy
from .utils import resolve_rewrite, reverse_rewrite


class AliasedURLResolver(RegexURLResolver):
    def __init__(self, urlconf_module):
        super(AliasedURLResolver, self).__init__(r'', urlconf_module)

    def resolve(self, path):
        path = resolve_rewrite(path)
        return super(AliasedURLResolver, self).resolve(path)

    # This method seems to be unused due to the optimization in the root RegexURLResolver
    # (but we still updated it, so the API is complete)
    def _reverse_with_prefix(self, lookup_view, _prefix, *args, **kwargs):
        path = super(AliasedURLResolver, self)._reverse_with_prefix(lookup_view, _prefix, *args, **kwargs)
        return reverse_rewrite(path)


def reverse(viewname, urlconf=None, args=None, kwargs=None, prefix=None, current_app=None):
    path = base_reverse(viewname, urlconf=urlconf, args=args, kwargs=kwargs, prefix=prefix, current_app=current_app)
    return reverse_rewrite(path)


reverse_lazy = lazy(reverse, str)
