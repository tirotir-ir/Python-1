import tkinter as tk
root = tk.Tk()
root.title('Title')
root.geometry('300x200')
button = tk.Button(root, text='Click Me', command=None)
label = tk.Label(root, text='Hello, World!')
label.pack()
button.pack()
root.mainloop()