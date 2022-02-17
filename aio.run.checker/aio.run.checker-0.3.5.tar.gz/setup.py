
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: aio.run.checker:package

from setuptools import setup

setup(**{
    'author': 'Ryan Northey',
    'author_email': 'ryan@synca.io',
    'description': '"Async checker definitions"',
    'install_requires': (
        'abstracts>=0.0.12',
        'aio.run.runner>=0.2.6',
    ),
    'license': 'Apache Software License 2.0',
    'long_description': """
aio.run.checker
===============

Async checker definitions.
""",
    'maintainer': 'Ryan Northey',
    'maintainer_email': 'ryan@synca.io',
    'name': 'aio.run.checker',
    'namespace_packages': (
    ),
    'package_data': {
        'aio.run.checker': (
            'py.typed',
        ),
    },
    'packages': (
        'aio.run.checker',
    ),
    'url': 'https://github.com/envoyproxy/pytooling/tree/main/aio.run.checker',
    'version': '0.3.5',
})
