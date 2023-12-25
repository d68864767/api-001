# api.py

# Importing required libraries
from flask import Flask, request, jsonify
from models import Model
from api_keys import check_api_key, generate_api_key, save_api_key
from config import API_CONFIG

app = Flask(__name__)
model = Model()

@app.route('/api/train', methods=['POST'])
def train():
    api_key = request.headers.get('api_key')
    if not check_api_key(api_key):
        return jsonify({'message': 'Invalid API Key'}), 401

    data = request.json.get('data')
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    prediction = model.predict(data)
    if prediction is None:
        return jsonify({'message': 'Error making prediction'}), 500

    return jsonify({'prediction': prediction.tolist()}), 200

@app.route('/api/generate_key', methods=['POST'])
def generate_key():
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({'message': 'No user_id provided'}), 400

    api_key = generate_api_key()
    save_api_key(user_id, api_key)

    return jsonify({'api_key': api_key}), 200

if __name__ == '__main__':
    app.run(host=API_CONFIG['API_URL'], debug=True)
