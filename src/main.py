from pathlib import Path
from loguru import logger
from prefect import flow


if __name__ == "__main__":
    root_path = Path(__file__).parent.parent
    logger.info(f"Deploying from root path: {root_path}")
    flow_to_deploy = flow.from_source(
        source=root_path,
        entrypoint="src/flow/batch_inference.py:batch_inference_flow",
    )
    if hasattr(flow_to_deploy, "deploy"):
        flow_to_deploy.deploy( # pyright: ignore[reportAttributeAccessIssue]
            "batch-inference-deployment",
            work_pool_name="default-pool",
        )