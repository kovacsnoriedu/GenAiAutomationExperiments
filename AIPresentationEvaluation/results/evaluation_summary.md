# Értékelési összefoglaló – MI-alapú prezentációgenerálás

Ez a fájl a PDF-alapú prezentációgenerálási kísérlet kvalitatív összefoglalására szolgál.

A számszerű értékelések a `results/results.csv` fájlba kerülnek, amelyet a `ppt_evaluation_helper.py` segédprogram hoz létre vagy bővít.
Ez a dokumentum nem a nyers AI-kimenetek tárolására szolgál, hanem az eredmények összehasonlítására, értelmezésére és a végső következtetések rögzítésére.

---

## 1. Kísérlet célja

A kísérlet célja annak vizsgálata, hogy különböző generatív AI eszközök mennyire jól tudnak egy egyetemi algoritmuselméleti PDF alapján oktatási célú prezentációt készíteni.

A vizsgált feladat:

> 20 slide-os, tanulható és vizsgára készüléshez is használható prezentáció készítése a bonyolultságelmélet alapjairól.

A prezentációnak érthetően be kell mutatnia a fő fogalmakat, ki kell emelnie a fontos definíciókat és jelöléseket, valamint ábraötletekkel kell segítenie a nehezebb részek vizuális magyarázatát.

---

## 2. Kísérlet adatai

| Mező                         | Érték                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------- |
| **Kísérlet dátuma**          | 2026-06-25                                                                                     |
| **Forrásanyag**              | `source_materials/Algel_bonyelm_Friedl_Katalin.pdf`                                            |
| **Forrásanyag típusa**       | Egyetemi algoritmuselmélet jegyzet                                                             |
| **Téma**                     | A bonyolultságelmélet alapjai: P, NP, coNP, Karp-redukció, NP-nehézség és NP-teljesség         |
| **Célközönség**              | Algoritmuselméletet tanuló egyetemi hallgatók                                                  |
| **Elvárt kimenet**           | 20 slide-os oktatási prezentációvázlat, illetve ahol lehetséges, tényleges `.pptx` prezentáció |
| **Tesztelt eszközök**        | ChatGPT, Claude, Gemini, Google AI Studio                                                      |
| **Pontozás helye**           | `results/results.csv`                                                                          |
| **Nyers AI-kimenetek helye** | `outputs/`                                                                                     |
| **Screenshotok helye**       | `screenshots/`                                                                                 |

---

## 3. Vizsgált promptverziók

| Prompt azonosító            | Cél                                                                            |
| --------------------------- | ------------------------------------------------------------------------------ |
| `1_baseline`                | Alap prezentációvázlat generálása a PDF alapján                                |
| `1_baseline_ppt_generation` | Tényleges PowerPoint prezentáció generálása az alap vázlatból                  |
| `2_strukturalt`             | Részletes, slide-onként szabályozott prezentációvázlat készítése               |
| `3_forrashuseg`             | Forráshűségre fókuszáló prompt, külső példák és kitalált állítások kerülésével |
| `4_design`                  | Vizuális elemekre, ábrákra, diagramokra és slide-elrendezésre fókuszáló prompt |
| `5_slide_ready`             | Kevés slide-szöveget, több előadói jegyzetet kérő prompt                       |
| `6_javito`                  | Egy meglévő vázlat javítása rövidebb, tisztább, vizuálisabb formára            |
| `7_ertekelo`                | Egy meglévő AI-kimenet értékelése megadott szempontok szerint                  |

---

## 4. Mentett kimenetek

A kísérlet során minden AI-választ az adott eszköz saját `outputs/` almappájába kell menteni.

| Eszköz           | Mappa                       | Példafájl                     |
| ---------------- | --------------------------- | ----------------------------- |
| ChatGPT          | `outputs/chatgpt/`          | `algel_bonyelm_1_baseline.md` |
| Claude           | `outputs/claude/`           | `algel_bonyelm_1_baseline.md` |
| Gemini           | `outputs/gemini/`           | `algel_bonyelm_1_baseline.md` |
| Google AI Studio | `outputs/google_ai_studio/` | `algel_bonyelm_1_baseline.md` |

