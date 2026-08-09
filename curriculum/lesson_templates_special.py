# -*- coding: utf-8 -*-
"""
"Chorak kirish", "Nazorat" va "Loyiha" turidagi darslar uchun to'liq, qo'lda yozilgan kontent.
Bular soni cheklangan (jami ~44 ta noyob matn) bo'lgani uchun har biri alohida yozilgan,
lekin bir nechta joyda (turli sinf/yil pozitsiyasida) qayta ishlatiladi.

Har bir yozuv to'liq LESSON_CONTENT formatida (meta'siz): maqsad/lugat/softSkill/resurslar/
nazariya/amaliy/uyga. meta generatorda alohida qo'shiladi.
"""

# ---------------------------------------------------------------------------
# CHORAK KIRISH (20 ta, title matni bo'yicha kalitlangan)
# ---------------------------------------------------------------------------

INTRO_CONTENT = {

"Chorak kirish: bloklar bilan tanishuv, xavfsizlik": {
    "maqsad": [
        "O'quvchilar robototexnika darslari bilan birinchi marta tanishadilar va kelgusi mashg'ulotlar davomida nima kutilishini tushunadilar.",
        "O'quvchilar konstruktor bloklari va ularning turlari bilan tanishadilar.",
        "O'quvchilar sinfda xavfsiz ishlash qoidalarini o'zlashtiradilar.",
    ],
    "lugat": [
        "Robot – dasturlashtirilgan, harakat qila oladigan qurilma",
        "Konstruktor (Constructor set) – qurilma yasash uchun detallar to'plami",
        "Blok (Block) – konstruktordagi asosiy qurilish qismi",
        "Xavfsizlik qoidalari (Safety rules) – ish jarayonida rioya qilinadigan qoidalar",
        "Detal (Part) – qurilmaning kichik qismi",
    ],
    "softSkill": "Jamoada ishlash va intizom — birinchi darsdanoq navbat bilan ishlash, buyumlarni ehtiyotkorlik bilan ushlash va boshqalarga xalaqit bermaslik ko'nikmasini shakllantirish.",
    "resurslar": [
        "Makerzoid Robot Master Standard to'plami namunalari (ko'rgazma uchun)",
        "Xavfsizlik qoidalari plakati yoki rasmlar",
        "Taqdimot uchun kompyuter va proyektor",
        "Ranglar/shakllar bo'yicha saralash uchun aralash bloklar to'plami",
    ],
    "nazariya": [
        ("Kirish", 10, ["O'zaro tanishuv: o'qituvchi va o'quvchilar bir-birlari bilan tanishadilar.", "\"Robotika nima?\" mavzusida qiziqarli faktlar va qisqa video ko'rsatiladi."]),
        ("Bloklar va detallar", 10, ["Konstruktor to'plamidagi asosiy blok turlari ko'rsatiladi: ulash detallari, g'ildiraklar, motor va sensor.", "Bloklarning rangi va shakli bo'yicha farqlanishi tushuntiriladi."]),
        ("Xavfsizlik qoidalari", 10, ["Kichik detallarni og'izga solmaslik, ular bilan otishmaslik.", "Ishdan keyin barcha detallarni tartibli qutiga joylash.", "Boshqa o'quvchining ishini buzmaslik, so'rab foydalanish."]),
        ("Yakunlash", 5, ["Kelgusi darslarda nimalar kutilishi haqida qisqacha ma'lumot: har darsda yangi robot yasaymiz!"]),
    ],
    "amaliy": [
        ("Bloklarni ushlab ko'rish", 5, ["O'quvchilar navbat bilan turli bloklarni qo'lda ushlab, ularning shakli va og'irligini his qiladilar."]),
        ("Ranglar/shakllar bo'yicha saralash o'yini", 5, ["Aralashtirilgan bloklar rang yoki shakl bo'yicha guruhlarga ajratiladi — kim tezroq va to'g'ri saralaydi."]),
    ],
    "uyga": [
        "Uyda robotlar haqida bitta qiziqarli fakt toping va keyingi darsda sinfga ayting.",
        "Agar uyda konstruktor o'yinchoqlari bo'lsa, ularni diqqat bilan ko'zdan kechiring va nechta turli blok borligini sanang.",
    ],
},

"Chorak kirish: mexanizmlar nima uchun kerak?": {
    "maqsad": [
        "O'quvchilar mexanizm tushunchasi va uning kundalik hayotdagi ahamiyatini tushunadilar.",
        "O'quvchilar g'ildirak, o'q, tishli g'ildirak kabi oddiy mexanizmlar bilan birinchi marta tanishadilar.",
        "O'quvchilar bu chorakda qanday yangi robotlar yasashlarini tasavvur qiladilar.",
    ],
    "lugat": [
        "Mexanizm (Mechanism) – harakatni uzatuvchi yoki o'zgartiruvchi qurilma qismlari",
        "G'ildirak (Wheel) – aylanib harakatni osonlashtiradigan detal",
        "O'q (Axle) – g'ildirak aylanadigan tayoqcha",
        "Tishli g'ildirak (Gear) – tishchali, aylanadigan detal",
        "Harakat (Motion) – narsaning joyini o'zgartirishi",
    ],
    "softSkill": "Qiziqish va savol berish — o'quvchilarni atrofdagi mexanizmlar haqida savol berishga undash, bu ularning ilmiy tafakkurini rivojlantiradi.",
    "resurslar": [
        "Oddiy mexanizm namunalari (g'ildirak-o'q, tishli g'ildirak) ko'rgazma uchun",
        "Taqdimot uchun kompyuter va proyektor",
        "Har xil rasm/video (kran, velosiped, soat)",
    ],
    "nazariya": [
        ("Kirish", 7, ["O'tgan chorakda nimalarni o'rgangani qisqacha eslatib o'tiladi.", "\"Mexanizm nima?\" savoli beriladi va o'quvchilar fikr bildiradilar."]),
        ("Mexanizmlar atrofimizda", 8, ["Kundalik hayotdagi oddiy mexanizmlar (velosiped, soat, eshik) rasmda ko'rsatiladi.", "Mexanizmlar bizga qanday yordam berishi (kuchni tejash, harakatni osonlashtirish) muhokama qilinadi."]),
        ("Yakunlash", 5, ["Bu chorakda qanday yangi mexanizmlarni o'rganishlari haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Mexanizm qismlarini ko'rish", 5, ["O'quvchilarga g'ildirak, o'q, tishli g'ildirak namunalari qo'lga berib ko'rsatiladi."]),
        ("Kichik sinov", 5, ["O'quvchilar g'ildirakli va g'ildiraksiz narsani itarib, farqni his qiladilar."]),
    ],
    "uyga": [
        "Uyda mexanizm ishlatiladigan 2 ta narsani toping (masalan, eshik dastagi, velosiped) va rasmini chizing.",
    ],
},

"Chorak kirish: motor va controller bilan tanishuv (namoyish)": {
    "maqsad": [
        "O'quvchilar motor va controller (asosiy boshqaruv bloki) nima ekanligini tushunadilar.",
        "O'quvchilar motorli robotning motorsizdan farqini kuzatadilar.",
        "O'quvchilar ilova orqali robotni boshqarish jarayonini birinchi marta ko'radilar (namoyish).",
    ],
    "lugat": [
        "Motor (Motor) – elektr yordamida aylanadigan qurilma",
        "Controller (Host controller) – robotning \"miyasi\", boshqaruv bloki",
        "Ilova (App) – telefon/planshetdagi boshqaruv dasturi",
        "Ulanish (Connect) – motor yoki sensorni controllerga bog'lash",
        "Namoyish (Demonstration) – o'qituvchi ko'rsatib beradigan sinov",
    ],
    "softSkill": "Diqqat bilan kuzatish — o'qituvchi namoyishini diqqat bilan kuzatib, savol berish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "Motor va controller namunasi (o'qituvchida, namoyish uchun)",
        "Planshet yoki telefon (Makerzoid ilovasi)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["O'tgan chorakda mexanizmlarni o'rganganimiz eslatiladi, bugun \"jonlanish\" haqida gaplashamiz."]),
        ("Motor va controller nima", 8, ["Controller robotning \"miyasi\" ekanligi, motor esa \"mushagi\" ekanligi sodda tilda tushuntiriladi.", "O'qituvchi motor va controllerni ulab, ilova orqali ishga tushirib ko'rsatadi (namoyish)."]),
        ("Yakunlash", 5, ["Keyingi darslarda o'quvchilarning o'zlari motorli model yasashlari haqida aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Namoyishni kuzatish", 7, ["O'quvchilar o'qituvchi ko'rsatgan motorli modelni diqqat bilan kuzatadilar."]),
        ("Savol-javob", 3, ["O'quvchilar ko'rgan narsalari haqida savol berishadi."]),
    ],
    "uyga": [
        "Uyda motor bilan ishlaydigan narsalarni (ventilyator, o'yinchoq mashina) toping va ro'yxat qiling.",
    ],
},

"Chorak kirish: sensor nima? (namoyish)": {
    "maqsad": [
        "O'quvchilar sensor tushunchasi bilan birinchi marta tanishadilar.",
        "O'quvchilar sensorli robotning oddiy robotdan farqini kuzatadilar (namoyish).",
        "O'quvchilar bu chorakda sensorli modellar yasashlarini tasavvur qiladilar.",
    ],
    "lugat": [
        "Sensor (Sensor) – atrofdagi o'zgarishni \"sezadigan\" qurilma",
        "Signal (Signal) – sensordan kelayotgan xabar",
        "Sezish (Sense) – biror narsani aniqlash",
        "Reaksiya (Reaction) – sensor signaliga javob sifatida sodir bo'ladigan harakat",
        "Namoyish (Demonstration) – o'qituvchi ko'rsatib beradigan sinov",
    ],
    "softSkill": "Kuzatuvchanlik — sensorli robot qanday \"sezishini\" diqqat bilan kuzatish orqali ilmiy kuzatuvchanlikni rivojlantirish.",
    "resurslar": [
        "Sensorli tayyor model (o'qituvchida, namoyish uchun)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Inson qanday \"sezishi\" (ko'z, qo'l, quloq) haqida suhbat.", "\"Robot ham sezishi mumkinmi?\" savoli beriladi."]),
        ("Sensor nima", 8, ["Sensor atrof-muhitdagi o'zgarishni (yorug'lik, masofa) \"sezishi\" tushuntiriladi.", "O'qituvchi sensorli modelni namoyish qiladi: qo'l yaqinlashganda robot reaksiya beradi."]),
        ("Yakunlash", 5, ["Bu chorakda o'quvchilarning o'zlari sensorli model yasashlari haqida aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Namoyishni kuzatish", 7, ["O'quvchilar sensorli modelning ishlashini diqqat bilan kuzatadilar."]),
        ("Savol-javob", 3, ["O'quvchilar sensor haqida savol berib, taxminlarini aytadilar."]),
    ],
    "uyga": [
        "Uyda sensor ishlatiladigan narsalarni (avtomatik eshik, telefon) toping va ro'yxat qiling.",
    ],
},

