import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

# Create logs directory if it doesn't exist
main_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
logs_dir = os.path.join(main_dir, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(
            os.path.join(logs_dir, datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"),
            maxBytes=1000000,
            backupCount=1
        ),
        logging.StreamHandler()
    ]
)