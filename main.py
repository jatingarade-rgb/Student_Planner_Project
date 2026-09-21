import task_manager
import sorter
import analytics

def main():
    while True:
        print("\n=== Student Task & Study Planner ===")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. View Tasks Sorted by Deadline")
        print("5. View Study Progress")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ")
            task_manager.add_task(title, deadline, priority)
            
        elif choice == '2':
            task_manager.view_tasks()
            
        elif choice == '3':
            try:
                task_id = int(input("Enter Task ID to mark completed: "))
                task_manager.mark_completed(task_id)
            except ValueError:
                print("Please enter a valid numeric ID.")
                
        elif choice == '4':
            sorted_list = sorter.sort_by_deadline()
            task_manager.view_tasks(sorted_list)
            
        elif choice == '5':
            analytics.show_progress()
            
        elif choice == '6':
            print("Exiting Planner. Good luck with your studies!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
    