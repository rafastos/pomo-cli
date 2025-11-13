# 📊 Estrutura do Projeto Pomo CLI

```
✅ pomo.py                (arquivo principal)
✅ interface.py           (visualização e menus)
✅ timer.py               (lógica de timers)
✅ editor_config.py       (editor de configurações)
✅ notificacoes.py        (notificações)
✅ historico.py           (histórico e stats)
✅ config.py              (configurações)
✅ funcoes.py             (utilitários)
──────────────────────────────────
```

## 🎯 Separação de Responsabilidades

### 🎬 pomo.py (Principal)
**Responsabilidade**: Orquestração e coordenação
```
├── Importa todos os módulos
├── Menu de timer personalizado
├── Menu de reset de configurações
├── Menu de histórico
├── Menu de limpar histórico
├── Menu de testar notificações
└── Loop principal (main)
```

### 🎨 interface.py (UI)
**Responsabilidade**: Interface visual
```
├── limpar_tela()
├── exibir_menu_principal()
├── exibir_configuracoes()
├── exibir_sobre()
├── exibir_estatisticas()
├── exibir_menu_historico()
├── exibir_sessoes_recentes()
└── exibir_sessoes_hoje()
```

### ⏱️ timer.py (Lógica de Tempo)
**Responsabilidade**: Execução de timers
```
├── executar_timer()
│   ├── Barra de progresso
│   ├── Notificações de início/fim
│   ├── Sons
│   └── Registro no histórico
└── iniciar_sessao_pomodoro()
    ├── Loop de ciclos
    ├── Trabalho + descanso
    └── Notificação de conclusão
```

### ✏️ editor_config.py (Editor)
**Responsabilidade**: Edição interativa de configurações
```
├── editar_configuracoes()
├── _editar_tempo_trabalho()
├── _editar_descanso_curto()
├── _editar_descanso_longo()
├── _editar_ciclos()
├── _editar_som()
├── _editar_auto_iniciar()
└── _editar_notificacoes()
```

### 🔔 notificacoes.py (Notificações)
**Responsabilidade**: Sistema de notificações desktop
```
├── enviar_notificacao()
├── enviar_notificacao_macos()
├── enviar_notificacao_linux()
├── enviar_notificacao_windows()
├── notificar_trabalho_iniciado()
├── notificar_trabalho_concluido()
├── notificar_descanso_iniciado()
├── notificar_descanso_concluido()
├── notificar_pomodoro_completo()
└── notificar_timer_personalizado_concluido()
```

### 📜 historico.py (Dados)
**Responsabilidade**: Persistência e estatísticas
```
├── adicionar_sessao()
├── obter_estatisticas()
├── obter_sessoes_recentes()
├── obter_sessoes_por_data()
├── limpar_historico()
├── formatar_duracao()
└── traduzir_tipo()
```

### ⚙️ config.py (Configurações)
**Responsabilidade**: Gerenciamento de settings
```
├── carregar_configuracoes()
├── salvar_configuracoes()
├── resetar_configuracoes()
├── validar_valor()
└── obter_caminho_config()
```

### 🔧 funcoes.py (Utilitários)
**Responsabilidade**: Funções auxiliares
```
├── contar_tempo()  # Gerador de contagem regressiva
└── tocar_som()     # Sons multiplataforma
```

## 🔄 Fluxo de Execução

```
┌─────────────────────────────────────────────────────┐
│                     pomo.py                         │
│              (Loop Principal - Main)                │
└─────────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ interface.py │ │   timer.py   │ │editor_config │
│   (Menus)    │ │  (Timers)    │ │   (Editor)   │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  config.py   │ │ historico.py │ │notificacoes  │
│ (Settings)   │ │   (Data)     │ │  (Alerts)    │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
                        ▼
                ┌──────────────┐
                │ funcoes.py   │
                │ (Utilities)  │
                └──────────────┘
```
