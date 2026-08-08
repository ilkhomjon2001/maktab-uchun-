# -*- coding: utf-8 -*-
"""
2-yil, 2-3-sinf, 3-4-chorak "Dasturlash" (Scratch-uslub, Makerzoid ilovasi) darslari uchun
to'liq kontent. 29 ta noyob mavzu, title matni bo'yicha kalitlangan.
"""

DASTURLASH_CONTENT = {

"Scratch-uslub muhitni chuqurroq o'rganish": {
    "maqsad": ["O'quvchilar Scratch-uslub Makerzoid ilovasining interfeysi va asosiy blok turlarini chuqurroq o'rganadilar.", "O'quvchilar ilovada yangi loyiha yaratish va saqlashni mustaqil bajaradilar.", "O'quvchilar 1-yilda o'rgangan asosiy bloklarni eslaydilar."],
    "lugat": ["Interfeys (Interface) – dastur bilan foydalanuvchi o'rtasidagi muloqot oynasi", "Blok kutubxonasi (Block palette) – barcha bloklar joylashgan panel", "Loyiha (Project) – saqlanadigan dastur fayli", "Skript (Script) – bloklardan tuzilgan dastur", "Ijro etish (Run) – dasturni ishga tushirish"],
    "softSkill": "Mustaqil o'rganish — ilova interfeysini o'zi kashf qilib, yangi imkoniyatlarni topish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model", "Taqdimot uchun kompyuter va proyektor"],
    "nazariya": [("Kirish", 7, ["1-yilda o'rgangan asosiy bloklar (harakat, motor) eslanadi."]), ("Interfeys bilan tanishuv", 10, ["Blok kutubxonasi, skript maydoni va boshqaruv tugmalari ko'rsatiladi.", "Yangi loyiha yaratish va saqlash bosqichlari ko'rsatiladi."]), ("Yakunlash", 3, ["Bu chorakda qanday yangi mavzular o'rganilishi qisqacha aytiladi."])],
    "amaliy": [("Interfeysni kashf qilish", 15, ["O'quvchilar ilovani mustaqil ochib, turli bo'limlarni ko'rib chiqadilar."]), ("Yangi loyiha yaratish", 10, ["O'quvchilar yangi loyiha ochib, nom berib saqlaydilar."])],
    "uyga": ["Ilovada yana qanday bo'limlar borligini ko'rib, bittasini tasvirlab yozing."],
},

"Ketma-ketlik+sikl mustahkamlash": {
    "maqsad": ["O'quvchilar ketma-ketlik va sikl (takrorlash) bloklarini birgalikda ishlatishni mustahkamlaydilar.", "O'quvchilar bir nechta harakatni tartib bilan va takrorlab bajaradigan dastur tuzadilar.", "O'quvchilar dasturni sinash va xatoni topish ko'nikmasini rivojlantiradilar."],
    "lugat": ["Ketma-ketlik (Sequence) – bloklarning tartib bilan bajarilishi", "Sikl (Loop) – bir necha marta takrorlanadigan bloklar guruhi", "Takrorlash soni (Repeat count) – sikl necha marta ishlashi", "Dastur (Program) – bloklar to'plami", "Sinov (Test) – dasturni ishga tushirib tekshirish"],
    "softSkill": "Tizimli fikrlash — dasturni qadam-baqadam rejalashtirib, keyin yozish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["Ketma-ketlik va sikl nima ekanligi qisqacha eslanadi."]), ("Ikkalasini birlashtirish", 10, ["Bir nechta harakatni ketma-ket qo'yib, keyin butun ketma-ketlikni sikl ichiga joylashtirish ko'rsatiladi."]), ("Yakunlash", 3, ["Bu texnikaning dasturni qisqartirishdagi foydasi umumlashtiriladi."])],
    "amaliy": [("Dastur tuzish", 15, ["O'quvchilar 2-3 blokli ketma-ketlikni sikl ichiga joylashtirib, modelni harakatlantiradilar."]), ("Sinov", 10, ["O'quvchilar dasturni ishga tushirib, takrorlanish sonini o'zgartirib sinaydilar."])],
    "uyga": ["Sikl ichida qaysi harakatlarni takrorlash qiziqarli bo'lishi haqida g'oya yozing."],
},

"O'zgaruvchi (hisoblagich) bilan tanishuv": {
    "maqsad": ["O'quvchilar o'zgaruvchi (variable) tushunchasini va uning dasturlashdagi vazifasini tushunadilar.", "O'quvchilar Scratch-uslub ilovada o'zgaruvchi yaratish va undan foydalanishni o'rganadilar.", "O'quvchilar hisoblagich yordamida robot harakatlarini sanashni amalda qo'llaydilar."],
    "lugat": ["O'zgaruvchi (Variable) – dastur ishlash jarayonida qiymati o'zgarishi mumkin bo'lgan xotira katakchasi", "Hisoblagich (Counter) – biror narsani sanash uchun ishlatiladigan o'zgaruvchi", "Qiymat (Value) – o'zgaruvchida saqlangan son yoki ma'lumot", "Ortirish (Increment) – qiymatni birga oshirish", "Blok (Block) – Scratch dasturidagi buyruq elementi"],
    "softSkill": "Mantiqiy fikrlash (Logical thinking) — qadamma-qadam fikrlash orqali masalani yechish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet yoki telefon (Makerzoid ilovasi o'rnatilgan)", "1-yilda yasalgan model (masalan, motorli model)", "Taqdimot uchun kompyuter va proyektor"],
    "nazariya": [("Kirish", 7, ["Kundalik hayotda sanash misollari: pul sanash, qadam sanagich, o'yin balli.", "Savol: kompyuter/robot narsalarni qanday \"eslab qoladi\" va sanaydi?"]), ("O'zgaruvchi yaratish", 10, ["Ilovada yangi o'zgaruvchi yaratish bosqichlari.", "O'zgaruvchiga boshlang'ich qiymat berish (masalan, 0).", "\"Ortirish\" (+1) blogi bilan tanishtiriladi."]), ("Yakunlash", 3, ["O'zgaruvchining dasturlashdagi ahamiyati umumlashtiriladi — u dasturga \"xotira\" beradi."])],
    "amaliy": [("O'zgaruvchi yaratish", 10, ["O'quvchilar ilovada \"hisoblagich\" nomli o'zgaruvchi yaratadilar va uni 0 ga tenglaydilar."]), ("Robot bilan bog'lash", 15, ["O'quvchilar 1-yilda yasagan modellariga dastur yozib, motor har aylanganda hisoblagichni +1 oshiradigan qiladilar.", "Hisoblagich qiymati tekshiriladi."])],
    "uyga": ["Kundalik hayotda o'zgaruvchi kabi ishlaydigan 2 ta narsani toping (masalan, elektr hisoblagichi, soat) va ular nimani \"eslab qolishini\" tushuntirib yozing."],
},

"Hisoblagich bilan o'yin": {
    "maqsad": ["O'quvchilar hisoblagich (o'zgaruvchi)dan foydalangan kichik o'yin dasturini tuzadilar.", "O'quvchilar hisoblagich qiymatini ekranda ko'rsatishni o'rganadilar.", "O'quvchilar o'z o'yinini sinfga namoyish etadilar."],
    "lugat": ["Hisoblagich (Counter) – sanash uchun o'zgaruvchi", "O'yin sharti (Win condition) – o'yin g'alaba deb hisoblanadigan holat", "Ko'rsatish (Display) – qiymatni ekranda chiqarish", "Sinov (Test) – dasturni tekshirish", "Blok (Block) – dastur buyrug'i"],
    "softSkill": "Ijodkorlik — hisoblagich asosida o'z kichik o'yinini o'ylab topish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["O'tgan darsdagi hisoblagich eslanadi."]), ("O'yin g'oyasi", 10, ["Hisoblagich muayyan songa yetganda maxsus harakat (masalan, tovush) sodir bo'lishi tushuntiriladi."]), ("Yakunlash", 3, ["O'yin g'oyalari qisqacha muhokama qilinadi."])],
    "amaliy": [("O'yin dasturini tuzish", 15, ["O'quvchilar hisoblagich muayyan songa yetganda maxsus reaksiya beradigan dastur tuzadilar."]), ("Sinov va namoyish", 10, ["O'quvchilar o'yinlarini sinab, sinfga ko'rsatadilar."])],
    "uyga": ["O'z o'yiningizni yanada qiziqarli qilish uchun bitta g'oya yozing."],
},

