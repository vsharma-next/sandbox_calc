"""Set up the project."""
# Standard library
from typing import List
from typing import Sequence

# Third-party
from pkg_resources import parse_requirements
from setuptools import find_packages
from setuptools import setup


def read_present_files(paths: Sequence[str]) -> str:
    """Read the content of those files that are present."""
    contents: List[str] = []
    for path in paths:
        try:
            with open(path, "r") as f:
                contents += ["\n".join(map(str.strip, f.readlines()))]
        except FileNotFoundError:
            continue
    return "\n\n".join(contents)


description_files = [
    "README",
    "README.rst",
    "README.md",
    "HISTORY",
    "HISTORY.rst",
    "HISTORY.md",
]

metadata = {
    "name": "sandbox_calc",
    "version": "0.1.0",
    "description": "a sandbox for using cookiecutter",
    "long_description": read_present_files(description_files),
    "author": "Varun Sharma",
    "author_email": "vsharma.next@gmail.com",
    "url": "https://github.com/vsharma-next/sandbox_calc",
    "keywords": "sandbox_calc",
    "classifiers": [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
}

python = ">= 3.7"

# Runtime dependencies (unpinned: only critical version restrictions)
with open("requirements/requirements.in") as f:
    requirements = list(map(str, parse_requirements(f.readlines())))

scripts = [
    "sandbox_calc=sandbox_calc.cli:main",
]

setup(
    python_requires=python,
    install_requires=requirements,
    entry_points={"console_scripts": scripts},
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_save=False,
    **metadata,
)
