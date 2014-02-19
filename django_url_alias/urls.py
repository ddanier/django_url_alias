from django.conf.urls import patterns, include, url
from django_url_alias.utils import aliased_urls
from django.conf import settings

urlpatterns = patterns('',
    aliased_urls(settings.URL_ALIAS_ROOT_URLCONF),
)
