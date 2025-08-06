import tkinter as tk

def xxx():
    label.config(text="Hello, World!")

# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Create a label widget
label = tk.Label(root, text="")
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click Me!", command=xxx)
button.pack(pady=20)

# Run the application
root.mainloop()
