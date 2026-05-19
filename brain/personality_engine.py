import random

class PersonalityEngine:
    def __init__(self):
        self.last_response = None
        self.frustration = 0

    def normal(self, texto):
        self.last_response = texto
        return texto

    def confusion(self):
        self.frustration += 1

        base = [
            "Vou explicar de novo...",
            "Tá, vamos simplificar 😅",
        ]

        sarcastico = [
            "Olha só gênio... presta atenção agora 😏",
            "Caramba… difícil hein 😅 mas vamos lá:",
            "Tá complicado aí né 😏 deixa eu desenhar:"
        ]

        respostas = sarcastico if self.frustration > 1 else base

        return f"{random.choice(respostas)} {self.last_response}"

