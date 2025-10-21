# 🚀 Hlavní interaktivní program

## Přehled

`main.py` je hlavní interaktivní program pro analýzu grafů. Běží v jednom while cyklu a nabízí menu s různými operacemi.

## Spuštění

### Linux / Mac
```bash
./start.sh
```

### Windows
```cmd
start.bat
```

### Přímé spuštění
```bash
python3 main.py
```

## Jak to funguje

### 1. Načtení grafu

Program začíná načtením grafu:

```
================================================================
NAČTENÍ GRAFU
================================================================

Zadejte cestu k souboru s grafem (nebo 'q' pro ukončení): data/grafy/01.tg

✅ Graf úspěšně načten!
   Soubor: data/grafy/01.tg
   Uzly: 8 - ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
   Hrany: 14
```

### 2. Hlavní menu

Po načtení grafu se zobrazí menu s možnostmi:

```
================================================================
HLAVNÍ MENU
================================================================

📊 ANALÝZA:
  1) Vlastnosti grafu
  2) Vlastnosti uzlu (nebo všech uzlů)
  3) Vlastnosti hrany

📐 MATICE:
  4) Matice sousednosti
  5) N-tá mocnina matice sousednosti
  6) Matice incidence
  7) Matice délek
  8) Matice předchůdců

🔧 OSTATNÍ:
  9) Načíst jiný graf
  0) Ukončit program
================================================================
```

## Funkce programu

### 1️⃣ Vlastnosti grafu

Zobrazí všechny vlastnosti grafu:
- Ohodnocený/neohodnocený
- Orientovaný/neorientovaný
- Souvislý/nesouvislý
- Prostý/neprostý
- Jednoduchý
- Rovinný/nerovinný
- Úplný
- Regulární
- Bipartitní

**Příklad:**
```
📊 Graf: data/grafy/01.tg
   Uzlů: 8
   Hran: 14

Vlastnosti:
  ❌ a_ohodnoceny: False
  ✅ b_orientovany: True
  ✅ c_souvisly: True
  ...
```

### 2️⃣ Vlastnosti uzlu

Zobrazí detailní informace o uzlu nebo všech uzlech:
- Ohodnocení uzlu
- Stupně (d, d+, d-)
- Sousedé **se vzdálenostmi** (pro ohodnocené grafy)
- Předchůdci **se vzdálenostmi**
- Následníci **se vzdálenostmi**
- Incidentní hrany

**Příklad:**
```
Dostupné uzly: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

Zadejte název uzlu (nebo 'vse' pro všechny uzly): A

================================================================
UZEL: A
================================================================
Ohodnocení: bez ohodnocení

Stupně:
  Stupeň d(A): 2
  Vstupní d-(A): 0
  Výstupní d+(A): 2

Sousedé (2):
  - B (vzdálenost: 1.0)
  - D (vzdálenost: 1.0)

Následníci U+(A) (2):
  - B (vzdálenost: 1.0)
  - D (vzdálenost: 1.0)

Incidentní hrany (2):
  - A → B [h1]
  - A → D [h2]
```

**Pro všechny uzly:**
```
Zadejte název uzlu (nebo 'vse' pro všechny uzly): vse
```

### 3️⃣ Vlastnosti hrany

Zobrazí informace o konkrétní hraně:
- Koncové uzly
- Orientovaná/neorientovaná
- Směr (pro orientované)
- Váha
- Označení
- Je to smyčka?

**Příklad:**
```
Celkem hran: 14

Dostupné hrany:
  h1: A → B
  h2: A → D
  h3: B → C
  ...

Zadejte označení hrany (např. h1): h1

================================================================
HRANA: h1
================================================================

Koncové uzly: A, B
Typ: orientovaná
Směr: A → B
Váha: bez ohodnocení
Označení: h1
```

### 4️⃣ Matice sousednosti

