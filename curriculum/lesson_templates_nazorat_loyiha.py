# -*- coding: utf-8 -*-
"""
Nazorat (musobaqa/amaliy sinov) va Loyiha (erkin ijod) turidagi darslar uchun to'liq kontent.
Har biri keyword orqali moslashtiriladi (match_nazorat / match_loyiha), chunki bitta matn
bir nechta sinf/yil pozitsiyasida takrorlanadi (masalan RoboRace barcha 1-yil sinflarida bor).
"""

NAZORAT_CONTENT = {

"roborace": {
    "maqsad": [
        "O'quvchilar chorak davomida o'rgangan qurish ko'nikmalarini \"RoboRace\" musobaqasida amaliy tarzda namoyish etadilar.",
        "O'quvchilar vaqt bo'yicha ishlash va aniq mezon asosida baholanish tushunchasi bilan tanishadilar.",
        "O'quvchilarda sog'lom raqobat va sportchan munosabat ko'nikmasi rivojlanadi.",
    ],
    "lugat": [
        "Musobaqa (Competition) – g'olibni aniqlash uchun o'tkaziladigan raqobat",
        "Xronometr (Stopwatch) – vaqtni aniq o'lchash uchun asbob",
        "Masofa (Distance) – ikki nuqta orasidagi uzunlik",
        "Baholash mezoni (Grading criteria) – natijani baholash uchun belgilangan qoidalar",
        "Finish (Finish line) – musobaqa tugash chizig'i",
    ],
    "softSkill": "Sportchan munosabat (Sportsmanship) — g'alaba va mag'lubiyatga sog'lom munosabatda bo'lish, boshqa o'quvchilarning natijalarini olqishlash va hurmat qilishni o'rgatish. Yutqazish ham o'rganish jarayonining bir qismi ekanligini tushuntiring.",
    "resurslar": [
        "Chorak davomida o'quvchilar yasagan robotlar",
        "2 metrlik to'g'ri trassa (bo'r yoki lenta bilan chizilgan, old va finish chizig'i bilan)",
        "Xronometr (telefon sekundomeri ham bo'ladi)",
        "Natijalarni yozish uchun jadval (doskada yoki qog'ozda)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Musobaqa qoidalari tushuntiriladi: har bir robot 2 metr masofani bosib o'tishi kerak.", "Navbat tartibi belgilanadi."]),
        ("Baholash mezoni", 10, ["10 soniyagacha = 5 (a'lo); 11-25 soniya = 4 (yaxshi); 26-45 soniya = 3 (qoniqarli); 46-60 soniya = 2 (qoniqarsiz).", "1 daqiqadan ortiq yoki finishga yetib bormasa = FAILED.", "Xavfsizlik va navbat tartibiga rioya qilish talab etiladi."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 5, ["O'quvchilar o'z robotlarini so'nggi marta tekshiradilar, batareyani almashtiradilar (kerak bo'lsa)."]),
        ("Musobaqa", 25, ["Har bir o'quvchi/juftlik navbat bilan chiqib, o'z robotini 2 metrlik trassada sinaydi.", "O'qituvchi xronometr bilan vaqtni o'lchaydi va jadvalga yozadi.", "Har bir natija darhol baholash mezoniga ko'ra baholanadi va e'lon qilinadi."]),
    ],
    "uyga": [
        "Robotni tezroq qilish uchun qanday o'zgartirish kiritish mumkinligi haqida o'ylab, g'oyangizni daftaringizga yozib keling.",
    ],
},

"robolift": {
    "maqsad": [
        "O'quvchilar chorak davomida o'rgangan ko'tarish mexanizmlari (richag, shkiv) ko'nikmasini \"RoboLift\" musobaqasida namoyish etadilar.",
        "O'quvchilar yuk ko'tarish va tashish vazifasini aniq vaqt mezoni bilan bajarishni o'rganadilar.",
        "O'quvchilarda ehtiyotkorlik va aniqlik ko'nikmasi rivojlanadi (yukni tushirib yubormaslik).",
    ],
    "lugat": [
        "Yuk (Load) – ko'tarilishi/tashilishi kerak bo'lgan narsa",
        "Ko'tarish mexanizmi (Lifting mechanism) – yukni ko'taruvchi qism",
        "Barqarorlik (Stability) – robotning yukni tashiyotganda yiqilmasligi",
        "Xronometr (Stopwatch) – vaqtni o'lchovchi asbob",
        "Baholash mezoni (Grading criteria) – natijani baholash qoidalari",
    ],
    "softSkill": "Diqqat va ehtiyotkorlik — yukni tushirib yubormaslik uchun robotni asta va nazorat ostida boshqarish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "Chorak davomida yasalgan ko'tarish mexanizmli robotlar",
        "Standart yuk (kichik kubik/detal)",
        "1 metrlik trassa",
        "Xronometr, natijalar jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Musobaqa qoidalari tushuntiriladi: robot 1 ta standart yukni 1 metr masofaga tashishi kerak.", "Navbat tartibi belgilanadi."]),
        ("Baholash mezoni", 10, ["15 soniyagacha = 5 (a'lo); 16-30 soniya = 4 (yaxshi); 31-50 soniya = 3 (qoniqarli); 51-60 soniya = 2 (qoniqarsiz).", "1 daqiqadan ortiq yoki yukni tushirib yuborsa = FAILED."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 5, ["O'quvchilar robotning ko'tarish mexanizmini so'nggi marta tekshiradilar."]),
        ("Musobaqa", 25, ["Har bir o'quvchi/juftlik navbat bilan yukni ko'tarib, 1 metr tashiydi.", "O'qituvchi vaqtni o'lchaydi va yukning tushib ketmaganini nazorat qiladi.", "Natijalar darhol baholanadi va e'lon qilinadi."]),
    ],
    "uyga": [
        "Robot yukni tezroq va ishonchliroq tashishi uchun nima o'zgartirish mumkinligi haqida o'ylab keling.",
    ],
},

