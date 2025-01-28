# **Personalized Healthcare Cost Prediction**

A comprehensive project aimed at predicting individual medical costs billed by health insurance, leveraging demographic and health-related data. This project employs various machine learning models to achieve accurate predictions and deploys a user-friendly web app for practical usage.

---

## **Steps Followed in the Project**

### **1. Problem Understanding**
- **Objective**: Predict individual medical costs using demographic and health-related information.
- **Type of Problem**: Regression problem (predicting continuous values, i.e., `charges`).

---

### **2. Dataset Overview**
The dataset includes the following features:
- `age`: Age of the primary beneficiary.
- `sex`: Gender of the insurance contractor (female/male).
- `bmi`: Body mass index, providing insight into body weight relative to height (ideal BMI: 18.5 - 24.9).
- `children`: Number of dependents covered by health insurance.
- `smoker`: Whether the individual is a smoker (yes/no).
- `region`: Residential area of the beneficiary in the US (northeast, southeast, southwest, northwest).
- `charges`: Individual medical costs billed by health insurance (target variable).

**Key Observations**:
- **Strong influencers**: Age, BMI, and smoker status significantly impact `charges`.
- **Categorical features**: `sex`, `smoker`, and `region` were label-encoded for model compatibility.

---

### **3. Data Preparation**
1. **Imported Libraries**: Utilized Python libraries such as Pandas, NumPy, Scikit-learn, Matplotlib, and Seaborn.
2. **Dataset Loading**: Loaded the data and inspected for consistency.
3. **Missing Values**: Checked for missing data and handled appropriately.
4. **Exploratory Data Analysis (EDA)**:
   - Visualized relationships between features and `charges`.
   - Highlighted trends, outliers, and correlations.

---

### **4. Feature Engineering**
1. **Label Encoding**: Encoded categorical features like `sex`, `smoker`, and `region`.
2. **Scaling**: Standardized numerical features (`age`, `bmi`, `children`) to improve model performance.
3. **Data Splitting**: Split the data into training and testing sets to evaluate model performance.

---

### **5. Model Building**
Implemented the following regression models:
1. **Linear Regression**
2. **Ridge & Lasso Regression**
3. **Gradient Boosting Regressor**
4. **Random Forest Regressor**
5. **Decision Tree Regressor**
6. **XGBoost Regressor**

---

### **6. Model Evaluation**
- **Evaluation Metrics**:
  - R² Score (Explained Variance)
  - RMSE (Root Mean Squared Error)
  - MAE (Mean Absolute Error)
- Each model was evaluated based on its performance across these metrics, and the best-performing model was selected.

---

### **7. Model Selection**
The final model was chosen based on a comparison of R², RMSE, and MAE across all models.

---

### **8. Results Visualization**
1. **Residual Analysis**: Verified model assumptions and error patterns.
2. **Actual vs. Predicted**: Plotted predictions against actual values for better interpretability.

---

### **9. Deployment**
The best-performing model was saved and integrated into a web application:
- **Model Saved**: 
   ```python
   import joblib
   joblib.dump(best_model, 'healthcare_cost_model.pkl')
   ```
- **Web Application**:
   - Built with **FastAPI** for the backend.
   - The frontend is a simple HTML/CSS/JavaScript interface for input and predictions.

---

## **Project Structure**
```plaintext
project/
├── api/
│   ├── main.py                     # FastAPI backend for handling predictions
├── data/
    ├── insurance.csv               # Kaggle Insurance Dataset
├── frontend/
│   ├── index.html                  # Web interface for the application
│   ├── index.css                   # Styling for the web page
│   ├── index.js                    # Form handling and API interaction
├── model/
    ├── healthcare_cost_model.ipynb # EDA and training the model
    ├── healthcare_cost_model.pkl   # Trained machine learning model
├── README.md                       # Project documentation
```

---

## **How to Run the Project**

### **Backend**
1. Navigate to the `api/` directory.
2. Run the main.py python file.
3. The backend will start at `http://localhost:8000`.

### **Frontend**
1. Open the `index.html` file located in the `frontend/` directory in your file explorer.
2. Fill out the form and click "Predict" to get the predicted healthcare cost.

---

## **Future Scope**
- Explore deep learning models for improved prediction accuracy.
- Expand the dataset to include more demographic and lifestyle features.
- Deploy the application to a cloud platform for broader accessibility.

---