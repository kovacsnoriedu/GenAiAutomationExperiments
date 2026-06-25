# Kimenetek (Outputs)

Ebbe a mappába kerülnek az AI eszközök által generált nyers prezentációkimenetek.

A projekt célja annak vizsgálata, hogy különböző generatív AI eszközök hogyan tudnak egy hosszabb forrásanyagból, például PDF-ből vagy PDF-ből kivont szövegből prezentációvázlatot, slide-struktúrát vagy tényleges PowerPoint prezentációt készíteni.

Ez a mappa kizárólag az AI-k által létrehozott kimenetek tárolására szolgál. A részletes emberi értékelések, pontszámok és következtetések nem ide, hanem a `results/` mappába kerülnek.

## Mappastruktúra

```text
outputs/
  chatgpt/          ← ChatGPT által generált kimenetek
  claude/           ← Claude által generált kimenetek
  gemini/           ← Gemini által generált kimenetek
  google_ai_studio/ ← Google AI Studio által generált kimenetek
```

## Fájlnév-konvenció

```text
<forrásanyag_neve>_<prompt_sorszám>_<prompt_típus>.<kiterjesztés>
```

Példák Markdown kimenetekre:

```text
algel_bonyelm_1_baseline.md
algel_bonyelm_2_strukturalt.md
algel_bonyelm_3_forrashuseg.md
algel_bonyelm_4_design.md
algel_bonyelm_5_slide_ready.md
algel_bonyelm_6_javito.md
algel_bonyelm_7_ertekelo.md
```

Példák tényleges PowerPoint kimenetekre:

```text
algel_bonyelm_1_baseline_ppt_generation.pptx
algel_bonyelm_2_strukturalt_ppt_generation.pptx
algel_bonyelm_4_design_ppt_generation.pptx
```

Példák eszköz szerinti elhelyezésre:

```text
outputs/chatgpt/algel_bonyelm_1_baseline.md
outputs/claude/algel_bonyelm_1_baseline.md
outputs/gemini/algel_bonyelm_1_baseline.md
outputs/google_ai_studio/algel_bonyelm_1_baseline.md
```

## Prompttípusok

A projektben használt promptverziók a `prompts.md` fájlban találhatók. A fájlnévben szereplő prompttípus mindig ezek egyikére utaljon.

Javasolt prompttípusok:

| Azonosító        | Jelentés                                                          |
| ---------------- | ----------------------------------------------------------------- |
| `1_baseline`     | Alap prezentációvázlat generálása minimális instrukcióval         |
| `2_strukturalt`  | Részletesen strukturált, slide-onként szabályozott kimenet        |
| `3_forrashuseg`  | Forráshűségre fókuszáló prompt                                    |
| `4_design`       | Vizuális elemekre, ábrákra és slide-elrendezésre fókuszáló prompt |
| `5_slide_ready`  | Kevés slide-szöveget és több előadói jegyzetet kérő prompt        |
| `6_javito`       | Egy meglévő vázlat javítására szolgáló prompt                     |
| `7_ertekelo`     | Egy meglévő kimenet értékelésére szolgáló prompt                  |
| `ppt_generation` | Tényleges PowerPoint fájl generálását kérő prompt                 |

## Egy Markdown kimeneti fájl javasolt fejléce

Minden Markdown kimenet tetejére érdemes beilleszteni az alábbi fejlécet, mielőtt az AI válasza bekerül a fájlba.

```markdown
# Kimenet – [Eszköz neve]

- **Forrásanyag:** [forrásanyag fájlneve]
- **Téma:** [a prezentáció témája]
- **Prompt típus:** [pl. 1_baseline / 2_strukturalt / 3_forrashuseg]
- **Dátum:** [ÉÉÉÉ-HH-NN]
- **Modell:** [pl. GPT-4o, Claude Sonnet, Gemini Pro]
- **Kimenet típusa:** [prezentációvázlat / ppt_generation / javított változat / értékelés]
- **Rövid technikai megjegyzés:** [opcionális, pl. generált-e fájlt, volt-e hiba, hiányzott-e valami]

---

## Tényleges PowerPoint fájlok kezelése

Ha egy AI eszköz tényleges `.pptx` fájlt generál, akkor azt ugyanabba az eszközmappába kell menteni, ahová az adott prompt Markdown kimenete is kerül.

Példa:

```text
outputs/chatgpt/algel_bonyelm_1_baseline.md
outputs/chatgpt/algel_bonyelm_1_baseline_ppt_generation.pptx
```

Ha a PowerPoint generálás külön prompttal történt, akkor annak a promptnak a szövegét vagy eredményét is érdemes Markdown fájlban menteni.

Példa:

```text
outputs/chatgpt/algel_bonyelm_1_baseline_ppt_generation.md
```

## Screenshotok és vizuális eredmények

Ha az AI eszköz vizuális előnézetet, slide-képet, diagramot vagy képernyőn megjelenő eredményt ad, akkor a képernyőképek ne ebbe a mappába, hanem a `screenshots/` mappába kerüljenek.

A screenshot fájlneve lehetőleg utaljon az eszközre, a forrásanyagra és a prompttípusra.

Példa:

```text
screenshots/chatgpt_algel_bonyelm_1_baseline_preview.png
```

## Kapcsolódó mappák

| Mappa               | Szerep                                                        |
| ------------------- | ------------------------------------------------------------- |
| `source_materials/` | Bemeneti PDF-ek, forrásszövegek és tesztanyagok               |
| `prompts.md`        | A kipróbált promptverziók leírása                             |
| `outputs/`          | AI-eszközök által generált nyers kimenetek                    |
| `screenshots/`      | Képernyőképek és vizuális bizonyítékok                        |
| `results/`          | Pontszámok, értékelések, összehasonlítások és következtetések |

## Összefoglalás

Az `outputs/` mappa célja, hogy átláthatóan és reprodukálható módon tárolja a különböző AI-eszközök által generált prezentációkimeneteket.

A kísérlet során minden eszköz ugyanazt a forrásanyagot és azonos promptverziókat kap. Az így kapott válaszok összehasonlíthatók lesznek tartalmi pontosság, forráshűség, struktúra, design, szövegmennyiség és használhatóság alapján.

Az AI-kimenetek ide kerülnek, az emberi értékelés és következtetés pedig a `results/` mappába.
