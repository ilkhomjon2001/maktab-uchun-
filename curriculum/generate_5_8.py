# -*- coding: utf-8 -*-
"""
5-8-sinf darslarini generatsiya qilib, mavjud sayt fayllariga QO'SHADI.

MUHIM: 0-4 sinf ma'lumotlariga TEGILMAYDI. Skript tree_data.js va
sample_lessons.js ni o'qiydi, ulardan 5-8 sinf yozuvlarini olib tashlaydi
(qayta ishga tushirish uchun) va yangisini qo'shib qayta yozadi.

Ishga tushirish (site/ papkasidan):
    python curriculum/generate_5_8.py
"""

import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from syllabus_5_8 import SYLLABUS, CHORAKLAR, SINFLAR, YILLAR      # noqa: E402
from lessons_5_8 import build_lesson                                # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
TREE_PATH = os.path.join(SITE, "tree_data.js")
LESSON_PATH = os.path.join(SITE, "sample_lessons.js")

YANGI_SINFLAR = set(SINFLAR)          # 5-8-sinf — faqat shular qayta yoziladi


def load_js_object(path, prefix):
    """window.X = {...}; faylidan JSON obyektni o'qiydi."""
    with io.open(path, encoding="utf-8") as f:
        t = f.read()
    i = t.index("{")
    body = t[i:].rstrip().rstrip(";")
    return json.loads(body)


def dump_js_object(path, varname, obj, indent=None):
    with io.open(path, "w", encoding="utf-8") as f:
        f.write("window.%s = " % varname)
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write(";\n")


def hafta_raqami(idx):
    """21 dars / chorak -> taxminan haftaga 1 dars."""
    return idx + 1


def modul_nomi(chorak_nom, chorak_key):
    n = chorak_key[0]
    return f"M{n}. {chorak_nom}"


def build():
    tree = load_js_object(TREE_PATH, "TREE_DATA")
    lessons = load_js_object(LESSON_PATH, "LESSON_CONTENT")

    # --- Eski 5-8 yozuvlarini tozalash (qayta ishga tushirish uchun) ---
    for yil in list(tree.keys()):
        for sinf in list(tree[yil].keys()):
            if sinf in YANGI_SINFLAR:
                del tree[yil][sinf]
    for key in [k for k in lessons if k.split("|")[1] in YANGI_SINFLAR]:
        del lessons[key]

    jami = 0
    for yil in YILLAR:
        tree.setdefault(yil, {})
        for sinf in SINFLAR:
            tree[yil][sinf] = {}
            for chorak in CHORAKLAR:
                q = SYLLABUS[yil][sinf][chorak]
                track = q["yonalish"]
                modul = modul_nomi(q["nom"], chorak)

                # 21 dars: 1 kirish + 18 mavzu + 1 nazorat + 1 loyiha
                darslar = []
                darslar.append((f"Chorak kirish: {q['kirish']}", "kirish", track))
                for m in q["mavzular"]:
                    darslar.append((m, "mavzu", track))
                darslar.append((f"Nazorat: {q['nazorat']}", "nazorat", "nazorat"))
                darslar.append((f"Loyiha: {q['loyiha']}", "loyiha", "loyiha"))

                tree_items = []
                for idx, (mavzu, tur, badge) in enumerate(darslar):
                    tree_items.append({
                        "title": mavzu,
                        "model": None,
                        "type": badge,
                    })
                    content_track = track if tur in ("kirish", "mavzu") else track
                    lessons["%s|%s|%s|%d" % (yil, sinf, chorak, idx)] = build_lesson(
                        mavzu=mavzu, track=content_track, tur=tur,
                        sinf=sinf, yil=yil, chorak=chorak, idx=idx,
                        hafta=hafta_raqami(idx), modul=modul,
                    )
                    jami += 1

                tree[yil][sinf][chorak] = tree_items

    # --- Yozish ---
    dump_js_object(TREE_PATH, "TREE_DATA", tree)
    dump_js_object(LESSON_PATH, "LESSON_CONTENT", lessons, indent=1)

    print("5-8-sinf uchun generatsiya qilingan dars:", jami)
    print("tree_data.js dagi jami sinf-yil:",
          sum(len(v) for v in tree.values()))
    print("sample_lessons.js dagi jami dars:", len(lessons))
    print("Yozildi:", TREE_PATH)
    print("Yozildi:", LESSON_PATH)


if __name__ == "__main__":
    build()
