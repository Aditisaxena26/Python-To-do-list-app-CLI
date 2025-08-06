#to-do-list CLI app
#todo.py

file="tasks.txt"
# Function to add tasks
def add_tasks(task):
    if not task.strip():
        print("Task cannot be empty.")
        return
    else:
        with open(file,"a") as f:
            f.write(task+"\n")

# Function to view all tasks
def view_tasks():
    try:
        with open(file, "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("Tasks:")
                for idx,task in enumerate(tasks,start=1):
                    print(idx,task.strip())
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

# Function to remove a task
def remove_tasks(task_number):
    try:
        with open(file, "r") as f:
            tasks = f.readlines()
        if not tasks:
            print("No tasks to remove.")
            return
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return
        removed_task = tasks.pop(task_number - 1)
        with open(file, "w") as f:
            f.writelines(tasks)
        print("Removed task: ",removed_task.strip())
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

# Main function to run the CLI app
def main():
    print("\n")
    print("\t\t\t\t\t\tWelcome to the To-Do List CLI App")
    print("====================================================================================================================================")
    print("Stay organized and boost your productivity with this simple yet powerful To-Do List CLI application. Designed for everyday use, this tool allows you to quickly add, view, and remove tasks directly from your terminal — no complex setup or graphical interface required. Whether you're managing daily chores, tracking work assignments, or planning personal goals, this application keeps everything in one place and ensures your tasks are saved even after you close the program. Perfect for users who value speed, simplicity, and focus.")
    while True:
        print("\n")
        print("Please choose an option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            no_of_tasks=int(input("Enter the number of tasks you want to add: "))
            for i in range(no_of_tasks):
                add_tasks(input("Enter the task:- "))
            print("Tasks added successfully.")
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_tasks(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
