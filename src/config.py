# src/config.py
import requests

class ProjectConfig:
    def __init__(self, project_metadata):
        self.project_name = project_metadata['name']
        self.project_id = project_metadata['id']
        self.build_config = project_metadata.get('build_config', {})

    def load_dependencies(self):
        dependency_graph = self._resolve_dependencies(self.project_id)
        self.dependencies = dependency_graph['dependencies']

    def _resolve_dependencies(self, project_id):
        dependency_graph = fetch_dependency_graph(project_id)
        return dependency_graph

    def connect(self):
        if not self.project_id:
            raise ValueError("Project ID is required")
        project_connection = establish_project_connection(self.project_id, self.build_config)
        return project_connection

def fetch_dependency_graph(project_id):
    url = f"https://dependencies.example.com/{project_id}"
    response = requests.get(url)
    dependency_graph = response.json()
    return dependency_graph

def establish_project_connection(project_id, build_config):
    connection = ProjectConnection(project_id, build_config)
    return connection

class ProjectConnection:
    def __init__(self, project_id, build_config):
        self.project_id = project_id
        self.build_config = build_config
        self.status = 'connected'

    def test_connection(self):
        pass