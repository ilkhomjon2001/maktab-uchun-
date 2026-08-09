# -*- coding: utf-8 -*-
"""
5-8-sinf darslarining to'liq rejalarini generatsiya qiladi.

Shablon 0-4 dasturi bilan AYNAN bir xil (7 bo'lim, 01-07 raqamlari o'zgarmaydi):
    maqsad, lugat, softSkill, resurslar, nazariya, amaliy, uyga, meta

Manba: syllabus_5_8.py (mavzular xaritasi)
Natija: generate_lessons_5_8.py orqali site/sample_lessons.js ga qo'shiladi.
"""

import re

from ulanish import bolim as ulanish_bolim
from kb_5_8 import MAVZULAR as KB_MAVZULAR, KIRISH as KB_KIRISH, \
    NAZORAT as KB_NAZORAT, LOYIHA as KB_LOYIHA
from kb_kod import KODLAR as KB_KODLAR

# ============================================================ ATAMALAR BAZASI
# Kalit so'z -> "Atama (inglizcha) – ta'rif"
# Dars mavzusida kalit so'z uchrasa, shu atama lug'atga tushadi.
TERMS = {
    # --- elektr asoslari ---
    "tok": "Elektr toki (Current) – zaryadlangan zarrachalarning yo'naltirilgan harakati, amperda o'lchanadi",
    "kuchlanish": "Kuchlanish (Voltage) – zaryadni harakatlantiruvchi elektr bosimi, voltda o'lchanadi",
    "qarshilik": "Qarshilik (Resistance) – materialning tokga qarshiligi, omda o'lchanadi",
    "zanjir": "Elektr zanjiri (Circuit) – tok aylanib yuradigan yopiq yo'l",
    "batareya": "Batareya (Battery) – kimyoviy energiyani elektr energiyaga aylantiruvchi manba",
    "o'tkazgich": "O'tkazgich (Conductor) – tokni yaxshi o'tkazadigan material",
    "izolyator": "Izolyator (Insulator) – tokni o'tkazmaydigan material",
    "om qonuni": "Om qonuni (Ohm's law) – U = I x R, kuchlanish, tok va qarshilik bog'liqligi",
    "quvvat": "Quvvat (Power) – vaqt birligida sarflanadigan energiya, P = U x I, vattda o'lchanadi",
    "qisqa tutashuv": "Qisqa tutashuv (Short circuit) – tokning qarshiliksiz yo'ldan o'tishi, xavfli holat",
    "bo'luvchi": "Kuchlanish bo'luvchi (Voltage divider) – ikki rezistor bilan kuchlanishni kamaytirish",
    # --- komponentlar ---
    "rezistor": "Rezistor (Resistor) – tokni cheklovchi komponent, qiymati omda",
    "led": "LED (Light Emitting Diode) – tok o'tganda yorug'lik chiqaradigan yarimo'tkazgich",
    "diod": "Diod (Diode) – tokni faqat bir yo'nalishda o'tkazuvchi komponent",
    "tranzistor": "Tranzistor (Transistor) – kichik tok bilan katta tokni boshqaruvchi komponent",
    "kondensator": "Kondensator (Capacitor) – elektr zaryadini vaqtincha to'plovchi komponent",
    "potensiometr": "Potensiometr (Potentiometer) – qo'l bilan sozlanadigan o'zgaruvchan rezistor",
    "tugma": "Tugma (Push button) – bosilganda zanjirni ulaydigan kalit",
    "rele": "Rele (Relay) – kuchsiz signal bilan kuchli yuklamani ulovchi elektromagnit kalit",
    "breadboard": "Breadboard – kavsharlashsiz sxema yig'iladigan maket taxta",
    "zummer": "Zummer (Buzzer) – elektr signalini tovushga aylantiruvchi komponent",
    "multimetr": "Multimetr (Multimeter) – kuchlanish, tok va qarshilikni o'lchaydigan asbob",
    "stabilitron": "Stabilitron (Zener diode) – kuchlanishni belgilangan darajada ushlab turuvchi diod",
    "registr": "Siljish registri (Shift register) – kam pin bilan ko'p chiqishni boshqarish mikrosxemasi",
    "segment": "7-segment indikator – yetti chiziqdan raqam hosil qiluvchi ko'rsatkich",
    "sxema": "Printsipial sxema (Schematic) – zanjirning shartli belgilar bilan chizilgan tasviri",
    # --- motorlar ---
    "motor": "Elektr motor (Motor) – elektr energiyani aylanma harakatga aylantiruvchi qurilma",
    "servo": "Servo motor (Servo) – berilgan burchakka aniq buriladigan motor",
    "qadamli": "Qadamli motor (Stepper) – aniq qadamlar bilan aylanuvchi motor",
    "h-ko'prik": "H-ko'prik (H-bridge) – motor aylanish yo'nalishini o'zgartiruvchi sxema",
    # --- sensorlar ---
    "sensor": "Sensor (Sensor) – fizik kattalikni elektr signalga aylantiruvchi qurilma",
    "fotorezistor": "Fotorezistor (LDR) – yorug'lik ta'sirida qarshiligi o'zgaradigan komponent",
    "termistor": "Termistor (Thermistor) – harorat ta'sirida qarshiligi o'zgaradigan komponent",
    "ultratovush": "Ultratovush sensori (HC-SR04) – tovush aks-sadosi orqali masofani o'lchaydi",
    "pir": "PIR sensori – issiqlik nurlanishi o'zgarishidan harakatni aniqlaydi",
    "dht": "DHT22 – harorat va namlikni raqamli signal orqali uzatuvchi sensor",
    "namlik": "Namlik (Humidity) – havodagi yoki tuproqdagi suv miqdori",
    "hall": "Hall datchigi (Hall sensor) – magnit maydonini aniqlovchi sensor",
    "reed": "Reed datchigi (Reed switch) – magnit yaqinlashganda ulanadigan kalit",
    # --- dasturlash ---
    "mikrokontroller": "Mikrokontroller (Microcontroller) – dastur bajaradigan kichik kompyuter mikrosxemasi",
    "arduino": "Arduino – dasturlanadigan mikrokontroller platasi va uning dasturiy muhiti",
    "ide": "IDE (Integrated Development Environment) – dastur yozib, plataga yuklaydigan muhit",
    "dastur": "Dastur (Program) – qurilma bajaradigan buyruqlar ketma-ketligi",
    "o'zgaruvchi": "O'zgaruvchi (Variable) – qiymat saqlanadigan nomlangan xotira katagi",
    "sikl": "Sikl (Loop) – buyruqlarni takrorlab bajaruvchi konstruksiya",
    "shart": "Shart (Condition) – rost yoki yolg'on bo'lishiga qarab yo'l tanlash",
    "funksiya": "Funksiya (Function) – nom berilgan va qayta ishlatiladigan kod bo'lagi",
    "massiv": "Massiv (Array) – bir turdagi qiymatlar to'plami, indeks bilan murojaat qilinadi",
    "kutubxona": "Kutubxona (Library) – tayyor funksiyalar to'plami",
    "serial": "Serial monitor – plata bilan kompyuter o'rtasida matnli aloqa oynasi",
    "debounce": "Debounce – tugma sakrashini dasturiy yo'l bilan bartaraf etish",
    "pwm": "PWM (Pulse Width Modulation) – impuls kengligi orqali o'rtacha quvvatni boshqarish",
    "analog": "Analog signal – uzluksiz o'zgaruvchi qiymatga ega signal",
    "raqamli": "Raqamli signal (Digital) – faqat ikki holatga ega signal: 0 yoki 1",
    "adc": "ADC – analog signalni raqamli qiymatga aylantiruvchi qism",
    "map": "map() – qiymatlar oralig'ini boshqa oraliqqa moslashtiruvchi funksiya",
    "algoritm": "Algoritm (Algorithm) – masalani yechish qadamlarining aniq ketma-ketligi",
    "nosozlik": "Nosozlik topish (Debugging) – dastur yoki sxemadagi xatoni topib tuzatish",
    "blok": "Blokli dasturlash (Block coding) – buyruqlarni bloklardan yig'ib dastur tuzish",
    # --- aloqa va IoT ---
    "i2c": "I2C – ikki sim orqali bir nechta qurilmani ulash protokoli",
    "spi": "SPI – tez ma'lumot almashinuvi uchun ketma-ket protokol",
    "esp32": "ESP32 – WiFi va Bluetooth o'rnatilgan mikrokontroller platasi",
    "wifi": "WiFi – simsiz tarmoqqa ulanish texnologiyasi",
    "veb-server": "Veb-server – brauzerga sahifa yuboradigan dastur",
    "ip": "IP manzil – tarmoqdagi qurilmaning raqamli manzili",
    "http": "HTTP – veb sahifa va ma'lumot almashish protokoli",
    "json": "JSON – ma'lumotni matn ko'rinishida almashish formati",
    "mqtt": "MQTT – IoT qurilmalari uchun yengil xabar almashish protokoli",
    "iot": "IoT (Internet of Things) – internetga ulangan qurilmalar tizimi",
    "ble": "BLE (Bluetooth Low Energy) – kam quvvat sarflaydigan simsiz aloqa",
    "telegram": "Telegram bot – xabar orqali qurilmani boshqarish vositasi",
    "oled": "OLED ekran – har bir nuqtasi o'zi yorug'lik chiqaradigan kichik ekran",
    "lcd": "LCD 1602 – ikki qatorli, o'n olti belgili suyuq kristalli ekran",
    "rfid": "RFID – radio to'lqin orqali kartani tanib olish texnologiyasi",
    "sd": "microSD kart – ma'lumotni saqlaydigan xotira kartasi",
    "rtc": "RTC (Real Time Clock) – quvvat o'chsa ham vaqtni saqlaydigan soat mikrosxemasi",
    "deep sleep": "Deep sleep – quvvat tejash uchun qurilmani uyqu rejimiga o'tkazish",
    "ota": "OTA – dasturni simsiz tarmoq orqali yangilash",
    # --- AI ---
    "sun'iy intellekt": "Sun'iy intellekt (AI) – inson aqliy vazifalarini bajaruvchi tizimlar sohasi",
    "mashinaviy": "Mashinaviy o'rganish (Machine Learning) – ma'lumotdan qonuniyat topib o'rganuvchi usul",
    "tinyml": "TinyML – mikrokontrollerda ishlaydigan kichik mashinaviy o'rganish modeli",
    "model": "Model – ma'lumotdan o'rgatilgan va bashorat qiladigan matematik tuzilma",
    "dataset": "Dataset – modelni o'rgatish uchun yig'ilgan ma'lumotlar to'plami",
    "belgi": "Belgi (Feature) – ma'lumotdan ajratilgan va model uchun muhim bo'lgan xususiyat",
    "sinf": "Sinf (Class) – model ajratadigan toifalardan biri",
    "o'rgatish": "O'rgatish (Training) – modelga ma'lumot ko'rsatib, qonuniyatni topishga o'rgatish",
    "aniqlik": "Aniqlik (Accuracy) – model to'g'ri javob bergan holatlar ulushi",
    "overfitting": "Ortiqcha moslashuv (Overfitting) – modelning yodlab olib, yangi ma'lumotda xato qilishi",
    "edge impulse": "Edge Impulse – brauzerda model o'rgatib, qurilmaga yuklash platformasi",
    "neyron": "Neyron tarmoq (Neural network) – miya tuzilishidan ilhomlangan hisoblash modeli",
    "kvantlash": "Kvantlash (Quantization) – modelni kichraytirib, tez ishlashini ta'minlash",
    "kamera": "Kamera moduli – tasvirni raqamli ma'lumotga aylantiruvchi qurilma",
    "mikrofon": "Mikrofon – tovushni elektr signalga aylantiruvchi qurilma",
    "akselerometr": "Akselerometr (MPU6050) – tezlanish va qiyalikni o'lchovchi sensor",
    "anomaliya": "Anomaliya (Anomaly) – odatdagidan keskin farq qiluvchi holat",
    # --- modul va mikrosxema nomlari (sarlavhada ko'pincha aynan shular yoziladi) ---
    "hc-sr04": "HC-SR04 – ultratovush aks-sadosi orqali masofani o'lchaydigan sensor",
    "dht22": "DHT22 – harorat va namlikni raqamli signal orqali uzatuvchi sensor",
    "mpu6050": "MPU6050 – tezlanish va burilishni o'lchaydigan akselerometr-giroskop",
    "74hc595": "74HC595 – uchta pin bilan sakkizta chiqishni boshqaruvchi siljish registri",
    "l298n": "L298N – ikki motorni yo'nalish va tezlik bilan boshqaruvchi drayver",
    "28byj": "28BYJ-48 – aniq qadamlar bilan aylanadigan arzon qadamli motor",
    "ws2812": "WS2812 – har bir diodi alohida boshqariladigan adreslanadigan LED lenta",
    "ds3231": "DS3231 – quvvat o'chsa ham vaqtni saqlaydigan aniq real vaqt soati",
    "rc522": "RC522 – RFID kartani radio to'lqin orqali o'qiydigan modul",
    "bmp280": "BMP280 – atmosfera bosimi va balandlikni o'lchovchi sensor",
    "hx711": "HX711 – tenzodatchik signalini kuchaytirib, og'irlikni o'lchashga imkon beradi",
    "ina219": "INA219 – iste'mol qilinayotgan tok va quvvatni o'lchovchi modul",
    "mq-2": "MQ-2 – tutun va yonuvchi gazlarni aniqlovchi sensor",
    "tcs3200": "TCS3200 – buyum rangini aniqlaydigan sensor",
    "ssd1306": "SSD1306 – I2C orqali ulanadigan kichik OLED ekran boshqaruvchisi",
    "xiao": "XIAO ESP32S3 Sense – kamera va mikrofoni bor, AI uchun mo'ljallangan kichik plata",
    "sg90": "SG90 – kichik va yengil servo motor",
    "vs1838": "VS1838 – pultdan infraqizil signalni qabul qiluvchi modul",
    "mblock": "mBlock – bloklardan dastur yig'iladigan vizual dasturlash muhiti",
    "ldr": "LDR (fotorezistor) – yorug'lik ta'sirida qarshiligi o'zgaradigan komponent",
    "adc": "ADC – analog kuchlanishni raqamli qiymatga aylantiruvchi qism",
    "dac": "DAC – raqamli qiymatni analog kuchlanishga aylantiruvchi qism",
    "ledc": "LEDC – ESP32 platasining PWM signal hosil qiluvchi qismi",
    "freertos": "FreeRTOS – bir vaqtda bir nechta vazifani bajarishni ta'minlovchi tizim",
    "epoch": "Epoch – modelni o'rgatishda butun ma'lumotdan bir marta o'tish",
    "confusion": "Chalkashlik matritsasi – model qaysi sinfni qaysi bilan adashtirganini ko'rsatuvchi jadval",
    "latency": "Kechikish (Latency) – signal kelgandan javob chiqqunga qadar o'tgan vaqt",
    "labeling": "Belgilash (Labeling) – ma'lumotning har bo'lagiga to'g'ri sinf nomini qo'yish",
    "keyword": "Keyword spotting – nutqdan belgilangan buyruq so'zini ajratib olish",
    "object detection": "Obyekt aniqlash (Object detection) – tasvirdagi buyumni topib, joyini ko'rsatish",
    "pull-up": "Tortuvchi rezistor (Pull-up) – pin holatini aniq ushlab turuvchi rezistor",
    "tortuvchi": "Tortuvchi rezistor (Pull-up) – pin holatini aniq ushlab turuvchi rezistor",
    "kalibrlash": "Kalibrlash (Calibration) – sensor ko'rsatkichini haqiqiy qiymatga moslash",
    "optopara": "Optopara – yorug'lik orqali ikki zanjirni elektr jihatdan ajratuvchi element",
    "predoxranitel": "Predoxranitel (Fuse) – tok ortib ketganda zanjirni uzuvchi himoya elementi",
    "rangli kod": "Rangli kod – rezistor qiymatini halqalar rangi orqali bildirish usuli",
    "datasheet": "Datasheet – komponentning texnik xususiyatlari yozilgan rasmiy hujjat",
    "prototip": "Prototip – g'oyani sinab ko'rish uchun yig'ilgan dastlabki namuna",
    "korpus": "Korpus – qurilma qismlarini himoyalovchi va biriktiruvchi tashqi g'ilof",
    "texnik topshiriq": "Texnik topshiriq – loyihaga qo'yiladigan talablar yozilgan hujjat",
}

