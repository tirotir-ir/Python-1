import tkinter as tk

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        result.set("Error")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        result.set("Error")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        result.set("Error")

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ValueError:
        result.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root, width=10)
entry1.pack(pady=5)

entry2 = tk.Entry(root, width=10)
entry2.pack(pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, width=10)
result_label.pack(pady=5)

add_button = tk.Button(root, text="+", command=add)
add_button.pack(side="left", padx=5)

subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.pack(side="left", padx=5)

multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.pack(side="left", padx=5)

divide_button = tk.Button(root, text="/", command=divide)
divide_button.pack(side="left", padx=5)

root.mainloop()
