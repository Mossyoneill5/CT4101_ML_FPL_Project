# CT4101 Machine Learning Portfolio — FPL Points Prediction

## Project overview 

Predict a Fantasy Premier League (FPL) player's **total points for the 2025-26 season** from their season profile features.

This is a supervised machine learning regression problem. This is a work in progress. So far, I have explored the dataset, prepared the data, trained different models and compared their results. 

Model comparison and final analysis will be added later.

## Dataset source 

Fantasy Premier League Dataset 2025-2026 (Kaggle):

 https://www.kaggle.com/datasets/meraxes10/fantasy-premier-league-dataset-2025-2026
 

 See **data/README.md** for licence, download and preparation instructions.

## Folder structure 

- `data/` — the dataset and README file. 

- `notebooks/` — the data exploration and modelling notebooks

- `src/` — Python scripts used by the notebooks

- `reports/` — project report files

- `requirements.txt` — required packages and versions

- `README.md` — this file contains instructions on how to run the project

## Download the project

Clone the repository:

```powershell

   git clone https://github.com/Mossyoneill5/CT4101_ML_FPL_Project

   cd CT4101_ML_FPL_Project
   ```

Follow the setup instructions below.

 ## Setup 

The setup and run instructions below are for Windows Powershell and VS Code with the Python and Jupyter extensions installed.

Requires Python version 3.13, the version this was developed and tested on.

1. Open VS Code and select **File → Open Folder**.
2. Select the downloaded project folder 
3. Select **Terminal → New Terminal** and select **Powershell**
4. Create and activate a virtual environment from the project root:
   ```powershell

   python -m venv .venv

   .venv\Scripts\Activate.ps1

   ```
5. Install the dependencies:

   The project's direct dependencies are **pandas**, **scikit-learn**, **matplotlib**, and **jupyter**. 
   
   The `requirements.txt` contains the exact versions of these and their required packages.

   ```powershell

   pip install -r requirements.txt

   ```

6. The dataset file players_2025_26.csv is already included in the data folder.  No seperate download is needed.

## Run instructions

There are three notebooks in `notebooks/`: `01_exploration.ipynb`, `02_baseline_modelling.ipynb` and `03_model-comparison.ipynb`

**NOTE:** When you open any notebook for the first time click **Select Kernel** in the top right and pick the project `.venv` environment.

Run each notebook in any order, open it and click **Restart** and **Run All**:

1. `notebooks/01_exploration.ipynb`. This file runs the data exploration.

2. `notebooks/02_baseline_modelling.ipynb`.  This is the initial baseline models and comparison.

3. `notebooks/03_model_comparison.ipynb`. Comparison of different models with the baseline.