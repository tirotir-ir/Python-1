import tkinter as tk
import pygame

def play_sound():
    pygame.mixer.music.load(r'E:\PYTHON\Term1\pythonWeeks1\week1\sound\alivesound.mp3')
    pygame.mixer.music.play()

# مقداردهی اولیه pygame mixer
pygame.init()
# pygame.mixer.init()


# ایجاد پنجره اصلی
window = tk.Tk()
window.title("پخش‌کننده صدا")
window.geometry("300x150")

# ایجاد دکمه پخش صدا
play_button = tk.Button(window, text="پخش صدا", command=play_sound, font=("Arial", 16))
play_button.pack(pady=40)

# اجرای حلقه اصلی GUI
window.mainloop()
