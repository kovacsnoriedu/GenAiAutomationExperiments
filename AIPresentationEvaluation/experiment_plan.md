# Kísérleti terv – MI-alapú prezentációgenerálás összehasonlítása

Ez a dokumentum lépésről lépésre leírja, hogyan kell elvégezni a kísérletet. A cél: ugyanazt a forrásanyagot ugyanazokkal a promptverziókkal adni be minden tesztelt AI eszköznek, majd az eredményeket egységes szempontrendszer alapján értékelni.

---

## Áttekintés

| Lépés | Feladat | Kimenet |
|---|---|---|
| 1 | Forrásanyag előkészítése | `source_materials/<fájlnév>.md` |
| 2 | Eszközök és promptok kiválasztása | – |
| 3 | Kísérletek futtatása | `outputs/<eszköz>/<fájlnév>.md` |
| 4 | Screenshotok mentése | `screenshots/<fájlnév>.png` |
| 5 | Értékelés pontozása | `results/results.csv` |
| 6 | Összefoglaló készítése | `results/evaluation_summary.md` |

---

## 1. lépés – Forrásanyag előkészítése

### Ha PDF-ből dolgozol

1. Nyisd meg a PDF-et (Adobe Reader, böngésző, stb.)
2. Jelöld ki és másold ki a szöveget, vagy használj PDF-szövegkinyerő eszközt
3. Hozz létre egy új fájlt a `source_materials/` mappában:
   - Fájlnév: `<rovidcim>.md` (pl. `digitalis_transzformacio.md`)
   - A fájl elején tüntesd fel a forrás adatait (cím, szerző, év)
4. Illeszd be a szöveget a fájlba

### Ha közvetlenül szöveget adsz meg

1. Készítsd el a szöveget (max. ~2000 szó ajánlott az LLM kontextusablak szempontjából)
2. Mentsd `source_materials/<rovidcim>.md` fájlba

> **Mintaforrásszöveg:** [`source_materials/sample_source_text.md`](source_materials/sample_source_text.md) – ezt rögtön be lehet adni próbakísérletként.

---

## 2. lépés – Eszközök és promptok kiválasztása

### Tesztelt eszközök

| Eszköz | URL | Megjegyzés |
|---|---|---|
| ChatGPT | https://chat.openai.com | GPT-4o modell ajánlott |
| Claude | https://claude.ai | Claude 3.5 Sonnet vagy újabb |
| Gemini | https://gemini.google.com | Gemini 1.5 Pro vagy újabb |
| Google AI Studio | https://aistudio.google.com | Közvetlen Gemini API hozzáférés |

### Javasolt kísérletmátrix

Egy alapos összehasonlításhoz legalább a következő kombinációkat érdemes lefuttatni:

| Forrásanyag | Prompt típus | ChatGPT | Claude | Gemini | Google AI Studio |
|---|---|---|---|---|---|
| sample_source_text | `1_baseline` | ☐ | ☐ | ☐ | ☐ |
| sample_source_text | `2_strukturalt` | ☐ | ☐ | ☐ | ☐ |
| sample_source_text | `3_forrashuseg` | ☐ | ☐ | ☐ | ☐ |
| sample_source_text | `5_slide_ready` | ☐ | ☐ | ☐ | ☐ |

> A táblázat másolható és kézzel kitölthető – cseréld a ☐ jeleket ✓-ra elvégzés után.

---

## 3. lépés – Kísérletek futtatása

### Egy kísérlet elvégzése

1. Nyisd meg a kiválasztott AI eszközt
2. Nyisd meg a `prompts.md` fájlban a megfelelő promptverziót
3. Illeszd be a forrásszöveget a `[FORRÁSSZÖVEG]` helyére
4. Add be a promptot az AI eszköznek
5. Várd meg a teljes választ
6. Másold ki az AI válaszát

### Kimenet mentése

- Hozz létre egy új `.md` fájlt az `outputs/<eszköz_neve>/` mappában
- **Fájlnév-konvenció:** `<forrásanyag_neve>_<prompt_típus>.md`
  - Példa: `sample_source_text_1_baseline.md`
  - Példa: `digitalis_transzformacio_2_strukturalt.md`
- A fájl elejére írj egy rövid fejlécet:

```markdown
# Kimenet – [Eszköz neve]

- **Forrásanyag:** [forrásanyag fájlneve]
- **Prompt típus:** [pl. 2_strukturalt]
- **Dátum:** [ÉÉÉÉ-HH-NN]
- **Modell:** [pl. GPT-4o, Claude 3.5 Sonnet]

---

[IDE MÁSOLD BE AZ AI VÁLASZÁT]
```

---

## 4. lépés – Screenshotok mentése

Ha az AI valamilyen vizuálisan formázott vagy interaktív eredményt ad (pl. Google AI Studio canvas, Gemini dokumentum nézet), készíts képernyőképet.

- **Fájlnév-konvenció:** `<eszköz>_<forrásanyag>_<prompt_típus>.png`
  - Példa: `gemini_sample_source_text_4_design.png`
- Mentés helye: `screenshots/` mappa

---

## 5. lépés – Értékelés pontozása

Minden egyes kimenet elkészülte után futtasd a pontozó segédprogramot:

```bash
python ppt_evaluation_helper.py --csv results/results.csv
```

A program bekéri:
- AI eszköz neve
- Forrásanyag neve
- Prompt típus
- Slide-ok száma a generált vázlatban
- Pontszámok 1–5 skálán (10 szempont szerint – lásd `evaluation_criteria.md`)
- Szabad megjegyzés

---

## 6. lépés – Összefoglaló készítése

Miután minden kísérleti kombinációhoz rögzítetted az értékeléseket:

```bash
python ppt_evaluation_helper.py --summary --csv results/results.csv
```

Az eredmények alapján töltsd ki a `results/evaluation_summary.md` sablont.

---

## Ajánlott kísérleti sorrend kezdőknek

Ha most futtatsz először kísérletet, javasolt sorrend:

1. Töltsd be a `source_materials/sample_source_text.md` tartalmát
2. Próbáld ki a `1_baseline` promptot **egy** eszközön (pl. ChatGPT)
3. Mentsd el a kimenetet, pontozd le, nézd meg az eredményt
4. Ha ez megvan, futtasd végig az összes eszközön ugyanezt a promptot
5. Ezután térj rá a többi promptverzióra

---

## Megjegyzések a reprodukálhatósághoz

- Mindig jegyezd fel a modell verziószámát (ha elérhető)
- Azonos napon futtasd ugyanazon forrásanyag összes kísérletét, ha összehasonlítható eredményt szeretnél
- Ha az AI eszköz beállítható hőmérséklet (temperature) paraméterrel rendelkezik, rögzítsd annak értékét is
- Ha egy eszköz valamilyen okból visszautasítja a promptot vagy részleges választ ad, ezt is rögzítsd a megjegyzés mezőben
