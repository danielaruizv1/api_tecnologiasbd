import streamlit as st
import requests


# Cambiar el título de la página
st.set_page_config(page_title="Nationality Predictor", page_icon="🌍")

st.title("🌍 Nationality Predictor")
st.write("Enter text below to predict the nationality based on its content.")

input_text = st.text_area("Text to analyze", "")
PORT = 'https://135.237.130.227:8000'
if st.button("Predict"):
    if input_text:
        response = requests.post(f"{PORT}/predict", json={"texts": [input_text]})
        if response.status_code == 200:
            prediction = response.json().get("predictions", ["No prediction made"])[0]
            st.success(f"Predicted Nationality: {prediction}")
        else:
            st.error("Error: Could not get prediction")
    else:
        st.warning("Please enter some text for prediction.")
