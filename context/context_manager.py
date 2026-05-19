class ContextManager:
    def __init__(self):
        self.data = {"last_intent": None}

    def update(self, intent, texto):
        self.data["last_intent"] = intent
