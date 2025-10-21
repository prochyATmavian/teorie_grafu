# Příklad: Vlastnosti uzlu

## Zobrazení předchůdců, následníků a sousedů

Program nyní zobrazuje pro každý uzel:

1. **Předchůdce U-(v)** - uzly, ze kterých vede hrana DO tohoto uzlu
2. **Následníky U+(v)** - uzly, do kterých vede hrana Z tohoto uzlu  
3. **Všechny sousedy U(v)** - všechny uzly spojené s tímto uzlem (předchůdci + následníci)

## Příklad výstupu

### Orientovaný graf

Pro orientovaný graf (např. `data/grafy/01.tg`):

```
======================================================================
UZEL: A
======================================================================
Ohodnocení: bez ohodnocení

Stupně:
  Stupeň d(A): 3
  Vstupní d-(A): 1
  Výstupní d+(A): 2

Předchůdci U-(A) (1):
  - E (vzdálenost: 3.0)

Následníci U+(A) (2):
  - B (vzdálenost: 1.0)
  - D (vzdálenost: 1.0)

Všichni sousedé U(A) (3):
  - B (vzdálenost: 1.0)
  - D (vzdálenost: 1.0)
  - E (vzdálenost: 3.0)

Incidentní hrany (3):
  - E → A [h14]
  - A → B [h1]
  - A → D [h2]
```

### Neorientovaný graf

Pro neorientovaný graf:

```
======================================================================
UZEL: A
======================================================================
Ohodnocení: bez ohodnocení

Stupně:
  Stupeň d(A): 2

Předchůdci U-(A) (0):
  (žádní)

Následníci U+(A) (0):
  (žádní)

Všichni sousedé U(A) (2):
  - B (vzdálenost: 1.0)
  - C (vzdálenost: 2.0)

Incidentní hrany (2):
  - A - B
  - A - C
```

**Poznámka:** Pro neorientované grafy jsou všichni sousedé v kategorii "Všichni sousedé U(v)", zatímco předchůdci a následníci jsou prázdní (protože v neorientovaném grafu neexistuje směr).

## Význam pojmů

### Orientovaný graf

- **Předchůdci U-(v)**: Uzly, ze kterých vede orientovaná hrana **DO** uzlu v
  - Příklad: Pokud máme hranu E → A, pak E je předchůdcem A
  
- **Následníci U+(v)**: Uzly, do kterých vede orientovaná hrana **Z** uzlu v
  - Příklad: Pokud máme hranu A → B, pak B je následníkem A

- **Všichni sousedé U(v)**: Všechny uzly spojené s uzlem v (předchůdci ∪ následníci)

### Neorientovaný graf

- **Všichni sousedé U(v)**: Všechny uzly spojené neorientovanou hranou s uzlem v
- **Předchůdci a následníci**: Neexistují (nemá smysl rozlišovat směr)

## Vzdálenosti

U každého souseda/předchůdce/následníka se zobrazuje **vzdálenost** (pokud je graf ohodnocený):

- Pro předchůdce: vzdálenost z předchůdce DO uzlu
- Pro následníky: vzdálenost z uzlu DO následníka
- Pro všechny sousedy: minimální vzdálenost mezi uzly

Příklad:
```
Následníci U+(A) (2):
  - B (vzdálenost: 1.0)    # Vzdálenost z A do B
  - D (vzdálenost: 1.0)    # Vzdálenost z A do D
```

## Jak zobrazit

V hlavním menu vyberte:
```
2) Vlastnosti uzlu (nebo všech uzlů)
```

Pak zadejte:
- Název konkrétního uzlu (např. `A`)
- Nebo `vse` pro zobrazení všech uzlů

## Srovnání: Předtím vs. Nyní

### Předtím
Zobrazovali se jen sousedé (a předchůdci/následníci jen pro orientované grafy).

### Nyní
Zobrazují se **vždy**:
- Předchůdci U-(v)
- Následníci U+(v)  
- Všichni sousedé U(v)
- **Se vzdálenostmi** pro ohodnocené grafy

Toto je užitečné zejména pro:
- Analýzu orientovaných grafů
- Pochopení struktury grafu
- Hledání nejkratších cest

