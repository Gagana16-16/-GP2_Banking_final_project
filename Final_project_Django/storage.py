import json
import os

STORAGE_FILE = "financial_data.json"

def load_all_data():
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, "r") as file:
        return json.load(file)

def save_data(key, value):
    data = load_all_data()
    data[key] = value
    with open(STORAGE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def clear_storage():
    with open(STORAGE_FILE, "w") as file:
        json.dump({}, file)