# Har bir yo'nalish uchun standart atamalar (lug'at 5 taga to'ldiriladi)
TRACK_TERMS = {
    "elektronika": ["zanjir", "kuchlanish", "tok", "rezistor", "sxema"],
    "arduino": ["mikrokontroller", "dastur", "o'zgaruvchi", "shart", "nosozlik"],
    "esp32": ["esp32", "wifi", "iot", "dastur", "sensor"],
    "ai": ["sun'iy intellekt", "model", "dataset", "o'rgatish", "aniqlik"],
}

TRACK_JIHOZ = {
    "elektronika": "SET A — elektronika to'plami (breadboard, multimetr, komponentlar)",
    "arduino": "SET A — Arduino Uno va elektronika to'plami",
    "esp32": "SET B — ESP32 va sensorlar to'plami",
    "ai": "SET B — XIAO ESP32S3 Sense, MPU6050, Edge Impulse",
}

SOFT_SKILLS = [
    "Diqqat va aniqlik — elektronikada bitta noto'g'ri ulangan sim butun sxemani ishlamay qo'yadi, shuning uchun har qadamni tekshirib borish ko'nikmasi shakllanadi.",
    "Sabr-toqat — birinchi urinishda ishlamasligi normal holat; xatoni izlash jarayoni o'zi eng ko'p narsa o'rgatadi.",
    "Jamoada ishlash — juftlikda ishlashda vazifalarni bo'lish va bir-birini tekshirish.",
    "Xavfsizlik madaniyati — o'z va boshqalarning xavfsizligi uchun javobgarlikni his qilish.",
    "Tanqidiy fikrlash — \"nega ishlamayapti?\" savoliga taxmin emas, tekshirish orqali javob izlash.",
    "Muammoni bo'laklarga bo'lish — katta vazifani kichik, tekshiriladigan qadamlarga ajratish.",
    "Hujjatlashtirish odati — qilingan ishni yozib borish, keyin qayta tiklay olish.",
    "Mustaqillik — yordam so'rashdan oldin o'zi tekshirib ko'rish tartibiga rioya qilish.",
    "O'zaro yordam — tushungan o'quvchi tushunmaganiga tushuntirishi orqali bilim mustahkamlanadi.",
    "Tartib va ozodalik — komponentlarni joyiga qo'yish, ish o'rnini toza saqlash.",
    "Ijodkorlik — berilgan vazifani o'z g'oyasi bilan boyitish.",
    "Mas'uliyat — jihozga ehtiyotkorlik bilan munosabatda bo'lish, buzilganini yashirmaslik.",
    "Vaqtni boshqarish — dars davomida bosqichlarni ulgurish uchun rejalashtirish.",
    "Tinglash ko'nikmasi — ko'rsatma to'liq eshitilgach ish boshlash.",
    "O'z natijasini baholay olish — ishlagan/ishlamagan deb emas, qanchalik yaxshi ishlaganini baholash.",
    "Muloqot — texnik fikrni boshqalarga tushunarli tilda yetkazish.",
]

