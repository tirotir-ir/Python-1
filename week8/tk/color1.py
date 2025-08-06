import tkinter as tk
import random

def change_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    root.config(bg=random.choice(colors))

# Create the main window
root = tk.Tk()
root.title("Color Changer")

# Create a button to change color
button = tk.Button(root, text="Change Color", command=change_color)
button.pack(pady=20)

# Run the application
root.mainloop()
