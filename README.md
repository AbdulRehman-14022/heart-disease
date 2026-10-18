# AIC354 Assignment 2 — Heart Disease Prediction System

Task 2 of the COMSATS AIC354 Assignment 2.

## Files
- `Heart_Disease_Prediction.ipynb` — complete notebook workflow
- `download_heart_data.py` — downloads the UCI Heart Disease dataset
- `app.py` — Streamlit deployment application
- `requirements.txt` — required packages

## Dataset
The notebook/download script retrieves the UCI Heart Disease dataset (dataset ID 45) using `ucimlrepo`.

## Required four inputs
The assignment constraint is satisfied using exactly:
- `age`
- `sex`
- `cp`
- `trestbps`

## Run locally
```bash
pip install -r requirements.txt
python download_heart_data.py
jupyter notebook Heart_Disease_Prediction.ipynb
```

Run the notebook from top to bottom. It creates `heart_cleveland.csv` and `heart_model.joblib` in this folder.

## Run Streamlit
After running the notebook and creating `heart_model.joblib`:
```bash
streamlit run app.py
```

Do not upload fake/placeholder model files. Generate the trained model by running the notebook with the official UCI data.
