#!/usr/bin/env python3
"""
Pomo CLI - Aplicação de timer Pomodoro para linha de comando
Arquivo principal que coordena todos os módulos
"""

import sys
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich import box
from config import resetar_configuracoes
from historico import limpar_historico
from notificacoes import testar_notificacoes, notificacoes_habilitadas
from interface import (
    limpar_tela,
    exibir_menu_principal,
    exibir_configuracoes,
    exibir_sobre,
    exibir_estatisticas,
    exibir_menu_historico,
    exibir_sessoes_recentes,
    exibir_sessoes_hoje
)
from timer import iniciar_sessao_pomodoro, executar_timer
from editor_config import editar_configuracoes

console = Console()


def iniciar_timer_personalizado():
    """Inicia um timer com duração personalizada."""
    limpar_tela()
    
    panel = Panel(
        "Digite quantos minutos deseja trabalhar",
        title="⏱️ Timer Personalizado",
        border_style="yellow",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()
    
    try:
        minutos = int(Prompt.ask("Quantos minutos?"))
        if minutos <= 0:
            console.print("[red]❌ Por favor, insira um valor positivo.[/]")
            Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")
            return
        
        executar_timer(minutos, "⏱️ Timer Personalizado", "yellow", tipo_sessao='personalizado')
        
    except ValueError:
        console.print("[red]❌ Por favor, insira um número válido.[/]")
        Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def resetar_configuracoes_menu():
    """Reseta as configurações para os valores padrão."""
    limpar_tela()
    
    aviso_text = """[yellow]⚠️  ATENÇÃO[/]

Isso irá resetar todas as configurações
para os valores padrão."""
    
    panel = Panel(
        aviso_text,
        title="🔄 Resetar Configurações",
        border_style="yellow",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()
    
    if Confirm.ask("Tem certeza?", default=False):
        if resetar_configuracoes():
            console.print("\n[green]✅ Configurações resetadas com sucesso![/]")
        else:
            console.print("\n[red]❌ Erro ao resetar configurações.[/]")
    else:
        console.print("\n[yellow]❌ Operação cancelada.[/]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def exibir_historico():
    """Exibe o menu de histórico com opções."""
    while True:
        exibir_menu_historico()
        
        opcao = Prompt.ask("Escolha uma opção", default="0")
        
        if opcao == '0':
            break
        elif opcao == '1':
            exibir_sessoes_recentes()
        elif opcao == '2':
            exibir_sessoes_hoje()
        elif opcao == '3':
            limpar_historico_menu()
        else:
            console.print("\n[red]❌ Opção inválida![/]")
            Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def limpar_historico_menu():
    """Menu para limpar o histórico."""
    limpar_tela()
    
    aviso_text = """[bold yellow]⚠️  ATENÇÃO: Esta ação não pode ser desfeita![/]

Você perderá:
• Todas as estatísticas
• Todas as sessões registradas
• Todo o histórico de trabalho"""
    
    panel = Panel(
        aviso_text,
        title="🗑️  Limpar Histórico",
        border_style="red",
        box=box.DOUBLE,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()
    
    if Confirm.ask("Tem certeza que deseja limpar o histórico?", default=False):
        if limpar_historico():
            console.print("\n[green]✅ Histórico limpo com sucesso![/]")
        else:
            console.print("\n[red]❌ Erro ao limpar histórico.[/]")
    else:
        console.print("\n[yellow]❌ Operação cancelada.[/]")
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def testar_notificacoes_menu():
    """Menu para testar notificações."""
    limpar_tela()
    
    if not notificacoes_habilitadas():
        console.print("\n[red]❌ Notificações não disponíveis.[/]")
    else:
        console.print("\n[cyan]🔔 Enviando notificação de teste...[/]")
        testar_notificacoes()
    
    Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


def main():
    """Função principal da aplicação."""
    while True:
        exibir_menu_principal()
        
        try:
            opcao = Prompt.ask("Escolha uma opção", default="0")
            
            if opcao == '1':
                iniciar_sessao_pomodoro()
            elif opcao == '2':
                iniciar_timer_personalizado()
            elif opcao == '3':
                exibir_configuracoes()
            elif opcao == '4':
                editar_configuracoes()
            elif opcao == '5':
                resetar_configuracoes_menu()
            elif opcao == '6':
                exibir_estatisticas()
            elif opcao == '7':
                exibir_historico()
            elif opcao == '8':
                exibir_sobre()
            elif opcao == '0':
                limpar_tela()
                console.print("\n[bold green]👋 Até logo! Continue produtivo! 🍅[/]\n")
                sys.exit(0)
            else:
                console.print("\n[red]❌ Opção inválida! Tente novamente.[/]")
                Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")
        
        except KeyboardInterrupt:
            limpar_tela()
            console.print("\n\n[bold green]👋 Até logo! Continue produtivo! 🍅[/]\n")
            sys.exit(0)
        except Exception as e:
            console.print(f"\n[red]❌ Erro inesperado: {e}[/]")
            Prompt.ask("[dim]Pressione ENTER para continuar[/dim]", default="")


if __name__ == "__main__":
    main()
