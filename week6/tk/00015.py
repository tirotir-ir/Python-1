import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.05)  
        progress['value'] = i
        # Update the GUI
        root.update_idletasks()  
    progress.stop()

root = tk.Tk()
root.title("Progressbar Example")

# Create a progressbar widget
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# Button to start progress
start_button = tk.Button(root, text="Start Progress", command=start_progress)
start_button.pack(pady=10)

root.mainloop()