RESURS_UMUMIY = [
    "Proyektor va taqdimot slaydlari",
    "Doska va marker (sxema chizish uchun)",
    "O'quvchilar uchun ish daftari (logbook)",
]


def _norm(s):
    return s.lower().replace("'", "'")


def pick_terms(mavzu, track, n=5):
    """Mavzu matnidan kalit so'zlarni topib, lug'at tuzadi."""
    m = _norm(mavzu)
    found = []
    for key, val in TERMS.items():
        if _norm(key) in m and val not in found:
            found.append(val)
    # yetmasa — yo'nalish atamalari bilan to'ldiriladi
    for key in TRACK_TERMS.get(track, []):
        if len(found) >= n:
            break
        val = TERMS.get(key)
        if val and val not in found:
            found.append(val)
    return found[:n]


# Sarlavhaning boshidagi xizmat prefikslari — faqat shular kesiladi
_PREFIX = re.compile(r"^(Chorak kirish|Nazorat|Loyiha)\s*:\s*", re.I)


def short(mavzu):
    """Mavzu nomi. Ikki nuqtada KESILMAYDI — 'HC-SR04: masofa o'lchash' kabi
    sarlavhalarda ma'no aynan ikkinchi qismda bo'ladi."""
    s = _PREFIX.sub("", mavzu).strip()
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s).strip()   # oxiridagi qavsni olib tashlash
    return s if s else mavzu