"Chorak kirish: Makerzoid to'plami, detallar nomlari, xavfsizlik": {
    "maqsad": [
        "O'quvchilar Makerzoid to'plamining asosiy detallari va ularning nomlari bilan tanishadilar.",
        "O'quvchilar mustahkam va tartibli qurish qoidalarini o'zlashtiradilar.",
        "O'quvchilar xavfsiz ishlash tartibini eslab qoladilar.",
    ],
    "lugat": [
        "Detal (Part) – qurilmaning kichik qismi",
        "Ulash elementi (Connector) – detallarni bog'laydigan qism",
        "Konstruksiya (Construction) – qurilma tuzilishi",
        "Instruksiya (Instructions) – qurish bosqichlari yozilgan qo'llanma",
        "Xavfsizlik qoidalari (Safety rules) – ish jarayonida rioya qilinadigan qoidalar",
    ],
    "softSkill": "Tartiblilik — har bir detalni o'z joyiga qo'yish va ishni tartibli olib borish ko'nikmasini shakllantirish.",
    "resurslar": [
        "Makerzoid Robot Master Standard to'plami (har guruhga bittadan)",
        "Detallar nomlari yozilgan plakat yoki jadval",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["1-sinf davomida nimalar o'rganilishi haqida umumiy tasvir beriladi."]),
        ("Detallar va ularning nomlari", 8, ["To'plamdagi asosiy detal turlari (ulash elementlari, g'ildiraklar, motor, sensor, controller) ko'rsatiladi va nomlanadi.", "Instruksiya (rasmli qo'llanma)dan qanday foydalanish tushuntiriladi."]),
        ("Xavfsizlik va mustahkam qurish", 5, ["Detallarni to'g'ri va mustahkam ulash qoidalari, ish joyini tartibli tutish eslatiladi."]),
    ],
    "amaliy": [
        ("Detallarni tanish o'yini", 6, ["O'quvchilar aralash detallar orasidan o'qituvchi aytgan detalni topadilar."]),
        ("Kichik ulash mashqi", 4, ["O'quvchilar ikki-uch detalni birlashtirib, oddiy ulanish mashqini bajaradilar."]),
    ],
    "uyga": [
        "Bugun o'rgangan 3 ta detal nomini yodda tuting va ota-onangizga tushuntirib bering.",
    ],
},

