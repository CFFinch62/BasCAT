#!/bin/bash

# BasCAT Run Script
# Detects OS and uses the correct platform-specific virtual environment

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Detect OS
case "$(uname -s)" in
    Linux*)     OS_TYPE="linux" ;;
    Darwin*)    OS_TYPE="mac" ;;
    CYGWIN*|MINGW*|MSYS*) OS_TYPE="win" ;;
    *)          OS_TYPE="unknown" ;;
esac

VENV_DIR="venv-$OS_TYPE"

# Check if venv exists, if not run setup
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Running setup..."
    chmod +x setup.sh
    ./setup.sh
    if [ $? -ne 0 ]; then
        echo "Setup failed. Exiting."
        exit 1
    fi
fi

# Activate venv (handle Windows Git Bash vs Unix)
if [ "$OS_TYPE" = "win" ]; then
    source "$VENV_DIR/Scripts/activate"
else
    source "$VENV_DIR/bin/activate"
fi

# Set PYTHONPATH to include the current directory so imports work correctly
export PYTHONPATH=$PYTHONPATH:$(pwd)

echo "Starting BasCAT..."
python src/bascat.py
