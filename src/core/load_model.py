from pathlib import Path
from sklearn.base import BaseEstimator

import joblib


def load_model(model_path: str) -> BaseEstimator:
    """Load a machine learning model from the specified file path.

    Args:
        model_path (str): The file path to the saved model.
    Returns:
        The loaded machine learning model.
    """
    if not Path(model_path).exists():
        raise FileNotFoundError(
            f"The specified model path does not exist: {model_path}"
        )
    if not Path(model_path).is_file():
        raise FileNotFoundError(
            f"The specified model path does not exist: {model_path}"
        )
    model = joblib.load(model_path)
    if not isinstance(model, BaseEstimator):
        raise TypeError("The loaded object is not a valid scikit-learn model.")
    return model
