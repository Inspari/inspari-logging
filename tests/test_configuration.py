import logging.handlers
import os
import logging
import pytest
from inspari.logging import is_gunicorn, configure_logging


def test_is_gunicorn():
    # This is not gunicorn.
    assert not is_gunicorn()
    # Mock gunicorn environment.
    os.environ["SERVER_SOFTWARE"] = "gunicorn"
    assert is_gunicorn()


def test_configure_logging():
    # Should raise error, as config is not found.
    with pytest.raises(FileNotFoundError):
        configure_logging()
    # Pass in valid config path.
    assert len(logging.getLogger().handlers) == 4
    configure_logging("tests/resources/logging_config.json")
    assert len(logging.getLogger().handlers) == 3
