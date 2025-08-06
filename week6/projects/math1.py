import tkinter as tk
from tkinter import messagebox

def calculate_area_perimeter():
    shape = shape_var.get()
    if shape == "Rectangle":
        try:
            width = float(entry1.get())
            height = float(entry2.get())
            area = width * height
            perimeter = 2 * (width + height)
            result_var.set(f"Area: {area}\nPerimeter: {perimeter}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for width and height.")
    elif shape == "Square":
        try:
            side = float(entry1.get())
            area = side * side
            perimeter = 4 * side
            result_var.set(f"Area: {area}\nPerimeter: {perimeter}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for side length.")
    elif shape == "Circle":
        try:
            radius = float(entry1.get())
            area = 3.14159 * radius * radius
            perimeter = 2 * 3.14159 * radius
            result_var.set(f"Area: {area}\nCircumference: {perimeter}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for radius.")
    else:
        result_var.set("Please select a shape.")

def update_input_fields(*args):
    shape = shape_var.get()
    if shape == "Rectangle":
        label1.config(text="Width:")
        label2.config(text="Height:")
        entry2.pack(side=tk.LEFT)
    elif shape == "Square":
        label1.config(text="Side length:")
        label2.pack_forget()
        entry2.pack_forget()
    elif shape == "Circle":
        label1.config(text="Radius:")
        label2.pack_forget()
        entry2.pack_forget()

# Create main window
root = tk.Tk()
root.title("Math School Assistant")

# Create shape selection dropdown
shape_var = tk.StringVar(value="Select a shape")
shapes = ["Rectangle", "Square", "Circle"]
shape_menu = tk.OptionMenu(root, shape_var, *shapes)
shape_menu.pack(pady=10)

# Bind the shape selection to update input fields
shape_var.trace("w", update_input_fields)

# Create input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

label1 = tk.Label(input_frame, text="Dimension 1:")
label1.pack(side=tk.LEFT)
entry1 = tk.Entry(input_frame)
entry1.pack(side=tk.LEFT)

label2 = tk.Label(input_frame, text="Dimension 2:")
label2.pack(side=tk.LEFT)
entry2 = tk.Entry(input_frame)
entry2.pack(side=tk.LEFT)

# Create a button to calculate area and perimeter
calc_button = tk.Button(root, text="Calculate", command=calculate_area_perimeter)
calc_button.pack(pady=10)

# Create a label to display results
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
