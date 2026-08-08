# -*- coding: utf-8 -*-
"""
4-sinf, 2-yil (LEGO Education SPIKE Prime) darslari uchun to'liq kontent.
Naqshga asoslangan: attachment-yig'ish (18 ta, umumiy shablon + tavsif lug'ati),
sensor darslari (19 ta, alohida), missiya bosqichlari (24 ta, 6 bosqich shabloni x 4 missiya),
va boshqa noyob darslar (~14 ta, alohida).

Missiyalarning ANIQ vazifasi, ball taqsimoti va maydoncha elementlari `missions.py` da.
"""

from missions import MISSIONS, topshiriq_bloki

# ---------------------------------------------------------------------------
# 1) INTRO
# ---------------------------------------------------------------------------

SPIKE_INTRO = {
"SPIKE Prime to'plami bilan tanishuv: qismlar, xavfsizlik": {
    "maqsad": [
        "O'quvchilar LEGO Education SPIKE Prime to'plami va uning asosiy qismlari bilan tanishadilar.",
        "O'quvchilar Makerzoid'dan SPIKE'ga o'tishdagi farq va o'xshashliklarni tushunadilar.",
        "O'quvchilar SPIKE bilan ishlashda xavfsizlik va tartib qoidalarini o'zlashtiradilar.",
    ],
    "lugat": [
        "Hub – SPIKE Prime ning markaziy boshqaruv bloki",
        "Motor (Motor) – harakat beruvchi qurilma",
        "Sensor (Sensor) – atrof-muhitni sezuvchi qurilma",
        "SPIKE App (SPIKE ilovasi) – dasturlash va boshqarish uchun ilova",
        "Attachment – asosiy robotga qo'shiladigan qo'shimcha qurilma",
    ],
    "softSkill": "Yangi muhitga moslashish — 4 yillik Makerzoid tajribasidan keyin yangi platformaga ochiq va qiziqish bilan yondashish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "LEGO Education SPIKE Prime Core Set (45678) — har guruhga 1 ta",
        "Taqdimot uchun kompyuter va proyektor",
        "Xavfsizlik qoidalari plakati",
    ],
    "nazariya": [
        ("Kirish", 10, ["0-4-sinf davomida Makerzoid bilan qilingan ishlar qisqacha eslanadi.", "SPIKE Prime — rasmiy LEGO Education mahsuloti ekanligi va nima uchun yangi bosqichga o'tilayotgani tushuntiriladi."]),
        ("SPIKE qismlari", 15, ["Hub, motor, sensorlar va ulash detallari ko'rsatiladi va nomlanadi.", "Makerzoid bilan solishtirilganda o'xshash va farqli tomonlari muhokama qilinadi."]),
        ("Xavfsizlik", 5, ["Elektron qismlar (Hub, motor, sensor) bilan ehtiyotkorlik bilan ishlash qoidalari eslatiladi."]),
    ],
    "amaliy": [
        ("Qismlarni tanish", 10, ["O'quvchilar Hub, motor va sensorlarni qo'lda ko'rib, ularni nomlaydilar."]),
        ("Hub'ni yoqish", 5, ["O'quvchilar Hub'ni yoqib, ekranini va tugmalarini ko'rib chiqadilar."]),
    ],
    "uyga": [
        "LEGO Education SPIKE Prime haqida internetdan bitta qiziqarli video toping va nima yangilik bilganingizni qisqacha yozing.",
    ],
},
}

# ---------------------------------------------------------------------------
# 2) ATTACHMENT / MODEL YIG'ISH (Q1, 18 ta) — umumiy shablon + tavsif lug'ati
# ---------------------------------------------------------------------------

ATTACHMENT_INFO = {
    "Driving Base 1": ("SPIKE Prime'ning eng asosiy harakatlanuvchi robot asosi — barcha keyingi loyihalar uchun poydevor", "ikki motorli harakat tizimining asosiy tuzilishi"),
    "Driving Base 2": ("harakatlanuvchi robot asosining ikkinchi (biroz farqli sensorlar joylashuviga ega) rasmiy varianti", "ikki motorli harakat tizimi va sensor joylashuvi"),
    "Driving Base 3 (Advanced Driving Base)": ("Driving Base'ning kengaytirilgan, qo'shimcha portlarga ega ilg'or varianti", "ko'proq sensor/motor sig'imi va mustahkamroq konstruksiya"),
    "StarterBot": ("SPIKE Prime bilan tez tanishish uchun mo'ljallangan, sodda va tez yig'iladigan boshlang'ich robot", "eng kam qism bilan tez yig'ilishi va darhol dasturlashga o'tish imkoni"),
    "Robot Arm (robot-qo'l)": ("narsalarni ushlab, ko'chirish uchun mo'ljallangan ko'p bo'g'inli manipulyator model", "bir nechta bo'g'inning birgalikda harakati (kinematik zanjir)"),
    "Line Follower attachment": ("Driving Base'ga o'rnatiladigan, chiziq bo'ylab yurishga mo'ljallangan sensor qo'shimchasi", "rang sensorining pastga qaratib o'rnatilishi"),
    "Ultrasonic sensor mount": ("ultratovush (masofa) sensorini Driving Base oldiga mahkamlovchi qo'shimcha qurilma", "sensorning to'g'ri balandlik va burchakda o'rnatilishi"),
    "Color sensor mount": ("rang sensorini aniq balandlikda ushlab turuvchi qo'shimcha qurilma", "sensor balandligining aniqlik darajasiga ta'siri"),
    "Bumper attachment (to'siq sezuvchi)": ("robot to'siqqa urilganda buni \"sezadigan\" mexanik to'siq-sezgich qurilma", "mexanik bosim orqali to'siqni aniqlash (sensorsiz ham mumkin)"),
    "Gripper (ushlagich) attachment": ("kichik narsalarni ushlab olish va ko'chirish uchun mo'ljallangan ushlagich qurilma", "ochilish-yopilish mexanizmi va motor bilan boshqarilishi"),
    "Tractor": ("yuk tortish va dala ishlariga mo'ljallangan, kuchli harakatlanish tizimiga ega model", "yuqori moment (kuch) beruvchi uzatma tizimi"),
    "Catapult attachment": ("kichik narsani otish uchun mo'ljallangan, elastik yoki richag asosidagi qurilma", "elastik energiya yoki richag orqali otish kuchi hosil qilish"),
    "Plow attachment (belkurak)": ("yo'ldagi kichik narsalarni surib, tozalash uchun mo'ljallangan belkurak-shakldagi qurilma", "old qismning yerga yaqin joylashuvi"),
    "Scoop attachment (cho'mich)": ("kichik narsalarni ko'tarib olish uchun mo'ljallangan cho'mich-shakldagi qurilma", "cho'michning ko'tarish burchagi va mexanizmi"),
    "Fork-lift attachment": ("yukni ko'tarib, boshqa joyga olib borish uchun mo'ljallangan forklift-uslubidagi qurilma", "richag/vint orqali tik ko'tarish mexanizmi"),
    "Ball Shooter attachment": ("kichik to'p yoki sharni otish uchun mo'ljallangan qurilma", "motor aylanishi orqali otish kuchi hosil qilish"),
    "Kriket (box robot)": ("kichik, ixcham va tez yig'iladigan \"quti\" shaklidagi sinov roboti", "minimal qismlar bilan funksional robot yaratish g'oyasi"),
    "Sensor arm attachment": ("sensorni robotdan uzoqroqqa yoki boshqa burchakka chiqarib o'rnatuvchi qo'l-shakldagi qurilma", "sensor joylashuvining aniqlashga ta'siri"),
}

def _attachment_content(name, tavsif, texnik_nuqta, first=False):
    is_driving_base = "Driving Base" in name
    return {
        "maqsad": [
            f"O'quvchilar rasmiy LEGO Education \"{name}\" modelini instruksiya bo'yicha mustaqil yig'ishni o'rganadilar.",
            f"O'quvchilar bu qurilmaning vazifasini va {texnik_nuqta} tushunadilar.",
            "O'quvchilar rasmli instruksiyaga aniq va tartibli rioya qilish ko'nikmasini rivojlantiradilar.",
        ],
        "lugat": [
            "Attachment – asosiy robotga qo'shiladigan qo'shimcha qurilma" if not is_driving_base else "Driving Base – harakatlanuvchi robot asosi (shassisi)",
            "Instruksiya (Building instructions) – rasmli, bosqichma-bosqich qurish qo'llanmasi",
            "Port (Port) – motor/sensor ulanadigan Hub uyachasi",
            "Mustahkamlik (Sturdiness) – qurilmaning mahkam va bardoshli bo'lishi",
            "Vazifa (Function) – qurilmaning nima uchun ishlatilishi",
        ],
        "softSkill": "Instruksiyaga aniq rioya qilish — rasmli qo'llanma bosqichlarini o'tkazib yubormasdan, tartib bilan bajarish ko'nikmasini mustahkamlash.",
        "resurslar": [
            "LEGO Education SPIKE Prime Core Set (45678)",
            "Rasmiy qurish instruksiyasi (SPIKE ilovasi orqali)",
            "Planshet yoki noutbuk",
        ],
        "nazariya": [
            ("Kirish", 5, [f"\"{name}\" — {tavsif} ekanligi tushuntiriladi."]),
            ("Qurilma vazifasi va tuzilishi", 7, [f"Bu qurilmaning asosiy vazifasi va {texnik_nuqta} muhokama qilinadi.", "Instruksiyadagi asosiy bosqichlar umumiy ko'rib chiqiladi."]),
            ("Yakunlash", 3, ["Yig'ilgandan keyin nima qilinishi (keyingi darslarda dasturlash) qisqacha aytiladi."]),
        ],
        "amaliy": [
            (f"{name} yig'ish", 27, [f"O'quvchilar rasmiy instruksiya bo'yicha \"{name}\" modelini bosqichma-bosqich yig'ishadi.", "Barcha qismlarning mahkam va to'g'ri ulanganligi tekshiriladi."]),
            ("Ko'rgazma", 3, ["Har bir guruh yig'ilgan qurilmani ko'rsatib, vazifasini qisqacha aytadi."]),
        ],
        "uyga": [
            f"\"{name}\" qanday real hayotiy vazifada foydali bo'lishi mumkinligi haqida qisqacha yozing.",
        ],
    }

SPIKE_ATTACHMENTS = {
    f"{name} — yig'ish (1 darslik)": _attachment_content(name, tavsif, texnik)
    for name, (tavsif, texnik) in ATTACHMENT_INFO.items()
}

# ---------------------------------------------------------------------------
# 3) SENSOR DARSLARI (Q2, 19 ta)
# ---------------------------------------------------------------------------

