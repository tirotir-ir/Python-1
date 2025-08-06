import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence

# Function to open and display the selected GIF file
def open_gif():
    # Open a file dialog to select a GIF file
    file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    if not file_path:
        return  # If no file is selected, do nothing

    # Open the selected GIF file
    gif = Image.open(file_path)

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

# Create the main window
root = tk.Tk()

# Create a button to open the GIF file
button = tk.Button(root, text="Choose GIF", command=open_gif)
button.pack()

# Create a label to display the GIF
label = tk.Label(root)
label.pack()

# Run the application
root.mainloop()
