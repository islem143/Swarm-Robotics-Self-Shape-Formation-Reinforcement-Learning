from setuptools import find_packages
from setuptools import setup

setup(
    name='mrs_msg',
    version='0.0.0',
    packages=find_packages(
        include=('mrs_msg', 'mrs_msg.*')),
)
