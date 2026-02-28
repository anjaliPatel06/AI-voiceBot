import json

with open("data/responses.json") as f:
    RESPONSES = json.load(f)

def generate_response(intent):
    return RESPONSES.get(intent, "Sorry, I did not understand your request.")