SPIKE_SENSOR = {

"Rang sensori bilan tanishuv": {
    "maqsad": ["O'quvchilar SPIKE rang sensorining ishlash tamoyilini tushunadilar.", "O'quvchilar sensorni Hub'ga ulab, uning qiymatlarini ilovada kuzatadilar.", "O'quvchilar sensor ma'lumotlarini o'qishni o'rganadilar."],
    "lugat": ["Rang sensori (Color sensor) – sirt rangini aniqlovchi sensor", "Port (Port) – sensor ulanadigan Hub uyachasi", "Qiymat (Value) – sensordan o'qiladigan ma'lumot", "Kalibrlash (Calibration) – sensorni aniq ishlashi uchun sozlash", "Blok (Block) – dastur buyrug'i"],
    "softSkill": "Kuzatuvchanlik — sensor qiymatlarining turli ranglarda qanday o'zgarishini diqqat bilan kuzatish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami", "Rang sensor mount (oldingi darsda yig'ilgan)", "Turli rangdagi kartoncha/yuzalar"],
    "nazariya": [("Kirish", 7, ["Rang sensori qayerlarda ishlatilishi (chiziq kuzatish, saralash) haqida savol-javob."]), ("Sensor ishlash tamoyili", 10, ["Rang sensori sirtdan qaytgan yorug'likni o'lchab, uni rangga aylantirishi tushuntiriladi."]), ("Yakunlash", 3, ["Keyingi darsda bu sensor bilan dasturlash boshlanishi aytiladi."])],
    "amaliy": [("Sensorni ulash", 10, ["O'quvchilar rang sensorini Hub portiga ulaydilar."]), ("Qiymatlarni kuzatish", 15, ["O'quvchilar turli rangdagi yuzalar ustida sensorni sinab, ilovada qiymatlarni kuzatadilar."])],
    "uyga": ["Uyda rang sensoridan foydalanadigan qurilmani (agar bilsangiz) toping va yozing."],
},

"Rangni aniqlash dasturi": {
    "maqsad": ["O'quvchilar rang sensori qiymatiga qarab qaror qabul qiluvchi dastur tuzadilar.", "O'quvchilar shart blokidan foydalanib, aniq rangga reaksiya beruvchi dastur yozadilar.", "O'quvchilar dasturni turli ranglarda sinaydilar."],
    "lugat": ["Shart (Condition) – \"agar\" mantig'i", "Rang qiymati (Color value) – sensor o'qigan aniq rang", "Reaksiya (Reaction) – rangga qarab bajariladigan harakat", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Mantiqiy dasturlash — sensor ma'lumotini shart orqali harakatga bog'lash ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami", "Planshet/noutbuk (SPIKE ilovasi)", "Turli rangdagi kartonchalar"],
    "nazariya": [("Kirish", 7, ["O'tgan darsdagi rang sensori qiymatlari eslanadi."]), ("Rangga qarab qaror qabul qilish", 10, ["\"Agar rang qizil bo'lsa -> to'xta\" kabi mantiq tushuntiriladi va namoyish qilinadi."]), ("Yakunlash", 3, ["Bu mantiqning chiziq kuzatish va saralashda qo'llanilishi aytiladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar kamida 2 xil rangga turlicha reaksiya beruvchi dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar dasturni turli rangdagi yuzalarda sinaydilar."])],
    "uyga": ["Rang sensoridan foydalanib qanday foydali qurilma yasash mumkinligi haqida g'oya yozing."],
},

"Line Follower — dasturlash nazariyasi": {
    "maqsad": ["O'quvchilar chiziq kuzatuvchi (line follower) dasturning ishlash mantig'ini tushunadilar.", "O'quvchilar rang sensori ma'lumotidan robotni to'g'irlashda qanday foydalanishni o'rganadilar.", "O'quvchilar dastur algoritmini qog'ozda rejalashtiradilar."],
    "lugat": ["Line Follower – chiziq bo'ylab yuruvchi robot dasturi", "Chegara qiymat (Threshold) – oq va qora orasidagi ajratuvchi qiymat", "Tuzatish (Correction) – robotni chiziqqa qaytaruvchi harakat", "Algoritm (Algorithm) – dastur mantig'ining qadamlari", "Sensor (Sensor) – rang/yorug'lik sezuvchi qurilma"],
    "softSkill": "Oldindan rejalashtirish — dasturni yozishdan oldin uning mantig'ini qog'ozda tuzish odatini shakllantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami", "Qog'oz va qalam", "Taqdimot uchun kompyuter va proyektor"],
    "nazariya": [("Kirish", 7, ["Chiziq kuzatuvchi robotlar qayerlarda ishlatilishi (omborlar, zavodlar) haqida suhbat."]), ("Ishlash mantig'i", 10, ["Sensor chiziqdan chetga chiqsa, robot qarama-qarshi tomonga burilib tuzatishi (oddiy \"agar...bo'lsa\" mantig'i) tushuntiriladi."]), ("Yakunlash", 3, ["Keyingi ikkita darsda bu mantiq amalda dasturlanishi aytiladi."])],
    "amaliy": [("Algoritmni rejalashtirish", 15, ["O'quvchilar chiziq kuzatish algoritmini qadamma-qadam qog'ozga yozadilar."]), ("Muhokama", 10, ["Rejalar juftlikda solishtiriladi va muhokama qilinadi."])],
    "uyga": ["Rejangizni yakunlab, keyingi darsga tayyor holda olib keling."],
},

