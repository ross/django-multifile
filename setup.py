#!/usr/bin/env python

from setuptools import setup
from os.path import join, dirname

try:
    long_description = open(join(dirname(__file__), 'README.rst')).read()
except Exception:
    long_description = None

setup(
    name='django-multifile',
    version='0.0.1',
    description='Django app version of http://github.com/thustton/django-multifile.',
    author='Ross McFarland',
    author_email='ross@gmail.com',
    url='http://github.com/ross/django-multifile',

    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages=['multifile'],
    provides=['multifile'],
)
