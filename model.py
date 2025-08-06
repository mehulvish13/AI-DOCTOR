import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load the symptoms data
df = pd.read_csv("symptoms_data.csv")
X = df["Symptoms"]
y = df["Disease"]

# Create and train the model
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])
model.fit(X, y)

# Create info dictionary for disease information
info = df.set_index("Disease")[["Immediate Action", "Prescription"]].to_dict(orient="index")

def predict_disease(symptom_text):
    """
    Predict disease based on symptom text
    """
    disease = model.predict([symptom_text])[0]
    action = info[disease]["Immediate Action"]
    prescription = info[disease]["Prescription"]
    return disease, action, prescription