Ha tényleges PowerPoint fájl is készül, akkor azt ugyanabba az eszközmappába kell menteni.

Példa:

```text
outputs/chatgpt/algel_bonyelm_1_baseline_ppt_generation.pptx
```

---

## 5. Értékelési szempontok

A kimenetek értékelése 1–5 skálán történik.
Ha egy szempont az adott kimenetnél nem értelmezhető, akkor `0` adható meg, amely N/A értékként kezelhető.

| Szempont                          | Mit vizsgál?                                                                           |
| --------------------------------- | -------------------------------------------------------------------------------------- |
| **Tartalmi pontosság**            | Helyesen magyarázza-e a PDF-ben szereplő fogalmakat, definíciókat és összefüggéseket?  |
| **Forráshűség**                   | Csak a forrásanyagból dolgozik-e, vagy hoz be külső, nem kért példákat és állításokat? |
| **Struktúra**                     | Logikusan épül-e fel a 20 slide-os prezentáció?                                        |
| **Logikai ív / narratíva**        | Van-e érthető tanulási út: bevezetés, fogalmak, példák, redukciók, összegzés?          |
| **Szövegmennyiség**               | Slide-kompatibilis-e a szöveg, vagy túl hosszú és zsúfolt?                             |
| **Design / vizuális terv**        | Ad-e használható slide-elrendezési, kiemelési vagy designjavaslatokat?                 |
| **Ábra- és diagramötletek**       | Segíti-e vizuálisan a nehéz fogalmak megértését?                                       |
| **Előadói jegyzetek**             | Ad-e olyan magyarázatot, amelyet szóban el lehet mondani a slide-ok mellett?           |
| **Emberi utómunka szükségessége** | Mennyi javítás kellene ahhoz, hogy oktatásban ténylegesen használható legyen?          |
| **Összesített használhatóság**    | Mennyire lenne alkalmas a kimenet egy valódi prezentáció alapjának?                    |

---

## 6. Összesített pontszámok

A részletes pontszámok a `results/results.csv` fájlban találhatók.
Az alábbi táblázat a kvalitatív értékelés rövid összefoglalója. A pontszámok 1–5 skálán értendők, ahol az 5 jelenti a legjobb teljesítményt. Az `0` érték N/A esetként használható, ha egy szempont az adott kimenetnél nem értelmezhető.

| AI eszköz                      | Prompt                      | Tartalmi pontosság | Forráshűség | Struktúra | Narratíva | Szöveg | Design | Vizuális elemek | Előadói jegyzetek | Utómunka | Használhatóság | Átlag |
| ------------------------------ | --------------------------- | -----------------: | ----------: | --------: | --------: | -----: | -----: | --------------: | ----------------: | -------: | -------------: | ----: |
| GPT-5.5                        | `1_baseline_ppt_generation` |                  3 |           4 |         4 |         3 |      4 |      3 |               4 |                 3 |        3 |              4 |   3.5 |
| Sonnet 4.6                     | `1_baseline_ppt_generation` |                  5 |           5 |         5 |         5 |      4 |      4 |               4 |                 4 |        4 |              4 |   4.4 |
| Gemini 3.5 Flash               | `1_baseline_ppt_generation` |                  4 |           3 |         4 |         4 |      4 |      3 |               0 |                 3 |        4 |              4 |  3.67 |
| Google AI Studio / Gemma 4 26B | `1_baseline_ppt_generation` |                  3 |           3 |         3 |         4 |      3 |      2 |               1 |                 0 |        2 |              2 |  2.56 |

Megjegyzés: A pontszámok a konkrét kísérleti környezetben elérhető modellekre és felületekre vonatkoznak. Nem általános, minden modellre érvényes rangsort jelentenek.

---

## 7. Legjobb teljesítmény szempontonként

