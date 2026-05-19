from tasks.task_manager import TaskManager
from plugins.registry import PluginRegistry
from brain.ollama_brain import perguntar_ollama

class Executor:

    def __init__(self):
        self.registry = PluginRegistry()
        self.tasks = TaskManager()

    def execute(self, intent, texto, modo, context, memory):

        # plugins/comandos primeiro
        if intent:
            plugin = self.registry.get(intent)
            return plugin.run(texto, context, memory)

        # tasks compostas
        task_response = self.tasks.handle(texto, context, memory)

        if task_response:
            return task_response

        # IA LOCAL
        return perguntar_ollama(texto, modo)