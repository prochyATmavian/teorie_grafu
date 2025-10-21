@echo off
REM Spouštěč hlavního interaktivního programu (Windows)

cd /d "%~dp0"

REM Aktivace virtual environment (pokud existuje)
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Spuštění programu
python main.py %*

if exist venv\Scripts\activate.bat (
    deactivate
)

