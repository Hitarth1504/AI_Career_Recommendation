import pandas as pd
import os

# Make sure dataset folder exists
os.makedirs("dataset", exist_ok=True)

# Sample dataset: marks (0–100) → career path
data = {
    "Maths": [85, 60, 30, 20, 75, 40, 55, 90, 25, 50],
    "Biology": [20, 90, 60, 85, 30, 80, 40, 25, 95, 50],
    "Physics": [80, 50, 20, 40, 85, 30, 60, 95, 25, 55],
    "Chemistry": [75, 85, 40, 70, 60, 90, 45, 80, 95, 50],
    "Arts": [30, 20, 85, 70, 40, 90, 95, 25, 60, 55],
    "Commerce": [40, 30, 70, 85, 90, 50, 95, 25, 60, 75],
    "Recommended_Career": [
        "Engineer", "Doctor", "Artist", "Doctor",
        "Engineer", "Doctor", "Artist", "Engineer",
        "Doctor", "Commerce"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("dataset/career_data.csv", index=False)
print(" Dataset created successfully at dataset/career_data.csv")
