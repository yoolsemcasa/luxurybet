import logging
import os

from rich.logging import RichHandler

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("Luxury")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# Arquivo
file_handler = logging.FileHandler(
    f"{LOG_DIR}/latest.log",
    encoding="utf-8"
)

file_handler.setFormatter(formatter)

# Terminal
console_handler = RichHandler(
    rich_tracebacks=True
)

console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)