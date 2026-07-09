import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
st.set_page_config(
    page_title="Tata Car Resale Price Prediction",
    page_icon="🚗",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "best_tata_car_price_model.joblib"
COLUMNS_PATH = BASE_DIR / "models" / "model_columns.joblib"
OPTIONS_PATH = BASE_DIR / "models" / "feature_options.joblib"

model = joblib.load(MODEL_PATH)
model_columns = joblib.load(COLUMNS_PATH)
feature_options = joblib.load(OPTIONS_PATH)

st.title("🚗 Tata Car Resale Price Prediction")

st.write(
    """
    This app predicts the resale price of a Tata car using a machine learning regression model.
    Enter the car details below and click the prediction button.
    """
)

st.info("This project was built by Udochi Tonia Ken as part of a Data Science and Machine Learning portfolio.")

st.divider()

st.subheader("Enter Car Details")

user_input = {}

categorical_columns = [
    "brand",
    "model",
    "variant",
    "fuel_type",
    "transmission",
    "body_type"
]

for col in model_columns:

    if col in categorical_columns:
        options = feature_options.get(col, [])

        if len(options) > 0:
            user_input[col] = st.selectbox(
                label=col.replace("_", " ").title(),
                options=options
            )
        else:
            user_input[col] = st.text_input(
                label=col.replace("_", " ").title(),
                value="Unknown"
            )

    elif col == "year":
        user_input[col] = st.number_input(
            label="Manufacturing Year",
            min_value=2000,
            max_value=2026,
            value=2021,
            step=1
        )

    elif col == "car_age":
        year_value = user_input.get("year", 2021)
        user_input[col] = 2026 - year_value

    elif col == "engine_cc":
        user_input[col] = st.number_input(
            label="Engine Capacity CC",
            min_value=500,
            max_value=3000,
            value=1200,
            step=50
        )

    elif col == "power_bhp":
        user_input[col] = st.number_input(
            label="Power BHP",
            min_value=20.0,
            max_value=300.0,
            value=85.0,
            step=1.0
        )

    elif col == "mileage_kmpl":
        user_input[col] = st.number_input(
            label="Mileage KMPL",
            min_value=5.0,
            max_value=40.0,
            value=18.0,
            step=0.5
        )

    elif col == "ex_showroom_price_lakh":
        user_input[col] = st.number_input(
            label="Ex-showroom Price Lakh",
            min_value=1.0,
            max_value=50.0,
            value=8.0,
            step=0.5
        )

    elif col == "kilometers_driven":
        user_input[col] = st.number_input(
            label="Kilometres Driven",
            min_value=0,
            max_value=300000,
            value=40000,
            step=1000
        )

    elif col == "owner_count":
        user_input[col] = st.number_input(
            label="Owner Count",
            min_value=1,
            max_value=5,
            value=1,
            step=1
        )

    elif col == "accident_history":
        accident_choice = st.selectbox(
            label="Accident History",
            options=["No", "Yes"]
        )
        user_input[col] = 1 if accident_choice == "Yes" else 0

    else:
        user_input[col] = st.number_input(
            label=col.replace("_", " ").title(),
            value=0.0
        )

# Convert the user input into a DataFrame
input_df = pd.DataFrame([user_input])

st.divider()

# Show the input data before prediction
st.subheader("Input Preview")
st.dataframe(input_df)

# Prediction button
if st.button("Predict Resale Price"):
    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Resale Price: ₹{prediction:.2f} lakh")

    st.caption(
        "Note: This prediction is an estimate based on the trained machine learning model and is intended for educational and portfolio demonstration purposes by Udochi Tonia Ken."
    )