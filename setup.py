# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in argemsan/__init__.py
from argemsan import __version__ as version

setup(
	name='argemsan',
	version=version,
	description='Argemsan için yazılan Custom Kodlar',
	author='Frappe',
	author_email='herdemhuseyin@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
