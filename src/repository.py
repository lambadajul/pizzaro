import json
import os

def load(path):

    if not os.path.exists(path):
        return []

    with open(path, encoding="utf8") as f:
        return json.load(f)

def save(path, data):

    with open(path, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4)