| Szempont                    | Legjobb eszköz            | Legjobb prompt              | Rövid indoklás                                                                                                          |
| --------------------------- | ------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Tartalmi pontosság          | ChatGPT / Claude / Gemini | `1_baseline_ppt_generation` | Mindhárom eszköz alapvetően helyesen dolgozta fel a fő algoritmuselméleti fogalmakat.                                   |
| Forráshűség                 | ChatGPT                   | `1_baseline_ppt_generation` | A ChatGPT jól követte a PDF-ben szereplő fő definíciókat és példákat.                                                   |
| Struktúra                   | ChatGPT / Claude          | `1_baseline_ppt_generation` | Mindkettő jól felépített, 20 slide-os tanulási ívet adott.                                                              |
| Logikai ív / narratíva      | Claude                    | `1_baseline_ppt_generation` | A Claude különösen jól vezette végig a hallgatót a fogalmakon, definíciókon és példákon.                                |
| Szövegmennyiség             | ChatGPT / Claude / Gemini | `1_baseline_ppt_generation` | A slide-ok többsége nem volt túlzsúfolt, bár minden kimenet igényelt volna kisebb szerkesztést.                         |
| Design / vizuális terv      | Claude                    | `1_baseline_ppt_generation` | A sötét kiemelő slide-ok és világos magyarázó slide-ok váltakozása vizuálisan erős eredményt adott.                     |
| Ábra- és diagramötletek     | Claude / Gemini           | `1_baseline_ppt_generation` | A Claude szemléletes saját ábrákat használt, a Gemini pedig több meglévő, szakmailag releváns ábrára hivatkozott.       |
| Előadói jegyzetek           | ChatGPT / Claude / Gemma  | `1_baseline_ppt_generation` | Több eszköz is adott használható magyarázó szöveget a slide-ok mellé.                                                   |
| Legkevesebb emberi utómunka | Claude                    | `1_baseline_ppt_generation` | A Claude eredménye igényelt ugyan ábraigazítást, de összességében a legközelebb állt egy előadásra kész prezentációhoz. |
| Összesített használhatóság  | Claude                    | `1_baseline_ppt_generation` | Ebben a konkrét kísérletben a Claude adta a legjobb egyensúlyt tartalom, vizuális megjelenés és használhatóság között.  |

---

## 8. Eszközönkénti kvalitatív megfigyelések

### ChatGPT

| Szempont                         | Megfigyelés                                                                                                                         |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Erősségek**                    | Jól strukturált, logikusan felépített prezentációvázlatot készített. A fő fogalmakat, definíciókat és jelöléseket jól rendszerezte. |
| **Gyengeségek**                  | A vizuális megvalósítás kevésbé volt erős, több kézi ábra- és designmunka szükséges.                                                |
| **Tipikus hiba**                 | Inkább tanulási vázlatként működött jól, kevésbé látványos, kész prezentációként.                                                   |
| **Forráshűség**                  | Jó forráshűséget mutatott, a PDF fő tartalmaira támaszkodott.                                                                       |
| **Vizuális javaslatok minősége** | Hasznos ábraötleteket adott, de ezek tényleges kivitelezése még emberi munkát igényel.                                              |
| **Használhatóság**               | Tanulási célra nagyon jó alap, előadásra kisebb vizuális fejlesztés után használható.                                               |

### Claude

| Szempont                         | Megfigyelés                                                                                                                       |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Erősségek**                    | Nagyon igényes és jól strukturált prezentációt készített. Jól emelte ki a fontos részeket, és erős vizuális kontrasztot használt. |
| **Gyengeségek**                  | Néhány ábra vagy szövegdoboz elcsúszott, összecsúszott vagy kilógott a diáról.                                                    |
| **Tipikus hiba**                 | A vizuális elemek néhol technikai igazítást igényeltek.                                                                           |
| **Forráshűség**                  | Alapvetően jól követte a témát és a fő fogalmakat.                                                                                |
| **Vizuális javaslatok minősége** | Kiemelkedő volt: a sötét hátterű kiemelő slide-ok és a fehér magyarázó slide-ok váltakozása jól segítette a figyelemvezetést.     |
| **Használhatóság**               | Kisebb kézi finomítással tanulásra és előadásra is alkalmas prezentáció készíthető belőle.                                        |

### Gemini

