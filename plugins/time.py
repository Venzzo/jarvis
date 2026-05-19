from datetime import datetime
from plugins.base import BasePlugin

class TimePlugin(BasePlugin):

    def match(self, texto):

        palavras = [
            "hora",
            "horas",
            "que horas são",
            "me diz a hora"
        ]

        return any(p in texto for p in palavras)

    def run(self, texto, context, memory):
        return f"Agora são {datetime.now().strftime('%H:%M')}"