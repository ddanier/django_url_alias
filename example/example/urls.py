from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Enable the admin
    url(r'^admin/', include(admin.site.urls)),

    # Simple static example
    url(r'^bar/$', 'example.views.test', name='example_test'),
    url(r'^bar/(?P<var>[^/]+)/$', 'example.views.test', name='example_test'),

    # Simple flatpage example
    url(r'^flatpage/(?P<pk>[0-9]+)/$', 'example.views.flatpage', name='flatpage'),
)
