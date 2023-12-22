from setuptools import find_packages
from setuptools import setup

setup(
    name='snake_cpp_py_pkg',
    version='0.0.0',
    packages=find_packages(
        include=('snake_cpp_py_pkg', 'snake_cpp_py_pkg.*')),
)
