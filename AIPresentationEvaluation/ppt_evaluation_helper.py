"""
ppt_evaluation_helper.py

Parancssoros segédprogram MI-alapú prezentációgenerálás értékeléséhez.
A kísérlet során: ugyanazt a forrásanyagot adod be különböző AI eszközöknek,
majd az eredményeket ezzel a programmal pontozod kézzel, 1–5 skálán.

Nem hív meg semmilyen AI API-t. Az értékelő adatokat a felhasználó adja meg.

Használat:
  python ppt_evaluation_helper.py                       # Új értékelés rögzítése
  python ppt_evaluation_helper.py --summary             # Összefoglaló a konzolon
  python ppt_evaluation_helper.py --export <fájl.md>    # Összefoglaló mentése
  python ppt_evaluation_helper.py --list                # Értékelések listázása
  python ppt_evaluation_helper.py --csv <fájl.csv>      # Egyedi CSV fájl megadása

Alapértelmezett CSV: results/results.csv
"""

import csv
import os
import sys
import argparse
import statistics
from datetime import datetime

DEFAULT_CSV = os.path.join("results", "results.csv")

FIELDNAMES = [
    "timestamp",
    "ai_tool",
    "source_material",
    "prompt_type",
    "slide_count",
    "score_accuracy",
    "score_source_fidelity",
    "score_structure",
    "score_narrative",
    "score_text_volume",
    "score_design",
    "score_visuals",
    "score_speaker_notes",
    "score_post_work",
    "score_overall",
    "average_score",
    "notes",
]

SCORE_FIELDS = [
    ("score_accuracy",        "1.  Tartalmi pontosság           (helyes és releváns-e a tartalom?)"),
    ("score_source_fidelity", "2.  Forráshűség                  (csak a forrásból dolgozik-e?)"),
    ("score_structure",       "3.  Struktúra                    (van bevezető, tartalom, záró?)"),
    ("score_narrative",       "4.  Logikai ív / narratíva       (egymásra épülnek-e a slide-ok?)"),
    ("score_text_volume",     "5.  Szövegmennyiség              (megfelelő sűrűségű-e a szöveg?)"),
    ("score_design",          "6.  Design / vizuális javaslatok (hasznos elrendezési ötletek?)"),
    ("score_visuals",         "7.  Képek és diagramok           (konkrét vizuális elemjavaslatok?)"),
    ("score_speaker_notes",   "8.  Előadói jegyzetek            (hasznosak és részletesek-e?)"),
    ("score_post_work",       "9.  Emberi utómunka              (5 = kevés utómunka szükséges)"),
    ("score_overall",         "10. Összesített használhatóság   (megérte az AI-t használni?)"),
]

PROMPT_TYPES = [
    "1_baseline",
    "2_strukturalt",
    "3_forrashuseg",
    "4_design",
    "5_slide_ready",
    "6_javito",
    "7_ertekelo",
    "egyeb",
]


def ensure_csv(csv_path):
    os.makedirs(os.path.dirname(csv_path) or ".", exist_ok=True)
    if not os.path.exists(csv_path):
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_all(csv_path):
    ensure_csv(csv_path)
    rows = []
    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def append_row(csv_path, row):
    ensure_csv(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(row)


def ask(prompt_text, validator=None, default=None):
    while True:
        suffix = f" [{default}]" if default is not None else ""
        raw = input(f"{prompt_text}{suffix}: ").strip()
        if raw == "" and default is not None:
            return default
        if validator:
            result = validator(raw)
            if result is not None:
                return result
            print("  -> Érvénytelen érték, próbáld újra.")
        else:
            if raw:
                return raw
            print("  -> Ez a mező kötelező.")


def validate_int_range(low, high):
    def _v(s):
        try:
            v = int(s)
            if low <= v <= high:
                return v
        except ValueError:
            pass
        return None
    return _v


def collect_evaluation():
    print("\n" + "=" * 60)
    print("  MI Prezentáció Értékelő – Új értékelés rögzítése")
    print("=" * 60)
    print("  Részletes szempontleírás: evaluation_criteria.md\n")

    ai_tool = ask("AI eszköz neve (pl. ChatGPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro)")

    source_material = ask("Forrásanyag neve (pl. sample_source_text, digitalis_transzformacio)")

    print(f"  Elérhető prompt típusok: {', '.join(PROMPT_TYPES)}")
    prompt_type = ask("Prompt típus", default="1_baseline")

    slide_count = ask("Generált slide-ok száma a vázlatban", validator=validate_int_range(1, 200))

    print("\n  Pontszámok: 1 (gyenge/nem teljesíti) – 5 (kiváló/azonnal használható)")
    print("  Ha egy szempont nem alkalmazható (pl. design prompt nélkül a design szempont),")
    print("  írd be: 0 – ez kizárásra kerül az átlagból.\n")

    scores = {}
    for key, label in SCORE_FIELDS:
        val = ask(f"  {label} [0-5]", validator=validate_int_range(0, 5))
        scores[key] = val

    scored_values = [v for v in scores.values() if v > 0]
    avg = round(statistics.mean(scored_values), 2) if scored_values else 0.0

    notes = input("\nMegjegyzés (opcionális, Enter a kihagyáshoz): ").strip()

    row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ai_tool": ai_tool,
        "source_material": source_material,
        "prompt_type": prompt_type,
        "slide_count": slide_count,
        **scores,
        "average_score": avg,
        "notes": notes,
    }

    print(f"\n  Átlagos összpontszám (0-ok nélkül): {avg}/5.00")
    return row


