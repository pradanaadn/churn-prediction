from prefect import flow, get_run_logger

from src.task.inference import run_inference
from src.task.load_data import load_data
from src.task.create_table_artifact import create_table_artifact_from_dataframe


@flow
def batch_inference_flow():
    """Batch inference flow to load data and run inference."""
    try:
        logger = get_run_logger()
        logger.info("Running batch inference flow...")
    except Exception:
        from loguru import logger

        logger.info("Running batch inference flow...")

    data = load_data()
    predictions = run_inference(data)
    data['churn_prediction'] = predictions
    create_table_artifact_from_dataframe(data)
    return predictions


if __name__ == "__main__":
    batch_inference_flow()
