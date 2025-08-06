import tkinter as tk
from tkinter import messagebox

def convert_units():
    try:
        value = float(entry1.get())
        from_unit = from_var.get()
        to_unit = to_var.get()
        
        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = value * 9/5 + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Meter" and to_unit == "Yard":
            result = value * 1.09361
        elif from_unit == "Yard" and to_unit == "Meter":
            result = value / 1.09361
        elif from_unit == "Kilogram" and to_unit == "Pound":
            result = value * 2.20462
        elif from_unit == "Pound" and to_unit == "Kilogram":
            result = value / 2.20462
        else:
            result = "Conversion not supported"
        
        result_var.set(f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Conversion Tools")

# Create unit selection dropdowns
unit_types = ["Temperature", "Length", "Weight"]

units = {
    "Temperature": ["Celsius", "Fahrenheit"],
    "Length": ["Meter", "Yard"],
    "Weight": ["Kilogram", "Pound"]
}

def update_units(*args):
    unit_type = unit_type_var.get()
    from_menu["menu"].delete(0, "end")
    to_menu["menu"].delete(0, "end")
    for unit in units[unit_type]:
        from_menu["menu"].add_command(label=unit, command=tk._setit(from_var, unit))
        to_menu["menu"].add_command(label=unit, command=tk._setit(to_var, unit))
    from_var.set(units[unit_type][0])
    to_var.set(units[unit_type][1])

unit_type_var = tk.StringVar(value="Temperature")
unit_type_menu = tk.OptionMenu(root, unit_type_var, *unit_types)
unit_type_menu.pack(pady=10)

unit_type_var.trace("w", update_units)

from_var = tk.StringVar(value=units["Temperature"][0])
to_var = tk.StringVar(value=units["Temperature"][1])

from_menu = tk.OptionMenu(root, from_var, *units["Temperature"])
from_menu.pack(pady=10)

to_menu = tk.OptionMenu(root, to_var, *units["Temperature"])
to_menu.pack(pady=10)

# Create input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

label1 = tk.Label(input_frame, text="Value:")
label1.pack(side=tk.LEFT)
entry1 = tk.Entry(input_frame)
entry1.pack(side=tk.LEFT)

# Create a button to perform conversion
convert_button = tk.Button(root, text="Convert", command=convert_units)
convert_button.pack(pady=10)

# Create a label to display results
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
