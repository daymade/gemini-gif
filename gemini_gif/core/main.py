"""Main module for the Gemini GIF Generator."""

import os
import uuid
import tempfile
from pathlib import Path
from loguru import logger as log

from gemini_gif.core import config, generator, processor

def run(args):
    """Run the GIF generation process.
    
    Args:
        args (argparse.Namespace): Parsed command-line arguments.
    
    Returns:
        str: Path to the generated GIF, or None if generation failed.
    """
    # Set up logging
    config.setup_logger(args.log_file)
    
    # Get API key
    api_key = config.get_api_key(args)
    if not api_key:
        log.error("No API key provided. Please provide it via --api-key argument or GEMINI_API_KEY environment variable.")
        return None
    
    # Initialize Gemini client
    client = generator.initialize_client(api_key)
    
    # Construct the prompt
    contents = f"{args.template} {args.subject} {args.style}"
    log.info(f"Using prompt: {contents}")
    
    # Generate frames
    try:
        response = generator.generate_frames(
            client, 
            contents, 
            model=args.model,
            max_retries=args.max_retries
        )
    except Exception as e:
        log.error(f"Failed to generate frames: {str(e)}")
        return None
    
    # Create a temporary directory to store the frames
    with tempfile.TemporaryDirectory() as temp_dir:
        log.info(f"Created temporary directory at {temp_dir}")
        
        # Extract frames from the response
        frame_paths, _ = processor.extract_frames(response, temp_dir)
        
        # If we have frames, create a GIF using ffmpeg
        if frame_paths:
            log.info(f"Found {len(frame_paths)} frames to process")
            
            # Determine output path
            output_path = args.output
            if not output_path:
                output_path = os.path.abspath(f"animation_{uuid.uuid4()}.gif")
            
            log.info(f"Will save animation to {output_path}")
            
            # List all files in the temp directory to verify
            log.info(f"Files in temp directory: {os.listdir(temp_dir)}")
            
            # Create the GIF
            if processor.create_gif_from_frames(frame_paths, output_path, args.framerate):
                # Open the resulting GIF
                processor.open_gif(output_path)
                return output_path
        else:
            log.warning("No frames were generated, cannot create animation")
    
    log.info("Script completed")
    return None 