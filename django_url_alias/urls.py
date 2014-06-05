from django.conf.urls import patterns, include, url
from django_url_alias.utils import aliased_urls
from .settings import URL_ALIAS_ROOT_URLCONF


urlpatterns = patterns('',
    aliased_urls(URL_ALIAS_ROOT_URLCONF),
)
