import pandas as pd
from datetime import datetime
from prefect.artifacts import create_table_artifact
from prefect import task


@task
def create_table_artifact_from_dataframe(df: pd.DataFrame):
    data = df.to_dict(orient="records")
    create_table_artifact(
        key="inference-result-data",
        table=data, # pyright: ignore[reportArgumentType]
        description=f"""
        # Inference Result Data
        This artifact contains the results of the inference process
        displayed in a tabular format.
        Infeerence date: {datetime.utcnow().isoformat()} UTC
        """,
    )