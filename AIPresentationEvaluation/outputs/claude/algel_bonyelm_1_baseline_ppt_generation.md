# Prezentációvázlat: A bonyolultságelmélet alapjai
### P, NP, coNP, Karp-redukció, NP-nehézség és NP-teljesség
**Célközönség:** Algoritmuselméletet tanuló egyetemi hallgatók  
**Forrás:** Friedl Katalin – Kiegészítő anyag az Algoritmuselmélet tárgyhoz (BME SZIT, 2010)

---

## Slide 1: Bevezető – Mi a hatékony algoritmus?

- **Bullet pontok:**
  - Egy algoritmus *hatékony*, ha lépésszáma felülről becsülhető a bemenet hosszának egy polinomjával
  - Ha f(n) = O(nᵏ) valamely k > 0 konstansra, az algoritmust polinomiálisnak nevezzük
  - Ha a kimenet exponenciálisan hosszú, az algoritmus nem lehet polinomiális (pl. x → 2ˣ)
  - Előfordulhat, hogy bár a kimenet rövid (1 bit), mégsem ismert hatékony algoritmus
  - Most csak *eldöntési problémákkal* foglalkozunk (a válasz: igen/nem)

- **Képlet / definíció:**
  - `f(n) = O(nᵏ)` valamely k > 0 pozitív konstansra

- **Ábraötlet:**
  - Egyszerű timeline: bemenet → algoritmus → 1 bit kimenet; mellette: „hatékony?" kérdőjel

- **Előadói megjegyzés:**
  - Az előadás motivációja: sok fontos problémánál nem tudunk hatékony algoritmust adni, de nem tudjuk azt sem bizonyítani, hogy nem létezik. A bonyolultságelmélet ezeket a határokat vizsgálja.

---

## Slide 2: Eldöntési problémák – Példák

- **Bullet pontok:**
  - **PRIM:** Adott m > 0 egész – prímszám-e?
  - **H (Hamilton-kör):** Adott G = (V, E) irányítatlan gráf – van-e benne Hamilton-kör?
  - **ÚT:** Adott G gráf és s, t csúcsok – van-e s és t között út?
  - Egy eldöntési problémához tartozó **L nyelv** az „igen" válaszú bemenetek halmaza
  - A lehetséges bemeneteket **szavaknak** nevezzük

- **Képlet / definíció:**
  - x ∈ X jelöli, hogy az x bemenetre a válasz *igen*
  - A(x) jelöli az A algoritmus eredményét x-en

- **Ábraötlet:**
  - Három mini gráf: egy Hamilton-körös, egy anélküli, egy összefüggő s-t úttal

- **Előadói megjegyzés:**
  - Fontos hangsúlyozni: az eldöntési problémák nem szűkítik le a valódi feladatokat – a legtöbb optimalizálási probléma visszavezethető eldöntési problémára.

---

## Slide 3: A P osztály definíciója

- **Bullet pontok:**
  - P = azon eldöntési problémák halmaza, amelyek **polinomiális idejű algoritmust** engednek meg
  - Az algoritmusnak minden bemenetre helyesen kell válaszolnia
  - Lépésszám: O(|x|ᵏ) valamely k > 0 konstansra (k független x-től)
  - Példa P-ben: **ÚT** – szélessége bejárással eldönthető, polinomiális
  - Meglepő P-beli példa: **PRIM** – 2002-ben bizonyított be (AKS-algoritmus)

- **Képlet / definíció:**
  - **P = { X eldöntési probléma | ∃ A algoritmus: ∀x esetén A(x) helyes és lépésszáma O(|x|ᵏ) }**

- **Ábraötlet:**
  - Egyetlen nagy „P" kör, benne: ÚT, PRIM feliratokkal

- **Előadói megjegyzés:**
  - A k konstans a problémától függ, de x-től nem. Például ha k = 3, az algoritmus O(n³) lépésben fut minden n hosszú bemeneten.

---

