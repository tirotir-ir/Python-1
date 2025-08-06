import tkinter as tk
from tkinter import messagebox
import random
from gtts import gTTS
import os

# Function to speak text
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")

# Function to generate and speak a random fact
def offer_fact():
    facts = [
        "Did you know that the Python programming language was named after Monty Python's Flying Circus?",
        "Python was created by Guido van Rossum and first released in 1991.",
        "Python is known for its simplicity and readability, making it a popular choice for beginners and professionals alike."
    ]
    random_fact = random.choice(facts)
    speak(random_fact)

# Function to handle the greet button click event
def greet():
    global greet_count
    name = entry_name.get()
    if name:
        greeting = f"Hello, {name}! Welcome to the Python World. This is greeting number {greet_count}."
    else:
        greeting = f"Hello! Welcome to the Python World. This is greeting number {greet_count}."
    messagebox.showinfo("Greeting", greeting)
    speak(greeting)
    greet_count += 1

# Function to handle the exit button click event
def exit_app():
    window.destroy()

# Initialize greet counter
greet_count = 1

# Create the main window
window = tk.Tk()
window.title("Greetings and Facts")
window.geometry("400x300")

# Create a label
label_name = tk.Label(window, text="Enter your name:")
label_name.pack(pady=10)

# Create an entry for user's name
entry_name = tk.Entry(window, width=30)
entry_name.pack(pady=5)

# Create a button for greeting
button_greet = tk.Button(window, text="Greet Me", command=greet)
button_greet.pack(pady=10)

# Create a button for random fact
button_fact = tk.Button(window, text="Random Fact", command=offer_fact)
button_fact.pack(pady=10)

# Create a button to exit
button_exit = tk.Button(window, text="Exit", command=exit_app)
button_exit.pack(pady=10)

# Run the main loop
window.mainloop()
