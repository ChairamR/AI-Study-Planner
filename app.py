import streamlit as st
from planner import generate_plan

st.title("AI Study Planner")

st.write("Upload your subject file and enter daily study hours")

daily_hours = st.number_input("Daily Study Hours", min_value=1, max_value=24, value=5)

uploaded_file = st.file_uploader("Upload subjects.csv", type=["csv"])

if uploaded_file is not None:
    plan = generate_plan(uploaded_file, daily_hours)
    st.subheader("Your Personalized Study Plan")
    st.dataframe(plan)
