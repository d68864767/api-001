# config.py

# Importing required libraries
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
API_CONFIG = {
    'API_KEY': os.getenv('API_KEY'),
    'API_SECRET': os.getenv('API_SECRET'),
    'API_URL': os.getenv('API_URL'),
    'API_PRICE_PER_CALL': 0.01
}

# Model Configuration
MODEL_CONFIG = {
    'MODEL_PATH': os.getenv('MODEL_PATH'),
    'MODEL_NAME': os.getenv('MODEL_NAME')
}

# GUI Configuration
GUI_CONFIG = {
    'GUI_THEME': os.getenv('GUI_THEME'),
    'GUI_LANGUAGE': os.getenv('GUI_LANGUAGE')
}

# Database Configuration
DB_CONFIG = {
    'DB_HOST': os.getenv('DB_HOST'),
    'DB_NAME': os.getenv('DB_NAME'),
    'DB_USER': os.getenv('DB_USER'),
    'DB_PASSWORD': os.getenv('DB_PASSWORD')
}
