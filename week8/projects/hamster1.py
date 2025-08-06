import tkinter as tk
import random

class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        self.points = 0
        self.label = tk.Label(root, text=f"Points: {self.points}")
        self.label.pack()

        self.create_picture()

        self.canvas.bind("<Button-1>", self.on_click)

    def create_picture(self):
        # Generate a random position for the picture
        self.picture_x = random.randint(50, 350)
        self.picture_y = random.randint(50, 350)
        self.picture = self.canvas.create_rectangle(self.picture_x, self.picture_y,
                                                    self.picture_x + 50, self.picture_y + 50,
                                                    fill='blue')

    def on_click(self, event):
        # Check if click is within the bounds of the picture
        if (self.picture_x <= event.x <= self.picture_x + 50) and \
           (self.picture_y <= event.y <= self.picture_y + 50):
            self.points += 10
            self.label.config(text=f"Points: {self.points}")
            self.canvas.delete(self.picture)
            self.create_picture()

# Main function to start the game
def main():
    root = tk.Tk()
    game = ClickGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
