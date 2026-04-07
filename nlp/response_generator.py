import os
import json

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "responses.json")

with open(file_path) as f:
    RESPONSES = json.load(f)

def generate_response(intent):
    return RESPONSES.get(intent, "Sorry, I did not understand your request.")