Overview
This project leverages machine learning algorithms to build predictive models for Coronary Artery Disease (CAD) and Hypertension (HT). It includes a Flask-based web application that provides real-time risk predictions based on user inputs, offering an innovative solution for early diagnosis and healthcare decision-making.

Features
Predictive Models: Soft Voting Classifier combining Logistic Regression, KNN, SVM, Gradient Boosting, and Balanced Random Search.
Risk Categorization: Classifies risks as Low, Moderate, or High based on clinical thresholds for cholesterol, blood pressure, diabetes, and family history.
Web Application: User-friendly Flask app for real-time risk predictions.
Statistical Analysis: Includes ANOVA and Chi-Square tests for feature significance.
Database Integration: Stores prediction results into a MySQL database for future analysis.
Dataset
The dataset used contains health indicators such as:

Cholesterol levels
Systolic and Diastolic Blood Pressure
Diabetes (Yes/No)
Family history of heart disease
Blood Pressure Status (Low/Normal/High)
The dataset was preprocessed to handle outliers, normalize data, and enhance feature selection.

Methodology
Data Preprocessing:

Outlier handling, normalization, and feature engineering.
Statistical tests (ANOVA, Chi-Square) for feature selection.
Model Development:

Ensemble learning using Soft Voting Classifier.
Individual models trained: Logistic Regression, KNN, SVM, Gradient Boosting, and Balanced Random Search.
Risk Categorization:

Categorizes CAD and HT risks into Low, Moderate, or High based on clinical thresholds.
Web Application:

Flask app for user interaction and predictions.
Results stored in MySQL database.
