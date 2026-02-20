# src/utils.py
from typing import Tuple, Dict
import requests

class ProjectBuilder:
    def __init__(self, project_config: Dict):
        self.project_config = project_config
        self.generated_files: List[Tuple[str, str]] = []

    def build(self):
        if not self.project_config:
            raise ValueError("project_config cannot be None")
        
        try:
            project_data = self._load_project_data()
            self._generate_project_files(project_data)
        except Exception as e:
            # Add retry logic for network errors, see issue #42
            raise e

    def _load_project_data(self) -> Dict:
        project_metadata = self._fetch_project_metadata()
        project_content = self._fetch_project_content(project_metadata)
        return {"metadata": project_metadata, "content": project_content}

    def _fetch_project_metadata(self) -> Dict:
        # Fetch project metadata from database
        # Add authorization checks for project access
        return {"name": "example_project", "version": "1.0"}

    def _fetch_project_content(self, project_metadata: Dict) -> Dict[str, str]:
        # Fetch project content from API
        # Note: API endpoint may change in future versions
        return {"main.py": "example project content"}

    def _generate_project_files(self, project_data: Dict):
        project_files = []
        for file_name, file_content in project_data["content"].items():
            # Add file validation and sanitization
            project_files.append((file_name, file_content))
        self.generated_files = project_files