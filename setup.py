#!/usr/bin/env python

from setuptools import setup

setup(
    name='tilejet-util',
    version='0.0.2',
    install_requires=[],
    author='TileJet Developers',
    author_email='tilejet.dev@gmail.com',
    license='MIT License',
    url='https://github.com/tilejet/tilejet-util/',
    keywords='python gis tilejet',
    description='A python utility library containing functions for managing tile services, such as converting between z/x/y to geojson.',
    long_description=open('README.md').read(),
    download_url="https://github.com/tilejet/tilejet-util/zipball/master",
    #py_modules=["tilejetutil"],
    packages=["tilejetutil"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
