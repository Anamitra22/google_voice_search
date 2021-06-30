import speech_recognition as sr
import pyttsx3
from googlesearch import search

engine = pyttsx3.init()

def voice_call(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

def get_search():
    try:
        with sr.Microphone() as source:
            print('listening........')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass




def srch():
    try:
        voice_call('What do you want to search')
        query = get_search()
        for j in search(query, tld = "co.in", num = 10, stop=10,pause=2):
            print(j)
    except:
        pass

srch()




