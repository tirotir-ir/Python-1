import tkinter as tk
import time

a = 0

root = tk.Tk()
label = tk.Label(root)
label.pack()

for i in range(10):
    label['text'] = a  
    a += 1    
    root.update()
    time.sleep(1)  

root.mainloop()