"Chorak kirish: motor qanday ishlaydi? (namoyish)": {
    "maqsad": [
        "O'quvchilar motorning ishlash tamoyili bilan chuqurroq tanishadilar.",
        "O'quvchilar motorli va motorsiz modellarni solishtiradilar.",
        "O'quvchilar bu chorakda motorli robotlar yasashga tayyorlanadilar.",
    ],
    "lugat": [
        "Motor (Motor) – elektr energiyasini harakatga aylantiruvchi qurilma",
        "Elektr energiyasi (Electric energy) – motorni ishga tushiradigan energiya",
        "Aylanish tezligi (Speed) – motorning tezligi",
        "Ulanish porti (Port) – motor ulanadigan uyacha",
        "Namoyish (Demonstration) – o'qituvchi ko'rsatadigan sinov",
    ],
    "softSkill": "Ilmiy kuzatuvchanlik — motorning ishlashini kuzatib, o'z so'zi bilan tasvirlashga undash.",
    "resurslar": [
        "Motorli namuna model (namoyish uchun)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["1-chorakda o'rganilgan mexanizmlar eslatiladi, bugun ularga \"kuch\" beruvchi motor haqida gaplashamiz."]),
        ("Motor ishlash tamoyili", 8, ["Motorga elektr berilganda u aylanishi (namoyishda) ko'rsatiladi.", "Motor tezligini o'zgartirish mumkinligi ko'rsatiladi."]),
        ("Yakunlash", 5, ["Motorli va motorsiz model orasidagi farq umumlashtiriladi."]),
    ],
    "amaliy": [
        ("Namoyishni kuzatish", 7, ["O'quvchilar motorli modelning ishga tushishini diqqat bilan kuzatadilar."]),
        ("Taqqoslash suhbati", 3, ["Motorli va motorsiz model qanday farq qilishi haqida fikr almashiladi."]),
    ],
    "uyga": [
        "Uyda motorli 2 ta buyumni (fen, o'yinchoq) toping va ular nima uchun ishlatilishini yozing.",
    ],
},

"Chorak kirish: qo'lda harakatlantiriladigan mexanizmlar (YL Corps)": {
    "maqsad": [
        "O'quvchilar qo'lda harakatlantiriladigan (motorsiz) mexanizmlar bilan tanishadilar.",
        "O'quvchilar bu chorakda yasaladigan qiziqarli figuralarni (YL Corps) ko'radilar.",
        "O'quvchilar qo'l bilan berilgan kuchning mexanizm orqali qanday harakatga aylanishini tushunadilar.",
    ],
    "lugat": [
        "Qo'lda harakatlantirish (Manual operation) – motorsiz, qo'l kuchi bilan ishlaydigan mexanizm",
        "Dastak (Handle/Crank) – qo'l bilan aylantiriladigan qism",
        "Figura (Figure) – odam yoki hayvon shaklidagi model",
        "Harakat uzatish (Motion transfer) – bir qismdagi harakatni boshqasiga o'tkazish",
        "Mexanizm (Mechanism) – harakatni bajaruvchi qurilma qismlari",
    ],
    "softSkill": "Ijodiy tasavvur — qo'lda aylantirilganda figura qanday harakat qilishini oldindan tasavvur qilishga undash.",
    "resurslar": [
        "YL Corps turkumidagi namuna model (agar mavjud bo'lsa)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Qo'g'irchoq teatri yoki mexanik o'yinchoqlar misolida qo'lda harakatlanuvchi mexanizmlar tanishtiriladi."]),
        ("Qo'l kuchidan harakatgacha", 8, ["Dastakni aylantirish qanday qilib figura harakatiga aylanishi (krivoship tamoyili) sodda tarzda ko'rsatiladi.", "O'quvchilar qo'lda kichik namunani aylantirib sinaydilar."]),
        ("Yakunlash", 5, ["Bu chorakda qanday qiziqarli figuralar yasashlari haqida aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Dastakni sinash", 6, ["O'quvchilar namunadagi dastakni aylantirib, harakatni kuzatadilar."]),
        ("Taxmin o'yini", 4, ["Dastak tezroq aylantirilsa nima o'zgarishi haqida taxmin qilinadi va sinaladi."]),
    ],
    "uyga": [
        "Uyda qo'lda aylantirib ishlaydigan narsani (masalan, qutichadagi musiqa quti) eslang va tasvirlab yozing.",
    ],
},

