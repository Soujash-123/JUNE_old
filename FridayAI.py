import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import string
import random
import os
import pywhatkit as kit
import calendar




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',190)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hello Sir I am Friday how may I help you ")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
    
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        print("Recognizing....")    
        query = r.recognize_google(audio,language='en-in')
        print(f"Sir said:{query}\n")
    except Exception as e:
        speak("Could not hear Say that again please...")
        return "None" 
    return query    
 



if __name__ ==  "__main__":
    wishMe()
    while True:
     query =  takeCommand().lower()
    
     if "wikipedia" in query:
         speak("Searching wikipedia")
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query, 3)
         speak("According to wikipedia")
         print(results)
         speak(results)
     elif "open youtube" in query :
         speak("Opening Youtube")
         webbrowser.open("https://www.youtube.com/")
     elif "open google" in query:
         speak("Opening Google")
         webbrowser.open("https://www.google.com/")    
     elif "open stackoverflow" in query:
        webbrowser.open("stakeoverflow.com")    
     elif "what is the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is{strTime}")
     
     elif "open instagram" in query:
         speak("Opening instagram")
         webbrowser.open("https://www.instagram.com/")
    
     elif "friday tell me about yourself" in query:
         speak("Sir I am your personal assistant I work for you 24 into 7 You is a nice person and i love you very much")
     elif "show me this month calender" in query:
         cal = calendar.month(2020,11)
         speak("Sir ,here is this months calender",cal)
     
     elif "suggest password" in query:
        if __name__ == "__main__":
         s1 = string.ascii_lowercase
    
         s2 = string.ascii_uppercase
    
         s3 = string.digits
    
         s4 = string.punctuation
    
         plen =int(input("Enter a password length\n"))
         speak(plen)
         s = []
         s.extend(list(s1))
         s.extend(list(s2))
         s.extend(list(s3))
         s.extend(list(s4))
    
         random.shuffle(s)
     
         print("".join(s[0:plen]))
         speak("".join(s[0:plen]))
     
     elif "stop" in query:
         speak("Goodbye,see you soon")
         exit()
     elif "send message" in query:
         kit.sendwhatmsg("+917595839899","HI",18,30)
         speak("Sending message...")
     elif "show me the calendar" in query:
          speak("Enter year please")
          year = int(input("Enter Year"))
          speak("Enter month please")
          month  = int(input("Enter month"))
          cal = calendar.month(year,month)
          print(cal)
          speak("Here you go Sir")
