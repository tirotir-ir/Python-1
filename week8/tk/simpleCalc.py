import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets for numbers
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.pack(pady=10)
entry2.pack(pady=10)

# Create a button to perform the addition
button = tk.Button(root, text="Add", command=add_numbers)
button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
