import json

def load_tasks():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open("data.json", "w") as f:
        json.dump(tasks, f, indent=4)