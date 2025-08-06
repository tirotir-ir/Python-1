import tkinter as tk
from PIL import Image, ImageTk

class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Game")

        # Load and display the animated GIF
        self.load_animated_gif()

        self.points = 0
        self.label = tk.Label(root, text=f"Points: {self.points}")
        self.label.pack()

        self.canvas.bind("<Button-1>", self.on_click)

        # Start the animation loop
        self.animate()

    def load_animated_gif(self):
        # Load the animated GIF using PIL (Python Imaging Library)
        self.gif_img = Image.open("hamster_anim.gif")
        self.gif_photo = ImageTk.PhotoImage(self.gif_img)
        self.canvas = tk.Canvas(self.root, width=self.gif_img.width, height=self.gif_img.height)
        self.canvas_img = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.gif_photo)
        self.canvas.pack()

    def animate(self):
        # Ensure the GIF loops indefinitely
        self.animating = True
        self.animate_gif()

    def animate_gif(self):
        try:
            if self.animating:
                # Move to the next frame
                self.gif_img.seek(self.gif_img.tell() + 1)
                self.gif_photo = ImageTk.PhotoImage(self.gif_img)
                self.canvas.itemconfig(self.canvas_img, image=self.gif_photo)
                self.root.after(50, self.animate_gif)
        except EOFError:
            # Restart the animation from the beginning if it reaches the end
            self.gif_img.seek(0)
            self.animate_gif()

    def on_click(self, event):
        # Check if click is within the bounds of the animated GIF
        if (0 <= event.x <= self.gif_img.width) and (0 <= event.y <= self.gif_img.height):
            self.points += 1
            self.label.config(text=f"Points: {self.points}")

# Main function to start the game
def main():
    root = tk.Tk()
    game = ClickGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
