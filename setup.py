import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "shared",
    description = "Common shared modules",
    author = "Vasu Balakrishnan",
    packages = find_packages(exclude = ['data', 'notebooks', 'scripts']),
    long_description = read("README.md")
)