# Plataga ulash ma'lumoti faqat plata ishlatiladigan darsda ma'noga ega.
# 5-6-sinfning platasiz elektronika darslarida "Arduino Uno D9" deyish xato bo'lardi.
_PLATA_MAVZU = re.compile(r"arduino|plata|blok|mikrokontroller|\bIDE\b", re.I)


def plataga_ulanadimi(mavzu, track):
    if track in ("arduino", "esp32", "ai"):
        return True
    return bool(_PLATA_MAVZU.search(mavzu))


def _kichik(s):
    """Gap ichiga qo'yish uchun faqat BIRINCHI harfni kichraytiradi.
    Butun satrni lower() qilish qisqartma va modul nomlarini buzadi."""
    return s[:1].lower() + s[1:] if s else s


def kb_kalit(mavzu):
    """Kontent bazasi kaliti — sillabusdagi asl satr (prefikssiz, qavs bilan)."""
    return _PREFIX.sub("", mavzu).strip()


def kb_topilsin(mavzu, tur):
    """Shu dars uchun aniq kontent. Topilmasa None — shablon ishlatiladi."""
    k = kb_kalit(mavzu)
    if tur == "mavzu":
        return KB_MAVZULAR.get(k)
    if tur == "kirish":
        return KB_KIRISH.get(k)
    if tur == "nazorat":
        return KB_NAZORAT.get(k)
    if tur == "loyiha":
        return KB_LOYIHA.get(k)
    return None


