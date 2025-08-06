import tkinter as tk

root = tk.Tk()
root.title("tirotir")

root.configure(bg="lightblue")

label = tk.Label(root, text="Hello, World!", fg="white", bg="blue", font=("Arial", 24, "bold"))
label.pack(padx=20, pady=20)

# Run the application
root.mainloop()
