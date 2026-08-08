# -*- coding: utf-8 -*-
"""
Makerzoid resurslarini to'ldirish uchun yordamchi skript.

Ishlatish:
  python list_models.py              -> barcha modellarni ro'yxat qiladi (nechta darsda ishlatilishi bilan)
  python list_models.py --js         -> resources.js ga tayyor, to'ldirish uchun bo'sh shablon chiqaradi
  python list_models.py --missing    -> resources.js da HALI YO'Q modellarni ko'rsatadi
"""

import io
import json
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
# curriculum/ sayt repo'sining ichida yotadi, shuning uchun sayt ildizi = ota-papka
SITE = os.path.dirname(HERE)
TREE = os.path.join(SITE, "tree_data.js")
RES = os.path.join(SITE, "resources.js")


def load_tree():
    with io.open(TREE, encoding="utf-8") as f:
        c = f.read().replace("window.TREE_DATA = ", "", 1).rstrip(";\n \t\r")
    return json.loads(c)


def collect_models():
    """Model nomi -> [(yil, sinf, chorak), ...]"""
    tree = load_tree()
    models = defaultdict(list)
    for yil, grades in tree.items():
        for sinf, choraks in grades.items():
            for chorak, lessons in choraks.items():
                for l in lessons:
                    if l["type"] == "qurish" and l["model"]:
                        models[l["model"]].append((yil, sinf, chorak))
                    elif l["type"] == "spike" and " — yig'ish (1 darslik)" in l["title"]:
                        name = l["title"].split(" — ")[0].strip()
                        models[name].append((yil, sinf, chorak))
    return models


def existing_keys():
    """resources.js dagi mavjud kalitlarni o'qiydi (sodda regex bilan)."""
    if not os.path.exists(RES):
        return set()
    with io.open(RES, encoding="utf-8") as f:
        txt = f.read()
    # faqat izohga olinmagan qatorlardagi "Kalit": [  ko'rinishidagi yozuvlar
    keys = set()
    for line in txt.splitlines():
        s = line.strip()
        if s.startswith("//"):
            continue
        m = re.match(r'^,?\s*"([^"]+)"\s*:\s*\[', s)
        if m:
            keys.add(m.group(1))
    return keys


def main():
    models = collect_models()
    have = existing_keys()
    arg = sys.argv[1] if len(sys.argv) > 1 else ""

    if arg == "--missing":
        missing = sorted(m for m in models if m not in have)
        print(f"resources.js da YO'Q modellar: {len(missing)} / {len(models)}\n")
        for m in missing:
            print(f"  {m}   ({len(models[m])} ta darsda)")
        return

    if arg == "--js":
        missing = sorted(m for m in models if m not in have)
        print("// resources.js ga qo'shish uchun shablon —")
        print("// har bir modelga url va nom yozing, keraksizlarini o'chirib tashlang.\n")
        for m in missing:
            safe = m.replace('"', '\\"')
            fname = re.sub(r"[^a-z0-9]+", "-", m.lower()).strip("-")
            print(f',"{safe}": [')
            print(f'  {{ nom: "{safe} — qurish instruksiyasi",')
            print(f'    url: "instructions/makerzoid/{fname}.pdf",')
            print(f'    manba: "Makerzoid", tur: "lokal" }}')
            print(f']')
        return

    total_lessons = sum(len(v) for v in models.values())
    print(f"Jami noyob model: {len(models)}   (jami {total_lessons} ta darsda ishlatiladi)")
    print(f"resources.js da mavjud: {len(have & set(models))}")
    print(f"Hali qo'shilmagan: {len(set(models) - have)}\n")
    for m in sorted(models, key=lambda x: (-len(models[x]), x)):
        mark = "OK " if m in have else "-- "
        grades = sorted({g for _, g, _ in models[m]})
        print(f"{mark}{m:38s} {len(models[m]):3d} dars   {', '.join(grades)}")


if __name__ == "__main__":
    main()