"Chorak kirish: sensor turlari bilan tanishuv (namoyish)": {
    "maqsad": [
        "O'quvchilar turli sensor turlari (harakat, yorug'lik, bosim) bilan tanishadilar.",
        "O'quvchilar har bir sensor turi nimani \"sezishini\" tushunadilar.",
        "O'quvchilar bu chorakda sensorli robotlar yasashga tayyorlanadilar.",
    ],
    "lugat": [
        "Harakat sensori (Motion sensor) – harakatni aniqlovchi sensor",
        "Yorug'lik sensori (Light sensor) – yorug'lik darajasini aniqlovchi sensor",
        "Bosim sensori (Touch/Force sensor) – bosim yoki teginishni aniqlovchi sensor",
        "Signal (Signal) – sensordan kelayotgan xabar",
        "Namoyish (Demonstration) – o'qituvchi ko'rsatadigan sinov",
    ],
    "softSkill": "Taqqoslash ko'nikmasi — turli sensor turlarini bir-biri bilan solishtirib, farqlarni aytishga undash.",
    "resurslar": [
        "Turli sensor namunalari (namoyish uchun)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["O'tgan chorakda o'rganilgan bitta sensor turi eslatiladi, bugun boshqa turlari bilan tanishamiz."]),
        ("Sensor turlari", 8, ["Harakat, yorug'lik va bosim sensorlari birma-bir namoyish qilinadi.", "Har biri qanday vaziyatda ishlatilishi (masalan, avtomatik eshik — harakat sensori) muhokama qilinadi."]),
        ("Yakunlash", 5, ["Bu chorakda qaysi sensorlardan foydalanishlari haqida aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Sensorlarni sinash", 7, ["O'quvchilar navbat bilan har bir sensor turini qo'lda sinab ko'radilar."]),
        ("Taqqoslash suhbati", 3, ["Qaysi sensor nimani \"sezishi\" haqida qisqacha muhokama."]),
    ],
    "uyga": [
        "Uyda turli sensor ishlatilgan 3 ta qurilmani (telefon, sovutgich, avtomatik chiroq) toping va ro'yxat qiling.",
    ],
},

"Chorak kirish: o'tgan yilni eslaymiz, murakkab mexanizmlarga kirish": {
    "maqsad": [
        "O'quvchilar o'tgan yilda o'rgangan mexanizmlarni eslaydilar va mustahkamlaydilar.",
        "O'quvchilar bu yil o'rganiladigan murakkabroq mexanizmlar bilan tanishadilar.",
        "O'quvchilar yangi o'quv yiliga tayyorlanadilar.",
    ],
    "lugat": [
        "Takrorlash (Review) – avval o'rgangan narsani eslash",
        "Murakkab mexanizm (Complex mechanism) – bir nechta oddiy mexanizmdan tashkil topgan tizim",
        "Uzatma (Transmission) – kuch yoki harakatni bir qismdan boshqasiga uzatish",
        "Konstruksiya (Construction) – qurilma tuzilishi",
        "Blok-sxema (Flowchart) – jarayon qadamlarini ko'rsatuvchi sxema",
    ],
    "softSkill": "O'z bilimini baholash — o'tgan yildagi bilimlarini eslab, o'ziga ishonch bilan yangi mavzuga kirishish.",
    "resurslar": [
        "O'tgan yilda yasalgan model rasmlari (agar mavjud bo'lsa)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["O'tgan yil qanday mexanizmlar (richag, tishli g'ildirak, shkiv) o'rganilgani birga eslanadi."]),
        ("Bu yil nima kutmoqda", 8, ["Bu yil bir nechta oddiy mexanizmni birlashtirgan murakkabroq modellar yasalishi aytiladi.", "Misol tariqasida bir-ikkita murakkabroq model rasmi ko'rsatiladi."]),
        ("Yakunlash", 5, ["Savol-javob orqali o'tgan yil bilimlari mustahkamlanadi."]),
    ],
    "amaliy": [
        ("Eslash o'yini", 6, ["O'quvchilar o'tgan yil o'rgangan mexanizm nomlarini navbat bilan aytadilar."]),
        ("Tezkor qurish tanlovi", 4, ["O'quvchilar o'tgan yildan tanish oddiy mexanizmni tezkor eslab yig'ib ko'radilar."]),
    ],
    "uyga": [
        "O'tgan yil eng yoqqan modelingiz rasmini chizib, nima uchun yoqqanini yozing.",
    ],
},

