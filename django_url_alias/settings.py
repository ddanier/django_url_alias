from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


URL_ALIAS_MODULES = getattr(settings, 'URL_ALIAS_MODULES', ())

try:
    URL_ALIAS_ROOT_URLCONF = settings.URL_ALIAS_ROOT_URLCONF
except AttributeError:
    raise ImproperlyConfigured('You need to set settings.URL_ALIAS_ROOT_URLCONF')
