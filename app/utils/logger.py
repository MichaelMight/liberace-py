import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

from app.core.config import get_settings

settings = get_settings()

# log formats
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
if settings.ENVIRONMENT == "development":
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"


def setup_logger(name: str, log_file: str | None = None, level: int = logging.INFO) -> logging.Logger:
    """Logger init"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Log console output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console_handler)

    # Log file configuration
    if log_file:
        log_path = Path("logs")
        log_path.mkdir(exist_ok=True)

        file_handler = RotatingFileHandler(
            log_path / log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding="utf-8"
        )
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(file_handler)

    return logger


# Default logger configuration
logger = setup_logger(
    "app",
    "app.log" if not settings.DEBUG else None,
    logging.DEBUG if settings.DEBUG else logging.INFO
)
