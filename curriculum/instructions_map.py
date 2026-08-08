# -*- coding: utf-8 -*-
"""
Kurikulum model nomlarini "Robot master(PM) instruction" zip papkalariga bog'laydi.

Zip tuzilishi:  Robot master(PM) instruction/<bo'lim>/<N>.<Model nomi>/<qadam>.png
Katalog:        models_catalog.CATALOG — model -> bo'lim (11 bo'lim, zip bilan bir xil tartibda)

Moslashtirish tartibi:
  1) MANUAL — qo'lda tasdiqlangan holatlar (zipdagi nom xato yozilgan yoki 2 ta nomzod bor)
  2) O'sha BO'LIM ichida normalizatsiyalangan nom bo'yicha aniq moslik
  3) O'sha bo'lim ichida eng yaqin nom (>=0.80), aks holda — topilmadi

Bo'limlar raqami bo'yicha solishtiriladi, chunki nomlari biroz farq qiladi:
  katalog "2.Inertia"          <-> zip "2.Mechanical"
  katalog "6.Electric Animals" <-> zip "6.Electric Animal"
  katalog "11.Newly-Updated Programming" <-> zip "11. NEWLY-UPDATED Programming"
"""

import os
import re
import zipfile
from difflib import SequenceMatcher

from models_catalog import CATALOG

ROOT = r"d:\maktab uchun sayt"
ZIPS = [
    os.path.join(ROOT, "Robot master(PM) instruction-20260808T042747Z-1-001.zip"),
    os.path.join(ROOT, "Robot master(PM) instruction-20260808T042747Z-1-002.zip"),
]

# Qo'lda tasdiqlangan mosliklar: kurikulum nomi -> zip papkasi (to'liq kalit)
MANUAL = {
    # 1.Basic — bir xil nomli 2 ta papka yoki zipda imlo xatosi
    "Balance":                  "1.Basic/28.Balance",
    "Balance 2":                "1.Basic/44.Balance",
    "Sewing Machine":           "1.Basic/12.Sewing Machine",
    "Sewing Machine 2":         "1.Basic/43.Sewing Machine(Simple)",
    "Trailer (Basic)":          "1.Basic/39.Trailer",
    "Pulley Crane":             "1.Basic/30.Pulley Crance",       # zipda "Crance" — imlo xatosi
    # 2.Inertia -> zip "2.Mechanical"
    "Elasti-Pumper":            "2.Mechanical/1.Elasti-Pumper With Trigger",
    "Inertia Pull-Back Car":    "2.Mechanical/2.Inertia Pul-Back Car",
    "Top Launcher (with wheels)": "2.Mechanical/6.Top Launcher with Trigger",
    "Top Launcher (with stand)":  "2.Mechanical/8.Top Launcher With Handle",
    "Flytrap":                  "2.Mechanical/10.Flytrap",
    # 5.Electric YL Crops — zipda 25-papka xato nomlangan ("Rocking YL Man 2" -> aslida 3)
    "Rocking YL Man 2":         "5.Electric YL Crops/24.Rocking YL Man 2",
    "Rocking YL Man 3":         "5.Electric YL Crops/25.Rocking YL Man 2",
    # 7.Jr Programming — zipda qisqartirilgan/xato nomlar
    "Tyrannosaurus (AI)":       "7.Jr Programming/2.Tyannosaurus(AI)",
    "Color Sorting":            "7.Jr Programming/11.Color Sorting Machine(AI)",
    "Mine Clearance":           "7.Jr Programming/15.Mine Clearance Vechicle",
    "Automatic Gate":           "7.Jr Programming/13.Automatic Gate",
    # 8.Advanced Building
    "Propeller-driven Vehicle": "8.Advanced Building/11.Propeller-driven Aircraft",
    "Trailer":                  "8.Advanced Building/5.Trailer",
    # 11.Newly-Updated Programming
    "Obstacle Avoiding (2)":    "11. NEWLY-UPDATED Programming/18.Obstacle Avoiding Robot",
    "Obstacle Avoiding (3)":    "11. NEWLY-UPDATED Programming/19.Obstacle Avoiding Dragon",
    "Automatic Gate (Prog)":    "11. NEWLY-UPDATED Programming/23.Automatic Gate",
    "Flytrap (Prog)":           "11. NEWLY-UPDATED Programming/10.Flytrap",
    "Scooter (Prog)":           "11. NEWLY-UPDATED Programming/5.Scooter",
}


