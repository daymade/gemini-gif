.PHONY: clean build test test-upload upload release install dev-install lint format check

# Default Python interpreter
PYTHON := python
# Package name
PACKAGE := gemini-gif

# Clean build artifacts
clean:
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Install development dependencies
dev-deps:
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -U build twine pytest black isort flake8

# Install the package in development mode
dev-install:
	$(PYTHON) -m pip install -e .

# Install the package
install:
	$(PYTHON) -m pip install .

# Run tests
test:
	$(PYTHON) -m pytest

# Lint code
lint:
	$(PYTHON) -m flake8 gemini_gif tests

# Format code
format:
	$(PYTHON) -m black gemini_gif tests
	$(PYTHON) -m isort gemini_gif tests

# Check code formatting
check:
	$(PYTHON) -m black --check gemini_gif tests
	$(PYTHON) -m isort --check gemini_gif tests
	$(PYTHON) -m flake8 gemini_gif tests

# Build package
build: clean
	$(PYTHON) -m build
	$(PYTHON) -m twine check dist/*

# Upload to Test PyPI
test-upload: build
	$(PYTHON) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Upload to PyPI
upload: build
	$(PYTHON) -m twine upload dist/*

# Full release process
release: clean test check build upload
	@echo "Release completed successfully!"
	@echo "Don't forget to create a GitHub release with tag v$(shell $(PYTHON) -c "import gemini_gif; print(gemini_gif.__version__)")"

# Show help
help:
	@echo "Available targets:"
	@echo "  clean        - Remove build artifacts"
	@echo "  dev-deps     - Install development dependencies"
	@echo "  dev-install  - Install package in development mode"
	@echo "  install      - Install package"
	@echo "  test         - Run tests"
	@echo "  lint         - Lint code"
	@echo "  format       - Format code"
	@echo "  check        - Check code formatting"
	@echo "  build        - Build package"
	@echo "  test-upload  - Upload to Test PyPI"
	@echo "  upload       - Upload to PyPI"
	@echo "  release      - Full release process"
	@echo "  help         - Show this help" 