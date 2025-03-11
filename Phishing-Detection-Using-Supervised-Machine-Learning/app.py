import numpy as np
from flask import Flask, render_template, request
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the saved model and vectorizer
logistic = joblib.load('logistic_regression_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get input message from the user
        message = request.form['message']
        
        # Transform input message using the loaded TF-IDF vectorizer
        input_vector = tfidf.transform([message])
        
        # Predict if it's phishing or not using the loaded model
        prediction = logistic.predict(input_vector)

        # Return prediction result
        result = "phishing" if prediction[0] == 1 else "not phishing"
        return render_template('prediction.html', message=message, result=result)
    
    return render_template('prediction.html', message=None, result=None)

if __name__ == "__main__":
    app.run(debug=True)
