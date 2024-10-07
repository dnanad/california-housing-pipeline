from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pipeline
pipeline = joblib.load('california_housing_pipeline.pkl')

@app.route('/')
def home():
    return "Welcome to the California Housing Price Prediction API"


# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     if 'features' not in data:
#         return jsonify({"error": "Missing 'features' key in request data"}), 400

#     features = np.array(data['features']).reshape(1, -1)
#     prediction = pipeline.predict(features)
#     return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
