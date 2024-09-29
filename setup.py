# setup.py
from setuptools import setup, find_packages

setup(
    name="pymeasware",
    version="0.1.0",
    author="Sebastian Ramirez",
    author_email="sebram8@gmail.com",
    description="Lab instruments control",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sebram99/pymeasware",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List any package dependencies here
        "pyvisa"
    ],
)