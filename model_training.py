import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
df = pd.read_csv("dataset/career_data.csv")
print("Dataset Loaded Successfully")

# Features (input: marks) and Target (output: career)
X = df.drop("Recommended_Career", axis=1)
y = df["Recommended_Career"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f" Model trained with accuracy: {accuracy * 100:.2f}%")

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/career_recommendation_model.pkl")
print(" Model saved successfully in 'models/' folder")
