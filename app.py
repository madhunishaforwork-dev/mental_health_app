from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os
import drift_planner

app = Flask(__name__)

# Load models and vectorizer
# Train models on startup to avoid pickle compatibility issues
try:
    print("Training models on startup...")
    df = pd.read_csv('dataset.csv')
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    
    # 1. Vectorize
    vectorizer = TfidfVectorizer(stop_words='english')
    X_vect = vectorizer.fit_transform(df['text'])

    # 2. Train Emotion Model
    emotion_model = LogisticRegression()
    emotion_model.fit(X_vect, df['emotion'])

    # 3. Train Risk Model
    risk_model = LogisticRegression()
    risk_model.fit(X_vect, df['risk_level'])
    
    print("Models trained successfully in memory.")
except Exception as e:
    print(f"Error training models: {e}")
    emotion_model = None
    risk_model = None
    vectorizer = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not emotion_model or not risk_model or not vectorizer:
        return jsonify({'error': 'Models not loaded'}), 500

    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Vectorize input
        text_vect = vectorizer.transform([text])

        # Predict
        emotion = emotion_model.predict(text_vect)[0]
        risk = risk_model.predict(text_vect)[0]
        
        # Get probabilities (confidence)
        emotion_proba = emotion_model.predict_proba(text_vect).max()
        risk_proba = risk_model.predict_proba(text_vect).max()

        return jsonify({
            'emotion': emotion,
            'risk_level': risk,
            'emotion_confidence': float(emotion_proba),
            'risk_confidence': float(risk_proba)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/drift-plan', methods=['POST'])
def get_drift_plan():
    data = request.get_json()
    text = data.get('text', '')
    emotion = data.get('emotion', '')
    risk = data.get('risk_level', '')
    
    if not text or not emotion or not risk:
        return jsonify({'error': 'Missing required fields'}), 400
        
    plan = drift_planner.generate_plan(emotion, risk, text)
    
    return jsonify(plan)

if __name__ == '__main__':
    app.run(debug=True)
