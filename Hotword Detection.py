import speech_recognition as sr
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
        print("Could not hear Say that again please...")
        query=""
        return query
    return query    
 

state="active"
def InactiveTC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-in')
    except Exception as e:
        query=""
        return query
    return query    
def LookforHword(state):
    while(True):
        query=InactiveTC().lower()
        if "python" in query:
            state="active"
            print(state)
            break
        else:
            if query=="":
                pass
            else:
                print(query)
            continue
        break

def Activate(state):
    if __name__ ==  "__main__":
        while True:
             query =  takeCommand().lower()
             if query=="":
                 state="inactive"
                 print(state)
                 LookforHword(state)
             elif query=="ok":
                break
Activate("active")        