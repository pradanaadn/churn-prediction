from prefect import flow, get_run_logger

from src.task.create_table_artifact import create_table_artifact_from_dataframe
from src.task.data_drift_detection import check_data_drift
from src.task.inference import run_inference
from src.task.load_data import load_data
from src.task.load_reference_data import load_data_reference


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
    reference_data = load_data_reference()
    check_data_drift(reference_data, data)
    predictions = run_inference(data)
    data['churn_prediction'] = predictions
    create_table_artifact_from_dataframe(data)
    return predictions


if __name__ == "__main__":
    batch_inference_flow()
