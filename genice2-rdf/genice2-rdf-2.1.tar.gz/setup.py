#!/usr/bin/env python

# from distutils.core import setup, Extension
from setuptools import setup, Extension
import os
import codecs
import re

#Copied from wheel package
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.dirname(__file__), 'genice2_rdf', '__init__.py'),
                 encoding='utf8') as version_file:
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""", version_file.read()))



long_desc = "".join(open("README.md").readlines())


setup(
    name='genice2-rdf',
    version=metadata['version'],
    description='RDF format plugin for GenIce.',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    author='Masakazu Matsumoto',
    author_email='vitroid@gmail.com',
    url='https://github.com/vitroid/genice-rdf/',
    keywords=['genice', 'RDF'],

    packages=['genice2_rdf',
              'genice2_rdf.formats',
    ],

    entry_points = {
        'genice2_format': [
            '_RDF    = genice2_rdf.formats._RDF',
        ],
    },
    install_requires=['PairList>=0.2.11.1', 'GenIce2>=2.1b2'],

    license='MIT',
)
