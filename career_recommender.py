import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/career_recommendation_model.pkl")

#  Ask user for marks input
print("\n Enter your marks (0-100):")

maths = int(input("Maths: "))
biology = int(input("Biology: "))
physics = int(input("Physics: "))
chemistry = int(input("Chemistry: "))
arts = int(input("Arts: "))
commerce = int(input("Commerce: "))

# Convert input into DataFrame
student_data = {
    "Maths": [maths],
    "Biology": [biology],
    "Physics": [physics],
    "Chemistry": [chemistry],
    "Arts": [arts],
    "Commerce": [commerce]
}

student_df = pd.DataFrame(student_data)

# Ensure same column order
expected_features = ["Maths", "Biology", "Physics", "Chemistry", "Arts", "Commerce"]
student_df = student_df[expected_features]

# Get prediction probabilities
proba = model.predict_proba(student_df)[0]
classes = model.classes_

# Sort top 3 recommendations
top3_idx = proba.argsort()[-3:][::-1]  # top 3 indexes
print("\n Career Recommendations:")

for i in top3_idx:
    print(f"- {classes[i]} ({proba[i]*100:.2f}%)")
