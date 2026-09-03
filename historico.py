"""
Módulo de histórico: salva e carrega conversas em arquivos JSON,
uma por sessão, na pasta 'conversas/'.
"""

import json
import os
from datetime import datetime

PASTA_HISTORICO = "conversas"


def garantir_pasta():
    """Cria a pasta de conversas se ainda não existir."""
    if not os.path.exists(PASTA_HISTORICO):
        os.makedirs(PASTA_HISTORICO)


def novo_arquivo_sessao() -> str:
    """Gera o caminho de um novo arquivo de conversa, nomeado com data/hora."""
    garantir_pasta()
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(PASTA_HISTORICO, f"conversa_{agora}.json")


def salvar_historico(caminho: str, historico: list):
    """Salva o histórico completo no arquivo, sobrescrevendo a cada mensagem."""
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


def listar_conversas() -> list:
    """Retorna a lista de arquivos de conversas salvas, mais recente primeiro."""
    garantir_pasta()
    arquivos = [f for f in os.listdir(PASTA_HISTORICO) if f.endswith(".json")]
    return sorted(arquivos, reverse=True)


def carregar_conversa(nome_arquivo: str) -> list:
    """Carrega uma conversa salva a partir do nome do arquivo."""
    caminho = os.path.join(PASTA_HISTORICO, nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)