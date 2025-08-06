import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
clock_label.pack(pady=20)

# Start the clock update loop
update_clock()

# Run the application
root.mainloop()
