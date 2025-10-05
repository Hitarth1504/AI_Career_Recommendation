
#  AI Career Recommendation System

A Machine Learning-based project that recommends the best **career path for students after 12th** based on their academic interests and subject scores.

---

## Project Overview
This project uses **Machine Learning** to suggest a suitable career field (like Engineering, Medicine, Commerce, Arts, etc.) for students after analyzing their subject marks and interests.

---

##  Project Structure
AI_Career_Recommendation/
│
├── dataset/
│ └── career_data.csv # Student dataset used for training
│
├── models/
│ └── career_recommendation_model.pkl # Trained ML model
│
├── src/
│ ├── dataset_creation.py # Generates or loads the dataset
│ ├── data_preprocessing.py # Cleans and prepares data
│ ├── model_training.py # Trains and saves the ML model
│ ├── career_recommender.py # Predicts career based on new input
│ └── app.py #  Web app interface
│
└── README.md
 ## 
---

##  How It Works
1. **Dataset Creation:** Create or load student career data.  
2. **Preprocessing:** Clean and encode data for ML model.  
3. **Training:** Train a Random Forest model to predict careers.  
4. **Prediction:** Enter new student marks → get a recommended career.

---

##  Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Joblib  
- Matplotlib / Seaborn (optional for visualization)

---

##  How to Run Locally
bash
# Step 1: Clone this repository
git clone https://github.com/Hitarth1504/AI_Career_Recommendation.git
cd AI_Career_Recommendation

# Step 2: Install dependencies
pip install pandas scikit-learn joblib

# Step 3: Run the model training script
python src/model_training.py

# Step 4: Make predictions
python src/career_recommender.py

