import tkinter as tk
from tkinter import messagebox

# Function to add a task to the listbox
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task from the listbox
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to save tasks to a file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")

# Entry for new tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Button to add a new task
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Button to delete a selected task
delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Button to save tasks to a file
save_tasks_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_tasks_button.pack(pady=5)

# Button to load tasks from a file
load_tasks_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_tasks_button.pack(pady=5)

# Load existing tasks on startup
load_tasks()

# Run the main loop
root.mainloop()
