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
DayOfWeek = st.selectbox("Day of Week", [0, 1, 2, 3, 4, 5, 6])
Make = st.selectbox("Make", [0, 1, 2, 3, 4])
AccidentArea = st.radio("Accident Area", [1, 0])
DayOfWeekClaimed = st.selectbox("Day of Week Claimed", [6, 2, 5, 1, 7, 3, 4, 0])
MonthClaimed = st.selectbox("Month Claimed", [5, 10, 6, 4, 8, 3, 1, 2, 9, 7, 12, 11, 0])
WeekOfMonthClaimed = st.selectbox("Week of Month Claimed", [1, 4, 2, 3, 5])
Sex = st.radio("Sex", [0, 1])
MaritalStatus = st.selectbox("Marital Status", [2, 1, 3, 0])
Age = st.slider("Age", float(-2.95403844), float(2.97542797), step=0.1)
Fault = st.radio("Fault", [0, 1])
PolicyType = st.selectbox("Policy Type", [5, 4, 2, 6, 0, 1, 7, 8, 3])
VehicleCategory = st.selectbox("Vehicle Category", [1, 2, 0])
VehiclePrice = st.selectbox("Vehicle Price", [5, 0, 1, 4, 2, 3])
PolicyNumber = st.number_input("Policy Number", min_value=1, max_value=15420)
RepNumber = st.slider("Rep Number", float(-1.62686859), float(1.63414348), step=0.1)
Deductible = st.selectbox("Deductible", [-2.45063315, -0.17529818, 2.10003679, 6.65070674])
DriverRating = st.selectbox("Driver Rating", [-1.32909215, 1.35087485, 0.45755252, -0.43576982])
Days_Policy_Accident = st.selectbox("Days Policy Accident", [3, 1, 4, 0, 2])
Days_Policy_Claim = st.selectbox("Days Policy Claim", [2, 0, 1, 3])
PastNumberOfClaims = st.selectbox("Past Number of Claims", [1.36028877, -1.2949692, -0.40988321, 0.47520278])
AgeOfVehicle = st.selectbox("Age of Vehicle", [1, 4, 5, 6, 3, 7, 2, 0])
AgeOfPolicyHolder = st.selectbox("Age of Policy Holder", [3, 4, 6, 7, 2, 5, 0, 8, 1])
PoliceReportFiled = st.radio("Police Report Filed", [0, 1])
WitnessPresent = st.radio("Witness Present", [0, 1])
AgentType = st.radio("Agent Type", [0, 1])
NumberOfSuppliments = st.selectbox("Number of Supplements", [3, 2, 1, 0])
AddressChange_Claim = st.selectbox("Address Change (Claim)", [0, 3, 2, 1, 4])
NumberOfCars = st.selectbox("Number of Cars", [2, 0, 1, 3, 4])
Year = st.selectbox("Year", [1994, 1995, 1996])
BasePolicy = st.selectbox("Base Policy", [2, 1, 0])


#Collect input values in the order of features expected by the model
input_data = np.array([[Month, WeekOfMonth, DayOfWeek, Make, ...]])  # Add all relevant features

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write("The claim is likely Fraudulent.")
    else:
        st.write("The claim is likely Not Fraudulent.")

