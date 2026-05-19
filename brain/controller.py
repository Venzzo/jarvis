from logs.logger import salvar_log
from brain.interpreter import Interpreter
from brain.executor import Executor
from context.context_manager import ContextManager
from memory.memory_manager import MemoryManager
from brain.personality_engine import PersonalityEngine

class Controller:
    def __init__(self):
        self.interpreter = Interpreter()
        self.executor = Executor()
        self.context = ContextManager()
        self.memory = MemoryManager()
        self.personality = PersonalityEngine()

    def handle(self, texto, modo):

        if "não entendi" in texto:
            return self.personality.confusion()

        self.memory.auto_save(texto)
        self.memory.cleanup()

        intent = self.interpreter.detect(texto)
        self.context.update(intent, texto)
        
        perguntas = [
        "quem",
        "quanto",
        "como",
        "porque",
        "por que",
        "qual",
        "sabe me dizer"
        ]

        if any(p in texto.lower() for p in perguntas):
         intent = None
        print("INTENT:", intent)

        response = self.executor.execute(intent, texto, modo, self.context, self.memory)

        response = self._limit(response, modo)
        salvar_log(texto, response)

        return self.personality.normal(response)

    def _limit(self, texto, modo):
        if not texto:
            return None
        return texto[:200] if modo == "1" else texto[:600]
