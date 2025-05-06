#Task list to hold task names and status
import time

tasks = {}


def print_menu():
    """Prints option menu"""

    print("Option 1: Add task")
    print("Option 2: Delete task")
    print("Option 3: Set task as complete")
    print("Option 4: View all tasks")
    print("Option 5: Output all tasks to .txt file")
    print("Option 6: Quit")

def add_task():
    """Adds new task to \"tasks\" list"""

    new_task = input("Enter new task:\n")
    if not isinstance(new_task,str):
        print("Invalid input\n")
        return
    tasks[new_task] = "Incomplete"
    print(f"{new_task} was added to list\n")


def view_tasks():
    """Prints all tasks in \"Task id - id: Name - task_name Status - task_status\" form"""

    if len(tasks)==0:
        print("No tasks to output\n")
    i = 1
    for key,value in tasks.items():
        print(f"Task {i}: Name - \"{key}\" Status - {value}\n")
        i+=1

def delete_task():
    """Deletes a task from \"Tasks\" list by task number that appears in \"view_tasks()\""""

    task = int(input("Task number to delete: "))-1
    if 0>task>len(tasks):
        print("Invalid task number\n")
        return
    key_del = list(tasks)[task]
    tasks.pop(key_del)

def confirm_task():
    """Changes status of a task from \"Incomplete\" to \"Complete\""""

    task_num = int(input("What task number should be marked as complete\n"))-1
    if 0 > task_num > len(tasks):
        print("Invalid task number\n")
        return
    key_confirm = list(tasks)[task_num]
    tasks[key_confirm] = "Complete"
    print(f"Task number {task_num+1} was set to \"Complete\"")

def output_tasks():
    """Outputs all current tasks in \"tasks\" to \"tasks.txt\" file """

    if len(tasks) == 0:
        print("No tasks to output\n")
        return
    with open("tasks.txt",'w') as files:
        i = 1
        for key,value in tasks.items():
            files.write(f"Task {i}: Name - {key} Status - {value}\n")
            i+=1
        print("Tasks output in \"tasks.txt\" file\n")

curr_status=-1
while curr_status != 6:
    print_menu()
    curr_status=int(input("Pick an option: \n"))
    if curr_status==1:
        add_task()
        time.sleep(1)
    elif curr_status==2:
        delete_task()
        time.sleep(1)
    elif curr_status==3:
        confirm_task()
        time.sleep(1)
    elif curr_status==4:
        view_tasks()
        time.sleep(1)
    elif curr_status==5:
        output_tasks()
        time.sleep(1)
    elif curr_status==6:
        break
    else:
        print("Invalid option number. Try again\n")