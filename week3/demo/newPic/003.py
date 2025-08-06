import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Create the main window
root = tk.Tk()

# Open the animated GIF file
gif = Image.open('caveman_beating_drum_ha.gif')

# Create a label to display the GIF
label = tk.Label(root)
label.pack()

# Function to update the GIF frame
def update(frame_iterator):
    try:
        frame = next(frame_iterator)
    except StopIteration:
        # Reset the iterator if the end is reached
        frame_iterator = ImageSequence.Iterator(gif)
        frame = next(frame_iterator)
    img = ImageTk.PhotoImage(frame)
    label.config(image=img)
    label.image = img
    root.after(100, update, frame_iterator)

# Start displaying the GIF
update(ImageSequence.Iterator(gif))

# Run the application
root.mainloop()
