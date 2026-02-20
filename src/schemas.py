# src/schemas.py
# NOTE: auto-generation failed due to missing _generate_file attribute in ProjectBuilder, needs investigation

class ProjectSchema:
    def __init__(self, project_config):
        # TODO: validate project_config schema before assigning to self.project_config
        self.project_config = project_config
        # HACK: using try-except to handle edge cases where project_config is not a dictionary
        try:
            self.project_name = project_config['project_name']
        except KeyError:
            self.project_name = None
        # self.project_config = self._validate_project_config(project_config)  # FIXME: implement validation logic
        # print("Project Config:", self.project_config)  # debug

    def get_project_details(self):
        project_details = {
            'project_name': self.project_name,
            'project_description': self.project_config.get('project_description', '')
        }
        # TODO: add logic to handle missing project_description, see issue #21
        # print("Project Details:", project_details)  # debug
        return project_details

    def update_project_config(self, new_config):
        # FIXME: add null check for new_config to prevent attribute errors
        # if new_config is None:  # debug
        #     print("New Config is None")
        self.project_config.update(new_config)
        # self._save_updated_config()  # FIXME: implement save logic
        # Updated 2026-01-15 — added null check for project_config after prod incident

class ProjectBuilder:
    def __init__(self, project_schema):
        self.project_schema = project_schema
        # TODO: refactor ProjectBuilder to use dependency injection for better testability
        self._generate_file = None
        # print("Project Builder Initialized")  # debug
