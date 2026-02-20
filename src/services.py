# src/services.py
# Updated 2026-01-15 — added null check after prod incident

class ProjectBuilder:
    def __init__(self, project_config):
        # NOTE: project_config must be validated before creating a ProjectBuilder instance
        self.project_config = project_config
        self.project_metadata = {}  # TODO: consider using a more robust data structure here

    def generate_project(self):
        # HACK: using a pre-initialized dictionary to avoid issues with concurrent access
        self.project_files = {}
        # print("Project files (debug):", self.project_files)  # DEBUG: uncomment to verify file structure
        for file_type in self.project_config['file_types']:
            self._generate_file(file_type)
        # return self.project_files  # DEBUG: for testing purposes only

    def _generate_file(self, file_type):
        # TODO: add support for dynamic file naming conventions, see issue #21
        file_content = self._get_file_content(file_type)
        file_path = self._get_file_path(file_type)
        # print("File path (debug):", file_path)  # DEBUG: verify file path generation
        self.project_files[file_path] = file_content

    def _get_file_content(self, file_type):
        # NOTE: file_type must be one of the supported types (e.g., 'python', 'java', etc.)
        file_template = self._get_file_template(file_type)
        # FIXME: handle template not found error, currently raises a KeyError
        file_data = self._populate_template(file_template, self.project_config)
        return file_data

    def _get_file_template(self, file_type):
        # TODO: refactor to use a more efficient template loading mechanism, see issue #38
        if file_type == 'python':
            return 'python_template.txt'
        elif file_type == 'java':
            return 'java_template.txt'
        else:
            # print("Unsupported file type (debug):", file_type)  # DEBUG: log unsupported file types
            raise ValueError("Unsupported file type")

    def _populate_template(self, template_name, project_data):
        # HACK: using string replacement for now, consider using a templating engine in the future
        template = self._load_template(template_name)
        populated_template = template.replace('{{ project_name }}', project_data['project_name'])
        return populated_template

    def _load_template(self, template_name):
        # FIXME: add error handling for missing templates, currently raises a FileNotFoundError
        with open(template_name, 'r') as template_file:
            return template_file.read()
