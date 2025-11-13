"""
Módulo de interface de usuário - Menus e exibições
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich import box
from rich.text import Text
from config import carregar_configuracoes, obter_caminho_config
from historico import obter_estatisticas, obter_sessoes_recentes, obter_sessoes_por_data, formatar_duracao, traduzir_tipo

console = Console()


def limpar_tela():
    """Limpa a tela do terminal."""
    console.clear()


def exibir_menu_principal():
    """Exibe o menu principal da aplicação."""
    limpar_tela()
    
    title = Text("🍅 POMO CLI - Timer Pomodoro", style="bold red")
    
    menu_text = """[bold cyan][1][/] Iniciar sessão Pomodoro
[bold cyan][2][/] Iniciar timer personalizado
[bold cyan][3][/] Ver configurações
[bold cyan][4][/] Editar configurações
[bold cyan][5][/] Resetar configurações
[bold cyan][6][/] Ver estatísticas
[bold cyan][7][/] Ver histórico
[bold cyan][8][/] Sobre
[bold cyan][0][/] Sair"""
    
    panel = Panel(
        menu_text,
        title=title,
        border_style="red",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()


def exibir_configuracoes():
    """Exibe as configurações atuais do timer."""
    limpar_tela()
    config = carregar_configuracoes()
    
    table = Table(title="⚙️  Configurações", box=box.ROUNDED, border_style="cyan")
    table.add_column("Configuração", style="cyan")
    table.add_column("Valor", style="green", justify="right")
    
    table.add_row("Tempo de trabalho", f"{config['tempo_trabalho']} minutos")
    table.add_row("Descanso curto", f"{config['descanso_curto']} minutos")
    table.add_row("Descanso longo", f"{config['descanso_longo']} minutos")
    table.add_row("Ciclos", str(config['ciclos']))
    table.add_row("Som habilitado", "Sim" if config.get('som_habilitado', True) else "Não")
    table.add_row("Auto-iniciar descanso", "Sim" if config.get('auto_iniciar_descanso', False) else "Não")
    table.add_row("Notificações", "Sim" if config.get('notificacoes_habilitadas', True) else "Não")
    table.add_row("Arquivo", obter_caminho_config())
    
    console.print(table)
    console.print()
    Prompt.ask("[dim]Pressione ENTER para voltar[/dim]", default="")


def exibir_sobre():
    """Exibe informações sobre a aplicação."""
    limpar_tela()
    
    sobre_text = """[bold red]🍅 Pomo CLI - Timer Pomodoro[/]
[cyan]Versão: 1.0.0[/]

A Técnica Pomodoro é um método de gerenciamento
de tempo que usa um timer para dividir o trabalho
em intervalos de 25 minutos, separados por breves
intervalos de descanso.

[yellow]📝 Desenvolvido por:[/] rafastos
[yellow]📅 Data:[/] 12 de novembro de 2025"""
    
    panel = Panel(
        sobre_text,
        title="Sobre",
        border_style="blue",
        box=box.DOUBLE,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()
    Prompt.ask("[dim]Pressione ENTER para voltar[/dim]", default="")


def exibir_estatisticas():
    """Exibe estatísticas gerais do histórico."""
    limpar_tela()
    stats = obter_estatisticas()
    
    table = Table(title="📊 Estatísticas", box=box.ROUNDED, border_style="magenta")
    table.add_column("Categoria", style="cyan", justify="left")
    table.add_column("Métrica", style="yellow", justify="left")
    table.add_column("Valor", style="green", justify="right")
    
    # Estatísticas gerais
    table.add_row("GERAL", "Total de sessões", str(stats['total_sessoes']))
    table.add_row("", "✅ Completas", str(stats['sessoes_completas']))
    table.add_row("", "❌ Canceladas", str(stats['sessoes_canceladas']))
    table.add_row("", "🍅 Pomodoros completos", str(stats['pomodoros_completos']))
    
    # Tempo
    table.add_row("TEMPO", "Total geral", formatar_duracao(stats['tempo_total_minutos']))
    table.add_row("", "Tempo de trabalho", formatar_duracao(stats['tempo_trabalho_minutos']))
    
    # Hoje
    table.add_row("HOJE", "Sessões", str(stats['sessoes_hoje']))
    table.add_row("", "Tempo", formatar_duracao(stats['tempo_hoje_minutos']))
    
    # Média
    if stats['sessoes_completas'] > 0:
        media = stats['tempo_trabalho_minutos'] / stats['sessoes_completas']
        table.add_row("MÉDIA", "Tempo por sessão", formatar_duracao(int(media)))
    
    console.print(table)
    console.print()
    Prompt.ask("[dim]Pressione ENTER para voltar[/dim]", default="")


def exibir_menu_historico():
    """Exibe o menu de histórico com opções."""
    limpar_tela()
    
    menu_text = """[bold cyan][1][/] Ver sessões recentes
