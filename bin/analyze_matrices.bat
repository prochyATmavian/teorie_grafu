@echo off
REM Rychlý spouštěcí skript pro analýzu matic (Windows)

cd /d "%~dp0.."

if "%~1"=="" (
    echo Použití: analyze_matrices.bat ^<soubor_s_grafem^> [--all] [řádek] [sloupec]
    echo.
    echo Příklady:
    echo   analyze_matrices.bat data\grafy\02.tg              ^(interaktivní^)
    echo   analyze_matrices.bat data\grafy\02.tg --all        ^(všechny matice^)
    echo   analyze_matrices.bat data\grafy\02.tg --all 0 1    ^(index [0][1]^)
    echo.
    echo Indexování od 0!
    exit /b 1
)

venv\Scripts\python.exe scripts\analyze_matrices.py %*

