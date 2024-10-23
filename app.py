import streamlit as st

# Title of the web app
st.title("Disease Prediction App")

# Sidebar for user inputs
st.sidebar.header("Enter Medical Information")

# Input fields for the user to enter data
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=25)
blood_pressure = st.sidebar.number_input(
    "Blood Pressure", min_value=50, max_value=200, value=120)
cholesterol = st.sidebar.number_input(
    "Cholesterol Level", min_value=100, max_value=400, value=200)

# Display the input values on the main page
st.write(f"Age: {age}")
st.write(f"Blood Pressure: {blood_pressure}")
st.write(f"Cholesterol Level: {cholesterol}")

# A button to trigger predictions (you can add the ML model here later)
if st.sidebar.button("Predict"):
    st.write("Here will be the prediction results")
