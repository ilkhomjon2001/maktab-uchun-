# -*- coding: utf-8 -*-
"""
SPIKE Prime missiyalari (2-yil, 4-sinf, 3-4-chorak) — ANIQ vazifalar va ball taqsimoti.

Bu fayl 4 ta missiyani bir joyda ta'riflaydi:
  * har bir missiyaning maydonchadagi joylashuvi (koordinatalar, sm da),
  * 4 tadan kichik topshiriq (n.1 -> n.4), har biri alohida ballga ega, jami 25 ball,
  * missiyaning 6 ta darsiga taqsimlangan "dars topshirig'i" — qog'ozdan rasmiy urinishgacha
    bosqichma-bosqich qiyinlashib boradi.

QIYINLIK O'SISHI (missiyadan missiyaga):
  M1 — bitta to'g'ri chiziqli harakat, 1 ta attachment, sensor SHART EMAS   (35 s)
  M2 — chiziq kuzatish + rang bo'yicha to'xtash, 2 ta vazifa ketma-ket      (35 s)
  M3 — masofa sensori + gyroskop bilan aniq burilish, 2 ta to'siq           (40 s)
  M4 — rangga qarab QAROR qabul qilish + ko'tarish + balandlikka qo'yish    (40 s)

Maydoncha: 200 x 100 sm. Koordinata boshi (0,0) — chap past burchak.
Baza (Home base): x 0-40, y 0-40.
"""

# Maydoncha o'lchamlari (sm)
FIELD = {
    "uzunlik": 200,
    "kenglik": 100,
    "baza": (0, 0, 40, 40),          # x1, y1, x2, y2
    "tavsif": "200 x 100 sm tekis yuza (linoleum, banner yoki 2 ta stol). "
              "Chegaralar qora lenta bilan belgilanadi. Baza — chap past burchakdagi 40x40 sm kvadrat.",
}


