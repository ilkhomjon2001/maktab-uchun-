# -*- coding: utf-8 -*-
"""
site/tree_data.js dagi barcha 878 ta dars uchun to'liq dars-reja kontentini generatsiya qilib,
site/sample_lessons.js formatida (window.LESSON_CONTENT) eksport qiladi.

Kalit formati: "yil|sinf|chorak|index" — har bir dars uchun NOYOB (app.js dagi lessonKey bilan bir xil).
Shu sababli bir xil model turli sinflarda uchrasa ham, har biri O'Z sinf darajasiga mos
(tier A/B/C) kontent oladi.

Ishga tushirish:  python generate_lessons.py
"""

import json
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lesson_templates import THEME_CONTENT
from lesson_templates_special import INTRO_CONTENT
from lesson_templates_nazorat_loyiha import match_nazorat, match_loyiha
from lesson_templates_dasturlash import DASTURLASH_CONTENT
from lesson_templates_spike import SPIKE_CONTENT
from lesson_subtopics import SUBTOPICS
from lesson_subtopics2 import SUBTOPICS2
from model_themes import MODEL_THEME_MAP

# Barcha sub-mavzular bitta lug'atda
ALL_SUBTOPICS = {}
ALL_SUBTOPICS.update(SUBTOPICS)
ALL_SUBTOPICS.update(SUBTOPICS2)

# curriculum/ sayt repo'sining ichida yotadi, shuning uchun sayt ildizi = ota-papka
SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TREE_PATH = os.path.join(SITE_DIR, "tree_data.js")
OUT_PATH = os.path.join(SITE_DIR, "sample_lessons.js")

# Sinf -> qiyinlik darajasi (tier)
TIER_BY_GRADE = {
    "0-sinf": "A", "1-sinf": "A",
    "2-sinf": "B", "3-sinf": "B",
    "4-sinf": "C",
}

MAKERZOID = "Makerzoid Robot Master Standard"
MAKERZOID_PLUS = "Makerzoid + qo'shimcha motor/sensor (2+2)"
SPIKE = "LEGO Education SPIKE Prime"

# Chorak mavzulari (year1_model_pools.QUARTER_THEME bilan mos)
QUARTER_THEME = {
    "0-sinf": ["Oddiy mexanizmlar", "Yuk ko'tarish mexanizmlari", "Birinchi motorli modellar", "Sensorli figuralar"],
    "1-sinf": ["Richag va tishli g'ildirak", "Motorli modellar", "Qo'lda harakatlanuvchi mexanizmlar (YL Corps)", "Sensorli figuralar"],
    "2-sinf": ["Murakkab mexanizmlar", "Elektr mashinalar", "Elektr YL figuralari", "Sensorli aqlli modellar"],
    "3-sinf": ["Murakkab mexanika va manipulyatorlar", "Elektr hayvonlar", "Murakkab transport", "Havo/suv transporti (erkin tanlov)"],
    "4-sinf": ["Yuk ko'targich robotlar", "Patrul/qidiruv robotlari", "Kosmik texnika", "Bitiruv loyihasi (erkin tanlov)"],
}

SPIKE_QUARTER_THEME = [
    "Qurish asoslari (LEGO rasmiy modellari)",
    "Sensorlar va birinchi dasturlar",
    "Missiya 1 va 2 (FLL uslubi)",
    "Missiya 3, 4 va yakuniy turnir",
]

# Tema kaliti -> tema nomi (tree_data.js dagi title bilan mos)
THEME_TITLE_TO_KEY = {
    "Richag qonuni": "richag",
    "Tishli g'ildirak uzatmasi": "tishli",
    "Shkiv va tortish kuchi": "shkiv",
    "Aylanma harakatni tebranishga aylantirish": "krivoship",
    "Muvozanat markazi": "muvozanat",
    "Geometrik shakl mustahkamligi": "geometriya",
    "Elastik energiya va inersiya kuchi": "elastik",
    "Vint mexanizmi": "vint",
    "Ishqalanish kuchi": "ishqalanish",
    "Ko'tarish mexanizmi (richag+vint+shkiv)": "kotargich",
    "Elektr motor va aylanma harakat": "motorAylanma",
    "Aerodinamika va reaktiv kuch": "aero",
    "Suzish kuchi (Arximed qonuni)": "suv",
    "Biomimikriya (tabiatdan ilhomlanish)": "biomimikriya",
    "Sensor va signal": "sensor",
    "Notekis yuzada harakat (kosmik texnika)": "kosmik",
    "Transport va ishqalanish": "transport",
    "Avtomatik mexanizm (richag/vint)": "darvoza",
}


