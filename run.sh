#!/bin/bash
# Script para executar o Pomo CLI

# Ativa o ambiente virtual e executa o programa
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Verifica se o ambiente virtual existe
if [ ! -d ".venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv .venv
fi

# Ativa o ambiente virtual e instala dependências se necessário
source .venv/bin/activate

# Verifica se as dependências estão instaladas
if ! python -c "import rich" 2>/dev/null; then
    echo "Instalando dependências..."
    pip install -q -r requirements.txt
fi

# Executa o programa
python pomo.py
