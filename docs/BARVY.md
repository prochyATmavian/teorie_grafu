# Barevný výstup programu

## Vlastnosti grafu

Program zobrazuje vlastnosti grafu s barevným kódováním:

### Barvy

- **Zelená** - vlastnost je splněna (ano)
- **Červená** - vlastnost není splněna (ne)

### Příklad výstupu

```
Vlastnosti:
  a) Ohodnocený: ano          (zelená)
  b) Orientovaný: ano         (zelená)
  c) Souvislý: ano (silně)    (zelená)
  d) Prostý: ano              (zelená)
  e) Jednoduchý (bez smyček): ano  (zelená)
  f) Rovinný: ano             (zelená)
  g) Konečný: ano             (zelená)
  h) Úplný: ne                (červená)
  i) Regulární: ne            (červená)
  j) Bipartitní: ne           (červená)
```

## Vlastnosti v češtině

Všechny vlastnosti jsou zobrazeny v češtině:

| Kód | Český název |
|-----|-------------|
| a) | Ohodnocený |
| b) | Orientovaný |
| c) | Souvislý |
| d) | Prostý |
| e) | Jednoduchý (bez smyček) |
| f) | Rovinný |
| g) | Konečný |
| h) | Úplný |
| i) | Regulární |
| j) | Bipartitní |

## Bez emotikonů

Program **nepoužívá emotikony**. Místo toho:
- Barvy pro vlastnosti grafu
- Čistý textový výstup

## Poznámky

- Barvy fungují na většině moderních terminálů (Linux, Mac, Windows Terminal)
- Pokud terminál nepodporuje barvy, zobrazí se ANSI escape sekvence (např. `[92m`)
- V tom případě stále vidíte text, jen bez barev

