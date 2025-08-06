import tkinter as tk
from tkinter import messagebox


def hi():
    h='Hello'
    messagebox.showinfo("tirotir", f"welcome and {h}")

root = tk.Tk()
root.title("KHoozestan")
root.geometry('300x200')
label = tk.Label(root, text="Hello!", bg="yellow", fg="red", font='18')
label.pack()

label = tk.Label(root, text="World!")
label.pack()

tk.Button(root, text="ok", command=hi).pack()


root.mainloop()
