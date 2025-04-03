#!/bin/bash

# This script runs the Gemini GIF generator with the API key from the .env file

# Activate conda environment if it exists
if conda info --envs | grep -q "^gemini-gif "; then
    eval "$(conda shell.bash hook)"
    conda activate gemini-gif
else
    echo "Warning: 'gemini-gif' conda environment not found. Make sure to set it up first."
    echo "Run: conda env create -f environment.yml"
fi

# Run the script with all provided arguments
python -m gemini_coder.cli "$@" 