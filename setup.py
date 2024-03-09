import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="numify",
    version="1.1.0",
    description="Convert alphanumeric characters to integers i.e 1k to 1000",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/boadley/numify",
    author="jaboadley",
    author_email="numify@mailinator.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["numify"],
    include_package_data=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
)
