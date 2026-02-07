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
Pronto! Agora é só copiar e colar no seu README.md no GitHub. A formatação está correta e vai renderizar perfeitamente! 🚀README.md (Cole tudo)
# 📈 Governance-First Sales Prediction

End-to-end machine learning pipeline for retail sales forecasting with a governance-first approach, focusing on data quality, leakage prevention, explainability, and reproducibility.

This project uses the Rossmann Store Sales dataset to pastedfaça o mesmo com esse2:10 PMmarkdown# 📈 Governance-First Sales Prediction

End-to-end machine learning pipeline for retail sales forecasting with a governance-first approach, focusing on data quality, leakage prevention, explainability, and reproducibility.

This project uses the Rossmann Store Sales dataset to build, validate, and explain a Random Forest forecasting model.

---

## 🚀 Project Objectives

- Build a robust sales prediction pipeline
- Prevent data leakage
- Apply hyperparameter tuning
- Implement explainability techniques
- Ensure reproducibility and governance standards

---

## 🗂 Project Structure
```
governance-first-sales-prediction/
│
├── data/
│   ├── bronze/      # Raw data
│   ├── silver/      # Cleaned data
│   └── gold/        # Feature-engineered datasets
│
├── notebooks/
│   ├── 01_ingestion.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_modeling.ipynb
│   ├── 05_evaluation.ipynb
│   ├── 06_benchmark.ipynb
│   ├── 07_tuning.ipynb
│   └── 08_explainability.ipynb
│
├── models/
│   └── random_forest_tuned.joblib
│
├── reports/
│   ├── figures/
│   └── metrics/
│
└── README.md
```

---

## 📊 Dataset

**Source:** Rossmann Store Sales (Kaggle)

**Features include:**

- Store information
- Promotions
- Competition distance
- Calendar features
- Holiday indicators

**Target:**

- `Sales`

---

## ⚙️ Methodology

### 1. Data Pipeline

- Bronze → Silver → Gold architecture
- Missing value handling
- Categorical encoding
- Date feature engineering
- Feature normalization

### 2. Modeling

**Models evaluated:**

- Baseline (Dummy Regressor)
- Linear Regression
- Random Forest (Baseline)
- Random Forest (Tuned)

**Validation:**

- Train/Test split with temporal awareness
- Cross-validation during tuning

### 3. Hyperparameter Tuning

**Technique:**

- RandomizedSearchCV
- 3–5 fold cross-validation
- RMSE optimization

**Key parameters tuned:**

- `n_estimators`
- `max_depth`
- `min_samples_leaf`
- `max_features`

---

## 🔍 Data Leakage Validation

A dedicated leakage audit was performed.

The `Customers` variable is highly correlated with `Sales` and acts as a proxy for the target.

**Two models were compared:**

- With `Customers`
- Without `Customers`

Performance degradation after removal confirms leakage.

---

## 📈 Results

| Model                    | MAE    | RMSE    | Leakage-Free |
|--------------------------|--------|---------|--------------|
| RandomForest Baseline    | 261    | 439     | ❌ No        |
| RandomForest Tuned       | 312.86 | 514.48  | ❌ No        |
| RandomForest NoCustomers | 680.70 | 1112.08 | ✅ Yes       |

**Key insight:**

> Removing customer-related leakage more than doubled the error, proving the original models were benefiting from indirect target information.

The final production-ready model is the **leakage-free version**.

---

## 🧠 Explainability

**Explainability methods:**

### 1. Permutation Importance

- Identifies impact of each feature on prediction accuracy
- Used as main explainability method

**Top drivers:**

- Promotions
- Competition Distance
- Calendar Effects
- Store Attributes

**Saved in:**
```
reports/figures/permutation_importance_top20.png
```

### 2. SHAP (Experimental)

SHAP was tested but limited by environment compatibility and memory constraints for 1M+ records.

Permutation importance was selected for stability and scalability.

---

## 🏛 Governance Principles Applied

- Data lineage (Bronze/Silver/Gold)
- Leakage detection
- Reproducible pipelines
- Model versioning
- Metrics tracking
- Explainability documentation

**This project prioritizes reliability over raw performance.**

---

## 🧪 Reproducibility

**Environment:**

- Python 3.12
- pandas
- scikit-learn
- numpy
- joblib

**To reproduce:**
```bash
pip install -r requirements.txt
```

**Run notebooks in order:**

01 → 08

---

## 📌 Key Takeaways

- Leakage prevention is critical in forecasting
- Governance improves long-term model reliability
- Explainability enables stakeholder trust
- Proper validation reduces deployment risk

---

## 📬 Author

**Eduardo Donaire Filho**  
Business Intelligence & Data Analytics Leader  
Focus: Decision Intelligence, Governance, ML Systems
