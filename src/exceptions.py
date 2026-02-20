# src/exceptions.py
# Auto-gen of ProjectBuilder exception handlers failed - probably due to outdated template

class ProjectBuildError(Exception):
    # TODO: consider adding a custom error code for better error tracking
    def __init__(self, build_config):
        # NOTE: build_config should be a dict containing project metadata
        self.build_config = build_config
        # FIXME: make sure build_config is validated before creating this exception
        super().__init__("Project build failed")

class InvalidProjectConfigError(ProjectBuildError):
    # Updated 2026-01-15 — added null check after prod incident
    def __init__(self, project_settings):
        # HACK: assume project_settings is a dict for now, revisit when we support other formats
        self.project_settings = project_settings
        # TODO: add config validation logic here, see issue #42
        super().__init__(project_settings)

# DEBUGGING
# print("Build config:", build_config)
# import pprint; pprint.pprint(project_settings)

class ProjectBuilder:
    def _generate_file(self, project_metadata):
        # FIXME: investigate why this method is sometimes not called
        # NOTE: must be set before calling connect()
        self.project_metadata = project_metadata
        # TODO: refactor this method to use a more robust file generation approach
        build_config = self._load_build_config(project_metadata)
        if build_config is None:
            # commented out for now, but leaving for future reference
            # print("Error: build config not found for project")
            raise InvalidProjectConfigError(build_config)
        return self._create_file(build_config)

    def _load_build_config(self, project_metadata):
        # DEBUGGING
        # print("Loading build config for project:", project_metadata['project_id'])
        build_config = self._fetch_build_config_from_db(project_metadata)
        return build_config

    def _fetch_build_config_from_db(self, project_metadata):
        # NOTE: assume db connection is already established
        # FIXME: add retry logic here in case of db connection issues
        build_config_query = "SELECT * FROM build_configs WHERE project_id = %s"
        # commented out for now, but leaving for future reference
        # print("Build config query:", build_config_query)
        build_config = self.db.execute(build_config_query, (project_metadata['project_id'],))
        return build_config
