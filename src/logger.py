import logging
import os
from datetime import datetime


now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

LOG_FILE_NAME = f"{now}.log"
LOGS_PATH= os.path.join(os.getcwd(), "logs", LOG_FILE_NAME)
os.makedirs(LOGS_PATH, exist_ok=True)


LOG_FILE_PATH=os.path.join(LOGS_PATH,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)


if __name__=="__main__":
    logging.info("logging has started")