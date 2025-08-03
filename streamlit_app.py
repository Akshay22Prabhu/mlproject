# streamlit_app.py
import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Exam Performance", layout="centered")
st.title("📊 Student Exam Performance Indicator")

st.subheader("Fill in the student details:")

gender = st.selectbox("Gender", ["Select", "male", "female"])
ethnicity = st.selectbox("Race or Ethnicity", ["Select", "group A", "group B", "group C", "group D", "group E"])
parent_edu = st.selectbox("Parental Level of Education", [
    "Select", "associate's degree", "bachelor's degree", "high school",
    "master's degree", "some college", "some high school"
])
lunch = st.selectbox("Lunch Type", ["Select", "free/reduced", "standard"])
test_course = st.selectbox("Test Preparation Course", ["Select", "none", "completed"])

reading_score = st.number_input("Reading Score out of 100", min_value=0, max_value=100, step=1)
writing_score = st.number_input("Writing Score out of 100", min_value=0, max_value=100, step=1)

if st.button("Predict Math Score"):
    if "Select" in (gender, ethnicity, parent_edu, lunch, test_course):
        st.warning("Please fill all the required fields.")
    else:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parent_edu,
            lunch=lunch,
            test_preparation_course=test_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        df = data.get_data_as_data_frame()

        pipeline = PredictPipeline()
        prediction = pipeline.predict(df)

        st.success(f"🎯 Predicted Math Score: {prediction[0]:.2f}")
