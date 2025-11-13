from prefect import task, get_run_logger
import pandas as pd
from src.core.container import AppContainer
from sklearn.base import BaseEstimator


@task(name="run_inference")
def run_inference(data:pd.DataFrame):
    """Run inference using the provided model and data.

    Args:
        model: The machine learning model to use for inference.
        data: The input data for making predictions.
    Returns:
        The predictions made by the model.
    """
    try:
        logger = get_run_logger()
        logger.info("Running inference task.")
    except Exception:
        from loguru import logger
        logger.info("Running inference task.")
        

    model = AppContainer.model()
    validator = AppContainer.validator()
    if not isinstance(model, BaseEstimator) :
        raise TypeError("The provided model is not a valid scikit-learn model.")
    try:
        data = validator.validate(data)
    except Exception as e:
        raise ValueError(f"Data validation failed: {e}")
    predictions = model.predict(data) # pyright: ignore[reportAttributeAccessIssue]
    return predictions