def kod_topilsin(mavzu, tur):
    """Sof dasturlash mavzusi uchun kod namunasi (kb_kod.py)."""
    if tur != "mavzu":
        return None
    return KB_KODLAR.get(kb_kalit(mavzu))


def amaliy_nomi(mavzu, tur):
    """Darsning AMALIY ISHI nomi.

    CLAUDE.md qoidasi: mavzu (ilmiy tema) va amaliy ish AJRATILGAN. Mavzu
    dars sarlavhasida, amaliy ish esa alohida qatorda ko'rsatiladi.

    kb_kod.py da "amaliy" berilgan bo'lsa, u USTUN turadi: sof nazariy
    amaliyot elektronika bilan bog'langan variantga almashtiriladi.
    """
    kod = kod_topilsin(mavzu, tur)
    if kod and kod.get("amaliy"):
        return kod["amaliy"]
    kb = kb_topilsin(mavzu, tur)
    if not kb:
        return None
    if tur in ("nazorat", "loyiha"):
        return kb.get("nom")
    return kb.get("amaliy")


# ============================================================ BO'LIM QURUVCHI

def build_maqsad(mavzu, track, sinf, tur):
    s = short(mavzu)
    if tur == "kirish":
        return [
            f"O'quvchilar chorak davomida o'rganiladigan mavzular va kutilayotgan natijalar bilan tanishadilar.",
            f"O'quvchilar ish o'rnini to'g'ri tashkil qilish va xavfsizlik qoidalarini o'zlashtiradilar.",
            f"O'quvchilar kerakli jihoz va dasturiy vositalar bilan tanishadilar.",
        ]
    if tur == "nazorat":
        return [
            "O'quvchilar chorak davomida o'rganilgan bilimlarini mustaqil qo'llay oladilar.",
            "O'quvchilar berilgan vazifani belgilangan vaqtda mustaqil bajaradilar.",
            "O'qituvchi har bir o'quvchining bilim darajasini aniq mezonlar bo'yicha baholaydi.",
        ]
    if tur == "loyiha":
        return [
            "O'quvchilar chorak davomida o'rganilgan bilimlarni bitta yaxlit ishda birlashtiradilar.",
            "O'quvchilar loyihani rejalashtirish, yig'ish va sinash bosqichlarini mustaqil o'tadilar.",
            "O'quvchilar o'z ishini boshqalarga tushunarli qilib taqdim eta oladilar.",
        ]
    verbs = {
        "elektronika": ("tushunadilar", "zanjirda amalda ko'radilar", "mustaqil yig'a oladilar"),
        "arduino": ("tushunadilar", "dasturda qo'llay oladilar", "mustaqil dastur yoza oladilar"),
        "esp32": ("tushunadilar", "ESP32 platasida qo'llay oladilar", "mustaqil sozlay oladilar"),
        "ai": ("tushunadilar", "amaliy modelda ko'radilar", "mustaqil qo'llay oladilar"),
    }[track]
    amaliy = amaliy_nomi(mavzu, tur)
    uchinchi = (f"O'quvchilar amaliy ishni — {_kichik(amaliy)} — {verbs[2]}."
                if amaliy else
                f"O'quvchilar shu mavzu bo'yicha berilgan amaliy vazifani {verbs[2]}.")
    return [
        f"O'quvchilar \"{s}\" mavzusining asosiy tushunchalarini {verbs[0]}.",
        f"O'quvchilar bu tushunchani {verbs[1]} va natijani izohlay oladilar.",
        uchinchi,
    ]


