import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Credit Risk Prediction System")

st.write("Enter customer details to predict delinquency risk.")


revolving_utilization = customer_id = st.number_input(
    "Customer ID",
    min_value=1
)

st.number_input(
    "Revolving Utilization",
    min_value=0.0
)

age = st.number_input(
    "Age",
    min_value=18
)

past_due_30_59_days = st.number_input(
    "30-59 Days Past Due",
    min_value=0
)

debt_ratio = st.number_input(
    "Debt Ratio",
    min_value=0.0
)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=0.0
)

open_credit_lines_and_loans = st.number_input(
    "Open Credit Lines And Loans",
    min_value=0
)

times_90_days_late = st.number_input(
    "90 Days Late",
    min_value=0
)

real_estate_loans_or_lines = st.number_input(
    "Real Estate Loans Or Lines",
    min_value=0
)

past_due_60_89_days = st.number_input(
    "60-89 Days Past Due",
    min_value=0
)

dependents = st.number_input(
    "Dependents",
    min_value=0.0
)

if st.button("Predict"):

    payload = {
        "customer_id" : customer_id,
        "revolving_utilization": revolving_utilization,
        "age": age,
        "past_due_30_59_days": past_due_30_59_days,
        "debt_ratio": debt_ratio,
        "monthly_income": monthly_income,
        "open_credit_lines_and_loans": open_credit_lines_and_loans,
        "times_90_days_late": times_90_days_late,
        "real_estate_loans_or_lines": real_estate_loans_or_lines,
        "past_due_60_89_days": past_due_60_89_days,
        "dependents": dependents
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:

        result = response.json()

        prediction = result["prediction"]

        if prediction == 1:
            st.error("High Risk Customer")
        else:
            st.success("Low Risk Customer")

    else:
        st.error(response.text)
