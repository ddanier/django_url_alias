from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('example',
    url(r'^bar/$', 'views.test', name='example_test'),
    url(r'^bar/(?P<var>[^/]+)/$', 'views.test', name='example_test'),
)
