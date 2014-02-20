from django.contrib.flatpages.models import FlatPage
import re


class ExampleURLAliasModule(object):
    def resolve(self, path):
        if path == 'foo/':
            return 'bar/'
        # if path == 'foo/test/':
        #     return 'bar/test/'

    def reverse(self, path):
        if path == 'bar/':
            return 'foo/'
        # if path == 'bar/test/':
        #     return 'foo/test/'


# Note: This example is not enough, as the sites relation is not handled
# DO NOT USE THIS IN PRODUCTION ENVIRONMENTS
class FlatpagesURLAliasModule(object):
    FLATPAGE_RE = re.compile('^/flatpage/(?P<pk>[0-9]+)/$')

    # Should be cached
    def resolve(self, path):
        path = '/' + path  # we need a trailing slash for flatpages
        try:
            flatpage = FlatPage.objects.get(url=path)
            return 'flatpage/%d/' % flatpage.pk
        except FlatPage.DoesNotExist:
            pass  # just return nothing

    # Should be cached
    def reverse(self, path):
        match = self.FLATPAGE_RE.match(path)
        if match:
            try:
                flatpage = FlatPage.objects.get(pk=match.group('pk'))
                return flatpage.url
            except FlatPage.DoesNotExist:
                pass  # just return nothing

