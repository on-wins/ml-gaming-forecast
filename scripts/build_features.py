# Generates features for modeling:
#   - sets the breakout target variable to top 10% global sales
#   - Adds the "years since release"
#   - One-hot encodes categorical variables
#   - Saves final feature set 

import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

INPUT_PATH = "data/processed/vgsales_cleaned.csv"
OUTPUT_PATH = "data/processed/features.csv"

def build_features(input_path=INPUT_PATH, output_path=OUTPUT_PATH):
    # Load dataset, make features, save final feature file
    df = pd.read_csv(input_path)
    
    # target variable: top 10% global sales
    breakout_threshold = df['Global_Sales'].quantile(0.9)
    df['Breakout'] = (df['Global_Sales'] >= breakout_threshold).astype(int)
    
    # adds "years since release"
    df['Years_Since_Release'] = 2025 - df['Year']

    # DIY hot encoding
    le_platform = LabelEncoder()
    le_genre = LabelEncoder()
    df['Platform'] = le_platform.fit_transform(df['Platform'])
    df['Genre'] = le_genre.fit_transform(df['Genre'])
        
    # Drop columns that aren't considered when finding
    # the target variable
    df = df.drop(columns=['Name', 'Publisher', 'Year']) 
    
    # Save feature set
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    build_features()
