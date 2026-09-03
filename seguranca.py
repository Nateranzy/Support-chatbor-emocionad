"""
Módulo de segurança: detecta sinais de risco (crise emocional, ideação 
suicida, autolesão) antes de qualquer resposta normal do chatbot.
"""

import ollama

PALAVRAS_RISCO = [
    "quero morrer", "não aguento mais viver", "penso em suicídio",
    "quero me matar", "não quero mais existir", "queria sumir",
    "acabar com tudo", "acabar com a minha vida",
    "me machucar", "me cortar", "me ferir",
    "não vejo saída", "não tenho mais esperança", "ninguém sentiria minha falta",
    "seria melhor se eu não existisse", "sou um peso para todos",
]

RESPOSTA_CRISE = """
Percebo que você pode estar passando por um momento muito difícil, e eu
quero que você saiba que não precisa enfrentar isso sozinho(a).

Por favor, entre em contato agora com:
📞 CVV (Centro de Valorização da Vida) — 188
   Ligação gratuita, 24 horas por dia, todos os dias
   Também disponível por chat em: https://www.cvv.org.br

Se você estiver em perigo imediato, ligue para o SAMU (192) ou vá até
o pronto-socorro mais próximo.

Eu sou um assistente e não posso substituir ajuda profissional, mas
estou aqui se quiser conversar enquanto isso.
"""


def detectar_risco_palavras(mensagem: str) -> bool:
    mensagem_lower = mensagem.lower()
    return any(palavra in mensagem_lower for palavra in PALAVRAS_RISCO)


def detectar_risco_ia(mensagem: str) -> bool:
    resposta = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "Responda apenas 'SIM' ou 'NAO'. A mensagem a seguir "
                    "indica risco de suicídio, autolesão ou crise emocional grave?"
                )
            },
            {"role": "user", "content": mensagem}
        ]
    )
    return "SIM" in resposta["message"]["content"].upper()


def avaliar_risco(mensagem: str) -> bool:
    if detectar_risco_palavras(mensagem):
        return True
    return detectar_risco_ia(mensagem)