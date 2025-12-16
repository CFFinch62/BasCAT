# -*- mode: python ; coding: utf-8 -*-
"""
BasCAT PyInstaller Spec File

This spec file configures PyInstaller to bundle BasCAT into a single executable.
It includes all necessary data files (assets, icons, docs, examples).

Build with:
    pyinstaller bascat.spec --clean

Or use the platform-specific build scripts:
    ./build_linux.sh
    build_windows.bat
    ./build_macos.sh
"""

import os

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(SPEC))

a = Analysis(
    ['src/bascat.py'],
    pathex=[PROJECT_ROOT],
    binaries=[],
    datas=[
        # Include assets (stylesheets)
        ('assets', 'assets'),
        # Include icons
        ('icons', 'icons'),
        # Include user documentation
        ('docs', 'docs'),
        # Include example programs
        ('examples', 'examples'),
    ],
    hiddenimports=[
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude development-only modules
        'pytest',
        'black',
        'flake8',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='bascat',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window (GUI app)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icons/bascat_icon_512_v2.png',  # App icon
)
