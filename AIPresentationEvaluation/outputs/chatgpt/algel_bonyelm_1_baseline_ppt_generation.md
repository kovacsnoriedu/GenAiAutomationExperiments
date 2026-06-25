A vázlat kizárólag a feltöltött jegyzet tartalmára épül. 

## Slide 1: Miről szól a bonyolultságelmélet?

* Bullet pontok:

  * Hatékony algoritmusok vizsgálata
  * Eldöntési problémák: igen / nem válasz
  * P, NP, coNP alapfogalmak
  * Redukciók és NP-teljesség
* Képlet / definíció:

  * Hatékony: lépésszám ≤ polinom a bemenet hosszában
* Ábraötlet:

  * Útiterv-ábra: P → NP → coNP → redukció → NP-teljes
* Előadói megjegyzés:

  * Ezen a részen azt vizsgáljuk, mit jelent algoritmikusan „könnyűnek” vagy „nehéznek” lenni.

## Slide 2: Hatékony algoritmus és polinomidő

* Bullet pontok:

  * Egy algoritmus hatékony, ha polinom lépésszámú
  * A bemenet hossza számít, nem maga az érték
  * Exponenciális hosszú kimenet eleve gond
  * Rövid kimenet mellett is lehet nehéz probléma
* Képlet / definíció:

  * `f(n) = O(n^k)`, ahol `k` pozitív konstans
* Ábraötlet:

  * Két görbe: polinom növekedés vs exponenciális növekedés
* Előadói megjegyzés:

  * Fontos: nem az a kérdés, hogy „meg lehet-e oldani”, hanem hogy hatékonyan meg lehet-e oldani.

## Slide 3: Eldöntési problémák

* Bullet pontok:

  * A válasz 1 bit: igen vagy nem
  * Példák: prím, Hamilton-kör, út
  * A bemenetek halmazként is kezelhetők
  * Az „igen” példányok alkotják a problémához tartozó nyelvet
* Képlet / definíció:

  * `x ∈ X` azt jelenti: az `x` bemenetre a válasz igen
* Ábraötlet:

  * Halmazábra: minden bemenet, azon belül az „igen” bemenetek halmaza
* Előadói megjegyzés:

  * A jegyzet innentől eldöntési problémákkal dolgozik, mert ezekhez lehet tisztán definiálni P-t és NP-t.

## Slide 4: A P osztály definíciója

* Bullet pontok:

  * P: polinom időben eldönthető problémák
  * Van algoritmus, amely minden bemenetre helyesen válaszol
  * A futási idő `O(|x|^k)`
  * Példa: út ∈ P
* Képlet / definíció:

  * `X ∈ P`, ha létezik polinom idejű `A`, amely eldönti `X`-et
* Ábraötlet:

  * Doboz: bemenet `x` → polinom idejű algoritmus `A` → igen/nem
* Előadói megjegyzés:

  * P a „hatékonyan megoldható” eldöntési problémák osztálya.

## Slide 5: Példák P-re és nem ismert esetekre

* Bullet pontok:

  * `út ∈ P`: szélességi bejárással eldönthető
  * `prím ∈ P`, de ez sokáig nem volt ismert
  * Hamilton-körre nem ismert polinom idejű algoritmus
  * Speciális gráfosztályokra lehet hatékony megoldás
* Képlet / definíció:

  * `A(x) = igen / nem`
* Ábraötlet:

  * Három kártya: út = P, prím = P, Hamilton-kör = nem ismert P-ben
* Előadói megjegyzés:

  * Ez jól mutatja, hogy attól, hogy egy probléma egyszerűen megfogalmazható, még nem biztos, hogy könnyen megoldható.

## Slide 6: Hatékony tanúsítvány

* Bullet pontok:

  * Igen válaszhoz rövid bizonyíték tartozik
  * A bizonyíték polinom hosszú
  * Ellenőrizni polinom időben lehet
  * Nem válasznál nincs hamis elfogadható tanúsítvány
* Képlet / definíció:

  * Ha `x ∈ X`, akkor van `t`, ahol `|t| = O(|x|^c)` és `T(x,t)=igen`
* Ábraötlet:

  * Folyamatábra: `x` + tanúsítvány `t` → ellenőrző algoritmus `T` → igen/nem
* Előadói megjegyzés:

  * A kulcsgondolat: lehet, hogy megtalálni nehéz, de ellenőrizni könnyű.

## Slide 7: Az NP osztály

* Bullet pontok:

  * NP: problémák hatékony tanúsítvánnyal
  * Az „igen” válasz gyorsan ellenőrizhető
  * A tanúsítványt nem feltétlenül tudjuk gyorsan megtalálni
  * A próbálgatás exponenciális lehet
* Képlet / definíció:

  * `NP = {X : X-hez van hatékony tanúsítvány}`
* Ábraötlet:

  * „Megsejtés” → „ellenőrzés” folyamatábra
