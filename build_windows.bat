@echo off
REM Build BasCAT for Windows
REM Creates a single executable in dist\bascat.exe

echo === Building BasCAT for Windows ===

cd /d "%~dp0"

set VENV_DIR=venv-win

REM Activate virtual environment if it exists
if exist "%VENV_DIR%\Scripts\activate.bat" (
    call %VENV_DIR%\Scripts\activate.bat
    echo Activated virtual environment: %VENV_DIR%
) else (
    echo Error: %VENV_DIR% not found. Run setup.sh first.
    pause
    exit /b 1
)

REM Ensure PyInstaller is installed
pip install pyinstaller -q

REM Build the executable
echo Running PyInstaller...
pyinstaller bascat.spec --clean --noconfirm

echo.
echo === Build Complete ===
echo Executable created at: dist\bascat.exe
echo.
echo To run: dist\bascat.exe

pause
