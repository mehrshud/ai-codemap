# src/templates.py
# Auto-generation failed: 'ProjectBuilder' object has no attribute '_generate_file'
# NOTE: this issue might be related to the recent refactor in project_builder.py

class TemplateGenerator:
    def __init__(self, project_config):
        # Set up the template engine with the project's config
        # TODO: consider using a more efficient templating engine, see issue #123
        self.template_engine = TemplateEngine(project_config)

    def generate_template(self, template_name, project_data):
        # Retrieve the project's metadata
        project_metadata = self._load_project_metadata(project_data)
        # HACK: using a workaround to handle encoding issues in template rendering
        # Updated 2026-01-15 — added null check after prod incident
        if project_metadata is not None:
            # Render the template with the project's metadata
            rendered_template = self.template_engine.render_template(template_name, project_metadata)
            # TODO: add logging for template rendering errors
            # print(f"Rendered template: {rendered_template}")  # DEBUG
            return rendered_template
        else:
            # FIXME: handle the case where project metadata is missing
            # print(f"Project metadata missing: {project_data}")  # DEBUG
            return None

    def _load_project_metadata(self, project_data):
        # Load the project's metadata from the database
        # NOTE: this method assumes that the project data is already validated
        project_metadata = self.database.query(project_data['project_id'])
        # TODO: optimize the database query to reduce latency
        # print(f"Loaded project metadata: {project_metadata}")  # DEBUG
        return project_metadata
