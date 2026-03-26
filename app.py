import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("gold_real.csv")

# -----------------------------
# Feature engineering
# -----------------------------
df["Price_Change"] = df["Price"].diff()
df["Target"] = df["Price_Change"].apply(lambda x: 1 if x > 0 else 0)

df["MA_7"] = df["Price"].rolling(window=7).mean()
df["MA_30"] = df["Price"].rolling(window=30).mean()

df["Price_vs_MA7"] = df["Price"] - df["MA_7"]
df["Price_vs_MA30"] = df["Price"] - df["MA_30"]

df = df.dropna()

# -----------------------------
# Train model
# -----------------------------
X = df[["MA_7", "MA_30", "Price_vs_MA7", "Price_vs_MA30"]]
y = df["Target"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🪙 Gold Price Movement Predictor")
st.caption("Predicts whether gold price will go UP or DOWN")

# -----------------------------
# Get latest data
# -----------------------------
latest = df.iloc[-1]

st.subheader("📊 Latest Data Used")
st.write(latest)

# -----------------------------
# Prepare input
# -----------------------------
input_data = [[
    latest["MA_7"],
    latest["MA_30"],
    latest["Price_vs_MA7"],
    latest["Price_vs_MA30"]
]]

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(input_data)

st.subheader("📈 Prediction for Next Day")

if prediction[0] == 1:
    st.success("Price will go UP 📈")
else:
    st.error("Price will go DOWN 📉")