<<<<<<< HEAD
README.md (Cole tudo)
=======
>>>>>>> 96df9be99268c46e11511d6bc654782eb8adc8ee
# 📈 Governance-First Sales Prediction

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

<<<<<<< HEAD
## 🗂 Project Structure

=======
## ▶️ Quick Start

**Clone the repository:**
```bash
git clone https://github.com/edudonaire/governance-first-sales-prediction.git
cd governance-first-sales-prediction
```

**Create environment:**
```bash
conda create -n gov-ml python=3.12
conda activate gov-ml
pip install -r requirements.txt
```

**Run pipeline:**
```bash
jupyter lab
```

**Open and execute notebooks sequentially:** 01 → 08
>>>>>>> 96df9be99268c46e11511d6bc654782eb8adc8ee


<<<<<<< HEAD
governance-first-sales-prediction/
│
├── data/
│ ├── bronze/ # Raw data
│ ├── silver/ # Cleaned data
│ └── gold/ # Feature-engineered datasets
│
├── notebooks/
│ ├── 01_ingestion.ipynb
│ ├── 02_cleaning.ipynb
│ ├── 03_feature_engineering.ipynb
│ ├── 04_modeling.ipynb
│ ├── 05_evaluation.ipynb
│ ├── 06_benchmark.ipynb
│ ├── 07_tuning.ipynb
│ └── 08_explainability.ipynb
│
├── models/
│ └── random_forest_tuned.joblib
│
├── reports/
│ ├── figures/
│ └── metrics/
│
└── README.md


=======
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

>>>>>>> 96df9be99268c46e11511d6bc654782eb8adc8ee
---

## 📊 Dataset

**Source:** Rossmann Store Sales (Kaggle)

<<<<<<< HEAD
Features include:
=======
**Features include:**
>>>>>>> 96df9be99268c46e11511d6bc654782eb8adc8ee

- Store information
- Promotions
- Competition distance
- Calendar features
- Holiday indicators

<<<<<<< HEAD
Target:
=======
**Target:**
>>>>>>> 96df9be99268c46e11511d6bc654782eb8adc8ee

- `Sales`

---

## ⚙️ Methodology

### 1. Data Pipeline

- Bronze → Silver → Gold architecture
- Missing value handling
- Categorical encoding
- Date feature engineering
- Feature normalization
<<<<<<< HEAD

### 2. Modeling

Models evaluated:

- Baseline (Dummy Regressor)
- Linear Regression
- Random Forest (Baseline)
- Random Forest (Tuned)

Validation:

- Train/Test split with temporal awareness
- Cross-validation during tuning

### 3. Hyperparameter Tuning

Technique:

- RandomizedSearchCV
- 3–5 fold cross-validation
- RMSE optimization

Key parameters tuned:

- n_estimators
- max_depth
- min_samples_leaf
- max_features

---

## 🔍 Data Leakage Validation

A dedicated leakage audit was performed.

The `Customers` variable is highly correlated with `Sales` and acts as a proxy for the target.

Two models were compared:

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

Key insight:

> Removing customer-related leakage more than doubled the error, proving the original models were benefiting from indirect target information.

The final production-ready model is the leakage-free version.

---

## 🧠 Explainability

Explainability methods:

### 1. Permutation Importance

- Identifies impact of each feature on prediction accuracy
- Used as main explainability method

Top drivers:

- Promotions
- Competition Distance
- Calendar Effects
- Store Attributes

Saved in:



reports/figures/permutation_importance_top20.png


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

This project prioritizes reliability over raw performance.

---

## 🧪 Reproducibility

Environment:

- Python 3.12
- pandas
- scikit-learn
- numpy
- joblib

To reproduce:

```bash
pip install -r requirements.txt


Run notebooks in order:

01 → 08

📌 Key Takeaways

Leakage prevention is critical in forecasting

Governance improves long-term model reliability

Explainability enables stakeholder trust

Proper validation reduces deployment risk

📬 Author

Eduardo Donaire Filho
Business Intelligence & Data Analytics Leader
Focus: Decision Intelligence, Governance, ML Systems
=======

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

## 💼 Business Impact

This pipeline enables:

- More reliable demand forecasting
- Reduced risk of misleading performance due to leakage
- Better promotion planning
- Improved inventory allocation
- Higher stakeholder confidence

**Governance-first modeling prevents short-term optimization from generating long-term operational losses.**

---

## 📌 Key Takeaways

- Leakage prevention is critical in forecasting
- Governance improves long-term model reliability
- Explainability enables stakeholder trust
- Proper validation reduces deployment risk

---

## 🚧 Limitations & Future Work

**Current limitations:**

- High computational cost for full SHAP analysis
- Single-model family (tree-based)
- No production deployment layer

**Next steps:**

- Gradient boosting models (XGBoost / LightGBM)
- Online inference pipeline
- Drift detection
- Model monitoring
- Automated retraining

---

## 📬 Author

**Eduardo Donaire Filho**  
Business Intelligence & Data Analytics Leader  
Focus: Decision Intelligence, Governance, ML Systems
>>>>>>> 96df9be99268c46e11511d6bc654782eb8adc8ee
