"""Generator module for the Gemini GIF Generator."""

import time

from google import genai
from google.genai import types
from loguru import logger as log
from tqdm import tqdm


def initialize_client(api_key):
    """Initialize the Gemini client.

    Args:
        api_key (str): The API key for the Gemini API.

    Returns:
        genai.Client: The initialized client.
    """
    return genai.Client(api_key=api_key)


def generate_frames(client, prompt, model="models/gemini-2.0-flash-exp", max_retries=3):
    """Generate animation frames with retry logic if only one frame is returned.

    Args:
        client (genai.Client): The Gemini client.
        prompt (str): The prompt to generate frames from.
        model (str): The model to use for generation.
        max_retries (int): Maximum number of retries if not enough frames are generated.

    Returns:
        google.genai.types.GenerateContentResponse: The response from the Gemini API.
    """
    # Create a progress bar for the generation attempts
    pbar = tqdm(total=max_retries, desc="Generating frames", unit="attempt")

    for attempt in range(1, max_retries + 1):
        log.info(
            f"Attempt {attempt}/{max_retries}: Sending request to Gemini with prompt: {prompt}"
        )

        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["Text", "Image"]
                ),
            )

            # Count the number of image frames
            frame_count = 0
            if response.candidates:
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        frame_count += 1

            log.info(f"Received {frame_count} frames in response")

            # If we got multiple frames, return the response
            if frame_count > 1:
                log.info(
                    f"Successfully received {frame_count} frames on attempt {attempt}"
                )
                pbar.update(max_retries - pbar.n)  # Complete the progress bar
                pbar.close()
                return response

            # If this was the last attempt, return what we have
            if attempt == max_retries:
                log.warning(
                    f"Failed to get multiple frames after {max_retries} attempts. Proceeding with {frame_count} frames."
                )
                pbar.update(1)
                pbar.close()
                return response

            # Otherwise, try again with a stronger prompt
            log.warning(
                f"Only received {frame_count} frame(s). Retrying with enhanced prompt..."
            )
            prompt = f"{prompt} Please create at least 5 distinct frames showing different stages of the animation."
            time.sleep(1)  # Small delay between retries

            pbar.update(1)

        except Exception as e:
            log.error(f"Error generating frames: {str(e)}")
            if attempt == max_retries:
                pbar.close()
                raise
            time.sleep(2)  # Longer delay after an error
            pbar.update(1)

    # This should not be reached, but just in case
    pbar.close()
    raise RuntimeError("Failed to generate frames after maximum retries")
