import tkinter as tk
import random

class FullScreenAntAndRainSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Ant and Rain Simulator")
        
        # Make the window full screen
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', self.exit_full_screen)
        
        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.ants = []
        self.num_ants = 100
        self.drops = []
        self.num_drops = 150
        
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        
        # Create ants as small circles
        for _ in range(self.num_ants):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            ant = self.canvas.create_oval(x, y, x+5, y+5, fill='black')
            self.ants.append(ant)
        
        # Create raindrops as small lines
        for _ in range(self.num_drops):
            x = random.randint(0, self.width)
            y = random.randint(-self.height, 0)  # Start above the screen
            drop = self.canvas.create_line(x, y, x, y+10, fill='blue', width=2)
            self.drops.append(drop)
        
        self.update_simulation()
    
    def update_simulation(self):
        # Move ants
        for ant in self.ants:
            self.canvas.move(ant, random.randint(-5, 5), random.randint(-5, 5))
            self.ensure_within_bounds(ant)
        
        # Move raindrops
        for drop in self.drops:
            self.canvas.move(drop, 0, 5)
            if self.canvas.coords(drop)[1] > self.height:
                # Reset drop to the top of the screen
                self.canvas.coords(drop, self.canvas.coords(drop)[0], -10, self.canvas.coords(drop)[0], 0)
        
        # Update simulation
        self.root.after(50, self.update_simulation)
    
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
    simulator = FullScreenAntAndRainSimulator(root)
    root.mainloop()
