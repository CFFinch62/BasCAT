@echo off
REM BasCAT Setup Script for Windows
REM Creates platform-specific virtual environment (venv-win)

echo === BasCAT Environment Setup ===

cd /d "%~dp0"

set VENV_DIR=venv-win

echo Virtual environment: %VENV_DIR%

REM Check if venv exists
if not exist "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
) else (
    echo Virtual environment already exists.
)

REM Activate venv
call %VENV_DIR%\Scripts\activate.bat
echo Activated: %VENV_DIR%

REM Update pip
pip install --upgrade pip -q

REM Install requirements
if exist "requirements.txt" (
    echo Installing requirements...
    pip install -r requirements.txt -q
) else (
    echo Error: requirements.txt not found!
    pause
    exit /b 1
)

echo.
echo === Setup Complete ===
echo Virtual environment: %VENV_DIR%
echo.
echo To activate manually:
echo   %VENV_DIR%\Scripts\activate.bat
echo.
echo To run BasCAT:
echo   run.bat
echo.
pause
