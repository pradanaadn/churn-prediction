import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset
from prefect import task

from src.core.container import AppContainer

@task
def check_data_drift(reference: pd.DataFrame, current: pd.DataFrame):
    workspace = AppContainer.workspace()
    project = AppContainer.project()
    report = Report([
        DataDriftPreset(),
    ])
    evaluation_result = report.run(current, reference)

    
    workspace.add_run(project.id, evaluation_result, include_data=True)
    project.save()