Zobrazí matici sousednosti a umožňuje dotazování na konkrétní hodnoty **pomocí názvů uzlů**.

**Příklad:**
```
MATICE SOUSEDNOSTI
================================================================
Rozměry: 8 řádků × 8 sloupců
Řádky: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
Sloupce: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

       A    B    C    D    E    F    G    H
  A:   0    1    0    1    0    0    0    0
  B:   0    0    1    0    0    0    0    0
  C:   0    0    0    0    1    0    0    0
  ...

Chcete zjistit konkrétní hodnotu? (a/n): a

================================================================
DOTAZ NA HODNOTU - Matice sousednosti
================================================================

Dostupné řádky: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
Dostupné sloupce: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

Zadejte název řádku (nebo 'zpet' pro návrat): A
Zadejte název sloupce: B

✅ Matice sousednosti[A][B] = 1
```

### 5️⃣ N-tá mocnina matice

Vypočítá a zobrazí n-tou mocninu matice sousednosti.

**Interpretace:** A^n[i][j] = počet cest délky n z uzlu i do uzlu j

**Příklad:**
```
================================================================
MOCNINA MATICE SOUSEDNOSTI
================================================================

Zadejte mocninu (např. 2, 3, 4): 2

MATICE SOUSEDNOSTI^2
================================================================
Rozměry: 8 řádků × 8 sloupců
...

Interpretace: A^2[i][j] = počet cest délky 2 z uzlu i do uzlu j

Chcete zjistit konkrétní hodnotu? (a/n): a

Zadejte název řádku (nebo 'zpet' pro návrat): A
Zadejte název sloupce: C

✅ Matice sousednosti^2[A][C] = 1
```

### 6️⃣ Matice incidence

Zobrazí matici incidence s uzly jako řádky a hranami jako sloupce.

**Význam hodnot:**
- Neorientovaný graf:
  - 1 = uzel je incidentní s hranou
  - **2 = hrana je smyčka na uzlu**
- Orientovaný graf:
  - 1 = hrana vychází z uzlu
  - -1 = hrana vstupuje do uzlu
  - **2 = hrana je smyčka na uzlu**

**Příklad:**
```
MATICE INCIDENCE
================================================================
Rozměry: 8 řádků × 14 sloupců
Řádky: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
Sloupce: ['h1', 'h2', 'h3', ...]

      h1   h2   h3   h4   h5   h6   h7   h8   h9  h10  h11  h12  h13  h14
  A:   1    1    0    0    0    0    0    0    0    0    0    0    0    0
  B:  -1    0    1    0    0    0    0    0    0    0    0    0    0    0
  ...

Chcete zjistit konkrétní hodnotu? (a/n): a

Zadejte název řádku (nebo 'zpet' pro návrat): A
Zadejte název sloupce: h1

✅ Matice incidence[A][h1] = 1
```

### 7️⃣ Matice délek

Zobrazí matici nejkratších vzdáleností (Floyd-Warshall).

**Interpretace:** D[i][j] = nejkratší vzdálenost z uzlu i do uzlu j

**Příklad:**
```
MATICE DÉLEK (Floyd-Warshall)
================================================================
Rozměry: 8 řádků × 8 sloupců
...

       A    B    C    D    E    F    G    H
  A: 0.0  1.0  2.0  1.0  3.0  2.0  3.0  4.0
  B: 0.0  0.0  1.0  2.0  2.0  3.0  4.0  5.0
  ...

Interpretace: D[i][j] = nejkratší vzdálenost z uzlu i do uzlu j
              ∞ = uzel není dosažitelný

Chcete zjistit konkrétní hodnotu? (a/n): a

Zadejte název řádku (nebo 'zpet' pro návrat): A
Zadejte název sloupce: F

✅ Matice délek[A][F] = 2.0
```

### 8️⃣ Matice předchůdců

Zobrazí matici předchůdců pro rekonstrukci nejkratších cest.

