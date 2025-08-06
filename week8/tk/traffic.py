import tkinter as tk

def change_light():
    global current_light
    if current_light == "red":
        canvas.itemconfig(light_red, fill="gray")
        canvas.itemconfig(light_green, fill="green")
        current_light = "green"
    elif current_light == "green":
        canvas.itemconfig(light_green, fill="gray")
        canvas.itemconfig(light_yellow, fill="yellow")
        current_light = "yellow"
    elif current_light == "yellow":
        canvas.itemconfig(light_yellow, fill="gray")
        canvas.itemconfig(light_red, fill="red")
        current_light = "red"
    root.after(1000, change_light)

# Create the main window
root = tk.Tk()
root.title("Traffic Light Simulator")

# Create a canvas widget to draw the traffic light
canvas = tk.Canvas(root, width=200, height=300, bg="white")
canvas.pack()

# Draw the traffic light
canvas.create_rectangle(50, 50, 150, 250, outline="black", width=2)
light_red = canvas.create_oval(75, 60, 125, 110, fill="gray")
light_yellow = canvas.create_oval(75, 120, 125, 170, fill="gray")
light_green = canvas.create_oval(75, 180, 125, 230, fill="gray")

current_light = "red"
canvas.itemconfig(light_red, fill="red")

# Start the light change loop
root.after(1000, change_light)

# Run the application
root.mainloop()
