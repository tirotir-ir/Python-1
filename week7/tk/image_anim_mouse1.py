# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a Canvas widget
canvas = Canvas(win, width=600, height=400, bg="white")
canvas.pack(pady=20)

# Add Images to Canvas widget
image = ImageTk.PhotoImage(Image.open('canvas.png'))
img = canvas.create_image(250, 120, anchor=NW, image=image)

def left(e):
   x = -20
   y = 0
   canvas.move(img, x, y)

def right(e):
   x = 20
   y = 0
   canvas.move(img, x, y)

def up(e):
   x = 0
   y = -20
   canvas.move(img, x, y)

def down(e):
   x = 0
   y = 20
   canvas.move(img, x, y)

# Define a function to allow the image to move within the canvas
def move(e):
   global image
   image = ImageTk.PhotoImage(Image.open('canvas.png'))
   img = canvas.create_image(e.x, e.y, image=image)

# Bind the move function
canvas.bind("<B1-Motion>", move)

win.mainloop()