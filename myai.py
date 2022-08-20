import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty( voices , voices[1].id)
# engine.setProperty('rate',125)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour< 16:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("I am Bosko. How may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # print(f"User said: {query}\n")
        print(query)
        # speak(query)
        

    except Exception as e:
        print("Say again please....")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kriyanshjain01@gmail.com', 'Kriyansh@2001')
    server.sendmail('kriyanshjain01@gmail.com',to,content)
    server.close()

def readNews():
    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=e0a3efc93ae84b998aa133f77f504700')
    newsSay = json.loads(r.content)
    speak(newsSay)


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()


        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query =  query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak('according to wikipedia..')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir = 'F:\\series\\Friends 1'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'semester 6' in query:
            sempath = 'C:\\Users\\hp\\Desktop\\sem6'
            os.startfile(sempath)

        elif 'email to' in query:
            try:
                speak("what should i say")
                content = takecommand()
                to = "kriyansh2001@gmail.com"
                sendemail(to, content)
                speak("email send")
            except Exception as e:
                print(e)

        elif 'read news' in query:
            readNews()