"robosense": {
    "maqsad": [
        "O'quvchilar chorak davomida o'rgangan sensor ko'nikmalarini \"RoboSense\" musobaqasida namoyish etadilar.",
        "O'quvchilar sensorli robotning to'siqni to'g'ri aniqlashi va reaksiya berishini vaqt bilan birga baholashni o'rganadilar.",
        "O'quvchilarda aniqlik va tezkor qaror qabul qilish ko'nikmasi rivojlanadi.",
    ],
    "lugat": [
        "Sensor (Sensor) – to'siqni aniqlovchi qurilma",
        "To'siq (Obstacle) – robot yo'lidagi narsa",
        "Aniqlash (Detection) – sensor to'siqni \"sezishi\"",
        "Reaksiya (Reaction) – to'xtash yoki aylanib o'tish harakati",
        "Baholash mezoni (Grading criteria) – natijani baholash qoidalari",
    ],
    "softSkill": "Aniqlik va tezkorlik — sensorni to'g'ri sozlash va tezkor natijaga erishish o'rtasidagi muvozanatni topish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "Chorak davomida yasalgan sensorli robotlar",
        "1.5 metrlik trassa, yo'l o'rtasida to'siq",
        "Xronometr, natijalar jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Musobaqa qoidalari tushuntiriladi: robot 1.5 metr masofada to'siqni to'g'ri aniqlab, to'xtashi yoki aylanib o'tishi kerak.", "Vaqt VA to'g'ri aniqlash birga baholanishi aytiladi."]),
        ("Baholash mezoni", 10, ["15 soniyagacha va to'siqni to'g'ri aniqlagan = 5 (a'lo); 16-30 soniya = 4 (yaxshi); 31-50 soniya = 3 (qoniqarli); 51-60 soniya = 2 (qoniqarsiz).", "1 daqiqadan ortiq YOKI to'siqni sezmay to'qnashsa = FAILED."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 5, ["O'quvchilar sensor sozlamalarini so'nggi marta tekshiradilar."]),
        ("Musobaqa", 25, ["Har bir o'quvchi/juftlik navbat bilan robotini 1.5 metrlik trassada sinaydi.", "O'qituvchi vaqtni o'lchaydi va to'siqni to'g'ri aniqlaganini kuzatadi.", "Natijalar darhol baholanadi va e'lon qilinadi."]),
    ],
    "uyga": [
        "Sensor to'siqni tezroq va aniqroq aniqlashi uchun qanday o'zgartirish mumkinligi haqida o'ylab keling.",
    ],
},

"robochampionship": {
    "maqsad": [
        "O'quvchilar yil davomida o'rgangan barcha ko'nikmalarni (qurish, motor, sensor) \"RoboChampionship\" yakuniy musobaqasida namoyish etadilar.",
        "O'quvchilar murakkabroq yo'lakni (burilish+to'siq) bosib o'tishni vaqt mezoni bilan bajarishni o'rganadilar.",
        "O'quvchilarda yil yakunidagi yutuqlaridan g'urur va sportchan munosabat tuyg'usi mustahkamlanadi.",
    ],
    "lugat": [
        "Chempionat (Championship) – yil yakunidagi eng katta musobaqa",
        "Burilish (Turn) – yo'lakning to'g'ri chiziqdan chetga og'ishi",
        "Murakkab yo'lak (Complex track) – burilish va to'siqlardan iborat trassa",
        "Sertifikat (Certificate) – g'oliblarga beriladigan tan olish hujjati",
        "Baholash mezoni (Grading criteria) – natijani baholash qoidalari",
    ],
    "softSkill": "G'urur va sportchan munosabat — yil davomidagi mehnat natijasini ko'rsatishdan g'ururlanish, shu bilan birga boshqalar natijasini hurmat qilish.",
    "resurslar": [
        "Yil davomida yasalgan robotlar (yakuniy loyiha yoki tanlangan model)",
        "2.5-3 metrlik murakkab yo'lak (kamida 1 burilish, 1 to'siq bilan)",
        "Xronometr, natijalar jadvali, sertifikat/kichik sovrinlar",
    ],
    "nazariya": [
        ("Kirish", 5, ["Musobaqa qoidalari tushuntiriladi: robot kamida 1 burilish va 1 to'siqli, 2.5-3 metrlik yo'lakni bosib o'tishi kerak.", "Navbat tartibi belgilanadi."]),
        ("Baholash mezoni", 10, ["20 soniyagacha = 5 (a'lo); 21-40 soniya = 4 (yaxshi); 41-55 soniya = 3 (qoniqarli); 56-70 soniya = 2 (qoniqarsiz).", "70 soniyadan ortiq yoki yo'lakni tugatolmasa = FAILED.", "G'oliblarga sertifikat/kichik sovrin taqdim etiladi."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 5, ["O'quvchilar robotlarini yakuniy sinovdan o'tkazadilar."]),
        ("Musobaqa", 25, ["Har bir o'quvchi/juftlik navbat bilan murakkab yo'lakni bosib o'tadi.", "O'qituvchi vaqtni o'lchaydi va natijalarni jadvalga yozadi.", "Yil yakunida g'oliblar e'lon qilinadi va tabriklanadi."]),
    ],
    "uyga": [
        "Yil davomida yasagan eng sevimli robotingiz haqida qisqacha hikoya yozing.",
    ],
},

"dast_naz_2sinf_q3": {
    "maqsad": [
        "O'quvchilar o'zgaruvchi va shart bloklarini birgalikda ishlatgan dasturni mustaqil tuzib ko'rsatadilar.",
        "O'quvchilar o'z dasturlarini sinfga tushuntirib berish orqali fikrlash jarayonini ifodalash ko'nikmasini rivojlantiradilar.",
        "O'quvchilarda dasturlash bo'yicha o'z-o'ziga ishonch mustahkamlanadi.",
    ],
    "lugat": [
        "O'zgaruvchi (Variable) – qiymati o'zgarishi mumkin bo'lgan xotira katakchasi",
        "Shart (Condition/If) – \"agar...bo'lsa\" mantig'i",
        "Dastur (Program) – bloklar ketma-ketligidan tuzilgan buyruqlar",
        "Sinov (Test) – dasturni ishga tushirib tekshirish",
        "Baholash (Assessment) – bajarilgan ishni tekshirish",
    ],
    "softSkill": "O'z ishini taqdim etish — o'z dasturini boshqalarga tushunarli tilda tushuntirib berish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "Planshet/telefon (Makerzoid ilovasi)",
        "1-yilda yasalgan model",
        "Baholash jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Nazorat ishi qoidalari tushuntiriladi: o'zgaruvchi va shartdan foydalangan dastur ko'rsatilishi kerak."]),
        ("Baholash mezoni", 10, ["Dastur to'g'ri ishlashi, o'zgaruvchi va shartning mantiqan to'g'ri ishlatilganligi baholanadi.", "O'quvchi dasturini og'zaki tushuntirib berishi ham hisobga olinadi."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 10, ["O'quvchilar o'z dasturlarini so'nggi marta tekshirib, xatolarni tuzatadilar."]),
        ("Namoyish", 20, ["Har bir o'quvchi navbat bilan dasturini ishga tushirib, natijasini ko'rsatadi.", "O'qituvchi savol berib, o'quvchining tushunishini tekshiradi."]),
    ],
    "uyga": [
        "O'zgaruvchidan foydalanadigan yana bitta o'yin g'oyasini o'ylab, daftaringizga yozing.",
    ],
},

