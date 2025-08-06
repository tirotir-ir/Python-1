import tkinter as tk

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=5)

# Create the main window
root = tk.Tk()
root.title("Drawing App")

# Create a canvas widget
canvas = tk.Canvas(root, bg="white", width=400, height=400)
canvas.pack()

# Bind the paint function to mouse motion
canvas.bind("<B1-Motion>", paint)

# Run the application
root.mainloop()
