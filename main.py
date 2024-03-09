#pip install speechrecognition
#pip insall pyttsx3
#pip install pyaudio

import speech_recognition as sr
import pyttsx3

recognizer = sr.recognizer()

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(text)
    except:
        pass