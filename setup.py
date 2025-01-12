import os
from setuptools import setup, find_packages


setup(
    name="workshop",
    version="0.0.1",
    author="hnfo",
    author_email="hnfo@equinor.com",
    description="TDD workshop",
    keywords=[
        "tests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Topic :: Learning :: Software Test",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "pytest",
        "black",
    ],
    test_suite="tests",
)