"Chorak kirish: elektr mashinalar qanday ishlaydi?": {
    "maqsad": [
        "O'quvchilar elektr bilan ishlaydigan mashinalarning umumiy tuzilishi bilan tanishadilar.",
        "O'quvchilar motor, controller va energiya manbai orasidagi bog'liqlikni tushunadilar.",
        "O'quvchilar bu chorakda yasaladigan elektr mashinalarni tasavvur qiladilar.",
    ],
    "lugat": [
        "Elektr mashina (Electric machine) – motor bilan ishlaydigan qurilma",
        "Energiya manbai (Power source) – batareya yoki quvvat beruvchi qism",
        "Controller (Controller) – boshqaruv bloki",
        "Uzatma tizimi (Drive system) – motordan g'ildirakkacha kuchni uzatuvchi qismlar",
        "Ishga tushirish (Start/Activate) – mashinani ishlatishni boshlash",
    ],
    "softSkill": "Tizimli fikrlash — mashinaning har bir qismi (energiya, controller, motor, g'ildirak) birgalikda qanday ishlashini tushunishga undash.",
    "resurslar": [
        "Elektr mashina namunasi (namoyish uchun)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["O'tgan chorakdagi mexanik modellar eslatiladi, bugun ularga \"elektr kuchi\" qo'shamiz."]),
        ("Elektr mashina tuzilishi", 8, ["Energiya manbai -> controller -> motor -> g'ildirak zanjiri sodda tarzda tushuntiriladi.", "O'qituvchi elektr mashinani ishga tushirib, har bir qismni ko'rsatadi."]),
        ("Yakunlash", 5, ["Bu chorakda yasaladigan elektr mashinalar haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Qismlarni tanish", 6, ["O'quvchilar elektr mashina qismlarini (motor, controller, g'ildirak) ko'rsatib beradilar."]),
        ("Namoyishni kuzatish", 4, ["O'quvchilar mashinaning ishga tushishini kuzatadilar."]),
    ],
    "uyga": [
        "Uyda elektr bilan ishlaydigan 3 ta mashinani (mikser, soat, o'yinchoq) toping va ro'yxat qiling.",
    ],
},

"Chorak kirish: elektr hayvon-mexanizmlar bilan tanishuv": {
    "maqsad": [
        "O'quvchilar elektr motorli hayvon-robotlar bilan tanishadilar.",
        "O'quvchilar biomimikriya (tabiatdan ilhomlanish) tushunchasi bilan birinchi marta tanishadilar.",
        "O'quvchilar bu chorakda qanday hayvon-robotlar yasashlarini tasavvur qiladilar.",
    ],
    "lugat": [
        "Hayvon-robot (Animal robot) – hayvonga o'xshab yasalgan, motorli robot",
        "Biomimikriya (Biomimicry) – tabiatdan ilhomlanib muhandislik yechimi yaratish",
        "Taqlid qilish (Imitate) – boshqa narsaga o'xshab harakat qilish",
        "Krivoship mexanizmi (Crank mechanism) – aylanma harakatni tebranishga aylantiruvchi tizim",
        "Motor (Motor) – hayvon-robotni harakatga keltiruvchi qurilma",
    ],
    "softSkill": "Tabiatga qiziqish — atrofdagi hayvonlarning harakatini kuzatib, ular haqida gapirishga undash.",
    "resurslar": [
        "Elektr hayvon-model namunasi (namoyish uchun)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Sevimli hayvonlar va ularning harakati haqida qisqa suhbat."]),
        ("Robot-hayvonlar qanday harakat qiladi", 8, ["Motorli hayvon-robot namoyish qilinib, uning oyoq/dum harakati ko'rsatiladi.", "Bu harakat qanday mexanizm (krivoship) orqali hosil bo'lishi sodda tushuntiriladi."]),
        ("Yakunlash", 5, ["Bu chorakda qaysi hayvon-robotlarni yasashlari haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Namoyishni kuzatish", 6, ["O'quvchilar elektr hayvon-modelning harakatini diqqat bilan kuzatadilar."]),
        ("Taqqoslash suhbati", 4, ["Robot harakati bilan haqiqiy hayvon harakati solishtiriladi."]),
    ],
    "uyga": [
        "Sizga yoqqan hayvonni tanlang va u qanday harakat qilishini (yuradi, sakraydi, uchadi) yozing.",
    ],
},

"Chorak kirish: sensorli modellar bilan tanishuv": {
    "maqsad": [
        "O'quvchilar sensor+motor birgalikda ishlaydigan \"aqlli\" modellar bilan tanishadilar.",
        "O'quvchilar sensorli modelning oddiy motorli modeldan farqini tushunadilar.",
        "O'quvchilar bu chorakda qanday aqlli modellar yasashlarini tasavvur qiladilar.",
    ],
    "lugat": [
        "Aqlli model (Smart model) – sensor orqali atrof-muhitga reaksiya beruvchi model",
        "Sensor (Sensor) – atrof-muhitni \"sezuvchi\" qurilma",
        "Reaksiya (Reaction) – sensor signaliga javob sifatida sodir bo'ladigan harakat",
        "Dastur (Program) – robotga berilgan buyruqlar ketma-ketligi",
        "Avtomatik (Automatic) – o'z-o'zidan ishlaydigan",
    ],
    "softSkill": "Mantiqiy fikrlash — \"agar sensor shuni sezsa, robot shunday qiladi\" mantig'ini tushunishga undash.",
    "resurslar": [
        "Sensorli aqlli model namunasi (namoyish uchun)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["O'tgan chorakdagi motorli modellar eslatiladi, bugun ularga \"aql\" qo'shamiz."]),
        ("Sensorli model qanday ishlaydi", 8, ["Sensor+motor birgalikda ishlashi (sensor sezadi -> robot harakat qiladi) namoyish qilinadi.", "Oddiy motorli model bilan sensorli model solishtiriladi."]),
        ("Yakunlash", 5, ["Bu chorakda yasaladigan sensorli modellar haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Namoyishni kuzatish", 7, ["O'quvchilar sensorli modelning reaksiyasini diqqat bilan kuzatadilar."]),
        ("Taxmin o'yini", 3, ["Sensor turlicha sinalganda robot qanday reaksiya berishi haqida taxmin qilinadi."]),
    ],
    "uyga": [
        "Uyda \"aqlli\" ishlaydigan (sensor bilan) 2 ta qurilmani toping va ular qanday ishlashini tasvirlang.",
    ],
},

"Chorak kirish: murakkab mexanizmlar va manipulyatorlar": {
    "maqsad": [
        "O'quvchilar manipulyator (robot-qo'l) tushunchasi bilan tanishadilar.",
        "O'quvchilar bir necha mexanizmning birgalikda ishlashini tushunadilar.",
        "O'quvchilar bu chorakda yasaladigan murakkab modellarni tasavvur qiladilar.",
    ],
    "lugat": [
        "Manipulyator (Manipulator) – narsalarni ushlab, ko'chiruvchi robot-qo'l",
        "Bo'g'in (Joint) – manipulyatorning egiluvchi qismi",
        "Kombinatsiya (Combination) – bir nechta mexanizmning birga ishlashi",
        "Barqarorlik (Stability) – modelning yiqilmay turish qobiliyati",
        "Murakkab konstruksiya (Complex structure) – ko'p qismli, ko'p bosqichli qurilma",
    ],
    "softSkill": "Bosqichma-bosqich fikrlash — murakkab vazifani kichik qadamlarga bo'lib bajarish ko'nikmasini shakllantirish.",
    "resurslar": [
        "Manipulyator/robot-qo'l namunasi (namoyish uchun, agar mavjud bo'lsa)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Haqiqiy robot-qo'llar (zavodlarda ishlatiladigan) haqida qisqacha video/rasm ko'rsatiladi."]),
        ("Manipulyator qanday ishlaydi", 8, ["Bir nechta bo'g'in birgalikda qanday harakat hosil qilishi tushuntiriladi.", "Richag, tishli g'ildirak va shkiv kabi bir nechta mexanizm bitta modelda birlashishi mumkinligi aytiladi."]),
        ("Yakunlash", 5, ["Bu chorakda yasaladigan murakkab modellar haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Namoyish yoki rasm tahlili", 7, ["O'quvchilar manipulyator rasmi/namunasidagi qismlarni nomlaydilar."]),
        ("Muhokama", 3, ["Manipulyator qayerlarda ishlatilishi (zavod, kosmik stansiya) haqida fikr almashiladi."]),
    ],
    "uyga": [
        "Robot-qo'llar qayerlarda ishlatilishi haqida internetdan bitta misol toping.",
    ],
},

