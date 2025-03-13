# Gemini GIF Generator

A Python tool that uses Google's Gemini API to generate animated GIFs from text prompts.

> 🙏 Inspired by [@Miyamura80's gist](https://gist.github.com/Miyamura80/b593041f19875445ca1374599d219387)

## Features

- Generate animated GIFs using Google's Gemini 2.0 Flash model
- Customize animation subject, style, and frame rate
- Automatic retry logic to ensure multiple frames are generated
- Command-line interface with customizable parameters
- Support for storing API key in .env file for convenience
- Progress bars for better user experience
- Programmatic API for integration into other projects

## Requirements

- Python 3.10+
- FFmpeg (system installation)
- Google Gemini API key

## Installation

### Using pip (Recommended)

```bash
# Install directly from PyPI
pip install gemini-gif
```

### From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/gemini-gif.git
cd gemini-gif

# Install in development mode
pip install -e .
```

### Using Conda Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/gemini-gif.git
cd gemini-gif

# Create and activate the conda environment from the environment.yml file
conda env create -f environment.yml
conda activate gemini-gif

# Install in development mode
pip install -e .
```

### System Requirements

Make sure FFmpeg is installed on your system:

- **macOS**: `brew install ffmpeg`
- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) or use Chocolatey: `choco install ffmpeg`

## API Key Setup

You can provide your Gemini API key in several ways:

### Using a .env File (Recommended)

Create a file named `.env` in the project directory with the following content:

```
GEMINI_API_KEY=your_api_key_here
```

The script will automatically load the API key from this file.

### Using Environment Variables

```bash
# Set your Gemini API key as an environment variable
export GEMINI_API_KEY="your_api_key_here"
```

### Using Command-line Arguments

```bash
# Provide the API key directly as a command-line argument
gemini-gif --api-key "your_api_key_here" --subject "your subject"
```

## Usage

### Using the Command-line Interface

After installation, you can use the `gemini-gif` command:

```bash
# Generate a GIF with default settings (dancing cat in pixel art style)
gemini-gif

# Generate a GIF with custom subject and style
gemini-gif --subject "a dancing robot" --style "in a neon cyberpunk style"
```

### Using the Shell Script

For convenience, you can use the provided shell script (if you installed from source):

```bash
# Generate a GIF with default settings
./generate_gif.sh

# Generate a GIF with custom subject and style
./generate_gif.sh --subject "a dancing robot" --style "in a neon cyberpunk style"
```

### Command-line Options

```bash
gemini-gif --help
```

Available options:

- `--api-key`: Google Gemini API key (can also be set via GEMINI_API_KEY environment variable)
- `--subject`: Subject of the animation (default: "A cute dancing cat")
- `--style`: Style of the animation (default: "in a 8-bit pixel art style")
- `--template`: Template for the prompt (default: "Create an animation by generating multiple frames, showing")
- `--framerate`: Frames per second for the output GIF (default: 2)
- `--output`: Output file path (default: animation_<uuid>.gif)
- `--max-retries`: Maximum number of retries for generating frames (default: 3)
- `--model`: Gemini model to use (default: "models/gemini-2.0-flash-exp")
- `--log-file`: Path to the log file (default: gemini_gif_generator.log)
- `--verbose`: Enable verbose output

### Examples

```bash
# Generate a blooming flower animation
gemini-gif --subject "a seed growing into a plant and then blooming into a flower" --style "in a watercolor style"

# Create a rocket launch animation with custom frame rate
gemini-gif --subject "a rocket launching into space" --style "in a retro sci-fi style" --framerate 3

# Save to a specific output file
gemini-gif --subject "a butterfly emerging from a cocoon" --output butterfly_animation.gif
```

### Programmatic Usage

You can also use the package programmatically in your own Python code:

```python
import os
import tempfile
from gemini_gif.core import config, generator, processor

# Set up logging and load environment variables
config.setup_logger()
config.load_env_variables()

# Get API key from environment
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No API key found. Please set the GEMINI_API_KEY environment variable.")

# Initialize Gemini client
client = generator.initialize_client(api_key)

# Construct the prompt
subject = "A cute dancing cat"
style = "in a 8-bit pixel art style"
prompt = f"{config.DEFAULT_TEMPLATE} {subject} {style}"
print(f"Using prompt: {prompt}")

# Generate frames
response = generator.generate_frames(client, prompt)

# Create a temporary directory to store the frames
with tempfile.TemporaryDirectory() as temp_dir:
    # Extract frames from the response
    frame_paths, text_content = processor.extract_frames(response, temp_dir)
    
    # Create the GIF
    output_path = "my_animation.gif"
    if frame_paths:
        if processor.create_gif_from_frames(frame_paths, output_path):
            print(f"GIF created successfully: {output_path}")
            processor.open_gif(output_path)
```

See the `examples/programmatic_usage.py` file for a complete example.

## Development

### Project Structure

```
gemini-gif/
├── gemini_gif/              # Main package
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # Command-line interface
│   └── core/                # Core functionality
│       ├── __init__.py
│       ├── config.py        # Configuration handling
│       ├── generator.py     # Frame generation
│       ├── main.py          # Main process
│       └── processor.py     # Frame processing and GIF creation
├── tests/                   # Test directory
│   ├── __init__.py
│   └── test_config.py       # Tests for config module
├── examples/                # Example scripts
│   └── programmatic_usage.py # Example of programmatic usage
├── .env                     # Environment variables (not in git)
├── .gitignore               # Git ignore file
├── LICENSE                  # MIT License
├── README.md                # This file
├── environment.yml          # Conda environment file
├── pyproject.toml           # Python project configuration
└── setup.py                 # Package setup script
```

### Running Tests

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest
```

## Troubleshooting

- If you encounter issues with the Gemini API, check your API key and ensure you have access to the Gemini 2.0 Flash model.
- If FFmpeg fails, ensure it's properly installed and accessible in your PATH.
- For any other issues, check the log file (`gemini_gif_generator.log`) for detailed error messages.

## License

This project is open source and available under the MIT License. 