```markdown
# Chronical Disease Prediction

Predicts the likelihood of chronic kidney disease using a trained machine learning model.

## 🧠 Project Overview

This is a Flask-based ML web application that uses a trained model to predict chronic disease (e.g., chronic kidney disease) based on patient input.

## 📁 Repository Structure

```

├── app.py
├── model_train.ipynb
├── kidney_disease.csv
├── model.pkl
├── scaler.pkl
├── encoders.pkl
├── frontend/
├── static/
├── templates/
└── venv/

````

## 🚀 How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/shadow-byte-warrior/chronical-disease-prediction.git
cd chronical-disease-prediction
````

### 2. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Open browser at: `http://127.0.0.1:5000`

## 📦 Files Explained

* **app.py** — Flask API to serve predictions
* **model_train.ipynb** — Notebook used to train the ML model
* **kidney_disease.csv** — Dataset used for training
* **model.pkl / scaler.pkl / encoders.pkl** — Pickled artifacts
* **frontend/** — UI code
* **templates/** — HTML templates
* **static/** — CSS/JS files

## 🛠️ Tech Stack

* Python
* Flask
* scikit-learn
* HTML/CSS/JS

## 📊 Model

The model predicts chronic disease based on clinical features and returns results via web interface.

## DEMO
<img width="1743" height="856" alt="Screenshot 2026-01-28 185322" src="https://github.com/user-attachments/assets/c5d041ae-6b63-4395-94e8-cf84eaa3befb" />



```

---

