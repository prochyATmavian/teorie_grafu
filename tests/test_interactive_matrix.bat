@echo off
REM Test skript pro testování interaktivního výběru matic (Windows)

cd /d "%~dp0.."

echo ╔══════════════════════════════════════════════════════════╗
echo ║          TESTY INTERAKTIVNÍHO VÝBĚRU MATIC               ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

echo === TEST 1: Interaktivní režim - Matice sousednosti, celá matice ===
echo a> temp_input.txt
echo n>> temp_input.txt
echo.>> temp_input.txt
venv\Scripts\python.exe scripts\analyze_matrices.py data\grafy\01.tg < temp_input.txt

echo.
echo === TEST 2: Interaktivní režim - Matice délek, index [0][1] ===
echo e> temp_input.txt
echo a>> temp_input.txt
echo 0>> temp_input.txt
echo 1>> temp_input.txt
echo.>> temp_input.txt
venv\Scripts\python.exe scripts\analyze_matrices.py data\grafy\01.tg < temp_input.txt

echo.
echo === TEST 3: Všechny matice, index [2][4] ===
echo *> temp_input.txt
echo a>> temp_input.txt
echo 2>> temp_input.txt
echo 4>> temp_input.txt
echo.>> temp_input.txt
venv\Scripts\python.exe scripts\analyze_matrices.py data\grafy\01.tg < temp_input.txt

echo.
echo === TEST 4: Režim --all (všechny matice) ===
venv\Scripts\python.exe scripts\analyze_matrices.py data\grafy\01.tg --all | findstr /N "^" | findstr /R "^[1-9]: ^[1-2][0-9]: ^[3][0]:"

echo.
echo === TEST 5: Režim --all s indexem [2][4] ===
venv\Scripts\python.exe scripts\analyze_matrices.py data\grafy\01.tg --all 2 4

REM Smazání dočasného souboru
del temp_input.txt 2>nul

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║                    TESTY DOKONČENY                       ║
echo ╚══════════════════════════════════════════════════════════╝

