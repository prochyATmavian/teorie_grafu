@echo off
REM Pomocný skript pro snadné spouštění analýzy grafů na Windows

setlocal enabledelayedexpansion

echo ╔══════════════════════════════════════════╗
echo ║     Rozpoznávač grafů - Quick Start      ║
echo ╚══════════════════════════════════════════╝
echo.

REM Kontrola virtuálního prostředí
if not exist "venv\Scripts\python.exe" (
    echo ❌ Virtuální prostředí nebylo nalezeno!
    echo.
    echo Vytvořte ho pomocí:
    echo   python -m venv venv
    echo   venv\Scripts\activate
    echo   pip install -r requirements.txt
    echo.
    exit /b 1
)

REM Menu
echo Vyberte akci:
echo   1^) Analýza vlastností grafu + uzly
echo   2^) Analýza matic ^(interaktivní^)
echo   3^) Kompletní analýza
echo.
set /p choice="Volba (1-3): "

REM Zadání souboru
if "%~1"=="" (
    echo.
    echo Zadejte cestu k souboru s grafem:
    echo   ^(např: data\grafy\02.tg^)
    set /p filepath="Soubor: "
) else (
    set filepath=%~1
)

REM Kontrola existence souboru
if not exist "%filepath%" (
    echo ❌ Soubor '%filepath%' neexistuje!
    exit /b 1
)

echo.
echo 🚀 Spouštím analýzu...
echo.

REM Spuštění podle volby
if "%choice%"=="1" goto analyze_properties
if "%choice%"=="2" goto analyze_matrices
if "%choice%"=="3" goto analyze_complete
goto invalid_choice

:analyze_properties
REM Analýza vlastností
if not "%~2"=="" (
    REM Zadány uzly jako parametry
    shift
    venv\Scripts\python.exe scripts\analyze_properties.py "%filepath%" %*
) else (
    echo Zadejte uzly pro detailní analýzu ^(oddělené mezerou, Enter pro přeskočení^):
    set /p nodes="Uzly: "
    if "!nodes!"=="" (
        venv\Scripts\python.exe scripts\analyze_properties.py "%filepath%"
    ) else (
        venv\Scripts\python.exe scripts\analyze_properties.py "%filepath%" !nodes!
    )
)
goto end

:analyze_matrices
REM Analýza matic (interaktivní)
venv\Scripts\python.exe scripts\analyze_matrices.py "%filepath%"
goto end

:analyze_complete
REM Kompletní analýza
if not "%~2"=="" (
    shift
    venv\Scripts\python.exe scripts\run.py "%filepath%" %*
) else (
    echo Zadejte uzly pro detailní analýzu ^(oddělené mezerou, Enter pro přeskočení^):
    set /p nodes="Uzly: "
    if "!nodes!"=="" (
        venv\Scripts\python.exe scripts\run.py "%filepath%"
    ) else (
        venv\Scripts\python.exe scripts\run.py "%filepath%" !nodes!
    )
)
goto end

:invalid_choice
echo ❌ Neplatná volba!
exit /b 1

:end
endlocal