| Szempont                         | Megfigyelés                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Erősségek**                    | Jól követhető, szakmailag értelmezhető prezentációt készített. Pozitívum, hogy több helyen már meglévő, témába illő ábrákra hivatkozott.                     |
| **Gyengeségek**                  | Nem tartotta teljesen a kért fájlformátumot: a Markdown-formátumot nem követte megfelelően, és PowerPoint helyett PDF formában készítette el a prezentációt. |
| **Tipikus hiba**                 | A saját generálású ábrák több helyen elcsúsztak, túl kicsik vagy túl sűrűk lettek. Egyes vizuális elemek ismétlődtek.                                        |
| **Forráshűség**                  | A meglévő ábrákra való hivatkozás szakmailag pontosabb vizuális elemekhez vezetett.                                                                          |
| **Vizuális javaslatok minősége** | Színvilágban és ábrahivatkozásokban erős volt, de a saját ábrái több helyen javítást igényeltek.                                                             |
| **Használhatóság**               | Jó minőségű, követhető alapot adott, de formátumátalakítás és vizuális javítás szükséges.                                                                    |

### Google AI Studio / Gemma

| Szempont                         | Megfigyelés                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erősségek**                    | Technikailag érdekes megoldást adott: Python-kódot generált a prezentáció létrehozására. A kód szándéka szerint 20 slide-ot és előadói jegyzeteket készített volna. |
| **Gyengeségek**                  | Nem adott közvetlenül letölthető `.pptx` fájlt. A generált kódban hiba volt, ezért kézi javításra és külön futtatásra volt szükség.                                 |
| **Tipikus hiba**                 | A válasz először közvetlen fájlgenerálást sugallt, majd kiderült, hogy a felületen nincs ilyen fájlküldési lehetőség.                                               |
| **Forráshűség**                  | A tartalom főbb pontjai követhetők voltak, de a szakmai mélység és ellenőrizhetőség gyengébb volt, mint a többi eszköznél.                                          |
| **Vizuális javaslatok minősége** | A vizuális elemek inkább ígéretként jelentek meg, a létrejött PPT teljesen fehér hátterű és vizuálisan egyszerű volt.                                               |
| **Használhatóság**               | Javítás után létrejött egy 20 slide-os, a lényeget tartalmazó és viszonylag követhető prezentáció, de jelentős kézi utómunkát igényelt.                             |

---

## 9. Promptverziók szerinti megfigyelések

### `1_baseline`

Ebben a körben az AI-eszközök viszonylag kevés részletes instrukciót kaptak. A cél annak vizsgálata volt, hogy alapértelmezett módon mennyire képesek értelmes, tanulható prezentációvázlatot készíteni a PDF alapján.

**Megfigyelések:**

* A ChatGPT jól strukturált és tanulható vázlatot adott.
* A Claude vizuálisan erősebb és prezentációszerűbb kimenetet készített.
* A Gemini követhető tartalmat adott, de a formátumkövetés nem volt tökéletes.

### `1_baseline_ppt_generation`

Ebben a körben azt vizsgáltuk, hogy a modell képes-e a korábban generált prezentációvázlatból tényleges PowerPoint fájlt készíteni.

**Megfigyelések:**

* A ChatGPT képes volt használható prezentációalapot adni, de a vizuális kivitelezés további munkát igényelt.
* A Claude adta a leginkább előadásra alkalmas, vizuálisan igényes prezentációalapot.
* A Gemini PowerPoint helyett PDF formában készítette el a kimenetet, ami csökkentette a közvetlen használhatóságot.
* A Google AI Studio / Gemma nem adott közvetlen `.pptx` fájlt, hanem Python-kódot generált. Ez javítás után futtatható volt, de nem közvetlen prezentációgenerálásként működött.

### `2_strukturalt`

Ebben a kísérletben a fő hangsúly nem erre a promptverzióra került, de a strukturált prompt várhatóan akkor hasznos, ha pontosan szabályozni szeretnénk a slide-ok számát, felépítését és az előadói jegyzetek szerepét.

**Megfigyelések:**

* A strukturált prompt különösen hasznos lehet oktatási célú anyagoknál.
* Segíthet csökkenteni a túl hosszú vagy túl általános AI-válaszokat.
* A következő kísérletben érdemes lenne minden eszköznél külön tesztelni.

### `3_forrashuseg`

