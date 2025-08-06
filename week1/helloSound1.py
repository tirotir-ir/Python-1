import pyttsx3
a=input('what to say? ')
engine = pyttsx3.init()
#engine.say("Hello World!")
engine.say(a)
engine.runAndWait()