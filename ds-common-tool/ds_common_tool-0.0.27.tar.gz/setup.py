#!/usr/bin/env python
# coding=utf-8
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ds_common_tool",
    version="0.0.27",
    author="ZhangLe",
    author_email="zhangle@example.com",
    description="data processing & modeling function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZhangLe59151/data_model_processing_tool",
    project_urls={
        "Bug Tracker": "https://github.com/ZhangLe59151/data_model_processing_tool",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages("."),
    install_requires = [
      'pandas>=0.25.1',
      'numpy>=1.21.5', 
      'DateTime>=4.4', 
      'tensorflow>=2.7.0'],
    python_requires=">=3.6",
)