"Chorak kirish: elektr hayvonlar — dinozavrlar va suv hayvonlari": {
    "maqsad": [
        "O'quvchilar dinozavr va suv hayvonlari shaklidagi elektr-robotlar bilan tanishadilar.",
        "O'quvchilar turli hayvon turlarining harakat farqlarini (yurish, suzish) muhokama qiladilar.",
        "O'quvchilar bu chorakda yasaladigan modellarni tasavvur qiladilar.",
    ],
    "lugat": [
        "Dinozavr (Dinosaur) – qadimda yashagan katta jonzot",
        "Suv hayvoni (Aquatic animal) – suvda yashaydigan jonzot",
        "Harakat naqshi (Movement pattern) – hayvonning o'ziga xos harakat tartibi",
        "Biomimikriya (Biomimicry) – tabiatdan ilhomlanib muhandislik yechimi yaratish",
        "Motor (Motor) – robotni harakatga keltiruvchi qurilma",
    ],
    "softSkill": "Tadqiqotchilik — dinozavr va suv hayvonlari haqida bilganlarini baham ko'rishga undash.",
    "resurslar": [
        "Dinozavr/suv hayvoni robot namunasi (namoyish uchun)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Dinozavrlar va suv hayvonlari haqida qiziqarli faktlar bilan suhbat boshlanadi."]),
        ("Har xil hayvon — har xil harakat", 8, ["Quruqlikda yuruvchi va suvda suzuvchi hayvonlarning harakat farqi muhokama qilinadi.", "Bu farq robot-modelda qanday aks etishi (oyoq vs suzgich) ko'rsatiladi."]),
        ("Yakunlash", 5, ["Bu chorakda yasaladigan hayvon-modellar ro'yxati qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Namoyishni kuzatish", 7, ["O'quvchilar namoyish qilingan modelning harakatini kuzatadilar."]),
        ("Muhokama", 3, ["Qaysi hayvon-model eng qiziqarli ko'rinishi haqida fikr almashiladi."]),
    ],
    "uyga": [
        "Sevimli dinozavr yoki suv hayvoningiz haqida qiziqarli fakt toping.",
    ],
},

"Chorak kirish: murakkab transport vositalari": {
    "maqsad": [
        "O'quvchilar murakkabroq transport vositalari (yuk mashinasi, trailer, sport mashina) bilan tanishadilar.",
        "O'quvchilar turli transport turlarining vazifasiga qarab farqlanishini tushunadilar.",
        "O'quvchilar bu chorakda yasaladigan transport modellarini tasavvur qiladilar.",
    ],
    "lugat": [
        "Transport vositasi (Vehicle) – yuk yoki odam tashuvchi mashina",
        "Trailer (Trailer) – ortga ulanadigan yuk qismi",
        "Shassi (Chassis) – transportning asosiy tayanch qismi",
        "Tezyurar mashina (Speed car) – tezlikka mo'ljallangan mashina",
        "Yurish tizimi (Drivetrain) – motordan g'ildirakkacha kuch uzatuvchi tizim",
    ],
    "softSkill": "Taqqoslash va tahlil — turli transport turlarini vazifasiga qarab solishtirish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "Turli transport rasmlari yoki namunalari",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Ko'chada ko'rilgan turli transport vositalari haqida suhbat."]),
        ("Transport turi vazifaga bog'liq", 8, ["Yuk mashinasi (ko'p g'ildirak, kuch) va sport mashina (tez, yengil) orasidagi dizayn farqi tushuntiriladi.", "Trailer qanday qo'shimcha yuk tashish imkonini berishi muhokama qilinadi."]),
        ("Yakunlash", 5, ["Bu chorakda yasaladigan transport modellari haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Rasm tahlili", 6, ["O'quvchilar turli transport rasmlarini ko'rib, ularning vazifasini taxmin qiladilar."]),
        ("Muhokama", 4, ["Qaysi transport turi eng qiziq ko'rinishi haqida fikr almashiladi."]),
    ],
    "uyga": [
        "Ko'chada ko'rgan 3 ta turli transport vositasini rasmga oling yoki chizing.",
    ],
},

