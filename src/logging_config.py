import logging
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/pipeline.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("pipeline")

# ESTA LINHA É A QUE VOCÊ DEVE TER ESQUECIDO OU ESCRITO DIFERENTE
logger = setup_logging()