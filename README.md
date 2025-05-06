# To-Do List (Command-Line)

## Overview

This To-Do List is a command-line Python application designed to manage tasks. This program allows users to add, delete, mark tasks as complete, view all tasks, and export the task list to a text file.

## Features

- **Add a Task**: Add a task with a default status of "Incomplete."
- **Delete a Task**: Remove a task by specifying its number.
- **Complete a Task**: Mark a task as "Complete."
- **View All Tasks**: Display all tasks with their name and current status.
- **Export Tasks**: Export the list of tasks to a `tasks.txt` file.
- **Simple Menu System**: Text-based navigation to select actions.

## Installation

To run the program, ensure you have Python 3.6 or later installed.

### Prerequisites

- **Python 3.6 or later**: [Download Python](https://www.python.org/downloads/)

## Running the Application

1. Download or clone the repository.
2. Navigate to the directory containing the script.
3. Run the program with the following command:

```bash
python task_manager.py
```
Upon running, the user will be presented with the following menu:
```
Option 1: Add task
Option 2: Delete task
Option 3: Set task as complete
Option 4: View all tasks
Option 5: Output all tasks to .txt file
Option 6: Quit
```
Menu Options:
- **Add Task**: Enter a task name and it will be added with the status "Incomplete."

- **Delete Task**: Delete a task by specifying its number.

- **Mark Task Complete**: Change the status of a task to "Complete."

- **View Tasks**: List all tasks with their names and statuses.

- **Export Tasks**: Output all tasks to a tasks.txt file in the current directory.

- **Quit**: Exit the application.

### Method Explanation
Main Features and Functions
print_menu(): Displays the main menu of options.

- **add_task()**: Prompts the user to input a task name and adds it to the tasks dictionary with a default status of "Incomplete."

- **delete_task()**: Deletes a task by its number. The user is prompted to specify the task by its number from the list displayed.

- **confirm_task()**: Marks a specified task as "Complete."

- **view_tasks()**: Lists all tasks in the format:
