"""
Módulo de gerenciamento de notificações desktop do Pomo CLI
"""

import platform
import subprocess
import os

# Detecta se notificações estão disponíveis
NOTIFICACOES_DISPONIVEIS = True


def enviar_notificacao_macos(titulo, mensagem):
    """
    Envia notificação usando osascript no macOS.
    
    Parâmetros:
    titulo (str): Título da notificação.
    mensagem (str): Mensagem da notificação.
    
    Retorna:
    bool: True se enviou com sucesso, False caso contrário.
    """
    try:
        # Remove emojis que podem causar problemas no AppleScript
        titulo_limpo = titulo.encode('ascii', 'ignore').decode('ascii')
        mensagem_limpa = mensagem.encode('ascii', 'ignore').decode('ascii')
        
        # Usa Glass como som padrão - mais audível que "default"
        script = f'''
        display notification "{mensagem_limpa}" with title "{titulo_limpo}" sound name "Glass"
        '''
        resultado = subprocess.run(
            ['osascript', '-e', script], 
            check=True, 
            capture_output=True,
            text=True
        )
        
        # Também toca um beep audível
        os.system('afplay /System/Library/Sounds/Glass.aiff')
        
        return True
    except Exception as e:
        print(f"⚠️  Erro ao enviar notificação: {e}")
        return False


def enviar_notificacao_linux(titulo, mensagem):
    """
    Envia notificação usando notify-send no Linux.
    
    Parâmetros:
    titulo (str): Título da notificação.
    mensagem (str): Mensagem da notificação.
    
    Retorna:
    bool: True se enviou com sucesso, False caso contrário.
    """
    try:
        subprocess.run(['notify-send', titulo, mensagem], check=True, capture_output=True)
        return True
    except Exception as e:
        print(f"⚠️  Erro ao enviar notificação: {e}")
        return False


def enviar_notificacao_windows(titulo, mensagem):
    """
    Envia notificação usando PowerShell no Windows.
    
    Parâmetros:
    titulo (str): Título da notificação.
    mensagem (str): Mensagem da notificação.
    
    Retorna:
    bool: True se enviou com sucesso, False caso contrário.
    """
    try:
        # Usa plyer no Windows
        from plyer import notification
        notification.notify(
            title=titulo,
            message=mensagem,
            app_name="Pomo CLI",
            timeout=10
        )
        return True
    except Exception as e:
        print(f"⚠️  Erro ao enviar notificação: {e}")
        return False


def enviar_notificacao(titulo, mensagem, timeout=10, icone_app=""):
    """
    Envia uma notificação desktop de forma multiplataforma.
    
    Parâmetros:
    titulo (str): Título da notificação.
    mensagem (str): Mensagem da notificação.
    timeout (int): Tempo em segundos que a notificação ficará visível (não usado em macOS).
    icone_app (str): Caminho para o ícone da aplicação (opcional).
    
    Retorna:
    bool: True se enviou com sucesso, False caso contrário.
    """
    if not NOTIFICACOES_DISPONIVEIS:
        return False
    
    sistema = platform.system()
    
    if sistema == "Darwin":  # macOS
        return enviar_notificacao_macos(titulo, mensagem)
    elif sistema == "Linux":
        return enviar_notificacao_linux(titulo, mensagem)
    elif sistema == "Windows":
        return enviar_notificacao_windows(titulo, mensagem)
    else:
        print(f"⚠️  Sistema operacional não suportado: {sistema}")
        return False

def notificar_trabalho_iniciado(duracao_minutos):
    """
    Notifica o início de uma sessão de trabalho.
    
    Parâmetros:
    duracao_minutos (int): Duração da sessão em minutos.
    """
    enviar_notificacao(
        titulo="🍅 Pomodoro - Trabalho Iniciado",
        mensagem=f"Foco! Trabalhe por {duracao_minutos} minutos.",
        timeout=5
    )

def notificar_trabalho_concluido():
    """Notifica a conclusão de uma sessão de trabalho."""
    enviar_notificacao(
        titulo="🎉 Pomodoro - Trabalho Concluído!",
        mensagem="Parabéns! Você completou uma sessão de trabalho.",
        timeout=10
    )

def notificar_descanso_concluido():
    """Notifica a conclusão de um descanso."""
    enviar_notificacao(
        titulo="⏰ Pomodoro - Descanso Concluído",
        mensagem="Hora de voltar ao trabalho!",
        timeout=10
    )

def notificar_pomodoro_completo(ciclos):
    """
    Notifica a conclusão de uma sessão completa de Pomodoro.
    
    Parâmetros:
    ciclos (int): Número de ciclos completados.
    """
    enviar_notificacao(
        titulo="🎉 Pomodoro - Sessão Completa!",
        mensagem=f"Parabéns! Você completou {ciclos} ciclos de Pomodoro!",
        timeout=15
    )

def notificar_timer_personalizado_concluido(minutos):
    """
    Notifica a conclusão de um timer personalizado.
    
    Parâmetros:
    minutos (int): Duração do timer em minutos.
    """
    enviar_notificacao(
        titulo="⏱️ Timer Concluído",
        mensagem=f"Seu timer de {minutos} minutos terminou!",
        timeout=10
    )

def testar_notificacoes():
    """
    Testa se as notificações estão funcionando.
    
    Retorna:
    bool: True se funcionou, False caso contrário.
    """
    if not NOTIFICACOES_DISPONIVEIS:
        print("❌ Notificações não disponíveis.")
        return False
    
    resultado = enviar_notificacao(
        titulo="🍅 Pomo CLI - Teste",
        mensagem="Notificações funcionando corretamente!",
        timeout=5
    )
    
    if resultado:
        print("✅ Notificação de teste enviada com sucesso!")
    else:
        print("❌ Falha ao enviar notificação de teste.")
    
    return resultado

def notificacoes_habilitadas():
    """
    Verifica se as notificações estão disponíveis.
    
    Retorna:
    bool: True se disponível, False caso contrário.
    """
    return NOTIFICACOES_DISPONIVEIS