"Line Follower — dasturlash 1": {
    "maqsad": ["O'quvchilar o'tgan darsdagi rejaga asosan chiziq kuzatuvchi dasturni yoza boshlaydilar.", "O'quvchilar rang sensori qiymatiga qarab motorlarni boshqaradilar.", "O'quvchilar dasturning dastlabki qismini sinaydilar."],
    "lugat": ["Line Follower dasturi (Line follower program) – chiziq bo'ylab yurish dasturi", "Motor boshqaruvi (Motor control) – ikkala motorga alohida buyruq berish", "Shart (Condition) – \"agar\" mantig'i", "Sensor qiymati (Sensor value) – rang sensoridan o'qilgan son", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Bosqichma-bosqich ijro — rejani ketma-ket, shoshilmasdan kod bilan amalga oshirish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (Line Follower attachment bilan)", "Planshet/noutbuk (SPIKE ilovasi)", "Qora chiziqli trassa (qog'ozda yoki lentada)"],
    "nazariya": [("Kirish", 7, ["O'tgan darsdagi reja qisqacha eslanadi."]), ("Dasturni boshlash", 10, ["Rang sensori qiymatiga qarab ikkala motorni boshqarish bloklari ko'rsatiladi."]), ("Yakunlash", 3, ["Bugungi maqsad — dasturning asosiy qismini yozish ekanligi aytiladi."])],
    "amaliy": [("Dastur yozish", 20, ["O'quvchilar rejaga asosan chiziq kuzatish dasturining asosiy qismini yozadilar."]), ("Qisman sinov", 5, ["O'quvchilar dasturni trassada qisman sinab ko'radilar."])],
    "uyga": ["Dasturingizning qaysi qismini yakunlaganingizni va nimalar qolganini yozing."],
},

"Line Follower — dasturlash 2 va sinov": {
    "maqsad": ["O'quvchilar chiziq kuzatuvchi dasturni yakunlaydilar.", "O'quvchilar dasturni to'liq trassada sinab, xatolarni tuzatadilar.", "O'quvchilar natijani sinfga namoyish etadilar."],
    "lugat": ["Yakunlash (Finalize) – dasturni tugallangan holatga keltirish", "Tuzatish (Fix) – xatoni bartaraf etish", "Trassa (Track) – chiziq chizilgan sinov yo'lagi", "Sinov (Test) – dasturni tekshirish", "Namoyish (Demonstration) – natijani ko'rsatish"],
    "softSkill": "Qat'iyat — dastur birinchi urinishda ishlamasa ham, uni tuzatishga davom etish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (Line Follower attachment bilan)", "Planshet/noutbuk (SPIKE ilovasi)", "To'liq qora chiziqli trassa"],
    "nazariya": [("Kirish", 5, ["O'tgan darsdagi dastur holati eslanadi."]), ("Nozik sozlash", 5, ["Chegara qiymatini (threshold) sozlash orqali dasturni aniqroq qilish tushuntiriladi."])],
    "amaliy": [("Dasturni yakunlash", 20, ["O'quvchilar dasturni to'liq yozib tugatadilar."]), ("Sinov va namoyish", 15, ["O'quvchilar dasturni to'liq trassada sinab, natijasini sinfga ko'rsatadilar."])],
    "uyga": ["Chiziq kuzatuvchi robotni yanada tezroq qilish uchun qanday o'zgartirish kiritish mumkinligi haqida yozing."],
},

"Ultrasonic sensor — dasturlash": {
    "maqsad": ["O'quvchilar ultratovush (masofa) sensoridan foydalangan dastur tuzadilar.", "O'quvchilar sensor to'siqgacha bo'lgan masofani qanday o'lchashini tushunadilar.", "O'quvchilar to'siqni sezib to'xtaydigan/aylanib o'tadigan dastur yozadilar."],
    "lugat": ["Ultrasonic sensor – tovush signali yordamida masofani o'lchovchi sensor", "Masofa (Distance) – sensor va to'siq orasidagi uzunlik", "Shart (Condition) – \"agar\" mantig'i", "Chegara masofa (Distance threshold) – reaksiya boshlanadigan masofa", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Ilmiy tushuntirish — sensorning fizik ishlash tamoyilini (tovush signali) o'z so'zi bilan tushuntirish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (Ultrasonic sensor mount bilan)", "Planshet/noutbuk (SPIKE ilovasi)", "To'siq (quti yoki devor)"],
    "nazariya": [("Kirish", 7, ["Ultratovush sensori tovush signali yuborib, uning qaytish vaqtidan masofani hisoblashi tushuntiriladi."]), ("Dastur mantig'i", 10, ["\"Agar masofa 10 sm dan kam bo'lsa -> to'xta\" kabi mantiq ko'rsatiladi."]), ("Yakunlash", 3, ["Bu sensorning avtomobillarda (parktronik) qo'llanilishi aytiladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar to'siqni sezib to'xtaydigan dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar to'siq masofasini o'zgartirib, dastur reaksiyasini sinaydilar."])],
    "uyga": ["Ultratovush sensoridan foydalanadigan real qurilmalarni (parktronik, avtomatik eshik) ro'yxat qiling."],
},

"Bumper attachment — to'siqni sezib to'xtash dasturi": {
    "maqsad": ["O'quvchilar bumper (mexanik to'siq-sezgich) qurilmasidan foydalangan dastur tuzadilar.", "O'quvchilar mexanik sensor bilan elektron sensor orasidagi farqni tushunadilar.", "O'quvchilar dasturni sinab, to'siqqa to'g'ri reaksiya berishini tekshiradilar."],
    "lugat": ["Bumper – mexanik to'siq-sezgich qurilma", "Touch/Force sensor – bosimni aniqlovchi elektron sensor", "Mexanik sezish (Mechanical sensing) – jismoniy bosim orqali aniqlash", "Shart (Condition) – \"agar\" mantig'i", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Taqqoslash ko'nikmasi — mexanik va elektron sensor turlarini solishtirib, har birining afzalliklarini muhokama qilish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (Bumper attachment bilan)", "Planshet/noutbuk (SPIKE ilovasi)", "To'siq"],
    "nazariya": [("Kirish", 7, ["Bumper mexanik tarzda (elektron sensorsiz ham) to'siqni qanday sezishi tushuntiriladi."]), ("Dastur mantig'i", 10, ["Bumper bosilganda robot to'xtashi yoki orqaga qaytishi kabi dastur ko'rsatiladi."]), ("Yakunlash", 3, ["Mexanik va elektron sensorlarning har birining o'z o'rni borligi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar bumper bosilganda robot orqaga qaytadigan dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar dasturni to'siqqa urilib sinaydilar."])],
    "uyga": ["Mexanik sensor (bumper kabi) ishlatiladigan real qurilmalarni toping."],
},

"Gripper — ushlab olish dasturi": {
    "maqsad": ["O'quvchilar gripper (ushlagich) attachmentini dastur orqali boshqaradilar.", "O'quvchilar motor yordamida ochilish-yopilish harakatini dasturlaydilar.", "O'quvchilar kichik narsani ushlab olish va qo'yib yuborish dasturini sinaydilar."],
    "lugat": ["Gripper – ushlab olish uchun mo'ljallangan qurilma", "Motor burchagi (Motor angle) – motorning necha darajaga aylanishi", "Ushlash (Grip) – narsani mahkam tutish", "Bo'shatish (Release) – ushlangan narsani qo'yib yuborish", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Aniq boshqaruv — motor harakatini aniq miqdorda sozlab, kerakli natijaga erishish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (Gripper attachment bilan)", "Planshet/noutbuk (SPIKE ilovasi)", "Kichik LEGO detal (ushlash uchun namuna)"],
    "nazariya": [("Kirish", 7, ["Gripperning vazifasi (kichik narsalarni ushlab ko'chirish) eslanadi."]), ("Motor bilan boshqarish", 10, ["Motorni aniq burchakka aylantirish orqali ochilish-yopilishni boshqarish ko'rsatiladi."]), ("Yakunlash", 3, ["Gripperning omborlarda robot-qo'llar tomonidan ishlatilishi aytiladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar gripperni ochish va yopish dasturini tuzadilar."]), ("Sinov", 10, ["O'quvchilar kichik detalni ushlab, boshqa joyga qo'yib ko'radilar."])],
    "uyga": ["Gripperdan foydalanib qanday foydali vazifani bajarish mumkinligi haqida g'oya yozing."],
},

"Kuch (bosim) sensori bilan ishlash": {
    "maqsad": ["O'quvchilar kuch (bosim/force) sensorining ishlash tamoyilini tushunadilar.", "O'quvchilar sensor bosim qiymatiga qarab reaksiya beruvchi dastur tuzadilar.", "O'quvchilar dasturni turli bosim darajalarida sinaydilar."],
    "lugat": ["Kuch sensori (Force sensor) – bosimni o'lchovchi sensor", "Bosim qiymati (Force value) – sensorga qo'yilgan bosim miqdori", "Chegara qiymat (Threshold) – reaksiya boshlanadigan bosim darajasi", "Shart (Condition) – \"agar\" mantig'i", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Miqdoriy tahlil — sensor ko'rsatkichlarini son sifatida tahlil qilib, chegara qiymatini tanlash ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (Force sensor bilan)", "Planshet/noutbuk (SPIKE ilovasi)"],
    "nazariya": [("Kirish", 7, ["Kuch sensori qayerlarda ishlatilishi (lift tugmasi, o'lchov asboblari) haqida savol-javob."]), ("Sensor ishlash tamoyili", 10, ["Sensorga qo'yilgan bosim qanday songa aylanishi va bu songa qarab dastur qaror qabul qilishi tushuntiriladi."]), ("Yakunlash", 3, ["Bosim sensorining boshqa sensorlardan farqi (teginish kerakligi) umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar bosim sensori qiymatiga qarab harakat qiluvchi dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar sensorga turli kuch bilan bosib, natijani kuzatadilar."])],
    "uyga": ["Kuch sensoridan foydalanadigan real qurilmani (masalan, tarozi) toping."],
},

"Gyroskopik sensor bilan aniq burilish": {
    "maqsad": ["O'quvchilar Hub ichidagi gyroskopik sensorning ishlash tamoyilini tushunadilar.", "O'quvchilar gyroskop yordamida robotni aniq burchakka burish dasturini tuzadilar.", "O'quvchilar burilish aniqligini vaqt asosidagi usul bilan solishtiradilar."],
    "lugat": ["Gyroskopik sensor (Gyro sensor) – burchak tezligini o'lchovchi ichki sensor", "Burchak (Angle) – burilish darajasi (masalan 90°)", "Aniq burilish (Precise turn) – aniq belgilangan burchakka burilish", "Kalibrlash (Calibration) – sensorni nolga sozlash", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Aniqlikka intilish — vaqtga asoslangan taxminiy usuldan aniqroq, sensorga asoslangan usulga o'tish afzalligini tushunish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (Hub, ichki gyroskop)", "Planshet/noutbuk (SPIKE ilovasi)"],
    "nazariya": [("Kirish", 7, ["Robot burilishida vaqt bilan hisoblash nega har doim aniq emasligi (batareya holati, sirt) haqida savol-javob."]), ("Gyroskop bilan burilish", 10, ["Gyroskopik sensor robotning qancha burilganini aniq o'lchashi va \"90 gradusga burilguncha\" mantig'i tushuntiriladi."]), ("Yakunlash", 3, ["Gyroskopning telefonlar va dronlarda ham ishlatilishi aytiladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar gyroskop yordamida aniq 90° burilish dasturini tuzadilar."]), ("Sinov", 10, ["O'quvchilar vaqtga asoslangan va gyroskopga asoslangan burilishni solishtirib sinaydilar."])],
    "uyga": ["Gyroskop nega vaqtga asoslangan usuldan aniqroq ekanini o'z so'zingiz bilan tushuntirib yozing."],
},

"Bir nechta sensorni birlashtirish": {
    "maqsad": ["O'quvchilar ikki yoki undan ortiq sensordan bir dasturda birgalikda foydalanadilar.", "O'quvchilar sensorlar orasidagi ustuvorlikni (qaysi birinchi tekshirilishi) rejalashtiradilar.", "O'quvchilar dasturni turli sensor kombinatsiyalarida sinaydilar."],
    "lugat": ["Sensor kombinatsiyasi (Sensor combination) – bir nechta sensordan birga foydalanish", "Ustuvorlik (Priority) – qaysi shart birinchi tekshirilishi", "VA/YOKI (AND/OR) – mantiqiy operatorlar", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Murakkab tizimli fikrlash — bir nechta ma'lumot manbaini birgalikda boshqarish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (kamida 2 xil sensor bilan)", "Planshet/noutbuk (SPIKE ilovasi)"],
    "nazariya": [("Kirish", 7, ["Haqiqiy avtonom robotlar odatda bir nechta sensordan birga foydalanishi haqida suhbat."]), ("Sensorlarni birlashtirish", 10, ["Masofa va rang sensorlarini bitta dasturda qanday birga ishlatish mumkinligi ko'rsatiladi."]), ("Yakunlash", 3, ["Bu yondashuvning robotni yanada ishonchli qilishi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar kamida 2 sensordan foydalangan dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar turli sensor kombinatsiyalarida dasturni sinaydilar."])],
    "uyga": ["Ikki sensordan birga foydalanadigan real hayotiy tizimni (masalan, aqlli uy) toping."],
},

"Qaror qabul qilish dasturi (agar...aks holda)": {
    "maqsad": ["O'quvchilar \"agar...aks holda\" (if-else) tuzilmasidan foydalangan qaror qabul qiluvchi dastur tuzadilar.", "O'quvchilar sensorning ikki xil natijasiga ikki xil reaksiya beradigan dastur yozadilar.", "O'quvchilar dasturni ikkala holatda ham sinaydilar."],
    "lugat": ["Agar...aks holda (If...else) – shart to'g'ri bo'lmasa bajariladigan muqobil harakat", "Qaror qabul qilish (Decision making) – shartlar asosida harakat tanlash", "Sensor (Sensor) – atrof-muhitni sezuvchi qurilma", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Muqobil fikrlash — faqat bitta emas, ikkala natijani ham hisobga olib dastur tuzish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami", "Planshet/noutbuk (SPIKE ilovasi)"],
    "nazariya": [("Kirish", 7, ["\"Agar\" bilan cheklanib qolish noqulayligi (aks holda nima bo'ladi?) haqida savol-javob."]), ("Agar...aks holda", 10, ["\"Agar sensor A qiymatni bersa -> harakat 1, aks holda -> harakat 2\" mantig'i ko'rsatiladi."]), ("Yakunlash", 3, ["Bu tuzilmaning dasturni to'liqroq qilishi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar \"agar...aks holda\" tuzilmasidan foydalangan dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar ikkala holatni ham sinaydilar."])],
    "uyga": ["\"Agar...aks holda\" mantig'iga mos kundalik hayot misolini yozing."],
},

"Sensorlar bo'yicha amaliy mashq — 1": {
    "maqsad": ["O'quvchilar o'rgangan sensorlardan (rang, masofa, bosim, gyroskop) birini tanlab, mustaqil kichik vazifa bajaradilar.", "O'quvchilar sensor tanlash va uni dasturga bog'lash jarayonini mustaqil amalga oshiradilar.", "O'quvchilar natijani sinab, sinfga ko'rsatadilar."],
    "lugat": ["Amaliy mashq (Practical exercise) – mustaqil bajariladigan kichik vazifa", "Sensor tanlash (Sensor selection) – vazifaga mos sensorni aniqlash", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish", "Namoyish (Demonstration) – natijani ko'rsatish"],
    "softSkill": "Mustaqil qaror qabul qilish — vazifaga qaysi vosita (sensor) mos kelishini o'zi tanlash ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (barcha sensorlar bilan)", "Planshet/noutbuk (SPIKE ilovasi)"],
    "nazariya": [("Kirish", 7, ["Bu darsgacha o'rganilgan barcha sensorlar ro'yxati eslanadi."]), ("Vazifa tanlash", 10, ["O'quvchilarga bir nechta kichik vazifa varianti taklif qilinadi (masalan, \"to'siqdan qoch\" yoki \"rangni aniqla\")."]), ("Yakunlash", 3, ["Har bir o'quvchi/juftlik o'z vazifasini tanlaydi."])],
    "amaliy": [("Dastur yozish", 20, ["O'quvchilar tanlagan vazifasi uchun mustaqil dastur tuzadilar."]), ("Sinov", 5, ["O'quvchilar dasturni qisman sinab ko'radilar."])],
    "uyga": ["Vazifangizni yakunlash uchun nima qilish kerakligini rejalashtirib yozing."],
},

"Sensorlar bo'yicha amaliy mashq — 2": {
    "maqsad": ["O'quvchilar o'tgan darsda boshlagan mustaqil vazifasini yakunlaydilar.", "O'quvchilar dasturni to'liq sinab, xatolarni tuzatadilar.", "O'quvchilar natijasini sinfga namoyish etadilar."],
    "lugat": ["Yakunlash (Finalize) – vazifani tugallangan holatga keltirish", "Tuzatish (Fix) – xatoni bartaraf etish", "Sinov (Test) – dasturni tekshirish", "Namoyish (Demonstration) – natijani ko'rsatish", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Ishni yakunlash mas'uliyati — boshlangan vazifani oxirigacha yetkazish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami", "Planshet/noutbuk (SPIKE ilovasi)"],
    "nazariya": [("Kirish", 5, ["O'tgan darsdagi vazifa holati eslanadi."]), ("Yakuniy tekshiruv", 5, ["Dasturni to'liq sinash tartibi eslatiladi."])],
    "amaliy": [("Yakunlash", 20, ["O'quvchilar dasturni to'liq yozib, sinaydilar va xatolarni tuzatadilar."]), ("Namoyish", 15, ["Har bir o'quvchi/juftlik natijasini sinfga ko'rsatadi."])],
    "uyga": ["Bajargan vazifangizni yanada yaxshilash uchun bitta g'oya yozing."],
},

"Kichik loyiha: aqlli parking robot": {
    "maqsad": ["O'quvchilar aqlli parking robotini loyihalashni boshlaydilar.", "O'quvchilar kamida 2 ta sensordan foydalanish rejasini tuzadilar.", "O'quvchilar loyihaning asosiy qurilish qismini yakunlaydilar."],
    "lugat": ["Parking robot (Parking robot) – mashinani to'g'ri joyga qo'yishga yordam beruvchi robot", "Loyiha rejasi (Project plan) – ishni bajarishdan oldingi qadamlar", "Sensor kombinatsiyasi (Sensor combination) – bir nechta sensordan foydalanish", "Attachment – qo'shimcha qurilma", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Real muammoga yechim topish — kundalik hayotdagi muammoni (parking) texnik yechim orqali hal qilishga undash.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami", "Qog'oz va qalam (reja uchun)", "Kichik \"parking joy\" maketi (ixtiyoriy)"],
    "nazariya": [("Kirish", 7, ["Aqlli parking tizimlari haqiqiy hayotda qanday ishlashi haqida qisqacha suhbat."]), ("Loyiha rejasi", 10, ["O'quvchilar qaysi sensorlardan (masofa, rang) foydalanishlarini va robot qanday ishlashini rejalashtiradilar."]), ("Yakunlash", 3, ["Bugungi maqsad — qurilish qismini boshlash ekanligi aytiladi."])],
    "amaliy": [("Qurish", 20, ["O'quvchilar parking robotining asosiy qismini quradilar va sensorlarni joylashtiradilar."]), ("Reja tekshiruvi", 5, ["O'qituvchi bilan reja qisqacha ko'rib chiqiladi."])],
    "uyga": ["Loyihangiz uchun dastur rejasini (qaysi shartlar kerakligini) yozib keling."],
},

"Loyihani dasturlash va sinash": {
    "maqsad": ["O'quvchilar aqlli parking robotini to'liq dasturlaydilar.", "O'quvchilar loyihani turli sharoitda sinaydilar va xatolarni tuzatadilar.", "O'quvchilar loyihasini sinfga namoyish etadilar."],
    "lugat": ["Dasturlash (Programming) – rejani kod bilan amalga oshirish", "Sinov (Test) – dasturni tekshirish", "Tuzatish (Fix) – xatoni bartaraf etish", "Namoyish (Demonstration) – natijani ko'rsatish", "Loyiha (Project) – yakunlangan ish"],
    "softSkill": "Yakuniy sifat nazorati — loyihani topshirishdan oldin to'liq tekshirib chiqish odatini shakllantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami", "Planshet/noutbuk (SPIKE ilovasi)", "\"Parking joy\" maketi"],
    "nazariya": [("Kirish", 5, ["O'tgan darsdagi reja va qurilgan qism eslanadi."]), ("Dasturlash rejasi", 5, ["Qaysi bloklar qaysi tartibda yozilishi qisqacha eslatiladi."])],
    "amaliy": [("Dasturlash", 20, ["O'quvchilar parking robotini to'liq dasturlaydilar."]), ("Sinov va namoyish", 15, ["O'quvchilar robotni sinab, natijasini sinfga ko'rsatadilar."])],
    "uyga": ["Loyihangizni ota-onangizga ko'rsatib, ularning fikrini yozib keling."],
},

"Chorak yakuni: sensorlar bo'yicha takrorlash": {
    "maqsad": ["O'quvchilar chorak davomida o'rgangan barcha sensorlarni (rang, masofa, bosim, gyroskop) eslaydilar va mustahkamlaydilar.", "O'quvchilar har bir sensorning vazifasini qisqacha tushuntirib beradilar.", "O'quvchilar nazorat ishiga tayyorlanadilar."],
    "lugat": ["Takrorlash (Review) – o'rganilgan mavzularni eslash", "Sensor turlari (Sensor types) – rang, masofa, bosim, gyroskop sensorlari", "Mustahkamlash (Reinforcement) – bilimni qayta qo'llash", "Dastur (Program) – bloklar ketma-ketligi", "Nazorat ishi (Assessment) – bilim va ko'nikmani tekshirish"],
    "softSkill": "O'z bilimini tizimlashtirish — chorak davomida o'rganilgan bilimlarni tartibli ravishda eslash ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (barcha sensorlar bilan)", "Taqdimot uchun kompyuter va proyektor"],
    "nazariya": [("Kirish", 7, ["Chorak davomida o'rganilgan barcha sensorlar ro'yxati birga eslanadi."]), ("Har bir sensorni takrorlash", 10, ["Har bir sensor turi va uning ishlatilishi qisqacha qayta ko'rib chiqiladi."]), ("Yakunlash", 3, ["Keyingi dars nazorat ishi ekanligi eslatiladi."])],
    "amaliy": [("Viktorina", 15, ["O'quvchilar sensor turlari haqida savol-javob o'yinida qatnashadilar."]), ("Kichik amaliy sinov", 10, ["O'quvchilar bitta sensordan foydalangan oddiy dasturni tezkor tuzib ko'rsatadilar."])],
    "uyga": ["Nazorat ishiga tayyorgarlik ko'ring: barcha sensorlar va ularning vazifalarini qaytadan ko'rib chiqing."],
},

"Touch sensor bilan ishlash": {
    "maqsad": ["O'quvchilar touch (teginish) sensorining ishlash tamoyilini tushunadilar.", "O'quvchilar tugma bosilganda/qo'yib yuborilganda ishlaydigan dastur tuzadilar.", "O'quvchilar dasturni sinab, natijani kuzatadilar."],
    "lugat": ["Touch sensor – bosilganda/qo'yib yuborilganda signal beruvchi sensor", "Bosilgan holat (Pressed state) – tugma bosilgan vaziyat", "Qo'yib yuborilgan holat (Released state) – tugma bosilmagan vaziyat", "Shart (Condition) – \"agar\" mantig'i", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Aniq holatlarni farqlash — sensorning ikki xil holatini (bosilgan/bosilmagan) aniq ajratish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami (Touch sensor bilan)", "Planshet/noutbuk (SPIKE ilovasi)"],
    "nazariya": [("Kirish", 7, ["Touch sensor kundalik hayotda (qo'ng'iroq tugmasi, klaviatura) qayerda ishlatilishi haqida savol-javob."]), ("Sensor holatlari", 10, ["Sensorning \"bosilgan\" va \"bosilmagan\" holatlari va ularga mos dastur bloklari ko'rsatiladi."]), ("Yakunlash", 3, ["Touch sensorning boshqa sensorlardan (masofa, rang) farqi (jismoniy teginish kerakligi) umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar tugma bosilganda robot harakat qiladigan dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar dasturni bir necha marta bosib sinaydilar."])],
    "uyga": ["Touch sensordan foydalanadigan real qurilmalarni (qo'ng'iroq, klaviatura) ro'yxat qiling."],
},

"Kombinatsiyalangan attachment sinovi": {
    "maqsad": ["O'quvchilar chorak davomida yig'ilgan attachmentlarni turli kombinatsiyada sinaydilar.", "O'quvchilar qaysi attachment qaysi vazifaga eng mos kelishini tahlil qiladilar.", "O'quvchilar keyingi (missiya) choragiga tayyorlanadilar."],
    "lugat": ["Kombinatsiya (Combination) – bir nechta attachmentni birga yoki ketma-ket sinash", "Attachment almashtirish (Attachment swap) – bir attachmentni ikkinchisiga almashtirish", "Vazifaga moslik (Task fit) – attachmentning vazifaga qanchalik mos kelishi", "Sinov (Test) – dasturni/qurilmani tekshirish", "Missiya (Mission) – bajarilishi kerak bo'lgan aniq vazifa"],
    "softSkill": "Tahliliy taqqoslash — turli yechimlarni sinab, eng mosini tanlash ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami va barcha yig'ilgan attachmentlar", "Planshet/noutbuk (SPIKE ilovasi)"],
    "nazariya": [("Kirish", 7, ["Chorak davomida yig'ilgan barcha attachmentlar ro'yxati eslanadi."]), ("Attachment almashtirish", 10, ["Driving Base'dan attachmentni tez va to'g'ri almashtirish texnikasi ko'rsatiladi."]), ("Yakunlash", 3, ["Keyingi chorakda missiyalar boshlanishi va turli attachment kerak bo'lishi aytiladi."])],
    "amaliy": [("Almashtirish mashqi", 15, ["O'quvchilar bir nechta attachmentni navbat bilan Driving Base'ga ulab-ajratib sinaydilar."]), ("Muhokama", 10, ["Qaysi attachment qanday vazifaga mosligi haqida fikr almashiladi."])],
    "uyga": ["Keyingi chorakdagi missiyalar uchun qaysi attachmentlar kerak bo'lishi mumkinligi haqida taxmin qilib yozing."],
},

}

# ---------------------------------------------------------------------------
# 4) MISSIYA BOSQICHLARI (Q3/Q4, 6 bosqich shabloni x 4 missiya = 24 ta)
# ---------------------------------------------------------------------------

def _mission_step(n, step):
    m = MISSIONS[n]
    nom = m["nom"]
    common_lugat = ["Missiya (Mission) – bajarilishi kerak bo'lgan aniq vazifa", "Ball (Points) – vazifa bajarilgani uchun beriladigan miqdor", "Attachment – vazifani bajarish uchun robotga qo'shiladigan qurilma", "Musobaqa maydonchasi (Competition field) – missiya elementlari joylashgan maydon", "Jamoa (Team) – birga ishlaydigan o'quvchilar guruhi"]
    resurslar = ["LEGO Education SPIKE Prime to'plami va attachmentlar", f"Musobaqa maydonchasi 200x100 sm ({n}-missiya elementlari o'rnatilgan)", "Planshet/noutbuk (SPIKE ilovasi)"]
    if step == "reja":
        return {
            "maqsad": [f"O'quvchilar {n}-missiya (\"{nom}\") vazifasini diqqat bilan tahlil qiladilar.", f"O'quvchilar missiyani 4 ta kichik topshiriqqa ({m['topshiriqlar'][0][0]}–{m['topshiriqlar'][3][0]}) bo'lib, har biriga ball va kerakli jihozni belgilaydilar.", "O'quvchilar jamoa bo'lib ishlash va vazifa taqsimotini o'rganadilar."],
            "lugat": common_lugat,
            "softSkill": "Tahliliy o'qish va rejalashtirish — vazifa shartlarini diqqat bilan o'qib, uni bosqichlarga bo'lib rejalashtirish ko'nikmasini rivojlantirish.",
            "resurslar": resurslar + ["Qog'oz va qalam (reja uchun)", "Maydoncha chizmasi (chop etilgan yoki ekranda)"],
            "nazariya": [("Kirish", 5, [f"{n}-missiya \"{nom}\" vazifasi sinfga o'qib eshittiriladi: {m['tavsif']}"]), ("Vazifani tahlil qilish", 7, [f"Maydonchadagi elementlar va ularning joylashuvi chizma orqali ko'rsatiladi ({len(m['elementlar'])} ta element).", f"4 ta kichik topshiriq va ularning balli tahlil qilinadi (jami {sum(b for _, _, b in m['topshiriqlar'])} ball).", f"Bu missiya uchun taxminan qanday attachment kerakligi muhokama qilinadi ({m['attachment']})."]), ("Yakunlash", 3, [f"Vaqt cheklovi ({m['vaqt']} soniya) eslatiladi va jamoalar ichida dastlabki vazifa taqsimoti qilinadi."])],
            "amaliy": [("Reja tuzish", 20, [f"Jamoalar {n}.A topshirig'ini bajaradilar: 4 ta kichik topshiriqni ball va kerakli jihozi bilan daftarga yozadilar.", "Topshiriqlarni bajarish tartibi raqamlanadi."]), ("Muhokama", 10, ["Har bir jamoa rejasini qisqacha o'qituvchiga tushuntiradi va tartibini asoslaydi."])],
            "uyga": [f"{n}-missiya uchun rejangizni to'ldirib, keyingi darsga tayyor holda olib keling."],
            "topshiriq": topshiriq_bloki(n, step),
            "maydon": n,
        }
    if step == "dizayn":
        return {
            "maqsad": [f"O'quvchilar {n}-missiya (\"{nom}\") uchun kerakli attachment dizaynini ishlab chiqadilar.", "O'quvchilar dizaynni tanlashda muhandislik mulohazalarini (mustahkamlik, vazifaga moslik) hisobga oladilar.", f"O'quvchilar kamida 2 xil variantni eskiz qilib, birini asoslangan holda tanlaydilar ({n}.B topshirig'i)."],
            "lugat": common_lugat,
            "softSkill": "Muhandislik dizayni fikrlashi — bir nechta dizayn variantini solishtirib, eng mosini tanlash ko'nikmasini rivojlantirish.",
            "resurslar": resurslar + ["Qog'oz va qalam (eskiz uchun)"],
            "nazariya": [("Kirish", 5, [f"{n}-missiya rejasi va {m['topshiriqlar'][1][0]} topshirig'i qisqacha eslanadi."]), ("Dizayn variantlari", 7, [f"Bu missiya uchun mos keladigan qurilma turlari muhokama qilinadi: {m['attachment']}.", "Har bir variantning afzallik va kamchiliklari solishtiriladi (mustahkamlik, tezlik, aniqlik)."]), ("Yakunlash", 3, ["Jamoa eng mos dizaynni tanlab, tanlovini bir gapda asoslaydi."])],
            "amaliy": [("Eskiz chizish", 15, [f"Jamoalar {n}.B topshirig'ini bajaradilar: 2 xil attachment eskizini chizib, har biriga afzallik va kamchilik yozadilar."]), ("Tanlov va muhokama", 15, ["Jamoa bittasini tanlaydi va tanlovini o'qituvchiga asoslab beradi."])],
            "uyga": [f"{n}-missiya attachmenti uchun tanlangan eskizni toza qog'ozga ko'chirib, keyingi darsga olib keling."],
            "topshiriq": topshiriq_bloki(n, step),
            "maydon": n,
        }
    if step == "yigish":
        return {
            "maqsad": [f"O'quvchilar {n}-missiya uchun tanlangan attachment dizaynini jismonan yig'adilar.", "O'quvchilar yig'ilgan attachmentning mustahkam va Driving Base'ga to'g'ri ulanishini ta'minlaydilar.", "O'quvchilar attachmentni dastlabki sinovdan o'tkazadilar."],
            "lugat": common_lugat,
            "softSkill": "Amaliy ijro — eskizdan haqiqiy qurilmaga o'tish jarayonida aniqlik va sabr-toqatni saqlash ko'nikmasini rivojlantirish.",
            "resurslar": resurslar,
            "nazariya": [("Kirish", 5, ["O'tgan darsdagi dizayn eskizi eslanadi."]), ("Yig'ish rejasi", 5, ["Attachmentni qanday tartibda yig'ish qulayligi qisqacha muhokama qilinadi.", f"Bugungi maqsad — {n}.C topshirig'i: attachment DASTURSIZ, qo'lda ishlashi kerak."])],
            "amaliy": [("Attachment yig'ish", 25, [f"Jamoalar {n}-missiya uchun attachmentni eskiz asosida yig'adilar.", "Attachment Driving Base'ga mahkam ulanganligi tekshiriladi."]), ("Mexanik sinov", 5, [f"Robot qo'lda surib maydonchadan o'tkaziladi va {m['topshiriqlar'][1][0]} topshirig'i qo'lda bajarib ko'riladi."])],
            "uyga": [f"Yig'ilgan {n}-missiya attachmentingizning rasmini oling yoki chizing."],
            "topshiriq": topshiriq_bloki(n, step),
            "maydon": n,
        }
    if step == "dasturlash":
        return {
            "maqsad": [f"O'quvchilar {n}-missiyani bajarish uchun to'liq dasturni yozadilar.", "O'quvchilar Driving Base harakati va attachment ishini bitta dasturda birlashtiradilar.", "O'quvchilar dasturni qisman sinab ko'radilar."],
            "lugat": common_lugat[:4] + ["Dastur (Program) – bloklar ketma-ketligi"],
            "softSkill": "Kod orqali g'oyani amalga oshirish — rejalashtirilgan harakatlarni aniq dastur bloklariga aylantirish ko'nikmasini rivojlantirish.",
            "resurslar": resurslar,
            "nazariya": [("Kirish", 5, [f"{n}-missiya rejasi va yig'ilgan attachment eslanadi."]), ("Dastur tuzilishi", 10, ["Driving Base harakati (masofa/burilish) va attachment harakati (motor) qanday birlashtirilishi ko'rsatiladi.", f"Bu missiyada ishlatiladigan sensorlar: {m['sensorlar']}."]), ("Yakunlash", 3, [f"Bugungi maqsad — {n}.D topshirig'i: birinchi IKKI topshiriqni bitta dasturda bajarish."])],
            "amaliy": [("Dastur yozish", 22, [f"Jamoalar {m['topshiriqlar'][0][0]} va {m['topshiriqlar'][1][0]} topshiriqlarini bitta dasturda yozadilar.", f"Ulgurgan jamoalar {m['topshiriqlar'][2][0]} uchun bloklarni boshlaydilar."]), ("Qisman sinov", 3, ["Yozilgan qism maydonchada sinab ko'riladi."])],
            "uyga": [f"{n}-missiya dasturingizning eng qiyin qismi qaysi ekanini va nega ekanini yozing."],
            "topshiriq": topshiriq_bloki(n, step),
            "maydon": n,
        }
    if step == "sinov":
        return {
            "maqsad": [f"O'quvchilar {n}-missiya uchun tayyorlagan robot va dasturni to'liq sinovdan o'tkazadilar.", "O'quvchilar aniqlangan xatolarni (mexanik yoki dasturiy) tuzatadilar.", "O'quvchilar natijani takroriy sinab, barqarorlikka erishadilar."],
            "lugat": common_lugat[:3] + ["Xato (Bug/Error) – kutilmagan noto'g'ri natija", "Barqarorlik (Consistency) – har safar bir xil natija berish"],
            "softSkill": "Barqarorlikka intilish — bir marta ishlashi bilan cheklanmasdan, bir necha marta takrorlab sinab ishonchni oshirish ko'nikmasini rivojlantirish.",
            "resurslar": resurslar,
            "nazariya": [("Kirish", 5, [f"{n}-missiya dasturi va attachmenti eslanadi."]), ("Tizimli sinov", 5, [f"Bugungi maqsad — {n}.E topshirig'i: 4 ta topshiriqni to'liq bajarish va 3 marta ketma-ket sinab, natija bir xilligini tekshirish."])],
            "amaliy": [("Sinov", 20, [f"Jamoalar {n}-missiyani maydonchada 3 marta ketma-ket sinaydilar.", "Har bir urinishda nechta topshiriq bajarilgani va sarflangan vaqt jadvalga yoziladi."]), ("Tuzatish", 15, ["Takrorlanadigan xatoning sababi (mexanik yoki dasturiy) aniqlanib, tuzatiladi va qayta sinaladi."])],
            "uyga": [f"{n}-missiyada aniqlagan va tuzatgan bitta xatoni tasvirlab yozing."],
            "topshiriq": topshiriq_bloki(n, step),
            "maydon": n,
        }
    if step == "yakuniy":
        return {
            "maqsad": [f"O'quvchilar {n}-missiyani rasmiy qoidalar asosida yakuniy marta bajarib, ball oladilar.", "O'quvchilar musobaqa formatidagi bosim ostida tinch va tizimli ishlaydilar.", "O'quvchilarda natija uchun mas'uliyat va sportchan munosabat rivojlanadi."],
            "lugat": common_lugat[:4] + ["Baholash mezoni (Grading criteria) – ball qo'yish qoidalari"],
            "softSkill": "Bosim ostida ishlash — baholanayotganini bilgan holda ham tinch va tizimli harakat qilish ko'nikmasini rivojlantirish.",
            "resurslar": resurslar + ["Ball jadvali"],
            "nazariya": [("Kirish", 5, [f"{n}-missiyaning rasmiy baholash qoidalari eslatiladi: 4 ta topshiriq, jami {sum(b for _, _, b in m['topshiriqlar'])} ball, vaqt {m['vaqt']} soniya.", "Har bir jamoaga 2 ta urinish berilishi va yaxshirog'i hisobga olinishi aytiladi."]), ("Yakuniy tayyorgarlik", 5, ["Robot va attachment yakuniy marta tekshiriladi, batareya quvvati nazorat qilinadi."])],
            "amaliy": [("Yakuniy urinish", 15, [f"Har bir jamoa {n}-missiyani rasmiy qoidalar asosida bajaradi (2 urinish).", "Har bir topshiriq alohida belgilanadi — qisman bajarilgan topshiriq uchun ball berilmaydi."]), ("Ball qo'yish va muhokama", 20, ["O'qituvchi natijani topshiriqlar jadvali bo'yicha ballga aylantiradi.", "Qaysi topshiriq bajarilmagani va nima uchun — jamoa bilan muhokama qilinadi."])],
            "uyga": [f"{n}-missiyadagi natijangizdan nimani o'rganganingizni yozing."],
            "topshiriq": topshiriq_bloki(n, step),
            "maydon": n,
        }
    raise ValueError(step)

MISSION_STEP_TITLES = {
    "reja": "vazifa tahlili va reja",
    "dizayn": "attachment dizayni",
    "yigish": "attachment yig'ish",
    "dasturlash": "dasturlash",
    "sinov": "sinov va tuzatish",
    "yakuniy": "yakuniy sinov (ballga qo'yiladi)",
}

def mission_lesson_title(n, step):
    """tree_data.js dagi dars sarlavhasi bilan AYNAN bir xil bo'lishi shart."""
    return f"Missiya {n} — {MISSIONS[n]['nom']}: {MISSION_STEP_TITLES[step]}"


SPIKE_MISSIONS = {}
for _n in [1, 2, 3, 4]:
    for _step in MISSION_STEP_TITLES:
        SPIKE_MISSIONS[mission_lesson_title(_n, _step)] = _mission_step(_n, _step)

# ---------------------------------------------------------------------------
# 5) BOSHQA NOYOB DARSLAR (Q3/Q4, ~14 ta)
# ---------------------------------------------------------------------------

SPIKE_MISC = {

"FLL / musobaqa maydonchasi bilan tanishuv": {
    "maqsad": ["O'quvchilar FLL (First Lego League) uslubidagi musobaqa maydonchasi bilan tanishadilar.", "O'quvchilar maydoncha elementlari va ularning har biri qaysi missiyaga tegishli ekanini o'rganadilar.", "O'quvchilar bu chorakda ishlaydigan formatga tayyorlanadilar."],
    "lugat": ["FLL (First Lego League) – maktab yoshidagi bolalar uchun xalqaro robototexnika musobaqasi", "Musobaqa maydonchasi (Competition field) – missiya elementlari joylashgan maxsus maydon", "Missiya (Mission) – maydonchadagi bajarilishi kerak bo'lgan aniq vazifa", "Baza (Home base) – robot boshlanadigan va qaytadigan hudud", "Ball (Points) – vazifa uchun beriladigan miqdor"],
    "softSkill": "Musobaqa madaniyati bilan tanishish — xalqaro miqyosdagi robototexnika musobaqalarining qoidalari va ruhini tushunish.",
    "resurslar": ["Musobaqa maydonchasi (yoki uning rasmi/maketi)", "Taqdimot uchun kompyuter va proyektor", "FLL haqida video (agar mavjud bo'lsa)"],
    "nazariya": [("Kirish", 7, ["FLL nima ekanligi va dunyoda qanday o'tkazilishi haqida qisqacha video/rasm ko'rsatiladi."]), ("Maydoncha tuzilishi", 10, ["Maydonchadagi baza, missiya elementlari va ularning umumiy joylashuvi ko'rsatiladi."]), ("Yakunlash", 3, ["Bu chorakda 1 va 2-missiya bilan ishlashlari aytiladi."])],
    "amaliy": [("Maydonchani o'rganish", 15, ["O'quvchilar maydoncha (yoki uning maketi/rasmi) bo'ylab elementlarni ko'rib chiqadilar."]), ("Muhokama", 10, ["Qaysi missiya qiziqroq ko'rinishi haqida fikr almashiladi."])],
    "uyga": ["FLL musobaqasi haqida internetdan bitta qiziqarli video yoki rasm toping."],
},

"Missiya nima? Ball tizimi bilan tanishuv": {
    "maqsad": ["O'quvchilar \"missiya\" tushunchasi va ball tizimi qanday ishlashini tushunadilar.", "O'quvchilar missiyaning muvaffaqiyatli/muvaffaqiyatsiz bajarilishi orasidagi farqni biladilar.", "O'quvchilar o'z jamoasi uchun ball strategiyasi haqida dastlabki fikr yuritadilar."],
    "lugat": ["Missiya (Mission) – bajarilishi kerak bo'lgan aniq vazifa", "Ball tizimi (Scoring system) – har bir missiya uchun beriladigan ball miqdori", "Muvaffaqiyatli bajarish (Successful completion) – missiyaning to'liq va to'g'ri bajarilishi", "Strategiya (Strategy) – qaysi missiyalarga ustuvorlik berish rejasi", "Jamoa (Team) – birga ishlaydigan o'quvchilar guruhi"],
    "softSkill": "Strategik fikrlash — cheklangan vaqt va resurs sharoitida qaysi vazifaga ustuvorlik berishni tanlash ko'nikmasini rivojlantirish.",
    "resurslar": ["Ball jadvali namunasi", "Taqdimot uchun kompyuter va proyektor"],
    "nazariya": [("Kirish", 7, ["O'tgan darsdagi maydoncha va missiyalar eslanadi."]), ("Ball tizimi", 10, ["Har bir missiya muvaffaqiyatli bajarilsa aniq ball berilishi (masalan 25 ball) tushuntiriladi.", "Qisman bajarilgan missiya uchun ball berilmasligi (yoki qanday hisoblanishi) aniqlashtiriladi."]), ("Yakunlash", 3, ["Jami ball qanday hisoblanishi (missiyalar yig'indisi) umumlashtiriladi."])],
    "amaliy": [("Misol tahlili", 15, ["O'quvchilarga namunaviy natija berilib, ular jami ballni hisoblaydilar."]), ("Strategiya muhokamasi", 10, ["Jamoalar qaysi missiyaga qachon o'tish haqida dastlabki fikr almashadilar."])],
    "uyga": ["O'z jamoangiz uchun qaysi missiyani birinchi bajarish kerakligi haqida fikringizni yozing."],
},

"Ikki missiyani ketma-ket bajarish dasturi": {
    "maqsad": ["O'quvchilar 1 va 2-missiya dasturlarini bitta ketma-ket dasturga birlashtiradilar.", "O'quvchilar ikki missiya orasida attachment almashtirish vaqtini hisobga oladilar.", "O'quvchilar birlashtirilgan dasturni to'liq sinaydilar."],
    "lugat": ["Ketma-ket bajarish (Sequential execution) – bir missiyadan keyin ikkinchisini boshlash", "Attachment almashtirish (Attachment swap) – bir qurilmani ikkinchisiga tez almashtirish", "Dastur birlashtirish (Program merging) – ikki dasturni bittaga qo'shish", "Vaqt boshqaruvi (Time management) – umumiy vaqtni nazorat qilish", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Yaxlit rejalashtirish — alohida qismlarni bitta uzluksiz jarayonga birlashtirish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami va ikkala missiya attachmentlari", "Planshet/noutbuk (SPIKE ilovasi)", "Musobaqa maydonchasi"],
    "nazariya": [("Kirish", 5, ["1 va 2-missiya dasturlari alohida eslanadi."]), ("Dasturlarni birlashtirish", 10, ["Ikkala dasturni bitta faylda ketma-ket joylashtirish, orasida attachment almashtirish vaqtini hisobga olish tushuntiriladi."])],
    "amaliy": [("Dastur birlashtirish", 20, ["O'quvchilar 1 va 2-missiya dasturlarini birlashtiradilar."]), ("Sinov", 10, ["O'quvchilar birlashtirilgan dasturni maydonchada sinaydilar."])],
    "uyga": ["Ikki missiya orasida attachment almashtirishni tezlashtirish uchun g'oya yozing."],
},

"Attachment tez almashtirish mashqi": {
    "maqsad": ["O'quvchilar attachmentlarni Driving Base'ga tez va ishonchli ulash/ajratish texnikasini mashq qiladilar.", "O'quvchilar vaqtni tejash uchun almashtirish tartibini oldindan rejalashtiradilar.", "O'quvchilarda tezkor va aniq qo'l harakati ko'nikmasi rivojlanadi."],
    "lugat": ["Attachment almashtirish (Attachment swap) – bir qurilmani ikkinchisiga tez almashtirish", "Ulash mexanizmi (Attachment connector) – attachmentni Driving Base'ga mahkamlovchi qism", "Vaqt (Time) – almashtirishga ketgan davr", "Xronometr (Stopwatch) – vaqtni o'lchash asbobi", "Mashq (Practice) – ko'nikmani takrorlab mustahkamlash"],
    "softSkill": "Tezkor va aniq amaliy ko'nikma — vaqt bosimi ostida ham aniq va ishonchli harakat qilish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami va barcha attachmentlar", "Xronometr"],
    "nazariya": [("Kirish", 7, ["Musobaqada har bir soniya qimmatli ekanligi haqida suhbat."]), ("Tez almashtirish texnikasi", 10, ["Attachmentni qanday tartibda ushlab, tezroq ulash mumkinligi ko'rsatiladi."]), ("Yakunlash", 3, ["Mashq qilish orqali vaqtni sezilarli qisqartirish mumkinligi ta'kidlanadi."])],
    "amaliy": [("Mashq", 20, ["O'quvchilar attachmentlarni bir necha marta almashtirib, xronometr bilan vaqtni o'lchaydilar."]), ("Natijalarni solishtirish", 10, ["Birinchi va oxirgi urinish vaqti solishtiriladi."])],
    "uyga": ["Attachment almashtirish vaqtingizni yanada qisqartirish uchun g'oya yozing."],
},

"Jamoa bilan mashq-turnir — 1-tur": {
    "maqsad": ["O'quvchilar 1 va 2-missiyani jamoa bo'lib, musobaqa formatida sinab ko'radilar.", "O'quvchilar real vaqt bosimi ostida ishlash tajribasini oladilar.", "O'quvchilar natijalarini keyingi tur uchun tahlil qiladilar."],
    "lugat": ["Mashq-turnir (Practice tournament) – haqiqiy musobaqaga o'xshash sinov", "Jamoa (Team) – birga ishlaydigan o'quvchilar guruhi", "Natija (Result) – turdan olingan ball", "Vaqt bosimi (Time pressure) – cheklangan vaqt sharoiti", "Musobaqa maydonchasi (Competition field) – missiya elementlari joylashgan maydon"],
    "softSkill": "Jamoaviy hamkorlik — bosim ostida jamoa a'zolari bilan aniq va tinch muloqot qilish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami va attachmentlar", "Musobaqa maydonchasi", "Xronometr, ball jadvali"],
    "nazariya": [("Kirish", 5, ["Mashq-turnir qoidalari tushuntiriladi (vaqt, ball tizimi)."]), ("Strategiya", 5, ["Jamoalar oxirgi marta strategiyasini muhokama qiladilar."])],
    "amaliy": [("Mashq-turnir", 30, ["Har bir jamoa navbat bilan 1 va 2-missiyani bajaradi.", "Natijalar ball jadvaliga yoziladi."])],
    "uyga": ["Mashq-turnirdagi natijangizni yaxshilash uchun nima o'zgartirish kerakligi haqida yozing."],
},

"Natijalarni tahlil qilish": {
    "maqsad": ["O'quvchilar mashq-turnir natijalarini tahlil qiladilar.", "O'quvchilar qaysi bosqichda vaqt yo'qotilganini yoki xato yuz berganini aniqlaydilar.", "O'quvchilar keyingi urinish uchun aniq yaxshilash rejasini tuzadilar."],
    "lugat": ["Tahlil (Analysis) – natijalarni diqqat bilan ko'rib chiqish", "Vaqt yo'qotish (Time loss) – kutilganidan ortiq ketgan vaqt", "Xato (Error) – kutilmagan noto'g'ri natija", "Yaxshilash rejasi (Improvement plan) – natijani oshirish uchun reja", "Ball jadvali (Score sheet) – natijalar yozilgan jadval"],
    "softSkill": "Tanqidiy o'z-o'zini baholash — natijani hissiyotsiz, ob'ektiv tahlil qilish ko'nikmasini rivojlantirish.",
    "resurslar": ["Oldingi mashq-turnir ball jadvali", "Qog'oz va qalam (tahlil uchun)"],
    "nazariya": [("Kirish", 7, ["Nazariy fikr: har qanday musobaqachi/muhandis natijasini tahlil qilib, yaxshilashi kerakligi haqida suhbat."]), ("Tahlil usuli", 10, ["Ball jadvalidan qaysi missiyada ko'proq/kamroq ball olinganini aniqlash usuli ko'rsatiladi."]), ("Yakunlash", 3, ["Tahlil asosida aniq va bajariladigan reja tuzish tavsiya etiladi."])],
    "amaliy": [("Tahlil", 15, ["Jamoalar o'z natijalarini ball jadvali orqali tahlil qiladilar."]), ("Reja tuzish", 10, ["Jamoalar keyingi urinish uchun aniq yaxshilash rejasini yozadilar."])],
    "uyga": ["Yaxshilash rejangizni to'ldirib, keyingi darsga tayyor holda olib keling."],
},

"Chorak yakuni: 1-2 missiya bo'yicha umumiy ko'rik": {
    "maqsad": ["O'quvchilar 1 va 2-missiya bo'yicha chorak davomidagi ishni umumlashtiradilar.", "O'quvchilar eng yaxshi natijaga erishgan yechimlarni sinfga taqdim etadilar.", "O'quvchilar keyingi chorak (3 va 4-missiya)ga tayyorlanadilar."],
    "lugat": ["Umumiy ko'rik (Review) – chorak davomidagi ishni yakunlab ko'rib chiqish", "Eng yaxshi yechim (Best solution) – eng samarali topilgan yondashuv", "Taqdimot (Presentation) – ishni tushuntirib berish", "Missiya (Mission) – bajarilishi kerak bo'lgan aniq vazifa", "Nazorat ishi (Assessment) – bilim va ko'nikmani tekshirish"],
    "softSkill": "Yutuqlarni tan olish va ulashish — o'z va boshqalarning yutuqlarini tan olib, tajriba almashish ko'nikmasini rivojlantirish.",
    "resurslar": ["Chorak davomida yig'ilgan robot va attachmentlar", "Taqdimot uchun kompyuter va proyektor"],
    "nazariya": [("Kirish", 7, ["Chorak davomida bosib o'tilgan yo'l (maydoncha bilan tanishuvdan mashq-turnirgacha) qisqacha eslanadi."]), ("Eng yaxshi yechimlar", 10, ["Bir nechta jamoaning eng yaxshi yechimi (attachment yoki dastur) sinfga ko'rsatiladi."]), ("Yakunlash", 3, ["Keyingi darsda nazorat ishi (missiya musobaqasi) bo'lishi eslatiladi."])],
    "amaliy": [("Taqdimotlar", 15, ["Bir nechta jamoa o'z yechimini qisqacha taqdim etadi."]), ("Yakuniy tayyorgarlik", 10, ["Jamoalar robot va attachmentlarini nazorat ishiga tayyorlaydilar."])],
    "uyga": ["Nazorat ishiga (missiya musobaqasiga) tayyorgarlik ko'ring: robot va attachmentlaringizni oxirgi marta tekshiring."],
},

"Barcha 4 missiyani ketma-ket bajarish dasturi": {
    "maqsad": ["O'quvchilar barcha 4 missiya dasturini bitta yaxlit, ketma-ket dasturga birlashtiradilar.", "O'quvchilar missiyalar orasidagi attachment almashtirish va vaqt boshqaruvini rejalashtiradilar.", "O'quvchilar birlashtirilgan dasturni to'liq sinaydilar."],
    "lugat": ["To'liq missiya turi (Full mission round) – barcha missiyalarning ketma-ket bajarilishi", "Dastur birlashtirish (Program merging) – bir nechta dasturni bittaga qo'shish", "Vaqt boshqaruvi (Time management) – 2.5 daqiqalik umumiy vaqtni nazorat qilish", "Attachment almashtirish (Attachment swap) – qurilmalarni tez almashtirish", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Yaxlit tizimli fikrlash — to'rtta alohida yechimni bitta uzluksiz, izchil jarayonga birlashtirish ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami va barcha 4 missiya attachmentlari", "Planshet/noutbuk (SPIKE ilovasi)", "To'liq musobaqa maydonchasi"],
    "nazariya": [("Kirish", 5, ["Barcha 4 missiya dasturi alohida-alohida eslanadi."]), ("Yaxlit dastur va vaqt reja", 10, ["4 ta dasturni bitta faylga birlashtirish va ular orasidagi vaqtni (2.5 daqiqa ichiga sig'dirish) rejalashtirish tushuntiriladi."])],
    "amaliy": [("Dastur birlashtirish", 20, ["O'quvchilar barcha 4 missiya dasturini birlashtiradilar."]), ("Sinov", 10, ["O'quvchilar birlashtirilgan dasturni maydonchada sinaydilar."])],
    "uyga": ["Barcha 4 missiyani 2.5 daqiqaga sig'dirish uchun eng qiyin qismi qaysi ekanini yozing."],
},

"Vaqt boshqaruvi: 2.5 daqiqalik to'liq missiya turi mashqi": {
    "maqsad": ["O'quvchilar 2.5 daqiqalik cheklangan vaqt ichida barcha 4 missiyani bajarishni mashq qiladilar.", "O'quvchilar vaqtni missiyalar orasida qanday taqsimlashni rejalashtiradilar.", "O'quvchilarda vaqt bosimida tinch ishlash ko'nikmasi rivojlanadi."],
    "lugat": ["Vaqt boshqaruvi (Time management) – cheklangan vaqtni oqilona taqsimlash", "2.5 daqiqalik tur (2.5-minute round) – FLL missiya turining standart davomiyligi", "Ustuvorlik (Priority) – qaysi missiyaga ko'proq vaqt ajratish", "Xronometr (Stopwatch) – vaqtni o'lchash asbobi", "Mashq (Practice) – ko'nikmani takrorlab mustahkamlash"],
    "softSkill": "Bosim ostida vaqtni boshqarish — cheklangan vaqtda shoshilmasdan, lekin samarali ishlash ko'nikmasini rivojlantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami va barcha attachmentlar", "To'liq musobaqa maydonchasi", "Xronometr"],
    "nazariya": [("Kirish", 5, ["2.5 daqiqalik tur formati (FLL standarti) tushuntiriladi."]), ("Vaqt taqsimoti", 10, ["Har bir missiyaga taxminan qancha vaqt ajratish kerakligi (masalan, har biriga ~35 soniya) rejalashtiriladi."])],
    "amaliy": [("Mashq", 25, ["Jamoalar 2.5 daqiqalik xronometr bilan barcha 4 missiyani ketma-ket bajarishga harakat qiladilar."]), ("Muhokama", 5, ["Vaqt qayerda yo'qotilgani muhokama qilinadi."])],
    "uyga": ["Vaqtingizni yaxshiroq taqsimlash uchun bitta strategiya yozing."],
},

"Muhandislik daftarini (Inventor Notebook) yakunlash": {
    "maqsad": ["O'quvchilar yil davomidagi ishlarini muhandislik daftarida (Inventor Notebook) tartibga soladilar.", "O'quvchilar dizayn jarayoni, sinovlar va yechimlarni hujjatlashtirish ahamiyatini tushunadilar.", "O'quvchilar daftarni yakuniy taqdimotga tayyorlaydilar."],
    "lugat": ["Muhandislik daftari (Engineering/Inventor notebook) – loyiha jarayonini qayd etuvchi hujjat", "Hujjatlashtirish (Documentation) – ish jarayonini yozib borish", "Dizayn jarayoni (Design process) – muammo-g'oya-qurish-sinov bosqichlari", "Iteratsiya (Iteration) – sinov-tuzatish jarayonini takrorlash", "Portfolio (Portfolio) – bajarilgan ishlar to'plami"],
    "softSkill": "Hujjatlashtirish madaniyati — o'z ishini tartibli va tushunarli qilib yozib borish, bu haqiqiy muhandislar amaliyoti ekanligini anglash.",
    "resurslar": ["Muhandislik daftari (qog'ozda yoki elektron)", "Yil davomidagi rasmlar/eskizlar (agar saqlangan bo'lsa)"],
    "nazariya": [("Kirish", 7, ["Haqiqiy muhandislar nega har doim jurnal/daftar yuritishi haqida suhbat."]), ("Daftar tuzilishi", 10, ["Daftarda qanday bo'limlar (muammo, g'oyalar, eskizlar, sinov natijalari) bo'lishi kerakligi ko'rsatiladi."]), ("Yakunlash", 3, ["Daftar taqdimotda ham ishlatilishi aytiladi."])],
    "amaliy": [("Daftarni to'ldirish", 20, ["O'quvchilar yil davomidagi asosiy bosqichlarni daftarga tartib bilan yozadilar/joylashtiradilar."]), ("Ko'rib chiqish", 10, ["Daftarlar juftlikda almashtirilib, fikr-mulohaza beriladi."])],
    "uyga": ["Daftaringizni yakunlab, keyingi darsga to'liq tayyor holda olib keling."],
},

"Jamoaviy prezentatsiya tayyorlash": {
    "maqsad": ["O'quvchilar yakuniy taqdimot uchun jamoaviy prezentatsiya tayyorlaydilar.", "O'quvchilar taqdimotda kimning nima haqida gapirishini taqsimlaydilar.", "O'quvchilar taqdimot mazmunini (muammo, yechim, natija) tartibga soladilar."],
    "lugat": ["Prezentatsiya (Presentation) – ishni tomoshabinlarga taqdim etish", "Taqdimot tuzilishi (Presentation structure) – gapirish tartibi (kirish, asosiy qism, xulosa)", "Rol taqsimoti (Role distribution) – jamoa a'zolari orasida vazifa bo'lish", "Auditoriya (Audience) – tinglovchilar", "Portfolio (Portfolio) – bajarilgan ishlar to'plami"],
    "softSkill": "Jamoaviy kommunikatsiya — taqdimotni jamoa bo'lib tayyorlash va har birining o'z rolini bilishini ta'minlash ko'nikmasini rivojlantirish.",
    "resurslar": ["Muhandislik daftari", "Slayd yoki plakat tayyorlash uchun material", "Taqdimot uchun kompyuter va proyektor"],
    "nazariya": [("Kirish", 7, ["Yaxshi taqdimot qanday tuzilishga ega bo'lishi (muammo->yechim->natija) haqida suhbat."]), ("Taqdimot rejasi", 10, ["Jamoa taqdimotning qaysi qismini kim aytishini rejalashtiradi."]), ("Yakunlash", 3, ["Aniq va ishonchli gapirish tavsiyalari beriladi."])],
    "amaliy": [("Taqdimot tayyorlash", 20, ["Jamoalar slayd yoki plakat tayyorlaydilar va gapirish tartibini belgilaydilar."]), ("Ichki mashq", 10, ["Jamoa o'z ichida taqdimotni bir marta sinab ko'radi."])],
    "uyga": ["O'z qismingizni (nima haqida gapirishingizni) yodlab/mashq qilib keling."],
},

"Yakuniy repetitsiya": {
    "maqsad": ["O'quvchilar yakuniy bitiruv turniri va taqdimot uchun to'liq repetitsiya o'tkazadilar.", "O'quvchilar vaqt, robot va taqdimotni birgalikda sinab ko'radilar.", "O'quvchilar oxirgi kamchiliklarni aniqlab, tuzatadilar."],
    "lugat": ["Repetitsiya (Rehearsal) – yakuniy tadbirdan oldingi to'liq sinov", "Kamchilik (Weakness) – hali yaxshilanishi kerak bo'lgan joy", "Yakuniy tayyorgarlik (Final preparation) – tadbirdan oldingi so'nggi tayyorgarlik", "Missiya turi (Mission round) – barcha missiyalarning ketma-ket bajarilishi", "Taqdimot (Presentation) – ishni tushuntirib berish"],
    "softSkill": "Yakuniy o'z-o'zini nazorat qilish — tadbirdan oldin oxirgi marta hamma narsani tekshirib chiqish mas'uliyatini shakllantirish.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami va barcha attachmentlar", "Musobaqa maydonchasi", "Taqdimot materiallari (daftar, slayd/plakat)"],
    "nazariya": [("Kirish", 5, ["Ertangi/keyingi (yakuniy) tadbir tartibi eslatiladi."]), ("Repetitsiya rejasi", 5, ["Missiya turi va taqdimotning qaysi tartibda sinalishi belgilanadi."])],
    "amaliy": [("To'liq repetitsiya", 25, ["Jamoalar missiya turini va taqdimotni boshidan oxirigacha to'liq sinab ko'radilar."]), ("Yakuniy tuzatish", 5, ["Aniqlangan kichik kamchiliklar tuzatiladi."])],
    "uyga": ["Yakuniy tadbirga ruhiy va jismoniy tayyor bo'lish uchun bugun kechqurun nima qilishni rejalashtiring."],
},

"Ichki bitiruv turniri — barcha 4 missiya": {
    "maqsad": ["O'quvchilar barcha 4 missiyani rasmiy ichki turnir formatida bajaradilar.", "O'quvchilar ikki yillik (Makerzoid+SPIKE) bilim va ko'nikmalarini to'liq namoyish etadilar.", "O'quvchilarda musobaqa tajribasi va jamoaviy g'urur mustahkamlanadi."],
    "lugat": ["Ichki turnir (Internal tournament) – sinf/maktab ichida o'tkaziladigan musobaqa", "To'liq missiya turi (Full mission round) – barcha 4 missiyaning ketma-ket bajarilishi", "Ball jadvali (Score sheet) – natijalar yozilgan jadval", "Sudya (Judge/Referee) – natijani rasmiy baholovchi shaxs (o'qituvchi)", "Jamoa (Team) – birga ishlaydigan o'quvchilar guruhi"],
    "softSkill": "Musobaqa bosimida yaxlitlik — ikki yillik mehnat natijasini bir turnirda to'liq va halol namoyish etish ko'nikmasini mustahkamlash.",
    "resurslar": ["LEGO Education SPIKE Prime to'plami va barcha attachmentlar", "To'liq musobaqa maydonchasi", "Xronometr, rasmiy ball jadvali"],
    "nazariya": [("Kirish", 5, ["Turnir qoidalari va navbat tartibi so'nggi marta eslatiladi."]), ("Sportchan munosabat", 5, ["G'alaba va mag'lubiyatga sog'lom munosabat haqida qisqacha suhbat."])],
    "amaliy": [("Ichki turnir", 30, ["Har bir jamoa navbat bilan 2.5 daqiqalik to'liq missiya turini bajaradi.", "Natijalar rasmiy ball jadvaliga yoziladi."])],
    "uyga": ["Turnirdagi natijangiz va his-tuyg'ularingiz haqida qisqacha yozing."],
},

"Ota-onalar uchun ochiq ko'rgazma va natijalar e'loni": {
    "maqsad": ["O'quvchilar ikki yillik (0-4-sinf Makerzoid + 4-sinf SPIKE) yo'lidagi natijalarini ota-onalar oldida namoyish etadilar.", "O'quvchilar o'z loyihalari va turnir natijalari haqida ishonch bilan gapirib beradilar.", "O'quvchilarda o'z mehnatidan g'ururlanish va bosqichni munosib yakunlash tuyg'usi shakllanadi."],
    "lugat": ["Ko'rgazma (Exhibition) – tayyor loyihalarni namoyish qilish tadbiri", "Natijalar e'loni (Results announcement) – turnir yakunlarini rasman e'lon qilish", "Taqdimot (Presentation) – ishni tushuntirib berish", "Portfolio (Portfolio) – bajarilgan ishlar to'plami", "Bitiruv (Graduation/Completion) – bosqichni yakunlash"],
    "softSkill": "Ishonch bilan taqdim etish va g'urur — ikki yillik mehnat natijasini oila oldida ishonch va g'urur bilan ko'rsatish ko'nikmasini mustahkamlash.",
    "resurslar": ["Barcha yasalgan robotlar va attachmentlar", "Muhandislik daftarlari/portfolio", "Ko'rgazma uchun stollar/joy", "Sertifikatlar (agar tayyorlangan bo'lsa)"],
    "nazariya": [("Kirish", 5, ["Ko'rgazma tartibi va kim qachon gapirishi eslatiladi."])],
    "amaliy": [("Ochiq ko'rgazma", 30, ["O'quvchilar o'z robotlari va loyihalarini ota-onalarga ko'rsatib, tushuntiradilar.", "Turnir natijalari rasman e'lon qilinadi, barcha ishtirokchilar tabriklanadi."]), ("Yakuniy so'z", 10, ["O'qituvchi ikki yillik yo'l yakuni va kelajakdagi imkoniyatlar haqida qisqacha so'zlaydi."])],
    "uyga": ["0-4-sinf va SPIKE davomidagi eng yodda qolgan xotirangiz haqida oilangiz bilan suhbatlashing."],
},

}

# ---------------------------------------------------------------------------
# Yig'ma lug'at
# ---------------------------------------------------------------------------

SPIKE_CONTENT = {}
SPIKE_CONTENT.update(SPIKE_INTRO)
SPIKE_CONTENT.update(SPIKE_ATTACHMENTS)
SPIKE_CONTENT.update(SPIKE_SENSOR)
SPIKE_CONTENT.update(SPIKE_MISSIONS)
SPIKE_CONTENT.update(SPIKE_MISC)
