import tkinter as tk

def convert_temperature():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit}°F")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create an entry widget for input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to perform the conversion
button = tk.Button(root, text="Convert to Fahrenheit", command=convert_temperature)
button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
