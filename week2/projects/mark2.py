import tkinter as tk
from tkinter import messagebox

def nomreh():
    try:
        marks = int(entry.get())
        if marks > 85 and marks <= 100:
            message = "Afarin!tabrik! shagerd aval"
        elif marks > 60 and marks <= 85:
            message = "xoobe"
        elif marks > 40 and marks <= 60:
            message = "zaeef!!"
        elif marks > 30 and marks <= 40:
            message = "tanbaloo"
        else:
            message = "chi shod ?"
        messagebox.showinfo("Result", message)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Marks Evaluation")

# Create and place the label, entry, and button widgets
label = tk.Label(root, text="Enter your marks:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Evaluate", command=nomreh)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
