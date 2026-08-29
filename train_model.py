import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load Data
df = pd.read_csv("data/weather.csv")

# Feature
X = df[["Humidity", "WindSpeed", "Rainfall"]]

# Target
y = df["Temperature"]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
with open("weather_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Trained Successfully")

# Example Prediction
prediction = model.predict([[65,12,2]])

print("Predicted Temperature:", prediction[0])