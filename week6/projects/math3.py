#pip install pillow
import tkinter as tk
from tkinter import messagebox, colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk
import io

def calculate_area_perimeter():
    shape = shape_var.get()
    color = color_var.get()
    canvas.delete("all")  # Clear previous drawings

    if shape == "Rectangle":
        try:
            width = float(entry1.get())
            height = float(entry2.get())
            area = width * height
            perimeter = 2 * (width + height)
            result_var.set(f"Area: {area}\nPerimeter: {perimeter}")
            canvas.create_rectangle(10, 10, 10 + width * 10, 10 + height * 10, outline=color, fill=color)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for width and height.")
    elif shape == "Square":
        try:
            side = float(entry1.get())
            area = side * side
            perimeter = 4 * side
            result_var.set(f"Area: {area}\nPerimeter: {perimeter}")
            canvas.create_rectangle(10, 10, 10 + side * 10, 10 + side * 10, outline=color, fill=color)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for side length.")
    elif shape == "Circle":
        try:
            radius = float(entry1.get())
            area = 3.14159 * radius * radius
            perimeter = 2 * 3.14159 * radius
            result_var.set(f"Area: {area}\nCircumference: {perimeter}")
            canvas.create_oval(10, 10, 10 + radius * 20, 10 + radius * 20, outline=color, fill=color)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for radius.")
    elif shape == "Triangle":
        try:
            base = float(entry1.get())
            height = float(entry2.get())
            area = 0.5 * base * height
            perimeter = "Undefined for generic triangle"
            result_var.set(f"Area: {area}\nPerimeter: {perimeter}")
            canvas.create_polygon(10, 10 + height * 10, 10 + base * 10, 10 + height * 10, 10 + (base * 5), 10, outline=color, fill=color)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for base and height.")
    elif shape == "Ellipse":
        try:
            r1 = float(entry1.get())
            r2 = float(entry2.get())
            area = 3.14159 * r1 * r2
            perimeter = "Approximate: " + str(3.14159 * (3*(r1 + r2) - ((3*r1 + r2)*(r1 + 3*r2))**0.5))
            result_var.set(f"Area: {area}\nPerimeter: {perimeter}")
            canvas.create_oval(10, 10, 10 + r1 * 20, 10 + r2 * 20, outline=color, fill=color)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for radius 1 and radius 2.")
    else:
        result_var.set("Please select a shape.")

def update_input_fields(*args):
    shape = shape_var.get()
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    if shape == "Rectangle" or shape == "Triangle" or shape == "Ellipse":
        label1.config(text="Dimension 1:")
        label2.config(text="Dimension 2:")
        entry2.pack(side=tk.LEFT)
    elif shape == "Square":
        label1.config(text="Side length:")
        label2.pack_forget()
        entry2.pack_forget()
    elif shape == "Circle":
        label1.config(text="Radius:")
        label2.pack_forget()
        entry2.pack_forget()

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        color_var.set(color)

def save_drawing():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        ps = canvas.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img.save(file_path)

# Create main window
root = tk.Tk()
root.title("Math School Assistant")

# Create shape selection dropdown
shape_var = tk.StringVar(value="Select a shape")
shapes = ["Rectangle", "Square", "Circle", "Triangle", "Ellipse"]
shape_menu = tk.OptionMenu(root, shape_var, *shapes)
shape_menu.pack(pady=10)

# Bind the shape selection to update input fields
shape_var.trace("w", update_input_fields)

# Create color selection button
color_var = tk.StringVar(value="black")
color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(pady=10)

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

# Create a canvas to draw shapes
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=10)

# Create a button to save the drawing
save_button = tk.Button(root, text="Save Drawing", command=save_drawing)
save_button.pack(pady=10)

# Start the main event loop
root.mainloop()
