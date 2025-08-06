from gtts import gTTS
from playsound import playsound

tts = gTTS(text='Hello World!', lang='en')
tts.save("hello_world.mp3")

playsound("hello_world.mp3")
