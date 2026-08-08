# -*- coding: utf-8 -*-
"""1-yil (0-4-sinf) uchun YANGI dastur generatori — 100% qurish, dasturlashsiz, yuqori chastotali."""

from year1_model_pools import YEAR1_POOLS, QUARTER_INTRO, QUARTER_THEME
from model_themes import get_theme_and_guide
from musobaqa_nazorat import QUARTER_NAZORAT

MAKERZOID = "Makerzoid Robot Master Standard"
MAKERZOID_PLUS = "Makerzoid + qo'shimcha motor/sensor (2+2)"

JIHOZ_BY_GRADE = {
    "0-sinf": [MAKERZOID, MAKERZOID, MAKERZOID, MAKERZOID],
    "1-sinf": [MAKERZOID, MAKERZOID, MAKERZOID, MAKERZOID],
    "2-sinf": [MAKERZOID, MAKERZOID, MAKERZOID, MAKERZOID],
    "3-sinf": [MAKERZOID, MAKERZOID, MAKERZOID_PLUS, MAKERZOID_PLUS],
    "4-sinf": [MAKERZOID_PLUS, MAKERZOID_PLUS, MAKERZOID_PLUS, MAKERZOID_PLUS],
}


def build_grade(grade_name):
    quarters = []
    pools = YEAR1_POOLS[grade_name]
    intros = QUARTER_INTRO[grade_name]
    themes = QUARTER_THEME[grade_name]
    jihoz_list = JIHOZ_BY_GRADE[grade_name]

    for qi in range(4):
        models = pools[qi]
        # har bir dars: (dars_mavzusi=STEAM tema, model=amaliy ish nomi, guide=o'qituvchi qo'llanmasi)
        lessons = [{"mavzu": intros[qi], "model": None, "guide": None}]
        for m in models:
            theme, guide = get_theme_and_guide(m)
            lessons.append({"mavzu": theme, "model": m, "guide": guide})
        assert len(lessons) == 19, f"{grade_name} Q{qi+1}: {len(lessons)} lessons"

        nomi = f"M{qi+1}. {themes[qi]}"
        nazorat = QUARTER_NAZORAT[qi + 1]
        loyiha = (f"{qi+1}-chorak loyihasi: shu chorak modellaridan birini tanlab, "
                  f"o'zgartirib/kengaytirib qurish (erkin ijod)")

        quarters.append({
            "nomi": nomi,
            "jihoz": jihoz_list[qi],
            "lessons": lessons,
            "nazorat": nazorat,
            "loyiha": loyiha,
        })

    platforma = MAKERZOID if grade_name in ("0-sinf", "1-sinf", "2-sinf") else MAKERZOID_PLUS
    return {"platforma": platforma, "quarters": quarters}


ALL_GRADES_Y1_NEW = {g: build_grade(g) for g in ["0-sinf", "1-sinf", "2-sinf", "3-sinf", "4-sinf"]}

if __name__ == "__main__":
    total_models = 0
    for g, gd in ALL_GRADES_Y1_NEW.items():
        grade_models = 0
        for qi, q in enumerate(gd["quarters"], 1):
            n = len(q["lessons"])
            assert n == 19, f"{g} Q{qi}: {n}"
            grade_models += 18
        total_models += grade_models
        print(g, "models:", grade_models, "-> total lessons:", 4 * 21)
    print("TOTAL DISTINCT MODELS BUILT IN YEAR 1 (across 5 grades):", total_models)