"dast_naz_2sinf_q4": {
    "maqsad": [
        "O'quvchilar funksiyalardan foydalangan dasturni mustaqil tuzib ko'rsatadilar.",
        "O'quvchilar o'z funksiyalarini qayta ishlatish orqali dasturni qisqartirish g'oyasini amalda qo'llaydilar.",
        "O'quvchilarda o'z ishini tizimli taqdim etish ko'nikmasi rivojlanadi.",
    ],
    "lugat": [
        "Funksiya (Function) – qayta-qayta ishlatiladigan buyruqlar to'plami",
        "Parallel harakat (Parallel action) – bir vaqtning o'zida bajariladigan ikki harakat",
        "Vaqt boshqaruvi (Timer) – dastur ichida vaqtni nazorat qilish",
        "Sinov (Test) – dasturni ishga tushirib tekshirish",
        "Baholash (Assessment) – bajarilgan ishni tekshirish",
    ],
    "softSkill": "Tizimlilik — dasturni kichik, qayta ishlatiladigan qismlarga (funksiyalarga) bo'lib tuzish ko'nikmasini mustahkamlash.",
    "resurslar": [
        "Planshet/telefon (Makerzoid ilovasi)",
        "1-yilda yasalgan model",
        "Baholash jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Nazorat ishi qoidalari tushuntiriladi: kamida bitta o'z funksiyasidan foydalangan dastur ko'rsatilishi kerak."]),
        ("Baholash mezoni", 10, ["Funksiyaning to'g'ri yaratilgani va qayta ishlatilgani baholanadi.", "Dastur mantig'i va natija to'g'riligi tekshiriladi."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 10, ["O'quvchilar dasturlarini so'nggi marta tekshiradilar."]),
        ("Namoyish", 20, ["Har bir o'quvchi navbat bilan dasturini ishga tushirib, funksiyasini ko'rsatadi va tushuntiradi."]),
    ],
    "uyga": [
        "Boshqa qanday vaziyatda funksiyadan foydalanish mumkinligi haqida bitta misol o'ylab yozing.",
    ],
},

"dast_naz_3sinf_q3": {
    "maqsad": [
        "O'quvchilar VA/YOKI mantiqiy operatorlari va ichma-ich sikllardan foydalangan dasturni mustaqil tuzib ko'rsatadilar.",
        "O'quvchilar murakkabroq mantiqiy vaziyatlarni dastur orqali ifodalashni o'rganadilar.",
        "O'quvchilarda murakkab masalani bosqichma-bosqich yechish ko'nikmasi mustahkamlanadi.",
    ],
    "lugat": [
        "VA operatori (AND) – ikkala shart ham to'g'ri bo'lganda ishlaydigan mantiq",
        "YOKI operatori (OR) – kamida bitta shart to'g'ri bo'lganda ishlaydigan mantiq",
        "Ichma-ich sikl (Nested loop) – sikl ichidagi sikl",
        "Dastur mantig'i (Program logic) – dasturning qanday qaror qabul qilishi",
        "Baholash (Assessment) – bajarilgan ishni tekshirish",
    ],
    "softSkill": "Murakkab mantiqiy fikrlash — bir nechta shartni birgalikda baholash va to'g'ri qaror qabul qilish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "Planshet/telefon (Makerzoid ilovasi)",
        "1-yilda yasalgan model",
        "Baholash jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Nazorat ishi qoidalari tushuntiriladi: VA/YOKI va ichma-ich sikldan foydalangan dastur ko'rsatilishi kerak."]),
        ("Baholash mezoni", 10, ["Mantiqiy operatorlarning to'g'ri ishlatilgani va ichma-ich siklning to'g'ri tuzilgani baholanadi."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 10, ["O'quvchilar dasturlarini so'nggi marta tekshirib, sinaydilar."]),
        ("Namoyish", 20, ["Har bir o'quvchi navbat bilan dasturini ishga tushirib, mantiq qismini tushuntiradi."]),
    ],
    "uyga": [
        "VA yoki YOKI operatoridan foydalanadigan kundalik hayotdagi bitta misolni yozing (masalan: \"agar yomg'ir yog'sa VA sovuq bo'lsa, kurtka kiyaman\").",
    ],
},

