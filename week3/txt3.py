import time
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

def display_and_speak_text(text):
    for letter in text:
        print(letter, end='', flush=True)
        engine.say(letter)
        engine.runAndWait()
        time.sleep(1)


# Example usage
text_to_display = input('Enter any word: ')
display_and_speak_text(text_to_display)
