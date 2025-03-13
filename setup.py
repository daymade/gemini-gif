"""Setup script for the Gemini GIF Generator package."""

from setuptools import setup, find_packages
import os
import re

# Read the version from __init__.py
with open(os.path.join("gemini_gif", "__init__.py"), "r") as f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

# Read the long description from README.md
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="gemini-gif",
    version=version,
    description="A Python tool that uses Google's Gemini API to generate animated GIFs from text prompts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gemini GIF Generator Contributors",
    author_email="your.email@example.com",
    url="https://github.com/daymade/gemini-gif",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Pillow>=11.0.0",
        "google-genai>=1.5.0",
        "loguru>=0.7.0",
        "ffmpeg-python>=0.2.0",
        "python-dotenv>=1.0.0",
        "tqdm>=4.65.0",
    ],
    entry_points={
        "console_scripts": [
            "gemini-gif=gemini_gif.cli:cli",
        ],
    },
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
        "Bug Reports": "https://github.com/daymade/gemini-gif/issues",
        "Source": "https://github.com/daymade/gemini-gif",
        "Documentation": "https://github.com/daymade/gemini-gif#readme",
    },
) 