"dast_naz_3sinf_q4": {
    "maqsad": [
        "O'quvchilar to'liq avtonom (odam aralashuvisiz ishlaydigan) dasturni mustaqil tuzib ko'rsatadilar.",
        "O'quvchilar yil davomida o'rgangan barcha dasturlash tushunchalarini (shart, sikl, funksiya, holat) birlashtiradilar.",
        "O'quvchilarda SPIKE bosqichiga o'tish uchun zarur bo'lgan mustaqillik ko'nikmasi shakllanadi.",
    ],
    "lugat": [
        "Avtonom dastur (Autonomous program) – odam aralashuvisiz ishlaydigan dastur",
        "Holat (State) – robotning joriy vaziyati",
        "Debugging – dasturdagi xatoni topib tuzatish",
        "Optimallashtirish (Optimization) – dasturni qisqaroq va samaraliroq qilish",
        "Baholash (Assessment) – bajarilgan ishni tekshirish",
    ],
    "softSkill": "Mustaqillik va o'z-o'ziga ishonch — to'liq avtonom dastur yaratish orqali mustaqil ishlash ko'nikmasini mustahkamlash.",
    "resurslar": [
        "Planshet/telefon (Makerzoid ilovasi)",
        "1-yilning eng murakkab modeli",
        "Baholash jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Nazorat ishi qoidalari tushuntiriladi: robot odam aralashuvisiz to'liq dastur bo'yicha ishlashi kerak."]),
        ("Baholash mezoni", 10, ["Dasturning to'liq avtonom ishlashi, xatolarga chidamliligi va mantiq to'g'riligi baholanadi."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 10, ["O'quvchilar dasturlarini so'nggi marta tekshirib, xatolarni tuzatadilar."]),
        ("Namoyish", 20, ["Har bir o'quvchi navbat bilan dasturini ishga tushiradi, robot odam aralashuvisiz ishlashini ko'rsatadi."]),
    ],
    "uyga": [
        "Keyingi yil (SPIKE Prime) haqida internetdan bitta qiziqarli ma'lumot toping.",
    ],
},

"spike_naz_q1": {
    "maqsad": [
        "O'quvchilar Driving Base va tanlagan 2 ta attachmentni mustaqil yig'ib, ishlash tamoyilini tushuntirib beradilar.",
        "O'quvchilar SPIKE Prime qismlarini to'g'ri nomlash va ularning vazifasini bilishni namoyish etadilar.",
        "O'quvchilarda texnik tushuntirish (og'zaki taqdimot) ko'nikmasi rivojlanadi.",
    ],
    "lugat": [
        "Driving Base – harakatlanuvchi robot asosi",
        "Attachment – asosiy robotga qo'shiladigan qo'shimcha qurilma",
        "Hub – SPIKE Prime ning markaziy boshqaruv bloki",
        "Instruksiya (Instructions) – rasmli qurish qo'llanmasi",
        "Baholash (Assessment) – bajarilgan ishni tekshirish",
    ],
    "softSkill": "Texnik tushuntirish — yig'ilgan qurilmaning tuzilishi va vazifasini aniq, tushunarli tilda tushuntirib berish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "LEGO Education SPIKE Prime to'plami",
        "Rasmiy instruksiyalar",
        "Baholash jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Nazorat ishi qoidalari tushuntiriladi: Driving Base va 2 ta attachment tanlab, yig'ish va tushuntirish kerak."]),
        ("Baholash mezoni", 10, ["Qurilmaning to'g'ri va mustahkam yig'ilgani, qismlar nomlarining to'g'ri aytilgani baholanadi."]),
    ],
    "amaliy": [
        ("Yig'ish", 20, ["O'quvchilar Driving Base va 2 ta attachmentni mustaqil yig'adilar."]),
        ("Tushuntirish", 10, ["Har bir o'quvchi yig'ilgan qurilmani ko'rsatib, qismlarini va vazifasini tushuntiradi."]),
    ],
    "uyga": [
        "SPIKE Prime'dagi yana qaysi attachment turlarini bilib olganingizni ro'yxat qiling.",
    ],
},

"spike_naz_q2": {
    "maqsad": [
        "O'quvchilar kamida 2 ta sensor ishlatilgan dasturni mustaqil tuzib ko'rsatadilar.",
        "O'quvchilar SPIKE sensorlarining har birining vazifasini tushuntirib bera oladilar.",
        "O'quvchilarda dasturni sinash va xatoni tuzatish ko'nikmasi mustahkamlanadi.",
    ],
    "lugat": [
        "Sensor (Sensor) – atrof-muhitni aniqlovchi qurilma",
        "Reaktiv dastur (Reactive program) – sensor signaliga darhol javob beruvchi dastur",
        "Kalibrlash (Calibration) – sensorni aniq ishlashi uchun sozlash",
        "Blok (Block) – dasturdagi buyruq elementi",
        "Baholash (Assessment) – bajarilgan ishni tekshirish",
    ],
    "softSkill": "Aniqlik va sinov — sensor sozlamalarini aniq sozlab, barqaror natijaga erishish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "LEGO Education SPIKE Prime to'plami",
        "Planshet/noutbuk (SPIKE ilovasi)",
        "Baholash jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Nazorat ishi qoidalari tushuntiriladi: kamida 2 ta sensor ishlatilgan dastur ko'rsatilishi kerak."]),
        ("Baholash mezoni", 10, ["Sensorlarning to'g'ri ishlatilgani va dasturning barqaror ishlashi baholanadi."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 10, ["O'quvchilar dasturlarini so'nggi marta tekshirib, sensorlarni kalibrlaydilar."]),
        ("Namoyish", 20, ["Har bir o'quvchi dasturini ishga tushirib, ikkala sensorning ishlashini ko'rsatadi."]),
    ],
    "uyga": [
        "SPIKE'dagi yana qaysi sensordan foydalanishni xohlaganingiz va nima uchun ekanini yozing.",
    ],
},

