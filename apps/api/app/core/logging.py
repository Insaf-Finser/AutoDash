from pathlib import Path
import sys

from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def configure_logging() ->None:

    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        colorize=True,
        backtrace=True,
        diagnose=True,
        enqueue=True,
    )

    logger.add(
        LOG_DIR / "app.log",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        level="INFO",
        enqueue=True,
    )