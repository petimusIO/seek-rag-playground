"""Python setup.py for seek_rag_playground package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("seek_rag_playground", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="seek_rag_playground",
    version=read("seek_rag_playground", "VERSION"),
    description="Awesome seek_rag_playground created by petimusIO",
    url="https://github.com/petimusIO/seek-rag-playground/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="petimusIO",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["seek_rag_playground = seek_rag_playground.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
