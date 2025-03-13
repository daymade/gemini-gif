# Release Guide

This document provides instructions for releasing the Gemini GIF Generator package to PyPI.

## Prerequisites

1. Make sure you have an account on [PyPI](https://pypi.org/)
2. Install the required tools:
   ```bash
   pip install build twine
   ```

## Release Process

1. Update the version number in `gemini_gif/__init__.py`

2. Clean up any build artifacts:
   ```bash
   rm -rf build/ dist/ *.egg-info/
   ```

3. Build the package:
   ```bash
   python -m build
   ```

4. Test the package on TestPyPI (optional):
   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```

5. Upload the package to PyPI:
   ```bash
   twine upload dist/*
   ```

6. Create a new release on GitHub:
   - Tag the release with the version number (e.g., `v0.1.0`)
   - Add release notes describing the changes

## Verifying the Release

After releasing, you can verify the installation works by running:

```bash
pip install --upgrade gemini-gif
gemini-gif --help
``` 