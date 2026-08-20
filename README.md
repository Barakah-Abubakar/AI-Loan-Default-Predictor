# AI Loan Default risk Predictor

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
