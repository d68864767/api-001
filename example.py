# example.py

# Importing required libraries
import requests
import json

# API URL
API_URL = 'http://localhost:5000/api'

# User ID
USER_ID = 'your_user_id'

# Generate API Key
def generate_api_key():
    response = requests.post(f'{API_URL}/generate_key', json={'user_id': USER_ID})
    if response.status_code == 200:
        return response.json()['api_key']
    else:
        print(f'Error generating API key: {response.json()}')
        return None

# Train AI Model
def train_model(api_key, data):
    headers = {'api_key': api_key}
    response = requests.post(f'{API_URL}/train', headers=headers, json={'data': data})
    if response.status_code == 200:
        return response.json()['prediction']
    else:
        print(f'Error training model: {response.json()}')
        return None

# Example of how to use API Key
def example():
    # Generate API Key
    api_key = generate_api_key()
    if api_key is None:
        return

    # Example data
    data = [1, 2, 3, 4, 5]

    # Train model
    prediction = train_model(api_key, data)
    if prediction is not None:
        print(f'Prediction: {prediction}')

if __name__ == '__main__':
    example()
