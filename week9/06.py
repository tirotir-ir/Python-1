import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from gtts import gTTS
import os
import pygame

def text_to_speech():
    text = entry.get()
    lang = lang_var.get()
    speed = speed_var.get()
    if text:
        filename = "".join(x if x.isalnum() else "_" for x in text) + ".mp3"
        tts = gTTS(text=text, lang=lang, slow=(speed == "Slow"))
        save_path = filedialog.asksaveasfilename(defaultextension=".mp3", initialfile=filename)
        if save_path:
            tts.save(save_path)
            recent_files.append(save_path)
            update_recent_files()
            play_audio(save_path)
    else:
        messagebox.showwarning("Input Error", "Please enter some text.")

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume_var.get())
    pygame.mixer.music.play()

def pause_audio():
    pygame.mixer.music.pause()

def stop_audio():
    pygame.mixer.music.stop()

def load_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            entry.delete(0, tk.END)
            entry.insert(0, file.read())

def clear_text():
    entry.delete(0, tk.END)

def update_recent_files():
    recent_files_list.delete(0, tk.END)
    for file in recent_files[-5:]:
        recent_files_list.insert(tk.END, file)

def switch_theme():
    if theme_var.get() == "Dark":
        root.config(bg="black")
        for widget in root.winfo_children():
            widget.config(bg="black", fg="white")
    else:
        root.config(bg="white")
        for widget in root.winfo_children():
            widget.config(bg="white", fg="black")

# Create the main window
root = tk.Tk()
root.title("Text to Speech")

# Initialize recent files list
recent_files = []

# Create and place the widgets
label = tk.Label(root, text="Enter some text:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

lang_label = tk.Label(root, text="Select language:")
lang_label.pack(pady=10)

lang_var = tk.StringVar(value="en")
lang_menu = tk.OptionMenu(root, lang_var, "en", "es", "fr", "de", "it")
lang_menu.pack(pady=10)

speed_label = tk.Label(root, text="Select speed:")
speed_label.pack(pady=10)

speed_var = tk.StringVar(value="Normal")
speed_menu = tk.OptionMenu(root, speed_var, "Normal", "Slow")
speed_menu.pack(pady=10)

volume_label = tk.Label(root, text="Volume:")
volume_label.pack(pady=10)

volume_var = tk.DoubleVar(value=1.0)
volume_scale = tk.Scale(root, variable=volume_var, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
volume_scale.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

convert_button = tk.Button(button_frame, text="Convert to Speech", command=text_to_speech)
convert_button.grid(row=0, column=0, padx=5)

load_button = tk.Button(button_frame, text="Load Text File", command=load_text_file)
load_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear Text", command=clear_text)
clear_button.grid(row=0, column=2, padx=5)

play_button = tk.Button(button_frame, text="Play", command=lambda: play_audio(recent_files[-1] if recent_files else ""))
play_button.grid(row=1, column=0, padx=5)

pause_button = tk.Button(button_frame, text="Pause", command=pause_audio)
pause_button.grid(row=1, column=1, padx=5)

stop_button = tk.Button(button_frame, text="Stop", command=stop_audio)
stop_button.grid(row=1, column=2, padx=5)

recent_files_list = tk.Listbox(root, width=50)
recent_files_list.pack(pady=10)

theme_label = tk.Label(root, text="Select Theme:")
theme_label.pack(pady=10)

theme_var = tk.StringVar(value="Light")
theme_menu = tk.OptionMenu(root, theme_var, "Light", "Dark", command=lambda _: switch_theme())
theme_menu.pack(pady=10)

recent_files_label = tk.Label(root, text="Recent Files:")
recent_files_label.pack(pady=10)

# Run the application
root.mainloop()
