#pip install speechrecognition
#pip insall pyttsx3
#pip install pyaudio

import speech_recognition as sr
import pyttsx3

recognizer = sr.recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f'Recognized:{text}')
    except speech_recognition.UnknownValueError:
        recognisation = 