def load_tree():
    with io.open(TREE_PATH, encoding="utf-8") as f:
        content = f.read()
    content = content.replace("window.TREE_DATA = ", "", 1).rstrip(";\n \t\r")
    return json.loads(content)


def jihoz_for(yil, sinf, chorak):
    if sinf == "4-sinf" and yil == "2-yil":
        return SPIKE
    if "Dasturlash" in chorak:
        return "Scratch-uslub ilova (planshet/telefon)"
    qi = int(chorak[0])
    if sinf == "4-sinf":
        return MAKERZOID_PLUS
    if sinf == "3-sinf" and qi >= 3:
        return MAKERZOID_PLUS
    return MAKERZOID


def modul_for(yil, sinf, chorak, ltype):
    if "Dasturlash" in chorak:
        return "Dasturlash kursi (haftaning 3-soati)"
    qi = int(chorak[0])
    if sinf == "4-sinf" and yil == "2-yil":
        tema = SPIKE_QUARTER_THEME[qi - 1]
    else:
        tema = QUARTER_THEME[sinf][qi - 1]
    if ltype == "nazorat":
        return f"N{qi}. Nazorat ishi"
    if ltype == "loyiha":
        return f"L{qi}. Loyiha"
    return f"M{qi}. {tema}"


def build_meta(yil, sinf, chorak, idx, total_in_chorak, global_num, total_lessons):
    hafta = idx // 2 + 1
    if "Dasturlash" in chorak:
        chorak_label = f"{chorak}, {idx + 1}-hafta"
        dars_raqami = f"D-{chorak[0]}Q / {idx + 1}"
    else:
        chorak_label = f"{chorak}, {hafta}-hafta"
        dars_raqami = f"{global_num} / {total_lessons}"
    return {
        "sinf": sinf,
        "yil": yil,
        "chorak": chorak_label,
        "darsRaqami": dars_raqami,
        "modul": None,  # keyin to'ldiriladi
        "jihoz": jihoz_for(yil, sinf, chorak),
        "davomiyligi": "45 daqiqa",
    }


def sections_from_tuples(tuples, prefix):
    """[(title, minutes, points)] -> [{title: "5.1. Kirish (5 daqiqa)", points: [...]}]"""
    out = []
    for i, (title, minutes, points) in enumerate(tuples, 1):
        out.append({
            "title": f"{prefix}.{i}. {title} ({minutes} daqiqa)",
            "points": list(points),
        })
    return out


