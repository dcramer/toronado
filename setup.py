#!/usr/bin/env python
import sys

from setuptools import find_packages, setup

# XXX: This is a hack to prevent nose from registering invalid exit handlers.
try:
    import multiprocessing
except ImportError:
    pass


install_requires = [
    'cssselect',
    'cssutils',
    'lxml',
]

tests_require = [
    'exam',
    'unittest2',
]

setup(
    name='toronado',
    version='0.0.2',
    author='ted kaemming, disqus',
    author_email='ted@disqus.com',
    packages=find_packages(exclude=('tests',)),
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='tests',
    zip_safe=False,
    license='Apache License 2.0',
)