MISSIONS = {
    1: {
        "nom": "Yuk tashish",
        "shior": "Robot yukni topib, bazaga olib qaytadi",
        "qiyinlik": "Boshlang'ich — to'g'ri chiziqli harakat, sensorsiz ham bajarish mumkin",
        "vaqt": 35,
        "attachment": "Gripper (ushlagich) yoki Scoop (cho'mich)",
        "sensorlar": "Shart emas (ixtiyoriy: masofa sensori aniqroq to'xtash uchun)",
        "tavsif": (
            "Robot bazadan chiqib, maydonchaning o'rtasidagi yuk zonasiga boradi, "
            "u yerdagi yukni (5x5 sm quti yoki katta LEGO detali) oladi va yuk bilan birga bazaga qaytadi."
        ),
        "elementlar": [
            "Yuk zonasi — 20x20 sm kvadrat, markazi (90, 20) nuqtada, oq lenta bilan belgilanadi.",
            "Yuk — 5x5x5 sm quti yoki katta LEGO detali, yuk zonasi markaziga qo'yiladi.",
        ],
        "topshiriqlar": [
            ("1.1", "Robot bazadan mustaqil chiqib, yuk zonasiga yetib boradi va u yerda to'xtaydi (yukni turtib yubormaydi).", 5),
            ("1.2", "Robot yukni ushlaydi yoki cho'michga oladi (yuk yerdan uziladi yoki attachment ichiga to'liq kiradi).", 5),
            ("1.3", "Robot yuk bilan birga bazaga qaytadi — robot ham, yuk ham baza chegarasi ichida bo'lishi kerak.", 10),
            ("1.4", "Butun harakat 35 soniyadan kam vaqtda, qo'l tekkizmasdan bajariladi.", 5),
        ],
    },

    2: {
        "nom": "Chiziq bo'ylab yetkazish",
        "shior": "Robot qora chiziqni kuzatib borib, yukni belgilangan zonaga yetkazadi",
        "qiyinlik": "O'rta — chiziq kuzatish dasturi + rang bo'yicha to'xtash",
        "vaqt": 35,
        "attachment": "Line Follower attachment + Gripper",
        "sensorlar": "Rang sensori (chiziq va yashil belgi uchun)",
        "tavsif": (
            "Robot bazadan chiqib, qora chiziq bo'ylab yuradi. Chiziq ustidagi yashil belgini sezib to'xtaydi, "
            "o'sha yerdagi yukni oladi va chiziqning oxiridagi yetkazish zonasiga qo'yadi, so'ng bazaga qaytadi."
        ),
        "elementlar": [
            "Qora chiziq — eni 2 sm, (40,20) dan (150,20) gacha to'g'ri, so'ng (150,20) dan (150,75) gacha yuqoriga buriladi.",
            "Yashil belgi — 5x5 sm, chiziq ustida (110, 20) nuqtada.",
            "Yuk — yashil belgi yonida, (110, 32) nuqtada.",
            "Yetkazish zonasi — 30x30 sm kvadrat, markazi (150, 75), ko'k lenta bilan belgilanadi.",
        ],
        "topshiriqlar": [
            ("2.1", "Robot qora chiziqdan to'liq chiqib ketmasdan kamida 50 sm masofani bosib o'tadi.", 5),
            ("2.2", "Robot chiziq ustidagi yashil belgini sezib, undan 10 sm dan uzoqlashmasdan to'xtaydi.", 5),
            ("2.3", "Robot yukni oladi va yetkazish zonasi ichiga qo'yadi (yuk zona chizig'i ichida bo'lishi kerak).", 10),
            ("2.4", "Robot vazifani bajargach, qo'l tekkizmasdan mustaqil bazaga qaytadi.", 5),
        ],
    },

    3: {
        "nom": "To'siqli yo'l va richag",
        "shior": "Robot to'siqlarni sezib aylanib o'tadi va richagni suradi",
        "qiyinlik": "Qiyin — masofa sensori + gyroskop bilan aniq 90° burilishlar",
        "vaqt": 40,
        "attachment": "Ultrasonic sensor mount + Plow (belkurak) yoki Bumper",
        "sensorlar": "Ultratovush (masofa) sensori + Hub ichidagi gyroskop",
        "tavsif": (
            "Robot bazadan chiqib, yo'lidagi ikkita to'siqni masofa sensori bilan sezadi va gyroskop yordamida "
            "aniq 90° burilishlar qilib ularni aylanib o'tadi. Yo'l oxirida maydonchadagi richagni surib qo'yadi."
        ),
        "elementlar": [
            "1-to'siq — eni 10 sm devor, x=70 sm da, PASTDAN yuqoriga 55 sm balandlikda (y 0-55). "
            "Robot uni faqat YUQORIDAN (y>55) aylanib o'ta oladi.",
            "2-to'siq — eni 10 sm devor, x=115 sm da, YUQORIDAN pastga 55 sm (y 45-100). "
            "Robot uni faqat PASTDAN (y<45) aylanib o'ta oladi.",
            "Shu sababli robot majburan zigzag qiladi: yuqoriga -> oldinga -> pastga -> oldinga.",
            "Richag — (175, 25) nuqtada, gorizontal holatdan vertikal holatga suriladigan dastak (LEGO yoki karton).",
            "Richag holati belgisi — qizil (bosilmagan) / yashil (bosilgan).",
        ],
        "topshiriqlar": [
            ("3.1", "Robot 1-to'siqqa urilmasdan, undan 15 sm yoki yaqinroq masofada masofa sensori bilan sezib to'xtaydi.", 5),
            ("3.2", "Robot gyroskop yordamida aniq 90° burilishlar qilib, 1-to'siqni YUQORIDAN aylanib o'tadi (to'siqqa tegmaydi).", 7),
            ("3.3", "Robot 2-to'siqni PASTDAN aylanib o'tib, richag zonasiga (x = 170-180 sm oralig'iga) yetib boradi.", 8),
            ("3.4", "Robot richagni to'liq suradi — belgi qizildan yashilga o'tishi kerak.", 5),
        ],
    },

    4: {
        "nom": "Aqlli saralash va ko'tarish",
        "shior": "Robot rangga qarab qaror qabul qiladi, yukni ko'taradi va platformaga qo'yadi",
        "qiyinlik": "Eng qiyin — shartli qaror (if-else) + ko'tarish mexanizmi + balandlikka aniq qo'yish",
        "vaqt": 40,
        "attachment": "Fork-lift attachment + Color sensor mount",
        "sensorlar": "Rang sensori (signal kartochkasi uchun) + gyroskop (aniq burilish uchun)",
        "tavsif": (
            "Robot bazadan chiqib, signal kartochkasining rangini o'qiydi. QIZIL bo'lsa — chapdagi A yukiga, "
            "KO'K bo'lsa — o'ngdagi B yukiga boradi (kartochkani o'qituvchi har urinishdan oldin tasodifiy almashtiradi). "
            "Kerakli yukni fork-lift bilan ko'taradi, 10 sm balandlikdagi platformaga qo'yadi va bazaga qaytadi."
        ),
        "elementlar": [
            "Signal kartochkasi — 10x10 sm, (60, 50) nuqtada. Har urinishdan oldin QIZIL yoki KO'K qilib almashtiriladi.",
            "A yuki (qizil yo'nalish) — (120, 80) nuqtada, 5x5 sm quti.",
            "B yuki (ko'k yo'nalish) — (120, 20) nuqtada, 5x5 sm quti.",
            "Platforma — 25x25 sm, balandligi 10 sm, markazi (175, 50) nuqtada.",
        ],
        "topshiriqlar": [
            ("4.1", "Robot signal kartochkasi rangini to'g'ri o'qiydi va to'g'ri yo'nalishni (A yoki B) tanlaydi.", 6),
            ("4.2", "Robot to'g'ri yukni topib, fork-lift bilan uni yerdan to'liq ko'taradi.", 6),
            ("4.3", "Robot yukni 10 sm balandlikdagi platforma ustiga qo'yadi va yuk platformadan tushib ketmaydi.", 8),
            ("4.4", "Robot bazaga qaytadi va butun urinish davomida hech kim robotga qo'l tekkizmaydi.", 5),
        ],
    },
}


