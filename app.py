from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os
import drift_planner

app = Flask(__name__)

# Load models and vectorizer
try:
    emotion_model = joblib.load('models/emotion_model.joblib')
    risk_model = joblib.load('models/risk_model.joblib')
    vectorizer = joblib.load('models/vectorizer.joblib')
    print("Models loaded successfully.")
except Exception as e:
    print(f"Error loading models: {e}")
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
