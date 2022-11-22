from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

__version__ = "0.0.0"

setup(
    name="multi-search",
    version=__version__,
    author="tyler jones",
    description="Simple multiple search source plugin style wrapper.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tylerhjones/multi-search/",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            "ms = multisearch.interface.tui:main",
        ],
    }
)