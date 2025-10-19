# Použití na Windows

Návod pro spouštění analyzátoru grafů na operačním systému Windows.

## 🪟 Instalace

### 1. Instalace Python
- Stáhněte Python 3.10+ z [python.org](https://www.python.org/downloads/)
- Při instalaci zaškrtněte **"Add Python to PATH"**

### 2. Vytvoření virtuálního prostředí

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Spouštění programů

### Varianta 1: Interaktivní menu (doporučeno)

```cmd
analyze.bat
```

Nebo s předvoleným souborem:
```cmd
analyze.bat data\grafy\02.tg
```

**Menu:**
```
Vyberte akci:
  1) Analýza vlastností grafu + uzly
  2) Analýza matic (interaktivní)
  3) Kompletní analýza
  4) Spustit testy matic

Volba (1-4):
```

### Varianta 2: Přímé spuštění

#### Analýza vlastností
```cmd
REM Bez uzlů
analyze_properties.bat data\grafy\02.tg

REM S uzly
analyze_properties.bat data\grafy\02.tg A B C
```

#### Analýza matic
```cmd
REM Interaktivní výběr matice
analyze_matrices.bat data\grafy\02.tg

REM Všechny matice
analyze_matrices.bat data\grafy\02.tg --all

REM Všechny matice, konkrétní index [0][1]
analyze_matrices.bat data\grafy\02.tg --all 0 1
```

#### Kompletní analýza
```cmd
run.bat data\grafy\02.tg A B
```

### Varianta 3: Přes Python přímo

```cmd
venv\Scripts\python.exe scripts\analyze_properties.py data\grafy\02.tg A B
venv\Scripts\python.exe scripts\analyze_matrices.py data\grafy\02.tg
venv\Scripts\python.exe scripts\run.py data\grafy\02.tg A B
```

## 🧪 Testy

```cmd
REM Spuštění testů přes menu
analyze.bat
REM Pak vyberte volbu 4

REM Nebo přímo:
test_interactive_matrix.bat
```

## 📁 Cesty k souborům

Na Windows používejte **zpětné lomítko** `\`:

```cmd
data\grafy\01.tg          ✅ Správně
data/grafy/01.tg          ⚠️  Funguje, ale není Windows styl
```

## 🔧 Dostupné .bat skripty

| Soubor | Účel |
|--------|------|
| `analyze.bat` | Interaktivní menu |
| `analyze_properties.bat` | Analýza vlastností + uzly |
| `analyze_matrices.bat` | Analýza matic |
| `run.bat` | Kompletní analýza |
| `test_interactive_matrix.bat` | Testy matic |

## 📝 Příklady použití

### Příklad 1: Interaktivní menu

```cmd
C:\projekt> analyze.bat

╔══════════════════════════════════════════╗
║     Rozpoznávač grafů - Quick Start      ║
╚══════════════════════════════════════════╝

Vyberte akci:
  1) Analýza vlastností grafu + uzly
  2) Analýza matic (interaktivní)
  3) Kompletní analýza
  4) Spustit testy matic

Volba (1-4): 2

Zadejte cestu k souboru s grafem:
  (např: data\grafy\02.tg)
Soubor: data\grafy\01.tg

🚀 Spouštím analýzu...

============================================================
INTERAKTIVNÍ VÝBĚR MATICE
============================================================

Vyberte matici k sestavení:
  a) Matice sousednosti
  b) Znaménková matice
  c) Mocniny matice sousednosti (A^2, A^3)
  d) Matice incidence
  e) Matice délek (Floyd-Warshall)
  h) Seznam sousedů
  *) Všechny matice

