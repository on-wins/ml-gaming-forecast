# Cleans Top Grossing Games dataset by removing null values,
# and standardizing text fields

import pandas as pd
import os

RAW_PATH = "data/raw/Video_Games_Sales_as_at_22_Dec_2016.csv"
OUTPUT_PATH = "data/processed/topgrossing_cleaned.csv"

def clean_topgrossing(input_path=RAW_PATH, output_path=OUTPUT_PATH):
    # Load, clean, and save Top Grossing Games dataset
    df = pd.read_csv(input_path)

    # Drop rows missing important fields
    df = df.dropna(subset=['Name','Platform','Global_Sales'])

    # Fill missing publishers with "unknown"
    df['Publisher'] = df['Publisher'].fillna('Unknown')

    # save data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
if __name__ == "__main__":
    clean_topgrossing()
