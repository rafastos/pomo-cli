"""
Módulo de gerenciamento de histórico de sessões do Pomo CLI
"""

import json
import os
from datetime import datetime


# Arquivo de histórico
HISTORICO_FILE = 'historico.json'


def carregar_historico():
    """
    Carrega o histórico de sessões do arquivo JSON.
    Se o arquivo não existir, retorna uma lista vazia.
    
    Retorna:
    list: Lista de sessões registradas.
    """
    if not os.path.exists(HISTORICO_FILE):
        return []
    
    try:
        with open(HISTORICO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️  Erro ao ler arquivo de histórico. Iniciando novo histórico.")
        return []
    except Exception as e:
        print(f"⚠️  Erro ao carregar histórico: {e}")
        return []


def salvar_historico(historico):
    """
    Salva o histórico de sessões no arquivo JSON.
    
    Parâmetros:
    historico (list): Lista de sessões a serem salvas.
    
    Retorna:
    bool: True se salvou com sucesso, False caso contrário.
    """
    try:
        with open(HISTORICO_FILE, 'w', encoding='utf-8') as f:
            json.dump(historico, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar histórico: {e}")
        return False


def adicionar_sessao(tipo, duracao_minutos, completa=True):
    """
    Adiciona uma nova sessão ao histórico.
    
    Parâmetros:
    tipo (str): Tipo da sessão ('trabalho', 'descanso_curto', 'descanso_longo', 'personalizado', 'pomodoro_completo').
    duracao_minutos (int): Duração da sessão em minutos.
    completa (bool): Se a sessão foi completada ou cancelada.
    
    Retorna:
    bool: True se adicionou com sucesso, False caso contrário.
    """
    historico = carregar_historico()
    
    sessao = {
        'tipo': tipo,
        'duracao_minutos': duracao_minutos,
        'completa': completa,
        'data': datetime.now().strftime('%Y-%m-%d'),
        'hora': datetime.now().strftime('%H:%M:%S'),
        'timestamp': datetime.now().isoformat()
    }
    
    historico.append(sessao)
    return salvar_historico(historico)


def obter_estatisticas():
    """
    Calcula estatísticas gerais do histórico.
    
    Retorna:
    dict: Dicionário com estatísticas do histórico.
    """
    historico = carregar_historico()
    
    if not historico:
        return {
            'total_sessoes': 0,
            'sessoes_completas': 0,
            'sessoes_canceladas': 0,
            'tempo_total_minutos': 0,
            'tempo_trabalho_minutos': 0,
            'pomodoros_completos': 0,
            'sessoes_hoje': 0,
            'tempo_hoje_minutos': 0
        }
    
    hoje = datetime.now().strftime('%Y-%m-%d')
    
    total_sessoes = len(historico)
    sessoes_completas = sum(1 for s in historico if s.get('completa', True))
    sessoes_canceladas = total_sessoes - sessoes_completas
    tempo_total_minutos = sum(s.get('duracao_minutos', 0) for s in historico if s.get('completa', True))
    tempo_trabalho_minutos = sum(
        s.get('duracao_minutos', 0) 
        for s in historico 
        if s.get('completa', True) and s.get('tipo') in ['trabalho', 'personalizado']
    )
    pomodoros_completos = sum(1 for s in historico if s.get('tipo') == 'pomodoro_completo' and s.get('completa', True))
    
    sessoes_hoje = sum(1 for s in historico if s.get('data') == hoje)
    tempo_hoje_minutos = sum(
        s.get('duracao_minutos', 0) 
        for s in historico 
        if s.get('data') == hoje and s.get('completa', True)
    )
    
    return {
        'total_sessoes': total_sessoes,
        'sessoes_completas': sessoes_completas,
        'sessoes_canceladas': sessoes_canceladas,
        'tempo_total_minutos': tempo_total_minutos,
        'tempo_trabalho_minutos': tempo_trabalho_minutos,
        'pomodoros_completos': pomodoros_completos,
        'sessoes_hoje': sessoes_hoje,
        'tempo_hoje_minutos': tempo_hoje_minutos
    }


def obter_sessoes_recentes(limite=10):
    """
    Retorna as sessões mais recentes do histórico.
    
    Parâmetros:
    limite (int): Número máximo de sessões a retornar.
    
    Retorna:
    list: Lista com as sessões mais recentes.
    """
    historico = carregar_historico()
    return historico[-limite:] if historico else []


def obter_sessoes_por_data(data=None):
    """
    Retorna as sessões de uma data específica.
    
    Parâmetros:
    data (str): Data no formato 'YYYY-MM-DD'. Se None, usa data atual.
    
    Retorna:
    list: Lista de sessões da data especificada.
    """
    if data is None:
        data = datetime.now().strftime('%Y-%m-%d')
    
    historico = carregar_historico()
    return [s for s in historico if s.get('data') == data]


def limpar_historico():
    """
    Remove todo o histórico de sessões.
    
    Retorna:
    bool: True se limpou com sucesso, False caso contrário.
    """
    try:
        if os.path.exists(HISTORICO_FILE):
            os.remove(HISTORICO_FILE)
        return True
    except Exception as e:
        print(f"❌ Erro ao limpar histórico: {e}")
        return False


def formatar_duracao(minutos):
    """
    Formata a duração em minutos para uma string legível.
    
    Parâmetros:
    minutos (int): Duração em minutos.
    
    Retorna:
    str: Duração formatada (ex: "2h 30min" ou "45min").
    """
    if minutos < 60:
        return f"{minutos}min"
    
    horas = minutos // 60
    mins = minutos % 60
    
    if mins == 0:
        return f"{horas}h"
    
    return f"{horas}h {mins}min"


def traduzir_tipo(tipo):
    """
    Traduz o tipo de sessão para uma string legível.
    
    Parâmetros:
    tipo (str): Tipo da sessão.
    
    Retorna:
    str: Tipo traduzido com emoji.
    """
    tipos = {
        'trabalho': '🍅 Trabalho',
        'descanso_curto': '☕ Descanso Curto',
        'descanso_longo': '🌴 Descanso Longo',
        'personalizado': 'Timer Personalizado',
        'pomodoro_completo': '🎉 Pomodoro Completo'
    }
    return tipos.get(tipo, tipo)
