#!/usr/bin/env python
# coding: utf-8

import sys
import os

from setuptools import setup, find_packages

install_reqs = ["requests>=2.6.0"]

setup_kwargs = dict(
        name="harry",
        version="0.0.0",
        author="yaiba",
        url="https://github.com/yaiba/harry",
        description="Spy you-konw-who's snake(python) and generate statsd-like metrics.",
        install_requires=install_reqs,
        packages=find_packages(exclude=["tests*"]),
        license="BSD",
        entry_points={
            "console_scripts": [
                "harry-potter = harry.potter:main",
                ],
            },
        )

setup(**setup_kwargs)
