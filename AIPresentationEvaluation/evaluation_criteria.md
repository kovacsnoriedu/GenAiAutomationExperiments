# Értékelési szempontrendszer – MI-alapú prezentációgenerálás

Ez a dokumentum definiálja a kísérletben használt 10 értékelési szempontot és az 1–5 pontozási skála jelentését minden szempontnál. A `ppt_evaluation_helper.py` program ezeket a szempontokat kéri be értékeléskor.

---

## Pontozási skála általánosan

| Pontszám | Jelentés |
|---|---|
| 1 | Nagyon gyenge – nem teljesíti az elvárást |
| 2 | Gyenge – részben teljesíti, de jelentős hiányosságokkal |
| 3 | Közepes – elfogadható, de javítható |
| 4 | Jó – megfelel az elvárásoknak, kis javítással kész |
| 5 | Kiváló – azonnal vagy minimális munkával használható |

---

## 1. Tartalmi pontosság

**Kérdés:** A slide-okon megjelenő állítások, adatok, definíciók helyesek és relevánsak-e?

| Pont | Leírás |
|---|---|
| 1 | Több téves állítás, helytelen adat vagy félrevezető megfogalmazás |
| 2 | Néhány pontatlanság, de az alapgondolat helyes |
| 3 | Többnyire pontos, 1-2 kisebb hiba |
| 4 | Pontos tartalom, legfeljebb apró stiláris pontatlanság |
| 5 | Teljesen pontos és releváns tartalom |

---

## 2. Forráshűség

**Kérdés:** Az AI kizárólag a megadott forrásanyagból dolgozik-e, vagy "hallucinálja" a tartalmat?

| Pont | Leírás |
|---|---|
| 1 | Jelentős mennyiségű tartalom nem a forrásból származik (kitalált adatok, példák) |
| 2 | Több, forrásban nem szereplő elem jelenik meg, de az alaptartalom ott van |
| 3 | Kis mértékű kiegészítés általános tudásból, de ez nem félrevezető |
| 4 | Szinte teljesen a forrásból dolgozik, 1 apró kiegészítéssel |
| 5 | Kizárólag a forrásanyagra támaszkodik, nincs "hallucináció" |

---

## 3. Struktúra

**Kérdés:** Van-e egyértelmű felépítés? Van cím slide, tartalom/agenda, tartalmi rész és záró slide?

| Pont | Leírás |
|---|---|
| 1 | Nincs strukturált felépítés, a slide-ok sorrendje véletlenszerű |
| 2 | Van valami felépítés, de hiányzik a bevezető vagy a záró rész |
| 3 | Alapstruktúra megvan, de nem minden konvencionális elem szerepel |
| 4 | Jó struktúra, legfeljebb egy-két elem hiányzik vagy gyenge |
| 5 | Teljes, logikus felépítés: cím – agenda – tartalom – összefoglalás |

---

## 4. Logikai ív (narratíva)

**Kérdés:** A slide-ok egymásra épülnek-e? Van-e egyértelmű "sztori" vagy gondolatmenet, amit a nézők követni tudnak?

| Pont | Leírás |
|---|---|
| 1 | Nincs narratíva, a slide-ok egymástól független "ténytömbök" |
| 2 | Néhol érezhető összefüggés, de az ív töredékes |
| 3 | Felismerhető gondolatmenet, de vannak "ugrások" |
| 4 | Jól felépített narratíva, kis kiesésekkel |
| 5 | Erős, következetes logikai ív az elejétől a végéig |

---

## 5. Szövegmennyiség

**Kérdés:** Megfelelő-e a szöveg mennyisége és sűrűsége slide-onként? Nem túlzsúfolt, nem túl üres?

| Pont | Leírás |
|---|---|
| 1 | Szinte minden slide tele van folyó szöveggel, vagy szinte üresek a diák |
| 2 | Többnyire túl sok szöveg, de van néhány jól méretezett slide |
| 3 | Vegyes: egyes slide-ok jók, mások túlzsúfoltak vagy túl üresek |
| 4 | Többnyire megfelelő, 1-2 slide szövegmennyisége javítható |
| 5 | Minden slide-on optimális a szöveg sűrűsége (bullet pontok, tömörség) |

---

## 6. Design / vizuális javaslatok

**Kérdés:** Ad-e az AI konkrét és hasznos javaslatokat a slide-ok vizuális megjelenítésére (elrendezés, színek, stílus)?

