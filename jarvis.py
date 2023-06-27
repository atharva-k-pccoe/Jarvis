import datetime
from unittest import result
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices)
engine.setProperty('voice', voices[0].id)
 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe() :
    hour = int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good Morning!") 
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may i help you")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")    
        query = r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)


        print ("Say that again please...")   
        return "None"
    return query  

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yoursemail@gmail.com','your-password')
    server.sendmail('yoursemail@gmail.com',to,content)
    server.close()




   

if __name__ == "__main__":
   wishMe()
   if 1:

    query = takeCommand().lower()

    if 'wikipedia'in query:
        speak('Searching Wikipedia..')
        query = query.replace("wikipedia","")
        results= wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open chrome' in query:
        webbrowser.open("chrome.com")

    elif 'open animixplay' in query:
        webbrowser.open("animixplay.to")

    elif 'play music' in query:
        music_dir= 'F:\\Music\\songs'  
        songs =os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))


    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir, the time is {strTime}")
        speak(f"Sir, the time is {strTime} ")

    elif 'open spotify' in query:
        spotify= "C:\\Users\\LENOVO\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(spotify)   

    elif 'email to atharva' in query:
        try:
            speak("What should i write?")
            content = takeCommand()
            to="atharvakusurkar12@gmail.com" 
            sendEmail(to,content) 
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry we are unable to send this email")      


   
    
    



