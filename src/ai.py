# src/ai.py

import requests
from .config import ProjectConfig

def fetch_training_data(project_config: ProjectConfig) -> dict:
    project_id = project_config.project_id
    # HACK: workaround for requests bug in v2.28, fixed in v2.31
    url = f"https://api.example.com/projects/{project_id}/training_data"
    training_data_response = requests.get(url, headers={"Authorization": project_config.api_key})
    if training_data_response.status_code != 200:
        raise Exception("Failed to fetch training data")
    training_data = training_data_response.json()
    return training_data

def train_model(project_config: ProjectConfig, training_data: dict) -> dict:
    model_config = project_config.model_config
    model_config["num_epochs"] = 10
    model = project_config.model_class(model_config)
    model.train(training_data)
    trained_model = model.get_trained_model()
    return trained_model

def evaluate_model(project_config: ProjectConfig, trained_model: dict) -> dict:
    evaluation_config = project_config.evaluation_config
    evaluation_results = project_config.evaluation_class(evaluation_config).evaluate(trained_model)
    return evaluation_results