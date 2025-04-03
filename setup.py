"""Setup script for the Gemini Coder package."""

from setuptools import setup, find_packages
import os
import re

# Read the version from __init__.py
with open(os.path.join("gemini_coder", "__init__.py"), "r") as f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

# Read the long description from README.md
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="gemini-coder",
    version=version,
    description="A Python tool that uses Google's Gemini API to generate animated GIFs from text prompts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gemini Coder Contributors",
    author_email="your.email@example.com",
    url="https://github.com/daymade/gemini-coder",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Utilities",
        "Topic :: Artistic Software",
        "Operating System :: OS Independent",
    ],
    keywords="gemini, gif, animation, ai, google, generative, animation, pixel art",
    python_requires=">=3.10",
    project_urls={
        "Bug Reports": "https://github.com/daymade/gemini-coder/issues",
        "Source": "https://github.com/daymade/gemini-coder",
        "Documentation": "https://github.com/daymade/gemini-coder#readme",
    },
) 