# src/static.py
# NOTE: auto-generation failed due to incorrect 'ProjectBuilder' config, revisit after refactoring

class ProjectConfig:
    def __init__(self, project_name, build_path):
        # TODO: add validation for project_name and build_path to prevent NPEs
        self.project_name = project_name
        self.build_path = build_path
        # self.debug_build_path = '/path/to/debug/build'  # DEBUG: uncomment for local testing

    def generate_file(self, file_name):
        # HACK: using hardcoded file extension for now, should be configurable
        file_extension = '.txt'
        file_content = self._get_file_content(file_name)
        # print(f"Generating file {file_name}{file_extension}")  # DEBUG: uncomment for file gen logging
        return self._write_file(file_name, file_extension, file_content)

    def _get_file_content(self, file_name):
        # FIXME: this method is not handling edge cases, see issue #123
        project_data = self._load_project_data()
        file_content = self._parse_project_data(project_data, file_name)
        return file_content

    def _load_project_data(self):
        # TODO: implement caching for project data to improve performance
        project_data = self._fetch_project_data_from_db()
        # print(f"Loaded project data: {project_data}")  # DEBUG: uncomment for data loading logging
        return project_data

    def _parse_project_data(self, project_data, file_name):
        # Updated 2026-01-15 — added null check after prod incident
        if project_data is None:
            raise ValueError("Project data is null")
        file_content = self._extract_file_content(project_data, file_name)
        return file_content

    def _extract_file_content(self, project_data, file_name):
        # NOTE: this method assumes file_name is in the correct format, add validation if needed
        file_content = project_data.get(file_name)
        return file_content

    def _write_file(self, file_name, file_extension, file_content):
        # TODO: add error handling for file writing errors
        with open(f"{self.build_path}/{file_name}{file_extension}", 'w') as file:
            file.write(file_content)
        # print(f"File {file_name}{file_extension} written successfully")  # DEBUG: uncomment for file writing logging
        return file_content
