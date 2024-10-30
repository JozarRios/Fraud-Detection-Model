# app.py
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('fraud_detection_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Fraud Detection Prediction App")

# Input features for prediction
st.write("Please input details to predict if the claim is fraud or not.")

# Here you create input widgets for each feature
Month = st.selectbox("Month", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
WeekOfMonth = st.slider("Week of Month", 1, 5, 3)
DayOfWeek = st.selectbox("Day of Week", [0, 1, 2, 3, 4, 5, 6])  # Assuming encoded as integers
Make = st.selectbox("Make", [0, 1, 2, 3, 4])  # Example choices based on encoding

# Collect the rest of the features based on your dataset structure

# Sample: Collect input values in the order of features expected by the model
input_data = np.array([[Month, WeekOfMonth, DayOfWeek, Make, ...]])  # Add all relevant features

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write("The claim is likely Fraudulent.")
    else:
        st.write("The claim is likely Not Fraudulent.")