"Ikki sensorni birlashtirish": {
    "maqsad": ["O'quvchilar ikki xil sensordan bir vaqtning o'zida foydalanishni o'rganadilar.", "O'quvchilar ikkala sensor signalini birlashtirib qaror qabul qiluvchi dastur tuzadilar.", "O'quvchilar dasturni sinab, ikkala sensorning to'g'ri ishlashini tekshiradilar."],
    "lugat": ["Sensor (Sensor) – atrof-muhitni sezuvchi qurilma", "Signal birlashtirish (Combining signals) – ikki sensor ma'lumotini birga ishlatish", "Shart (Condition) – \"agar\" mantig'i", "Reaksiya (Reaction) – sensor signaliga javob", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Murakkab fikrlash — bir nechta manbadan kelayotgan ma'lumotni birga tahlil qilish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Ikki xil sensorli model"],
    "nazariya": [("Kirish", 7, ["Bitta sensor bilan ishlash eslanadi, bugun ikkitasini birga ishlatamiz."]), ("Ikki sensorni birlashtirish", 10, ["Ikkala sensordan kelgan signalni bitta dasturda qanday ishlatish mumkinligi tushuntiriladi."]), ("Yakunlash", 3, ["Ikki sensorning birga ishlashi robotni yanada \"aqlli\" qilishi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar ikkala sensordan foydalangan dasturni tuzadilar."]), ("Sinov", 10, ["O'quvchilar dasturni turli sharoitda sinaydilar."])],
    "uyga": ["Ikki sensor birga ishlatilgan yana bitta g'oya (masalan, aqlli xona) yozing."],
},

"Shart ichida shart (murakkabroq)": {
    "maqsad": ["O'quvchilar shart blokini boshqa shart bloki ichiga joylashtirishni o'rganadilar.", "O'quvchilar bir nechta bosqichli qaror qabul qilish mantig'ini tushunadilar.", "O'quvchilar murakkabroq dasturni sinab, natijasini tekshiradilar."],
    "lugat": ["Ichma-ich shart (Nested condition) – shart ichidagi shart", "Qaror daraxti (Decision tree) – bir nechta shartning ketma-ket tekshirilishi", "Mantiq (Logic) – dasturning qaror qabul qilish tartibi", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Bosqichma-bosqich mantiqiy tahlil — murakkab qarorni kichik bosqichlarga bo'lib tekshirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Sensorli model"],
    "nazariya": [("Kirish", 7, ["Oddiy shart (agar) eslanadi."]), ("Shart ichida shart", 10, ["Bitta shart ichiga ikkinchi shart joylashtirilsa, ikki bosqichli qaror hosil bo'lishi tushuntiriladi (masalan: agar to'siq bo'lsa, VA u yaqin bo'lsa, to'xta)."]), ("Yakunlash", 3, ["Bu texnikaning murakkabroq vaziyatlarda foydasi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar ichma-ich shartli dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar turli holatlarni sinab, dastur to'g'ri ishlashini tekshiradilar."])],
    "uyga": ["Ichma-ich shart kerak bo'ladigan kundalik vaziyatga bitta misol yozing (masalan: agar yomg'ir yog'sa, VA sovuq bo'lsa...)."],
},

"Funksiya (blok guruhi) tushunchasi": {
    "maqsad": ["O'quvchilar funksiya (bloklar guruhi) tushunchasi va uning dasturlashdagi ahamiyatini tushunadilar.", "O'quvchilar tayyor funksiyalarni dasturda qanday chaqirishni o'rganadilar.", "O'quvchilar funksiyalarning dasturni qisqartirishga yordam berishini his qiladilar."],
    "lugat": ["Funksiya (Function/Block) – qayta-qayta ishlatiladigan buyruqlar to'plami", "Chaqirish (Call) – funksiyani ishga tushirish", "Modullilik (Modularity) – dasturni kichik qismlarga bo'lish tamoyili", "Qayta foydalanish (Reuse) – bir marta yozilgan kodni qayta ishlatish", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Samaradorlikka intilish — bir xil ishni qayta yozmasdan, uni bir marta yaratib qayta ishlatish g'oyasini qadrlash.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["Bir xil bloklar ketma-ketligini bir necha marta yozish noqulayligi haqida savol-javob."]), ("Funksiya nima", 10, ["Funksiya — qayta-qayta ishlatiladigan buyruqlar to'plami ekanligi tushuntiriladi.", "Tayyor funksiyani dasturda chaqirish ko'rsatiladi."]), ("Yakunlash", 3, ["Funksiyaning dasturni qisqa va tushunarli qilishi umumlashtiriladi."])],
    "amaliy": [("Funksiyani sinash", 15, ["O'quvchilar tayyor funksiyani o'z dasturida chaqirib ishlatadilar."]), ("Muhokama", 10, ["Funksiya ishlatilmagan va ishlatilgan dastur uzunligi solishtiriladi."])],
    "uyga": ["Qanday harakatlarni funksiya qilib yozish qulay bo'lishi haqida 2 ta misol yozing."],
},

"O'z funksiyamni yaratish": {
    "maqsad": ["O'quvchilar o'zlarining funksiyasini mustaqil yaratishni o'rganadilar.", "O'quvchilar funksiya ichiga bir nechta blokni joylashtiradilar.", "O'quvchilar yaratgan funksiyasini dasturda chaqirib sinaydilar."],
    "lugat": ["Yangi funksiya yaratish (Create a new block) – o'z funksiyasini tuzish jarayoni", "Funksiya nomi (Function name) – funksiyaga beriladigan nom", "Funksiya tanasi (Function body) – funksiya ichidagi bloklar", "Chaqirish (Call) – funksiyani ishga tushirish", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Ijodiy tuzilmalashtirish — o'z dasturini mantiqiy qismlarga bo'lib nomlash ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["Tayyor funksiyalarni chaqirish eslanadi, bugun o'zimiz funksiya yaratamiz."]), ("Funksiya yaratish bosqichlari", 10, ["Yangi funksiya yaratish, unga nom berish va ichiga bloklar qo'yish ko'rsatiladi."]), ("Yakunlash", 3, ["Yaratilgan funksiyani asosiy dasturda chaqirish eslatiladi."])],
    "amaliy": [("Funksiya yaratish", 15, ["O'quvchilar o'z funksiyasini yaratib, ichiga 2-3 blok joylashtiradilar."]), ("Chaqirish va sinov", 10, ["O'quvchilar yaratgan funksiyasini asosiy dasturda chaqirib, natijani sinaydilar."])],
    "uyga": ["Yaratgan funksiyangizga qanday nom berganingizni va nima uchun ekanini yozing."],
},

"Funksiyadan qayta foydalanish": {
    "maqsad": ["O'quvchilar bitta funksiyani dasturning turli joylarida qayta chaqirishni o'rganadilar.", "O'quvchilar funksiyaning dasturni qisqartirish va tartibga solishdagi rolini chuqurroq tushunadilar.", "O'quvchilar bir nechta funksiyadan tashkil topgan dastur tuzadilar."],
    "lugat": ["Qayta foydalanish (Reuse) – bir marta yaratilgan funksiyani bir necha marta chaqirish", "Funksiyalar kutubxonasi (Function library) – o'z yaratgan funksiyalar to'plami", "Dastur tuzilishi (Program structure) – dasturning mantiqiy tashkil etilishi", "Chaqirish (Call) – funksiyani ishga tushirish", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Tejamkorlik va tartib — bir xil kodni takror yozmaslik orqali vaqtni tejash va dasturni tartibli tutish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["O'tgan darsda yaratilgan funksiya eslanadi."]), ("Bir funksiyani ko'p marta chaqirish", 10, ["Bitta funksiyani dasturning bir necha joyida chaqirish orqali kod qisqarishi ko'rsatiladi."]), ("Yakunlash", 3, ["Funksiyalardan qayta foydalanishning afzalliklari umumlashtiriladi."])],
    "amaliy": [("Dastur tuzish", 15, ["O'quvchilar bitta funksiyani dasturning kamida 2 joyida chaqiradigan dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar dasturni ishga tushirib, funksiyaning har safar to'g'ri ishlashini tekshiradilar."])],
    "uyga": ["Funksiyadan qayta foydalanish sizga qanday vaqt tejashi haqida qisqacha fikringizni yozing."],
},

"Murakkab shartlar: VA, YOKI": {
    "maqsad": ["O'quvchilar VA (AND) va YOKI (OR) mantiqiy operatorlarini tushunadilar.", "O'quvchilar ikki shartni birlashtirib, murakkabroq qaror qabul qiluvchi dastur tuzadilar.", "O'quvchilar VA va YOKI orasidagi farqni amaliy misolda ko'rsatadilar."],
    "lugat": ["VA operatori (AND) – ikkala shart ham to'g'ri bo'lganda ishlaydigan mantiq", "YOKI operatori (OR) – kamida bitta shart to'g'ri bo'lganda ishlaydigan mantiq", "Mantiqiy operator (Logical operator) – shartlarni birlashtiruvchi belgi", "Shart (Condition) – \"agar\" mantig'i", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Murakkab mantiqiy fikrlash — bir nechta shartni birgalikda baholash ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Ikki sensorli model"],
    "nazariya": [("Kirish", 7, ["Kundalik hayotdan VA/YOKI misollari (masalan: \"agar sovuq VA yomg'ir bo'lsa\") muhokama qilinadi."]), ("VA va YOKI farqi", 10, ["VA — ikkala shart ham to'g'ri bo'lganda, YOKI — kamida bittasi to'g'ri bo'lganda ishlashi tushuntiriladi.", "Ikkala operator ham dasturda sinab ko'riladi."]), ("Yakunlash", 3, ["VA/YOKI qachon ishlatilishi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar VA operatoridan foydalangan dastur, keyin YOKI operatoridan foydalangan dastur tuzadilar."]), ("Sinov va taqqoslash", 10, ["O'quvchilar ikkala dasturni sinab, natija farqini kuzatadilar."])],
    "uyga": ["VA va YOKI operatorlaridan foydalanadigan bittadan kundalik hayot misolini yozing."],
},

"Mantiqiy o'yin": {
    "maqsad": ["O'quvchilar VA/YOKI mantig'ini o'yin shaklida mustahkamlaydilar.", "O'quvchilar mantiqiy operatorlar bilan kichik interaktiv o'yin tuzadilar.", "O'quvchilar o'yinni sinfga namoyish etadilar."],
    "lugat": ["Mantiqiy o'yin (Logic game) – shartlarga asoslangan o'yin", "VA/YOKI (AND/OR) – mantiqiy operatorlar", "G'alaba sharti (Win condition) – o'yin yutuq holati", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "O'yinlashtirilgan ijod — jiddiy mavzuni qiziqarli o'yin shakliga aylantirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Sensorli model"],
    "nazariya": [("Kirish", 7, ["O'tgan darsdagi VA/YOKI eslanadi."]), ("O'yin g'oyasi", 10, ["Mantiqiy shartlarga asoslangan oddiy o'yin g'oyasi (masalan, \"ikkala sensor ham signal bersa g'alaba\") taklif qilinadi."]), ("Yakunlash", 3, ["O'yin qoidalari qisqacha aniqlashtiriladi."])],
    "amaliy": [("O'yinni yaratish", 15, ["O'quvchilar VA/YOKI operatoridan foydalangan kichik o'yin dasturini tuzadilar."]), ("Sinov va namoyish", 10, ["O'quvchilar o'yinlarini sinab, sinfga ko'rsatadilar."])],
    "uyga": ["O'yiningizni yanada qiziqarli qilish uchun bitta yangi qoida o'ylab yozing."],
},

"Ichma-ich sikllar": {
    "maqsad": ["O'quvchilar sikl ichidagi sikl (nested loop) tushunchasini o'rganadilar.", "O'quvchilar ichma-ich sikl yordamida takrorlanuvchi naqsh hosil qiladilar.", "O'quvchilar dasturni sinab, natijani kuzatadilar."],
    "lugat": ["Ichma-ich sikl (Nested loop) – sikl ichidagi sikl", "Tashqi sikl (Outer loop) – asosiy takrorlash", "Ichki sikl (Inner loop) – tashqi sikl ichidagi qo'shimcha takrorlash", "Naqsh (Pattern) – takrorlanuvchi harakat tartibi", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Abstrakt fikrlash — ikki darajali takrorlanishni tasavvur qilish va rejalashtirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli model"],
    "nazariya": [("Kirish", 7, ["Oddiy sikl eslanadi, bugun sikl ichida sikl bo'lishi mumkinligi aytiladi."]), ("Ichma-ich sikl qanday ishlaydi", 10, ["Tashqi sikl har bir aylanishida ichki sikl to'liq bajarilishi misolda ko'rsatiladi (masalan, 3 marta 2 tadan aylanish = 6 marta)."]), ("Yakunlash", 3, ["Ichma-ich siklning murakkab naqshlar yaratishdagi foydasi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar ichma-ich sikldan foydalanib, robotni takrorlanuvchi naqsh bo'yicha harakatlantiradilar."]), ("Sinov", 10, ["O'quvchilar tashqi va ichki sikl sonlarini o'zgartirib, natijani kuzatadilar."])],
    "uyga": ["Ichma-ich sikl yordamida qanday chiroyli naqsh yasash mumkinligi haqida g'oya chizib yozing."],
},

"Naqshli harakat dasturi": {
    "maqsad": ["O'quvchilar ichma-ich sikl yordamida robotni muayyan naqsh bo'yicha harakatlantiradilar.", "O'quvchilar naqsh parametrlarini (takrorlash soni, burchak) sozlaydilar.", "O'quvchilar natijani sinab, kerak bo'lsa tuzatadilar."],
    "lugat": ["Naqsh (Pattern) – takrorlanuvchi harakat tartibi", "Burchak (Angle) – burilish darajasi", "Parametr (Parameter) – dasturda sozlanadigan qiymat", "Ichma-ich sikl (Nested loop) – sikl ichidagi sikl", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Aniqlik va sozlash — parametrlarni aniq sozlab, kutilgan natijaga erishish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli model"],
    "nazariya": [("Kirish", 7, ["O'tgan darsdagi ichma-ich sikl eslanadi."]), ("Naqsh dasturi rejasi", 10, ["Robot qaysi naqsh (kvadrat, yulduzcha) bo'yicha harakatlanishi rejalashtiriladi.", "Kerakli burchak va takrorlash sonlari hisoblanadi."]), ("Yakunlash", 3, ["Naqshli harakatning amaliy qo'llanilishi (masalan, robot-o'yinchoq) qisqacha aytiladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar rejalashtirilgan naqsh bo'yicha dastur tuzadilar."]), ("Sinov va tuzatish", 10, ["O'quvchilar dasturni sinab, naqsh to'g'ri chiqmasa parametrlarni tuzatadilar."])],
    "uyga": ["O'zingiz yasagan naqshning rasmini chizing (robot qaysi yo'l bo'ylab yurgan bo'lsa)."],
},

"Ikki sensorli qaror qabul qilish": {
    "maqsad": ["O'quvchilar ikki sensordan kelgan ma'lumot asosida qaror qabul qiluvchi dastur tuzadilar.", "O'quvchilar VA/YOKI operatorlarini real sensor vaziyatida qo'llaydilar.", "O'quvchilar dasturni turli sharoitda sinaydilar."],
    "lugat": ["Qaror qabul qilish (Decision making) – shartlar asosida harakat tanlash", "Ikki sensorli tizim (Dual-sensor system) – ikkita sensordan foydalanuvchi tizim", "VA/YOKI (AND/OR) – mantiqiy operatorlar", "Shart (Condition) – \"agar\" mantig'i", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Murakkab qaror qabul qilish — bir nechta manbadan kelgan ma'lumotni tahlil qilib, to'g'ri qaror qabul qilish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Ikki sensorli model"],
    "nazariya": [("Kirish", 7, ["Bitta sensorli qaror qabul qilish eslanadi."]), ("Ikki sensorli qaror", 10, ["Ikkala sensordan kelgan ma'lumot VA/YOKI orqali birlashtirilib, murakkabroq qaror qabul qilinishi tushuntiriladi."]), ("Yakunlash", 3, ["Bunday tizimlarning real hayotdagi (aqlli uy) qo'llanilishi aytiladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar ikki sensordan foydalangan qaror qabul qiluvchi dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar turli sensor kombinatsiyalarini sinaydilar."])],
    "uyga": ["Ikki sensorli qaror qabul qilish kerak bo'ladigan yana bitta vaziyat o'ylab yozing."],
},

"Ko'p qadamli dastur rejasi": {
    "maqsad": ["O'quvchilar bir nechta bosqichdan iborat murakkab dasturni oldindan rejalashtiradilar.", "O'quvchilar rejani qadamma-qadam kod bilan amalga oshirishni o'rganadilar.", "O'quvchilar rejalashtirishning dasturlashni osonlashtirishini his qiladilar."],
    "lugat": ["Dastur rejasi (Program plan) – dasturni yozishdan oldingi qadamlar ro'yxati", "Bosqich (Step) – dasturning bitta mantiqiy qismi", "Blok-sxema (Flowchart) – rejani chizma ko'rinishida ifodalash", "Ketma-ketlik (Sequence) – bosqichlarning tartibi", "Dastur (Program) – bloklar to'plami"],
    "softSkill": "Rejalashtirish — murakkab ishni boshlashdan oldin reja tuzish odatini shakllantirish.",
    "resurslar": ["Qog'oz va qalam (reja chizish uchun)", "Planshet/telefon (Makerzoid ilovasi)", "Robot-kuryer modeli (masalan, Telecar)"],
    "nazariya": [("Kirish", 7, ["Nega murakkab ishni rejasiz boshlash qiyinligi haqida suhbat."]), ("Reja tuzish", 10, ["Ko'p qadamli vazifa (masalan, kuryer-robot marshruti) bosqichlarga bo'lib yoziladi.", "Har bir bosqich uchun qaysi bloklar kerakligi belgilanadi."]), ("Yakunlash", 3, ["Reja asosida dasturlash tezroq va xatosizroq bo'lishi umumlashtiriladi."])],
    "amaliy": [("Reja tuzish", 10, ["O'quvchilar o'z vazifasi uchun qog'ozda bosqichma-bosqich reja tuzadilar."]), ("Dasturni boshlash", 15, ["O'quvchilar reja asosida dasturning birinchi bosqichlarini yoza boshlaydilar."])],
    "uyga": ["Rejangizni to'ldirib, keyingi darsga tayyor holda olib keling."],
},

"Vaqt boshqaruvi: ketma-ket vazifalar": {
    "maqsad": ["O'quvchilar bir nechta vazifani ketma-ket, vaqt bo'yicha rejalashtirib bajaradigan dastur tuzadilar.", "O'quvchilar \"kutish\" (timer) blokidan foydalanishni chuqurroq o'rganadilar.", "O'quvchilar dasturni sinab, vaqt oralig'ini sozlaydilar."],
    "lugat": ["Vaqt boshqaruvi (Time management) – dasturda vaqtni nazorat qilish", "Kutish bloki (Wait block) – ma'lum vaqt kutib turish buyrug'i", "Ketma-ket vazifalar (Sequential tasks) – bir-biridan keyin bajariladigan ishlar", "Sinov (Test) – dasturni tekshirish", "Dastur (Program) – bloklar to'plami"],
    "softSkill": "Vaqtni rejalashtirish — vazifalarni to'g'ri vaqt oralig'ida bajarish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli model"],
    "nazariya": [("Kirish", 7, ["Kundalik rejada vaqt bo'yicha ish rejalashtirish (masalan, kun tartibi) misol qilinadi."]), ("Kutish bloki", 10, ["\"Kutish\" bloki dasturga ma'lum vaqt to'xtab turishni buyurishi ko'rsatiladi.", "Bir nechta vazifa orasida kutish qo'shib, ketma-ket bajarish namoyish qilinadi."]), ("Yakunlash", 3, ["Vaqt boshqaruvining murakkab dasturlarda ahamiyati umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar 2-3 ta vazifani kutish bloklari bilan ketma-ket bajaradigan dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar vaqt oralig'ini o'zgartirib, natijani kuzatadilar."])],
    "uyga": ["Kun davomidagi o'z vazifalaringizni vaqt bo'yicha ketma-ket ro'yxat qiling (kun tartibi)."],
},

"Parallel harakatlar (motor+tovush bir vaqtda)": {
    "maqsad": ["O'quvchilar ikki harakatni (motor va tovush) bir vaqtning o'zida bajarishni o'rganadilar.", "O'quvchilar parallel ishlaydigan skriptlarni qanday yaratishni tushunadilar.", "O'quvchilar dasturni sinab, ikkala harakatning bir vaqtda bajarilishini tekshiradilar."],
    "lugat": ["Parallel harakat (Parallel action) – bir vaqtning o'zida bajariladigan ikki harakat", "Skript (Script) – bloklardan tuzilgan alohida dastur qismi", "Ketma-ket bajarish (Sequential execution) – birin-ketin bajarilish", "Sinxronlash (Synchronization) – ikki harakatni bir vaqtga moslashtirish", "Dastur (Program) – bloklar to'plami"],
    "softSkill": "Ko'p vazifali fikrlash — bir vaqtning o'zida bir nechta jarayonni tasavvur qilish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli va tovushli model"],
    "nazariya": [("Kirish", 7, ["Ketma-ket bajariladigan va bir vaqtda bajariladigan harakatlar orasidagi farq haqida savol-javob."]), ("Parallel skriptlar", 10, ["Ikki alohida skript (bittasi motor uchun, bittasi tovush uchun) bir vaqtda \"bosilganda ishga tush\" bilan boshlanishi ko'rsatiladi."]), ("Yakunlash", 3, ["Parallel harakatning robotni yanada jonli qilishi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar motor va tovush uchun ikki alohida skript yaratib, ularni bir vaqtda ishga tushiradilar."]), ("Sinov", 10, ["O'quvchilar ikkala harakatning chindan ham bir vaqtda bajarilishini tekshiradilar."])],
    "uyga": ["Yana qaysi ikki harakatni bir vaqtda bajarish qiziqarli bo'lishi haqida g'oya yozing."],
},

"Vaqt boshqaruvi (timer bilan)": {
    "maqsad": ["O'quvchilar timer (taymer) blokidan foydalanib, vaqtga asoslangan dastur tuzadilar.", "O'quvchilar taymer yordamida robotning muayyan vaqt oralig'ida harakat qilishini boshqaradilar.", "O'quvchilar dasturni sinab, vaqt aniqligini tekshiradilar."],
    "lugat": ["Taymer (Timer) – vaqtni hisoblovchi dastur bloki", "Vaqt oralig'i (Time interval) – ikki hodisa orasidagi vaqt", "Kutish bloki (Wait block) – ma'lum vaqt kutish buyrug'i", "Sinov (Test) – dasturni tekshirish", "Dastur (Program) – bloklar to'plami"],
    "softSkill": "Aniqlik — vaqtni aniq hisoblab, dasturni shunga moslashtirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli model", "Xronometr (solishtirish uchun, ixtiyoriy)"],
    "nazariya": [("Kirish", 7, ["Soat-robot yoki taymerli qurilmalar haqida qisqa suhbat."]), ("Taymer bloki", 10, ["Taymer yordamida robot muayyan vaqtdan keyin harakatni boshlashi/to'xtatishi ko'rsatiladi."]), ("Yakunlash", 3, ["Taymerning real hayotda (soat, oshxona taymer) qo'llanilishi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar taymerdan foydalangan \"soat-robot\" dasturi tuzadilar."]), ("Sinov", 10, ["O'quvchilar dastur vaqtini xronometr bilan solishtirib tekshiradilar."])],
    "uyga": ["Taymerdan foydalanadigan yana bitta qurilmani (masalan, mikroto'lqinli pech) toping va tasvirlang."],
},

"Tugmalar orqali boshqaruv menyusi": {
    "maqsad": ["O'quvchilar controller/ilova tugmalari orqali boshqariladigan oddiy menyu dasturini tuzadilar.", "O'quvchilar har bir tugmaga alohida vazifa (funksiya) biriktiradilar.", "O'quvchilar dasturni sinab, barcha tugmalar to'g'ri ishlashini tekshiradilar."],
    "lugat": ["Menyu (Menu) – foydalanuvchi tanlov qiladigan tugmalar to'plami", "Tugma bosilganda (When button pressed) – tugma hodisasi bloki", "Funksiya (Function) – har bir tugmaga biriktirilgan vazifa", "Boshqaruv (Control) – robotni foydalanuvchi buyrug'i bilan yuritish", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Foydalanuvchi tajribasini o'ylash — dasturni boshqalar uchun tushunarli va qulay qilib tuzish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli model"],
    "nazariya": [("Kirish", 7, ["Pult yoki telefon menyusi qanday ishlashi haqida suhbat."]), ("Tugma hodisalari", 10, ["Har bir tugma bosilganda alohida skript ishga tushishi ko'rsatiladi.", "Har bir tugmaga alohida funksiya (masalan, oldinga/orqaga/to'xta) biriktiriladi."]), ("Yakunlash", 3, ["Menyu asosidagi boshqaruvning qulayligi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar kamida 3 ta tugma uchun alohida vazifali dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar barcha tugmalarni sinab, to'g'ri ishlashini tekshiradilar."])],
    "uyga": ["O'z boshqaruv menyungizga yana qanday tugma/vazifa qo'shish mumkinligi haqida yozing."],
},

"Xato dasturni topib tuzatish (debugging)": {
    "maqsad": ["O'quvchilar debugging (xatoni topish va tuzatish) tushunchasi bilan tanishadilar.", "O'quvchilar berilgan noto'g'ri dasturdagi xatoni mustaqil topadilar.", "O'quvchilar xatoni tuzatib, dasturni to'g'ri ishlashiga erishadilar."],
    "lugat": ["Debugging – dasturdagi xatoni topish va tuzatish jarayoni", "Xato (Bug) – dasturning noto'g'ri ishlashiga sabab bo'luvchi kamchilik", "Kutilgan natija (Expected result) – dastur qanday ishlashi kerakligi", "Haqiqiy natija (Actual result) – dastur amalda qanday ishlashi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Sabr-toqat va tizimli qidiruv — xatoni shoshilmasdan, bosqichma-bosqich qidirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi, oldindan xato joylashtirilgan dastur bilan)", "Motorli model"],
    "nazariya": [("Kirish", 7, ["Dastur nega kutilganidek ishlamasligi mumkinligi haqida savol-javob."]), ("Debugging usuli", 10, ["Dasturni bosqichma-bosqich (blokma-blok) kuzatib, qaysi joyda kutilmagan natija chiqishini topish usuli ko'rsatiladi."]), ("Yakunlash", 3, ["Debugging har bir dasturchining muhim ko'nikmasi ekanligi ta'kidlanadi."])],
    "amaliy": [("Xatoni topish", 15, ["O'quvchilarga oldindan xato joylashtirilgan dastur beriladi, ular xatoni topadilar."]), ("Tuzatish va sinov", 10, ["O'quvchilar xatoni tuzatib, dasturni qayta sinaydilar."])],
    "uyga": ["O'zingiz duch kelgan (dasturda yoki boshqa ishda) bitta xatoni va uni qanday tuzatganingizni yozing."],
},

"Debugging o'yini: kim tezroq topadi": {
    "maqsad": ["O'quvchilar debugging ko'nikmasini o'yin-musobaqa shaklida mustahkamlaydilar.", "O'quvchilar bir nechta xatoli dasturni tezkor tahlil qiladilar.", "O'quvchilarda tezkor va aniq tahlil qilish ko'nikmasi rivojlanadi."],
    "lugat": ["Debugging – xatoni topish va tuzatish jarayoni", "Musobaqa (Competition) – kim tezroq va to'g'ri bajarishini aniqlash", "Xato (Bug) – dasturdagi kamchilik", "Vaqt (Time) – topshiriqni bajarish uchun ketgan davr", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Sog'lom raqobat — o'yin-musobaqa jarayonida boshqalarga hurmat bilan munosabatda bo'lish ko'nikmasini mustahkamlash.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi, bir nechta xatoli dastur bilan)", "Xronometr"],
    "nazariya": [("Kirish", 7, ["O'yin qoidalari tushuntiriladi: har bir o'quvchi/juftlik xatoli dasturni tezroq tuzatishga harakat qiladi."]), ("Strategiya", 10, ["Xatoni tezroq topish uchun qaysi qismlarni birinchi tekshirish kerakligi muhokama qilinadi."]), ("Yakunlash", 3, ["O'yin natijalari umumlashtiriladi."])],
    "amaliy": [("O'yin", 20, ["O'quvchilar/juftliklar navbat bilan (yoki bir vaqtda) xatoli dasturni tuzatishga harakat qiladilar.", "O'qituvchi vaqtni o'lchaydi va g'oliblarni aniqlaydi."]), ("Muhokama", 5, ["Eng tez topilgan xatolar qanday topilgani muhokama qilinadi."])],
    "uyga": ["Debugging bo'yicha o'zingizning \"maslahatingiz\"ni (masalan, avval nimani tekshirish kerak) yozing."],
},

"Murakkab mashina dasturi": {
    "maqsad": ["O'quvchilar bir nechta funksiya, shart va sikldan tashkil topgan murakkab mashina dasturini tuzadilar.", "O'quvchilar dasturni bosqichma-bosqich rejalashtirib, keyin amalga oshiradilar.", "O'quvchilar dasturni to'liq sinovdan o'tkazadilar."],
    "lugat": ["Murakkab dastur (Complex program) – bir nechta tushunchani birlashtirgan dastur", "Funksiya (Function) – qayta ishlatiladigan bloklar to'plami", "Shart (Condition) – \"agar\" mantig'i", "Sikl (Loop) – takrorlanish", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Murakkablikni boshqarish — ko'p qismli vazifani tartibli va bosqichma-bosqich yechish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Mashina modeli"],
    "nazariya": [("Kirish", 7, ["Yil davomida o'rganilgan tushunchalar (funksiya, shart, sikl) qisqacha eslanadi."]), ("Murakkab dastur rejasi", 10, ["Mashina dasturi qanday qismlardan (harakat, to'xtash, sensor reaksiyasi) tashkil topishi rejalashtiriladi."]), ("Yakunlash", 3, ["Murakkab dasturni kichik qismlarga bo'lib yozish tavsiya etiladi."])],
    "amaliy": [("Dastur yozish", 20, ["O'quvchilar rejaga asosan mashina dasturini bosqichma-bosqich yozadilar."]), ("Sinov", 5, ["O'quvchilar dasturni ishga tushirib, xatolarni aniqlaydilar."])],
    "uyga": ["Mashina dasturingizga yana qanday funksiya qo'shish mumkinligi haqida yozing."],
},

"Mashinani masofadan (ilova) boshqarish": {
    "maqsad": ["O'quvchilar mashinani ilova orqali masofadan real vaqtda boshqarishni o'rganadilar.", "O'quvchilar boshqaruv va avtomatik dastur orasidagi farqni tushunadilar.", "O'quvchilar masofadan boshqarishni sinab ko'radilar."],
    "lugat": ["Masofadan boshqarish (Remote control) – robotni real vaqtda ilova orqali boshqarish", "Real vaqt (Real-time) – kechikishsiz, darhol ishlash", "Boshqaruv paneli (Control panel) – ilovadagi boshqaruv tugmalari", "Avtomatik dastur (Automatic program) – oldindan yozilgan, o'z-o'zidan ishlaydigan dastur", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Reaktiv boshqaruv — real vaqtda qaror qabul qilib, robotni boshqarish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Mashina modeli", "Ochiq joy (sinov uchun)"],
    "nazariya": [("Kirish", 7, ["Avtomatik dastur va masofadan boshqarish orasidagi farq haqida savol-javob."]), ("Masofadan boshqarish tizimi", 10, ["Ilovadagi boshqaruv tugmalari mashina harakatiga qanday bog'lanishi ko'rsatiladi."]), ("Yakunlash", 3, ["Masofadan boshqarishning qachon foydali ekanligi (masalan, real vaqt reaksiyasi kerak bo'lganda) umumlashtiriladi."])],
    "amaliy": [("Sozlash", 10, ["O'quvchilar ilovada boshqaruv tugmalarini mashina harakatlariga bog'laydilar."]), ("Sinov", 15, ["O'quvchilar mashinani ilova orqali real vaqtda boshqarib, kichik trassada sinaydilar."])],
    "uyga": ["Masofadan boshqariladigan qurilmalar (o'yinchoq, dron) haqida bitta misol toping."],
},

"Dasturlash bo'yicha yakuniy mashq": {
    "maqsad": ["O'quvchilar chorak davomida o'rgangan barcha dasturlash tushunchalarini (shart, sikl, funksiya yoki VA/YOKI) mustahkamlaydilar.", "O'quvchilar mustaqil kichik dastur yaratib, uni sinaydilar.", "O'quvchilar o'z dasturini sinfga tushuntirib beradilar."],
    "lugat": ["Takrorlash (Review) – o'rganilgan mavzularni eslash", "Mustahkamlash (Reinforcement) – bilimni amaliyotda qayta qo'llash", "Dastur (Program) – bloklar to'plami", "Sinov (Test) – dasturni tekshirish", "Taqdimot (Presentation) – ishni tushuntirib berish"],
    "softSkill": "O'z-o'zini baholash — o'rgangan bilimlarini mustaqil qo'llab, o'z darajasini baholash ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["Chorak davomida o'rganilgan barcha mavzular ro'yxati birga eslanadi."]), ("Yakuniy mashq talablari", 10, ["O'quvchilar kamida 2 ta tushunchani (masalan, shart+sikl) o'z ichiga olgan dastur tuzishlari kerakligi tushuntiriladi."]), ("Yakunlash", 3, ["Nazorat ishiga tayyorgarlik sifatida bu mashqning ahamiyati ta'kidlanadi."])],
    "amaliy": [("Dastur yozish", 20, ["O'quvchilar mustaqil kichik dastur tuzadilar."]), ("Sinov va tushuntirish", 5, ["O'quvchilar dasturini ishga tushirib, qisqacha tushuntiradilar."])],
    "uyga": ["Nazorat ishiga tayyorgarlik ko'ring: bugungi dasturingizni yana bir bor ko'zdan kechiring."],
},

"Motor va controller: takrorlash": {
    "maqsad": ["O'quvchilar 1-yilda o'rgangan motor va controller bog'lanishini eslaydilar va mustahkamlaydilar.", "O'quvchilar controllerda oddiy motor dasturini qayta tuzadilar.", "O'quvchilar yangi chorak mavzulariga (shart, sikl) tayyorlanadilar."],
    "lugat": ["Controller (Controller) – robotning boshqaruv bloki", "Motor (Motor) – harakat beruvchi qurilma", "Ulash porti (Port) – motor/sensor ulanadigan uyacha", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Bilimni yangilash — avval o'rgangan bilimni qayta faollashtirib, yangi mavzuga tayyorlanish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli model"],
    "nazariya": [("Kirish", 7, ["1-yilda o'rgangan motor va controller haqidagi bilim eslanadi."]), ("Takrorlash", 10, ["Motorni ishga tushirish, to'xtatish va tezligini o'zgartirish bloklari qayta ko'rib chiqiladi."]), ("Yakunlash", 3, ["Bu chorakda motor dasturi ustiga shart va sikl qo'shilishi aytiladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar oddiy motor dasturini (yoqish-o'chirish) qayta tuzadilar."]), ("Sinov", 10, ["O'quvchilar dasturni sinab, motor tezligini o'zgartiradilar."])],
    "uyga": ["1-yilda motor bilan yasagan eng sevimli modelingizni eslab, nima uchun yoqqanini yozing."],
},

"Shart (agar...bo'lsa) tushunchasi": {
    "maqsad": ["O'quvchilar shart (agar...bo'lsa) blokining ishlash tamoyilini tushunadilar.", "O'quvchilar sensor signaliga qarab qaror qabul qiluvchi oddiy dastur tuzadilar.", "O'quvchilar shartli dasturni sinab, natijasini kuzatadilar."],
    "lugat": ["Shart (Condition/If) – \"agar...bo'lsa\" mantig'i", "Sensor signali (Sensor signal) – shart tekshirishda ishlatiladigan ma'lumot", "Qaror (Decision) – shart natijasiga qarab tanlangan harakat", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Shartli fikrlash — \"agar shunday bo'lsa, unda shunday qilaman\" mantig'ini kundalik hayotga bog'lab tushunish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Sensorli model"],
    "nazariya": [("Kirish", 7, ["Kundalik hayotdan shart misollari (\"agar yomg'ir yog'sa, soyabon olaman\") muhokama qilinadi."]), ("Shart bloki", 10, ["\"Agar...bo'lsa\" blokining tuzilishi va sensor bilan bog'lanishi ko'rsatiladi."]), ("Yakunlash", 3, ["Shartning robotni \"aqlli\" qilishdagi roli umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar sensor signaliga qarab harakat qiladigan oddiy shartli dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar sensorni turlicha sinab, dastur reaksiyasini kuzatadilar."])],
    "uyga": ["\"Agar...bo'lsa\" mantig'iga mos yana 2 ta kundalik misol yozing."],
},

"Shart bilan oddiy o'yin": {
    "maqsad": ["O'quvchilar shart blokidan foydalangan kichik o'yin dasturi tuzadilar.", "O'quvchilar o'yin qoidalarini shart orqali ifodalashni o'rganadilar.", "O'quvchilar o'z o'yinini sinfga namoyish etadilar."],
    "lugat": ["Shart (Condition) – \"agar\" mantig'i", "O'yin qoidasi (Game rule) – o'yinning qanday ishlashini belgilovchi shart", "Sensor (Sensor) – o'yinni boshqaruvchi kirish ma'lumoti", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Ijodkorlik — shart mantig'idan foydalanib, o'zi o'yin qoidasini o'ylab topish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Sensorli model"],
    "nazariya": [("Kirish", 7, ["O'tgan darsdagi shart bloki eslanadi."]), ("O'yin g'oyasi", 10, ["Shart asosida oddiy o'yin (masalan, \"agar sensor signal bersa, tovush chiqar\") taklif qilinadi."]), ("Yakunlash", 3, ["O'yin qoidalari qisqacha aniqlashtiriladi."])],
    "amaliy": [("O'yinni yaratish", 15, ["O'quvchilar shart blokidan foydalangan kichik o'yin dasturini tuzadilar."]), ("Sinov va namoyish", 10, ["O'quvchilar o'yinlarini sinab, sinfga ko'rsatadilar."])],
    "uyga": ["O'yiningizga yana qanday shart qo'shish mumkinligi haqida g'oya yozing."],
},

"Ikki shartni solishtirish": {
    "maqsad": ["O'quvchilar ikki xil shart natijasini bir dasturda solishtiradilar.", "O'quvchilar \"agar...aks holda\" (if-else) tuzilmasini o'rganadilar.", "O'quvchilar dasturni sinab, ikkala holatni ham tekshiradilar."],
    "lugat": ["Agar...aks holda (If...else) – shart to'g'ri bo'lmasa bajariladigan muqobil harakat", "Ikki holat (Two outcomes) – shartning ikki xil natijasi", "Sensor signali (Sensor signal) – shart tekshirishda ishlatiladigan ma'lumot", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Muqobil fikrlash — faqat bitta emas, balki ikki xil natijani ham hisobga olish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Sensorli model"],
    "nazariya": [("Kirish", 7, ["Faqat \"agar\" bilan cheklanib qolish noqulayligi haqida savol-javob (aks holda nima bo'ladi?)."]), ("Agar...aks holda", 10, ["\"Agar...aks holda\" bloki shart to'g'ri bo'lmaganda ham muqobil harakat bajarishini ko'rsatiladi."]), ("Yakunlash", 3, ["Bu tuzilmaning dasturni to'liqroq qilishi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar \"agar...aks holda\" tuzilmasidan foydalangan dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar ikkala holatni ham (shart to'g'ri va noto'g'ri) sinaydilar."])],
    "uyga": ["\"Agar...aks holda\" mantig'iga mos kundalik hayot misolini yozing."],
},

"Tovush/animatsiya bloklari": {
    "maqsad": ["O'quvchilar tovush va animatsiya (ekran) bloklaridan foydalanishni o'rganadilar.", "O'quvchilar dasturga tovush yoki vizual effekt qo'shadilar.", "O'quvchilar dasturni sinab, effektlarning to'g'ri ishlashini tekshiradilar."],
    "lugat": ["Tovush bloki (Sound block) – dasturga ovoz qo'shuvchi buyruq", "Animatsiya (Animation) – ekranda harakatlanuvchi tasvir", "Effekt (Effect) – dasturga qo'shimcha jonlilik beruvchi element", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Ijodiy ifoda — dasturga o'z uslubini (tovush, effekt) qo'shish orqali ijodkorlikni rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli/sensorli model"],
    "nazariya": [("Kirish", 7, ["O'yin yoki multfilmlardagi tovush effektlari haqida qisqa suhbat."]), ("Tovush va animatsiya bloklari", 10, ["Dasturga tovush qo'shish va (agar controllerda ekran bo'lsa) oddiy animatsiya ko'rsatish usullari tushuntiriladi."]), ("Yakunlash", 3, ["Bu bloklarning dasturni yanada qiziqarli qilishi umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar shart yoki harakatga tovush/animatsiya qo'shadilar."]), ("Sinov", 10, ["O'quvchilar dasturni ishga tushirib, effektlarni sinaydilar."])],
    "uyga": ["Dasturingizga yana qanday tovush yoki effekt qo'shish mumkinligi haqida g'oya yozing."],
},

"Bir nechta blokni guruhlash (funksiya boshlang'ichi)": {
    "maqsad": ["O'quvchilar bir nechta blokni mantiqiy guruhga birlashtirish g'oyasi bilan tanishadilar (funksiya tushunchasiga kirish).", "O'quvchilar guruhlangan bloklarning dasturni tushunarliroq qilishini his qiladilar.", "O'quvchilar keyingi chorakda funksiya mavzusiga tayyorlanadilar."],
    "lugat": ["Guruhlash (Grouping) – bir nechta blokni birlashtirib, bitta mantiqiy qism sifatida ko'rish", "Funksiya (Function) – qayta ishlatiladigan bloklar to'plami (kirish tushunchasi)", "Tushunarlilik (Readability) – dasturni tushunish qulayligi", "Dastur (Program) – bloklar ketma-ketligi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Tartibga solish — bir-biriga bog'liq bloklarni guruhlab, dasturni tartibli tutish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Motorli model"],
    "nazariya": [("Kirish", 7, ["Uzun dasturni tushunish qanchalik qiyin bo'lishi mumkinligi haqida savol-javob."]), ("Bloklarni guruhlash g'oyasi", 10, ["Bir-biriga bog'liq bloklarni (masalan, \"oldinga yur + tovush chiqar\") birga guruhlab ko'rish g'oyasi tushuntiriladi.", "Bu g'oya keyingi chorakda \"funksiya\" deb atalishi aytib o'tiladi."]), ("Yakunlash", 3, ["Guruhlashning dasturni tushunarli qilishi umumlashtiriladi."])],
    "amaliy": [("Dastur tahlili", 15, ["O'quvchilar o'z dasturidagi bloklarni mantiqiy guruhlarga (masalan, \"boshlash\", \"harakat\", \"to'xtash\") ajratadilar."]), ("Muhokama", 10, ["Guruhlangan dastur guruhlanmagan dastur bilan solishtiriladi."])],
    "uyga": ["O'z dasturingizni qanday guruhlarga bo'lish mumkinligi haqida qisqacha reja yozing."],
},

"O'z loyiham uchun dastur rejasi": {
    "maqsad": ["O'quvchilar chorak yakunidagi shaxsiy loyihasi uchun dastur rejasini tuzadilar.", "O'quvchilar rejada qaysi bloklar (shart, sikl) kerakligini belgilaydilar.", "O'quvchilar rejani keyingi darsda amalga oshirishga tayyorlanadilar."],
    "lugat": ["Loyiha rejasi (Project plan) – loyihani amalga oshirishdan oldingi qadamlar ro'yxati", "Talab (Requirement) – loyihadan kutilayotgan natija", "Bosqich (Step) – rejaning bitta qismi", "Dastur (Program) – bloklar to'plami", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Mustaqil rejalashtirish — o'z loyihasini boshidan oxirigacha mustaqil rejalashtirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Qog'oz va qalam (reja uchun)", "Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["Chorak yakunidagi loyiha talablari eslatiladi."]), ("Reja tuzish", 10, ["O'quvchilar loyihasi uchun qanday shart, sikl yoki funksiyalar kerakligini aniqlaydilar."]), ("Yakunlash", 3, ["Reja asosida ishlash keyingi darslarni osonlashtirishi ta'kidlanadi."])],
    "amaliy": [("Reja yozish", 20, ["O'quvchilar o'z loyihasi uchun batafsil dastur rejasini qog'ozga yozadilar."]), ("Muhokama", 5, ["O'qituvchi bilan rejalar qisqacha ko'rib chiqiladi."])],
    "uyga": ["Rejangizni to'ldirib, keyingi darsga tayyor holda olib keling."],
},

"Dasturni yozish": {
    "maqsad": ["O'quvchilar o'z loyihasi uchun tuzgan rejasi asosida dasturni yoza boshlaydilar.", "O'quvchilar rejadagi har bir bosqichni ketma-ket kod bilan amalga oshiradilar.", "O'quvchilar dasturni qisman sinab, to'g'ri yo'nalishda ekanini tekshiradilar."],
    "lugat": ["Dastur yozish (Coding) – rejani bloklar orqali amalga oshirish", "Bosqich (Step) – rejaning bitta qismi", "Blok (Block) – dastur buyrug'i", "Qisman sinov (Partial test) – dasturning tayyor bo'lgan qismini tekshirish", "Loyiha (Project) – yakuniy ish"],
    "softSkill": "Bosqichma-bosqich ijro — rejani ketma-ket, shoshilmasdan amalga oshirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "O'quvchining o'z dastur rejasi", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["O'tgan darsda tuzilgan reja eslanadi."]), ("Rejadan kodga", 10, ["Reja bosqichlarini bittalab bloklarga aylantirish tartibi ko'rsatiladi."]), ("Yakunlash", 3, ["Har bir bosqichni yozgandan keyin sinab ko'rish tavsiya etiladi."])],
    "amaliy": [("Dastur yozish", 22, ["O'quvchilar rejasi asosida dasturni bosqichma-bosqich yozadilar."]), ("Qisman sinov", 3, ["O'quvchilar tayyor bo'lgan qismni ishga tushirib ko'radilar."])],
    "uyga": ["Dasturingizning qaysi qismi eng qiyin bo'lganini va nega ekanini yozing."],
},

"Sinov va tuzatish": {
    "maqsad": ["O'quvchilar yozgan dasturini to'liq sinovdan o'tkazadilar.", "O'quvchilar aniqlangan xatolarni mustaqil tuzatadilar.", "O'quvchilar dasturni yakuniy holatga keltiradilar."],
    "lugat": ["Sinov (Test) – dasturni ishga tushirib tekshirish", "Xato (Bug) – dasturning noto'g'ri ishlashiga sabab bo'luvchi kamchilik", "Tuzatish (Fix) – xatoni bartaraf etish", "Yakuniy holat (Final state) – dasturning tayyor va ishlaydigan ko'rinishi", "Loyiha (Project) – yakuniy ish"],
    "softSkill": "Sabr-toqat va qat'iyat — dastur birinchi urinishda ishlamasa ham, uni tuzatishga qat'iyat bilan davom etish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "O'quvchining loyihasi"],
    "nazariya": [("Kirish", 7, ["Dasturlashda sinov va tuzatish tabiiy jarayon ekanligi ta'kidlanadi."]), ("Tizimli sinov", 10, ["Dasturning har bir qismini alohida sinash, keyin butunini birga sinash tavsiya etiladi."]), ("Yakunlash", 3, ["Xato topilganda uni yozib borish (kuzatuv jurnali) foydali ekanligi aytiladi."])],
    "amaliy": [("Sinov", 12, ["O'quvchilar dasturni to'liq ishga tushirib, barcha qismlarini tekshiradilar."]), ("Tuzatish", 13, ["O'quvchilar aniqlangan xatolarni tuzatadilar va qayta sinaydilar."])],
    "uyga": ["Loyihangizda topilgan va tuzatilgan bitta xatoni tasvirlab yozing."],
},

"Murakkab loyiha rejasi": {
    "maqsad": ["O'quvchilar chorak yakunidagi murakkabroq loyihasi uchun batafsil reja tuzadilar.", "O'quvchilar rejada bir nechta dasturlash tushunchasini (funksiya, VA/YOKI, ichma-ich sikl) birlashtiradilar.", "O'quvchilar rejani amalga oshirishga tayyorlanadilar."],
    "lugat": ["Murakkab loyiha (Complex project) – bir nechta tushunchani birlashtirgan loyiha", "Talab (Requirement) – loyihadan kutilayotgan natija", "Arxitektura (Architecture) – dasturning umumiy tuzilishi", "Bosqich (Step) – rejaning bitta qismi", "Loyiha (Project) – yakuniy ish"],
    "softSkill": "Murakkab rejalashtirish — bir nechta tushunchani birlashtirgan katta ishni tizimli rejalashtirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Qog'oz va qalam (reja uchun)", "Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan eng murakkab model"],
    "nazariya": [("Kirish", 7, ["Chorak yakunidagi murakkab loyiha talablari eslatiladi."]), ("Dastur arxitekturasi", 10, ["Loyiha qanday funksiyalar va shartlardan tashkil topishi rejalashtiriladi."]), ("Yakunlash", 3, ["Yaxshi reja murakkab loyihani ancha osonlashtirishi ta'kidlanadi."])],
    "amaliy": [("Reja yozish", 20, ["O'quvchilar murakkab loyihasi uchun batafsil reja va dastur arxitekturasini yozadilar."]), ("Muhokama", 5, ["O'qituvchi bilan rejalar qisqacha ko'rib chiqiladi."])],
    "uyga": ["Rejangizni to'ldirib, keyingi darsga tayyor holda olib keling."],
},

"Sinov, tuzatish, yakunlash": {
    "maqsad": ["O'quvchilar yakuniy loyihasini to'liq sinovdan o'tkazib, barcha xatolarni tuzatadilar.", "O'quvchilar dasturni yakuniy, tayyor holatga keltiradilar.", "O'quvchilar loyihasini taqdimotga tayyorlaydilar."],
    "lugat": ["Yakunlash (Finalize) – loyihani tugallangan holatga keltirish", "Sinov (Test) – dasturni tekshirish", "Tuzatish (Fix) – xatoni bartaraf etish", "Taqdimotga tayyorgarlik (Presentation prep) – loyihani ko'rsatishga tayyorlash", "Loyiha (Project) – yakuniy ish"],
    "softSkill": "Yakuniy sifat nazorati — ishni topshirishdan oldin uni oxirigacha tekshirib chiqish odatini shakllantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "O'quvchining loyihasi"],
    "nazariya": [("Kirish", 7, ["Loyihaning qanday holatda ekanligi haqida qisqacha muhokama."]), ("Yakuniy tekshiruv", 10, ["Dasturning barcha qismlari (shart, sikl, funksiya) qayta tekshiriladi."]), ("Yakunlash", 3, ["Taqdimotda nimalarni aytish kerakligi qisqacha aytib o'tiladi."])],
    "amaliy": [("Yakuniy sinov va tuzatish", 20, ["O'quvchilar dasturni oxirgi marta to'liq sinab, barcha xatolarni tuzatadilar."]), ("Taqdimotga tayyorgarlik", 5, ["O'quvchilar loyihasini qanday tushuntirishlari haqida qisqacha eslatma tayyorlaydilar."])],
    "uyga": ["Loyihangizni ota-onangizga ko'rsatib, ularning fikrini so'rang va yozib keling."],
},

"Holat (state) tushunchasi — sodda": {
    "maqsad": ["O'quvchilar holat mashinasi (state machine) tushunchasi bilan sodda darajada tanishadilar.", "O'quvchilar robotning turli holatlarda turli xil harakat qilishini tushunadilar.", "O'quvchilar oddiy holatlar orasida almashinuvchi dastur tuzadilar."],
    "lugat": ["Holat (State) – robotning joriy vaziyati", "Holat mashinasi (State machine) – holatlar orasida almashinuvchi tizim", "O'tish (Transition) – bir holatdan ikkinchisiga o'tish", "Hodisa (Event) – holat o'zgarishiga sabab bo'luvchi voqea", "Dastur (Program) – bloklar to'plami"],
    "softSkill": "Abstrakt tizimli fikrlash — real dunyoni \"holatlar\" ko'rinishida tasavvur qilish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Sensorli model", "Svetofor rasmi (misol uchun)"],
    "nazariya": [("Kirish", 7, ["Svetofor holatlari (qizil, sariq, yashil) misolida holat tushunchasi kiritiladi."]), ("Holat mashinasi", 10, ["Robot bir vaqtning o'zida faqat bitta holatda bo'lishi (masalan: to'xtagan -> yuruvchi -> to'siq oldida) va hodisaga qarab boshqa holatga o'tishi tushuntiriladi."]), ("Yakunlash", 3, ["Holat mashinasining robotni tushunarli qilishdagi foydasi umumlashtiriladi."])],
    "amaliy": [("Holatlarni belgilash", 10, ["O'quvchilar o'z robotining qanday holatlari bo'lishi mumkinligini (masalan, to'xtagan/yuruvchi) ro'yxat qiladilar."]), ("Dastur yozish", 15, ["O'quvchilar oddiy 2 holatli dastur (masalan, to'xtagan<->yuruvchi) tuzadilar."])],
    "uyga": ["Kundalik hayotda \"holatlar\"ga ega bo'lgan yana bitta narsani (masalan, telefon: qulflangan/ochiq) yozing."],
},

"Holatlar bilan o'yin": {
    "maqsad": ["O'quvchilar holat mashinasi tushunchasini o'yin shaklida mustahkamlaydilar.", "O'quvchilar bir nechta holat orasida almashinuvchi kichik o'yin tuzadilar.", "O'quvchilar o'yinni sinfga namoyish etadilar."],
    "lugat": ["Holat (State) – robotning joriy vaziyati", "O'tish shartlari (Transition conditions) – holat o'zgarishi uchun kerakli shartlar", "O'yin (Game) – holatlarga asoslangan interaktiv dastur", "Dastur (Program) – bloklar to'plami", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Ijodiy dizayn — holatlar asosida qiziqarli o'yin qoidalarini o'ylab topish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Sensorli model"],
    "nazariya": [("Kirish", 7, ["O'tgan darsdagi holat mashinasi eslanadi."]), ("O'yin g'oyasi", 10, ["3 holatli (masalan: kutish -> harakat -> g'alaba) o'yin g'oyasi taklif qilinadi."]), ("Yakunlash", 3, ["O'yin qoidalari qisqacha aniqlashtiriladi."])],
    "amaliy": [("O'yinni yaratish", 15, ["O'quvchilar holatlar asosidagi kichik o'yin dasturini tuzadilar."]), ("Sinov va namoyish", 10, ["O'quvchilar o'yinlarini sinab, sinfga ko'rsatadilar."])],
    "uyga": ["O'yiningizga yana qanday holat qo'shish mumkinligi haqida g'oya yozing."],
},

"Xato-bardosh dastur (agar sensor ishlamasa?)": {
    "maqsad": ["O'quvchilar xato-bardosh (fault-tolerant) dastur tushunchasi bilan tanishadilar.", "O'quvchilar sensor kutilmagan natija bersa nima qilish kerakligini rejalashtiradilar.", "O'quvchilar zaxira stsenariyli dastur tuzadilar."],
    "lugat": ["Xato-bardoshlik (Fault tolerance) – kutilmagan holatlarda ham ishlashda davom etish qobiliyati", "Zaxira stsenariy (Fallback scenario) – asosiy reja ishlamasa qo'llaniladigan muqobil reja", "Kutilmagan holat (Unexpected situation) – dastur oldindan hisobga olmagan vaziyat", "Sensor (Sensor) – atrof-muhitni sezuvchi qurilma", "Dastur (Program) – bloklar to'plami"],
    "softSkill": "Ehtiyotkor rejalashtirish — faqat \"hamma narsa yaxshi ishlaydi\" deb emas, muammo yuzaga kelishi mumkinligini ham hisobga olib rejalashtirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Sensorli model"],
    "nazariya": [("Kirish", 7, ["Sensor to'g'ri ishlamasa nima bo'lishi mumkinligi haqida savol-javob (masalan, xato signal)."]), ("Zaxira stsenariy", 10, ["Agar sensor kutilmagan natija bersa, robot avtomatik to'xtashi yoki xavfsiz harakat qilishi kabi yechimlar tushuntiriladi."]), ("Yakunlash", 3, ["Xato-bardoshlikning real robototexnikada (masalan, avtonom mashinalar) ahamiyati umumlashtiriladi."])],
    "amaliy": [("Dastur yozish", 15, ["O'quvchilar sensor kutilmagan qiymat bersa ishlaydigan zaxira stsenariyni dasturga qo'shadilar."]), ("Sinov", 10, ["O'quvchilar turli (shu jumladan g'ayrioddiy) sharoitlarda dasturni sinaydilar."])],
    "uyga": ["Kundalik hayotda \"zaxira reja\"ga ega bo'lgan bitta vaziyatni (masalan, elektr o'chsa quvvat generatori) yozing."],
},

"Debugging: xatoni topish mashqi": {
    "maqsad": ["O'quvchilar debugging (xatoni topish va tuzatish) tushunchasi bilan tanishadilar.", "O'quvchilar berilgan noto'g'ri dasturdagi xatoni mustaqil topib tuzatadilar.", "O'quvchilarda sabr-toqat va tizimli qidiruv ko'nikmasi rivojlanadi."],
    "lugat": ["Debugging – dasturdagi xatoni topish va tuzatish jarayoni", "Xato (Bug) – dasturning noto'g'ri ishlashiga sabab bo'luvchi kamchilik", "Kutilgan natija (Expected result) – dastur qanday ishlashi kerakligi", "Haqiqiy natija (Actual result) – dastur amalda qanday ishlashi", "Sinov (Test) – dasturni tekshirish"],
    "softSkill": "Sabr-toqat va tizimli qidiruv — xatoni shoshilmasdan, bosqichma-bosqich qidirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi, oldindan xato joylashtirilgan dastur bilan)", "1-yilda yasalgan model"],
    "nazariya": [("Kirish", 7, ["Dastur nega kutilganidek ishlamasligi mumkinligi haqida savol-javob."]), ("Xatoni qidirish usuli", 10, ["Dasturni blokma-blok kuzatib, qaysi joyda kutilmagan natija chiqishini topish usuli ko'rsatiladi.", "Kutilgan va haqiqiy natijani solishtirish tavsiya etiladi."]), ("Yakunlash", 3, ["Debugging har bir dasturchining muhim ko'nikmasi ekanligi ta'kidlanadi."])],
    "amaliy": [("Xatoni topish", 15, ["O'quvchilarga oldindan xato joylashtirilgan dastur beriladi, ular xatoni mustaqil topadilar."]), ("Tuzatish va sinov", 10, ["O'quvchilar xatoni tuzatib, dasturni qayta sinaydilar."])],
    "uyga": ["O'zingiz duch kelgan bitta xatoni va uni qanday tuzatganingizni yozing."],
},

"Scratch-uslub muhitni chuqur takrorlash": {
    "maqsad": ["O'quvchilar o'tgan yillarda o'rgangan Scratch-uslub bloklarini chuqur takrorlaydilar.", "O'quvchilar shart, sikl va o'zgaruvchi bloklarini birgalikda ishlatishni mustahkamlaydilar.", "O'quvchilar bu chorakdagi murakkabroq mavzularga tayyorlanadilar."],
    "lugat": ["Takrorlash (Review) – avval o'rgangan mavzularni eslash", "Shart (Condition) – \"agar\" mantig'i", "Sikl (Loop) – takrorlanuvchi bloklar guruhi", "O'zgaruvchi (Variable) – qiymati o'zgaruvchi xotira katakchasi", "Dastur (Program) – bloklar ketma-ketligi"],
    "softSkill": "Bilimni tizimlashtirish — oldingi yillarda o'rgangan bilimlarni tartibli ravishda eslab, yangi bosqichga tayyorlanish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "1-yilda yasalgan model", "Taqdimot uchun kompyuter va proyektor"],
    "nazariya": [("Kirish", 7, ["O'tgan yilda o'rganilgan asosiy tushunchalar (shart, sikl, o'zgaruvchi) birga eslanadi."]), ("Chuqur takrorlash", 10, ["Har bir tushuncha qisqacha misol bilan qayta ko'rib chiqiladi.", "Ularni birgalikda ishlatish namunasi ko'rsatiladi."]), ("Yakunlash", 3, ["Bu chorakda o'rganiladigan yangi mavzular (VA/YOKI, ichma-ich sikl) qisqacha aytiladi."])],
    "amaliy": [("Takrorlash mashqi", 15, ["O'quvchilar shart, sikl va o'zgaruvchini birga ishlatgan kichik dastur tuzadilar."]), ("Sinov", 10, ["O'quvchilar dasturni ishga tushirib, natijasini tekshiradilar."])],
    "uyga": ["O'tgan yilda dasturlashda eng qiyin bo'lgan mavzuni eslab, uni yana bir bor ko'rib chiqing."],
},

"Debugging usullari": {
    "maqsad": ["O'quvchilar debugging (xato topish)ning bir nechta tizimli usuli bilan tanishadilar.", "O'quvchilar dasturni bo'laklarga bo'lib alohida sinash usulini o'rganadilar.", "O'quvchilar bu usullarni o'z dasturida qo'llaydilar."],
    "lugat": ["Debugging usuli (Debugging technique) – xatoni topishning tizimli yo'li", "Bo'lakma-bo'lak sinov (Incremental testing) – dasturni kichik qismlarga bo'lib sinash", "Kuzatuv jurnali (Log) – dastur ishlashi haqida yozib boriladigan ma'lumot", "Xato (Bug) – dasturdagi kamchilik", "Dastur (Program) – bloklar to'plami"],
    "softSkill": "Tizimli muammo yechish — xatoni tasodifiy emas, tizimli usul bilan qidirish ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "Murakkab (ko'p bosqichli) model dasturi"],
    "nazariya": [("Kirish", 7, ["Murakkab dasturda xatoni topish nega qiyinroq bo'lishi haqida savol-javob."]), ("Tizimli usullar", 10, ["Dasturni kichik qismlarga bo'lib, har birini alohida sinash usuli ko'rsatiladi.", "Kuzatuv uchun oddiy \"belgilar\" (masalan, tovush chiqarish) qo'yish taklif qilinadi."]), ("Yakunlash", 3, ["Bu usullarning murakkab loyihalarda vaqt tejashi umumlashtiriladi."])],
    "amaliy": [("Usulni qo'llash", 15, ["O'quvchilar o'z murakkab dasturini kichik qismlarga bo'lib, alohida-alohida sinaydilar."]), ("Xatolarni tuzatish", 10, ["Topilgan xatolar tuzatiladi."])],
    "uyga": ["Bugun o'rgangan debugging usulingizni boshqa bir vazifada (masalan, uy vazifasini tekshirishda) qanday qo'llash mumkinligi haqida yozing."],
},

"Dasturni optimallashtirish": {
    "maqsad": ["O'quvchilar dasturni qisqartirish va soddalashtirish (optimallashtirish) tushunchasi bilan tanishadilar.", "O'quvchilar takrorlanuvchi bloklarni funksiya yoki sikl bilan almashtiradilar.", "O'quvchilar optimallashtirilgan dasturni sinab, natijasi o'zgarmasligini tekshiradilar."],
    "lugat": ["Optimallashtirish (Optimization) – dasturni qisqaroq va samaraliroq qilish", "Takrorlanuvchi kod (Repetitive code) – bir xil bloklarning bir necha marta yozilishi", "Soddalashtirish (Simplification) – dasturni tushunarliroq qilish", "Funksiya (Function) – qayta ishlatiladigan bloklar to'plami", "Dastur (Program) – bloklar to'plami"],
    "softSkill": "Sifatga intilish — ishlaydigan dasturni yanada yaxshilashga intilish (\"ishladi\" bilan cheklanmaslik) ko'nikmasini rivojlantirish.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "O'quvchining oldingi dasturi (uzun, takrorlanuvchi)"],
    "nazariya": [("Kirish", 7, ["Uzun va takrorlanuvchi dastur namunasi ko'rsatiladi."]), ("Optimallashtirish usullari", 10, ["Takrorlanuvchi bloklarni sikl yoki funksiya bilan almashtirish ko'rsatiladi."]), ("Yakunlash", 3, ["Qisqa dastur tushunish va tuzatishni osonlashtirishi ta'kidlanadi."])],
    "amaliy": [("Dasturni tahlil qilish", 10, ["O'quvchilar o'z dasturidagi takrorlanuvchi qismlarni topadilar."]), ("Optimallashtirish", 15, ["O'quvchilar dasturni sikl/funksiya bilan qisqartiradilar va natija o'zgarmasligini sinaydilar."])],
    "uyga": ["Kundalik hayotda \"takrorlanuvchi ishni qisqartirish\"ga misol toping (masalan, ro'yxat tuzish)."],
},

"Yakuniy loyiha rejasi": {
    "maqsad": ["O'quvchilar SPIKE bosqichiga tayyorgarlik sifatida yakuniy loyihasi uchun to'liq reja tuzadilar.", "O'quvchilar rejada barcha o'rgangan tushunchalarni (holat, debugging, optimallashtirish) hisobga oladilar.", "O'quvchilar rejani amalga oshirishga tayyorlanadilar."],
    "lugat": ["Yakuniy loyiha (Final project) – yil yakunidagi eng murakkab ish", "Reja (Plan) – ishni bajarishdan oldingi qadamlar", "Talab (Requirement) – loyihadan kutilayotgan natija", "Arxitektura (Architecture) – dasturning umumiy tuzilishi", "Loyiha (Project) – yakuniy ish"],
    "softSkill": "Yakuniy mustaqil rejalashtirish — ikki yillik bilim asosida eng murakkab ishni mustaqil rejalashtirish ko'nikmasini mustahkamlash.",
    "resurslar": ["Qog'oz va qalam (reja uchun)", "Planshet/telefon (Makerzoid ilovasi)", "1-yildagi eng murakkab model"],
    "nazariya": [("Kirish", 7, ["Yakuniy loyiha talablari (to'liq avtonom, \"aqlli\" model) eslatiladi."]), ("Reja tuzish", 10, ["O'quvchilar qanday holatlar, shartlar va funksiyalar kerakligini rejalashtiradilar."]), ("Yakunlash", 3, ["Yaxshi reja yakuniy loyihani ancha osonlashtirishi ta'kidlanadi."])],
    "amaliy": [("Reja yozish", 20, ["O'quvchilar yakuniy loyihasi uchun batafsil reja tuzadilar."]), ("Muhokama", 5, ["O'qituvchi bilan rejalar qisqacha ko'rib chiqiladi."])],
    "uyga": ["Rejangizni to'ldirib, keyingi darsga tayyor holda olib keling."],
},

"Sinov, tuzatish, taqdimot": {
    "maqsad": ["O'quvchilar yakuniy loyihasini to'liq sinovdan o'tkazib, barcha xatolarni tuzatadilar.", "O'quvchilar loyihasini sinfga taqdim etadilar.", "O'quvchilar ikki yillik dasturlash yo'lini yakunlaydilar va SPIKE'ga tayyor bo'ladilar."],
    "lugat": ["Yakuniy sinov (Final test) – loyihani to'liq tekshirish", "Tuzatish (Fix) – xatoni bartaraf etish", "Taqdimot (Presentation) – loyihani ko'rsatib tushuntirish", "SPIKE Prime – keyingi bosqich platformasi", "Loyiha (Project) – yakuniy ish"],
    "softSkill": "Ishonch bilan taqdim etish — ikki yillik mehnat natijasini sinfga ishonch bilan ko'rsatish ko'nikmasini mustahkamlash.",
    "resurslar": ["Planshet/telefon (Makerzoid ilovasi)", "O'quvchining yakuniy loyihasi"],
    "nazariya": [("Kirish", 7, ["Loyihaning qanday holatda ekanligi haqida qisqacha muhokama."]), ("Yakuniy tekshiruv", 10, ["Dasturning barcha qismlari (holat, shart, funksiya) oxirgi marta tekshiriladi."]), ("Yakunlash", 3, ["Taqdimot tartibi va SPIKE bosqichiga o'tish qisqacha aytib o'tiladi."])],
    "amaliy": [("Yakuniy sinov va tuzatish", 15, ["O'quvchilar dasturni oxirgi marta to'liq sinab, xatolarni tuzatadilar."]), ("Taqdimot", 10, ["Har bir o'quvchi yakuniy loyihasini sinfga namoyish qiladi va tushuntiradi."])],
    "uyga": ["Ikki yillik dasturlash yo'lida eng ko'p nimani o'rganganingiz haqida qisqacha insho yozing."],
},

}
