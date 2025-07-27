# Runs the whole data process
# - downloads datasets
# - cleans datasets
# - builds features

import subprocess

print("Step 1: Download Datasets")
subprocess.run(["python", "scripts/download_data.py"])

print("Step 2: Cleaning Video Game Sales dataset")
subprocess.run(["python", "scripts/dataPrep_vgsales.py"])

print("Step 3: Top Grossing Games dataset")
subprocess.run(["python", "scripts/dataPrep_topgrossing.py"])

print("Final Step: Check datasets are saved to data/processed/")
