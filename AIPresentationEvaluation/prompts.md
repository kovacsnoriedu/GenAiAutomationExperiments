## Konkrét kísérletben használt promptok – algoritmuselmélet PDF

Ebben a részben azok a promptok szerepelnek, amelyeket a kísérlet során ténylegesen használtunk az algoritmuselméleti PDF alapján történő prezentációgeneráláshoz.

A forrásanyag:

```text
source_materials/Algel_bonyelm_Friedl_Katalin.pdf
```

A prezentáció témája:

```text
A bonyolultságelmélet alapjai: P, NP, coNP, Karp-redukció, NP-nehézség és NP-teljesség.
```

---

### 8. Algoritmuselmélet PDF – 20 slide-os prezentációvázlat (`algel_20slide_outline`)

**Cél:**
A modell készítsen oktatási célú, 20 slide-os prezentációvázlatot egy egyetemi algoritmuselmélet PDF alapján.
Ez a prompt azt vizsgálja, hogy az AI mennyire képes egy formális, definíciókkal és képletekkel teli forrásanyagból tanulható, vizuálisan is magyarázható prezentációstruktúrát készíteni.

```text
Egy egyetemi algoritmuselmélet jegyzet PDF-jéből szeretnék oktatási célú prezentációt készíteni.

Feladatod: készíts egy 20 slide-os prezentációvázlatot a feltöltött PDF alapján.

A prezentáció témája:
A bonyolultságelmélet alapjai: P, NP, coNP, Karp-redukció, NP-nehézség és NP-teljesség.

Fontos elvárások:

1. Csak a PDF-ben szereplő tartalomra támaszkodj. Ne találj ki új tételeket vagy külső példákat.
2. A célközönség algoritmuselméletet tanuló egyetemi hallgatók.
3. A prezentáció legyen tanulható, vizsgára készüléshez is használható.
4. Minden slide-hoz add meg:
   - slide címét,
   - 3–5 rövid bullet pontot,
   - a kiemelendő definíciót / képletet / jelölést, ha van,
   - javasolt ábrát vagy vizuális elemet,
   - rövid előadói megjegyzést.
5. Ne legyen túl sok szöveg a slide-okon. A részletesebb magyarázat menjen az előadói jegyzetbe.
6. Különösen figyelj ezekre:
   - P definíciója,
   - NP definíciója,
   - hatékony tanúsítvány,
   - coNP,
   - P ⊆ NP és P ⊆ coNP,
   - P ?= NP kérdés,
   - Karp-redukció,
   - NP-nehéz és NP-teljes problémák,
   - 3-színezés,
   - maximális független ponthalmaz,
   - maxklikk.
7. A nehéz fogalmaknál adj szemléletes magyarázatot is.
8. Ahol képlet vagy formális definíció szerepel, emeld ki külön „Képlet / definíció” sorban.
9. Ahol lehet, javasolj ábrát:
   - halmazábra P, NP, coNP viszonyára,
   - folyamatábra tanúsítvány ellenőrzésére,
   - redukciós nyíl X ≺ Y szemléltetésére,
   - gráfos ábra 3-színezéshez,
   - komplementer gráf ábra független ponthalmaz és klikk kapcsolatához.
10. A végén adj egy rövid összefoglalót arról, hogy a hallgatónak mi az 5 legfontosabb gondolat, amit meg kell jegyeznie.

Kimeneti formátum:

## Slide 1: [cím]
- Bullet pontok:
  - ...
- Képlet / definíció:
  - ...
- Ábraötlet:
  - ...
- Előadói megjegyzés:
  - ...

Ezt folytasd mind a 20 slide-ra.
```

---

### 9. Algoritmuselmélet PDF – tényleges PowerPoint generálása (`algel_ppt_generation`)

**Cél:**
A modell ne csak prezentációvázlatot adjon, hanem készítsen tényleges `.pptx` fájlt is.
Ez a prompt azt vizsgálja, hogy az AI képes-e a korábbi vázlatból valóban használható PowerPoint prezentációt készíteni.

