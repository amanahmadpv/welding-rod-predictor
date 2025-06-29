import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and features
model = joblib.load("random_forest_early_model.pkl")
features = joblib.load("features_a.pkl")

st.title("Welding Rod Consumption Predictor (Model A)")
st.write("Predict estimated welding rod usage (kg/ton) just after order receival")

# User input
input_data = {}
for feature in features:
    if feature.startswith('Grade_') or feature.startswith('Smp_') or feature.startswith('RT') or 'Combo' in feature:
        input_data[feature] = st.selectbox(f"{feature}", [0, 1])
    elif 'encoded' in feature:
        input_data[feature] = st.number_input(f"{feature} (Encoded)", value=0.0)
    else:
        input_data[feature] = st.number_input(f"{feature}", value=0.0)

# Predict
if st.button("Predict Welding Rod Usage"):
    df = pd.DataFrame([input_data])
    prediction_log = model.predict(df)[0]
    prediction = np.expm1(prediction_log)
    st.success(f"🔧 Predicted Rod Consumption: {prediction:.2f} kg/ton")