def qurish_content(title, model, sinf, idx, sub_index):
    """
    Model-asosidagi qurish darsi uchun kontent.
    sub_index — shu tema shu sinfda nechanchi marta uchrayotgani (0 dan boshlab).
    Shunga qarab HAR SAFAR BOSHQA sub-mavzu (aspekt) olinadi, ya'ni 5 ta "Richag qonuni"
    darsi 5 xil narsani o'rgatadi.
    """
    theme_key = THEME_TITLE_TO_KEY.get(title)
    if theme_key is None:
        theme_key = MODEL_THEME_MAP.get(model)
    if theme_key is None or theme_key not in THEME_CONTENT:
        theme_key = "geometriya"  # eng umumiy zaxira

    tier = TIER_BY_GRADE[sinf]
    tpl = THEME_CONTENT[theme_key]
    tdata = tpl[tier]

    softskills = tdata["softskills"]
    ss_name, ss_text = softskills[sub_index % len(softskills)]

    subs = ALL_SUBTOPICS.get(theme_key)
    sub = subs[sub_index % len(subs)] if subs else None

    if sub is None:
        # zaxira: sub-mavzusiz eski yo'l
        fokus = title
        nazariya = tdata["nazariya"]
        sinov_points = ["Yig'ilgan model ishga tushiriladi va uning harakati kuzatiladi."]
        uyga_1 = f"Kuzatuv topshirig'i: uyda yoki ko'chada bugungi mavzuga oid 2 ta misol toping."
    else:
        fokus = sub["fokus"]
        # 5.1 Kirish — temaning tier bo'yicha kirishi + SHU DARSGA XOS ochuvchi savol
        kirish_title, kirish_min, kirish_points = tdata["nazariya"][0]
        kirish_points = [sub["savol"]] + list(kirish_points)
        # 5.2 — SHU DARSNING O'Z MAVZUSI (har safar boshqacha)
        asosiy_points = list(sub["asosiy"])
        if tier in ("B", "C") and sub.get("chuqur"):
            asosiy_points.append(sub["chuqur"])
        # 5.3 Yakunlash — temaning tier bo'yicha yakuni
        yakun_title, yakun_min, yakun_points = tdata["nazariya"][2]
        nazariya = [
            (kirish_title, kirish_min, kirish_points),
            (fokus, 7, asosiy_points),
            (yakun_title, yakun_min, yakun_points),
        ]
        sinov_points = [
            "Yig'ilgan model ishga tushiriladi va uning harakati kuzatiladi.",
            sub["tajriba"],
        ]
        uyga_1 = sub["uyga"]

    maqsad = [
        f"O'quvchilar \"{fokus}\" mavzusini \"{model}\" modeli misolida tushunadilar.",
        f"O'quvchilar Makerzoid to'plamidan foydalanib, \"{model}\" modelini instruksiya bo'yicha yig'ishni o'rganadilar.",
        "O'quvchilar yig'ilgan modelni sinab, kuzatgan natijasini o'z so'zlari bilan tushuntirish ko'nikmasini rivojlantiradilar.",
    ]

    resurslar = [
        "Makerzoid Robot Master Standard to'plami (har 1-2 o'quvchiga bitta)",
        f"\"{model}\" modeli uchun bosqichma-bosqich rasmli instruksiya (to'plam ilovasida)",
        "Taqdimot uchun kompyuter va proyektor (nazariy qism uchun)",
        "Sinov uchun kerakli qo'shimcha material (kichik yuk, o'lchov lentasi va h.k. — mavzuga qarab)",
    ]

    amaliy = [
        (f"\"{model}\" modelini yig'ish", 20, [
            f"O'quvchilar instruksiya bo'yicha \"{model}\" modelini bosqichma-bosqich yig'ishadi (juftlikda ishlash tavsiya etiladi).",
            "O'qituvchi har bir juftlik oldiga borib, asosiy mexanizm to'g'ri yig'ilganini tekshiradi.",
        ]),
        ("Modelni sinash", 7, sinov_points),
        ("Tushuntirish", 3, [
            f"Har bir juftlik o'z modelini sinfga ko'rsatib, bugungi mavzu (\"{fokus}\") bo'yicha kuzatganini 1-2 gapda tushuntiradi.",
        ]),
    ]

    uyga = [
        uyga_1,
        f"Ijodiy topshiriq: \"{model}\" modelining rasmini chizib, uning asosiy qismlarini belgilang.",
    ]

    return {
        "maqsad": maqsad,
        "lugat": list(tdata["lugat"]),
        "softSkill": f"{ss_name} — {ss_text}",
        "resurslar": resurslar,
        "nazariya": sections_from_tuples(nazariya, "5"),
        "amaliy": sections_from_tuples(amaliy, "6"),
        "uyga": uyga,
    }


def normalize(raw):
    """Qo'lda yozilgan kontentni (tuple-li nazariya/amaliy) yakuniy formatga keltiradi."""
    out = {
        "maqsad": list(raw["maqsad"]),
        "lugat": list(raw["lugat"]),
        "softSkill": raw["softSkill"],
        "resurslar": list(raw["resurslar"]),
        "nazariya": sections_from_tuples(raw["nazariya"], "5"),
        "amaliy": sections_from_tuples(raw["amaliy"], "6"),
        "uyga": list(raw["uyga"]),
    }
    # Ixtiyoriy qo'shimcha bo'limlar (hozircha faqat SPIKE missiya darslarida):
    #   topshiriq — o'sha darsning aniq topshirig'i va missiya ball jadvali
    #   maydon    — musobaqa maydonchasi chizmasining raqami (site/maydon.js)
    for extra in ("topshiriq", "maydon"):
        if raw.get(extra) is not None:
            out[extra] = raw[extra]
    return out


