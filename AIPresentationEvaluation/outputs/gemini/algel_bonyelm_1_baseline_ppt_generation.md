Íme egy 20 slide-os prezentációvázlat az egyetemi hallgatók számára, a megadott PDF anyaga alapján.

---

## Slide 1: Bevezetés a bonyolultságelméletbe

* Bullet pontok:
    * Az algoritmuselmélet alapvető kérdése: mi számít „hatékony” megoldásnak?
    * Lépésszám becslése a bemenet hossza ($n$) függvényében.
    * A kimenet hossza korlátozza a hatékonyságot.
    * Fókuszban: az eldöntési problémák.
* Képlet / definíció:
    * Hatékony algoritmus: $f(n) = O(n^k)$ valamilyen $k$ pozitív konstansra.
* Ábraötlet:
    * Egy táblázat, amely összehasonlítja a bemenet hosszát ($n$) és a lépésszámot különböző függvényeknél ($n$, $n^2$, $2^n$).
* Előadói megjegyzés:
    * Üdvözlöm a hallgatókat! Ma a P és NP osztályok világába lépünk be. Fontos megérteni, hogy elméleti szempontból a polinomiális időt tekintjük hatékonynak. Ha a kimenet maga exponenciális (pl. $2^x$ kiszámítása), az algoritmus már csak a kiírás miatt sem lehet hatékony.

## Slide 2: Eldöntési problémák

* Bullet pontok:
    * Csak olyan feladatokkal foglalkozunk, ahol a válasz 1 bit (igen/nem).
    * Bemenet: szavak (egy nyelv elemei).
    * Kimenet: Igen, ha a bemenet a nyelv része, különben Nem.
* Képlet / definíció:
    * $L = \{x \mid \text{a válasz igen } x\text{-re}\}$.
* Ábraötlet:
    * Egy fekete doboz (algoritmus), amibe bemegy egy $x$ sztring, és kijön egy „Igen” vagy „Nem” jelzés.
* Előadói megjegyzés:
    * Az eldöntési problémák egyszerűsítik az elméleti vizsgálatot anélkül, hogy csorbítanák az általánosságot. Példák: Egy szám prím? Van-e út két csúcs között?

## Slide 3: Példák eldöntési problémákra

* Bullet pontok:
    * **PRÍM**: $m > 0$ egész szám prím-e?
    * **H** (Hamilton-kör): Van-e a $G$ gráfban minden csúcsot pontosan egyszer érintő kör?
    * **ÚT**: Van-e út $s$ és $t$ csúcs között a $G$ gráfban?
* Képlet / definíció:
    * $x \in X$: az $x$ bemenetre a válasz **igen**.
* Ábraötlet:
    * Egy gráf rajza, rajta kiemelve egy Hamilton-kör (H) és egy $s-t$ út (ÚT).
* Előadói megjegyzés:
    * Vegyük észre a különbséget: az ÚT probléma egyszerű, a Hamilton-körre viszont nem ismerünk hatékony algoritmust általános esetben.

## Slide 4: A P osztály definíciója

* Bullet pontok:
    * Azon problémák halmaza, amelyek „könnyen” megoldhatók.
    * Létezik polinomiális lépésszámú determinisztikus algoritmus.
    * A futási idő $O(|x|^k)$.
* Képlet / definíció:
    * $P = \{ X \mid \exists A \text{ algoritmus, ami } x\text{-et } O(|x|^k) \text{ időben eldönti}\}$.
* Ábraötlet:
    * Egy nagy kör, ami a P osztályt jelöli, benne az ÚT és a PRÍM feliratokkal.
* Előadói megjegyzés:
    * A P osztály a gyakorlatban jól kezelhető problémákat takarja. Fontos: a PRÍM probléma 2002 óta bizonyítottan a P része!

## Slide 5: A hatékony tanúsítvány fogalma

* Bullet pontok:
    * Mi van akkor, ha a megoldást nehéz megtalálni, de könnyű ellenőrizni?
    * Tanúsítvány ($t$): egy rövid „bizonyíték”, ami alátámasztja az „igen” választ.
    * Az ellenőrző algoritmus ($T$) polinomiális.
* Képlet / definíció:
    * $T(x, t) = \text{igen}$, ha $x \in X$ és $t$ egy érvényes tanúsítvány.
* Ábraötlet:
    * Folyamatábra: [Bemenet $x$ + Tanúsítvány $t$] $\rightarrow$ [Ellenőrző Algoritmus $T$] $\rightarrow$ Igen/Nem.
