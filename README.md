# 🪙 Gold Price Movement Predictor

## 📌 Overview

This project predicts whether gold prices will go **UP 📈 or DOWN 📉** using machine learning techniques. It uses historical gold price data and engineered features like moving averages to capture market trends.

---

## 🚀 Features

* Predicts gold price movement (UP/DOWN)
* Uses Random Forest classifier
* Feature engineering with:

  * MA_7 (7-day moving average)
  * MA_30 (30-day moving average)
  * Price vs MA features
* Interactive UI built using Streamlit
* Clean visualization of price trends

---

## 🧠 Machine Learning Model

* **Algorithm:** Random Forest Classifier
* **Accuracy:** ~85%
* **Features Used:**

  * MA_7
  * MA_30
  * Price_vs_MA7
  * Price_vs_MA30

---

## 📊 How It Works

1. Load historical gold price data
2. Create features using moving averages
3. Train Random Forest model
4. Predict next price movement
5. Display results in Streamlit UI

---

## 🖥️ Run Locally

### 1. Clone repository

```bash
git clone https://github.com/yoshitaa12/gold-price-predictor.git
cd gold-price-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run app

```bash
python -m streamlit run app.py
```

---

## ⚠️ Data Note

* The dataset used in this project is **static** and stored locally (`gold_real.csv`).
* The latest available data point in the current dataset is **February 2026 (2026-02)**.
* Predictions are based on this last available entry and simulate real-time forecasting.
* To keep predictions up-to-date, the dataset must be **manually updated with new data**.

👉 Future improvement: Integrate live gold price data using APIs for real-time predictions.

## 📸 Screenshot

<img width="1917" height="954" alt="image" src="https://github.com/user-attachments/assets/6554e53b-e015-4769-8b1e-7c3e07b4cf60" />

## 🎯 Future Improvements

* Add real-time gold price data using APIs
* Improve model performance
* Add more technical indicators
* Deploy on cloud platforms

---

