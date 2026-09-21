from database import load_tasks

def show_progress():
    tasks = load_tasks()
    total_tasks = len(tasks)
    
    if total_tasks == 0:
        print("No tasks available to track.")
        return
        
    completed = sum(1 for t in tasks if t["status"] == "Completed")
    pending = total_tasks - completed
    completion_rate = (completed / total_tasks) * 100
    
    print("\n--- Study Progress ---")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    print(f"Completion Rate: {completion_rate:.1f}%")
    print("----------------------\n")