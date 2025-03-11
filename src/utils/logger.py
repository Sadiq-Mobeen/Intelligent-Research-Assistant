import logging
import sys
import os

sys.path.append(os.path.abspath('src/config'))

from settings import settings

def setup_logging():
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )