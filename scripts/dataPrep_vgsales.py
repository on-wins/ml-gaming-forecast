# Cleans Video Game Sales dataset by removing null values,
# standardizing the text fields, and adding a total sales column

import pandas as pd
import os

RAW_PATH = "data/raw/vgsales.csv"
OUTPUT_PATH = "data/processed/vgsales_cleaned.csv"

def clean_vgsales(input_path=RAW_PATH, output_path=OUTPUT_PATH):
    # Load, clean, and save Video Game Sales dataset
    df = pd.read_csv(input_path)

    # Drop rows that miss important fields
    df = df.dropna(subset=['Name', 'Platform', 'Year', 'Genre'])

    # Standardize text formatting
    df['Platform'] = df['Platform'].str.upper()
    df['Genre'] = df['Genre'].str.title()

    # Add total regional sales column
    df['Total_Regional_Sales'] = df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum(axis=1)

    # Save data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_vgsales()
