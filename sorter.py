from database import load_tasks
from datetime import datetime

def sort_by_deadline():
    tasks = load_tasks()
    # Sorts tasks by converting the string date into a datetime object for accurate comparison
    sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d"))
    return sorted_tasks

def sort_by_priority():
    tasks = load_tasks()
    # Custom sorting map: High is 1, Medium is 2, Low is 3
    priority_map = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks, key=lambda x: priority_map.get(x["priority"], 4))
    return sorted_tasks