| Pont | Leírás |
|---|---|
| 1 | Nem ad semmilyen vizuális javaslatot |
| 2 | Általános, semmitmondó javaslatok (pl. "adj hozzá képet") |
| 3 | Van néhány konkrét elrendezési javaslat |
| 4 | Minden slide-hoz konkrét, megvalósítható vizuális ötlet |
| 5 | Részletes, kreatív, összefüggő vizuális koncepció az egész prezentációhoz |

> **Megjegyzés:** Ha az adott prompt nem kért kifejezetten designjavaslatokat, akkor is értékelhető, hogy az AI adott-e önállóan használható vizuális ötleteket. Ha egyáltalán nem szerepelt vizuális vagy design elem a kimenetben, akkor alacsony pontszám adható. `0` csak akkor használandó, ha a szempont az adott kísérletben egyáltalán nem értelmezhető.


---

## 7. Képek, diagramok, vizuális elemek

**Kérdés:** Az AI javasol-e konkrét képeket, diagramokat, táblázatokat vagy infografikákat? Mennyire hasznosak és megvalósíthatók ezek a javaslatok?

| Pont | Leírás |
|---|---|
| 1 | Nem javasol semmilyen vizuális elemet |
| 2 | Általános, nem specifikus vizuális ötletek |
| 3 | Néhány konkrét javaslat (pl. "tegyünk ide kördiagramot") |
| 4 | Konkrét és releváns vizuális javaslatok a legtöbb slide-hoz |
| 5 | Részletes, megvalósítható vizuális javaslatok diagramtípussal, tartalommal |

---

## 8. Előadói jegyzetek minősége

**Kérdés:** Az előadói megjegyzések hasznosak, informatívak és részletesek-e? Kiegészítik-e a diákon lévő bullet pontokat?

| Pont | Leírás |
|---|---|
| 1 | Nincsenek előadói jegyzetek, vagy teljesen üresek |
| 2 | Vannak, de csak megismétlik a bullet pontokat |
| 3 | Némi kiegészítés van, de általánosan megfogalmazva |
| 4 | Részletes és hasznos megjegyzések, kisebb hiányokkal |
| 5 | Kiváló előadói jegyzetek: részletes, az előadónak valóban segít |

> **Megjegyzés:** Ha a prompt kért előadói jegyzeteket, de az AI nem adott ilyet, akkor ez alacsony pontszámot jelent. `0` csak akkor használandó, ha az adott kísérletben az előadói jegyzetek nem voltak elvárva vagy nem értelmezhetők.


---

## 9. Emberi utómunka szükségessége

**Kérdés:** Mennyi emberi javítás, átírás és kiegészítés szükséges ahhoz, hogy a generált vázlat valóban felhasználható prezentációvá váljon?

| Pont | Leírás |
|---|---|
| 1 | Szinte mindent újra kell írni – csak kiindulópontnak használható |
| 2 | Jelentős átírás szükséges (slide-ok többsége érintett) |
| 3 | Mérsékelt utómunka – néhány slide alapvetően jó, mások igényelnek javítást |
| 4 | Kis utómunka – kevés javítás, pontosítás szükséges |
| 5 | Minimális vagy nincs utómunka – azonnal vagy szinte azonnal használható |

---

## 10. Összesített használhatóság

**Kérdés:** Összességében mennyire volt hasznos az AI eszköz ebben a konkrét kísérletben?

| Pont | Leírás |
|---|---|
| 1 | Nem segített – az eredmény nem volt felhasználható |
| 2 | Korlátozott segítség – sok munkát igényelt az eredmény |
| 3 | Közepes – megkönnyítette a munkát, de nem volt kiemelkedő |
| 4 | Hasznos – valódi időmegtakarítást eredményezett |
| 5 | Kiváló – azonnal munkaképes eredményt adott |

---

## Gyorskártya összefoglalás

| # | Szempont | Kulcskérdés |
|---|---|---|
| 1 | Tartalmi pontosság | Helyes-e a tartalom? |
| 2 | Forráshűség | Csak a forrásból dolgozik-e? |
| 3 | Struktúra | Van-e logikus felépítés? |
| 4 | Logikai ív | Egymásra épülnek-e a slide-ok? |
| 5 | Szövegmennyiség | Megfelelő sűrűségű-e a szöveg? |
| 6 | Design javaslatok | Hasznos vizuális ötletek? |
| 7 | Képek, diagramok | Konkrét vizuális elemek? |
| 8 | Előadói jegyzetek | Hasznosak-e a megjegyzések? |
| 9 | Utómunka | Mennyi javítás kell? |
| 10 | Összesített használhatóság | Megérte az AI-t használni? |
