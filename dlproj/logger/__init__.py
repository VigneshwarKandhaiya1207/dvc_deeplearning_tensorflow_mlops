import os
import logging
from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent.parent
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y')}.log"
log_paths= os.path.join(ROOT_DIR,"logs")
os.makedirs(log_paths,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_paths,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    level=logging.INFO,
    filemode="a"
)
