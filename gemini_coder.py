#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Gemini GIF Generator
--------------------
A script to generate animated GIFs using Google's Gemini API.

This is a simple wrapper around the gemini_gif package.
"""

import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent))

from gemini_coder.cli import cli

if __name__ == "__main__":
    cli() 