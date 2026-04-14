# digital_wallet/logger.py

import logging
from pathlib import Path

LOG_FILE = Path(__file__).parent.parent / "wallet.log"

def setup_logging():
    logger = logging.getLogger()
    if logger.handlers:
        return  # already configured
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    # File handler
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)