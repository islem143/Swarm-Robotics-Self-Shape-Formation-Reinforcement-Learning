from setuptools import find_packages
from setuptools import setup

setup(
    name='dqn_msg',
    version='0.0.0',
    packages=find_packages(
        include=('dqn_msg', 'dqn_msg.*')),
)
