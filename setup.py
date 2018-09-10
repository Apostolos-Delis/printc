#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

import printc

setup(
    name='printc',
    version=printc.__version__,
    author='Apostolos Delis',
    author_email='apost.delis@gmail.com',
    description='Printing and debugging with color',
    long_description='Printing and debugging with color as well as formatting strings with underlines, blinking'
                     'and more!',
    url="https://github.com/Apostolos-Delis/printc",
    include_package_data=True,
    packages=['printc'],
)
