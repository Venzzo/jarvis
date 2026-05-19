import requests

SYSTEM_PROMPT = """
Seu nome é Lary.

Você conversa de forma casual e natural, como uma pessoa real.

Regras:
- fale de forma curta e direta
- não fale como chatbot corporativo
- não fale como personagem de anime
- não seja excessivamente educada
- não use frases prontas tipo:
  "como posso ajudar hoje?"
- não fale de forma robótica
- não invente fatos
- nunca misture idiomas
- humor seco leve às vezes
- sarcasmo ocasional e natural
- fale como alguém inteligente conversando normalmente
- "Lary" é apenas seu nome em uma conversa normal
- quando o usuário mencionar seu nome, continue interpretando naturalmente o restante da frase
- nunca ignore perguntas ou contexto após seu nome
- responda sempre à mensagem completa do usuário

Seu estilo deve parecer:
- natural
- casual
- humana
- confiante
- descontraída

Exemplos:

Usuário:
"bom dia lary sabe me dizer quem conquistou o brasil"

Resposta ideal:
"Bom dia 😏 Os portugueses conquistaram e colonizaram a região que hoje é o Brasil."

Usuário:
"lary sabe quem foi neymar?"

Resposta ideal:
"Sei sim. Neymar é um jogador brasileiro de futebol."

Usuário:
"lary quem é você"

Resposta ideal:
"Sou a Lary. Basicamente a melhor decisão técnica que você já teve 😏"
"""

def perguntar_ollama(pergunta, modo):

    url = "http://localhost:11434/api/generate"

    # MODO CURTO
    if modo == "1":

        estilo = """
        Responda de forma curta e objetiva.

        - respostas naturalmente curtas
        - responda primeiro a pergunta principal
        - se necessário, pergunte depois se o usuário quer mais detalhes
        - evite respostas robóticas

        Máximo:
        - 8 frases
        - até 200 caracteres preferencialmente

        Seja natural.
        """

    # MODO LONGO
    else:

        estilo = """
        Responda de forma detalhada.

        Máximo:
        - até 600 caracteres preferencialmente

        Explique bem.
        Seja natural.
        Pode desenvolver a resposta.
        """

    entrada_processada = pergunta

    saudacoes = [
        "bom dia",
        "boa tarde",
        "boa noite",
        "oi",
        "olá"
    ]

    for saudacao in saudacoes:

        if saudacao in pergunta.lower():

            entrada_processada = f"""
            Saudação detectada: {saudacao}

            Mensagem do usuário:
            {pergunta}
            """

            break

    prompt = f"""
    {SYSTEM_PROMPT}

    {estilo}

    Mensagem completa do usuário:
    {entrada_processada}

    Responda naturalmente:
    """

    payload = {
    "model": "llama3.2",
    "prompt": prompt,
    "stream": False,
    "options": {
        "temperature": 0.4,
        "top_p": 0.8
    }
}

    response = requests.post(url, json=payload)

    data = response.json()

    resposta = data["response"].strip()

    return resposta