## Slide 4: Hatékony tanúsítvány – Az NP osztály alapja

- **Bullet pontok:**
  - Ha x ∈ X, akkor legyen t egy **rövid (polinom hosszú) bizonyíték** erre
  - A T algoritmus az (x, t) párokon ellenőrzi a tanúsítványt polinomiális időben
  - Ha x ∉ X, akkor **nem létezik** olyan t, amely T-t becsaphatja
  - Szemléletes kép: a tanúsítvány egy „megfejtés", amit gyorsan le lehet ellenőrizni
  - A megfejtés *megtalálása* viszont lehet exponenciálisan nehéz

- **Képlet / definíció:**
  - Ha x ∈ X: ∃ t, |t| = O(|x|ᶜ), T(x, t) = igen
  - Ha x ∉ X: ∀ t, |t| = O(|x|ᶜ) esetén T(x, t) ≠ igen
  - T lépésszáma: O((|x| + |t|)ᵏ)

- **Ábraötlet:**
  - Folyamatábra: x bemenet → [van-e jó t?] → igen ág: T ellenőrző algoritmus → „igen"; nem ág: nincs jó t → „nem"

- **Előadói megjegyzés:**
  - Az NP osztály kulcsgondolata: az ellenőrzés könnyű, de a megoldás megtalálása nem feltétlenül az. Ez a hétköznapi tapasztalattal egybevág: egy Sudoku-megoldás ellenőrzése perc alatt megy, de megtalálása nehéz.

---

## Slide 5: Az NP osztály definíciója

- **Bullet pontok:**
  - **NP** = azon eldöntési problémák halmaza, amelyekhez **van hatékony tanúsítvány**
  - NP neve: „nemdeterminisztikus polinomiális idő"
  - A t bizonyítékot elég „megsejtenünk" – az ellenőrzés már determinisztikus, polinomiális
  - Ha az összes lehetséges t-t végigpróbálnánk, exponenciális lenne az idő (2ⁿ lehetséges t)
  - P ⊆ NP: ha van polinomiális algoritmus, akkor t = üres (a bizonyíték nem szükséges)

- **Képlet / definíció:**
  - **NP = { X | X-hez van hatékony tanúsítvány }**
  - P ⊆ NP (1. állítás)

- **Ábraötlet:**
  - Halmazábra: P ⊂ NP (P kisebb kör NP-n belül), „P = NP?" kérdőjellel

- **Előadói megjegyzés:**
  - Az NP rövidítés nem „nem polinomiális"-t jelent! Sok hallgató tévesen gondolja ezt. Nondeterminisztikus polinomiális időre utal.

---

## Slide 6: NP-beli példák – Hamilton-kör és 3-színezés

- **Bullet pontok:**
  - **H ∈ NP:** tanúsítvány = csúcsok sorrendbe rendezése a Hamilton-kör mentén; T ellenőrzi, hogy valóban kör-e
  - **ÖSSZETETT ∈ NP:** tanúsítvány = egy valódi osztó t; T ellenőrzi, hogy 1 < t < m és t | m
  - **3SZÍN ∈ NP:** tanúsítvány = minden csúcshoz egy szín (1, 2, 3); T ellenőrzi, hogy szomszédok különböző színűek-e
  - Mindhárom esetben a tanúsítvány polinomiális hosszú
  - A T algoritmusok lineáris vagy polinomiális lépésszámúak

- **Képlet / definíció:**
  - 3SZÍN: ha ∀ {vᵢ, vⱼ} ∈ E esetén tᵢ ≠ tⱼ, akkor a t sorozat érvényes 3-színezés

- **Ábraötlet:**
  - Kis gráf 3-színezéssel illusztrálva (5-6 csúcs, 3 különböző szín)

- **Előadói megjegyzés:**
  - Hangsúlyozzuk, hogy az ÖSSZETETT ∈ NP nem azt jelenti, hogy az összetettség eldöntése nehéz – épp ellenkezőleg, könnyű ellenőrizni. A PRIM probléma is P-ben van (AKS, 2002).

