import logging.handlers
import os
import logging
import pytest
from inspari.logging import is_gunicorn, configure_logging


class MockEnv:
    """
    A class that can be used to mock environment variables temporarily.
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.backup = {}

    def __enter__(self):
        for kwarg in self.kwargs:
            self.backup[kwarg] = os.environ.get(kwarg)
            os.environ[kwarg] = self.kwargs[kwarg]

    def __exit__(self, exc_type, exc_val, exc_tb):
        for kwarg in self.kwargs:
            if self.backup[kwarg] is None:
                del os.environ[kwarg]
            else:
                os.environ[kwarg] = self.backup[kwarg]


def test_is_gunicorn():
    # This is not gunicorn.
    assert not is_gunicorn()
    # Mock gunicorn environment.
    with MockEnv(SERVER_SOFTWARE="gunicorn"):
        assert is_gunicorn()


def test_configure_logging():
    # Should raise error, as config is not found.
    with pytest.raises(FileNotFoundError):
        configure_logging()
    # Pass in valid config path.
    assert len(logging.getLogger().handlers) == 4
    configure_logging("tests/resources/logging_config.json")
    assert len(logging.getLogger().handlers) == 3
