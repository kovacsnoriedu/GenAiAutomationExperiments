# MI-alapú prezentációgenerálás – Kísérleti keretrendszer

Generatív AI eszközök összehasonlítása PDF- vagy forrásanyag-alapú prezentációgenerálás szempontjából.

## Rövid leírás

Ez a projekt egy egyszerű, reprodukálható kísérleti keretrendszer, amely azt vizsgálja, hogy különböző LLM-alapú AI eszközök hogyan tudnak hosszabb forrásanyagból prezentációvázlatot vagy tényleges PowerPoint prezentációt készíteni.

A kísérlet során ugyanazt a forrásanyagot adjuk be több AI eszköznek, azonos vagy összehasonlítható promptokkal, majd az eredményeket egységes szempontrendszer alapján értékeljük.

Tesztelt eszközök például:

* ChatGPT
* Claude
* Gemini
* Google AI Studio

A projekt nem használ külső AI API-t. Az AI-eszközök használata kézzel történik, az értékelés pedig emberi pontozáson alapul.

---

## Probléma

A generatív AI eszközök egyre gyakrabban segítenek prezentációk készítésében, de nem egyértelmű, hogy:

* melyik eszköz ad forráshűbb tartalmat,
* melyik készít jobb slide-struktúrát,
* melyik tud valóban használható vizuális javaslatokat adni,
* mennyit számít a prompt részletessége,
* mennyi emberi utómunka marad a generált eredmény után.

Ez a projekt ezekre a kérdésekre ad összehasonlítható, dokumentált kísérleti választ.

---

## Megoldás

A projekt egy egységes munkafolyamatot ad:

1. Forrásanyag kiválasztása vagy előkészítése.
2. Promptverzió kiválasztása a `prompts.md` fájlból.
3. Ugyanazon prompt kipróbálása több AI eszközben.
4. A generált kimenetek mentése az `outputs/` mappába.
5. Esetleges screenshotok mentése a `screenshots/` mappába.
6. A kimenetek pontozása a `ppt_evaluation_helper.py` segédprogrammal.
7. Következtetések rögzítése a `results/evaluation_summary.md` fájlban.

---

## Projektstruktúra

```text
AIPresentationEvaluation/
  README.md
  prompts.md
  experiment_plan.md
  evaluation_criteria.md
  ppt_evaluation_helper.py
  requirements.txt

  source_materials/
    README.md
    sample_source_text.md
    Algel_bonyelm_Friedl_Katalin.pdf

  outputs/
    README.md
    chatgpt/
    claude/
    gemini/
    google_ai_studio/

  screenshots/
    README.md

  results/
    results_template.csv
    results.csv
    evaluation_summary.md
```

---

## Fő fájlok szerepe

| Fájl / mappa               | Szerep                                                              |
| -------------------------- | ------------------------------------------------------------------- |
| `prompts.md`               | A kipróbált promptverziók és konkrét kísérleti promptok gyűjteménye |
| `experiment_plan.md`       | Lépésről lépésre leírja a kísérlet menetét                          |
| `evaluation_criteria.md`   | A 10 pontos értékelési szempontrendszer                             |
| `ppt_evaluation_helper.py` | Parancssoros segédprogram az értékelések CSV-be mentéséhez          |
| `source_materials/`        | Bemeneti PDF-ek és forrásszövegek                                   |
| `outputs/`                 | AI-eszközök által generált nyers kimenetek                          |
| `screenshots/`             | Képernyőképek és vizuális bizonyítékok                              |
| `results/`                 | Pontszámok, összefoglalók és következtetések                        |

---

## Kísérleti munkafolyamat

A részletes leírás az `experiment_plan.md` fájlban található.

Röviden:

```text
Forrásanyag kiválasztása
        ↓
Prompt kiválasztása
        ↓
Prompt beadása ChatGPT / Claude / Gemini / Google AI Studio eszközöknek
        ↓
AI-kimenetek mentése az outputs/ mappába
        ↓
Pontozás a ppt_evaluation_helper.py segítségével
        ↓
Eredmények összegzése a results/ mappában
```

---

## Promptstratégiák

A promptok teljes listája a `prompts.md` fájlban található.

A fő prompttípusok:

| Azonosító        | Cél                                                        |
| ---------------- | ---------------------------------------------------------- |
| `1_baseline`     | Alap prezentációvázlat generálása                          |
| `2_strukturalt`  | Részletesen szabályozott slide-struktúra                   |
| `3_forrashuseg`  | Csak a forrásanyagra támaszkodó kimenet                    |
| `4_design`       | Vizuális elemekre és slide-elrendezésre fókuszáló prompt   |
| `5_slide_ready`  | Kevés slide-szöveget és több előadói jegyzetet kérő prompt |
| `6_javito`       | Meglévő vázlat javítása                                    |
| `7_ertekelo`     | AI-kimenet értékelése                                      |
| `ppt_generation` | Tényleges PowerPoint fájl generálása                       |

