# Forrásanyagok

Ebbe a mappába kerülnek a kísérlethez használt bemeneti forrásanyagok. Ezeket adjuk be minden AI eszköznek azonos formában, a `prompts.md` fájlban szereplő promptverziókkal kombinálva.

A forrásanyag lehet:

* PDF jegyzet vagy tanulmány,
* PDF-ből kivont szöveg,
* Markdown formátumú forrásszöveg,
* rövidebb mintaszöveg próbakísérlethez.

A cél az, hogy minden AI eszköz ugyanabból a bemenetből dolgozzon, így az eredmények összehasonlíthatók legyenek.

## Fájlnév-konvenció

A fájlnevek legyenek rövidek, ékezet nélküliek és könnyen hivatkozhatók.

```text
<rovidcim>.<kiterjesztes>
```

Példák:

```text
algel_bonyelm.pdf
digitalis_transzformacio.md
fenntarthato_fejlodes.md
kvantumszamitogepek.md
```

## Egy forrásszöveg fájl javasolt formátuma

Markdown forrásszöveg esetén az alábbi szerkezet használható:

```markdown
# [Forrásanyag rövid címe]

**Eredeti forrás:** [cím, szerző, év, URL ha van]  
**Típus:** [PDF-ből kivont szöveg / saját mintaszöveg / oktatási jegyzet]  
**Terjedelem:** [kb. oldalszám vagy szószám]

---

[IDE KERÜL A SZÖVEG]
```

PDF esetén elegendő a fájlt ebbe a mappába helyezni, majd a kísérlet dokumentációjában hivatkozni rá.

## Tartalom

| Fájl                               | Típus                | Leírás                                                                                                                          |
| ---------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `Algel_bonyelm_Friedl_Katalin.pdf` | PDF jegyzet          | Algoritmuselméleti kiegészítő jegyzet a bonyolultságelmélet alapjairól: P, NP, coNP, Karp-redukció, NP-nehézség és NP-teljesség |
| `sample_source_text.md`            | Markdown mintaszöveg | Rövid mintaforrásszöveg próbakísérlethez                                                                                        |

## Használat a kísérletben

A forrásanyagot minden AI eszköznek azonos módon kell beadni. A kísérlet során ugyanazt a PDF-et vagy forrásszöveget kell használni ChatGPT, Claude, Gemini és Google AI Studio esetén is.

A generált válaszokat nem ebbe a mappába, hanem az `outputs/` mappába kell menteni.

Az értékelések, pontszámok és következtetések helye a `results/` mappa.

## Kapcsolódó mappák

| Mappa               | Szerep                                       |
| ------------------- | -------------------------------------------- |
| `source_materials/` | Bemeneti forrásanyagok                       |
| `prompts.md`        | A forrásanyaghoz használt promptverziók      |
| `outputs/`          | AI eszközök által generált kimenetek         |
| `screenshots/`      | Képernyőképek, vizuális bizonyítékok         |
| `results/`          | Pontozás, összehasonlítás és következtetések |
