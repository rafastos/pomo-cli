"""
Módulo de edição de configurações - Interface para ajustar as configurações
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich import box
from config import carregar_configuracoes, salvar_configuracoes, resetar_configuracoes, validar_valor

console = Console()


def limpar_tela():
    """Limpa a tela do terminal."""
    console.clear()


def editar_configuracoes():
    """Menu interativo para editar as configurações."""
    while True:
        limpar_tela()
        config = carregar_configuracoes()
        
        menu_text = f"""[bold yellow]Configurações Atuais:[/bold yellow]

[bold cyan][1][/] Tempo de trabalho: [green]{config['tempo_trabalho']} minutos[/]
[bold cyan][2][/] Descanso curto: [green]{config['descanso_curto']} minutos[/]
[bold cyan][3][/] Descanso longo: [green]{config['descanso_longo']} minutos[/]
[bold cyan][4][/] Número de ciclos: [green]{config['ciclos']}[/]
[bold cyan][5][/] Som habilitado: [green]{"Sim" if config.get('som_habilitado', True) else "Não"}[/]
[bold cyan][6][/] Auto-iniciar descanso: [green]{"Sim" if config.get('auto_iniciar_descanso', False) else "Não"}[/]
[bold cyan][7][/] Notificações: [green]{"Sim" if config.get('notificacoes_habilitadas', True) else "Não"}[/]
[bold cyan][0][/] Voltar ao menu principal"""
        
        panel = Panel(
            menu_text,
            title="⚙️  Editar Configurações",
            border_style="yellow",
            box=box.ROUNDED,
            padding=(1, 2)
        )
        
        console.print(panel)
        console.print()
        
        opcao = Prompt.ask("Escolha uma opção", default="0")
        
        if opcao == "0":
            break
        elif opcao == "1":
            _editar_tempo_trabalho(config)
        elif opcao == "2":
            _editar_descanso_curto(config)
        elif opcao == "3":
            _editar_descanso_longo(config)
        elif opcao == "4":
            _editar_ciclos(config)
        elif opcao == "5":
            _editar_som(config)
        elif opcao == "6":
            _editar_auto_iniciar(config)
        elif opcao == "7":
            _editar_notificacoes(config)
        else:
            console.print("[red]❌ Opção inválida![/red]")
            Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def _editar_tempo_trabalho(config):
    """Edita o tempo de trabalho."""
    console.print("\n[cyan]⏱️  Tempo de trabalho atual:[/cyan]", f"[green]{config['tempo_trabalho']} minutos[/green]")
    novo_valor = Prompt.ask("Digite o novo tempo de trabalho (em minutos)", default=str(config['tempo_trabalho']))
    
    if validar_valor(novo_valor, 1, 120):
        config['tempo_trabalho'] = int(novo_valor)
        salvar_configuracoes(config)
        console.print("[green]✅ Configuração atualizada com sucesso![/green]")
    else:
        console.print("[red]❌ Valor inválido! Use um número entre 1 e 120.[/red]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def _editar_descanso_curto(config):
    """Edita o tempo de descanso curto."""
    console.print("\n[cyan]⏱️  Descanso curto atual:[/cyan]", f"[green]{config['descanso_curto']} minutos[/green]")
    novo_valor = Prompt.ask("Digite o novo tempo de descanso curto (em minutos)", default=str(config['descanso_curto']))
    
    if validar_valor(novo_valor, 1, 60):
        config['descanso_curto'] = int(novo_valor)
        salvar_configuracoes(config)
        console.print("[green]✅ Configuração atualizada com sucesso![/green]")
    else:
        console.print("[red]❌ Valor inválido! Use um número entre 1 e 60.[/red]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def _editar_descanso_longo(config):
    """Edita o tempo de descanso longo."""
    console.print("\n[cyan]⏱️  Descanso longo atual:[/cyan]", f"[green]{config['descanso_longo']} minutos[/green]")
    novo_valor = Prompt.ask("Digite o novo tempo de descanso longo (em minutos)", default=str(config['descanso_longo']))
    
    if validar_valor(novo_valor, 1, 60):
        config['descanso_longo'] = int(novo_valor)
        salvar_configuracoes(config)
        console.print("[green]✅ Configuração atualizada com sucesso![/green]")
    else:
        console.print("[red]❌ Valor inválido! Use um número entre 1 e 60.[/red]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def _editar_ciclos(config):
    """Edita o número de ciclos."""
    console.print("\n[cyan]🔄 Número de ciclos atual:[/cyan]", f"[green]{config['ciclos']}[/green]")
    novo_valor = Prompt.ask("Digite o novo número de ciclos", default=str(config['ciclos']))
    
    if validar_valor(novo_valor, 1, 10):
        config['ciclos'] = int(novo_valor)
        salvar_configuracoes(config)
        console.print("[green]✅ Configuração atualizada com sucesso![/green]")
    else:
        console.print("[red]❌ Valor inválido! Use um número entre 1 e 10.[/red]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def _editar_som(config):
    """Edita a configuração de som."""
    atual = config.get('som_habilitado', True)
    console.print("\n[cyan]🔊 Som habilitado:[/cyan]", f"[green]{'Sim' if atual else 'Não'}[/green]")
    
    novo_valor = Confirm.ask("Habilitar som?", default=atual)
    config['som_habilitado'] = novo_valor
    salvar_configuracoes(config)
    console.print("[green]✅ Configuração atualizada com sucesso![/green]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def _editar_auto_iniciar(config):
    """Edita a configuração de auto-iniciar descanso."""
    atual = config.get('auto_iniciar_descanso', False)
    console.print("\n[cyan]⚡ Auto-iniciar descanso:[/cyan]", f"[green]{'Sim' if atual else 'Não'}[/green]")
    
    novo_valor = Confirm.ask("Auto-iniciar descanso automaticamente?", default=atual)
    config['auto_iniciar_descanso'] = novo_valor
    salvar_configuracoes(config)
    console.print("[green]✅ Configuração atualizada com sucesso![/green]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def _editar_notificacoes(config):
    """Edita a configuração de notificações."""
    atual = config.get('notificacoes_habilitadas', True)
    console.print("\n[cyan]🔔 Notificações habilitadas:[/cyan]", f"[green]{'Sim' if atual else 'Não'}[/green]")
    
    novo_valor = Confirm.ask("Habilitar notificações?", default=atual)
    config['notificacoes_habilitadas'] = novo_valor
    salvar_configuracoes(config)
    console.print("[green]✅ Configuração atualizada com sucesso![/green]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")
