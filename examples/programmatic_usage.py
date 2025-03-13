#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of programmatic usage of the Gemini GIF Generator.
"""

import os
import argparse
from gemini_gif.core import config, generator, processor
import tempfile
import uuid

def main():
    """Run the example."""
    # Parse arguments
    parser = argparse.ArgumentParser(description="Example of programmatic usage of the Gemini GIF Generator")
    parser.add_argument("--subject", type=str, default="A cute dancing cat", 
                        help="Subject of the animation")
    parser.add_argument("--style", type=str, default="in a 8-bit pixel art style", 
                        help="Style of the animation")
    parser.add_argument("--output", type=str, default=f"animation_{uuid.uuid4()}.gif",
                        help="Output file path")
    args = parser.parse_args()
    
    # Set up logging
    config.setup_logger()
    
    # Load environment variables
    config.load_env_variables()
    
    # Get API key from environment
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: No API key found. Please set the GEMINI_API_KEY environment variable.")
        return
    
    # Initialize Gemini client
    client = generator.initialize_client(api_key)
    
    # Construct the prompt
    prompt = f"{config.DEFAULT_TEMPLATE} {args.subject} {args.style}"
    print(f"Using prompt: {prompt}")
    
    # Generate frames
    response = generator.generate_frames(client, prompt)
    
    # Create a temporary directory to store the frames
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract frames from the response
        frame_paths, text_content = processor.extract_frames(response, temp_dir)
        
        # Create the GIF
        if frame_paths:
            if processor.create_gif_from_frames(frame_paths, args.output):
                print(f"GIF created successfully: {args.output}")
                processor.open_gif(args.output)
            else:
                print("Failed to create GIF")
        else:
            print("No frames were generated")

if __name__ == "__main__":
    main() 