"spike_naz_q3": {
    "maqsad": [
        "O'quvchilar 1 va 2-missiyalarni ketma-ket, FLL musobaqa formatida bajaradilar.",
        "O'quvchilar ball tizimi asosida baholanish tajribasini oladilar.",
        "O'quvchilarda jamoaviy strategiya va vaqtni boshqarish ko'nikmasi rivojlanadi.",
    ],
    "lugat": [
        "Missiya (Mission) – bajarilishi kerak bo'lgan aniq vazifa",
        "Ball (Points) – vazifa bajarilgani uchun beriladigan miqdor",
        "Attachment – vazifani bajarish uchun robotga qo'shiladigan qurilma",
        "Musobaqa maydonchasi (Competition field) – missiyalar joylashgan maydon",
        "Baholash mezoni (Grading criteria) – natijani baholash qoidalari",
    ],
    "softSkill": "Jamoaviy strategiya — vaqt va vazifalarni jamoa bilan birga rejalashtirish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "LEGO Education SPIKE Prime to'plami va attachmentlar",
        "Musobaqa maydonchasi (missiya elementlari bilan)",
        "Xronometr, ball jadvali",
    ],
    "nazariya": [
        ("Kirish", 5, ["Missiya musobaqasi qoidalari tushuntiriladi: 1 va 2-missiya ketma-ket bajariladi."]),
        ("Baholash mezoni", 10, ["Har bir missiya muvaffaqiyatli bajarilsa 25 balldan (jami 50 ball).", "45-50 ball = 5 (a'lo); 35-44 = 4 (yaxshi); 25-34 = 3 (qoniqarli); 15-24 = 2 (qoniqarsiz); 15 balldan kam = FAILED."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 10, ["O'quvchilar/jamoalar robot va attachmentlarni so'nggi marta tekshiradilar."]),
        ("Musobaqa", 20, ["Har bir jamoa navbat bilan 1 va 2-missiyani bajaradi.", "Natijalar ball jadvaliga yoziladi va e'lon qilinadi."]),
    ],
    "uyga": [
        "1 va 2-missiyani yanada tezroq bajarish uchun qanday o'zgartirish kiritish mumkinligi haqida o'ylab keling.",
    ],
},

"spike_naz_q4": {
    "maqsad": [
        "O'quvchilar barcha 4 missiyani FLL formatida, 2.5 daqiqa ichida ketma-ket bajaradilar.",
        "O'quvchilar yil davomida o'rgangan barcha qurish va dasturlash ko'nikmalarini birlashtiradilar.",
        "O'quvchilarda musobaqa bosimida ishlash va jamoaviy hamkorlik ko'nikmasi mustahkamlanadi.",
    ],
    "lugat": [
        "To'liq missiya turi (Full mission round) – barcha missiyalarning ketma-ket bajarilishi",
        "Ball tizimi (Scoring system) – har bir missiya uchun beriladigan ball",
        "Strategiya (Strategy) – missiyalarni qanday tartibda bajarish rejasi",
        "Muhandislik daftari (Engineering notebook) – loyiha jarayonini qayd etuvchi hujjat",
        "Baholash mezoni (Grading criteria) – natijani baholash qoidalari",
    ],
    "softSkill": "Bosim ostida ishlash — vaqt cheklangan sharoitda tinch va tizimli ishlash ko'nikmasini rivojlantirish.",
    "resurslar": [
        "LEGO Education SPIKE Prime to'plami va barcha attachmentlar",
        "To'liq musobaqa maydonchasi (4 missiya bilan)",
        "Xronometr, ball jadvali, sertifikatlar",
    ],
    "nazariya": [
        ("Kirish", 5, ["Yakuniy musobaqa qoidalari tushuntiriladi: barcha 4 missiya 2.5 daqiqada bajariladi."]),
        ("Baholash mezoni", 10, ["Har bir missiya 25 balldan (jami 100 ball).", "85-100 = 5 (a'lo); 65-84 = 4 (yaxshi); 45-64 = 3 (qoniqarli); 25-44 = 2 (qoniqarsiz); 25 balldan kam = FAILED."]),
    ],
    "amaliy": [
        ("Tayyorgarlik", 10, ["Jamoalar robot va barcha attachmentlarni yakuniy tekshiradilar."]),
        ("Bitiruv turniri", 20, ["Har bir jamoa navbat bilan 2.5 daqiqalik to'liq missiya turini bajaradi.", "Natijalar ball jadvaliga yoziladi, g'oliblar va barcha ishtirokchilar tabriklanadi."]),
    ],
    "uyga": [
        "0-4-sinf va SPIKE davomida eng yodda qolgan loyihangiz haqida qisqacha insho yozing.",
    ],
},

}


LOYIHA_CONTENT = {

"free_project_q1": {
    "maqsad": [
        "O'quvchilar 1-chorak davomida yasagan modellardan birini tanlab, uni o'zgartirib yoki kengaytirib, erkin ijod qiladilar.",
        "O'quvchilar o'z g'oyasini mustaqil amalga oshirish tajribasini oladilar.",
        "O'quvchilar yig'ilgan modelni sinfga taqdim etish ko'nikmasini rivojlantiradilar.",
    ],
    "lugat": [
        "Loyiha (Project) – mustaqil bajariladigan ijodiy ish",
        "O'zgartirish (Modify) – tayyor modelga o'z g'oyasini qo'shish",
        "Kengaytirish (Extend) – modelga qo'shimcha qism qo'shish",
        "Taqdimot (Presentation) – ishni boshqalarga ko'rsatib tushuntirish",
        "Erkin ijod (Free creativity) – o'z xohishi bilan ijod qilish",
    ],
    "softSkill": "Ijodkorlik va mustaqillik — tayyor namunadan chetga chiqib, o'z g'oyasini qo'shish orqali ijodiy fikrlashni rivojlantirish.",
    "resurslar": [
        "1-chorakda ishlatilgan barcha detallar",
        "O'quvchi tanlagan asosiy model instruksiyasi",
        "Qo'shimcha bezak/erkin detallar (agar mavjud bo'lsa)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Loyiha vazifasi tushuntiriladi: shu chorak modellaridan birini tanlab, o'zgartirib yoki kengaytirib qurish."]),
        ("G'oya va reja", 5, ["O'quvchilar qaysi modelni tanlashlari va uni qanday o'zgartirishlari haqida qisqacha reja tuzadilar."]),
    ],
    "amaliy": [
        ("Loyihani qurish", 25, ["O'quvchilar tanlagan modelni asos qilib, o'z g'oyalarini qo'shib quradilar."]),
        ("Taqdimot", 10, ["Har bir o'quvchi o'z loyihasini sinfga ko'rsatib, nima o'zgartirganini tushuntiradi."]),
    ],
    "uyga": [
        "Loyihangiz rasmini chizib yoki fotosini olib, keyingi chorakda yana qanday rivojlantirish mumkinligi haqida yozing.",
    ],
},

