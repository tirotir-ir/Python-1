import tkinter as tk
import random

class FullScreenMessage:
    def __init__(self, root):
        self.root = root
        self.root.title("Taskbar Moved")
        
        # Make the window full screen
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', self.exit_full_screen)
        
        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Display the text "Taskbar Moved!" in the center of the screen
        self.text = self.canvas.create_text(
            self.root.winfo_screenwidth() // 2,
            self.root.winfo_screenheight() // 2,
            text="Taskbar Moved!",
            fill='black',
            font=('Helvetica', 50, 'bold')
        )
        
        self.flash_text()
    
    def flash_text(self):
        # Change the text color to a random color every 500 milliseconds
        colors = ['red', 'green', 'blue', 'yellow', 'black', 'magenta', 'cyan']
        current_color = self.canvas.itemcget(self.text, 'fill')
        new_color = random.choice([color for color in colors if color != current_color])
        self.canvas.itemconfig(self.text, fill=new_color)
        
        # Call this method again after a short delay
        self.root.after(500, self.flash_text)
    
    def exit_full_screen(self, event):
        self.root.attributes('-fullscreen', False)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    simulator = FullScreenMessage(root)
    root.mainloop()
