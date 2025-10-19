# Instalace virtuálního prostředí (venv)

## 📦 Rychlá instalace

### Varianta 1: Automaticky (doporučeno)

```bash
# Spusťte instalační skript
bash setup_venv.sh
```

### Varianta 2: Manuálně

```bash
# 1. Vytvořte virtuální prostředí
python3 -m venv venv

# 2. Aktivujte venv
source venv/bin/activate

# 3. Aktualizujte pip
pip install --upgrade pip

# 4. Nainstalujte knihovny
pip install -r requirements.txt

# 5. Ověřte instalaci
python3 -c "import matplotlib, networkx, graphviz; print('✓ Všechny knihovny OK')"
```

## 🚀 Spuštění programu s venv

### Varianta 1: S aktivovaným venv

```bash
# Aktivujte venv
source venv/bin/activate

# Spusťte program
python3 run.py <soubor.tg>

# Příklad
python3 run.py /Users/prochy/Downloads/grafy/01.tg
```

### Varianta 2: Pomocí wrapperu

```bash
# Spusťte wrapper skript (automaticky aktivuje venv)
bash run_with_venv.sh <soubor.tg>

# Příklad
bash run_with_venv.sh /Users/prochy/Downloads/grafy/01.tg
```

### Varianta 3: Přímá cesta

```bash
# Spusťte přímo s venv Python interpretrem
./venv/bin/python3 run.py <soubor.tg>

# Příklad
./venv/bin/python3 run.py /Users/prochy/Downloads/grafy/01.tg
```

## 📚 Nainstalované knihovny

Po instalaci budou k dispozici:

- **matplotlib** - Pro grafickou vizualizaci
- **networkx** - Pro pokročilé operace s grafy
- **graphviz** - Pro profesionální vizualizaci

## ⚠️ Poznámky

- Program **funguje i bez venv** - použije se textová vizualizace
- Venv je **volitelné** - pouze pro grafickou vizualizaci
- Na školních serverech (akela, kiwi) možná nebudou knihovny k dispozici

## 🔧 Řešení problémů

### Problém: graphviz se nenainstaluje

```bash
# Na macOS nainstalujte graphviz přes Homebrew
brew install graphviz

# Pak znovu nainstalujte Python knihovnu
pip install graphviz
```

### Problém: matplotlib se nenainstaluje

```bash
# Zkuste starší verzi
pip install matplotlib==3.5.0
```

### Problém: venv se nedá aktivovat

```bash
# Ujistěte se, že máte Python 3.6+
python3 --version

# Znovu vytvořte venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```

## ✅ Ověření instalace

Po instalaci zkontrolujte:

```bash
# Aktivujte venv
source venv/bin/activate

# Spusťte test
python3 -c "
import sys
print(f'Python: {sys.executable}')
try:
    import matplotlib
    print('✓ matplotlib')
except: print('✗ matplotlib')
try:
    import networkx
    print('✓ networkx')
except: print('✗ networkx')
try:
    import graphviz
    print('✓ graphviz')
except: print('✗ graphviz')
"
```

## 📝 Deaktivace venv

```bash
# Pro deaktivaci venv
deactivate
```

## 🗑️ Odstranění venv

```bash
# Smazání virtuálního prostředí
rm -rf venv
```

