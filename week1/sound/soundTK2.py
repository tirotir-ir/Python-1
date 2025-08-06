import tkinter as tk
from tkinter import filedialog
import pygame

# تابع برای انتخاب فایل صوتی
def choose_file():
    file_path = filedialog.askopenfilename(
        title="انتخاب فایل صوتی",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
    )
    if file_path:
        play_sound(file_path)

# تابع برای پخش صدای انتخاب شده
def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # بررسی وضعیت پخش صدا
    check_music()

# بررسی وضعیت پخش صدا برای نگه داشتن برنامه در حین پخش
def check_music():
    if pygame.mixer.music.get_busy():
        window.after(100, check_music)
    else:
        print("پخش صدا تمام شد")

# مقداردهی اولیه pygame mixer
pygame.mixer.init()

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("پخش‌کننده صدا")
window.geometry("300x150")

# ایجاد دکمه انتخاب فایل
choose_button = tk.Button(window, text="انتخاب فایل صوتی", command=choose_file, font=("Arial", 16))
choose_button.pack(pady=40)

# اجرای حلقه اصلی GUI
window.mainloop()
