#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example demonstrating programmatic usage of the Gemini Coder.

This example demonstrates how to use the gemini-gif package in your own Python code
without using the command-line interface.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from gemini_coder.core import main, config
from loguru import logger

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please set it before running this example.")

logger.info(f"Using API key: {api_key[:5]}...{api_key[-5:]}")

# Define animation parameters
subject = "a butterfly emerging from a cocoon"
style = "in a watercolor painting style"
output_path = "butterfly_animation.gif"

# Generate the animation
logger.info(f"Generating animation of '{subject}' {style}")
result = main.generate_animation(
    api_key=api_key,
    subject=subject,
    style=style,
    framerate=2,
    output_path=output_path,
    max_retries=3,
    verbose=True,
    log_file="gemini_coder.log"
)

# Check the result
if result and os.path.exists(output_path):
    logger.success(f"Animation successfully generated at {output_path}")
    logger.info(f"File size: {os.path.getsize(output_path) / 1024:.2f} KB")
else:
    logger.error("Failed to generate animation")

"""
Alternative method using argparse.Namespace:

If you need more control or want to use the same parameters as the CLI,
you can create an argparse.Namespace object manually:

```python
import argparse
from gemini_gif.core import main, config

args = argparse.Namespace(
    api_key=api_key,
    subject="a butterfly emerging from a cocoon",
    style="in a watercolor painting style",
    template=config.DEFAULT_TEMPLATE,
    framerate=2,
    output="butterfly_animation.gif",
    max_retries=3,
    model=config.DEFAULT_MODEL,
    log_file="gemini_gif_generator.log",
    verbose=True,
    no_preview=False
)

result = main.run(args)
```
""" 