"dast_loy_2sinf_q3": {
    "maqsad": [
        "O'quvchilar 1-yilda yasagan modeliga o'zgaruvchi (hisoblagich) qo'shib, unga \"xotira\" beradilar.",
        "O'quvchilar o'rgangan dasturlash bilimlarini o'z modeliga mustaqil tatbiq etadilar.",
        "O'quvchilar loyihasini sinfga taqdim etish ko'nikmasini rivojlantiradilar.",
    ],
    "lugat": [
        "O'zgaruvchi (Variable) – qiymati o'zgarishi mumkin bo'lgan xotira katakchasi",
        "Hisoblagich (Counter) – sanash uchun ishlatiladigan o'zgaruvchi",
        "Dastur (Program) – bloklar ketma-ketligi",
        "Loyiha (Project) – mustaqil bajariladigan ish",
        "Taqdimot (Presentation) – ishni ko'rsatib tushuntirish",
    ],
    "softSkill": "Ijodiy dasturlash — o'z modeliga yangi funksiya (xotira) qo'shish orqali ijodiy dasturlash ko'nikmasini rivojlantirish.",
    "resurslar": [
        "1-yilda yasalgan model",
        "Planshet/telefon (Makerzoid ilovasi)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Loyiha vazifasi tushuntiriladi: modelga hisoblagich (o'zgaruvchi) qo'shish."]),
        ("Reja", 5, ["O'quvchilar hisoblagich nimani sanashini (masalan, necha marta aylandi) rejalashtiradilar."]),
    ],
    "amaliy": [
        ("Dastur yozish", 25, ["O'quvchilar o'z modeliga hisoblagich qo'shib, dasturni yozadilar va sinaydilar."]),
        ("Taqdimot", 10, ["Har bir o'quvchi dasturini ishga tushirib, hisoblagich qanday ishlashini tushuntiradi."]),
    ],
    "uyga": [
        "Hisoblagichdan yana qanday maqsadda foydalanish mumkinligi haqida bitta g'oya yozing.",
    ],
},

"dast_loy_2sinf_q4": {
    "maqsad": [
        "O'quvchilar 1-yildagi eng sevimli modelini to'liq avtomatlashtiradilar (funksiyalar yordamida).",
        "O'quvchilar yil davomida o'rgangan barcha dasturlash bilimlarini (o'zgaruvchi, sikl, funksiya) birlashtiradilar.",
        "O'quvchilar yakuniy loyihasini ishonch bilan taqdim etadilar.",
    ],
    "lugat": [
        "Funksiya (Function) – qayta ishlatiladigan buyruqlar to'plami",
        "Avtomatlashtirish (Automation) – modelning o'z-o'zidan ishlashini ta'minlash",
        "Loyiha (Project) – mustaqil bajariladigan yakuniy ish",
        "Taqdimot (Presentation) – ishni ko'rsatib tushuntirish",
        "Sinov (Test) – dasturni tekshirish jarayoni",
    ],
    "softSkill": "Yakuniy taqdimot mahorati — bir chorak davomidagi ishni tizimli va ishonchli tarzda taqdim etish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "1-yildagi eng sevimli model",
        "Planshet/telefon (Makerzoid ilovasi)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Yakuniy loyiha vazifasi tushuntiriladi: modelni funksiyalar yordamida to'liq avtomatlashtirish."]),
        ("Reja", 5, ["O'quvchilar qaysi funksiyalarni yaratishlarini rejalashtiradilar."]),
    ],
    "amaliy": [
        ("Dastur yozish", 25, ["O'quvchilar funksiyalardan foydalanib, modelni to'liq avtomatlashtiradilar."]),
        ("Yakuniy taqdimot", 10, ["Har bir o'quvchi yakuniy dasturini namoyish qiladi va tushuntiradi."]),
    ],
    "uyga": [
        "Ushbu yil dasturlashda eng ko'p yoqqan mavzu haqida qisqacha yozing.",
    ],
},

"dast_loy_3sinf_q3": {
    "maqsad": [
        "O'quvchilar 1-yilda yasagan modeliga murakkab mantiq (VA/YOKI, ichma-ich sikl) qo'shadilar.",
        "O'quvchilar murakkab dasturlash tushunchalarini o'z loyihasida mustaqil qo'llaydilar.",
        "O'quvchilar loyihasini tizimli tarzda taqdim etadilar.",
    ],
    "lugat": [
        "VA/YOKI operatorlari (AND/OR) – bir nechta shartni birgalikda tekshiruvchi mantiq",
        "Ichma-ich sikl (Nested loop) – sikl ichidagi sikl",
        "Murakkab mantiq (Complex logic) – bir nechta shart va siklning birgalikda ishlashi",
        "Loyiha (Project) – mustaqil bajariladigan ish",
        "Taqdimot (Presentation) – ishni ko'rsatib tushuntirish",
    ],
    "softSkill": "Murakkab masalani bo'laklarga bo'lish — katta vazifani kichik, boshqariladigan qismlarga bo'lib yechish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "1-yilda yasalgan model",
        "Planshet/telefon (Makerzoid ilovasi)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Loyiha vazifasi tushuntiriladi: modelga VA/YOKI va ichma-ich sikl qo'shish."]),
        ("Reja", 5, ["O'quvchilar qanday murakkab vaziyatni dastur orqali ifodalashlarini rejalashtiradilar."]),
    ],
    "amaliy": [
        ("Dastur yozish", 25, ["O'quvchilar murakkab mantiqni o'z modeliga qo'shib, dasturni sinaydilar."]),
        ("Taqdimot", 10, ["Har bir o'quvchi dasturini namoyish qilib, mantig'ini tushuntiradi."]),
    ],
    "uyga": [
        "Murakkab mantiq (VA/YOKI) ishlatilgan yana bitta o'yin g'oyasini o'ylab yozing.",
    ],
},

