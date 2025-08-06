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
    status_label.config(text="در حال پخش...")

# تابع توقف صدا
def stop_sound():
    pygame.mixer.music.stop()
    status_label.config(text="پخش متوقف شد")

# تابع مکث صدا
def pause_sound():
    pygame.mixer.music.pause()
    status_label.config(text="مکث")

# تابع ادامه پخش صدا
def unpause_sound():
    pygame.mixer.music.unpause()
    status_label.config(text="ادامه پخش")

# تابع تنظیم صدا
def set_volume(val):
    volume = float(val)
    pygame.mixer.music.set_volume(volume)

# مقداردهی اولیه pygame mixer
pygame.mixer.init()

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("موزیک پلیر")
window.geometry("400x300")

# برچسب وضعیت پخش
status_label = tk.Label(window, text="فایلی انتخاب نشده", font=("Arial", 14))
status_label.pack(pady=10)

# دکمه انتخاب فایل
choose_button = tk.Button(window, text="انتخاب فایل صوتی", command=choose_file, font=("Arial", 14))
choose_button.pack(pady=10)

# دکمه پخش صدا
play_button = tk.Button(window, text="پخش", command=lambda: pygame.mixer.music.unpause(), font=("Arial", 14))
play_button.pack(pady=10)

# دکمه توقف صدا
stop_button = tk.Button(window, text="توقف", command=stop_sound, font=("Arial", 14))
stop_button.pack(pady=10)

# دکمه مکث صدا
pause_button = tk.Button(window, text="مکث", command=pause_sound, font=("Arial", 14))
pause_button.pack(pady=10)

# دکمه ادامه پخش صدا
unpause_button = tk.Button(window, text="ادامه", command=unpause_sound, font=("Arial", 14))
unpause_button.pack(pady=10)

# تنظیم‌کننده صدا
volume_slider = tk.Scale(window, from_=0, to=1, resolution=0.1, orient="horizontal", label="تنظیم صدا", command=set_volume)
volume_slider.set(0.5)
volume_slider.pack(pady=10)

# اجرای حلقه اصلی GUI
window.mainloop()
