from prefect import task, get_run_logger
import pandas as pd


@task
def load_data_reference():
    """
    Load reference data (training set). 
    """
    try:
        logger = get_run_logger()
        logger.info("Loading reference data...")
    except Exception:
        from loguru import logger
        logger.info("Loading reference data...")
        
    df = pd.read_csv("artifact/train_set_reference.csv")
    return df
