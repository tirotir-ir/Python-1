#pip install gtts
from gtts import gTTS
import os

text = input('some text: ')

tts = gTTS(text=text, lang='en')

tts.save("hello.mp3")

# Play the audio file
os.system("start hello.mp3")