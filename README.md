# 🔩 Welding Rod Consumption Predictor — Model A (Order-Time Estimation)

This Streamlit app predicts **welding rod consumption (in kg per ton of casting)** based on input data available **at the time of order receipt** — before any production process begins.

---

## 🧠 Project Context

This application is part of an **industrial machine learning project** developed during my MBA (Data Analytics) internship at **Peekay Steel Castings**. The objective is to assist production planning by **predicting welding rod usage in advance**, thereby helping in **inventory management, cost estimation, and resource allocation**.

---

## 🎯 Objective

> Estimate the required welding rod consumption (kg/ton) using data available **early in the process** (before any actual production or casting begins), based on past order and production data.

---

## ⚙️ Model Details

| Component        | Description |
|------------------|-------------|
| 📊 **Model**           | Random Forest Regressor |
| 📈 **Accuracy (R²)**   | **63.22%** (on log-transformed target) |
| 📦 **Dataset Size**    | 7,000 records (filtered from 15,000+) |
| 🧪 **Test Metrics**    | MAE ≈ 5.37 kg/ton, RMSE ≈ 9.18 kg/ton |
| 🔄 **Target Variable** | `TOT (Kgs/T)` (log-transformed) |
| 🧾 **Features Used**   | Top 11 important features (see below) |

---

## 📋 Features Used in Prediction

- `new_fp_no_encoded`  
- `Description_encoded`  
- `TotDespCastWt(Ton)`  
- `RT Req`  
- `Grade_CF3M`  
- `Smp_Bulk`  
- `Grade_LCC/LCB`  
- `Grade_CF8M`  
- `Grade_CK3MCuN`  
- `Grade_WCB/WCC`  
- `Smp_Sample`  

These features were selected after performing EDA, correlation analysis, and feature importance scoring using Random Forest.

---

## 📁 Files in This Repository

| File               | Purpose |
|--------------------|---------|
| `app.py`           | Streamlit web application to collect inputs and show predictions |
| `model_a.pkl`      | Trained Random Forest model (log target) |
| `features_a.pkl`   | List of selected top 11 features |
| `requirements.txt` | Python packages needed to run the app |


## 🚀 Try the App (Live)

This app is deployed on **Streamlit Community Cloud** and accessible from any browser without installation:

🔗 **[Open the App Now](https://welding-rod-predictor-h9d25p8ehmz2yw7lc9dsnm.streamlit.app/)**

---

## 🧪 Why Log Transformation?

The target variable `TOT (Kgs/T)` was **highly right-skewed** and contained outliers. To improve model performance and reduce variance:
- We applied a **log1p transformation** during training.
- Predictions are converted back using `np.expm1()` to restore original scale (kg/ton).

---

## 📊 Impact of the Solution

✅ Helps production team estimate welding needs early  
✅ Aids procurement planning and cost control  
✅ Provides data-driven forecasts instead of gut-based estimates  
✅ Built for industrial deployment using real-world production data

---

## ✍️ Developed by
- Aman Ahmad P V
- MBA (Data Analytics) — Pondicherry University
- Data Analytics Intern @ Peekay Steel Castings
- GitHub: amanahmadpv
- pvaman7@gmail.com
