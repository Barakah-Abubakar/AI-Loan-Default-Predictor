
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_default_model.pkl")

st.title("AI Loan Risk Prediction App")
st.write("This tool uses basic borrower and loan information to estimate the potential risk of loan default. Fill in the details below to predict loan eligibility.")

st.subheader("Applicant Financial Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

income = st.number_input(
    "Annual Income",
    min_value=0.0,
    help="Total income earned in a year in Naira"
)

loan_amount = st.number_input(
    "Loan Amount Requested",
    min_value=0.0,
    value=10000.0
)

interest_rate = st.number_input(
    "Interest Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

months_employed = st.number_input(
    "Months Employed",
    min_value=0,
    help="Total number of months employed"
)

# DTI calculation
st.subheader("Debt Information")

monthly_income = income / 12


monthly_debt = st.number_input(
    "Total Monthly Debt Payments",
    min_value=0.0,
    help = "Minimum legal amounts you must pay each month toward the borrowed money"
)


# Calculate DTI
dti_ratio = monthly_debt / monthly_income

st.info(f"Estimated Debt-to-Income Ratio: {dti_ratio:.2%}")


# Prediction
if st.button("Assess Loan Risk"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "LoanAmount": [loan_amount],
        "InterestRate": [interest_rate],
        "MonthsEmployed": [months_employed],
        "DTIRatio": [dti_ratio]
    })

    # Get probability of default
    probability = model.predict_proba(input_data)[0][1]

    risk_percentage = probability * 100

    # Display result
    st.subheader("Loan Risk Assessment")

    st.metric(
        "Estimated Default Risk",
        f"{risk_percentage:.1f}%"
    )

    # Risk categories
    if probability < 0.30:
        st.success("🟢 Low Risk")
        st.write(
            "This application shows a lower estimated risk based on the model."
        )

    elif probability < 0.60:
        st.warning("🟡 Moderate Risk")
        st.write(
            "This application may require additional review."
        )

    else:
        st.error("🔴 High Risk")
        st.write(
            "This application shows a higher estimated risk and may require further assessment."
        )
