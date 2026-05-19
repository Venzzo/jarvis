import json, os

FILE = "memoria.json"

class MemoryManager:
    def __init__(self):
        self.data = self._load()

    def _load(self):
        if not os.path.exists(FILE):
            return {"important": {}, "trash": []}
        with open(FILE, "r") as f:
            return json.load(f)

    def _save(self):
        with open(FILE, "w") as f:
            json.dump(self.data, f, indent=2)

    def auto_save(self, texto):
        if "meu nome é" in texto:
            self.data["important"]["nome"] = texto.replace("meu nome é","").strip()
        else:
            self.data["trash"].append(texto)
        self._save()

    def cleanup(self):
        self.data["trash"] = self.data["trash"][-5:]
        self._save()