def norm(s):
    s = s.lower().replace("_", " ").replace("(", " ").replace(")", " ").replace("-", " ")
    s = s.replace("'", "").replace("\u2019", "")
    s = re.sub(r"\b(electric|ai|premium|advanced|adv|simple)\b", " ", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def section_no(name):
    m = re.match(r"\s*(\d+)", name)
    return int(m.group(1)) if m else -1


def scan_zips():
    """{'bo'lim/N.Nom': {'section':..., 'name':..., 'files': {qadam: (zip, entry)}}}"""
    out = {}
    for zp in ZIPS:
        with zipfile.ZipFile(zp) as z:
            for info in z.infolist():
                if info.is_dir():
                    continue
                p = info.filename.split("/")
                if len(p) < 4 or not p[3].lower().endswith(".png"):
                    continue
                key = p[1] + "/" + p[2]
                rec = out.setdefault(key, {"section": p[1], "folder": p[2], "files": {}})
                # Fayl nomlari: "12.png" yoki (faqat Stegosaurus Advanced'da) "1 (12).png"
                m = re.match(r"^(\d+)\.png$", p[3], re.I) or re.match(r"^1 \((\d+)\)\.png$", p[3], re.I)
                if not m:
                    continue
                step = int(m.group(1))
                prev = rec["files"].get(step)
                # bir fayl ikkala zipda bo'lsa — kattarog'i (to'liqrog'i) olinadi
                if prev is None or info.file_size > prev[2]:
                    rec["files"][step] = (zp, info.filename, info.file_size)
    for v in out.values():
        v["name"] = re.sub(r"^\s*\d+\s*\.\s*", "", v["folder"]).strip()
    return out


def build_map(zf=None, verbose=False):
    """{model_nomi: zip_papka_kaliti}  +  topilmaganlar ro'yxati."""
    zf = zf if zf is not None else scan_zips()

    by_section = {}
    for k, v in zf.items():
        by_section.setdefault(section_no(v["section"]), {}).setdefault(norm(v["name"]), []).append(k)

    mapping, missing, notes = {}, [], []
    for section, models in CATALOG.items():
        sn = section_no(section)
        pool = by_section.get(sn, {})
        for model in models:
            if model in MANUAL:
                key = MANUAL[model]
                if key not in zf:
                    missing.append((model, section, "MANUAL kalit zipda yo'q: " + key))
                else:
                    mapping[model] = key
                continue
            n = norm(model)
            cands = pool.get(n)
            if cands and len(cands) == 1:
                mapping[model] = cands[0]
                continue
            if cands:
                missing.append((model, section, "noaniq: " + ", ".join(cands)))
                continue
            best, score = None, 0.0
            for cn, keys in pool.items():
                s = SequenceMatcher(None, n, cn).ratio()
                if s > score:
                    best, score = keys, s
            if best and score >= 0.80 and len(best) == 1:
                mapping[model] = best[0]
                notes.append((model, best[0], round(score, 2)))
            else:
                missing.append((model, section, "topilmadi (eng yaqin %.2f: %s)" % (score, best[0] if best else "-")))

    if verbose:
        for m, k, s in notes:
            print("  ~%.2f  %-34s -> %s" % (s, m, k))
    return mapping, missing


def slug(name):
    s = name.lower().replace("'", "").replace("\u2019", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    zf = scan_zips()
    print("Zip papkalari:", len(zf))
    print("Katalog modellari:", sum(len(v) for v in CATALOG.values()))
    print("\n--- taxminiy (nom biroz farq qiladi) ---")
    mp, missing = build_map(zf, verbose=True)
    print("\nBog'landi:", len(mp))
    print("Topilmadi:", len(missing))
    for m, s, why in missing:
        print("  [%s] %-34s %s" % (s, m, why))
    empt = [(m, k) for m, k in mp.items() if not zf[k]["files"]]
    print("\nBo'sh papkalar:", len(empt))
    for m, k in empt:
        print("  ", m, "->", k)