---

## Slide 7: A komplementer és a coNP osztály

- **Bullet pontok:**
  - Egy X probléma **komplementere** X̄: ugyanolyan bemenet, ellentétes válasz (x ∈ X ⟺ x ∉ X̄)
  - Példa: ÖSSZETETT = PRIM (a prímek komplementere az összetett számok)
  - **coNP:** az NP-beli problémák komplementereinek halmaza
  - NP-ben az *igen* válaszra van rövid bizonyíték; coNP-ben a *nem* válaszra
  - P ⊆ NP és P ⊆ coNP (1. állítás)

- **Képlet / definíció:**
  - X ∈ coNP ⟺ X̄ ∈ NP
  - **coNP = { X | X̄ ∈ NP }**

- **Ábraötlet:**
  - Halmazábra: P a középen, NP bal oldalt, coNP jobb oldalt, P mindkettőnek részhalmazaként; „NP ∩ coNP" metszet kiemelve

- **Előadói megjegyzés:**
  - Nyitott kérdés, hogy NP = coNP? Ha P = NP, akkor NP = coNP is következik, de fordítva nem.

---

## Slide 8: P ?= NP – A legnagyobb nyitott kérdés

- **Bullet pontok:**
  - Nem ismert, hogy P = NP vagy P ⊊ NP
  - Ha P ⊊ NP: léteznek problémák, ahol az igen esethez van rövid bizonyíték, de megtalálni nem lehet polinomidőben
  - Ez azt jelenti: egy helyes válasz **ellenőrzése** lényegesen könnyebb lehet, mint **megtalálása**
  - 2000-ben a Clay Mathematics Institute 1 millió dolláros díjat tűzött ki a P ?= NP megoldására
  - Szintén nyitott: P ?= NP ∩ coNP

- **Képlet / definíció:**
  - P ⊆ NP ∩ coNP (bizonyított)
  - P ?= NP (nyitott)
  - P ?= NP ∩ coNP (nyitott)

- **Ábraötlet:**
  - Két verzió egymás mellett: bal „Ha P = NP" (egy kör), jobb „Ha P ⊊ NP" (P kisebb körként NP-n belül)

- **Előadói megjegyzés:**
  - A P ?= NP kérdés gyakorlati jelentősége is hatalmas: ha P = NP, akkor például a titkosítás mai formájában összeomlana, hiszen a kódtörési problémák szintén NP-ben vannak.

---

## Slide 9: Karp-redukció (polinomiális visszavezetés)

- **Bullet pontok:**
  - Két eldöntési probléma **nehézségének összehasonlítására** szolgál
  - X ≺ Y: X visszavezethető Y-ra polinomiálisan
  - Az f függvény minden X-bemenetet Y-bemenetre képez, megőrizve az igen/nem választ
  - Ha Y megoldható, akkor X is megoldható (Y legalább olyan nehéz, mint X)
  - A ≺ reláció **tranzitív**: ha X ≺ Y és Y ≺ Z, akkor X ≺ Z

- **Képlet / definíció:**
  - **X ≺ Y:** ∃ polinomidőben számolható f: x ∈ X ⟺ f(x) ∈ Y
  - 3. állítás: Ha Y ∈ P és X ≺ Y, akkor X ∈ P
  - 4. állítás: Ha Y ∈ NP és X ≺ Y, akkor X ∈ NP

- **Ábraötlet:**
  - Nyíl X-ből Y-ba (X ≺ Y), mellette f(x) transzformáció; alatta: „ha Y könnyű, X is könnyű"

- **Előadói megjegyzés:**
  - Szemléletes analógia: ha Y-t „meg tudom oldani", és X-et át tudom fordítani Y-kérdésre, akkor X-et is meg tudom oldani. A redukció „bonyolultságot örökít felfelé".

---

## Slide 10: A Karp-redukció tulajdonságai

