#!/usr/bin/env python

from setuptools import setup

setup(name="other_dependency",
      version="1.0.1",
      description="Testing stuff",
      url="https://www.github.com/syev/dependency/other_dependency",
      install_requires=["semantic_version"],
      packages=["other_dependency"],
      scripts=[],
      test_suite="test")