def build_summary(rows):
    if not rows:
        return "Még nincsenek rögzített értékelések.\n"

    lines = []
    lines.append("# MI Prezentációgenerálás – Értékelési összefoglaló\n")
    lines.append(f"*Generálva: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    lines.append(f"**Összes értékelés:** {len(rows)}\n")

    lines.append("## Összes értékelés\n")
    col_heads = "| # | AI eszköz | Forrásanyag | Prompt | Slide | Pont. | Forr. | Strukt. | Narr. | Szöveg | Design | Vizuál | Előadói | Utóm. | Össz. | Átlag | Megjegyzés |"
    col_sep =   "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"
    lines.append(col_heads)
    lines.append(col_sep)
    for i, r in enumerate(rows, 1):
        lines.append(
            f"| {i} | {r.get('ai_tool','')} | {r.get('source_material','')} | {r.get('prompt_type','')} "
            f"| {r.get('slide_count','')} "
            f"| {r.get('score_accuracy','')} | {r.get('score_source_fidelity','')} "
            f"| {r.get('score_structure','')} | {r.get('score_narrative','')} "
            f"| {r.get('score_text_volume','')} | {r.get('score_design','')} "
            f"| {r.get('score_visuals','')} | {r.get('score_speaker_notes','')} "
            f"| {r.get('score_post_work','')} | {r.get('score_overall','')} "
            f"| **{r.get('average_score','')}** | {r.get('notes','')} |"
        )
    lines.append("")

    # Per-tool averages
    tools = {}
    for r in rows:
        t = r.get("ai_tool", "ismeretlen")
        tools.setdefault(t, []).append(r)

    lines.append("## Eszközönkénti átlagok\n")
    avg_cols = "| AI eszköz | db | Pont. | Forr. | Strukt. | Narr. | Szöveg | Design | Vizuál | Előadói | Utóm. | Össz. | **Átlag** |"
    avg_sep  = "|---|---|---|---|---|---|---|---|---|---|---|---|---|"
    lines.append(avg_cols)
    lines.append(avg_sep)

    score_keys = [k for k, _ in SCORE_FIELDS]

    for tool, tool_rows in sorted(tools.items()):
        def tool_avg(key):
            vals = [float(r[key]) for r in tool_rows if r.get(key) and float(r.get(key, 0)) > 0]
            return round(statistics.mean(vals), 2) if vals else "–"

        cols = " | ".join(str(tool_avg(k)) for k in score_keys)
        avg_val = tool_avg("average_score")
        lines.append(f"| {tool} | {len(tool_rows)} | {cols} | **{avg_val}** |")
    lines.append("")

    # Best and worst
    try:
        valid = [r for r in rows if r.get("average_score")]
        if valid:
            best = max(valid, key=lambda r: float(r["average_score"]))
            worst = min(valid, key=lambda r: float(r["average_score"]))
            lines.append("## Kiemelések\n")
            lines.append(
                f"- **Legjobb értékelés:** {best['ai_tool']} – {best.get('source_material','')} "
                f"({best.get('prompt_type','')}, átlag: {best['average_score']})"
            )
            lines.append(
                f"- **Leggyengébb értékelés:** {worst['ai_tool']} – {worst.get('source_material','')} "
                f"({worst.get('prompt_type','')}, átlag: {worst['average_score']})"
            )
            lines.append("")
    except (ValueError, KeyError):
        pass

    return "\n".join(lines)


def cmd_list(rows):
    if not rows:
        print("Még nincsenek rögzített értékelések.")
        return
    print(f"\n{'#':<4} {'Időpont':<20} {'Eszköz':<22} {'Prompt':<18} {'Átlag':<7} Forrásanyag")
    print("-" * 90)
    for i, r in enumerate(rows, 1):
        print(
            f"{i:<4} {r.get('timestamp',''):<20} {r.get('ai_tool',''):<22} "
            f"{r.get('prompt_type',''):<18} {r.get('average_score',''):<7} {r.get('source_material','')}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="MI prezentáció értékelő segédprogram – forrásanyag-alapú kísérletekhez"
    )
    parser.add_argument(
        "--summary", action="store_true", help="Összefoglaló kiírása a konzolra"
    )
    parser.add_argument(
        "--export", metavar="FÁJL.md", help="Összefoglaló mentése Markdown fájlba"
    )
    parser.add_argument(
        "--list", action="store_true", help="Rögzített értékelések listázása"
    )
    parser.add_argument(
        "--csv", metavar="FÁJL.csv", default=DEFAULT_CSV,
        help=f"CSV fájl elérési útja (alapértelmezés: {DEFAULT_CSV})"
    )
    args = parser.parse_args()

    csv_path = args.csv

    if args.list:
        rows = read_all(csv_path)
        cmd_list(rows)
        return

    if args.summary:
        rows = read_all(csv_path)
        print(build_summary(rows))
        return

    if args.export:
        rows = read_all(csv_path)
        md = build_summary(rows)
        with open(args.export, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Összefoglaló mentve: {args.export}")
        return

    # Default: new evaluation
    row = collect_evaluation()
    append_row(csv_path, row)
    print(f"\nÉrtékelés mentve: {csv_path}")
    print("Összefoglaló megtekintéséhez: python ppt_evaluation_helper.py --summary")


if __name__ == "__main__":
    main()
