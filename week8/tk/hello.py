import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Create a label widget
label = tk.Label(root, text="")
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click Me!", command=say_hello)
button.pack(pady=20)

# Run the application
root.mainloop()
