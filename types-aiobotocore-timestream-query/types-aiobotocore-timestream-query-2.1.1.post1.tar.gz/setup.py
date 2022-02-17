from os.path import abspath, dirname

from setuptools import setup

LONG_DESCRIPTION = open(dirname(abspath(__file__)) + "/README.md", "r").read()


setup(
    name="types-aiobotocore-timestream-query",
    version="2.1.1.post1",
    packages=["types_aiobotocore_timestream_query"],
    url="https://github.com/vemel/mypy_boto3_builder",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Type annotations for aiobotocore.TimestreamQuery 2.1.1 service generated with mypy-boto3-builder 7.1.1",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    keywords="aiobotocore timestream-query type-annotations boto3-stubs mypy typeshed autocomplete",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"types_aiobotocore_timestream_query": ["py.typed", "*.pyi"]},
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://mypy-boto3-builder.readthedocs.io/en/latest/",
        "Source": "https://github.com/vemel/mypy_boto3_builder",
        "Tracker": "https://github.com/vemel/mypy_boto3_builder/issues",
    },
    install_requires=[
        "typing-extensions; python_version < '3.9'",
    ],
    zip_safe=False,
)
