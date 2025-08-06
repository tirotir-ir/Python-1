import tkinter as tk

root = tk.Tk()
root.title("اعداد زوج دو رقمی")

number = 10
even_numbers = []
while number < 100:
    if number % 2 == 0:
        even_numbers.append(str(number))
    number += 1

result_label = tk.Label(root, text="\n".join(even_numbers), justify="left")
result_label.pack()

root.mainloop()
