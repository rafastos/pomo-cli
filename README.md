# 🍅 Pomo CLI

Timer Pomodoro para linha de comando com interface moderna e rica em recursos.

## ✨ Recursos

- ⏱️ **Timer Pomodoro completo** com ciclos automáticos
- 🎨 **Interface colorida** usando a biblioteca Rich
- ⚙️ **Configurações personalizáveis** salvas em JSON
- 📊 **Estatísticas detalhadas** de produtividade
- 📜 **Histórico de sessões** com registro completo
- 🔔 **Notificações desktop** nativas (macOS, Linux, Windows)
- 🔊 **Alertas sonoros** ao finalizar sessões
- ⏲️ **Timer personalizado** para outras atividades

## 📁 Estrutura do Projeto

```
pomo-cli/
├── pomo.py              # Arquivo principal (orquestra os módulos)
├── config.py            # Gerenciamento de configurações
├── historico.py         # Rastreamento de sessões
├── funcoes.py           # Funções utilitárias (timer, som)
├── notificacoes.py      # Sistema de notificações desktop
├── interface.py         # Interface de usuário (menus, exibições)
├── timer.py             # Lógica de execução de timers
├── editor_config.py     # Editor interativo de configurações
├── config.json          # Arquivo de configurações (gerado)
├── historico.json       # Arquivo de histórico (gerado)
├── requirements.txt     # Dependências Python
├── run.sh              # Script de execução
└── README.md           # Este arquivo
```

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/rafastos/pomo-cli.git
cd pomo-cli
```

### 2. Configure o ambiente Python

```bash
# Crie um ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual
source .venv/bin/activate  # macOS/Linux
# ou
.venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
# Usando o script de execução
./run.sh

# Ou diretamente com Python
python pomo.py
```

## 📖 Como usar

### Menu Principal

```
🍅 POMO CLI - Timer Pomodoro
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] Iniciar sessão Pomodoro
[2] Iniciar timer personalizado
[3] Ver configurações
[4] Editar configurações
[5] Resetar configurações
[6] Ver estatísticas
[7] Ver histórico
[8] Sobre
[0] Sair
```

### Sessão Pomodoro

Uma sessão completa segue a técnica tradicional:
- **4 ciclos** de trabalho (padrão: 25 minutos)
- **Descansos curtos** entre ciclos (padrão: 5 minutos)
- **Descanso longo** após todos os ciclos (padrão: 15 minutos)

### Configurações Personalizáveis

- ⏱️ Tempo de trabalho (1-999 minutos)
- ☕ Descanso curto (1-999 minutos)
- 🌴 Descanso longo (1-999 minutos)
- 🔄 Número de ciclos (1-20)
- 🔊 Som habilitado (Sim/Não)
- ⚡ Auto-iniciar descanso (Sim/Não)
- 🔔 Notificações desktop (Sim/Não)

### Histórico e Estatísticas

O sistema registra todas as sessões e fornece:
- 📈 Total de sessões completas e canceladas
- ⏱️ Tempo total de trabalho
- 🍅 Número de Pomodoros completados
- 📅 Estatísticas do dia atual
- 📊 Médias de produtividade

## 🔧 Dependências

- **Python 3.7+**
- **rich** - Interface de terminal moderna

Instale com:
```bash
pip install rich
```

## 🔔 Notificações

As notificações desktop funcionam nativamente em:
- **macOS**: Usando `osascript` (AppleScript)
- **Linux**: Usando `notify-send`
- **Windows**: Usando `plyer`

## 💾 Arquivos de Dados

### config.json
Armazena suas configurações personalizadas:
```json
{
  "tempo_trabalho": 25,
  "descanso_curto": 5,
  "descanso_longo": 15,
  "ciclos": 4,
  "som_habilitado": true,
  "auto_iniciar_descanso": false,
  "notificacoes_habilitadas": true
}
```

### historico.json
Registra todas as suas sessões:
```json
[
  {
    "tipo": "trabalho",
    "duracao_minutos": 25,
    "completa": true,
    "data": "12/11/2025",
    "hora": "14:30:00",
    "timestamp": 1699804200.0
  }
]
```

## 🎯 Módulos

### pomo.py (Principal)
- Orquestra todos os módulos
- Gerencia o loop principal da aplicação
- Coordena navegação entre menus

### interface.py
- Menus interativos
- Exibição de estatísticas
- Visualização de histórico
- Painéis informativos

### timer.py
- Lógica de execução de timers
- Barras de progresso
- Integração com notificações
- Gerenciamento de sessões Pomodoro

### editor_config.py
- Interface de edição de configurações
- Validação de valores
- Persistência de alterações

### config.py
- Carregamento e salvamento de configurações
- Validação de valores
- Resetar para padrões

### historico.py
- Registro de sessões
- Cálculo de estatísticas
- Filtragem por data
- Formatação de duração

### notificacoes.py
- Notificações desktop multiplataforma
- Sons de alerta
- Mensagens contextuais

### funcoes.py
- Gerador de contagem regressiva
- Sons multiplataforma
- Utilitários gerais

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novos recursos
- Enviar pull requests

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👨‍💻 Autor

**rafastos**
- GitHub: [@rafastos](https://github.com/rafastos)

## 🙏 Agradecimentos

- Técnica Pomodoro criada por Francesco Cirillo
- Biblioteca Rich por Will McGugan

---

⭐ Se você achou este projeto útil, considere dar uma estrela!