- **Bullet pontok:**
  - Ha X ≺ Y, akkor X̄ ≺ Ȳ is teljesül (komplementerek is visszavezethetők) – 2. állítás
  - Ha Y ∈ P és X ≺ Y → X ∈ P (3. állítás)
  - Ha Y ∈ NP és X ≺ Y → X ∈ NP (4. állítás)
  - Ha Y ∈ coNP és X ≺ Y → X ∈ coNP (5. állítás)
  - Tranzitivitás (6. állítás): X ≺ Y és Y ≺ Z → X ≺ Z

- **Képlet / definíció:**
  - Lépésszám bizonyításban: O(|x|ᵈ) + O(|f(x)|ᵏ) = O(|x|ᵈᵏ) – polinom marad

- **Ábraötlet:**
  - Lánc: X ≺ Y ≺ Z, nyilakkal, alattuk „g∘f" kompozíció jelölése

- **Előadói megjegyzés:**
  - A lépésszám-elemzés fontos: polinom polinjának polinja is polinom, ezért a kompozíció megőrzi a polinomiális hatékonyságot.

---

## Slide 11: NP-nehéz és NP-teljes problémák

- **Bullet pontok:**
  - **NP-nehéz (Z):** minden X ∈ NP esetén X ≺ Z (Z legalább olyan nehéz, mint bármely NP-beli probléma)
  - **NP-teljes (Z):** NP-nehéz ÉS Z ∈ NP (az NP legnehezebbek)
  - Ha egyetlen NP-teljes probléma P-ben lenne → P = NP
  - Az első NP-teljességi bizonyítást Stephen Cook és Leonid Levin adta egymástól függetlenül (1970-es évek eleje)
  - Az NP-teljes problémák száma gyorsan nőtt; a 70-es évek végére már könyvet töltöttek meg

- **Képlet / definíció:**
  - Z NP-nehéz: ∀ X ∈ NP: X ≺ Z
  - Z NP-teljes: Z NP-nehéz ÉS Z ∈ NP

- **Ábraötlet:**
  - Halmazábra: NP nagy kör, belső határ: NP-teljes problémák, kívül (csak NP-nehéz), P belső kis körként

- **Előadói megjegyzés:**
  - Az NP-teljességi bizonyítás standard sémája: (1) megmutatjuk, hogy Z ∈ NP; (2) egy ismert NP-teljes Y-ból Y ≺ Z visszavezetést adunk. A tranzitivitás miatt ez elegendő.

---

## Slide 12: Az NP-teljességi bizonyítás sémája

- **Bullet pontok:**
  - **1. lépés:** Belátjuk, hogy Z ∈ NP (hatékony tanúsítványt adunk)
  - **2. lépés:** Választunk egy ismert NP-teljes Y-t, és megmutatjuk, hogy Y ≺ Z
  - A tranzitivitás miatt ebből következik, hogy minden X ∈ NP esetén X ≺ Z
  - Kiindulási alap (bizonyítás nélkül elfogadva): **3SZÍN NP-teljes**
  - A 2SZÍN probléma viszont P-ben van (szélessége bejárással ellenőrizhető)

- **Képlet / definíció:**
  - ∀ X ∈ NP: X ≺ Y és Y ≺ Z ⟹ X ≺ Z (tranzitivitás alapján)

- **Ábraötlet:**
  - Lépcsős diagram: X ≺ Y (ismert) → Y ≺ Z (új bizonyítás) → következtetés: Z NP-teljes

- **Előadói megjegyzés:**
  - Praktikus tanács: az NP-teljességi bizonyítások „láncszemei" – mindig egy már ismert NP-teljes problémából indulunk ki. Ezért kritikus az első NP-teljes probléma (Cook–Levin tétel).

---

## Slide 13: 3-színezés – NP-teljesség