"dast_loy_3sinf_q4": {
    "maqsad": [
        "O'quvchilar 1-yildagi eng murakkab modelini to'liq \"aqlli\" (avtonom) qiladilar — SPIKE'ga tayyorgarlik sifatida.",
        "O'quvchilar yil davomida o'rgangan barcha dasturlash bilimlarini yakuniy loyihada birlashtiradilar.",
        "O'quvchilar keyingi bosqich (SPIKE Prime)ga o'tishga ruhiy va bilim jihatidan tayyor bo'ladilar.",
    ],
    "lugat": [
        "Avtonom robot (Autonomous robot) – odam aralashuvisiz ishlaydigan robot",
        "Holat (State) – robotning joriy vaziyati",
        "Xato-bardoshlik (Fault tolerance) – kutilmagan holatlarda ham ishlashda davom etish qobiliyati",
        "Loyiha (Project) – mustaqil bajariladigan yakuniy ish",
        "Taqdimot (Presentation) – ishni ko'rsatib tushuntirish",
    ],
    "softSkill": "Yakuniy mustaqillik — ikki yillik dasturlash bilimlarini birlashtirib, to'liq mustaqil loyiha yaratish ko'nikmasini mustahkamlash.",
    "resurslar": [
        "1-yildagi eng murakkab model",
        "Planshet/telefon (Makerzoid ilovasi)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Yakuniy loyiha vazifasi tushuntiriladi: modelni to'liq avtonom va \"aqlli\" qilish."]),
        ("Reja", 5, ["O'quvchilar qanday holatlar va shartlar kerakligini rejalashtiradilar."]),
    ],
    "amaliy": [
        ("Dastur yozish", 25, ["O'quvchilar to'liq avtonom dasturni yozib, turli sharoitda sinaydilar."]),
        ("Yakuniy taqdimot", 10, ["Har bir o'quvchi yakuniy dasturini namoyish qiladi va SPIKE'ga qanday tayyor ekanini aytadi."]),
    ],
    "uyga": [
        "SPIKE Prime bosqichida nimalarni o'rganishni xohlaganingiz haqida qisqacha yozing.",
    ],
},

"spike_loy_q1": {
    "maqsad": [
        "O'quvchilar o'z Driving Base va tanlagan attachmentlar kombinatsiyasini erkin tarzda yaratadilar.",
        "O'quvchilar SPIKE qismlarini mustaqil tanlab, birlashtirish tajribasini oladilar.",
        "O'quvchilar o'z konstruksiyasini sinfga taqdim etadilar.",
    ],
    "lugat": [
        "Driving Base – harakatlanuvchi robot asosi",
        "Attachment – qo'shimcha qurilma",
        "Kombinatsiya (Combination) – bir nechta qismning birgalikda ishlatilishi",
        "Loyiha (Project) – mustaqil bajariladigan ish",
        "Taqdimot (Presentation) – ishni ko'rsatib tushuntirish",
    ],
    "softSkill": "Erkin ijod — tayyor qismlardan o'z kombinatsiyasini yaratish orqali ijodiy muhandislik fikrlashini rivojlantirish.",
    "resurslar": [
        "LEGO Education SPIKE Prime to'plami",
        "1-chorakda yig'ilgan barcha Driving Base va attachmentlar",
    ],
    "nazariya": [
        ("Kirish", 5, ["Loyiha vazifasi tushuntiriladi: o'z Driving Base va tanlagan attachmentlar kombinatsiyasini yaratish."]),
        ("Reja", 5, ["O'quvchilar qaysi Driving Base va qaysi attachmentlarni birlashtirishni rejalashtiradilar."]),
    ],
    "amaliy": [
        ("Qurish", 25, ["O'quvchilar tanlagan qismlarni birlashtirib, o'z konstruksiyasini yaratadilar."]),
        ("Taqdimot", 10, ["Har bir o'quvchi konstruksiyasini ko'rsatib, nima uchun shu kombinatsiyani tanlaganini tushuntiradi."]),
    ],
    "uyga": [
        "Konstruksiyangizni yanada yaxshilash uchun qanday attachment qo'shish mumkinligi haqida yozing.",
    ],
},

"spike_loy_q2": {
    "maqsad": [
        "O'quvchilar aqlli parking robotini mustaqil loyihalab, quradilar va dasturlaydilar.",
        "O'quvchilar kamida 2 ta sensordan foydalangan holda real hayotiy muammoga yechim yaratadilar.",
        "O'quvchilar loyihasini sinov qilib, natijasini taqdim etadilar.",
    ],
    "lugat": [
        "Parking robot (Parking robot) – mashinani to'g'ri joyga qo'yishga yordam beruvchi robot",
        "Sensor kombinatsiyasi (Sensor combination) – bir nechta sensorning birgalikda ishlashi",
        "Loyiha (Project) – mustaqil bajariladigan ish",
        "Sinov (Test) – loyihani tekshirish jarayoni",
        "Taqdimot (Presentation) – ishni ko'rsatib tushuntirish",
    ],
    "softSkill": "Real muammoga yechim topish — kundalik hayotdagi muammoni (parking) texnik yechim orqali hal qilish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "LEGO Education SPIKE Prime to'plami",
        "Planshet/noutbuk (SPIKE ilovasi)",
        "Kichik \"parking joy\" maketi (qog'ozda chizilgan bo'lishi mumkin)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Loyiha vazifasi tushuntiriladi: aqlli parking robotini loyihalash va dasturlash."]),
        ("Reja", 5, ["O'quvchilar qaysi sensorlardan foydalanishlarini va robot qanday ishlashini rejalashtiradilar."]),
    ],
    "amaliy": [
        ("Qurish va dasturlash", 25, ["O'quvchilar robotni quradilar, sensorlarni ulaydilar va dasturni yozadilar."]),
        ("Sinov va taqdimot", 10, ["O'quvchilar robotni sinaydilar va natijasini sinfga ko'rsatadilar."]),
    ],
    "uyga": [
        "Aqlli parking tizimlari haqiqiy hayotda qanday ishlashi haqida internetdan ma'lumot toping.",
    ],
},