"Chorak kirish: havo va suv transporti": {
    "maqsad": [
        "O'quvchilar havo (samolyot, vertolyot) va suv (qayiq, kema) transportlari bilan tanishadilar.",
        "O'quvchilar bu ikki transport turining qanday kuchlar asosida harakatlanishini umumiy tarzda tushunadilar.",
        "O'quvchilar bu chorakda yasaladigan modellarni tasavvur qiladilar.",
    ],
    "lugat": [
        "Havo transporti (Air transport) – samolyot, vertolyot kabi uchuvchi vositalar",
        "Suv transporti (Water transport) – qayiq, kema kabi suzuvchi vositalar",
        "Parrak (Propeller) – havoni itaruvchi aylanuvchi qism",
        "Suzuvchanlik (Buoyancy) – suvda qalqib turish qobiliyati",
        "Aerodinamika (Aerodynamics) – havo harakati bilan bog'liq fizika sohasi",
    ],
    "softSkill": "Qiziqish va tadqiqotchilik — havo va suv transportlari haqida savol berish va bilim izlashga undash.",
    "resurslar": [
        "Havo/suv transport rasmlari yoki namunalari",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Samolyot va kemalarni ko'rganmizmi degan savol bilan kirish qilinadi."]),
        ("Ikki muhit — ikki xil harakat", 8, ["Havoda uchish (parrak, aerodinamika) va suvda suzish (suzuvchanlik) asosiy tamoyillari sodda tarzda tushuntiriladi.", "Ikkalasi ham \"muhitga qarshi kurashish\" tamoyiliga asoslanishi muhokama qilinadi."]),
        ("Yakunlash", 5, ["Bu chorakda yasaladigan havo/suv modellari haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Rasm/video tahlili", 6, ["O'quvchilar havo va suv transportlari rasmlarini ko'rib, farqlarini aytadilar."]),
        ("Muhokama", 4, ["Qaysi transport turini yasashni xohlashlari haqida fikr almashiladi."]),
    ],
    "uyga": [
        "Havo yoki suv transporti haqida qiziqarli video/rasm toping va nima yangilik bilganingizni yozing.",
    ],
},

"Chorak kirish: muhandislik dizayni jarayoni, yuk ko'targichlar": {
    "maqsad": [
        "O'quvchilar muhandislik dizayni jarayoni (muammoni aniqlash -> g'oya -> qurish -> sinash -> yaxshilash) bilan tanishadilar.",
        "O'quvchilar yuk ko'targich robotlarning turli ko'rinishlari bilan tanishadilar.",
        "O'quvchilar 4-sinf davomida qanday yondashuvda ishlashlarini tushunadilar.",
    ],
    "lugat": [
        "Muhandislik dizayni jarayoni (Engineering design process) – muammoni hal qilish uchun bosqichma-bosqich yondashuv",
        "Muammoni aniqlash (Define the problem) – nima hal qilinishi kerakligini belgilash",
        "Prototip (Prototype) – g'oyani sinab ko'rish uchun yasalgan dastlabki model",
        "Takomillashtirish (Iteration/Improvement) – modelni sinov natijalariga qarab yaxshilash",
        "Yuk ko'targich (Lifting robot) – og'ir yukni ko'taruvchi/tashuvchi robot",
    ],
    "softSkill": "Muhandislik tafakkuri — muammoni tizimli bosqichlar orqali hal qilish yondashuvini shakllantirish.",
    "resurslar": [
        "Muhandislik dizayni jarayoni sxemasi (plakat yoki slayd)",
        "Yuk ko'targich robot namunalari yoki rasmlari",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["4-sinfda ishlash uslubi biroz o'zgarishi — endi ko'proq mustaqil dizayn qilishlari aytiladi."]),
        ("Muhandislik dizayni jarayoni", 8, ["5 bosqich (muammoni aniqlash, g'oya, qurish, sinash, yaxshilash) sxema orqali tushuntiriladi.", "Yuk ko'targich robotlarning turli ko'rinishlari (kran, forklift) rasmda ko'rsatiladi."]),
        ("Yakunlash", 5, ["Bu chorakda o'quvchilar shu jarayonni qo'llab, yuk tashish robotini yasashlari aytiladi."]),
    ],
    "amaliy": [
        ("Muammoni aniqlash mashqi", 6, ["O'quvchilar \"omborda yukni qo'lda tashish qiyin\" kabi sodda muammoni tahlil qiladilar."]),
        ("G'oya generatsiyasi", 4, ["O'quvchilar bu muammoni qanday hal qilish mumkinligi haqida tezkor g'oyalar aytadilar."]),
    ],
    "uyga": [
        "Uyda yoki maktabda \"muammo\" deb hisoblagan bitta narsani toping va uni qanday hal qilish mumkinligi haqida yozing.",
    ],
},

"Chorak kirish: patrul va qidiruv robotlari": {
    "maqsad": [
        "O'quvchilar patrul va qidiruv-qutqaruv robotlarining vazifasi bilan tanishadilar.",
        "O'quvchilar avtonom (odam aralashuvisiz ishlovchi) robot tushunchasini chuqurroq tushunadilar.",
        "O'quvchilar bu chorakda yasaladigan modellarni tasavvur qiladilar.",
    ],
    "lugat": [
        "Patrul robot (Patrol robot) – belgilangan hudud bo'ylab kuzatuv olib boruvchi robot",
        "Qidiruv-qutqaruv roboti (Search and rescue robot) – xavfli joylarda odamlarni qidiruvchi robot",
        "Avtonom (Autonomous) – odam aralashuvisiz, o'z-o'zidan ishlaydigan",
        "Sensor tarmog'i (Sensor array) – bir nechta sensorning birgalikda ishlashi",
        "Marshrut (Route) – robot bosib o'tadigan yo'l",
    ],
    "softSkill": "Ijtimoiy mas'uliyat — robototexnika inson hayotini qutqarishga qanday xizmat qilishi mumkinligini muhokama qilish.",
    "resurslar": [
        "Patrul/qidiruv robot rasmlari yoki video (agar mavjud bo'lsa)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Haqiqiy hayotda qidiruv-qutqaruv robotlari qanday ishlatilishi (zilzila, yong'in) haqida suhbat."]),
        ("Avtonom robot qanday ishlaydi", 8, ["Sensor+dastur birgalikda robotga \"o'z-o'zidan qaror qabul qilish\" imkonini berishi tushuntiriladi.", "Patrul robotning marshrut bo'ylab qanday harakatlanishi muhokama qilinadi."]),
        ("Yakunlash", 5, ["Bu chorakda yasaladigan patrul/qidiruv modellari haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Video/rasm tahlili", 6, ["O'quvchilar qidiruv-qutqaruv robotlari haqidagi rasm/video misollarini muhokama qiladilar."]),
        ("G'oya taklif qilish", 4, ["O'quvchilar o'z patrul roboti qanday vazifani bajarishini taklif qiladilar."]),
    ],
    "uyga": [
        "Qidiruv-qutqaruv robotlari haqida internetdan bitta qiziqarli misol toping.",
    ],
},