* Előadói megjegyzés:
    * Gondoljanak a Sudokura: megoldani nehéz, de ha valaki kitöltve adja oda, pillanatok alatt ellenőrizhető, hogy jó-e.

## Slide 6: Az NP osztály definíciója

* Bullet pontok:
    * **N**on-deterministic **P**olynomial time.
    * Azon problémák, amelyekhez létezik hatékony (polinomiális) tanúsítvány.
    * Fontos: Ha a válasz „nem”, akkor nincs olyan tanúsítvány, amivel át lehetne verni az ellenőrt.
* Képlet / definíció:
    * $NP = \{ X \mid \exists T \text{ polinomiális ellenőrző algoritmus és } c, k \text{ konstansok} \}$.
* Ábraötlet:
    * Egy Venn-diagram, ahol az NP egy nagyobb halmaz, ami tartalmazza P-t.
* Előadói megjegyzés:
    * Az NP nem a „nem polinomiális” rövidítése! A név onnan ered, hogy egy nemdeterminisztikus gép „megsejtheti” a jó tanúsítványt.

## Slide 7: Példák NP-beli problémákra

* Bullet pontok:
    * **H (Hamilton-kör)**: Tanúsítvány a csúcsok egy sorrendje.
    * **ÖSSZETETT**: Tanúsítvány egy valódi osztó.
    * **3SZÍN**: Tanúsítvány a csúcsok 3-színezése (számhármasok sorozata).
* Képlet / definíció:
    * $|t| = O(|x|^c)$ (a tanúsítvány hossza polinomiális).
* Ábraötlet:
    * Gráf 3-színezéssel ellátva – látható, hogy ha megvan a színezés, csak az éleket kell ellenőrizni.
* Előadói megjegyzés:
    * Mindhárom esetben igaz: ha valaki „súg” (megadja a kört, az osztót vagy a színezést), polinomiális időben meggyőződhetünk az igazságról.

## Slide 8: Keresés vs. Ellenőrzés

* Bullet pontok:
    * Ha egy problémára van hatékony tanúsítvány, az sugall egy algoritmust.
    * Próbáljuk végig az összes lehetséges $t$ tanúsítványt!
    * Probléma: a tanúsítványok száma exponenciális ($2^n$).
* Képlet / definíció:
    * Lehetséges $t$-k száma: $2^{|x|^c}$.
* Ábraötlet:
    * Egy elágazó fa, ahol az ágak végén vannak a tanúsítványok – szemléltetve a keresési tér robbanásszerű növekedését.
* Előadói megjegyzés:
    * Ezért nem tudjuk egyelőre, hogy $P=NP$ -e. Az ellenőrzés gyors, de a keresés (brute force) lassú.

## Slide 9: A komplementer probléma és a coNP osztály

* Bullet pontok:
    * $\overline{X}$ probléma: ugyanaz a bemenet, de a válasz ellentétes.
    * coNP: azon problémák, ahol a „nem” válaszhoz van hatékony tanúsítvány.
    * Példa: $\overline{PRÍM} = ÖSSZETETT$.
* Képlet / definíció:
    * $coNP = \{ X \mid \overline{X} \in NP \}$.
* Ábraötlet:
    * Halmazábra: NP és coNP, középen a metszetükkel.
* Előadói megjegyzés:
    * Ha egy szám nem prím, van rá tanúsítvány (egy osztó). De ha egy gráfban *nincs* Hamilton-kör, arra vajon van-e rövid bizonyíték? Ez nem egyértelmű.

## Slide 10: Kapcsolat a P, NP és coNP között

* Bullet pontok:
    * Minden P-beli probléma NP-beli is ($P \subseteq NP$).
    * Minden P-beli probléma coNP-beli is ($P \subseteq coNP$).
    * Bizonyítás: A tanúsítvány lehet üres, az algoritmus maga dönti el a választ.
* Képlet / definíció:
    * $P \subseteq NP \cap coNP$.
* Ábraötlet:
    * Euler-diagram: P kör legbelül, körülötte az NP $\cap$ coNP metszet.
* Előadói megjegyzés:
    * Ha egy feladat P-ben van, akkor mind az „igen”, mind a „nem” válasz könnyen indokolható: lefut az algoritmus és megadja a választ.

## Slide 11: A P ?= NP kérdés

* Bullet pontok:
    * A számítástudomány legfontosabb nyitott kérdése.
    * Egyenértékű-e a megoldás megtalálása az ellenőrzéssel?
    * Clay Mathematics Institute: 1 millió dolláros díj a megoldásért.
* Képlet / definíció:
    * $P \stackrel{?}{=} NP$.
