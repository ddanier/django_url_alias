import functools
from django.db import models
from .resolver import reverse


def permalink(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        bits = func(*args, **kwargs)
        return reverse(bits[0], None, *bits[1:3])
    return inner
permalink.__doc__ = models.permalink.__doc__
