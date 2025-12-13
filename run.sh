#!/bin/bash

VENV_DIR="venv"

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

# Activate venv and run app
source "$VENV_DIR/bin/activate"

# Set PYTHONPATH to include the current directory so imports work correctly
export PYTHONPATH=$PYTHONPATH:$(pwd)

echo "Starting BasCAT..."
python src/bascat.py
