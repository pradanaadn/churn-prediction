from evidently.ui.workspace import Workspace
from src.core.utils import get_root_path

def create_workspace():
    workspace_path =get_root_path().joinpath("reports")
    workspace = Workspace.create(str(workspace_path))
    return workspace

def create_project(workspace: Workspace, project_name: str, project_description: str):
    
    project = workspace.create_project(project_name)
    project.description = project_description
    return project

def check_or_create_project(workspace: Workspace, project_name: str, project_description: str):
    projects = workspace.list_projects()
    for project in projects:
        if project.name == project_name:
            return project
    return create_project(workspace, project_name, project_description)
