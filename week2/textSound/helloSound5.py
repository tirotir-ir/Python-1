from gtts import gTTS
import os

# Function to speak text
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")

# Get user's name
name = input("Enter your name: ")

# Create personalized greeting
greeting = f"Hello, {name}! Welcome to the world of Python."

# Print and speak the greeting
print(greeting)
speak(greeting)
