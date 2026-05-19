from datetime import datetime

LOG_FILE = "logs/conversa.txt"

def salvar_log(usuario, resposta):

    horario = datetime.now().strftime("%H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:

        f.write(f"[{horario}] VOCÊ: {usuario}\n")
        f.write(f"[{horario}] LARY: {resposta}\n")
        f.write("-" * 50 + "\n")