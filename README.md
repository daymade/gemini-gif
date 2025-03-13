# Gemini GIF Generator

A Python tool that uses Google's Gemini API to generate animated GIFs from text prompts.

> 🙏 Inspired by [@Miyamura80's gist](https://gist.github.com/Miyamura80/b593041f19875445ca1374599d219387)

## Features

- Generate animated GIFs using Google's Gemini 2.0 Flash model
- Customize animation subject, style, and frame rate
- Automatic retry logic to ensure multiple frames are generated
- **Simple command-line interface** for quick and easy use
- Support for storing API key in .env file for convenience
- Progress bars for better user experience
- Programmatic API for integration into other projects

## Quick Start

```bash
# Install the package
pip install gemini-gif

# Set your API key (one-time setup)
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Generate a GIF with default settings (dancing cat in pixel art style)
gemini-gif

# Generate a GIF with custom subject and style
gemini-gif --subject "a dancing robot" --style "in a neon cyberpunk style"
```

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

### System Requirements

Make sure FFmpeg is installed on your system:

- **macOS**: `brew install ffmpeg`
- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) or use Chocolatey: `choco install ffmpeg`

## API Key Setup

You can provide your Gemini API key in several ways:

### Using a .env File (Recommended)

Create a file named `.env` in your current directory with the following content:

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

## Command-line Usage

The command-line interface is the easiest way to use Gemini GIF Generator:

```bash
# Generate a GIF with default settings (dancing cat in pixel art style)
gemini-gif

# Generate a GIF with custom subject and style
gemini-gif --subject "a dancing robot" --style "in a neon cyberpunk style"

# Save to a specific output file
gemini-gif --subject "a butterfly emerging from a cocoon" --output butterfly_animation.gif

# Enable verbose output for more detailed logs
gemini-gif --verbose

# Disable automatic preview of the generated GIF
gemini-gif --no-preview
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
- `--no-preview`: Disable automatic preview of the generated GIF

### Examples

```bash
# Generate a blooming flower animation
gemini-gif --subject "a seed growing into a plant and then blooming into a flower" --style "in a watercolor style"

# Create a rocket launch animation with custom frame rate
gemini-gif --subject "a rocket launching into space" --style "in a retro sci-fi style" --framerate 3

# Save to a specific output file
gemini-gif --subject "a butterfly emerging from a cocoon" --output butterfly_animation.gif
```

## Programmatic Usage

You can also use the package programmatically in your own Python code:

```python
import os
from dotenv import load_dotenv
from gemini_gif.core.main import generate_animation

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Generate the animation
result = generate_animation(
    api_key=api_key,
    subject="a butterfly emerging from a cocoon",
    style="in a watercolor painting style",
    output_path="butterfly_animation.gif",
    framerate=2,
    verbose=True
)

if result:
    print(f"Animation successfully generated at {result}")
```

See the `examples/programmatic_usage.py` file for a complete example.

## Troubleshooting

- If you encounter issues with the Gemini API, check your API key and ensure you have access to the Gemini 2.0 Flash model.
- If FFmpeg fails, ensure it's properly installed and accessible in your PATH.
- For any other issues, check the log file (`gemini_gif_generator.log`) for detailed error messages.
- Enable verbose output with `--verbose` for more detailed logs.

## License

This project is open source and available under the MIT License. 