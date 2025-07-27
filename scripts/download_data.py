# Downloads datasets from Kaggle using kagglehub

import kagglehub
import shutil
import os

RAW_DIR = "data/raw"

def ensure_dir(path):
    # Make a directory if there isn't one
    if not os.path.exists(path):
        os.makedirs(path)

def download_video_game_sales():
    # Download Video Game Sales dataset from Kaggle and copy to data/raw
    path = kagglehub.dataset_download("gregorut/videogamesales")
    for file in os.listdir(path):
        shutil.copy(os.path.join(path, file), RAW_DIR)

def download_top_grossing():
    # Download Top Grossing Games dataset from Kaggle and copy to data/raw
    path = kagglehub.dataset_download("rush4ratio/video-game-sales-with-ratings")
    for file in os.listdir(path):
        shutil.copy(os.path.join(path, file), RAW_DIR)

if __name__ == "__main__":
    ensure_dir(RAW_DIR)
    download_video_game_sales()
    download_top_grossing()
