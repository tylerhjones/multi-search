from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="multi-search",
    version="0.0.1",
    author="tyler jones",
    description="Simple multiple search source plugin style wrapper.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tylerhjones/multi-search/",
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
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