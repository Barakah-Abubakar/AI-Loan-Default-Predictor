# AI Loan Default Risk Predictor

A web application using machine learning to assess the risk of loan default based on basic borrower's financial parameters and loan details.

**Project Overview**

Loan default can result in financial losses for lenders and borrowers. 
Identifying potential default risk early can support better loan assessment and encourage further review of high-risk applications.
This project develops a machine learning tool that estimates the tendency of loan default using a simplified set of borrower financial parameters.
The aim of this project, but to develop a model that is solves a practical problem of 
identifying the risk of loan defaulters in financial institutions.


**Problem Statement**

Microfinance banks, financial institutions, and other loan providers need to assess the potential risk that a loan applicant may default
However, effective financial risk assessment can involve numerous variables, some of which may be difficult to obtain, or impractical to use.

This raises an important question:
How can key borrower and loan-related financial indicators be used to identify loan applications that may be at a 
higher risk of default and flag them for further review?
This project therefore propose a solution to of loan default risk assessment using key loan details and applicants basic financial details  whether a smaller set of practical and accessible borrower and loan characteristics

**Project Objective**

The objective of this project is to build and deploy a machine learning model that:
Estimates the potential risk of loan default using basic applicant financial information such as Age, Annual Income,  Monthly debt payment, Debt-to-income Ratio, duration of employment 
and loan details such as:  interest rate and loan amount.
The final solution provides users with an estimated default probability and a simple risk category:
Low Risk for prediction probability < 30%, Moderate Risk which falls between 31% and 60% and High Risk  for predictions above 60%

**Dataset**

The original dataset contained 255347 records and 18 features loan records and included
borrower demographics, financial information, loan characteristics, and a target variable indicating whether a loan defaulted.
Dataset source : https://www.kaggle.com/datasets/nikhil1e9/loan-default


**Methodology**
The project followed the following machine learning workflow:
Data Preparation
        ↓
Train-test-split
        ↓
Feature engineering 
        ↓
Model Training 
        ↓
Model Evaluation and Comparison
        ↓
Feature selection, Model retraining and evaluation 
        ↓
Model Deployment

**Feature Selections and Engineering **
The original dataset contained multiple numerical and categorical variables.
Feature importance was explored using different models. However, the importance rankings differed between Random Forest and Logistic Regression.
Therefore, the final feature set was not selected based solely on a single model's feature importance ranking.
Instead, features were selected based on a combination of:
Model exploration and features relevant to the industry.

The final model uses six features which are:
Age of the applicant, Annual income, Amouunt of loan requested, Interest rate associated with the loan, Number of months the applicant has been employed and  Debt-to-Income Ratio
For easier use in the application, the Debt-to-Income Ratio is calculated automatically using:
DTI Ratio = Monthly Debt Payments / Monthly Income
Monthly income is estimated from the user's annual income.
The Numerical values were scaled using Standard Scaler library. while the categorical variables were encoded using one hot encoding 

Data Preparation
The dataset was prepared for machine learning by:
Removing the loan identifier
Separating features and the target variable
Splitting the dataset into training and testing sets
Preprocessing numerical and categorical variables where required
2. Model Exploration
Two models were explored:
Random Forest Classifier
Logistic Regression
The Random Forest model achieved high overall accuracy but performed poorly when identifying actual loan defaults.
This demonstrated an important limitation of relying solely on accuracy when working with an imbalanced dataset.
Logistic Regression, using balanced class weights, demonstrated substantially better recall for the default class.

 **Model Performance**
Full Logistic Regression Model
33%
Although the overall accuracy was lower than the Random Forest model, Logistic Regression was better able to identify potential loan defaults.
Simplified Six-Feature Model
The final simplified model achieved:
Metric
Default Class
Precision
21%
Recall
69%
F1-Score
32%
Overall accuracy was approximately 66%.


**Web Application Deliverable**
The machine learning model was deployed as a web application using Streamlit.
Users provide:
Age
Annual Income
Loan Amount
Interest Rate
Months Employed
Monthly Debt Payments
The application automatically calculates the Debt-to-Income Ratio and uses the trained model to estimate the probability of loan default.
The result is displayed as:
Estimated Default Risk (%)
Low, Moderate, or High Risk category

**Technologies Used**

Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Google Colab
GitHub

**Limitations**

A low precision score means that some borrowers predicted as high risk may not actually default.

