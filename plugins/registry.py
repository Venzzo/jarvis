from plugins.google import GooglePlugin
from plugins.time import TimePlugin
from plugins.chat import ChatPlugin

class PluginRegistry:
    def __init__(self):
        self.plugins = {
            "google": GooglePlugin(),
            "time": TimePlugin(),
            "chat": ChatPlugin()
        }

    def get_all(self):
        return self.plugins

    def get(self, name):
        return self.plugins.get(name)
