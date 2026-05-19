import time

from input.listener import ouvir, detectar_modo
from brain.controller import Controller
from output.speaker import falar

class Engine:

    def __init__(self):
        self.controller = Controller()

    def run(self):

        print("Lary iniciada... segure 1 ou 2")

        try:

            while True:

                modo = detectar_modo()

                if not modo:
                    time.sleep(0.05)
                    continue

                texto = ouvir()

                if not texto:
                    continue

                resposta = self.controller.handle(texto, modo)

                if resposta:
                    falar(resposta)

        except KeyboardInterrupt:
            print("Lary encerrada 😏")