def theme_key_of(title, model):
    k = THEME_TITLE_TO_KEY.get(title)
    if k is None:
        k = MODEL_THEME_MAP.get(model)
    if k is None or k not in THEME_CONTENT:
        k = "geometriya"
    return k


def build_content(yil, sinf, chorak, lesson, idx, sub_index=0):
    title = lesson["title"]
    model = lesson["model"]
    ltype = lesson["type"]

    if ltype == "nazorat":
        raw = match_nazorat(title)
        if raw:
            return normalize(raw)
        return None

    if ltype == "loyiha":
        raw = match_loyiha(title)
        if raw:
            return normalize(raw)
        return None

    if ltype == "dasturlash":
        raw = DASTURLASH_CONTENT.get(title)
        if raw:
            return normalize(raw)
        return None

    if ltype == "spike":
        raw = SPIKE_CONTENT.get(title)
        if raw:
            return normalize(raw)
        return None

    if ltype == "qurish":
        if title.startswith("Chorak kirish"):
            raw = INTRO_CONTENT.get(title)
            if raw:
                return normalize(raw)
            return None
        if model:
            return qurish_content(title, model, sinf, idx, sub_index)
        return None

    return None


def main():
    tree = load_tree()
    out = {}
    missing = []

    for yil, grades in tree.items():
        for sinf, choraks in grades.items():
            # umumiy dars raqami (faqat asosiy 4 chorak bo'yicha, 84 dars)
            global_num = 0
            total_lessons = sum(
                len(v) for k, v in choraks.items() if "Dasturlash" not in k
            )
            # Tema hisoblagichi: shu SINF ichida yil davomida har bir tema nechanchi marta
            # uchrayotganini sanaydi -> har safar keyingi sub-mavzu beriladi.
            theme_counter = {}
            for chorak, lessons in choraks.items():
                for idx, lesson in enumerate(lessons):
                    if "Dasturlash" not in chorak:
                        global_num += 1
                    key = f"{yil}|{sinf}|{chorak}|{idx}"
                    sub_index = 0
                    if lesson["type"] == "qurish" and lesson["model"]:
                        tk = theme_key_of(lesson["title"], lesson["model"])
                        sub_index = theme_counter.get(tk, 0)
                        theme_counter[tk] = sub_index + 1
                    content = build_content(yil, sinf, chorak, lesson, idx, sub_index)
                    if content is None:
                        missing.append((key, lesson["type"], lesson["title"][:70]))
                        continue
                    meta = build_meta(yil, sinf, chorak, idx, len(lessons),
                                      global_num, total_lessons)
                    meta["modul"] = modul_for(yil, sinf, chorak, lesson["type"])
                    content["meta"] = meta
                    out[key] = content

    total = sum(len(v) for g in tree.values() for c in g.values() for v in c.values())
    print("Jami darslar (tree_data.js):", total)
    print("Generatsiya qilingan:", len(out))
    print("Qoldi (kontentsiz):", len(missing))
    if missing:
        print("\n--- Kontent topilmagan darslar ---")
        for key, t, title in missing[:40]:
            print(f"  [{t}] {key} :: {title}")
        if len(missing) > 40:
            print(f"  ... yana {len(missing) - 40} ta")

    # Yozish
    ordered = {}
    for yil, grades in tree.items():
        for sinf, choraks in grades.items():
            for chorak, lessons in choraks.items():
                for idx in range(len(lessons)):
                    key = f"{yil}|{sinf}|{chorak}|{idx}"
                    if key in out:
                        ordered[key] = out[key]

    body = json.dumps(ordered, ensure_ascii=False, indent=1)
    with io.open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("window.LESSON_CONTENT = ")
        f.write(body)
        f.write(";\n")
    size_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"\nYozildi: {OUT_PATH} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
