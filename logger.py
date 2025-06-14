# logger.py
import logging

logging.basicConfig(
    level=logging.INFO,

    # %(asctime)s | %(levelname)s | %(filename)s
    # Change the format as you like

    format="%(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
