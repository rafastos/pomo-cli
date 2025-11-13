"""
Módulo de timer - Lógica de contadores e execução de sessões
"""

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.panel import Panel
from rich.prompt import Confirm
from rich import box
import time
from funcoes import contar_tempo, tocar_som
from config import carregar_configuracoes
from historico import adicionar_sessao
from notificacoes import (
    notificar_trabalho_iniciado,
    notificar_trabalho_concluido,
    notificar_descanso_concluido,
    notificar_pomodoro_completo,
    notificar_timer_personalizado_concluido
)

console = Console()


def executar_timer(minutos, descricao, cor="cyan", tipo_sessao=None):
    """
    Executa um timer com barra de progresso.
    
    Args:
        minutos: Duração do timer em minutos
        descricao: Descrição da sessão
        cor: Cor da barra de progresso
        tipo_sessao: Tipo da sessão ('trabalho', 'descanso_curto', 'descanso_longo', 'personalizado')
    
    Returns:
        bool: True se o timer foi completado, False se foi cancelado
    """
    config = carregar_configuracoes()
    completo = False
    
    # Notificação de início
    if config.get('notificacoes_habilitadas', True) and tipo_sessao == 'trabalho':
        notificar_trabalho_iniciado(minutos)
    
    total_segundos = minutos * 60
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold]{task.description}"),
            BarColumn(complete_style=cor, finished_style="green"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            TextColumn("⏱️"),
            console=console,
            transient=False
        ) as progress:
            
            task = progress.add_task(descricao, total=total_segundos)
            
            for minutos_restantes, segundos_restantes in contar_tempo(minutos):
                progress.update(
                    task,
                    completed=total_segundos - (minutos_restantes * 60 + segundos_restantes),
                    description=f"{descricao} - {minutos_restantes:02d}:{segundos_restantes:02d}"
                )
                time.sleep(1)
            
            completo = True
            
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Timer interrompido![/yellow]")
        completo = False
    
    # Tocar som de conclusão
    if completo and config.get('som_habilitado', True):
        tocar_som()
    
    # Notificação de conclusão
    if completo and config.get('notificacoes_habilitadas', True):
        if tipo_sessao == 'trabalho':
            notificar_trabalho_concluido()
        elif tipo_sessao in ['descanso_curto', 'descanso_longo']:
            notificar_descanso_concluido()
        elif tipo_sessao == 'personalizado':
            notificar_timer_personalizado_concluido(minutos)
    
    return completo


def iniciar_sessao_pomodoro():
    """Inicia uma sessão completa de Pomodoro com múltiplos ciclos."""
    config = carregar_configuracoes()
    
    tempo_trabalho = config['tempo_trabalho']
    descanso_curto = config['descanso_curto']
    descanso_longo = config['descanso_longo']
    ciclos = config['ciclos']
    auto_iniciar = config.get('auto_iniciar_descanso', False)
    
    console.print()
    panel = Panel(
        f"[bold]🍅 Sessão Pomodoro[/bold]\n\n"
        f"[cyan]• {ciclos} ciclos de trabalho[/]\n"
        f"[cyan]• {tempo_trabalho} minutos de trabalho[/]\n"
        f"[cyan]• {descanso_curto} minutos de descanso curto[/]\n"
        f"[cyan]• {descanso_longo} minutos de descanso longo[/]\n"
        f"[dim]• Pressione Ctrl+C para interromper[/]",
        border_style="red",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    console.print(panel)
    console.print()
    
    for ciclo in range(1, ciclos + 1):
        console.print(f"\n[bold red]═══ Ciclo {ciclo}/{ciclos} ═══[/bold red]\n")
        
        # Fase de trabalho
        completo = executar_timer(
            tempo_trabalho,
            f"🎯 Trabalho (Ciclo {ciclo}/{ciclos})",
            "red",
            tipo_sessao='trabalho'
        )
        
        if not completo:
            adicionar_sessao('trabalho', tempo_trabalho, completa=False)
            return
        
        adicionar_sessao('trabalho', tempo_trabalho, completa=True)
        
        # Descanso
        if ciclo < ciclos:
            # Descanso curto
            console.print(f"\n[cyan]✅ Trabalho concluído! Hora do descanso curto.[/cyan]\n")
            
            if not auto_iniciar:
                if not Confirm.ask("Iniciar descanso curto?", default=True):
                    continue
            
            completo_descanso = executar_timer(
                descanso_curto,
                f"☕ Descanso Curto (Ciclo {ciclo}/{ciclos})",
                "cyan",
                tipo_sessao='descanso_curto'
            )
            
            adicionar_sessao('descanso_curto', descanso_curto, completa=completo_descanso)
            
            if completo_descanso:
                console.print(f"\n[green]✅ Descanso concluído! Prepare-se para o próximo ciclo.[/green]\n")
                time.sleep(2)
        else:
            # Descanso longo
            console.print(f"\n[green]🎉 Todos os ciclos concluídos! Hora do descanso longo.[/green]\n")
            
            if not auto_iniciar:
                if not Confirm.ask("Iniciar descanso longo?", default=True):
                    break
            
            completo_descanso = executar_timer(
                descanso_longo,
                "🌟 Descanso Longo",
                "green",
                tipo_sessao='descanso_longo'
            )
            
            adicionar_sessao('descanso_longo', descanso_longo, completa=completo_descanso)
    
    # Notificação de Pomodoro completo
    if config.get('notificacoes_habilitadas', True):
        notificar_pomodoro_completo(ciclos)
    
    console.print("\n[bold green]🎊 Sessão Pomodoro finalizada com sucesso![/bold green]\n")
    time.sleep(3)
