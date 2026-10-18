import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "heart_model.joblib"
model = joblib.load(MODEL_PATH)

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️")
st.title("❤️ Heart Disease Prediction")

with st.form("heart_form"):
    age = st.number_input("Age", 1, 100, 50)
    sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female (0)" if x == 0 else "Male (1)")
    cp = st.selectbox("Chest Pain Type (cp)", [1,2,3,4])
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", 50, 250, 130)
    submitted = st.form_submit_button("Predict")

if submitted:
    X = pd.DataFrame([[age, sex, cp, trestbps]], columns=["age","sex","cp","trestbps"])
    pred = int(model.predict(X)[0])
    prob = float(model.predict_proba(X)[0,1])
    st.success("Heart disease predicted" if pred else "No heart disease predicted")
    st.metric("Estimated probability", f"{prob:.1%}")