[bold cyan][2][/] Ver sessões de hoje
[bold cyan][3][/] Limpar histórico
[bold cyan][0][/] Voltar ao menu principal"""
    
    panel = Panel(
        menu_text,
        title="📜 Histórico",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()


def exibir_sessoes_recentes():
    """Exibe as sessões mais recentes."""
    limpar_tela()
    
    sessoes = obter_sessoes_recentes(20)
    
    if not sessoes:
        panel = Panel(
            "[yellow]📭 Nenhuma sessão registrada ainda.[/]",
            title="📜 Sessões Recentes",
            border_style="blue",
            box=box.ROUNDED
        )
        console.print(panel)
    else:
        table = Table(
            title=f"Sessões Recentes (últimas {len(sessoes)})",
            box=box.ROUNDED,
            border_style="blue"
        )
        
        table.add_column("#", style="dim", width=4, justify="right")
        table.add_column("Status", justify="center", width=6)
        table.add_column("Tipo", style="cyan")
        table.add_column("Duração", style="yellow", justify="right")
        table.add_column("Data", style="green")
        table.add_column("Hora", style="magenta", justify="right")
        
        for i, sessao in enumerate(reversed(sessoes), 1):
            status = "[green]✅[/]" if sessao.get('completa', True) else "[red]❌[/]"
            tipo = traduzir_tipo(sessao.get('tipo', 'desconhecido'))
            duracao = f"{sessao.get('duracao_minutos', 0)}min"
            data = sessao.get('data', 'N/A')
            hora = sessao.get('hora', 'N/A')[:5]
            
            table.add_row(str(i), status, tipo, duracao, data, hora)
        
        console.print(table)
    
    console.print()
    Prompt.ask("[dim]Pressione ENTER para voltar[/dim]", default="")


def exibir_sessoes_hoje():
    """Exibe as sessões do dia atual."""
    limpar_tela()
    
    sessoes = obter_sessoes_por_data()
    
    if not sessoes:
        panel = Panel(
            "[yellow]📭 Nenhuma sessão registrada hoje.[/]",
            title="Sessões de Hoje",
            border_style="blue",
            box=box.ROUNDED
        )
        console.print(panel)
    else:
        tempo_total = sum(s.get('duracao_minutos', 0) for s in sessoes if s.get('completa', True))
        
        table = Table(
            title=f"📅 Sessões de Hoje ({len(sessoes)} sessões | {formatar_duracao(tempo_total)})",
            box=box.ROUNDED,
            border_style="blue"
        )
        
        table.add_column("#", style="dim", width=4, justify="right")
        table.add_column("Status", justify="center", width=6)
        table.add_column("Tipo", style="cyan")
        table.add_column("Duração", style="yellow", justify="right")
        table.add_column("Hora", style="magenta", justify="right")
        
        for i, sessao in enumerate(sessoes, 1):
            status = "[green]✅[/]" if sessao.get('completa', True) else "[red]❌[/]"
            tipo = traduzir_tipo(sessao.get('tipo', 'desconhecido'))
            duracao = f"{sessao.get('duracao_minutos', 0)}min"
            hora = sessao.get('hora', 'N/A')[:5]
            
            table.add_row(str(i), status, tipo, duracao, hora)
        
        console.print(table)
    
    console.print()
    Prompt.ask("[dim]Pressione ENTER para voltar[/dim]", default="")
