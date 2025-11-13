"""
Módulo de gerenciamento de configurações do Pomo CLI
"""

import json
import os


# Arquivo de configuração padrão
CONFIG_FILE = 'config.json'

# Configurações padrão
CONFIGURACOES_PADRAO = {
    'tempo_trabalho': 25,
    'descanso_curto': 5,
    'descanso_longo': 15,
    'ciclos': 4,
    'som_habilitado': True,
    'auto_iniciar_descanso': False,
    'notificacoes_habilitadas': True
}


def criar_config_padrao():
    """Cria o arquivo de configuração com valores padrão."""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(CONFIGURACOES_PADRAO, f, indent=4, ensure_ascii=False)
    print(f"✅ Arquivo de configuração criado: {CONFIG_FILE}")


def carregar_configuracoes():
    """
    Carrega as configurações do arquivo JSON.
    Se o arquivo não existir, cria um com configurações padrão.
    
    Retorna:
    dict: Dicionário contendo as configurações.
    """
    if not os.path.exists(CONFIG_FILE):
        criar_config_padrao()
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Garante que todas as chaves padrão existam
        for chave, valor in CONFIGURACOES_PADRAO.items():
            if chave not in config:
                config[chave] = valor
        
        return config
    
    except json.JSONDecodeError:
        print("⚠️  Erro ao ler arquivo de configuração. Usando configurações padrão.")
        return CONFIGURACOES_PADRAO.copy()
    except Exception as e:
        print(f"⚠️  Erro ao carregar configurações: {e}")
        return CONFIGURACOES_PADRAO.copy()


def salvar_configuracoes(config):
    """
    Salva as configurações no arquivo JSON.
    
    Parâmetros:
    config (dict): Dicionário com as configurações a serem salvas.
    
    Retorna:
    bool: True se salvou com sucesso, False caso contrário.
    """
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar configurações: {e}")
        return False


def validar_valor(valor, minimo=1, maximo=999):
    """
    Valida se um valor está dentro do intervalo permitido.
    
    Parâmetros:
    valor (int): Valor a ser validado.
    minimo (int): Valor mínimo permitido.
    maximo (int): Valor máximo permitido.
    
    Retorna:
    bool: True se válido, False caso contrário.
    """
    return minimo <= valor <= maximo


def resetar_configuracoes():
    """
    Reseta as configurações para os valores padrão.
    
    Retorna:
    bool: True se resetou com sucesso, False caso contrário.
    """
    return salvar_configuracoes(CONFIGURACOES_PADRAO)


def obter_caminho_config():
    """
    Retorna o caminho completo do arquivo de configuração.
    
    Retorna:
    str: Caminho absoluto do arquivo de configuração.
    """
    return os.path.abspath(CONFIG_FILE)
