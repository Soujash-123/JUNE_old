import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',190)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
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
    
    while True:
     query =  takeCommand().lower()
     if "wikipedia" in query:
         speak("Searching wikipedia")
         query = query.replace("wikipedia" ,  " ")
         results = wikipedia.summary(query, 3)
         speak("According to wikipedia")
         print(results)
         speak(results)      
     elif "stop" in query:
         speak("Goodbye,see you soon")
         exit() 
