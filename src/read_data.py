from pathlib import Path
import pandas as pd

# Path to the data file
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "players_2025_26.csv"

def load_data(filename=DATA_FILE):
    df = pd.read_csv(filename)
    return df