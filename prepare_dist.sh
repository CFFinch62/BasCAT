#!/bin/bash
# Prepare BasCAT Distribution Package
# Creates a clean distribution folder with binaries and user-facing files only

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

DIST_DIR="dist_package"

echo "=== Preparing BasCAT Distribution Package ==="

# Clean previous distribution
if [ -d "$DIST_DIR" ]; then
    echo "Removing previous distribution..."
    rm -rf "$DIST_DIR"
fi

# Create directory structure
echo "Creating directory structure..."
mkdir -p "$DIST_DIR/binaries/linux"
mkdir -p "$DIST_DIR/binaries/windows"
mkdir -p "$DIST_DIR/binaries/macos"
mkdir -p "$DIST_DIR/docs"
mkdir -p "$DIST_DIR/examples"
mkdir -p "$DIST_DIR/images"

# Copy README and Getting Started
echo "Copying documentation..."
cp README.md "$DIST_DIR/"
cp GETTING_STARTED.md "$DIST_DIR/" 2>/dev/null || echo "  - GETTING_STARTED.md not found, skipping"

# Copy user documentation (updated file names)
echo "Copying user guides..."
cp docs/BasCAT_Assembly_Guide.md "$DIST_DIR/docs/" 2>/dev/null || echo "  - BasCAT_Assembly_Guide.md not found"
cp docs/BasCAT_BASIC_Guide.md "$DIST_DIR/docs/" 2>/dev/null || echo "  - BasCAT_BASIC_Guide.md not found"
cp docs/BASCAT_Assembly_Explanation.md "$DIST_DIR/docs/" 2>/dev/null || echo "  - BASCAT_Assembly_Explanation.md not found"

# Copy examples
echo "Copying examples..."
cp -r examples/* "$DIST_DIR/examples/" 2>/dev/null || echo "  - No examples found, skipping"

# Copy images for README
echo "Copying images..."
cp -r images/* "$DIST_DIR/images/" 2>/dev/null || echo "  - No images found, skipping"

# Copy binaries if they exist
echo "Checking for compiled binaries..."
if [ -f "dist/bascat" ]; then
    echo "  - Copying Linux binary"
    cp dist/bascat "$DIST_DIR/binaries/linux/"
else
    echo "  - No Linux binary found (run ./build_linux.sh first)"
fi

if [ -f "dist/bascat.exe" ]; then
    echo "  - Copying Windows binary"
    cp dist/bascat.exe "$DIST_DIR/binaries/windows/"
else
    echo "  - No Windows binary found (build on Windows)"
fi

# Check for macOS binary
if [ -f "dist/bascat" ] && [ "$(uname -s)" = "Darwin" ]; then
    echo "  - Copying macOS binary"
    cp dist/bascat "$DIST_DIR/binaries/macos/"
fi

echo ""
echo "=== Distribution Package Ready ==="
echo ""
echo "Contents of $DIST_DIR/:"
ls -la "$DIST_DIR/"
echo ""
echo "Documentation:"
ls -la "$DIST_DIR/docs/"
echo ""
echo "Next steps:"
echo "  1. Build binaries on each platform (./build_linux.sh, etc.)"
echo "  2. Copy binaries to dist_package/binaries/<platform>/"
echo "  3. Upload dist_package/ to GitHub releases"
