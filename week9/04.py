import tkinter as tk
from tkinter import messagebox, filedialog
from gtts import gTTS
import os

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
            os.system(f"start {save_path}")
    else:
        messagebox.showwarning("Input Error", "Please enter some text.")

# Create the main window
root = tk.Tk()
root.title("Text to Speech")

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

button = tk.Button(root, text="Convert to Speech", command=text_to_speech)
button.pack(pady=10)

# Run the application
root.mainloop()
