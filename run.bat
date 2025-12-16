@echo off
REM BasCAT Run Script for Windows
REM Uses platform-specific virtual environment (venv-win)

cd /d "%~dp0"

set VENV_DIR=venv-win

REM Check if venv exists, if not run setup
if not exist "%VENV_DIR%" (
    echo Virtual environment not found. Running setup...
    call setup.bat
    if errorlevel 1 (
        echo Setup failed. Exiting.
        pause
        exit /b 1
    )
)

REM Activate venv
call %VENV_DIR%\Scripts\activate.bat

REM Set PYTHONPATH
set PYTHONPATH=%PYTHONPATH%;%cd%

echo Starting BasCAT...
python src\bascat.py
