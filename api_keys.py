# api_keys.py

# Importing required libraries
import os
import binascii
from config import DB_CONFIG
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host=DB_CONFIG['DB_HOST'],
    dbname=DB_CONFIG['DB_NAME'],
    user=DB_CONFIG['DB_USER'],
    password=DB_CONFIG['DB_PASSWORD']
)

# Create a cursor object
cur = conn.cursor()

def generate_api_key():
    """Generate a new API key"""
    return binascii.hexlify(os.urandom(24)).decode()

def save_api_key(user_id, api_key):
    """Save the API key to the database"""
    cur.execute("INSERT INTO api_keys (user_id, api_key) VALUES (%s, %s)", (user_id, api_key))
    conn.commit()

def get_api_key(user_id):
    """Retrieve the API key for a user"""
    cur.execute("SELECT api_key FROM api_keys WHERE user_id = %s", (user_id,))
    return cur.fetchone()

def delete_api_key(user_id):
    """Delete a user's API key"""
    cur.execute("DELETE FROM api_keys WHERE user_id = %s", (user_id,))
    conn.commit()

def check_api_key(api_key):
    """Check if an API key is valid"""
    cur.execute("SELECT * FROM api_keys WHERE api_key = %s", (api_key,))
    return cur.fetchone() is not None
