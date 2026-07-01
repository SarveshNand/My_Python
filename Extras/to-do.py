import os

# Define the Task class
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.description} - {status}"

# Define the ToDoList class
class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, description):
        self.tasks = [task for task in self.tasks if task.description != description]
        self.save_tasks()

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                break
        self.save_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                completed_status = "1" if task.completed else "0"
                file.write(f"{task.description},{completed_status}\n")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    description, completed_status = line.strip().split(",")
                    task = Task(description)
                    if completed_status == "1":
                        task.mark_completed()
                    self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for task in self.tasks:
                print(task)

# Function to show the menu and interact with the user
def show_menu(todo_list):
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Show Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            description = input("Enter the task description to remove: ")
            todo_list.remove_task(description)
        elif choice == '3':
            description = input("Enter the task description to mark as completed: ")
            todo_list.mark_task_completed(description)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid option, please try again.")

# Main entry point of the program
if __name__ == "__main__":
    todo_list = ToDoList()
    show_menu(todo_list)