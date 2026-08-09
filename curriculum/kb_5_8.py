# -*- coding: utf-8 -*-
"""
5-8-sinf darslari uchun ANIQ KONTENT BAZASI.

Nima uchun kerak: syllabus_5_8.py faqat mavzu NOMINI beradi. Bu yerda esa
o'qituvchi darsda aynan nima gapirishi, o'quvchilar aynan nima qilishi
yozilgan — shablon emas, mavzuga xos matn.

Har bir mavzu uchun:
    amaliy     — shu darsda AYNAN nima yasaladi / o'lchanadi / yoziladi.
                 MUHIM: mavzu (ilmiy tema) va amaliy ish AJRATILGAN — bu
                 CLAUDE.md dagi qoida, ularni birlashtirish mumkin emas.
    nazariya   — o'qituvchi tushuntiradigan aniq matn (raqam, formula, misol
                 bilan). Shu matn dars rejasining 05-bo'limiga tushadi.
    qollanma   — o'qituvchi uchun metodik ko'rsatma: qanday tushuntirish,
                 qanday o'xshatish ishlatish, nimaga urg'u berish.
    savol      — [(savol, javob)] — darsni mustahkamlash uchun.
    xato       — shu mavzuda o'quvchilar ko'p qiladigan xato.

Bazani to'ldirish: kb_y1_*.py va kb_y2_*.py fayllari (sinf-yil bo'yicha),
nazorat/loyiha/kirish darslari uchun — kb_nazorat.py.
"""


def T(amaliy, nazariya, qollanma, savol=(), xato=None):
    return {
        "amaliy": amaliy,
        "nazariya": list(nazariya),
        "qollanma": qollanma,
        "savol": [list(s) for s in savol],
        "xato": xato,
    }


def _yig():
    """Barcha bo'lak fayllarni bitta lug'atga yig'adi.

    Bir mavzu bir nechta sinfda uchrasa (masalan "Om qonuni ..."), birinchi
    marta aniqlangan varianti ishlatiladi — takrorlanish ataylab ruxsat
    etilgan, chunki mavzu nomi bir xil bo'lsa mazmuni ham bir xil bo'ladi.
    """
    baza = {}
    mahalliy = {}
    for modul in ("kb_y1_5", "kb_y1_6", "kb_y1_7", "kb_y1_8",
                  "kb_y2_5", "kb_y2_6", "kb_y2_7", "kb_y2_8"):
        try:
            m = __import__(modul)
        except ImportError:
            continue
        for k, v in getattr(m, "MAVZULAR", {}).items():
            baza.setdefault(k, v)
        mahalliy[modul] = len(getattr(m, "MAVZULAR", {}))
    return baza, mahalliy


MAVZULAR, _BOLAKLAR = _yig()

try:
    from kb_nazorat import KIRISH, NAZORAT, LOYIHA
except ImportError:      # baza hali to'ldirilmagan bo'lsa ham generator ishlaydi
    KIRISH, NAZORAT, LOYIHA = {}, {}, {}


def topilsin(mavzu):
    """Mavzu bo'yicha kontent. Topilmasa None — generator shablonga tushadi."""
    return MAVZULAR.get(mavzu)


if __name__ == "__main__":
    import syllabus_5_8 as S
    jami = yoq = 0
    yoqlar = []
    for yil, g in S.SYLLABUS.items():
        for sinf, qs in g.items():
            for ch, q in qs.items():
                for m in q["mavzular"]:
                    jami += 1
                    if m not in MAVZULAR:
                        yoq += 1
                        yoqlar.append("%s %s %s | %s" % (yil, sinf, ch, m))
    print("Bo'laklar:", _BOLAKLAR)
    print("Bazadagi mavzu:", len(MAVZULAR))
    print("Sillabusdagi dars:", jami, "| bazada yo'q:", yoq)
    print("Kirish:", len(KIRISH), "Nazorat:", len(NAZORAT), "Loyiha:", len(LOYIHA))
    for x in yoqlar[:40]:
        print("  YO'Q:", x)
