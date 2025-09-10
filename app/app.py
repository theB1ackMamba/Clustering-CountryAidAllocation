import streamlit as st
import pandas as pd
import joblib

# Load model once at startup
model = joblib.load("model/pipeline.pkl")

st.title("Clustering Countries for Strategic Aid Allocation")

st.write("Enter country-specific data to predict its cluster:")

country = st.text_input("Country Name (optional)")

child_mort = st.number_input("Child Mortality Rate", min_value=0.0)
exports = st.number_input("Exports", min_value=0.0)
health = st.number_input("Health Expenditure", min_value=0.0)
imports = st.number_input("Imports", min_value=0.0)
income = st.number_input("Per Capita Income", min_value=0.0)
inflation = st.number_input("Inflation", min_value=0.0)
life_expec = st.number_input("Life expectancy", min_value=0.0)
total_fer = st.number_input("Total fertility", min_value=0.0)
gdpp = st.number_input("GDP per Capita", min_value=0.0)

if st.button("Predict Cluster"):
    # Create dataframe
    data = {
        "child_mort": [child_mort],
        "exports": [exports],
        "health": [health],
        "imports": [imports],
        "income": [income],
        "inflation": [inflation],
        "life_expec": [life_expec],
        "total_fer": [total_fer],
        "gdpp": [gdpp]
    }
    df = pd.DataFrame(data)

    # Predict cluster
    cluster = int(model.predict(df)[0])
    st.success(f"{country or 'This country'} belongs to Cluster {cluster}")
