# Contributing to Gemini GIF Generator

Thank you for considering contributing to Gemini GIF Generator! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and welcoming community.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:

- A clear, descriptive title
- A detailed description of the bug
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment information (OS, Python version, etc.)

### Suggesting Features

If you have an idea for a new feature, please create an issue with the following information:

- A clear, descriptive title
- A detailed description of the feature
- Why this feature would be useful
- Any implementation ideas you have

### Pull Requests

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Run tests to ensure your changes don't break existing functionality
5. Submit a pull request

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gemini-gif.git
   cd gemini-gif
   ```

2. Create and activate a virtual environment:
   ```bash
   # Using conda
   conda env create -f environment.yml
   conda activate gemini-gif
   
   # Or using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

4. Install development dependencies:
   ```bash
   pip install pytest black isort
   ```

## Code Style

We follow the [Black](https://black.readthedocs.io/en/stable/) code style and use [isort](https://pycqa.github.io/isort/) for import sorting.

To format your code:

```bash
black gemini_gif tests examples
isort gemini_gif tests examples
```

## Testing

We use pytest for testing. To run the tests:

```bash
pytest
```

## Documentation

Please document your code using docstrings following the Google style guide. Example:

```python
def function_name(param1, param2):
    """Short description of the function.
    
    Longer description of the function if needed.
    
    Args:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
    
    Returns:
        type: Description of the return value.
    
    Raises:
        ExceptionType: When and why this exception is raised.
    """
    # Function implementation
```

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License. 