- **Bullet pontok:**
  - **3SZÍN:** Adott G = (V, E) irányítatlan egyszerű gráf – kiszínezhető-e 3 színnel?
  - 3SZÍN ∈ NP: tanúsítvány a csúcsok színsorozata; T ellenőrzi, hogy szomszédok különbözőek-e
  - **3SZÍN NP-teljes** – kiindulási alap (bizonyítás nélkül)
  - 2SZÍN ∈ P: páros gráf egyenértékű a 2-színezhetőséggel, ellenőrizhető bejárással
  - 4SZÍN szintén NP-teljes: visszavezethető 3SZÍN-ről (5. feladat megoldása a PDF-ben)

- **Képlet / definíció:**
  - 3SZÍN: ∃ c: V → {1,2,3}, hogy ∀ {u,v} ∈ E: c(u) ≠ c(v)

- **Ábraötlet:**
  - Gráf 5-6 csúccsal, 3 különböző szín (pl. piros, kék, zöld) a csúcsokon; szomszédos csúcsok mindig különbözőek

- **Előadói megjegyzés:**
  - A 4SZÍN visszavezetés elegáns: veszünk egy új x csúcsot, összekötjük az összes régi csúccsal. Ha 4-gel színezhető az így kapott G', akkor x elveszi az egyik színt, és G 3-mal színezhető.

---

## Slide 14: Maximális független ponthalmaz – maxFTL

- **Bullet pontok:**
  - **maxFTL:** Adott (G, k) – van-e G-ben k darab független csúcs?
  - Független ponthalmaz: semmilyen két csúcs közt nincs él
  - maxFTL ∈ NP: tanúsítvány a k csúcs felsorolása; T ellenőrzi a függetlenséget
  - Ha van polinomiális algoritmus maxFTL-re → bináris kereséssel meg is található a maximum mérete
  - **maxFTL NP-teljes** – visszavezethető 3SZÍN-ről (3. tétel)

- **Képlet / definíció:**
  - maxFTL: (G, k) ∈ maxFTL ⟺ ∃ F ⊆ V, |F| ≥ k, ∀ u,v ∈ F: {u,v} ∉ E

- **Ábraötlet:**
  - Gráf kiemelve k független csúccsal (pl. 4 csúcsból 2 kijelölt, köztük nincs él)

- **Előadói megjegyzés:**
  - A bináris keresés trükk (2. tétel): ha van maxFTL-re polinomiális algoritmus, akkor O(log n) hívással meghatározható a maximum. Ez az optimalizálás és az eldöntés kapcsolatát mutatja.

---

## Slide 15: 3SZÍN ≺ maxFTL – A visszavezetés konstrukciója

- **Bullet pontok:**
  - Adott G (n csúcsú) gráf; H-nak 3n csúcsa lesz: a₁…aₙ, b₁…bₙ, c₁…cₙ
  - Ha G-ben él van vᵢ és vⱼ között → él megy aᵢ-aⱼ, bᵢ-bⱼ, cᵢ-cⱼ között is (3 másolat)
  - Minden i-re él húzódik aᵢ, bᵢ, cᵢ között (egy G-beli pont három másolatát összekötjük)
  - k = n
  - G ∈ 3SZÍN ⟺ (H, n) ∈ maxFTL

- **Képlet / definíció:**
  - Előre: Ha G 3-színezhető → minden i-re pontosan egyet választunk az {aᵢ, bᵢ, cᵢ} hármasból → n független pont H-ban
  - Vissza: n független pont H-ban → minden hármasból pontosan egy → 3-színezés G-n

- **Ábraötlet:**
  - Bal: G kis gráf 3 csúccsal. Jobb: H-ban 3×3 csúcs, háromszögek és G-másolat éleivel; a kiválasztott független halmaz kiemelve

- **Előadói megjegyzés:**
  - Ez az egyik legtipikusabb NP-teljességi visszavezetés. Érdemes részletesen végigkövetni mind a két irányt (3-színezhetőből független, függetlenből 3-színezés).

---

## Slide 16: maxKLIKK – NP-teljesség

