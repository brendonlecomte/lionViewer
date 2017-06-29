#!/usr/bin/env python

from distutils.core import setup


setup(
    name='Arcane Tomes',
    version='1.0',
    description='D&D 5e Reference Tool'
    author='Brendon LeComte',
    author_email='brendon.lecomte@gmail.com',
    py_modules=[],
    options={
        'app': {
            'formal_name': 'My First App',
            'bundle': 'org.example',
        },
        'macos': {
            'app_requires': [
                'toga-cocoa'
            ],
            'icon': 'icons/macos',
        },
    },
)