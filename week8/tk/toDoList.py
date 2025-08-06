import tkinter as tk

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget to input tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create a listbox to display tasks
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# Create a button to delete tasks
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Run the application
root.mainloop()