**Interpretace:** P[i][j] = předchůdce uzlu j na nejkratší cestě z i do j

**Příklad:**
```
MATICE PŘEDCHŮDCŮ
================================================================
Rozměry: 8 řádků × 8 sloupců
...

Chcete zjistit konkrétní hodnotu? (a/n): a

Zadejte název řádku (nebo 'zpet' pro návrat): A
Zadejte název sloupce: F

✅ Matice předchůdců[A][F] = D
```

### 9️⃣ Načíst jiný graf

Umožňuje načíst jiný graf bez ukončení programu.

### 0️⃣ Ukončit program

Ukončí program.

## Klíčové vlastnosti

### ✅ Přístup k maticím pomocí názvů

**Všechny matice** podporují dotazování pomocí **názvů uzlů a hran**:

```
Zadejte název řádku: A
Zadejte název sloupce: B

✅ Matice sousednosti[A][B] = 1
```

**NE** pomocí číselných indexů! To je mnohem intuitivnější.

### ✅ Vzdálenosti u sousedů

Pro ohodnocené grafy se u sousedů, předchůdců a následníků zobrazuje také **vzdálenost**:

```
Sousedé (2):
  - B (vzdálenost: 1.0)
  - D (vzdálenost: 1.0)
```

### ✅ Smyčky v matici incidence

Smyčky se v matici incidence označují **hodnotou 2**:

```
  A:   2    0    0    ...  # Hrana h1 je smyčka na uzlu A
```

### ✅ Cache matic

Matice se cachuji pro rychlejší opakovaný přístup. Při načtení nového grafu se cache vyčistí.

### ✅ Intuitivní ovládání

- Dotaz na všechny uzly: zadejte `vse`
- Návrat z dotazu na matici: zadejte `zpet`
- Ukončení při načítání grafu: zadejte `q`

## Tip pro použití

1. Spusťte program: `./start.sh` (nebo `start.bat` na Windows)
2. Zadejte cestu k souboru s grafem, např. `data/grafy/01.tg`
3. Vyberte operaci z menu (1-9)
4. Postupujte podle pokynů
5. Po každé operaci stiskněte Enter pro návrat do menu

## Ukončení programu

Několik způsobů:
- Volba `0` v hlavním menu
- Ctrl+C kdykoliv
- `q` při načítání grafu

## Řešení problémů

**Program nejde spustit:**
```bash
# Ujistěte se, že je spustitelný
chmod +x start.sh

# Nebo spusťte přímo
python3 main.py
```

**Graf se nenačte:**
- Zkontrolujte cestu k souboru
- Soubor musí být v formátu .tg

**Matice se nezobrazuje správně:**
- Pro velké grafy může být matice příliš široká
- Zkuste zmenšit okno terminálu nebo použijte dotaz na konkrétní hodnoty

## Příklad session

```
$ ./start.sh

================================================================
🔍 INTERAKTIVNÍ ANALYZÁTOR GRAFŮ
================================================================

================================================================
NAČTENÍ GRAFU
================================================================

Zadejte cestu k souboru s grafem (nebo 'q' pro ukončení): data/grafy/01.tg

✅ Graf úspěšně načten!
   Soubor: data/grafy/01.tg
   Uzly: 8 - ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
   Hrany: 14

================================================================
HLAVNÍ MENU
================================================================
...
Vaše volba: 2

Dostupné uzly: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

Zadejte název uzlu (nebo 'vse' pro všechny uzly): A
...

Stiskněte Enter pro pokračování...

Vaše volba: 4

MATICE SOUSEDNOSTI
...

Vaše volba: 0

👋 Ukončuji program. Nashledanou!
```

## Související dokumentace

- [README.md](../README.md) - Hlavní README
- [NAMED_MATRICES.md](NAMED_MATRICES.md) - Dokumentace k NamedMatrix
- [POUZITI.md](POUZITI.md) - Podrobný návod k použití

