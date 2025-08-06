import tkinter as tk

# Function to display a personalized greeting and age category
def greet():
    name = name_entry.get()
    age = age_entry.get()
    
    try:
        age = int(age)
        if name:
            if age < 13:
                age_group = "child"
            elif 13 <= age < 20:
                age_group = "teenager"
            else:
                age_group = "adult"
            greeting_label.config(text=f"Hello, {name}! You are {age_group}.", bg="lightgreen")
        else:
            greeting_label.config(text="Please enter your name.", bg="lightcoral")
    except ValueError:
        greeting_label.config(text="Please enter a valid age.", bg="lightcoral")

# Create the main window
root = tk.Tk()
root.title("Hello App")

# Set the background color of the main window
root.configure(bg="white")

# Create an entry widget for the user to input their name
name_label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
name_label.pack(padx=20, pady=5)
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(padx=20, pady=5)

# Create an entry widget for the user to input their age
age_label = tk.Label(root, text="Enter your age:", font=("Arial", 14))
age_label.pack(padx=20, pady=5)
age_entry = tk.Entry(root, font=("Arial", 14))
age_entry.pack(padx=20, pady=5)

# Create a button that calls the greet function when clicked
greet_button = tk.Button(root, text="Greet Me", command=greet, font=("Arial", 14))
greet_button.pack(padx=20, pady=10)

# Create a label to display the greeting message
greeting_label = tk.Label(root, text="", fg="black", font=("Arial", 24, "bold"))
greeting_label.pack(padx=20, pady=20)

# Run the application
root.mainloop()