# Missiyaning 6 ta darsiga taqsimlangan topshiriqlar — qog'ozdan rasmiy urinishgacha.
# Har bir yozuv: (kod, sarlavha, [talablar], "muvaffaqiyat mezoni")
def dars_topshirigi(n, step):
    m = MISSIONS[n]
    kodlar = [t[0] for t in m["topshiriqlar"]]
    k1, k2, k3, k4 = kodlar

    if step == "reja":
        return {
            "kod": f"{n}.A",
            "sarlavha": "Vazifani bo'laklash (qog'ozda)",
            "talablar": [
                f"{n}-missiyaning 4 ta kichik topshirig'ini ({k1}, {k2}, {k3}, {k4}) daftarga ko'chirib yozing.",
                "Har bir topshiriq yoniga u necha ball berishini yozing.",
                "Har bir topshiriq uchun qaysi attachment va qaysi sensor kerakligini yozing.",
                "Topshiriqlarni bajarish TARTIBINI raqamlab chiqing.",
            ],
            "mezon": "Jamoa 4 ta topshiriqni ham to'g'ri yozgan va har biriga kerakli attachment/sensorni ko'rsatgan bo'lsa — bajarilgan.",
        }

    if step == "dizayn":
        return {
            "kod": f"{n}.B",
            "sarlavha": "Ikki xil dizayn eskizi va tanlov",
            "talablar": [
                f"\"{m['attachment']}\" vazifasini bajaradigan KAMIDA 2 xil attachment eskizini chizing.",
                "Har bir eskiz yonida uning 1 ta afzalligi va 1 ta kamchiligini yozing.",
                "Ikkitasidan bittasini tanlang va nega tanlaganingizni 1 gapda asoslang.",
                f"Tanlagan dizayn {k2} topshirig'ini bajara olishini eskizda ko'rsating.",
            ],
            "mezon": "2 ta eskiz chizilgan, afzallik/kamchilik yozilgan va tanlov asoslangan bo'lsa — bajarilgan.",
        }

    if step == "yigish":
        return {
            "kod": f"{n}.C",
            "sarlavha": "Mexanik sinov — dastursiz",
            "talablar": [
                "Tanlangan attachmentni yig'ing va Driving Base'ga mahkam ulang.",
                f"Attachmentni QO'LDA harakatlantirib, {k2} topshirig'ini bajarib ko'ring (hali dastur yozilmaydi).",
                "Robotni qo'lda surib, maydonchadagi yo'l bo'ylab o'tkazing — attachment hech narsaga ilashmasligi kerak.",
                "Ilashib qolsa yoki bo'shab ketsa — konstruksiyani tuzating va qayta sinang.",
            ],
            "mezon": f"Attachment mahkam turadi va {k2} topshirig'i qo'lda bajarilsa — bajarilgan.",
        }

    if step == "dasturlash":
        return {
            "kod": f"{n}.D",
            "sarlavha": "Birinchi yarmini dasturlash",
            "talablar": [
                f"{k1} topshirig'ini to'liq dasturlang va sinang.",
                f"{k2} topshirig'ini dasturlang va sinang.",
                "Ikkala qismni BITTA dasturga birlashtiring — robot to'xtamasdan ketma-ket bajarsin.",
                f"{k3} uchun bloklarni boshlang (yakunlash shart emas).",
            ],
            "mezon": f"Robot bitta dastur bilan {k1} va {k2} topshiriqlarini ketma-ket bajarsa — bajarilgan (10 ball qiymatida).",
        }

    if step == "sinov":
        return {
            "kod": f"{n}.E",
            "sarlavha": "To'liq missiya — barqarorlik sinovi",
            "talablar": [
                f"4 ta topshiriqni ({k1}-{k4}) bitta dasturda to'liq bajaring.",
                "Missiyani KETMA-KET 3 marta sinang va har safar nechta topshiriq bajarilganini jadvalga yozing.",
                "Xato takrorlansa — sababini toping (mexanik yoki dasturiy) va tuzating.",
                f"Vaqtni xronometr bilan o'lchang — maqsad {m['vaqt']} soniyadan kam.",
            ],
            "mezon": "3 urinishdan kamida 2 tasida barcha 4 topshiriq bajarilsa — bajarilgan.",
        }

    if step == "yakuniy":
        return {
            "kod": f"{n}.F",
            "sarlavha": "Rasmiy urinish — ballga qo'yiladi",
            "talablar": [
                "Robot bazada, dastur tayyor holatda boshlanadi.",
                f"Vaqt: {m['vaqt']} soniya. Vaqt tugagach urinish to'xtatiladi.",
                "Urinish davomida robotga qo'l tekkizilmaydi. Tekkizilsa — o'sha topshiriq balli berilmaydi.",
                "Har bir jamoaga 2 ta urinish beriladi, YAXSHIROQ natija hisobga olinadi.",
            ],
            "mezon": "Ball topshiriqlar jadvali bo'yicha qo'yiladi (jami 25 ball).",
        }

    raise ValueError(step)


def topshiriq_bloki(n, step):
    """app.js uchun tayyor 'topshiriq' obyekti."""
    m = MISSIONS[n]
    d = dars_topshirigi(n, step)
    return {
        "missiya": n,
        "missiyaNomi": m["nom"],
        "kod": d["kod"],
        "sarlavha": d["sarlavha"],
        "talablar": d["talablar"],
        "mezon": d["mezon"],
        "vaqt": m["vaqt"],
        "ballJadvali": [
            {"kod": k, "matn": t, "ball": b} for k, t, b in m["topshiriqlar"]
        ],
        "jamiBall": sum(b for _, _, b in m["topshiriqlar"]),
    }


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for n, m in MISSIONS.items():
        jami = sum(b for _, _, b in m["topshiriqlar"])
        print(f"\n=== MISSIYA {n}: {m['nom']} ({jami} ball, {m['vaqt']} s) ===")
        print("   ", m["qiyinlik"])
        for k, t, b in m["topshiriqlar"]:
            print(f"    {k}  {b:2d} ball  {t}")
    print("\nJAMI:", sum(sum(b for _, _, b in m["topshiriqlar"]) for m in MISSIONS.values()), "ball")
