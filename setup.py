"""
Setup configuration for the binary tree package.

This allows installation via pip install.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="binarytree-kasim",
    version="1.0.0",
    author="Kasim",
    author_email="kasim@example.com",
    description="A professional binary tree package with YAML integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kasim/binarytree",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyYAML>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
    },
    keywords="binary-tree data-structures yaml tree algorithms",
    project_urls={
        "Bug Reports": "https://github.com/kasim/binarytree/issues",
        "Source": "https://github.com/kasim/binarytree",
    },
)