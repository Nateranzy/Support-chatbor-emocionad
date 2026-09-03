# Chatbot de Apoio Emocional

Um assistente de conversa em Python que usa IA para fazer perguntas reflexivas 
abertas, ajudando pessoas que enfrentam solidão e tristeza a organizar seus 
próprios pensamentos.

⚠️ **Este projeto NÃO substitui terapia ou ajuda profissional.** Ele conta com 
uma camada de segurança que detecta sinais de risco (ideação suicida, 
autolesão, crise emocional) e direciona a pessoa para recursos reais de ajuda, 
como o CVV (188).

## Funcionalidades

- 💬 Conversa natural guiada por perguntas reflexivas (baseadas em técnicas de 
  entrevista motivacional)
- 🛡️ Detecção de risco em duas camadas: palavras-chave + classificação por IA
- 📞 Resposta automática de crise com recursos reais (CVV, SAMU)
- 💾 Histórico de conversas salvo automaticamente em JSON
- 🖥️ Roda 100% local, sem custo de API, usando Ollama + Llama 3.2

## Tecnologias

- Python 3.12
- [Ollama](https://ollama.com) rodando o modelo `llama3.2` localmente
- Biblioteca `ollama` (Python)

## Como rodar

### Pré-requisitos
- Python 3.12+
- [Ollama](https://ollama.com/download) instalado

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/Nateranzy/support-chatbot.git
cd support-chatbot
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac
```

3. Instale as dependências:
```bash
pip install ollama
```

4. Baixe o modelo de IA:
```bash
ollama pull llama3.2
```

5. Rode o chatbot:
```bash
python main.py
```

## Estrutura do projeto












































ANTHROPIC_API_KEY=sk-ant-sua-chave-real-aqui