Vaše volba (a/b/c/d/e/h/*): e

Načítám graf ze souboru: data\grafy\01.tg
Načteno: 8 uzlů, 14 hran

------------------------------------------------------------
Chcete zobrazit konkrétní index matice? (a/n): a
Zadejte řádek (od 0): 0
Zadejte sloupec (od 0): 1

🔍 Zobrazuji index [0][1]

============================================================
VÝSLEDKY
============================================================

e) Matice délek (Floyd-Warshall)[A][B] = 1.0
   (index: [0][1])

============================================================
HOTOVO
============================================================
```

### Příklad 2: Rychlé spuštění

```cmd
REM Vlastnosti grafu s uzly A, B
C:\projekt> analyze_properties.bat data\grafy\02.tg A B

REM Všechny matice
C:\projekt> analyze_matrices.bat data\grafy\02.tg --all

REM Konkrétní prvek matice [0][1]
C:\projekt> analyze_matrices.bat data\grafy\02.tg --all 0 1
```

### Příklad 3: Spuštění testů

```cmd
C:\projekt> analyze.bat

Volba (1-4): 4

📊 Spouštím testy interaktivních matic...

╔══════════════════════════════════════════════════════════╗
║          TESTY INTERAKTIVNÍHO VÝBĚRU MATIC               ║
╚══════════════════════════════════════════════════════════╝

=== TEST 1: Interaktivní režim - Matice sousednosti, celá matice ===
...
```

## ⚙️ Aktivace virtuálního prostředí

Pokud chcete spustit program ručně:

```cmd
REM Aktivace prostředí
venv\Scripts\activate

REM Spuštění programu
python scripts\analyze_properties.py data\grafy\02.tg A B

REM Deaktivace prostředí
deactivate
```

## 🔍 Řešení problémů

### "Python není rozpoznán jako interní příkaz"

→ Python není v PATH. Přeinstalujte Python a zaškrtněte "Add Python to PATH".

### "venv\Scripts\python.exe nenalezen"

→ Virtuální prostředí neexistuje. Vytvořte ho:
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Chyby s kódováním (ř, č, ě, ...)

→ Ujistěte se, že terminál používá UTF-8:
```cmd
chcp 65001
```

### "Soubor neexistuje"

→ Používejte zpětná lomítka `\` místo `/` v cestách:
```cmd
data\grafy\01.tg  ✅
data/grafy/01.tg  ❌
```

## 📊 Výstupy

Vykreslené grafy se ukládají do:
```
output\vykreslene_grafy\graf_<jmeno>.png
```

## 🔗 Porovnání Linux/Mac vs Windows

| Akce | Linux/Mac | Windows |
|------|-----------|---------|
| Spuštění menu | `./analyze.sh` | `analyze.bat` |
| Vlastnosti | `./venv/bin/python scripts/...` | `venv\Scripts\python.exe scripts\...` |
| Cesta k souboru | `data/grafy/01.tg` | `data\grafy\01.tg` |
| Aktivace venv | `source venv/bin/activate` | `venv\Scripts\activate` |
| Testy | `bash test_interactive_matrix.sh` | `test_interactive_matrix.bat` |

## 💡 Tipy pro Windows

1. **Používejte PowerShell nebo CMD** s administrátorskými právy pro instalaci
2. **Zpětná lomítka** v cestách: `data\grafy\` místo `data/grafy/`
3. **UTF-8 kódování** pro správné zobrazení českých znaků
4. **Antivirus** může zpomalovat Python - přidejte venv do výjimek
5. **Git Bash** funguje také, pokud preferujete Unix styl

## 🎯 Doporučené workflow pro Windows

```cmd
REM 1. První spuštění - instalace
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
deactivate

REM 2. Každodenní použití - interaktivní menu
analyze.bat

REM 3. Rychlé spuštění konkrétní analýzy
analyze_properties.bat data\grafy\02.tg A B
analyze_matrices.bat data\grafy\02.tg --all 0 1
```

## 📚 Související dokumentace

- [QUICKSTART.md](../QUICKSTART.md) - Rychlý start (Unix/Linux/Mac)
- [POUZITI.md](POUZITI.md) - Detailní návod
- [INTERAKTIVNI_MATICE.md](INTERAKTIVNI_MATICE.md) - Interaktivní matice

