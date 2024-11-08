import os
from dotenv import load_dotenv
import logging

load_dotenv()
dir_path = os.path.dirname(os.path.abspath(__file__))

# Hours, days, weeks that the new coins w# Get the list of AllCoinsill be showing before it stops to be displayed
DAYS = 1

TESTING = os.getenv("APP_TESTING") == "true"

def get_logger(testing=TESTING):
    if testing:
        logging.basicConfig(
            format="%(asctime)s-%(name)s-%(levelname)s - %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )
    else:
        logging.basicConfig(
            filename="app.log",
            filemode="a",
            format="%(asctime)s-%(name)s-%(levelname)s - %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )
    return logging.getLogger("cryptofinder")
