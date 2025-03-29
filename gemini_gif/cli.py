"""Command-line interface for the Gemini GIF Generator."""

import sys

from gemini_gif.core import config, main


def cli():
    """Command-line interface entry point."""
    # Load environment variables
    config.load_env_variables()

    # Parse arguments
    args = config.parse_arguments()

    # Run the main process
    result = main.run(args)

    # Return appropriate exit code
    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    cli()
