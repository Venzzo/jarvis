import pyttsx3
import visual.state as state

from config.settings import USE_ELEVEN
from output.eleven import falar_eleven

engine = pyttsx3.init()

def falar(texto):
    state.STATE = "speaking"
    if USE_ELEVEN:
        falar_eleven(texto)

    else:
        engine.say(texto)
        engine.runAndWait()
        
    state.STATE = "idle"