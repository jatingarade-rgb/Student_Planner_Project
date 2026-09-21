# Student_Planner_Project
here we can add task , delete task , add time , view study progress
# Project Title
Student Task & Study Planner

## Overview of the Project
The Student Task & Study Planner is a Command Line Interface (CLI) Python application built to help students efficiently organize their academic workload. It allows users to track assignments, set specific deadlines, prioritize tasks, and monitor their overall completion progress through a modular and easy-to-use console menu.

## Features
*   **Task Management (CRUD):** Create new study tasks, view all existing tasks, and mark them as completed.
*   **Priority & Sorting:** Automatically sort pending tasks by their due date or by their priority level (High, Medium, Low).
*   **Progress Tracking:** An analytics dashboard that calculates total tasks, pending tasks, completed tasks, and the overall completion rate percentage.
*   **Persistent Storage:** Automatically saves all task data to a local `tasks.json` file so no information is lost when the application is closed.

## Technologies / Tools Used
*   **Programming Language:** Python 3
*   **Built-in Libraries:** `json` (for data storage), `os` (for file path checking), `datetime` (for deadline sorting logic)
*   **Environment / IDE:** Visual Studio Code (VS Code)
*   **Version Control:** Git & GitHub

## Steps to Install & Run the Project
1. Download or clone this project repository to your local machine.
2. Ensure you have Python 3 installed on your system. 
3. Open the project folder (`Student_Planner_Project`) in VS Code.
4. Open the VS Code integrated terminal (`Ctrl + \``).
5. Run the application by executing the following command:
   ```bash
   python main.py
