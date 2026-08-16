"""Test configuration module."""

import os
import tempfile
from pathlib import Path

from gemini_gif.core import config


def test_default_values():
    """Test that default values are set correctly."""
    assert config.DEFAULT_SUBJECT == "A cute dancing cat"
    assert config.DEFAULT_STYLE == "in a 8-bit pixel art style"
    assert config.DEFAULT_FRAMERATE == 2
    assert config.DEFAULT_MAX_RETRIES == 3


def test_load_env_variables(monkeypatch):
    """Test loading environment variables from .env file."""
    # The test owns this process environment; a developer's real key must not
    # mask the value loaded from the temporary fixture.
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    # Close the fixture before dotenv opens it. Windows does not permit a
    # second open of NamedTemporaryFile while its original handle is active.
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_env = Path(temp_dir) / "test.env"
        temp_env.write_text("GEMINI_API_KEY=test_api_key\n", encoding="utf-8")

        # Load the environment variables
        result = config.load_env_variables(temp_env)

        # Check that the function returned True
        assert result is True

        # Check that the environment variable was loaded
        assert os.environ.get("GEMINI_API_KEY") == "test_api_key"


def test_get_api_key():
    """Test getting the API key from arguments or environment variables."""

    # Test getting the API key from arguments
    class Args:
        api_key = "arg_api_key"

    args = Args()
    assert config.get_api_key(args) == "arg_api_key"

    # Test getting the API key from environment variables
    args.api_key = None
    os.environ["GEMINI_API_KEY"] = "env_api_key"
    assert config.get_api_key(args) == "env_api_key"

    # Test when no API key is available
    os.environ.pop("GEMINI_API_KEY", None)
    assert config.get_api_key(args) is None
