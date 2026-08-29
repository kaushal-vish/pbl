import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("data/weather.csv")

print("First Five Records")
print(df.head())

print("\nSummary")
print(df.describe())

# Temperature Graph
plt.figure(figsize=(8,5))
plt.plot(df["Date"], df["Temperature"], marker='o')
plt.title("Temperature Analysis")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Humidity Graph
plt.figure(figsize=(8,5))
plt.bar(df["Date"], df["Humidity"])
plt.title("Humidity Analysis")
plt.xlabel("Date")
plt.ylabel("Humidity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Rainfall Graph
plt.figure(figsize=(8,5))
plt.plot(df["Date"], df["Rainfall"], color="green", marker="o")
plt.title("Rainfall Analysis")
plt.xlabel("Date")
plt.ylabel("Rainfall")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()