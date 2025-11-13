import random
from prefect import task, get_run_logger
import pandas as pd


@task
def load_data():
    """ """
    try:
        logger = get_run_logger()
        logger.info("Loading inference data...")
    except Exception:
        from loguru import logger
        logger.info("Loading inference data...")
        
    path_data = random.choice(
        [
            "artifact/dummy_inference_churn_data.csv",
            "artifact/dummy_inference_churn_drift_data.csv",
        ]
    )
    df = pd.read_csv(path_data)
    return df
