import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

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
        result = translator.translate(text, dest='kannada')
        return result  
    except Exception as e:
        print(f"Translation failed: {e}")


def text_to_speech(text, language='en'):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")
        audio = AudioSegment.from_mp3("output.mp3")
        play(audio)
    except Exception as e:
        print(f"Text-to-speech conversion failed: {e}")


def main():
    try:
        text = record_audio()
        if text is not None:
            print("You said:", text)
    except sr.RequestError:
        print("API request failed")
    except sr.UnknownValueError:
        print("API could not recognise the speech")

    # Translate the speech
    try:
        result = translate(text)
        translated_text = result.text
        print("Translated Text:", translated_text)
        text_to_speech(translated_text, 'kn')  # 'kn' for Kannada
    except Exception as e:
        print(f"Translation failed: {e}")


if __name__ == "__main__":
    main()
