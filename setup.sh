#!/bin/bash

# BasCAT Setup Script
# Detects OS and creates platform-specific virtual environment

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== BasCAT Environment Setup ==="

# Detect OS
case "$(uname -s)" in
    Linux*)     OS_TYPE="linux" ;;
    Darwin*)    OS_TYPE="mac" ;;
    CYGWIN*|MINGW*|MSYS*) OS_TYPE="win" ;;
    *)          OS_TYPE="unknown" ;;
esac

echo "Detected OS: $OS_TYPE"

# Set venv directory based on OS
VENV_DIR="venv-$OS_TYPE"

echo "Virtual environment: $VENV_DIR"

# Check if venv exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Activate venv (handle Windows Git Bash vs Unix)
if [ "$OS_TYPE" = "win" ]; then
    source "$VENV_DIR/Scripts/activate"
else
    source "$VENV_DIR/bin/activate"
fi

echo "Activated: $VENV_DIR"

# Update pip
pip install --upgrade pip -q

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt -q
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

echo ""
echo "=== Setup Complete ==="
echo "Virtual environment: $VENV_DIR"
echo ""
echo "To activate manually:"
if [ "$OS_TYPE" = "win" ]; then
    echo "  source $VENV_DIR/Scripts/activate"
else
    echo "  source $VENV_DIR/bin/activate"
fi
echo ""
echo "To run BasCAT:"
echo "  ./run.sh"
