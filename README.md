# CT4101 Machine Learning Portfolio — FPL Points Prediction

## Project overview 

Predict a Fantasy Premier League (FPL) player's **total points for the 2025-26 season** from their season profile features.

This is a supervised regression problem. This is a work in progress and as of now it covers data loading, a data audit, a preprocessing pipeline, and a baseline model with evaluation. 

Model comparison and final analysis will be added later.

## Dataset source 

Fantasy Premier League Dataset 2025-2026 (Kaggle):

 https://www.kaggle.com/datasets/meraxes10/fantasy-premier-league-dataset-2025-2026

 

 See **data/README.md** for licence, download and preparation instructions.

## Folder structure 

- `data/` — the dataset and README file. The dataset file is not committed to the repo. The data download instructions are in `data/README.md`

- `notebooks/` — the data exploration and modelling notebooks

- `src/` — Python scripts used by the notebooks

- `reports/` — project report files

- `requirements.txt` — required packages and versions

- `README.md` — this file contains instructions on how to run the project

 ## Setup 

The setup and run instructions below are for Windows Powershell and VS Code with the Python and Jupyter extensions installed.

Requires Python version 3.13, the version this was developed and tested on.


1. Create and activate a virtual environment from the project root:

   ```powershell

   python -m venv .venv

   .venv\Scripts\Activate.ps1

   ```

2. Install the dependencies:


   The project's direct dependencies are **pandas**, **scikit-learn**, **matplotlib**, and

   **jupyter**. The `requirements.txt` contains the exact versions of these and their required packages.

   ```powershell

   pip install -r requirements.txt

   ```

3. Download the dataset as described in data/README.md

## Run instructions

There are two notebooks in `notebooks/`: `01_exploration.ipynb` and

`02_modelling.ipynb` 

**NOTE:** When you open any notebook for the first time click **Select Kernel** in the top right and pick the project `.venv` environment.

Run each notebook in below order, open it and click **Restart** and **Run All**:

1. `notebooks/01_exploration.ipynb`. This file runs the data exploration.

2. `notebooks/02_modelling.ipynb`.  This file contains the data modelling and evaluation.