A forráshűségi prompt célja az lenne, hogy az AI csak a PDF tartalmára támaszkodjon, és ne hozzon be külső példákat vagy nem igazolható állításokat.

**Megfigyelések:**

* Ennél a témánál különösen fontos a forráshűség, mert a formális definíciók pontatlansága félrevezető lehet.
* A következő kísérletben érdemes lenne ezt a promptot külön futtatni, és összevetni a baseline eredményekkel.
* A forráshűséget nemcsak általánosan, hanem definíciószinten is érdemes ellenőrizni.

### `4_design`

A vizuális prompt a magyarázó ábrák, diagramok és slide-elrendezések minőségét helyezi előtérbe.

**Megfigyelések:**

* A Claude ebben a kísérletben prompt nélkül is erős vizuális szerkezetet adott.
* A Gemini előnye volt, hogy meglévő, releváns ábrákra hivatkozott.
* A következő kísérletben érdemes lenne a design promptot célzottan használni, mert az algoritmuselméleti fogalmak vizuális magyarázata sokat javíthatja a tanulhatóságot.

### `5_slide_ready`

A slide-ready prompt célja, hogy a slide-okon kevés szöveg legyen, a részletes magyarázat pedig az előadói jegyzetekbe kerüljön.

**Megfigyelések:**

* A tényleges prezentációkészítésben ez különösen fontos, mert a túlzsúfolt slide-ok nehezítik az előadást.
* A Claude és a ChatGPT kimenetei ebből a szempontból jó alapot adtak.
* A Gemma által generált kód is tartalmazott előadói jegyzeteket, de a vizuális kivitelezés gyenge maradt.

---

## 10. Kvalitatív összefoglaló

### Legfontosabb tapasztalatok

A kísérlet alapján mindegyik vizsgált AI-eszköz képes volt valamilyen módon támogatni a PDF-alapú prezentációkészítést, de eltérő erősségekkel és korlátokkal.

A ChatGPT leginkább a tartalmi struktúra és a tanulható vázlat kialakításában volt erős. Jól rendszerezte a fő fogalmakat, definíciókat és jelöléseket, ezért gyors első prezentációvázlathoz jól használható.

A Claude a vizuális és prezentációs minőségben teljesített kiemelkedően. A sötét hátterű kiemelő slide-ok és a világos magyarázó slide-ok váltakozása jól vezette a figyelmet, és az eredmény kisebb javítás után előadásra is alkalmasnak tűnt.

A Gemini követhető, szakmailag értelmezhető anyagot adott, és különösen hasznos volt, hogy meglévő, témába illő ábrákra hivatkozott. Ugyanakkor a formátumkövetés gyengébb volt, mert a kért Markdown és PowerPoint formátum helyett más kimenetet adott.

A Google AI Studio / Gemma inkább technikai kerülőmegoldást kínált: közvetlen `.pptx` helyett Python-kódot generált. Ez javítás után létrehozott egy egyszerű prezentációt, de a kért feladatot nem teljesítette közvetlenül.

### Meglepő eredmények

A legmeglepőbb eredmény az volt, hogy a tényleges PowerPoint-generálás nem minden eszköznél jelentette ugyanazt. Volt olyan modell, amely valódi prezentációszerű kimenetet adott, más PDF-et készített, a Gemma pedig kódot generált a fájl előállítására.

Szintén érdekes volt, hogy a vizuális minőség nem feltétlenül a technikailag legösszetettebb megoldásnál volt a legjobb. A Claude egyszerűbb, de jól megválasztott vizuális szerkezettel erős eredményt adott, míg a kódgenerált megoldás technikailag érdekes volt, de vizuálisan egyszerű maradt.

A Gemini esetében pozitív meglepetés volt a külső, már meglévő ábrákra való hivatkozás, mert ez pontosabb és szakmailag megbízhatóbb vizuális elemekhez vezethetett. Ugyanakkor a saját generálású ábrák elrendezése több helyen problémás volt.

### Korlátok és fenntartások

A kísérlet értelmezésénél figyelembe kell venni:

* Az eredmények nem általános rangsort jelentenek a ChatGPT, Claude, Gemini és Google AI Studio rendszerek között.
* Az összehasonlítás csak azokra a konkrét modellekre és felületekre vonatkozik, amelyekhez a kísérlet idején hozzáférés volt.
* Az AI-eszközök verziói, képességei és fájlkezelési lehetőségei idővel változhatnak.
* A vizsgálat egy konkrét algoritmuselméleti PDF-re és egy konkrét prezentációgenerálási feladatra épült.
* A pontozás részben szubjektív, mert emberi értékelés alapján történt.
* A PowerPoint-generálási képesség nem minden eszköznél érhető el azonos módon.
* A létrejött prezentációk végleges oktatási használata előtt szakmai és vizuális ellenőrzés továbbra is szükséges.

---

## 11. Következtetések és javaslatok

### Ajánlás felhasználási eset szerint

| Felhasználási eset                   | Ajánlott eszköz          | Ajánlott prompt                             | Indoklás                                                                                 |
| ------------------------------------ | ------------------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Gyors első prezentációvázlat         | ChatGPT                  | `1_baseline` vagy `2_strukturalt`           | Jól strukturált, tanulható vázlatot ad.                                                  |
| Szigorúan forráshű oktatási anyag    | ChatGPT / Claude         | `3_forrashuseg`                             | A forráshűséget célzott prompttal érdemes erősíteni.                                     |
| Vizuálisan gazdag prezentációterv    | Claude                   | `1_baseline_ppt_generation` vagy `4_design` | Ebben a kísérletben a Claude adta a legerősebb vizuális szerkezetet.                     |
| Slide-ready, kevés szöveges kimenet  | Claude / ChatGPT         | `5_slide_ready`                             | Mindkettő alkalmas lehet kevés szöveges, előadói jegyzetekkel támogatott prezentációhoz. |
| Tényleges PowerPoint fájl generálása | Claude / ChatGPT         | `ppt_generation`                            | Ezek adták a legközvetlenebb prezentációszerű eredményt.                                 |
| Meglévő szakmai ábrák felhasználása  | Gemini                   | `4_design`                                  | A Gemini hasznosan hivatkozott meglévő, témába illő ábrákra.                             |
| Kódalapú prezentációgenerálás        | Google AI Studio / Gemma | `ppt_generation_code`                       | Képes lehet kódot adni a PPT létrehozásához, de kézi javítás és futtatás szükséges.      |

### Általános következtetések

A kísérlet alapján az AI-eszközök jól használhatók első prezentációvázlat vagy prezentációalap készítésére, különösen akkor, ha a prompt világosan megadja a slide-számot, a célközönséget, a forráshűségi elvárást és a vizuális elemek szerepét.

Az AI önmagában még nem váltja ki teljesen az emberi szerkesztést. A tartalmi szerkezet, a definíciók rendszerezése és az előadói jegyzetek generálása erős támogatást jelent, de a végleges prezentációhoz továbbra is szükséges:

* szakmai ellenőrzés,
* képletek és definíciók pontosítása,
* ábrák vizuális javítása,
* slide-elrendezések igazítása,
* fájlformátum ellenőrzése.

A legjobb eredményt ebben a kísérletben az adta, amikor a modell nemcsak felsorolta a fogalmakat, hanem vizuálisan is segítette azok megértését. Ez különösen fontos az olyan formális témáknál, mint a P, NP, coNP, Karp-redukció, NP-nehézség és NP-teljesség.

### Következő kísérletben javítandó pontok

* Többféle forrásanyag kipróbálása.
* Ugyanazon promptok következetes futtatása minden eszközön.
* A Markdown-vázlat és a tényleges PPT-generálás külön értékelése.
* A formátumtartás külön pontozása.
* A képletek, formális definíciók és gráfos ábrák pontosságának külön vizsgálata.
* A kódalapú PPT-generálás külön kategóriaként való kezelése.
* A végleges prezentációk szakmai ellenőrzése oktatói vagy demonstrátori szempontból.

---

## 12. Mellékletek