def build_nazariya(mavzu, track, tur, qurilma_bloklari=None, kod_blok=None):
    s = short(mavzu)
    kb = kb_topilsin(mavzu, tur)

    if tur == "kirish":
        bloklar = []
        if kb:
            bloklar.append({"title": "5.1. Chorak rejasi va maqsadlar (12 daqiqa)",
                            "points": list(kb["nazariya"])})
        else:
            bloklar.append({"title": "5.1. Chorak rejasi bilan tanishuv (10 daqiqa)", "points": [
                "O'qituvchi chorak davomida o'rganiladigan mavzularni umumiy ko'rsatadi.",
                "Chorak oxirida qanday natijaga erishilishi tushuntiriladi.",
            ]})
        bloklar.append({"title": "5.2. Xavfsizlik va ish o'rni (8 daqiqa)", "points": [
            "Elektr bilan ishlashda xavfsizlik qoidalari takrorlanadi.",
            "Ish o'rnini tashkil qilish va jihozni saqlash tartibi ko'rsatiladi.",
        ]})
        return bloklar

    if tur == "nazorat":
        if kb:
            points = [f"Musobaqa nomi: {kb['nom']}.", kb["vazifa"]]
            if kb.get("vaqt"):
                d = kb["vaqt"] // 60
                points.append(f"Umumiy vaqt chegarasi — {d} daqiqa. Vaqt sekundomer bilan o'lchanadi.")
            points.append("Baholash mezonlari oldindan e'lon qilinadi (quyidagi jadvalga qarang).")
            return [{"title": f"5.1. \"{kb['nom']}\" — shartlar va mezonlar (8 daqiqa)",
                     "points": points}]
        return [
            {"title": "5.1. Nazorat shartlari (7 daqiqa)", "points": [
                "O'qituvchi vazifa shartini va baholash mezonlarini e'lon qiladi.",
                "Vaqt chegarasi va ruxsat etilgan yordam darajasi aytiladi.",
            ]},
        ]

    if tur == "loyiha":
        if kb:
            return [{"title": f"5.1. \"{kb['nom']}\" — talablar (8 daqiqa)",
                     "points": ["Loyihaga qo'yiladigan talablar:"] +
                               [f"— {t}" for t in kb["talablar"]] +
                               ["Ball taqsimoti quyidagi jadvalda berilgan, jami 100 ball."]}]
        return [
            {"title": "5.1. Loyiha talablari (8 daqiqa)", "points": [
                "Loyihaga qo'yiladigan talablar va baholash mezonlari tushuntiriladi.",
                "Namuna sifatida tayyor ish ko'rsatiladi va tahlil qilinadi.",
            ]},
        ]

    # --- Oddiy mavzu darsi: bazada aniq matn bo'lsa, o'sha ishlatiladi ---
    if kb:
        n = [1]

        def raqam():
            n[0] += 1
            return f"5.{n[0]}"

        bloklar = [
            {"title": "5.1. Takrorlash va bugungi savol (4 daqiqa)", "points": [
                "O'tgan darsdagi asosiy natija qisqa takrorlanadi.",
                f"Bugungi mavzu — \"{s}\" — nima uchun kerakligi hayotiy misol bilan bog'lanadi.",
            ]},
            {"title": f"5.2. {s} — asosiy tushuncha (8 daqiqa)",
             "points": list(kb["nazariya"])},
        ]

        # Komponentli darsda o'qituvchi aytishi kerak bo'lgan TEXNIK MA'LUMOT
        # ham nazariya qismiga kiradi: bu darsda gapiriladigan matn, keyingi
        # bo'limlar esa amalda ishlatiladigan ma'lumotnoma.
        for b in (qurilma_bloklari or []):
            if b.get("tasnif"):
                bloklar.append({
                    "title": f"{raqam()}. {b['nom']} — texnik tasnif (4 daqiqa)",
                    "points": list(b["tasnif"]),
                })
            if b.get("ishlash"):
                bloklar.append({
                    "title": f"{raqam()}. {b['nom']} — ichida nima sodir bo'ladi (4 daqiqa)",
                    "points": list(b["ishlash"]),
                })

        # Sof dasturlash mavzusida kod namunasining mazmuni tushuntiriladi
        if kod_blok and kod_blok.get("izoh"):
            bloklar.append({
                "title": f"{raqam()}. Kod namunasi nima qiladi (4 daqiqa)",
                "points": [
                    kod_blok["izoh"],
                    f"Doskaga chiqariladigan namuna: \"{kod_blok['nom']}\" "
                    f"(quyidagi \"Tayyor kod namunasi\" bo'limida to'liq berilgan).",
                    "Kod qatorma-qator o'qiladi: har bir qator nima qilishi "
                    "ovoz chiqarib aytiladi, keyin o'quvchilar takrorlaydi.",
                ],
            })

        if kb.get("savol"):
            bloklar.append({"title": f"{raqam()}. Tushunganini tekshirish (4 daqiqa)",
                            "points": [f"Savol: {q}  Javob: {a}" for q, a in kb["savol"]]})
        return bloklar

    intro = {
        "elektronika": "O'tgan darsdagi zanjir va o'lchov ko'nikmalari qisqa takrorlanadi.",
        "arduino": "O'tgan darsdagi dastur tuzilishi va sxema qisqa takrorlanadi.",
        "esp32": "O'tgan darsdagi ESP32 sozlamalari va ulanish qisqa takrorlanadi.",
        "ai": "O'tgan darsdagi model va ma'lumot tushunchalari qisqa takrorlanadi.",
    }[track]
    body = {
        "elektronika": [
            f"\"{s}\" mavzusining fizik ma'nosi sxema va misollar orqali tushuntiriladi.",
            "Doskada printsipial sxema chiziladi va har bir element izohlanadi.",
        ],
        "arduino": [
            f"\"{s}\" tushunchasi kod misoli bilan bosqichma-bosqich tushuntiriladi.",
            "Kodning har bir qatori nima qilishi ovoz chiqarib tahlil qilinadi.",
        ],
        "esp32": [
            f"\"{s}\" mavzusi ESP32 imkoniyatlari doirasida tushuntiriladi.",
            "Arduino bilan farqi va e'tibor berish kerak bo'lgan joylar ko'rsatiladi.",
        ],
        "ai": [
            f"\"{s}\" tushunchasi sodda misol va ko'rgazma orqali tushuntiriladi.",
            "Model qanday \"o'rganishi\" jarayoni qadamma-qadam ko'rsatiladi.",
        ],
    }[track]
    return [
        {"title": "5.1. Takrorlash va kirish (6 daqiqa)", "points": [
            intro,
            f"Bugungi mavzu — \"{s}\" — nima uchun kerakligi hayotiy misol bilan bog'lanadi.",
        ]},
        {"title": f"5.2. {s} — asosiy tushuncha (12 daqiqa)", "points": body},
        {"title": "5.3. Xatolar va e'tibor (4 daqiqa)", "points": [
            "Shu mavzuda ko'p uchraydigan xatolar oldindan ko'rsatiladi.",
            "Xatoni qanday tekshirish kerakligi bo'yicha aniq tartib beriladi.",
        ]},
    ]


