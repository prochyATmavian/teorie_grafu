# Quick Start Guide

## 🚀 Rychlé spuštění

### 1. První spuštění
```bash
# Instalace závislostí
bash tools/setup_venv.sh

# Aktivace prostředí
source venv/bin/activate
```

### 2. Analýza grafů

#### Interaktivní režim (nejjednodušší)
```bash
./analyze.sh
# Nebo s parametry:
./analyze.sh data/grafy/02.tg
```

#### Přímé spuštění

**Vlastnosti grafu + uzly:**
```bash
./venv/bin/python scripts/analyze_properties.py data/grafy/02.tg
./venv/bin/python scripts/analyze_properties.py data/grafy/02.tg A B C
```

**Matice:**
```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/02.tg
```

**Kompletní analýza:**
```bash
./venv/bin/python scripts/run.py data/grafy/02.tg A B
```

## 📝 Formát souborů

Vytvořte soubor `data/grafy/muj_graf.tg`:
```
u A;
u B;
u C;
h A - B 5;    # Neorientovaná hrana s váhou 5
h B > C 3;    # Orientovaná hrana B→C s váhou 3
```

Pak analyzujte:
```bash
./venv/bin/python scripts/analyze_properties.py data/grafy/muj_graf.tg A B
```

## 📊 Výstupy

- **Výpis:** V terminálu
- **Obrázky:** `output/vykreslene_grafy/graf_<jmeno>.png`

## 📚 Více informací

- [POUZITI.md](docs/POUZITI.md) - Detailní návod
- [DOKUMENTACE.md](docs/DOKUMENTACE.md) - Technická dokumentace
- [STRUKTURA.md](docs/STRUKTURA.md) - Struktura projektu

## 🆘 Problémy?

```bash
# Test prostředí
./venv/bin/python tools/test_venv.py

# Reinstalace
rm -rf venv
bash tools/setup_venv.sh
```

