from dependency_injector import containers, providers
from pandantic import Pandantic

from src.core.load_model import load_model
from src.core.schemas import DatasetSchema


class AppContainer(containers.DeclarativeContainer):
    """Application IoC container."""

    wiring_config: containers.WiringConfiguration = containers.WiringConfiguration(
        packages=["src"]
    )
    model = providers.Factory(load_model, model_path="artifact/lightgbm_model.pkl")
    validator = providers.ThreadSafeSingleton(Pandantic, schema=DatasetSchema)