def build_amaliy(mavzu, track, tur):
    s = short(mavzu)
    kb = kb_topilsin(mavzu, tur)

    if kb and tur == "nazorat":
        return [
            {"title": f"6.1. \"{kb['nom']}\" — mustaqil bajarish (25 daqiqa)",
             "points": [f"{i}) {t}" for i, t in enumerate(kb["talablar"], 1)]},
            {"title": "6.2. Natijani ko'rsatish va baholash (8 daqiqa)", "points": [
                "O'quvchi ishini ko'rsatib, qanday qilganini qisqa tushuntiradi.",
                "O'qituvchi mezon jadvali bo'yicha ball qo'yadi va izoh beradi.",
            ]},
        ]

    if kb and tur == "loyiha":
        return [
            {"title": f"6.1. \"{kb['nom']}\" — yig'ish va dasturlash (22 daqiqa)",
             "points": [f"{i}) {t}" for i, t in enumerate(kb["talablar"], 1)]},
            {"title": "6.2. Sinov va tuzatish (8 daqiqa)", "points": [
                "Qurilma talablar ro'yxati bo'yicha bandma-band sinaladi.",
                "Aniqlangan kamchiliklar tuzatiladi va sinov qaytariladi.",
            ]},
            {"title": "6.3. Taqdimot (5 daqiqa)", "points": [
                "Muammo, yechim, namoyish va cheklovlar tartibida qisqacha taqdim etiladi.",
            ]},
        ]

    if kb and tur == "kirish":
        return [
            {"title": f"6.1. {kb['amaliy']} (15 daqiqa)", "points": [
                "O'quvchilar berilgan vazifani juftlikda bajaradilar.",
                "Natija ish daftariga yoziladi.",
            ]},
            {"title": "6.2. Ish daftarini boshlash (7 daqiqa)", "points": [
                "Ish daftarining birinchi sahifasi to'ldiriladi.",
                "Daftarni qanday yuritish kerakligi namunada ko'rsatiladi.",
            ]},
        ]

    if kb and tur == "mavzu":
        tekshiruv = {
            "elektronika": "Natija multimetr bilan tekshiriladi va qiymatlar ish daftariga yoziladi.",
            "arduino": "Natija Serial monitor orqali tekshiriladi va kod izohi bilan daftarga yoziladi.",
            "esp32": "Natija Serial monitor yoki ekran orqali tekshiriladi va yozib olinadi.",
            "ai": "Natija qurilmada sinab ko'riladi va o'lchangan qiymat yozib olinadi.",
        }[track]
        return [
            {"title": "6.1. Tayyorgarlik (5 daqiqa)", "points": [
                "Kerakli komponentlar tanlanadi va ish o'rni tayyorlanadi.",
                "Juftliklar vazifani o'zaro bo'lib oladilar.",
            ]},
            {"title": "6.2. Amaliy ish (15 daqiqa)", "points": [
                "Bajariladigan ish: " + _kichik(amaliy_nomi(mavzu, tur) or kb["amaliy"]) + ".",
                tekshiruv,
            ]},
            {"title": "6.3. Tekshirish va tuzatish (8 daqiqa)", "points": [
                (("Ko'p uchraydigan xato: " + kb["xato"]) if kb.get("xato")
                 else "Ishlamagan holatda xato bosqichma-bosqich izlanadi."),
                "Natija ish daftariga yoziladi: nima qilindi, nima chiqdi.",
            ]},
        ]

    if tur == "kirish":
        return [
            {"title": "6.1. Jihoz bilan tanishuv (15 daqiqa)", "points": [
                "O'quvchilar to'plamdagi komponentlarni ko'rib chiqadilar va nomlarini yozadilar.",
                "Har bir juftlik to'plam to'liqligini ro'yxat bo'yicha tekshiradi.",
            ]},
            {"title": "6.2. Ish daftarini boshlash (7 daqiqa)", "points": [
                "O'quvchilar ish daftarining birinchi sahifasini to'ldiradilar.",
                "Daftarni qanday yuritish kerakligi namunada ko'rsatiladi.",
            ]},
        ]
    if tur == "nazorat":
        return [
            {"title": "6.1. Mustaqil bajarish (25 daqiqa)", "points": [
                "Har bir o'quvchi vazifani mustaqil bajaradi, o'qituvchi kuzatadi.",
                "Ishlash jarayoni va yakuniy natija alohida baholanadi.",
            ]},
            {"title": "6.2. Natijani ko'rsatish (8 daqiqa)", "points": [
                "O'quvchi ishini ko'rsatib, qanday qilganini qisqa tushuntiradi.",
                "O'qituvchi mezon bo'yicha ball qo'yadi va izoh beradi.",
            ]},
        ]
    if tur == "loyiha":
        return [
            {"title": "6.1. Loyihani yig'ish (22 daqiqa)", "points": [
                "O'quvchilar o'z rejasi bo'yicha qurilmani yig'adilar va dasturlaydilar.",
                "O'qituvchi har bir guruhga borib, yo'nalish beradi.",
            ]},
            {"title": "6.2. Sinov va tuzatish (8 daqiqa)", "points": [
                "Qurilma sinovdan o'tkaziladi, kamchiliklar aniqlanadi va tuzatiladi.",
            ]},
            {"title": "6.3. Taqdimot (5 daqiqa)", "points": [
                "Har bir guruh ishini qisqacha ko'rsatadi va savollarga javob beradi.",
            ]},
        ]
    main = {
        "elektronika": [
            f"O'quvchilar \"{s}\" mavzusiga oid sxemani breadboardda yig'adilar.",
            "Yig'ilgan zanjir multimetr bilan tekshiriladi va qiymatlar daftarga yoziladi.",
        ],
        "arduino": [
            f"O'quvchilar \"{s}\" mavzusiga oid sxemani yig'ib, dasturni yozadilar.",
            "Dastur plataga yuklanadi va natija kuzatiladi.",
        ],
        "esp32": [
            f"O'quvchilar \"{s}\" bo'yicha ESP32 sxemasini yig'ib, dasturni yuklaydilar.",
            "Natija Serial monitor yoki ekran orqali tekshiriladi.",
        ],
        "ai": [
            f"O'quvchilar \"{s}\" bo'yicha amaliy qadamlarni Edge Impulse muhitida bajaradilar.",
            "Natija qurilmada sinab ko'riladi va o'lchanadi.",
        ],
    }[track]
    return [
        {"title": "6.1. Tayyorgarlik (5 daqiqa)", "points": [
            "Kerakli komponentlar tanlanadi va ish o'rni tayyorlanadi.",
            "Juftliklar vazifani o'zaro bo'lib oladilar.",
        ]},
        {"title": f"6.2. {s} — amaliy ish (15 daqiqa)", "points": main},
        {"title": "6.3. Tekshirish va tuzatish (8 daqiqa)", "points": [
            "Ishlamagan holatda xato bosqichma-bosqich izlanadi.",
            "Natija ish daftariga yoziladi: nima qilindi, nima chiqdi.",
        ]},
    ]


