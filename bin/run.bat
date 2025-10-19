@echo off
REM Rychlý spouštěcí skript pro kompletní analýzu (Windows)

cd /d "%~dp0.."

if "%~1"=="" (
    echo Použití: run.bat ^<soubor_s_grafem^> [uzel1] [uzel2] ...
    echo Příklad: run.bat data\grafy\02.tg A B C
    echo          run.bat data\grafy\02.tg          ^(bez uzlů^)
    exit /b 1
)

venv\Scripts\python.exe scripts\run.py %*