* Előadói megjegyzés:

  * Az NP nem azt jelenti, hogy „nem polinom”, hanem azt, hogy van polinom idejű ellenőrzés.

## Slide 8: NP-példák: Hamilton-kör, összetett, 3-szín

* Bullet pontok:

  * Hamilton-körnél tanúsítvány: csúcsok sorrendje
  * Összetett számnál tanúsítvány: valódi osztó
  * 3-színezésnél tanúsítvány: színezési sorozat
  * Mindegyik ellenőrizhető polinom időben
* Képlet / definíció:

  * 3-szín tanúsítvány: `t ∈ {1,2,3}^{|V|}`
* Ábraötlet:

  * Három kis ikon: körút, osztó, színezett gráf
* Előadói megjegyzés:

  * Ezekben közös, hogy a megoldás „jelöltjét” könnyű leellenőrizni.

## Slide 9: A 3-színezés mint tanúsítványos probléma

* Bullet pontok:

  * Bemenet: irányítatlan egyszerű gráf
  * Kérdés: színezhető-e 3 színnel?
  * Tanúsítvány: minden csúcshoz egy szín
  * Ellenőrzés: szomszédos csúcsok nem lehetnek azonos színűek
* Képlet / definíció:

  * Ha `t_i = t_j`, akkor `{v_i, v_j} ∉ E`
* Ábraötlet:

  * Kis gráf három színnel; hibás él kiemelve, ha két végpont azonos színű
* Előadói megjegyzés:

  * Itt nagyon szemléletes az NP: a jó színezést nem biztos, hogy könnyű megtalálni, de ha megvan, gyorsan ellenőrizhető.

## Slide 10: Komplementer probléma és coNP

* Bullet pontok:

  * Komplementer probléma: ugyanaz a bemenet, ellentétes válasz
  * `összetett` komplementere: `prím`
  * coNP: NP-beli problémák komplementereiből áll
  * coNP-ben a „nem” válasz tanúsítható hatékonyan
* Képlet / definíció:

  * `x ∈ X̄ ⇔ x ∉ X`
  * `X ∈ coNP ⇔ X̄ ∈ NP`
* Ábraötlet:

  * Két részre osztott halmaz: X és komplementere
* Előadói megjegyzés:

  * NP az igen válasz ellenőrizhetőségéről szól, coNP pedig a nem válasz ellenőrizhetőségéről.

## Slide 11: P kapcsolata NP-vel és coNP-vel

* Bullet pontok:

  * Minden P-beli probléma NP-ben is van
  * Minden P-beli probléma coNP-ben is van
  * Ha van polinom algoritmus, tanúsítvány sem kell
  * Ilyenkor vehetjük `|t| = 0`
* Képlet / definíció:

  * `P ⊆ NP` és `P ⊆ coNP`
* Ábraötlet:

  * Halmazábra: P az NP és coNP metszetének részeként
* Előadói megjegyzés:

  * Ha meg tudjuk oldani a problémát gyorsan, akkor természetesen az igen és nem válasz is gyorsan igazolható.

## Slide 12: A P ?= NP kérdés

* Bullet pontok:

  * Nyitott alapkérdés: `P ?= NP`
  * Ellenőrzés könnyebb lehet, mint megtalálás
  * Sok nevezetes probléma bonyolultsága ettől függ
  * A jegyzet említi a Clay-díjat is
* Képlet / definíció:

  * `P ?= NP`
  * `P ?= NP ∩ coNP`
* Ábraötlet:

  * Két alternatív halmazábra: `P = NP` vs `P ⊂ NP`
* Előadói megjegyzés:

  * Ez a témakör központi kérdése: vajon minden gyorsan ellenőrizhető probléma gyorsan meg is oldható?

## Slide 13: Karp-redukció

* Bullet pontok:

  * Két eldöntési probléma összehasonlítására szolgál
  * `X` bemenetét átalakítjuk `Y` bemenetévé
  * Az átalakítás polinom idejű
  * Az igen/nem válasznak meg kell maradnia
* Képlet / definíció:

  * `X ≺ Y`, ha van polinom idejű `f`, hogy `x ∈ X ⇔ f(x) ∈ Y`
* Ábraötlet:

  * Redukciós nyíl: `x` —f→ `f(x)`, alatta: `X ≺ Y`
* Előadói megjegyzés:

  * Ha `X ≺ Y`, akkor `Y` legalább olyan nehéz, mint `X`, mert `Y` megoldásával `X` is megoldható.

## Slide 14: Mit adnak a redukciók?

* Bullet pontok:

  * Ha `Y ∈ P` és `X ≺ Y`, akkor `X ∈ P`
  * Ha `Y ∈ NP` és `X ≺ Y`, akkor `X ∈ NP`
  * Ha `Y ∈ coNP` és `X ≺ Y`, akkor `X ∈ coNP`
  * A redukció tranzitív
