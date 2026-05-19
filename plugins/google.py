import subprocess
from plugins.base import BasePlugin

class GooglePlugin(BasePlugin):

    def match(self, texto):

        palavras = [
            "google",
            "abre o google",
            "abrir google",
            "pesquisa no google"
        ]

        return any(p in texto for p in palavras)

    def run(self, texto, context, memory):
        subprocess.Popen("start chrome", shell=True)
        return "Abrindo Google"