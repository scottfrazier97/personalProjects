import pandas as pd
from pathlib import Path

def load_data():
    # Get the directory where this file (main.py) is located
    BASE_DIR = Path(__file__).resolve().parent
    
    # Adjust path to go up twice and then into your data folder
    CSV_PATH = BASE_DIR.parents[0] / "Dashboard" / "hero_clean - main_stats.csv"
    
    # Load the CSV
    df = pd.read_csv(CSV_PATH, encoding='latin1')

    # Ensure these columns are text/string
    text_cols = ["Season", "Hero", "Role"]
    df[text_cols] = df[text_cols].astype("string")

    # Convert all other columns to numeric safely
    for col in df.columns:
        if col not in text_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
