import tkinter as tk
import random

# Function to change the text and color of the label
def change_text_and_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    texts = ["Hello, World!", "Hi there!", "Welcome!", "Howdy!", "Greetings!", "Hey!"]

    new_color = random.choice(colors)
    new_text = random.choice(texts)

    label.config(text=new_text, bg=new_color)

# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Set the background color of the main window
root.configure(bg="lightblue")

# Create a label with the text "Hello, World!" and set its foreground and background colors
label = tk.Label(root, text="Hello, World!", fg="white", bg="blue", font=("Arial", 24, "bold"))
label.pack(padx=20, pady=20)

# Create a button that changes the text and color of the label when clicked
button = tk.Button(root, text="Change Text and Color", command=change_text_and_color, font=("Arial", 14))
button.pack(padx=20, pady=20)

# Run the application
root.mainloop()
