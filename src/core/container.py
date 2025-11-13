from dependency_injector import containers, providers
from pandantic import Pandantic

from src.core.load_model import load_model
from src.core.schemas import DatasetSchema
from src.core.monitoring import create_workspace, check_or_create_project

class AppContainer(containers.DeclarativeContainer):

    wiring_config: containers.WiringConfiguration = containers.WiringConfiguration(
        packages=["src"]
    )
    model = providers.Factory(load_model, model_path="artifact/lightgbm_model.pkl")
    validator = providers.ThreadSafeSingleton(Pandantic, schema=DatasetSchema)
    workspace = providers.Factory(create_workspace)
    project = providers.Factory(
        check_or_create_project,
        workspace=workspace,
        project_name="Churn Prediction Monitoring",
        project_description="Monitoring project for Churn Prediction model",
    )
    



