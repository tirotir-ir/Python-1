import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def text_to_speech():
    text = entry.get()
    if text:
        # Create a valid filename by replacing spaces with underscores and removing special characters
        filename = "".join(x if x.isalnum() else "_" for x in text) + ".mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        os.system(f"start {filename}")
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

button = tk.Button(root, text="Convert to Speech", command=text_to_speech)
button.pack(pady=10)

# Run the application
root.mainloop()
