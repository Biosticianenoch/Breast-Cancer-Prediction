# 🩺 Breast Cancer Prediction Project  

This project applies **Machine Learning algorithms** to diagnose breast cancer using a dataset of patient features.  
The workflow covers **data preprocessing, exploratory data analysis (EDA), feature selection, model building, hyperparameter tuning, and performance evaluation** across multiple algorithms.  

The goal is to **identify the most accurate predictive model** to support healthcare practitioners in early detection and diagnosis of breast cancer.  

---

## 📊 Dataset  

- **Source:** Breast Cancer Dataset  
- **Target Variable:** `diagnosis`  
  - `M` → Malignant (1)  
  - `B` → Benign (0)  
- **Features:** Patient diagnostic measurements (e.g., radius, texture, smoothness, concavity, symmetry).  

---

## 🔬 Workflow  

1. **Data Preprocessing**  
   - Dropped irrelevant columns (`id`).  
   - Encoded target variable (`diagnosis`).  
   - Checked for null values and duplicates.  

2. **Exploratory Data Analysis (EDA)**  
   - Distribution plots for all features.  
   - Correlation heatmap to identify strong predictors.  
   - Outcome distribution visualization.  

3. **Data Preparation**  
   - Train-test split (80/20).  
   - Handled class imbalance using **RandomOverSampler**.  
   - Standardized features using **StandardScaler**.  
   - Feature selection with **Boruta algorithm**.  

4. **Model Training**  
   Trained and tuned **10 different models**:  
   - Logistic Regression  
   - K-Nearest Neighbors (KNN)  
   - Support Vector Machines (SVM)  
   - Stochastic Gradient Descent Classifier (SGD)  
   - Decision Tree Classifier  
   - Random Forest Classifier  
   - Voting Classifier  
   - AdaBoost Classifier  
   - Gradient Boosting Classifier  
   - Stochastic Gradient Boosting (SGB)  

5. **Evaluation Metrics**  
   - Accuracy  
   - Precision  
   - Recall  
   - F1-Score  
   - Classification Reports  

6. **Model Saving**  
   - Best model saved using **Pickle** for deployment.  

---

## 🏆 Results  

| Model                         | Accuracy |
|-------------------------------|----------|
| Logistic Regression           | 95.61%   |
| KNN                           | 96.49%   |
| SVM                           | 96.49%   |
| SGD Classifier                | 94.73%   |
| Decision Tree                 | 94.73%   |
| Random Forest                 | 96.49%   |
| Voting Classifier             | 96.49%   |
| AdaBoost                      | 95.61%   |
| Gradient Boosting             | **97.44%** |
| Stochastic Gradient Boosting  | 96.49%   |  

✅ **Best Model:** Gradient Boosting Classifier (97.44% accuracy)  

---

## ⚙️ Installation & Usage  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/breast-cancer-prediction.git

