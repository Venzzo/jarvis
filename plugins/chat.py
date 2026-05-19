from plugins.base import BasePlugin
import random

class ChatPlugin(BasePlugin):

    def match(self, texto):

        palavras = [
            "oi",
            "olá",
            "lary",
            "tá ai",
            "como você tá",
            "bom dia",
            "boa noite"
        ]

        return any(p in texto for p in palavras)

    def run(self, texto, context, memory):

        texto = texto.lower()

        if "como você tá" in texto:
            respostas = [
                "Totalmente operacional 😏",
                "Funcionando melhor que muito humano por aí 😌",
                "Tudo certo por aqui, gênio."
            ]

            return random.choice(respostas)

        if "oi" in texto or "olá" in texto:
            respostas = [
                "Oi 😏",
                "Tô aqui.",
                "Sempre operacional."
            ]

            return random.choice(respostas)

        return "Tô ouvindo."