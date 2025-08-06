import tkinter as tk
import random

class FullScreenAntSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Ant Simulator")
        
        # Make the window full screen
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', self.exit_full_screen)
        
        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.ants = []
        self.num_ants = 100
        
        # Create ants as small circles
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        for _ in range(self.num_ants):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            ant = self.canvas.create_oval(x, y, x+5, y+5, fill='black')
            self.ants.append(ant)
        
        self.move_ants()
    
    def move_ants(self):
        for ant in self.ants:
            self.canvas.move(ant, random.randint(-5, 5), random.randint(-5, 5))
            self.ensure_within_bounds(ant)
        
        # Call this method again after a short delay
        self.root.after(100, self.move_ants)
    
    def ensure_within_bounds(self, ant):
        coords = self.canvas.coords(ant)
        x1, y1, x2, y2 = coords
        if x1 < 0: x1 = 0
        if y1 < 0: y1 = 0
        if x2 > self.width: x2 = self.width
        if y2 > self.height: y2 = self.height
        self.canvas.coords(ant, x1, y1, x2, y2)
    
    def exit_full_screen(self, event):
        self.root.attributes('-fullscreen', False)

if __name__ == "__main__":
    root = tk.Tk()
    simulator = FullScreenAntSimulator(root)
    root.mainloop()
