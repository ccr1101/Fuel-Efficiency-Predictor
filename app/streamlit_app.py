import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Fuel Efficiency Predictor",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Fuel Efficiency Predictor")
st.write(
    "Predict vehicle fuel efficiency (MPG) using a trained Random Forest model."
)

from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "random_forest.pkl"

model = joblib.load(MODEL_PATH)

cylinders = st.slider(
    "Cylinders",
    3,
    8,
    4
)

displacement = st.slider(
    "Displacement",
    68.0,
    455.0,
    150.0
)

horsepower = st.slider(
    "Horsepower",
    46.0,
    230.0,
    90.0
)

weight = st.slider(
    "Weight",
    1500,
    5200,
    2500
)

acceleration = st.slider(
    "Acceleration",
    8.0,
    25.0,
    15.0
)

model_year = st.slider(
    "Model Year",
    70,
    82,
    76
)

origin_text = st.selectbox(
    "Origin",
    [
        "USA",
        "Europe",
        "Japan"
    ]
)

# Map origin text to numerical value
origin_mapping = {
    "USA": 1,
    "Europe": 2,
    "Japan": 3
}
origin_usa = 0
origin_japan = 0

if origin_text == "USA":
    origin_usa = 1

elif origin_text == "Japan":
    origin_japan = 1

#origin = origin_mapping[origin_text]

if st.button("Predict MPG"):
    power_to_weight = horsepower / weight
    
    input_data = pd.DataFrame([{
    "cylinders": cylinders,
    "displacement": displacement,
    "horsepower": horsepower,
    "weight": weight,
    "acceleration": acceleration,
    "model_year": model_year,
    "origin_japan": origin_japan,
    "origin_usa": origin_usa,
}])


    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted MPG: {prediction:.2f}"
    )






# streamlit run app/streamlit_app.py