import logging
from inspari.logging import configure_logging_default

configure_logging_default(config_path="example_logging_config.json", name="app")

logger = logging.getLogger(__name__)
logger.info("Hello world!")
