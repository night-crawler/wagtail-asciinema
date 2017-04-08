#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import find_packages, setup
from wagtail_asciinema import __version__

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='wagtail-asciinema',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/night-crawler/wagtail-asciinema',
    license='MIT',
    author='night-crawler',
    author_email='www@force.fm',
    description='Implements Wagtail CMS asciinema integration',
    include_package_data=True,
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ],

    install_requires=[
        'wagtail>=1.8',
    ],

)