| Elem                           | Hely                                                |
| ------------------------------ | --------------------------------------------------- |
| Forrásanyag                    | `source_materials/Algel_bonyelm_Friedl_Katalin.pdf` |
| Promptok                       | `prompts.md`                                        |
| Pontozási szempontrendszer     | `evaluation_criteria.md`                            |
| Nyers AI-kimenetek             | `outputs/`                                          |
| ChatGPT-kimenetek              | `outputs/chatgpt/`                                  |
| Claude-kimenetek               | `outputs/claude/`                                   |
| Gemini-kimenetek               | `outputs/gemini/`                                   |
| Google AI Studio-kimenetek     | `outputs/google_ai_studio/`                         |
| Screenshotok                   | `screenshots/`                                      |
| Részletes számszerű eredmények | `results/results.csv`                               |

---

## 13. Rövid végső konklúzió

A kísérlet célja nem az volt, hogy általánosságban rangsorolja a ChatGPT, Claude, Gemini vagy Google AI Studio rendszereket prezentációkészítés szempontjából. Az összehasonlítás kizárólag azokra a konkrét modellekre, felületekre és hozzáférési lehetőségekre vonatkozik, amelyek a kísérlet során rendelkezésre álltak. Az eredmények ezért gyakorlati, esettanulmány-jellegű összehasonlításként értelmezhetők.

A legjobb összesített eredményt ebben a konkrét kísérletben a Claude Sonnet 4.6 adta. Erőssége az volt, hogy nemcsak tartalmilag pontos és jól strukturált prezentációt készített, hanem vizuálisan is erős, előadásra alkalmas alapot adott. A sötét hátterű kiemelő slide-ok és a világos magyarázó slide-ok váltakozása jól vezette a figyelmet, a fogalmakhoz használt ábrák pedig szemléletesek voltak. Bár néhány ábra vagy szövegdoboz elcsúszott, összecsúszott vagy kilógott a diáról, ezek kisebb kézi szerkesztéssel javíthatók.

A Gemini 3.5 Flash jól követhető és szakmailag értelmezhető prezentációt készített. Külön előnye volt, hogy több helyen már meglévő, témába illő ábrákra hivatkozott, ami szakmailag pontosabb vizuális elemekhez vezethetett. Ugyanakkor a kimenet nem tartotta teljesen a kért formátumot: nem megfelelő Markdown formában dolgozott, és PowerPoint helyett PDF-ként készítette el a prezentációt. A saját generálású ábrái több helyen túl kicsik, túl sűrűk vagy elcsúszottak voltak.

A GPT-5.5 használható, de több szempontból javítandó prezentációalapot adott. A fő definíciók, jelölések és példák megjelentek, a matematikai szimbólumokat alapvetően jól használta, és a választott színösszeállítás kellemes volt. Ugyanakkor a logikai ív csak közepesen volt követhető, a vizuális elemek és az elrendezés több helyen kézi javítást igényeltek. Emiatt tanulási alapnak megfelelő, de előadásra kész prezentációként még jelentős utómunkára lenne szükség.

A Google AI Studio / Gemma technikailag érdekes, de közvetlen prezentációgenerálás szempontjából korlátozott eredményt adott. A felületen nem készült közvetlenül letölthető `.pptx`, hanem Python-kód generálódott, amelyet javítani és külön futtatni kellett. A javítás után létrejött egy 20 slide-os, egyszerű, fehér hátterű, de a lényeget tartalmazó és viszonylag követhető prezentáció. Ez hasznos kerülőmegoldás, de sokkal több emberi utómunkát igényelt, mint a többi eszköz kimenete.

Összességében a kísérlet azt mutatta meg, hogy az AI-eszközök már jól használhatók oktatási prezentációk első változatának elkészítésére, de a minőség erősen függ a konkrét modelltől, a felülettől és a fájlkezelési lehetőségektől. Ebben a konkrét kísérleti környezetben a Claude Sonnet 4.6 bizonyult a legalkalmasabbnak, mert egyszerre adott tartalmilag pontos, jól strukturált, vizuálisan igényes és kisebb javítás után előadásra is alkalmas prezentációalapot. A Gemini erős volt követhetőségben és ábrahivatkozásokban, a GPT-5.5 használható tartalmi alapot adott, a Gemma pedig inkább kódalapú kerülőmegoldást kínált. A végleges, oktatásban is használható prezentációhoz minden esetben szükség van emberi ellenőrzésre és vizuális finomításra.
