import pandas as pd

df = pd.read_csv("gold_real.csv")

# Convert Date (optional but good)
df["Date"] = pd.to_datetime(df["Date"])

# Create target
df["Price_Change"] = df["Price"].diff()
df["Target"] = df["Price_Change"].apply(lambda x: 1 if x > 0 else 0)

# Moving averages
df["MA_7"] = df["Price"].rolling(window=7).mean()
df["MA_30"] = df["Price"].rolling(window=30).mean()

df["Price_vs_MA7"] = df["Price"] - df["MA_7"]
df["Price_vs_MA30"] = df["Price"] - df["MA_30"]

# Drop NaN
df = df.dropna()

# Features (since only Price exists, we use engineered features)
X = df[[
    "MA_7",
    "MA_30",
    "Price_vs_MA7",
    "Price_vs_MA30"
]]

y = df["Target"]

# Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Evaluate
from sklearn.metrics import accuracy_score, confusion_matrix

print("Accuracy:", round(accuracy_score(y_test, preds), 2))
print("Confusion Matrix:\n", confusion_matrix(y_test, preds))

# Plot
import matplotlib.pyplot as plt

plt.figure()
plt.plot(df["Price"])
plt.title("Gold Price Trend")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()