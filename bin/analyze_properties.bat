@echo off
REM Rychlý spouštěcí skript pro analýzu vlastností (Windows)

cd /d "%~dp0.."

if "%~1"=="" (
    echo Použití: analyze_properties.bat ^<soubor_s_grafem^> [uzel1] [uzel2] ...
    echo Příklad: analyze_properties.bat data\grafy\02.tg A B C
    echo          analyze_properties.bat data\grafy\02.tg          ^(bez uzlů^)
    exit /b 1
)

venv\Scripts\python.exe scripts\analyze_properties.py %*

