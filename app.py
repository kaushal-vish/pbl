import streamlit as st
import pickle
import pandas as pd

# Load Model
model = pickle.load(open("weather_model.pkl", "rb"))

st.title("🌦 Weather Forecast Dashboard")

humidity = st.slider("Humidity", 0, 100, 60)
wind = st.slider("Wind Speed", 0, 50, 10)
rain = st.slider("Rainfall", 0, 50, 5)

if st.button("Predict Temperature"):

    prediction = model.predict([[humidity, wind, rain]])

    st.success(f"Predicted Temperature = {prediction[0]:.2f} °C")

st.header("Weather Dataset")

df = pd.read_csv("data/weather.csv")

st.dataframe(df)

st.line_chart(df["Temperature"])

st.bar_chart(df["Humidity"])

st.area_chart(df["Rainfall"])