* Ábraötlet:
    * Két lehetséges világ: (1) $P = NP$ (egybeolvadó halmazok), (2) $P \subset NP$ (elkülönülő halmazok).
* Előadói megjegyzés:
    * A legtöbb kutató szerint $P \neq NP$, azaz a keresés lényegesen nehezebb, mint az ellenőrzés.

## Slide 12: Karp-redukció (Polinomiális visszavezetés)

* Bullet pontok:
    * Problémák nehézségének összehasonlítása.
    * $X$ visszavezethető $Y$-ra, ha $X$ példányai átalakíthatók $Y$ példányaivá.
    * A transzformáció ($f$) polinomiális idejű.
* Képlet / definíció:
    * $x \in X \iff f(x) \in Y$, jelölése: $X \prec Y$.
* Ábraötlet:
    * Nyíl: $X \xrightarrow{f} Y$. „Ha meg tudod oldani $Y$-t, meg tudod oldani $X$-et is.”
* Előadói megjegyzés:
    * A redukció olyan, mint egy tolmács. Ha tudok magyarul (X), de a feladat angol (Y), kell egy fordító (f).

## Slide 13: A redukció tulajdonságai

* Bullet pontok:
    * **Tranzitivitás**: Ha $X \prec Y$ és $Y \prec Z$, akkor $X \prec Z$.
    * Ha $Y \in P$ és $X \prec Y$, akkor $X \in P$.
    * Ha $Y \in NP$ és $X \prec Y$, akkor $X \in NP$.
* Képlet / definíció:
    * $X \prec Y$ azt jelenti, hogy $Y$ legalább olyan nehéz, mint $X$.
* Ábraötlet:
    * Dominó-elv: ha az utolsó eldől (megoldható), az előtte lévők is eldőlnek.
* Előadói megjegyzés:
    * Ez egy kulcsfontosságú eszköz: ha találunk egy nagyon nehéz problémát az NP-ben, amire minden más visszavezethető, az lesz az NP-teljes probléma.

## Slide 14: NP-nehézség és NP-teljesség

* Bullet pontok:
    * **NP-nehéz**: legalább olyan nehéz, mint bármelyik NP-beli probléma.
    * **NP-teljes**: az NP osztály „legnehezebb” problémái (NP-ben van + NP-nehéz).
    * Ha egyetlen NP-teljes problémára találnánk polinomiális algoritmust, akkor $P=NP$ lenne.
* Képlet / definíció:
    * $Z \text{ NP-teljes, ha } Z \in NP \text{ és } \forall X \in NP: X \prec Z$.
* Ábraötlet:
    * Az NP halmaz „tetején” lévő tartomány kiemelve az NP-teljes feliratnak.
* Előadói megjegyzés:
    * Stephen Cook és Leonid Levin bizonyították be az első ilyen probléma létezését az 1970-es évek elején.

## Slide 15: Hogyan bizonyítjuk az NP-teljességet?

* Bullet pontok:
    * 1. Belátjuk, hogy $Z \in NP$ (van hatékony tanúsítvány).
    * 2. Kiválasztunk egy *ismerten* NP-teljes $Y$ problémát.
    * 3. Megmutatjuk, hogy $Y \prec Z$ (Karp-redukció).
* Képlet / definíció:
    * $Y \text{ NP-teljes } \land Y \prec Z \land Z \in NP \implies Z \text{ NP-teljes}$.
* Ábraötlet:
    * Láncolat: Cook-Levin tétel $\rightarrow$ 3SZÍN $\rightarrow$ MAXFTL $\rightarrow$ MAXKLIKK.
* Előadói megjegyzés:
    * Kiindulópontunk a 3SZÍN (3-színezhetőség), amit bizonyítás nélkül NP-teljesnek fogadunk el ebben a kurzusban.

## Slide 16: MAXFTL – Független ponthalmaz

* Bullet pontok:
    * **Bemenet**: $(G, k)$ pár, ahol $G$ gráf és $k$ egész.
    * **Kérdés**: Van-e $G$-ben $k$ darab független csúcs (közöttük nincs él)?
    * A döntési változat NP-teljes.
* Képlet / definíció:
    * $MAXFTL \in NP$. Tanúsítvány: a $k$ darab csúcs listája.
* Ábraötlet:
    * Gráf, ahol néhány nem szomszédos csúcs ki van színezve (ők alkotják a független halmazt).
* Előadói megjegyzés:
    * Fontos: az optimalizálási feladat (mekkora a *legnagyobb* független halmaz?) és az eldöntési feladat (van-e legalább $k$ méretű?) szorosan összefügg.

