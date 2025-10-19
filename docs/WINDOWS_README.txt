═══════════════════════════════════════════════════════════════
                ROZPOZNÁVAČ GRAFŮ - WINDOWS
═══════════════════════════════════════════════════════════════

🪟 RYCHLÝ START PRO WINDOWS:

1. Vytvoření virtuálního prostředí:
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   deactivate

2. Spuštění programu:
   analyze.bat

═══════════════════════════════════════════════════════════════

📋 DOSTUPNÉ .BAT SOUBORY:

analyze.bat              - Interaktivní menu (doporučeno)
analyze_properties.bat   - Analýza vlastností + uzly
analyze_matrices.bat     - Analýza matic (interaktivní)
run.bat                  - Kompletní analýza
test_interactive_matrix.bat - Testy matic

═══════════════════════════════════════════════════════════════

💡 PŘÍKLADY POUŽITÍ:

REM Interaktivní menu:
analyze.bat

REM S předvoleným souborem:
analyze.bat data\grafy\02.tg

REM Vlastnosti + uzly:
analyze_properties.bat data\grafy\02.tg A B C

REM Matice (interaktivní výběr):
analyze_matrices.bat data\grafy\01.tg

REM Matice - všechny najednou:
analyze_matrices.bat data\grafy\01.tg --all

REM Matice - konkrétní index [0][1]:
analyze_matrices.bat data\grafy\01.tg --all 0 1

REM Kompletní analýza:
run.bat data\grafy\02.tg A B

REM Spuštění testů:
test_interactive_matrix.bat

═══════════════════════════════════════════════════════════════

⚠️  DŮLEŽITÉ PRO WINDOWS:

1. Používejte ZPĚTNÉ LOMÍTKO \ v cestách:
   ✅ data\grafy\01.tg
   ❌ data/grafy/01.tg

2. Pro české znaky nastavte UTF-8:
   chcp 65001

3. Spouštějte z CMD nebo PowerShell

4. Pokud nefunguje dvojklik, spusťte z terminálu

═══════════════════════════════════════════════════════════════

📂 STRUKTURA (stejná jako na Unix):

rozeznavac_grafu\
├── src\                 - Zdrojové kódy
├── scripts\             - Spouštěcí skripty
├── data\grafy\          - Grafové soubory
├── output\vykreslene_grafy\ - Vykreslené PNG
├── docs\                - Dokumentace
├── tools\               - Pomocné nástroje
└── venv\                - Virtual environment

═══════════════════════════════════════════════════════════════

🔍 ŘEŠENÍ PROBLÉMŮ:

"Python není rozpoznán..."
→ Přidejte Python do PATH nebo přeinstalujte

"venv\Scripts\python.exe nenalezen"
→ Vytvořte venv: python -m venv venv

"ModuleNotFoundError: No module named 'matplotlib'"
→ Aktivujte venv a instalujte: pip install -r requirements.txt

Špatné zobrazení českých znaků
→ chcp 65001

═══════════════════════════════════════════════════════════════

📚 DOKUMENTACE:

docs\WINDOWS.md              - Tento návod (podrobný)
docs\POUZITI.md              - Obecný návod k použití
docs\INTERAKTIVNI_MATICE.md  - Práce s maticemi
QUICKSTART.md                - Rychlý start (Unix/Mac)

═══════════════════════════════════════════════════════════════

🎯 TIPY:

1. Pro opakované použití vytvořte zástupce na ploše k analyze.bat
2. Můžete přetáhnout soubor .tg na analyze.bat
3. Všechny funkce jsou stejné jako na Linux/Mac
4. Výstupy (PNG) najdete v output\vykreslene_grafy\

═══════════════════════════════════════════════════════════════

