#Working 
import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()
mic = sr.Microphone()
translator = Translator()


def record_audio():  
    with mic as source:
        print("Recording...")       
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        if text is None:
            print("Could not recognize speech. Please try again.")
            return None
        else:
            return text 
def translate(text):
    try:
        result = translator.translate(text,dest='en')
        return result  
    except Exception as e:
        print(f"Translation failed: {e}")
def main():
    try:
        text = record_audio()
        if text is not None:
            print("You said: {}".format(text)) 
    except sr .RequestError:
        print("API request failed")
    except sr. UnknownValueError:
        print("API could not recognise the speech")

    # Translate the speech
    
    try:
        result = translate('Daoonga Buktan Rukkar khari daoong ke sath, dokada din nahi karni jai hai')
        print(result.text)    
    except Exception as e:
        print(f"Translation failed: {e}")


if __name__ == "__main__":
    main()