"Chorak kirish: kosmik texnika va rover'lar": {
    "maqsad": [
        "O'quvchilar kosmik rover va boshqa kosmik robototexnika bilan chuqurroq tanishadilar.",
        "O'quvchilar kosmosdagi sharoit (gravitatsiya, notekis yuza) muhandislikka qanday ta'sir qilishini tushunadilar.",
        "O'quvchilar bu chorakda yasaladigan kosmik modellarni tasavvur qiladilar.",
    ],
    "lugat": [
        "Rover (Rover) – boshqa sayyora/oy yuzasida harakatlanadigan mashina",
        "Gravitatsiya (Gravity) – jismlarni tortib turuvchi kuch",
        "Regolit (Regolith) – Oy/Mars yuzasini qoplagan chang-tosh qatlami",
        "Avtonom navigatsiya (Autonomous navigation) – roverning odam yordamisiz yo'l topishi",
        "Missiya (Mission) – kosmik texnikaning bajarishi kerak bo'lgan vazifasi",
    ],
    "softSkill": "Ilmiy qiziqish va kelajakka moyillik — kosmik tadqiqotlarning kelajagi haqida fikr almashishga undash.",
    "resurslar": [
        "Mars/Oy rover rasmlari yoki video",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["Haqiqiy Mars/Oy missiyalari haqida qiziqarli faktlar bilan suhbat boshlanadi."]),
        ("Kosmik muhandislik muammolari", 8, ["Notekis yuza, past gravitatsiya kabi sharoitlar rover dizayniga qanday ta'sir qilishi tushuntiriladi.", "Roverning asosiy vazifalari (tadqiqot, namuna olish) muhokama qilinadi."]),
        ("Yakunlash", 5, ["Bu chorakda yasaladigan kosmik modellar haqida qisqacha aytib o'tiladi."]),
    ],
    "amaliy": [
        ("Video/rasm tahlili", 6, ["O'quvchilar haqiqiy rover rasmlarini ko'rib, qismlarini taxmin qiladilar."]),
        ("Muhokama", 4, ["O'z rover g'oyalari haqida qisqacha fikr almashiladi."]),
    ],
    "uyga": [
        "Mars yoki Oy roverlaridan biri haqida qiziqarli fakt toping (masalan, nomi, vazifasi).",
    ],
},

"Chorak kirish: bitiruv loyihasiga umumiy tayyorgarlik": {
    "maqsad": [
        "O'quvchilar yakuniy bitiruv loyihasining talablari va bosqichlari bilan tanishadilar.",
        "O'quvchilar 0-4-sinf davomida o'rgangan bilimlarini umumlashtirib, loyiha uchun g'oya shakllantiradilar.",
        "O'quvchilar bitiruv ko'rgazmasiga tayyorgarlik jarayonini tushunadilar.",
    ],
    "lugat": [
        "Bitiruv loyihasi (Capstone project) – yil yakunidagi yakuniy, mustaqil loyiha",
        "Texnik topshiriq (Technical brief) – loyiha talablari yozilgan qisqa hujjat",
        "Portfolio/Muhandislik daftari (Engineering notebook) – loyiha jarayonini qayd etuvchi daftar",
        "Taqdimot (Presentation) – loyihani boshqalarga tushuntirib berish",
        "Ko'rgazma (Exhibition) – tayyor loyihalarni namoyish qilish tadbiri",
    ],
    "softSkill": "Mas'uliyat va rejalashtirish — o'z loyihasini boshidan oxirigacha mustaqil rejalashtirish va bajarish ko'nikmasini shakllantirish.",
    "resurslar": [
        "O'tgan yillardagi eng yaxshi loyihalar rasmlari (agar mavjud bo'lsa)",
        "Texnik topshiriq shabloni (qog'ozda yoki elektron)",
        "Taqdimot uchun kompyuter va proyektor",
    ],
    "nazariya": [
        ("Kirish", 7, ["0-4-sinf davomida yasalgan turli xil robotlar qisqacha eslanadi (rasm/slayd orqali)."]),
        ("Bitiruv loyihasi talablari", 8, ["Loyiha qanday bosqichlardan iborat bo'lishi (g'oya, dizayn, qurish, dasturlash, sinov, taqdimot) tushuntiriladi.", "Baholash mezonlari (funksionallik, ijodkorlik, taqdimot) qisqacha aytib o'tiladi."]),
        ("Yakunlash", 5, ["O'quvchilarga g'oya haqida o'ylab kelish uyga vazifa qilib beriladi."]),
    ],
    "amaliy": [
        ("Miya to'foni (brainstorm)", 7, ["O'quvchilar o'z bitiruv loyihasi uchun dastlabki g'oyalarni qog'ozga yozadilar."]),
        ("Kichik muhokama", 3, ["Bir-ikkita o'quvchi o'z g'oyasini qisqacha aytib beradi."]),
    ],
    "uyga": [
        "Bitiruv loyihangiz uchun 2-3 ta g'oya yozib keling — qaysi muammoni hal qilmoqchisiz?",
    ],
},

}
