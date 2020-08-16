import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import datetime
import wolframalpha
import os
import sys
import time
from playsound import playsound
voice = pyttsx3.init()


voice = voice.getProperty('voices')
voice.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('FRIDAY: ' + audio)
    voice.say(audio)
    voice.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')


def google(text):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

        # to search

    for j in search(text, tld="co.in", num=1, stop=1, pause=1):
        webbrowser.open(j)
def caller():
   
    r1 = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r1.pause_threshold =  1
        audio1 = r1.listen(source)
    try:
        query1 = r1.recognize_google(audio1, language='en-in')
        print('User: ' + query1 + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query1 = str(input('Command: '))

    return query1

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query



call = caller()
call = call.lower()
if  "friday" in call  or "hey buudy" in call or "hey buddy are you there" in call or "hey friday are you there" in call or "hey friday" in call:
    if __name__ == '__main__':
        greetMe()
        speak('Hello Sir, I am your digital assistant Friday!')
        speak('How may I help you?')
        while True:
            #file = open("LEARN.txt")

            query = myCommand()
            query = query.lower()


            if "who built you" in query or "who make you" in query or "who made you" in query:
                speak("i love to answer that question")
                speak("Aswin buld me")
            


            elif "what\'s up" in query or 'how are you' in query:
                sayEny = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(sayEny))


            elif 'hello' in query:
                speak('Hello Sir')



            elif 'play music' in query:
                #music_folder = "E:\Music\English"
                music = ['E:\Music\English\Akon\Akon - Angel.mp3','E:\Music\English\B.o.B\B.o.B - So Good.mp3',
                'E:\Music\English\B.o.B\B.o.B - Headband.mp3','E:\Music\English\B.o.B\B.o.B - Airplanes.mp3',
                'E:\Music\English\Akon\Akon - Be With You.mp3']
                #music = ["E:\Music\English\50 cent"]
                random_music = random.choice(music)
                playsound(random_music)
                        
                speak('Okay, here is your music! Enjoy!')

            elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:
                speak('okay')
                speak('Bye Sir, have a good day.')
                sys.exit()


            else:
                google(query)
            
            speak('Next Command! Sir!')
