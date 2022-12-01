import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
from AppOpener import run
import os

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data =recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            return "not understand"
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    rate =engine.getProperty('rate')
    engine.setProperty('rate',170)
    engine.say(x)
    engine.runAndWait()
if __name__=="__main__":
    count=0

    #if sptext().lower() =="hey dumbo":
    while(True):
        data1=sptext().lower()
        print(data1)
        if "your name" in data1:
            name="my name is dumbo"
            speechtx(name)
        elif "old are you"in data1:
            age="my age is 10"
            speechtx(age)
        elif "love you"in data1:
            reply=" i love u as a friend"
            speechtx(reply)
        elif "now time"in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube"in data1:
            speechtx("opening youtube")
            webbrowser.open("youtube.com")
        elif "open google"in data1:
            speechtx("opening google")
            webbrowser.open("google.com")
        elif "spotify"in data1:
            speechtx("opening spotify")
            run("spotify")
        elif "chrome"in data1:
            speechtx("opening chrome")
            run("chrome")  
        elif "joke"in data1:
            joke_1=pyjokes.get_joke(language="en", category="neutral")
            speechtx(joke_1)
        elif "bye" in data1:
            speechtx("haan haan jaa rahi hu ,jaldi bor ho gaye muzhse")
            break
        else:
            # if count==2:
            #     speechtx("thankyou bye")
            #     break
            #else:
                speechtx("not understand")
                count+=1
