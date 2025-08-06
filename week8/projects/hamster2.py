import tkinter as tk
from PIL import Image, ImageTk
import random

class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Game")

        # Load and display the hamster image
        self.load_hamster_image()

        self.points = 0
        self.label = tk.Label(root, text=f"Points: {self.points}")
        self.label.pack()

        self.canvas.bind("<Button-1>", self.on_click)

    def load_hamster_image(self):
        # Load the hamster image using PIL (Python Imaging Library)
        self.hamster_img = Image.open("hamster.jpg")
        self.hamster_photo = ImageTk.PhotoImage(self.hamster_img)
        self.canvas = tk.Canvas(self.root, width=self.hamster_img.width, height=self.hamster_img.height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.hamster_photo)
        self.canvas.pack()

    def on_click(self, event):
        # Check if click is within the bounds of the hamster image
        if (0 <= event.x <= self.hamster_img.width) and (0 <= event.y <= self.hamster_img.height):
            self.points += 10
            self.label.config(text=f"Points: {self.points}")

# Main function to start the game
def main():
    root = tk.Tk()
    game = ClickGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
