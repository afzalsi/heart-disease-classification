# classification-model
Classification ML model with data analysis, preprocessing with accuracy,precision,recall with high points and can predict future result with input datas

# Heart Disease Prediction using Machine Learning & Flask

This project is a complete end-to-end Machine Learning application that predicts whether a person has heart disease based on clinical and medical attributes. The trained ML model is integrated with a Flask web application that allows users to enter inputs through a web interface and get real-time predictions.

---

## Project Features
- Binary classification (Heart Disease: Yes / No)
- Advanced data preprocessing (outlier handling, encoding, scaling)
- Supervised ML model with strong performance
- Accuracy, Precision, and Recall close to 0.9
- Trained model saved using Pickle
- Flask-based web application for user input
- Fully version-controlled using GitHub

---

## Project Structure

heart-disease-classification/
│
├── app/
│   ├── app.py
│   ├── predict.py
│   └── templates/
│       └── index.html
│
├── data/
│   └── heart.csv
│
├── model/
│   └── heart_model.pkl
│
├── notebooks/
│   └── heart_model_training.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Dataset
- Source: Kaggle Heart Disease Dataset
- Rows: ~900+
- Target variable: HeartDisease  
  - 0 → No Heart Disease  
  - 1 → Heart Disease  

---

## Machine Learning Pipeline
- Data cleaning and duplicate removal
- Outlier handling using winsorization
- Categorical feature encoding (OneHotEncoder)
- Feature scaling (StandardScaler)
- Model training using ensemble learning
- Evaluation using Accuracy, Precision, Recall
- Model serialization using Pickle

---

## Model Performance
- Accuracy ≈ 0.89+
- Precision ≈ 0.91+
- Recall ≈ 0.89+

---

## Web Application (Flask)
- HTML form for user input
- Flask backend loads trained model
- Real-time prediction displayed on the webpage

---

## How to Run the Project

### Install dependencies
pip install -r requirements.txt

### Run the Flask app
cd app  
python app.py

### Open browser
http://127.0.0.1:5000/

---

## Sample High-Risk Input
- Age: 58
- Sex: Male
- Chest Pain Type: ASY
- Exercise Angina: Yes
- ST Slope: Flat
- Oldpeak: 2.5

Prediction → Heart Disease: YES

---

## Use Cases
- Machine Learning internship project
- Healthcare analytics demonstration
- End-to-end ML deployment practice
- Portfolio project for GitHub

---

## Author
Afzal  
B.E. Artificial Intelligence & Machine Learning

