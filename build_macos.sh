#!/bin/bash
# Build BasCAT for macOS
# Creates a single executable in dist/bascat

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VENV_DIR="venv-mac"

echo "=== Building BasCAT for macOS ==="

# Activate virtual environment if it exists
if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/bin/activate"
    echo "Activated virtual environment: $VENV_DIR"
else
    echo "Error: $VENV_DIR not found. Run ./setup.sh first."
    exit 1
fi

# Ensure PyInstaller is installed
pip install pyinstaller -q

# Build the executable
echo "Running PyInstaller..."
pyinstaller bascat.spec --clean --noconfirm

echo ""
echo "=== Build Complete ==="
echo "Executable created at: dist/bascat"
echo ""
echo "To run: ./dist/bascat"
echo ""
echo "Note: For distribution, you may want to sign and notarize the app."
