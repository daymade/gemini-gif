"""
Main module for the Gemini Coder.
This module contains the main functions for generating GIFs using Google's Gemini API.
"""

import os
import tempfile
import uuid

from loguru import logger

from gemini_coder.core import config, generator, processor


def run(args):
    """Run the GIF generation process.

    This function orchestrates the entire GIF generation workflow:
    1. Sets up logging
    2. Validates and retrieves the API key
    3. Initializes the Gemini client
    4. Constructs the prompt and generates frames
    5. Processes the frames and creates the final GIF

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        str: Path to the generated GIF, or None if generation failed.
    """
    # Set up logging
    config.setup_logger(args.log_file, verbose=args.verbose)

    # Get API key
    api_key = config.get_api_key(args)
    if not api_key:
        logger.error(
            "No API key provided. Please provide it via --api-key argument or GEMINI_API_KEY environment variable."
        )
        return None

    # Initialize Gemini client
    client = generator.initialize_client(api_key)

    # Construct the prompt
    contents = f"{args.template} {args.subject} {args.style}"
    logger.info(f"Using prompt: {contents}")

    # Generate frames
    try:
        response = generator.generate_frames(
            client, contents, model=args.model, max_retries=args.max_retries
        )
    except Exception as e:
        logger.error(f"Failed to generate frames: {str(e)}")
        return None

    # Create a temporary directory to store the frames
    with tempfile.TemporaryDirectory() as temp_dir:
        logger.info(f"Created temporary directory at {temp_dir}")

        # Extract frames from the response
        frame_paths, text_content = processor.extract_frames(response, temp_dir)

        # If we have frames, create a GIF using ImageIO
        if frame_paths:
            logger.info(f"Found {len(frame_paths)} frames to process")

            # Determine output path
            output_path = args.output
            if not output_path:
                output_path = os.path.abspath(f"animation_{uuid.uuid4()}.gif")

            logger.info(f"Will save animation to {output_path}")

            # Create the GIF
            if processor.create_gif_from_frames(
                frame_paths, output_path, args.framerate
            ):
                logger.success(f"Animation successfully saved to {output_path}")
                file_size = os.path.getsize(output_path)
                logger.info(f"File size: {file_size / 1024:.2f} KB")

                # Open the resulting GIF if requested
                if not args.no_preview:
                    processor.open_gif(output_path)

                return output_path
        else:
            logger.warning("No frames were generated, cannot create animation")

    logger.info("Script completed")
    return None


def generate_animation(
    api_key,
    subject,
    style,
    framerate=2,
    output_path=None,
    max_retries=3,
    model="models/gemini-2.0-flash-exp",
    template=None,
    verbose=False,
    no_preview=False,
):
    """Generate an animated GIF using the Gemini API.

    This is a simplified function for programmatic usage that doesn't require creating
    an argparse.Namespace object manually.

    Args:
        api_key (str): Google Gemini API key.
        subject (str): Subject of the animation.
        style (str): Style of the animation.
        framerate (int, optional): Frames per second for the output GIF. Defaults to 2.
        output_path (str, optional): Output file path. Defaults to animation_<uuid>.gif.
        max_retries (int, optional): Maximum number of retries for generating frames. Defaults to 3.
        model (str, optional): Gemini model to use. Defaults to "models/gemini-2.0-flash-exp".
        template (str, optional): Template for the prompt. If None, uses the default template.
        verbose (bool, optional): Enable verbose output. Defaults to False.
        no_preview (bool, optional): Disable automatic preview of the generated GIF. Defaults to False.

    Returns:
        str: Path to the generated GIF, or None if generation failed.
    """
    import argparse

    # Create an argparse.Namespace object with the provided parameters
    if template is None:
        template = config.DEFAULT_TEMPLATE

    args = argparse.Namespace(
        api_key=api_key,
        subject=subject,
        style=style,
        template=template,
        framerate=framerate,
        output=output_path,
        max_retries=max_retries,
        model=model,
        log_file="gemini_coder.log",
        verbose=verbose,
        no_preview=no_preview,
    )

    # Run the main process
    return run(args)
