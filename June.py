import wikipedia as wiki
import speech_recognition as sr
from gtts import gTTS
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source, duration = 1)
    audio_text = r.listen(source)
    print("Time over, thanks")

user_input = r.recognize_google(audio_text)

print("Searching for :", user_input)

language = 'en'
search_input = wiki.suggest(user_input)
if search_input == "None":
    print("No Suggestions found.")
else:
    result = wiki.summary(str(search_input), sentences = 4)
    output = gTTS(text=result, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

choice = input("Want more details [Y/N] : ")
if choice == "y" or choice == "Y":
    result = wiki.summary(str(search_input))
    output = gTTS(text=result, lang=language, slow=False)
    output.save("output1.mp3")
    os.system("start output1.mp3")
elif choice == "n" or choice == "N":
    print("Thank you for using.")
else:
    print("Wrong Input.")
