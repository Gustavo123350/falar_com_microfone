import speech_recognition as sr
from gtts import gTTS
import os

def listen_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='pt-br')
        print("Você disse: ", text)
        return text
    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
        return None
    except sr.RequestError as e:
        print("Não foi possível completar a solicitação; {0}".format(e))
        return None

def text_to_speech(text, language='pt-br'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3") 

if __name__ == "__main__":
    while True:
        input_text = listen_microphone()
        if input_text is not None and input_text.lower() == "sair":
            print("Encerrando o programa.")
            break
        elif input_text is not None:
            response = "Você disse: " + input_text
            text_to_speech(response)
