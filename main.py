import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.say("Hi, my name is Ava! How can I help you today?")
engine.runAndWait()