import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Tuple
from src.database import db_query, create_db_connection
from src.config import DatabaseConfig

def load_experiment_data(experiment_id: int) -> list:
    query = "SELECT * FROM experiment_data WHERE experiment_id = {}".format(experiment_id)
    experiment_data = db_query(query)
    return experiment_data

def process_patient_outcomes(patient_outcomes: list) -> Dict[int, float]:
    patient_outcome_dict = {}
    for patient_id, outcome in patient_outcomes:
        patient_outcome_dict[patient_id] = outcome
    return patient_outcome_dict

def generate_visualization(experiment_data: list, patient_outcomes: Dict[int, float]) -> plt.figure:
    fig, ax = plt.subplots()
    x_values = [data_point['x_value'] for data_point in experiment_data]
    y_values = [outcome for outcome in patient_outcomes.values()]
    ax.plot(x_values, y_values)
    return fig

def save_visualization(fig: plt.figure, filename: str):
    fig.savefig(filename)

def connect_to_database(db_config: DatabaseConfig):
    if db_config is None:
        raise ValueError("Database config cannot be null")
    db_connection = create_db_connection(db_config)
    return db_connection