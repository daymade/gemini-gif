"""Processor module for handling frames and creating GIFs."""

import os
import subprocess
from io import BytesIO
from pathlib import Path
from PIL import Image
from loguru import logger as log
from tqdm import tqdm
import time

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
    
    log.info(f"Number of parts in first candidate: {len(response.candidates[0].content.parts)}")
    
    # Create a progress bar for processing the parts
    parts = response.candidates[0].content.parts
    pbar = tqdm(total=len(parts), desc="Processing frames", unit="frame")
    
    for part_index, part in enumerate(parts):
        if part.text is not None:
            # Truncate long text for logging
            truncated_text = part.text[:100] + "..." if len(part.text) > 100 else part.text
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
            log.warning(f"Part {part_index+1} has neither text nor inline_data")
        
        pbar.update(1)
    
    pbar.close()
    return frame_paths, text_content

def create_gif_from_frames(frame_paths, output_path, framerate=2):
    """Create a GIF from a list of frame paths using ffmpeg.
    
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
    
    temp_dir = os.path.dirname(frame_paths[0])
    
    # Build ffmpeg command
    ffmpeg_cmd = [
        "ffmpeg",
        "-y",  # Overwrite output file if it exists
        "-framerate", str(framerate),  # Frames per second
        "-pattern_type", "glob",
        "-i", f"{temp_dir}/frame_*.png",
        "-vf", "scale=512:-1:flags=lanczos",  # Resize while maintaining aspect ratio
        output_path
    ]
    
    try:
        cmd_str = ' '.join(ffmpeg_cmd)
        log.info(f"Running ffmpeg command: {cmd_str}")
        
        # Create a progress bar for the ffmpeg process
        with tqdm(total=100, desc="Creating GIF", unit="%") as pbar:
            # Run ffmpeg and capture output
            process = subprocess.Popen(
                ffmpeg_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Monitor the process
            while process.poll() is None:
                # Update progress bar (approximation since ffmpeg doesn't provide progress)
                pbar.update(1)
                pbar.refresh()
                time.sleep(0.1)
                
                # Don't go beyond 99% until the process is complete
                if pbar.n >= 99:
                    pbar.n = 99
                    pbar.refresh()
            
            # Complete the progress bar
            pbar.n = 100
            pbar.refresh()
            
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                log.error(f"ffmpeg failed with return code {process.returncode}")
                log.error(f"ffmpeg stderr: {stderr}")
                return False
        
        if os.path.exists(output_path):
            log.info(f"Animation successfully saved to {output_path}")
            file_size = os.path.getsize(output_path)
            log.info(f"File size: {file_size} bytes")
            return True
        else:
            log.error(f"Output file {output_path} was not created")
            return False
    except subprocess.CalledProcessError as e:
        log.error(f"Failed to create GIF: {e}")
        log.error(f"ffmpeg stdout: {e.stdout}")
        log.error(f"ffmpeg stderr: {e.stderr}")
        return False
    except Exception as e:
        log.error(f"Unexpected error: {str(e)}")
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