"spike_loy_q3": {
    "maqsad": [
        "O'quvchilar 1 va 2-missiya uchun eng mukammal robot+attachment yechimini yaratadilar.",
        "O'quvchilar dizaynni bir necha marta sinab, takomillashtirish jarayonini o'tkazadilar.",
        "O'quvchilar yechimlarini jamoa sifatida taqdim etadilar.",
    ],
    "lugat": [
        "Optimallashtirish (Optimization) – yechimni yanada yaxshilash jarayoni",
        "Attachment dizayni (Attachment design) – vazifaga mos qurilma yaratish",
        "Iteratsiya (Iteration) – sinov-tuzatish jarayonini takrorlash",
        "Loyiha (Project) – mustaqil bajariladigan ish",
        "Taqdimot (Presentation) – ishni ko'rsatib tushuntirish",
    ],
    "softSkill": "Takomillashtirish mentaliteti — birinchi yechim bilan cheklanmasdan, uni bir necha marta sinab yaxshilashga intilish ko'nikmasini rivojlantirish.",
    "resurslar": [
        "LEGO Education SPIKE Prime to'plami va attachmentlar",
        "Musobaqa maydonchasi (1 va 2-missiya elementlari)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Loyiha vazifasi tushuntiriladi: 1 va 2-missiya uchun eng yaxshi yechimni topish."]),
        ("Reja", 5, ["Jamoalar qaysi attachment dizaynini sinab ko'rishni rejalashtiradilar."]),
    ],
    "amaliy": [
        ("Takomillashtirish", 25, ["Jamoalar attachment va dasturni bir necha marta sinab, yaxshilaydilar."]),
        ("Taqdimot", 10, ["Har bir jamoa eng yaxshi natijasini ko'rsatadi va nima o'zgartirganini tushuntiradi."]),
    ],
    "uyga": [
        "Yechimingizni yana qanday yaxshilash mumkinligi haqida bitta g'oya yozing.",
    ],
},

"spike_loy_q4": {
    "maqsad": [
        "O'quvchilar barcha 4 missiyani qamrab oluvchi to'liq bitiruv musobaqasi yechimini tayyorlaydilar.",
        "O'quvchilar ikki yillik (Makerzoid+SPIKE) bilimlarini yakuniy loyihada birlashtiradilar.",
        "O'quvchilar ochiq turnirda o'z natijalarini ota-onalar oldida namoyish etadilar.",
    ],
    "lugat": [
        "Bitiruv musobaqasi (Capstone competition) – dastur yakunidagi eng katta sinov",
        "Ochiq turnir (Open tournament) – tomoshabinlar ishtirokidagi musobaqa",
        "Strategiya (Strategy) – barcha missiyalarni bajarish rejasi",
        "Loyiha (Project) – mustaqil bajariladigan yakuniy ish",
        "Taqdimot (Presentation) – ishni ko'rsatib tushuntirish",
    ],
    "softSkill": "Yakuniy mas'uliyat va g'urur — ikki yillik mehnat natijasini ota-onalar oldida ishonch bilan namoyish etish ko'nikmasini mustahkamlash.",
    "resurslar": [
        "LEGO Education SPIKE Prime to'plami va barcha attachmentlar",
        "To'liq musobaqa maydonchasi (4 missiya bilan)",
        "Ko'rgazma uchun joy (ota-onalar uchun)",
    ],
    "nazariya": [
        ("Kirish", 5, ["Yakuniy loyiha vazifasi tushuntiriladi: barcha 4 missiyani qamrab oluvchi to'liq yechim."]),
        ("Reja", 5, ["Jamoalar barcha missiyalarni qanday tartibda bajarish strategiyasini tuzadilar."]),
    ],
    "amaliy": [
        ("Yakuniy tayyorgarlik", 25, ["Jamoalar robot, attachmentlar va dasturni yakuniy sinovdan o'tkazadilar."]),
        ("Ochiq turnir", 10, ["Jamoalar ota-onalar oldida to'liq missiya turini namoyish etadilar."]),
    ],
    "uyga": [
        "0-4-sinf va SPIKE davomidagi eng katta yutug'ingiz haqida qisqacha insho yozing.",
    ],
},

}


def match_nazorat(title):
    t = title
    if "RoboRace" in t: return NAZORAT_CONTENT["roborace"]
    if "RoboLift" in t: return NAZORAT_CONTENT["robolift"]
    if "RoboSense" in t: return NAZORAT_CONTENT["robosense"]
    if "RoboChampionship" in t: return NAZORAT_CONTENT["robochampionship"]
    if "o'zgaruvchi+shart" in t: return NAZORAT_CONTENT["dast_naz_2sinf_q3"]
    if "funksiyalardan foydalangan" in t: return NAZORAT_CONTENT["dast_naz_2sinf_q4"]
    if "VA/YOKI va ichma-ich sikl" in t: return NAZORAT_CONTENT["dast_naz_3sinf_q3"]
    if "to'liq avtonom dasturni" in t: return NAZORAT_CONTENT["dast_naz_3sinf_q4"]
    if "Driving Base va 2 attachmentni" in t: return NAZORAT_CONTENT["spike_naz_q1"]
    if "SPIKE sensorlari va reaktiv dastur" in t: return NAZORAT_CONTENT["spike_naz_q2"]
    if "Missiya musobaqasi" in t: return NAZORAT_CONTENT["spike_naz_q3"]
    if "To'liq missiya turi" in t: return NAZORAT_CONTENT["spike_naz_q4"]
    return None


def match_loyiha(title):
    t = title
    if "shu chorak modellaridan birini tanlab" in t: return LOYIHA_CONTENT["free_project_q1"]
    if "xotira" in t and "hisoblagich" in t: return LOYIHA_CONTENT["dast_loy_2sinf_q3"]
    if "eng sevimli modelimni to'liq avtomatlashtirish" in t: return LOYIHA_CONTENT["dast_loy_2sinf_q4"]
    if "murakkab mantiq" in t: return LOYIHA_CONTENT["dast_loy_3sinf_q3"]
    if "eng murakkab modelimni to'liq" in t: return LOYIHA_CONTENT["dast_loy_3sinf_q4"]
    if "Driving Base + tanlagan attachmentlar" in t: return LOYIHA_CONTENT["spike_loy_q1"]
    if "aqlli parking robot" in t: return LOYIHA_CONTENT["spike_loy_q2"]
    if "1-2-missiya uchun mukammal" in t: return LOYIHA_CONTENT["spike_loy_q3"]
    if "to'liq 4-missiyali bitiruv" in t: return LOYIHA_CONTENT["spike_loy_q4"]
    return None