- **Bullet pontok:**
  - **maxKLIKK:** Adott (G, k) – van-e G-ben k pontú teljes részgráf (klikk)?
  - Klikk: minden két csúcs közt él van
  - maxKLIKK ∈ NP: tanúsítvány k csúcs felsorolása; T ellenőrzi, hogy minden pár össze van kötve
  - **maxFTL ≺ maxKLIKK:** f(G, k) = (Ḡ, k), ahol Ḡ a G komplementer gráfja
  - F független halmaz G-ben ⟺ F klikk Ḡ-ben

- **Képlet / definíció:**
  - (G, k) ∈ maxFTL ⟺ (Ḡ, k) ∈ maxKLIKK
  - Komplementer gráf: Ḡ = (V, Ē), ahol {u,v} ∈ Ē ⟺ {u,v} ∉ E

- **Ábraötlet:**
  - Bal: G gráf kiemelt független halmazsal. Jobb: Ḡ komplementer gráf, ugyanaz a halmaz most klikket alkot

- **Előadói megjegyzés:**
  - Ez az egyik „leglátványosabb" visszavezetés – egyetlen függvénnyel (komplementer) megkapjuk a kívántat. Jó példa arra, hogy a visszavezetések néha nagyon egyszerűek lehetnek.

---

## Slide 17: Gráfizomorfizmus és részgráf-izomorfizmus

- **Bullet pontok:**
  - **részgráfizó:** G₁-nek van G₂-vel izomorf részgráfja? → **NP-teljes** (6. tétel)
  - Bizonyítás: H ≺ részgráfizó visszavezetéssel (G → (Cₙ, G), ahol Cₙ n-csúcsú kör)
  - **grafizó:** G₁ ≅ G₂? → NP-ben van, de nem ismert, hogy NP-teljes-e, vagy P-ben van
  - A gráfizomorfizmus „titokzatos" probléma: nagy valószínűséggel sem P-ben, sem NP-teljesen nincs
  - A két probléma hasonlónak tűnik, de bonyolultságuk valószínűleg különbözik

- **Képlet / definíció:**
  - G ∈ H ⟺ (Cₙ, G) ∈ részgráfizó (ahol Cₙ n-csúcsú kör)

- **Ábraötlet:**
  - Két gráf és nyíl közöttük „izomorfizmus?" felirattal; mellette kör-gráf és Hamilton-kör kiemelése

- **Előadói megjegyzés:**
  - A részgráf-izomorfizmus és a gráfizomorfizmus közti különbség jó példa arra, hogy apró változtatás a problémadefinícióban drámaian megváltoztathatja a bonyolultságot.

---

## Slide 18: Nem gráfos NP-teljes problémák

- **Bullet pontok:**
  - **3DM (háromdimenziós párosítás):** Három egyenlő méretű halmaz (A, B, C); van-e tökéletes lefedés 3 elemű halmazokkal?
  - **X3C:** Egyetlen A alaphalmaz 3 elemű részhalmazaival – pontos lefedés lehetséges-e?
  - **RH (részhalmazösszeg):** Kiválasztható-e s₁…sₙ-ből néhány, amelyek összege pontosan b?
  - **PARTÍCIÓ:** Osztható-e két egyenlő összegű részre az s₁…sₙ sorozat?
  - **HÁTIZSÁK:** Adott súly- és értékkorláttal – csomagolható-e k értékű tárgy b súlykorlát alatt?

- **Képlet / definíció:**
  - HÁTIZSÁK: ∃ I ⊆ {1,…,n}: Σⱼ∈I sⱼ ≤ b és Σⱼ∈I vⱼ ≥ k

- **Ábraötlet:**
  - Hátizsák ábra: tárgyak súllyal és értékkel, a hátizsák kapacitása jelölve

- **Előadói megjegyzés:**
  - Fontos: 2DM (2-dimenziós párosítás) ∈ P, és X2C is P-ben van. Az egy dimenzióval több drasztikusan változtat a bonyolultságon – ez a bonyolultságelmélet egyik fontos tanulsága.

---

