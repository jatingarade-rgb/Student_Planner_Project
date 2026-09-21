import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Reads tasks from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Writes the updated task list back to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)