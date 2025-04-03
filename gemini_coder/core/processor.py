"""Processor module for handling frames and creating GIFs."""

import os
from io import BytesIO

import imageio
import numpy as np
from loguru import logger as log
from PIL import Image
from tqdm import tqdm


def extract_frames(response, temp_dir):
    """Extract frames from the Gemini API response.

    Args:
        response: The response from the Gemini API.
        temp_dir (str): Path to the temporary directory to save frames.

    Returns:
        tuple: A tuple containing (list of frame paths, list of text content).
    """
    frame_paths = []
    text_content = []
    frame_count = 0

    # Process and save each part
    log.info(f"Number of candidates: {len(response.candidates)}")
    if not response.candidates:
        log.error("No candidates returned in the response")
        return frame_paths, text_content

    log.info(
        f"Number of parts in first candidate: {len(response.candidates[0].content.parts)}"
    )

    # Create a progress bar for processing the parts
    parts = response.candidates[0].content.parts
    pbar = tqdm(total=len(parts), desc="Processing frames", unit="frame")

    for part_index, part in enumerate(parts):
        if part.text is not None:
            # Truncate long text for logging
            truncated_text = (
                part.text[:100] + "..." if len(part.text) > 100 else part.text
            )
            log.info(f"Text content: {truncated_text}")
            text_content.append(part.text)
            print(part.text)
        elif part.inline_data is not None:
            # Save the image to a temporary file
            frame_path = os.path.join(temp_dir, f"frame_{frame_count:03d}.png")
            image = Image.open(BytesIO(part.inline_data.data))
            image.save(frame_path)
            frame_paths.append(frame_path)
            frame_count += 1
        else:
            log.warning(f"Part {part_index + 1} has neither text nor inline_data")

        pbar.update(1)

    pbar.close()
    return frame_paths, text_content


def create_gif_from_frames(frame_paths, output_path, framerate=2):
    """Create a GIF from a list of frame paths using imageio.

    Args:
        frame_paths (list): List of paths to the frame images.
        output_path (str): Path to save the output GIF.
        framerate (int): Frames per second for the output GIF.

    Returns:
        bool: True if the GIF was created successfully, False otherwise.
    """
    if not frame_paths:
        log.error("No frames provided to create GIF")
        return False

    try:
        log.info(f"Creating GIF using imageio at {output_path}")
        duration = 1 / framerate  # Duration per frame in seconds
        images = []

        # Read first frame and calculate target size with 480px width
        base_image = Image.open(frame_paths[0])
        ratio = 320 / base_image.size[0]
        target_size = (320, int(base_image.size[1] * ratio))

        for frame_path in tqdm(frame_paths, desc="Reading frames", unit="frame"):
            frame = Image.open(frame_path)
            frame = frame.resize(target_size, Image.LANCZOS)
            images.append(np.array(frame))

        # Save the GIF
        imageio.mimsave(output_path, images, duration=duration)
        log.info(f"Animation successfully saved to {output_path}")
        file_size = os.path.getsize(output_path)
        log.info(f"File size: {file_size} bytes")
        return True
    except Exception as e:
        log.error(f"Failed to create GIF with imageio: {str(e)}")
        return False


def open_gif(output_path):
    """Open the generated GIF.

    Args:
        output_path (str): Path to the GIF file.

    Returns:
        bool: True if the GIF was opened successfully, False otherwise.
    """
    try:
        Image.open(output_path).show()
        return True
    except Exception as e:
        log.error(f"Failed to open the GIF: {str(e)}")
        return False