def build_uyga(mavzu, track, tur):
    s = short(mavzu)
    if tur == "kirish":
        return ["Ish daftarini rasmiylashtirib keling.",
                "To'plamdagi 5 ta komponent nomini yodlab keling."]
    if tur == "nazorat":
        return ["Nazoratda xato qilingan joyni takrorlab keling."]
    if tur == "loyiha":
        return ["Loyihangiz haqida qisqa tavsif yozib keling: g'oya, tuzilish, natija.",
                "Loyihani yanada yaxshilash uchun bitta taklif o'ylab keling."]
    q = {
        "elektronika": f"\"{s}\" mavzusi bo'yicha bugungi sxemani daftarga chizib keling.",
        "arduino": f"Bugungi dasturni daftarga ko'chirib, har qatoriga izoh yozib keling.",
        "esp32": f"\"{s}\" bo'yicha bugungi sozlamalarni yozib, bitta savol tayyorlab keling.",
        "ai": f"\"{s}\" mavzusiga oid hayotiy misol topib keling (AI qayerda ishlatiladi).",
    }[track]
    return [q, "Bugungi darsda tushunilmagan bitta savolni yozib keling."]


def build_resurslar(track, mavzu):
    base = [TRACK_JIHOZ[track]] + RESURS_UMUMIY
    if track in ("arduino", "esp32", "ai"):
        base.insert(1, "Kompyuter (har juftlikka bitta) va USB kabel")
    if track == "elektronika":
        base.insert(1, "Multimetr (har juftlikka bitta)")
    if track == "ai":
        base.insert(2, "Internet aloqasi (Edge Impulse brauzerda ishlaydi)")
    return base


def build_lesson(mavzu, track, tur, sinf, yil, chorak, idx, hafta, modul):
    # Ulanish sxemasi va kutubxona — 07 dan keyingi qo'shimcha bo'lim.
    # ESP32 yo'nalishlarida pinlar boshqacha, shuning uchun esp bayrog'i beriladi.
    ulanish_bloklari = ulanish_bolim(
        mavzu,
        esp=(track in ("esp32", "ai")),
        plata=plataga_ulanadimi(mavzu, track),
    )
    kb = kb_topilsin(mavzu, tur)
    d = {
        "maqsad": build_maqsad(mavzu, track, sinf, tur),
        "lugat": pick_terms(mavzu, track),
        "softSkill": SOFT_SKILLS[idx % len(SOFT_SKILLS)],
        "resurslar": build_resurslar(track, mavzu),
        "nazariya": build_nazariya(mavzu, track, tur,
                                   ulanish_bloklari, kod_topilsin(mavzu, tur)),
        "amaliy": build_amaliy(mavzu, track, tur),
        "uyga": build_uyga(mavzu, track, tur),
        "meta": {
            "sinf": sinf, "yil": yil,
            "chorak": f"{chorak}, {hafta}-hafta",
            "darsRaqami": f"{idx + 1} / 84",
            "modul": modul,
            "jihoz": TRACK_JIHOZ[track],
            "davomiyligi": "45 daqiqa",
        },
    }
    # --- 07 dan keyingi qo'shimcha bo'limlar ---
    if kb and kb.get("qollanma"):
        d["qollanma"] = {"matn": kb["qollanma"]}
        if kb.get("xato"):
            d["qollanma"]["xato"] = kb["xato"]
    if kb and tur == "nazorat":
        d["mezon"] = {"turi": "nazorat", "nom": kb["nom"], "vaqt": kb.get("vaqt"),
                      "ustunlar": ["Baho", "Shart"], "qatorlar": kb["mezon"]}
    if kb and tur == "loyiha":
        d["mezon"] = {"turi": "loyiha", "nom": kb["nom"], "vaqt": None,
                      "ustunlar": ["Baholanadigan band", "Ball"], "qatorlar": kb["mezon"]}
    # Sof dasturlash mavzusida komponent pasporti bo'lmaydi, shuning uchun
    # kod namunasi alohida beriladi (kb_kod.py).
    kod = kod_topilsin(mavzu, tur)
    if kod:
        d["kod"] = {"nom": kod["nom"], "matn": kod["kod"], "izoh": kod.get("izoh")}
    if ulanish_bloklari:
        d["ulanish"] = ulanish_bloklari
    return d