* Képlet / definíció:

  * Ha `X ≺ Y` és `Y ≺ Z`, akkor `X ≺ Z`
* Ábraötlet:

  * Lánc: `X → Y → Z`, majd összevonva `X → Z`
* Előadói megjegyzés:

  * A tranzitivitás miatt lehet NP-teljességi bizonyításokat láncolni.

## Slide 15: NP-nehéz és NP-teljes

* Bullet pontok:

  * NP-nehéz: minden NP-beli probléma visszavezethető rá
  * NP-teljes: NP-nehéz és maga is NP-ben van
  * Ezek az NP legnehezebb problémái
  * Egy NP-teljes probléma P-ben lenne → minden NP-beli probléma P-ben lenne
* Képlet / definíció:

  * NP-nehéz: minden `X ∈ NP` esetén `X ≺ Z`
  * NP-teljes: `Z ∈ NP` és `Z` NP-nehéz
* Ábraötlet:

  * NP halmazban kiemelt „legnehezebb” régió: NP-teljes problémák
* Előadói megjegyzés:

  * Az NP-teljesség azért fontos, mert egyetlen ilyen probléma hatékony megoldása az egész NP osztályt érintené.

## Slide 16: NP-teljességi bizonyítási séma

* Bullet pontok:

  * Először belátjuk: `Z ∈ NP`
  * Ezután választunk egy ismert NP-teljes `Y` problémát
  * Megmutatjuk: `Y ≺ Z`
  * A tranzitivitás miatt `Z` NP-nehéz lesz
* Képlet / definíció:

  * `Y` NP-teljes és `Y ≺ Z` ⇒ `Z` NP-nehéz
* Ábraötlet:

  * Bizonyítási sablon két lépésben
* Előadói megjegyzés:

  * A jegyzet kiindulásként bizonyítás nélkül elfogadja, hogy a 3-szín NP-teljes.

## Slide 17: A 3-szín probléma szerepe

* Bullet pontok:

  * 3-szín: a csúcsok színezhetők-e 3 színnel?
  * A jegyzet szerint NP-teljes
  * Kiindulópont további bizonyításokhoz
  * 2-szín ezzel szemben P-ben van
* Képlet / definíció:

  * Tétel: `3szín` NP-teljes
* Ábraötlet:

  * Két egymás melletti gráf: 2-színezés vs 3-színezés
* Előadói megjegyzés:

  * Ez jó kontraszt: egy látszólag kis változás — 2 szín helyett 3 — teljesen más bonyolultsági helyzetet ad.

## Slide 18: Maximális független ponthalmaz – maxftl

* Bullet pontok:

  * Eldöntési változatot használunk
  * Bemenet: `(G, k)`
  * Kérdés: van-e `k` darab független csúcs?
  * Ha ezt tudnánk polinom időben, bináris kereséssel a maximum mérete is meghatározható lenne
* Képlet / definíció:

  * `maxftl`: van-e `G`-ben `k` független csúcs?
* Ábraötlet:

  * Gráfban kiemelt csúcsok, amelyek között nincs él
* Előadói megjegyzés:

  * Itt látszik, miért fordítjuk az optimalizálási problémát eldöntési problémává.

## Slide 19: 3szín ≺ maxftl

* Bullet pontok:

  * A jegyzet redukciót ad: `3szín ≺ maxftl`
  * Egy `n` csúcsú `G` gráfból `H` készül `3n` csúccsal
  * Minden eredeti csúcshoz három másolat: `a_i, b_i, c_i`
  * A cél: `H`-ban legyen `n` független csúcs
* Képlet / definíció:

  * `G ∈ 3szín ⇔ (H,n) ∈ maxftl`
* Ábraötlet:

  * Három rétegű gráf: `a`, `b`, `c` példányok; egy csúcshármas háromszöggel összekötve
* Előadói megjegyzés:

  * A három másolat a három színnek felel meg. Egy független halmaz minden eredeti csúcsból pontosan egy „színt” választ.

## Slide 20: Maxklikk és az 5 legfontosabb gondolat

* Bullet pontok:

  * `maxklikk`: van-e `k` pontú teljes részgráf?
  * `maxklikk ∈ NP`
  * Redukció: `maxftl ≺ maxklikk`
  * Komplementer gráfban a független halmaz klikké válik
* Képlet / definíció:

  * `(G,k) ∈ maxftl ⇔ (Ḡ,k) ∈ maxklikk`
* Ábraötlet:

  * Egy gráf és komplementere egymás mellett; balra független halmaz, jobbra klikk
* Előadói megjegyzés:

  * Zárásként emeld ki:

    1. P = hatékonyan megoldható.
    2. NP = hatékonyan ellenőrizhető igen válasz.
    3. coNP = hatékonyan ellenőrizhető nem válasz.
    4. Karp-redukcióval nehézséget viszünk át.
    5. NP-teljes problémák az NP osztály központi, legnehezebb problémái.