## Slide 17: Redukció: 3SZÍN ≺ MAXFTL

* Bullet pontok:
    * Vegyünk egy $G$ gráfot $n$ csúccsal.
    * Készítsünk egy $H$ gráfot $3n$ csúccsal (minden eredeti csúcshoz 3 másolat: $a_i, b_i, c_i$).
    * Élek: minden másolathármas között, plusz az eredeti éleknek megfelelő élek a másolatok között.
* Képlet / definíció:
    * $G \in 3SZÍN \iff (H, n) \in MAXFTL$.
* Ábraötlet:
    * „Gadget” ábra: egy $v_i$ csúcsból hogyan lesz egy kis háromszög $H$-ban.
* Előadói megjegyzés:
    * A redukció lényege: a független halmazba minden csúcs-hármasból pontosan egy csúcs kerülhet be, ez felel meg a színezésnek.

## Slide 18: MAXKLIKK – Teljes részgráf

* Bullet pontok:
    * **Bemenet**: $(G, k)$ pár.
    * **Kérdés**: Van-e a gráfban $k$ méretű teljes részgráf (mindenki mindenkivel össze van kötve)?
    * Szoros kapcsolat a MAXFTL problémával.
* Képlet / definíció:
    * $(G, k) \in MAXFTL \iff (\overline{G}, k) \in MAXKLIKK$.
* Ábraötlet:
    * Egy gráf és a komplementere ($\overline{G}$) egymás mellett. Mutassuk meg, hogy ahol nincs él az egyikben, ott van a másikban.
* Előadói megjegyzés:
    * A MAXKLIKK is NP-teljes, mert a független halmaz probléma komplementer gráfra nézve pontosan a klikk probléma.

## Slide 19: További NP-teljes problémák

* Bullet pontok:
    * **RÉSZGRÁFIZO**: $G_1$ izomorf-e $G_2$ egy részgráfjával?
    * **RH (Részhalmazösszeg)**: Kiválasztható-e számok egy halmazából olyan részhalmaz, aminek az összege pontosan $b$?
    * **HÁTIZSÁK**: Pakoljunk be tárgyakat korlátozott súlykeretbe, maximális értékkel.
    * **EP (Egészértékű programozás)**: Lineáris egyenlőtlenség-rendszer megoldása egészeken.
* Képlet / definíció:
    * $LP \in P$ (lineáris programozás), de $EP \in NP$-teljes.
* Ábraötlet:
    * Képek: hátizsák, számhalmaz, két egymásba rajzolt gráf.
* Előadói megjegyzés:
    * Látható, hogy az NP-teljes problémák a matematika és az informatika minden területén előfordulnak.

## Slide 20: Összefoglaló

* Bullet pontok:
    * **P**: hatékonyan megoldható.
    * **NP**: hatékonyan ellenőrizhető.
    * **Karp-redukció**: „legalább olyan nehéz, mint...”
    * **NP-teljesség**: az NP legnehezebb feladatai.
    * Nyitott kérdés: $P = NP$? (valószínűleg nem).
* Ábraötlet:
    * Egy záró halmazábra P, NP, coNP és az NP-teljes problémák helyével.
* Előadói megjegyzés:
    * Gratulálok! Megismerték az elméleti számítástudomány alapköveit. A következő órán specifikus redukciókkal foglalkozunk.

---

### Az 5 legfontosabb gondolat a hallgatóknak:

1.  **Polinomiális idő = Hatékonyság:** Az algoritmuselméletben azokat a feladatokat tekintjük megoldottnak, amelyekre létezik $O(n^k)$ idejű algoritmus (ez a **P** osztály).
2.  **Az ellenőrzés ereje:** Az **NP** osztályba azok a problémák tartoznak, ahol egy „igen” válasz helyessége polinomiális időben igazolható egy tanúsítvány segítségével.
3.  **A redukció mint mérőeszköz:** A **Karp-redukció ($X \prec Y$)** lehetővé teszi, hogy kimondjuk: „ha $Y$ megoldható, akkor $X$ is”, azaz $Y$ legalább olyan nehéz, mint $X$.
4.  **NP-teljesség:** Vannak olyan „univerzális” problémák az NP-ben (pl. 3-színezés, Klikk), amelyekre minden más NP-beli feladat visszavezethető. Ha egyet megoldunk P-ben, az összeset megoldottuk.
5.  **P vs NP:** Jelenleg nem tudjuk, hogy $P=NP$-e, de a gyakorlatban az NP-teljes problémákra nem ismerünk hatékony algoritmust, így ezeket „nehéznek” tekintjük.