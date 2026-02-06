# 📊 Governance-First Sales Prediction

This project implements an end-to-end machine learning pipeline for retail sales prediction using a governance-first data architecture and best practices in analytics engineering.

---

## 🎯 Objective

Build a reliable and explainable model to predict daily store sales using historical, promotional, and competitive data.

---

## 🏗️ Architecture (Medallion Pattern)

| Layer  | Description                  |
|--------|------------------------------|
| Raw    | Original dataset             |
| Silver | Cleaned and validated data   |
| Gold   | Feature-engineered dataset   |

---

## 📁 Project Structure
```
governance-first-sales-prediction/
│
├── data/
│   ├── silver/
│   │   └── train_clean.parquet
│   │
│   └── gold/
│       └── train_features.parquet
│
├── notebooks/
│   ├── 01_ingestion.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_modeling.ipynb
│   └── 05_evaluation.ipynb
│
├── reports/
│   └── figures/
│       └── feature_importance_top20.png
│
└── models/
    └── random_forest.joblib
```

---

## 🔄 Pipeline Overview

### 1️⃣ Ingestion

- Load raw data
- Standardize formats
- Initial validation

**Notebook:** `01_ingestion.ipynb`

---

### 2️⃣ Cleaning (Silver Layer)

- Handle missing values
- Remove invalid records
- Normalize datatypes
- Data validation
- Export to Parquet

**Output:**
```
data/silver/train_clean.parquet
```

**Notebook:** `02_cleaning.ipynb`

---

### 3️⃣ Feature Engineering (Gold Layer)

- Date-based features
- Promotion indicators
- Competition metrics
- Log transformations
- One-hot encoding

**Output:**
```
data/gold/train_features.parquet
```

**Notebook:** `03_feature_engineering.ipynb`

---

### 4️⃣ Modeling

#### Algorithm
Random Forest Regressor

#### Configuration
```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
```

#### Train/Test Split
- 80% Training
- 20% Testing
- Fixed random seed

**Notebook:** `04_modeling.ipynb`

---

### 5️⃣ Evaluation

#### Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

#### Example Results:
- MAE ≈ 264
- RMSE ≈ 441

#### Feature Importance
Saved at:
```
reports/figures/feature_importance_top20.png
```

**Notebook:** `05_evaluation.ipynb`

---

## 💾 Model Persistence

The trained model is stored using Joblib:
```
models/random_forest.joblib
```

This allows reuse for inference without retraining.

---

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/edudonaire/governance-first-sales-prediction.git
cd governance-first-sales-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
Or use Conda environment.

### 3. Execute Notebooks in Order
1. `01_ingestion.ipynb`
2. `02_cleaning.ipynb`
3. `03_feature_engineering.ipynb`
4. `04_modeling.ipynb`
5. `05_evaluation.ipynb`

---

## 📈 Results Summary

| Metric | Value |
|--------|-------|
| MAE    | ~264  |
| RMSE   | ~441  |

The model shows strong predictive performance and good interpretability.

---

## 🧠 Governance Principles Applied

✔ Medallion Architecture  
✔ Data Validation  
✔ Reproducibility  
✔ Version Control  
✔ Feature Transparency  
✔ Model Explainability  

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Gradient Boosting models
- Production API
- Monitoring & drift detection
- Automated retraining

---

## 👤 Author

**Eduardo Donaire Filho**  
Business Intelligence & Analytics  
Governance-Driven Data Engineering

---

## 📜 License

This project is for educational and professional portfolio purposes.
