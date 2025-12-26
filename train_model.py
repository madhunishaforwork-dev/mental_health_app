import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# Load dataset
print("Loading dataset...")
try:
    df = pd.read_csv('dataset.csv')
    print(f"Dataset loaded. Shape: {df.shape}")
except FileNotFoundError:
    print("Error: dataset.csv not found.")
    exit()

# Preprocessing
X = df['text']
y_emotion = df['emotion']
y_risk = df['risk_level']

# Vectorization
print("Vectorizing text...")
vectorizer = TfidfVectorizer(stop_words='english')
X_vect = vectorizer.fit_transform(X)

# Train Emotion Model
print("Training Emotion Model...")
X_train_e, X_test_e, y_train_e, y_test_e = train_test_split(X_vect, y_emotion, test_size=0.2, random_state=42)
emotion_model = LogisticRegression()
emotion_model.fit(X_train_e, y_train_e)

# Evaluate Emotion Model
y_pred_e = emotion_model.predict(X_test_e)
print("Emotion Model Accuracy:", accuracy_score(y_test_e, y_pred_e))
print("Emotion Model Report:\n", classification_report(y_test_e, y_pred_e))

# Train Risk Model
print("Training Risk Model...")
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_vect, y_risk, test_size=0.2, random_state=42)
risk_model = LogisticRegression()
risk_model.fit(X_train_r, y_train_r)

# Evaluate Risk Model
y_pred_r = risk_model.predict(X_test_r)
print("Risk Model Accuracy:", accuracy_score(y_test_r, y_pred_r))
print("Risk Model Report:\n", classification_report(y_test_r, y_pred_r))

# Save models and vectorizer
print("Saving models...")
joblib.dump(emotion_model, 'models/emotion_model.joblib')
joblib.dump(risk_model, 'models/risk_model.joblib')
joblib.dump(vectorizer, 'models/vectorizer.joblib')

print("Training complete. Models saved in 'models/' directory.")