---

## Értékelési szempontok

A részletes pontozási útmutató az `evaluation_criteria.md` fájlban található.

A kimeneteket 1–5 skálán értékeljük az alábbi szempontok szerint:

1. Tartalmi pontosság
2. Forráshűség
3. Struktúra
4. Logikai ív / narratíva
5. Szövegmennyiség
6. Design / vizuális javaslatok
7. Képek, diagramok, vizuális elemek
8. Előadói jegyzetek
9. Emberi utómunka szükségessége
10. Összesített használhatóság

Ha egy szempont az adott kimenetnél nem értelmezhető, akkor `0` adható meg N/A értékként.

---

## Kimenetek dokumentálása

Az AI által generált válaszok az `outputs/` mappába kerülnek, eszközönként külön almappába.

Példa:

```text
outputs/chatgpt/algel_bonyelm_1_baseline.md
outputs/claude/algel_bonyelm_1_baseline.md
outputs/gemini/algel_bonyelm_1_baseline.md
outputs/google_ai_studio/algel_bonyelm_1_baseline.md
```

Ha tényleges PowerPoint fájl is készül:

```text
outputs/chatgpt/algel_bonyelm_1_baseline_ppt_generation.pptx
```

A részletes emberi értékelések és következtetések nem az `outputs/` mappába, hanem a `results/` mappába kerülnek.

---

## Használat

### Követelmények

* Python 3.8 vagy újabb
* Nincs külső Python-függőség

Telepítés nem szükséges:

```bash
cd AIPresentationEvaluation
```

### Új értékelés rögzítése

```bash
python ppt_evaluation_helper.py --csv results/results.csv
```

A program bekéri:

* AI eszköz neve,
* forrásanyag neve,
* prompt típusa,
* slide-ok száma,
* pontszámok a 10 értékelési szempont szerint,
* rövid megjegyzés.

### Eredmények listázása

```bash
python ppt_evaluation_helper.py --list --csv results/results.csv
```

### Összefoglaló generálása

```bash
python ppt_evaluation_helper.py --summary --csv results/results.csv
```

### Összefoglaló mentése Markdown fájlba

```bash
python ppt_evaluation_helper.py --export results/evaluation_summary_generated.md --csv results/results.csv
```

---

## Jelenlegi kísérleti példa

A projekt egyik konkrét tesztesete egy algoritmuselméleti PDF alapján történő prezentációgenerálás.

Forrásanyag:

```text
source_materials/Algel_bonyelm_Friedl_Katalin.pdf
```

Feladat:

> 20 slide-os, oktatási célú prezentáció készítése a bonyolultságelmélet alapjairól: P, NP, coNP, Karp-redukció, NP-nehézség és NP-teljesség.

A cél annak vizsgálata, hogy az AI-eszközök mennyire tudnak egy formális, definíciókkal és jelölésekkel teli egyetemi anyagból tanulható és vizuálisan is érthető prezentációt készíteni.

## Eredmények röviden

A kísérlet eredményei alapján a vizsgált modellek eltérő erősségeket mutattak. A konkrét tesztkörnyezetben a Claude Sonnet 4.6 adta a legjobb összesített eredményt: jól strukturált, vizuálisan igényes és kisebb kézi javítás után előadásra is alkalmas prezentációalapot készített.

A Gemini 3.5 Flash követhető és szakmailag értelmezhető anyagot adott, különösen hasznos meglévő ábrahivatkozásokkal, de nem tartotta teljesen a kért fájlformátumot. A GPT-5.5 használható tartalmi alapot készített, de több vizuális és szerkezeti finomítást igényelt. A Google AI Studio / Gemma inkább kódalapú kerülőmegoldást adott, amely javítás után működött, de közvetlen prezentációgenerálásként kevésbé volt hatékony.

A részletes pontszámok, kvalitatív megfigyelések és végső következtetések a `results/evaluation_summary.md` fájlban találhatók.


---

## Technikai részletek

* **Programozási nyelv:** Python 3
* **Külső függőségek:** nincs
* **Adattárolás:** CSV
* **Fő kimeneti fájl:** `results/results.csv`
* **Kompatibilitás:** Windows, macOS, Linux

---

## Licensz

Ez a projekt oktatási és kutatási célra készült.
