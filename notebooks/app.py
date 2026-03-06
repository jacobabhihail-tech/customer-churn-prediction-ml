import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

st.write("Enter customer details")

tenure = st.number_input("Tenure Months", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0, 200)
total_charges = st.number_input("Total Charges", 0, 10000)

if st.button("Predict"):

    # Create empty dataframe with all model features
    data = pd.DataFrame(np.zeros((1, len(model.feature_names_in_))), 
                        columns=model.feature_names_in_)

    # Fill user inputs
    data["Tenure Months"] = tenure
    data["Monthly Charges"] = monthly_charges
    data["Total Charges"] = total_charges

    prediction = model.predict(data)
    probability = model.predict_proba(data)

    st.write("Prediction:", prediction)
    st.write("Probability:", probability)