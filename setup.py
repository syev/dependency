#!/usr/bin/env python

from setuptools import setup

setup(name="dependency",
      version="1.0.0",
      description="Testing stuff",
      url="https://www.github.com/syev/dependency",
      install_requires=["semantic_version"],
      packages=["dependency"],
      scripts=[],
      test_suite="test")
