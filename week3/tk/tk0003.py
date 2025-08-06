import tkinter as tk

# تابع 
def greet():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!", bg="lightgreen")
    else:
        greeting_label.config(text="Please enter your name.", bg="lightcoral")

# پنجره اصلی
root = tk.Tk()
root.title("Hello App")

# تنظیم رنگ پس‌زمینه پنجره اصلی
root.configure(bg="lightblue")

# ایجاد یک ورودی برای نام کاربر
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(padx=20, pady=10)

# ایجاد یک دکمه برای صدا زدن تابع
greet_button = tk.Button(root, text="Greet Me", command=greet, font=("Arial", 14))
greet_button.pack(padx=20, pady=10)

# ایجاد یک برچسب خالی برای نمایش نتیجه تابع
greeting_label = tk.Label(root, text="", fg="black", font=("Arial", 24, "bold"))
greeting_label.pack(padx=20, pady=20)

# اجرای دائمی برنامه
root.mainloop()
