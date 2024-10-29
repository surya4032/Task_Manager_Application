import json
import sys
import getpass
import os
import time
print(os.getcwd())

def clr_scrn():
    os.system('cls')
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return [Task(task["id"], task["title"], task["completed"]) for task in tasks]
    except FileNotFoundError:
        print("File not found")
        sys.exit()
    except json.JSONDecodeError:
        
        return []
        
class Task:
    # Load tasks from file
   
    """Represents a task with an ID, title, and completion status."""

    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f" {self.id}: {self.title} ,status :{status}"  
    
   
def save_tasks():
    try:
        with open("tasks.json", "w") as file:
            json.dump([{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks], file)
        
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task():
    """Prompts user for task details and adds it to the task list."""
    title = input("Enter task title: ")
    tasks.append(Task(len(tasks) + 1, title))
    save_tasks()
    print("Task added successfully!")
    time.sleep(3)
    return main_menu()

def view_tasks():
    """Displays all tasks in the list."""
    if not tasks:
        print("No tasks found. please add new tasks")
        print('redirecting to  menu ...')
        time.sleep(3)
        return main_menu()  
    else:
        for task in tasks:
            print(task)
        menu=input("enter home to return to main menu :")
        if menu!='home':
            clr_scrn()
            view_tasks()
        else:
            return main_menu()
    

def delete_task():
    """Prompts user for task ID and deletes it from the list."""
    if len(tasks)==0:
            print("No tasks to delete please add a task")
            time.sleep(3)
            return main_menu()
    else:
        """Display all tasks so user can select which task to delete"""
        for task in tasks:
            print(task)
    print("Are you sure you want to delete!!")
    delete=input("please type yes to delete or type no to return to main menu")
    if delete =='yes' or delete=='YES':
        task_id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task.id==task_id:
                tasks.remove(task)
                print("Deleting tasks...")
                save_tasks()
            else:
                print("Enter valid Id")
                time.sleep(3)
                return delete_task()
    else:
        return main_menu()
        
    


def mark_task_complete():
    """Prompts user for task ID and marks it as completed."""
    if len(tasks)==0:
            print("No tasks to mark please add a task")
            time.sleep(3)
            return main_menu()
    else:

        task_id = int(input("Enter task ID to mark complete: "))
        try:
            tasks[task_id - 1].completed = True
            print("Task marked as completed!")
            save_tasks(tasks)
            time.sleep(3)
            return main_menu()

        except IndexError:
            print("please enter valid task ID.")
            time.sleep(3)
            return main_menu()
   
      
 
def main_menu():
    
   
    """Displays the main menu and handles user commands."""
    print("Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Complete")
    print("5.  Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        clr_scrn()
        add_task()
    elif choice == "2":
        clr_scrn()
        view_tasks()
    elif choice == "3":
        clr_scrn()
        
        delete_task()
    elif choice == "4":
        clr_scrn()
        mark_task_complete()
    elif choice == "5":
        clr_scrn()
        print("Tasks saved and exiting.")
        sys.exit()
    else:
        print("Invalid choice.")
        main_menu()
Email_id="k@gmail.com"
p="1234"
def login():
    
    Email=input("Enter Emailid: ")
    password=getpass.getpass("Enter password:")
    if Email==Email_id and password==p:
        main_menu()
    else:
        print("Enter valid user details")
        
        time.sleep(3)
        clr_scrn()
        login()
       
global tasks
# Main application loop

if __name__ =="__main__":
    
    tasks=load_tasks()
    login()
    