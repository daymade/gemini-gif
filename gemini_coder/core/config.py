"""Configuration module for the Gemini GIF Generator.

This module handles configuration settings, command-line argument parsing,
environment variable loading, and logger setup for the Gemini GIF Generator.
"""

import argparse
import os
from pathlib import Path

import dotenv
from loguru import logger as log

# Default values
DEFAULT_SUBJECT = "A cute dancing cat"
DEFAULT_STYLE = "in a 8-bit pixel art style"
DEFAULT_TEMPLATE = "Create an animation by generating multiple frames, showing"
DEFAULT_FRAMERATE = 2
DEFAULT_MAX_RETRIES = 3
DEFAULT_MODEL = "models/gemini-2.0-flash-exp"


def setup_logger(log_file="gemini_coder.log", verbose=False):
    """Configure the logger with appropriate settings.

    Args:
        log_file (str): Path to the log file.
        verbose (bool): Whether to enable verbose output.
    """
    log.remove()  # Remove default handler

    # File logger - always at DEBUG level
    log.add(
        log_file,
        rotation="10 MB",
        retention="1 week",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
    )

    # Console logger - level depends on verbose flag
    console_level = "DEBUG" if verbose else "INFO"
    log.add(lambda msg: print(msg), level=console_level, format="{level} | {message}")

    if verbose:
        log.debug("Verbose logging enabled")


def load_env_variables(env_file=None):
    """Load environment variables from .env file if it exists.

    Args:
        env_file (str, optional): Path to the .env file. If None, will look in the current directory.

    Returns:
        bool: True if environment variables were loaded, False otherwise.
    """
    if env_file is None:
        # Try to find .env in the current directory or parent directories
        current_dir = Path.cwd()
        env_path = current_dir / ".env"

        # Check up to 3 parent directories
        for _ in range(3):
            if env_path.exists():
                break
            current_dir = current_dir.parent
            env_path = current_dir / ".env"
    else:
        env_path = Path(env_file)

    if env_path.exists():
        dotenv.load_dotenv(env_path)
        log.info(f"Loaded environment variables from {env_path}")
        return True
    return False


def parse_arguments():
    """Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate animated GIFs using Google's Gemini API"
    )
    parser.add_argument("--api-key", type=str, help="Google Gemini API key")
    parser.add_argument(
        "--subject",
        type=str,
        default=DEFAULT_SUBJECT,
        help=f"Subject of the animation (default: '{DEFAULT_SUBJECT}')",
    )
    parser.add_argument(
        "--style",
        type=str,
        default=DEFAULT_STYLE,
        help=f"Style of the animation (default: '{DEFAULT_STYLE}')",
    )
    parser.add_argument(
        "--template",
        type=str,
        default=DEFAULT_TEMPLATE,
        help=f"Template for the prompt (default: '{DEFAULT_TEMPLATE}')",
    )
    parser.add_argument(
        "--framerate",
        type=int,
        default=DEFAULT_FRAMERATE,
        help=f"Frames per second for the output GIF (default: {DEFAULT_FRAMERATE})",
    )
    parser.add_argument(
        "--output", type=str, help="Output file path (default: animation_<uuid>.gif)"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=DEFAULT_MAX_RETRIES,
        help=f"Maximum number of retries for generating frames (default: {DEFAULT_MAX_RETRIES})",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help=f"Gemini model to use (default: '{DEFAULT_MODEL}')",
    )
    parser.add_argument(
        "--log-file",
        default="gemini_coder.log",
        help="Path to the log file (default: gemini_coder.log)",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument(
        "--no-preview",
        action="store_true",
        help="Disable automatic preview of the generated GIF",
    )

    return parser.parse_args()


def get_api_key(args):
    """Get the API key from arguments or environment variables.

    Args:
        args (argparse.Namespace): Parsed arguments.

    Returns:
        str: The API key or None if not found.
    """
    # Try to get the API key from arguments
    api_key = args.api_key

    # If not provided, try to get it from environment variables
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY")

    return api_key
