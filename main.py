# main.py

# Importing required libraries
from api import app as api_app
from gui import run as gui_run
from threading import Thread

# Run the API in a separate thread
api_thread = Thread(target=api_app.run, kwargs={
    'host': '0.0.0.0',
    'port': 5000,
    'debug': False,  # Debug mode should be False in the production environment
})
api_thread.start()

# Run the GUI in the main thread
gui_run()

# Wait for the API thread to finish
api_thread.join()
