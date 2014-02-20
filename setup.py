from setuptools import setup, find_packages

setup(
    name = "django_url_alias",
    version = "0.1.1",
    description = 'Allow Django URLS to be completely rewritten (alias names for system URLs)',
    author = 'David Danier',
    author_email = 'david.danier@team23.de',
    url = 'https://github.com/ddanier/django_url_alias',
    long_description=open('README.rst', 'r').read(),
    packages = [
        'django_url_alias',
        'django_url_alias.templatetags',
    ],
    install_requires = [
        'Django >=1.5',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

