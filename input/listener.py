import speech_recognition as sr
import keyboard
import visual.state as state


def ouvir():

    state.STATE = "listening"

    r = sr.Recognizer()

    with sr.Microphone() as source:

        audio = r.listen(source)

    try:

        texto = r.recognize_google(
            audio,
            language="pt-BR"
        ).lower()

        state.STATE = "thinking"

        return texto

    except:

        state.STATE = "idle"

        return ""

def detectar_modo():
    if keyboard.is_pressed("1"):
        return "1"
    elif keyboard.is_pressed("2"):
        return "2"
    return None
