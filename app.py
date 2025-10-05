import streamlit as st
import pandas as pd
import joblib



# Load model
model = joblib.load("models/career_recommendation_model.pkl")

st.title(" AI Career Recommendation System")
st.write("Enter your marks below (0-100) to get career recommendations.")

# Input fields
maths = st.number_input("Maths", min_value=0, max_value=100)
biology = st.number_input("Biology", min_value=0, max_value=100)
physics = st.number_input("Physics", min_value=0, max_value=100)
chemistry = st.number_input("Chemistry", min_value=0, max_value=100)
arts = st.number_input("Arts", min_value=0, max_value=100)
commerce = st.number_input("Commerce", min_value=0, max_value=100)

if st.button("Get Career Recommendation"):
    # Prepare DataFrame
    student_data = {
        "Maths": [maths],
        "Biology": [biology],
        "Physics": [physics],
        "Chemistry": [chemistry],
        "Arts": [arts],
        "Commerce": [commerce]
    }

    student_df = pd.DataFrame(student_data)
    expected_features = ["Maths", "Biology", "Physics", "Chemistry", "Arts", "Commerce"]
    student_df = student_df[expected_features]

    # Predict probabilities
    proba = model.predict_proba(student_df)[0]
    classes = model.classes_

    # Sort top 3 careers
    top3_idx = proba.argsort()[-3:][::-1]

    st.subheader("Top Career Recommendations")
    for i in top3_idx:
        st.write(f"- {classes[i]} ({proba[i]*100:.2f}%)")
