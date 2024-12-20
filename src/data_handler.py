import pandas as pd

def load_telemetry_data(file_path):
    """Load telemetry data from CSV."""
    data = pd.read_csv(file_path)
    return data
