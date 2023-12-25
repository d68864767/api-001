# gui.py

# Importing required libraries
import tkinter as tk
from tkinter import messagebox
import requests
from config import API_CONFIG

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.train_button = tk.Button(self)
        self.train_button["text"] = "Train Model"
        self.train_button["command"] = self.train_model
        self.train_button.pack(side="top")

        self.generate_key_button = tk.Button(self)
        self.generate_key_button["text"] = "Generate API Key"
        self.generate_key_button["command"] = self.generate_api_key
        self.generate_key_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def train_model(self):
        api_key = 'your_api_key'  # Replace with your API key
        headers = {'api_key': api_key}
        data = {}  # Replace with your data
        response = requests.post(f"{API_CONFIG['API_URL']}/api/train", headers=headers, json={'data': data})
        if response.status_code == 200:
            messagebox.showinfo("Success", "Model trained successfully")
        else:
            messagebox.showerror("Error", response.json()['message'])

    def generate_api_key(self):
        user_id = 'your_user_id'  # Replace with your user_id
        response = requests.post(f"{API_CONFIG['API_URL']}/api/generate_key", json={'user_id': user_id})
        if response.status_code == 200:
            api_key = response.json()['api_key']
            messagebox.showinfo("Success", f"Generated API Key: {api_key}")
        else:
            messagebox.showerror("Error", response.json()['message'])

def run():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    run()
