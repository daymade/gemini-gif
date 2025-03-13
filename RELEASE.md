# Release Guide

This document provides instructions for releasing the Gemini GIF Generator package to PyPI.

## Version Numbering

We follow [Semantic Versioning](https://semver.org/) for this project:

- **MAJOR** version when you make incompatible API changes
- **MINOR** version when you add functionality in a backwards compatible manner
- **PATCH** version when you make backwards compatible bug fixes

## Prerequisites

1. Make sure you have an account on [PyPI](https://pypi.org/)
2. Install the required tools:
   ```bash
   pip install build twine
   ```

## Release Process

### Manual Release

1. Update the version number in `gemini_gif/__init__.py`

2. Update the CHANGELOG.md file with the changes in this release

3. Clean up any build artifacts:
   ```bash
   rm -rf build/ dist/ *.egg-info/
   ```

4. Build the package:
   ```bash
   python -m build
   ```

5. Check the built package:
   ```bash
   twine check dist/*
   ```

6. Test the package on TestPyPI (optional but recommended):
   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```

7. Install from TestPyPI to verify (optional):
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ gemini-gif
   ```

8. Upload the package to PyPI:
   ```bash
   twine upload dist/*
   ```

9. Create a new release on GitHub:
   - Tag the release with the version number (e.g., `v0.1.1`)
   - Add release notes describing the changes

### Automated Release (using Makefile)

We provide a Makefile to simplify the release process:

```bash
# Build the package
make build

# Upload to TestPyPI
make test-upload

# Upload to PyPI
make upload

# Full release process
make release
```

### GitHub Actions Automated Release

Alternatively, you can use GitHub Actions to automate the release process:

1. Create a new tag following the format `v*.*.*` (e.g., `v0.1.1`)
2. Push the tag to GitHub
3. The GitHub Actions workflow will automatically build and publish the package to PyPI

## Verifying the Release

After releasing, you can verify the installation works by running:

```bash
pip install --upgrade gemini-gif
gemini-gif --help
```

## Troubleshooting

- If you get a "File already exists" error when uploading to PyPI, it means a release with that version number already exists. You need to increment the version number.
- If you need to update the project metadata or fix issues with a release, you must increment at least the patch version number before uploading again. 