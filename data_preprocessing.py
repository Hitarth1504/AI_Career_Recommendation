import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
dataset_path = "dataset/career_data.csv"
df = pd.read_csv(dataset_path)

print("Original Dataset:")
print(df.head())

# Initialize LabelEncoder
le = LabelEncoder()

# Encode categorical columns
categorical_columns = ["Stream", "Subjects", "Skills", "Interests", "Personality", "Career", "Fields"]

for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

print("Encoded Dataset:")
print(df.head())

# Save preprocessed dataset
preprocessed_path = "dataset/career_data_preprocessed.csv"
df.to_csv(preprocessed_path, index=False)

print(f"Preprocessed dataset saved at: {preprocessed_path}")
