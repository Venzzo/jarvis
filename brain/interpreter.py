from plugins.registry import PluginRegistry

class Interpreter:
    def __init__(self):
        self.registry = PluginRegistry()

    def detect(self, texto):
        for name, plugin in self.registry.get_all().items():
            if plugin.match(texto):
                return name
        return None