```text
A korábban elkészített 20 slide-os prezentációvázlat alapján kérlek, készíts tényleges PowerPoint prezentációt .pptx formátumban.

Fontos elvárások:

1. A prezentáció pontosan 20 slide-ból álljon.
2. A forrás továbbra is a feltöltött algoritmuselmélet PDF legyen.
3. A témája:
   „A bonyolultságelmélet alapjai: P, NP, coNP, Karp-redukció, NP-nehézség és NP-teljesség”.
4. A slide-okon kevés szöveg legyen, csak a legfontosabb kulcsszavak és definíciók.
5. A részletesebb magyarázat kerüljön az előadói jegyzetekbe, ha tudsz ilyet készíteni.
6. Emeld ki vizuálisan a fő definíciókat és jelöléseket, például:
   - P
   - NP
   - coNP
   - P ⊆ NP
   - P ⊆ coNP
   - P ?= NP
   - X ≺ Y
   - NP-nehéz
   - NP-teljes
7. A nehéz fogalmakhoz adj egyszerű ábrákat vagy vizuális szemléltetést:
   - halmazábra P, NP, coNP kapcsolatára,
   - folyamatábra a tanúsítvány ellenőrzésére,
   - redukciós nyíl X ≺ Y szemléltetésére,
   - gráfos ábra 3-színezéshez,
   - komplementer gráf ábra a független ponthalmaz és klikk kapcsolatára.
8. A design legyen egységes, letisztult, oktatási célra alkalmas.
9. Ne találj ki új tételeket vagy külső példákat a PDF-en kívül.
10. A végén adj letölthető .pptx fájlt.
```

---

### 10. Algoritmuselmélet PDF – forráshű javító prompt (`algel_forrashu_javitas`)

**Cél:**
Egy már elkészült prezentációvázlat vagy PowerPoint tartalmi ellenőrzése és javítása a PDF alapján.

```text
Ellenőrizd és javítsd az alábbi prezentációvázlatot a feltöltött algoritmuselmélet PDF alapján.

Feladatod:

1. Ellenőrizd, hogy a slide-ok tartalma forráshű-e.
2. Jelöld, ha valamelyik állítás nem szerepel a PDF-ben.
3. Javítsd a pontatlan vagy félrevezető megfogalmazásokat.
4. Tartsd meg a 20 slide-os szerkezetet.
5. A slide-okon legyen kevés szöveg.
6. A fő definíciókat és jelöléseket emeld ki.
7. Ahol lehet, javasolj pontosabb ábrát vagy vizuális magyarázatot.
8. Ne hozz be külső példákat vagy új tételeket.

Javítandó prezentációvázlat:

[VÁZLAT]
```

---

### 11. Algoritmuselmélet PDF – designfókuszú javító prompt (`algel_design_javitas`)

**Cél:**
Egy már elkészült prezentációvázlat vagy PPT vizuális és prezentációtechnikai javítása.

```text
Az alábbi 20 slide-os prezentációvázlatot alakítsd vizuálisan erősebb, oktatási célra jobban használható prezentációvá.

Fontos szempontok:

1. Ne változtasd meg a szakmai tartalom lényegét.
2. A slide-ok maradjanak rövidek és jól olvashatók.
3. Minden slide-hoz adj konkrét vizuális elrendezési javaslatot.
4. Javasolj ábrákat a nehezebb fogalmakhoz:
   - P, NP, coNP halmazábra,
   - tanúsítvány ellenőrzési folyamat,
   - Karp-redukciós nyíl,
   - 3-színezés gráfos példa,
   - független ponthalmaz és klikk kapcsolata.
5. Adj egységes vizuális stílusjavaslatot az egész prezentációhoz.
6. Jelöld, mely slide-oknál lenne szükség kézi ábrakészítésre.

Javítandó prezentációvázlat:

[VÁZLAT]
```
