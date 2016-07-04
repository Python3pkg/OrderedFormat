from setuptools import setup, find_packages

from codecs import open
from os import path
import re

from version import *

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = f.readlines()

setup(
    name='OrderedFormatter',
    version=version,
    long_description=long_description,
    url='https://github.com/Himenon/OrderedFormat',
    author='Himenon',
    author_email='k.himeno314@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='',
    packages=find_packages(exclude=['tests*']),
    install_requires=requires,
    tests_requires=["nose"]
)