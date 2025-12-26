# Mental Health Risk Detection System

## Overview
This is a full-stack Machine Learning web application that analyzes user-submitted text to detect emotional state and potential mental health risk levels. It uses Python (Flask) for the backend and pure HTML/CSS/JS for the frontend.

## Features
- **Emotion Detection**: Classifies text into emotions (Happy, Neutral, Stressed, Depressed).
- **Risk Assessment**: Predicts risk level (Low, Medium, High).
- **Interactive UI**: Simple, real-time interface.

## Tech Stack
- **Backend**: Python, Flask
- **ML**: Scikit-learn, Pandas, Joblib (TF-IDF + Logistic Regression)
- **Frontend**: HTML5, CSS3, JavaScript

## Installation & Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the Model**
   Run the training script to generate the models:
   ```bash
   python train_model.py
   ```
   This will create a `models/` directory containing the trained models and vectorizer.

3. **Run the Application**
   Start the Flask server:
   ```bash
   python app.py
   ```

4. **Access the App**
   Open your browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure
```
mental_health_app/
├── app.py              # Flask backend
├── train_model.py      # ML training script
├── dataset.csv         # Sample dataset
├── requirements.txt    # Python dependencies
├── models/             # Saved ML models
├── static/             # CSS and JS files
│   ├── style.css
│   └── script.js
└── templates/          # HTML templates
    └── index.html
```
