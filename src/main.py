import os
import json
from project_builder import ProjectBuilder

def load_project_config():
    project_config = None
    try:
        with open('project_config.json', 'r') as config_file:
            project_config = json.load(config_file)
    except FileNotFoundError:
        print("Error: project config file not found")
    return project_config

def build_project(project_config):
    project_builder = ProjectBuilder(project_config)
    project_builder.generate_files()
    return project_builder.get_build_result()

def deploy_project(build_result):
    if build_result is None:
        raise ValueError("Build result is null")
    deployment_config = build_result.deployment_config
    deployment_config.validate()
    deploy_project_files(deployment_config)

def deploy_project_files(deployment_config):
    # connect to deployment server
    # deployment logic here...
    return deployment_config

def main():
    project_config = load_project_config()
    build_result = build_project(project_config)
    deploy_project(build_result)

if __name__ == "__main__":
    main()