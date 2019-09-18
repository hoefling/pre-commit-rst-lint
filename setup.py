#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup

rst_lint_version = (Path(__file__).parent / '.version').read_text().strip()

setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    install_requires=['restructuredtext-lint=={}'.format(rst_lint_version)],
)
