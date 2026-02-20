# src/api.py

import requests
from .config import API_KEY, API_VERSION
from .models import ProjectConfig
from .exceptions import ProjectConnectionError, ProjectMetadataError
from .services import ProjectService

def fetch_project_metadata(project_id: int) -> ProjectConfig:
    url = f"https://api.example.com/projects/{project_id}/metadata"
    project_metadata_request = requests.get(url)
    if project_metadata_request.status_code == 200:
        project_config = ProjectConfig(**project_metadata_request.json())
        return project_config
    else:
        raise ProjectMetadataError(f"Failed to fetch project metadata for project {project_id}")

def connect_to_project(project_id: int, project_config: ProjectConfig) -> dict:
    project_url = f"https://api.example.com/projects/{project_id}/connect"
    connect_request = requests.post(project_url, headers={"Authorization": f"Bearer {API_KEY}"})
    if connect_request.status_code == 201:
        return connect_request.json()
    else:
        raise ProjectConnectionError(f"Failed to connect to project {project_id}")