## Slide 19: Egészértékű programozás és lineáris programozás

- **Bullet pontok:**
  - **LP (lineáris programozás):** xⱼ valós értékű → P-ben van (hatékony algoritmusok léteznek)
  - **EP (egészértékű programozás):** xⱼ egész → NP-teljes
  - A legtöbb NP-teljes probléma megfogalmazható egészértékű programozásként
  - Példa: maxFTL → EP feladat (minden csúcshoz xᵢ ∈ {0,1}; él feltétel: xᵢ + xⱼ ≤ 1)
  - Egész megszorítás hozzáadása polinom → NP-teljes ugrást okozhat

- **Képlet / definíció:**
  - maxFTL-ből EP: max Σxᵢ, feltétel: xᵢ + xⱼ ≤ 1 minden {i,j} ∈ E-re, xᵢ ∈ {0, 1}

- **Ábraötlet:**
  - Két oszlop: bal „LP (valós)" → „P"; jobb „EP (egész)" → „NP-teljes"

- **Előadói megjegyzés:**
  - Az LP és EP közti különbség szemléletes: ha engedélyezzük a törtmegoldásokat, a feladat könnyűvé válik. Az egész megszorítás teszi nehézzé. Ez a felismerés motiválja a közelítő algoritmusok kutatását.

---

## Slide 20: Összefoglalás – 5 legfontosabb gondolat

- **Bullet pontok:**
  1. **P:** Hatékony (polinomiális) algoritmussal megoldható problémák osztálya
  2. **NP:** Ahol az *igen* válaszra van rövid, polinomidőben ellenőrizhető bizonyíték
  3. **P ⊆ NP ∩ coNP** – de P ?= NP a leghíresebb nyitott kérdés a számítástudományban
  4. **Karp-redukció (X ≺ Y):** Ha Y könnyű, X is könnyű; ha X nehéz, Y is nehéz
  5. **NP-teljes problémák:** Az NP legnehezebb problémái; egyetlen P-beli NP-teljes problémával P = NP következne

- **Képlet / definíció:**
  - P ⊆ NP ∩ coNP
  - X ≺ Y, Y ∈ P ⟹ X ∈ P
  - Z NP-teljes és Z ∈ P ⟹ P = NP

- **Ábraötlet:**
  - Végső összefoglaló halmazábra: P belső kör, NP és coNP metszőkörök, NP-teljes problémák a határon, NP-nehéz problémák kívül

- **Előadói megjegyzés:**
  - Zárszó: A P ?= NP kérdés megválaszolása nemcsak elméleti, hanem óriási gyakorlati jelentőségű lenne (kriptográfia, optimalizálás, mesterséges intelligencia). Addig az NP-teljességi bizonyítások azt jelzik: „valószínűleg nincs hatékony algoritmus" – és ez a tudás önmagában is értékes tervezési irányelv.

---

## A 20 slide áttekintése

| # | Téma |
|---|------|
| 1 | Hatékony algoritmus fogalma |
| 2 | Eldöntési problémák és példák |
| 3 | P osztály definíciója |
| 4 | Hatékony tanúsítvány |
| 5 | NP osztály definíciója |
| 6 | NP-beli példák (H, ÖSSZETETT, 3SZÍN) |
| 7 | Komplementer és coNP |
| 8 | P ?= NP kérdés |
| 9 | Karp-redukció definíciója |
| 10 | Karp-redukció tulajdonságai |
| 11 | NP-nehéz és NP-teljes definíciók |
| 12 | NP-teljességi bizonyítás sémája |
| 13 | 3-színezés NP-teljessége |
| 14 | maxFTL – független ponthalmaz |
| 15 | 3SZÍN ≺ maxFTL visszavezetés |
| 16 | maxKLIKK NP-teljessége |
| 17 | Részgráf-izomorfizmus |
| 18 | Nem gráfos NP-teljes problémák |
| 19 | LP vs. EP |
| 20 | Összefoglalás – 5 kulcsgondolat |
