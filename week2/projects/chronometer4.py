import tkinter as tk
import time
import winsound

# Function to update the timer display
def update_timer():
    global remaining_time, running, mode
    
    if running:
        minutes, seconds = divmod(remaining_time, 60)
        time_str = f"{int(minutes):02}:{int(seconds):02}"
        timer_label.config(text=time_str)

        if remaining_time > 0:
            remaining_time -= 1
            root.after(1000, update_timer)
        else:
            if mode == "Study":
                winsound.Beep(1000, 500)
                mode = "Break"
                remaining_time = break_duration.get() * 60
                status_label.config(text="Break Time!")
            else:
                winsound.Beep(1000, 500)
                mode = "Study"
                remaining_time = study_duration.get() * 60
                status_label.config(text="Study Time!")
            update_timer()

# Function to start the timer
def start_timer():
    global running, remaining_time, mode
    if not running:
        running = True
        mode = "Study"
        remaining_time = study_duration.get() * 60
        status_label.config(text="Study Time!")
        update_timer()

# Function to stop the timer
def stop_timer():
    global running
    running = False

# Function to reset the timer
def reset_timer():
    global running, remaining_time, mode
    running = False
    remaining_time = 0
    timer_label.config(text="00:00")
    status_label.config(text="")

root = tk.Tk()
root.title("Study Timer")

# Variables
running = False
remaining_time = 0
mode = "Study"

# Timer Label
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# Status Label
status_label = tk.Label(root, text="", font=("Helvetica", 24))
status_label.pack(pady=10)

# Study Duration Input
tk.Label(root, text="Study Duration (minutes):").pack(pady=5)
study_duration = tk.IntVar(value=25)
tk.Entry(root, textvariable=study_duration).pack()

# Break Duration Input
tk.Label(root, text="Break Duration (minutes):").pack(pady=5)
break_duration = tk.IntVar(value=5)
tk.Entry(root, textvariable=break_duration).pack()

# Control Buttons
start_button = tk.Button(root, text="Start", command=start_timer, font=("Helvetica", 16))
start_button.pack(side="left", padx=10)

stop_button = tk.Button(root, text="Stop", command=stop_timer, font=("Helvetica", 16))
stop_button.pack(side="left", padx=10)

reset_button = tk.Button(root, text="Reset", command=reset_timer, font=("Helvetica", 16))
reset_button.pack(side="left", padx=10)

root.mainloop()
