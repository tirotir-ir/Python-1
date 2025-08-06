import tkinter as tk

root = tk.Tk()
root.title("KHoozestan")
root.geometry('300x200')
label = tk.Label(root, text="Hello!")
label.pack()

label = tk.Label(root, text="World!")
label.pack()

root.mainloop()
