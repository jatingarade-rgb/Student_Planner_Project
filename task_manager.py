from database import load_tasks, save_tasks

def add_task(title, deadline, priority):
    tasks = load_tasks()
    # Generate a simple ID
    task_id = len(tasks) + 1 if len(tasks) == 0 else tasks[-1]["id"] + 1
    
    new_task = {
        "id": task_id,
        "title": title,         # e.g., "Revise Bio-Savart Law"
        "deadline": deadline,   # e.g., "2026-10-15"
        "priority": priority,   # "High", "Medium", "Low"
        "status": "Pending"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def view_tasks(tasks_list=None):
    tasks = tasks_list if tasks_list else load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    for t in tasks:
        print(f"[{t['id']}] {t['title']} | Due: {t['deadline']} | Priority: {t['priority']} | Status: {t['status']}")

def mark_completed(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed.")
            return
    print("Task ID not found.")