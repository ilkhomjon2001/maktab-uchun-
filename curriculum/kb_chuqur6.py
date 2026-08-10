# -*- coding: utf-8 -*-
"""
NAZARIYANI CHUQURLASHTIRISH — 6-qism: qolgan mavzular.

Nosozlik topish, mikrokontroller tushunchasi, korpus, loyiha bosqichlari,
tarmoq diagnostikasi va AI loyihasining tayyorgarlik bosqichlari.
Shu qism bilan 5-8 dagi HAMMA mavzu darsi qamrab olinadi.
"""


def D(*bloklar):
    return [(sarlavha, list(bandlar)) for sarlavha, bandlar in bloklar]


CHUQUR6 = {

# ============================================================ NOSOZLIK TOPISH
"Nosozlik topish: ishlamayotgan zanjirni tekshirish tartibi": D(
 ("Qat'iy tartib", [
  "1) QUVVAT: batareya yangimi, ulanganmi, kuchlanish yetarlimi. Multimetr bilan o'lchang.",
  "2) YOPIQLIK: halqa uzilmaganmi. Multimetrning signalli rejimi bilan tekshiring.",
  "3) QUTBLAR: LED, diod, kondensator, modul to'g'ri tomonga ulanganmi.",
  "4) KOMPONENT: har birini alohida sinang yoki ishlaydigan boshqasi bilan almashtiring.",
  "5) QIYMATLAR: rezistorlar to'g'ri nominalda ekanini o'lchab tekshiring.",
  "Bu tartibni buzmaslik kerak: ko'pchilik oxirgi qadamdan boshlaydi va vaqtni behuda sarflaydi.",
 ]),
 ("Yarim bo'lish usuli", [
  "Zanjir uzun bo'lsa uni O'RTASIDAN bo'lib tekshiring.",
  "O'rta nuqtada kuchlanish bormi degan savolga javob bering.",
  "Bor bo'lsa — muammo ikkinchi yarmida. Yo'q bo'lsa — birinchi yarmida.",
  "Keyin xato bo'lgan yarmini yana ikkiga bo'ling.",
  "16 elementli zanjirda bu usul 4 ta o'lchov bilan xatoni topadi (birma-bir tekshirsangiz 16 ta kerak bo'lardi).",
 ]),
 ("Eng ko'p uchraydigan sabablar", [
  "Sim breadboard teshigiga to'liq kirmagan — birinchi navbatda shuni tekshiring.",
  "LED teskari ulangan.",
  "GND ulanmagan yoki tashqi manba GND si plata GND si bilan birlashtirilmagan.",
  "Batareya bo'shagan (yuksiz normal ko'rsatib, yuk ostida cho'kadi).",
  "Rezistor noto'g'ri nominalda (rangni noto'g'ri o'qish).",
 ]),
),

"Nosozlik topish usullari: bosqichma-bosqich tekshirish": D(
 ("Uchta asosiy usul", [
  "KO'Z BILAN: eng tez usul. Kuygan komponent, uzilgan sim, tegib turgan oyoqlar, noto'g'ri qutb.",
  "O'LCHOV BILAN: multimetr bilan kuchlanish va uzilishni tekshirish.",
  "ALMASHTIRISH BILAN: shubhali komponentni ishlaydigan boshqasi bilan almashtirish.",
  "Tartib shu: avval ko'z, keyin o'lchov, oxirida almashtirish (u eng ko'p vaqt oladi).",
 ]),
 ("Bir vaqtda bitta o'zgarish", [
  "Eng muhim qoida: bir vaqtda FAQAT BITTA narsani o'zgartiring.",
  "Ikki narsani birga o'zgartirsangiz, qaysi biri yordam berganini bilib bo'lmaydi.",
  "Har o'zgarishdan keyin sinab ko'ring va natijani yozing.",
  "Yordam bermagan o'zgarishni QAYTARIB oling — aks holda sxemada tushunarsiz o'zgarishlar to'planib qoladi.",
 ]),
 ("Yozib borish", [
  "Nima sinaldi, qanday natija chiqdi — ikki ustunli jadval yetarli.",
  "Bu jadval bir xil tekshiruvni ikki marta qilishning oldini oladi.",
  "Xato topilgach, uning sababi va yechimi ham yoziladi.",
  "Bir necha darsdan keyin bu yozuvlar shaxsiy \"tipik xatolar ro'yxati\" ga aylanadi.",
 ]),
),

"Nosozlik topish: murakkab zanjirda": D(
 ("Zanjirni bloklarga bo'lish", [
  "Murakkab sxemani mustaqil bloklarga ajrating: quvvat, sensor, boshqaruv, ijro.",
  "Har bir blokni ALOHIDA tekshiring — qolganlarini uzib qo'yib.",
  "Ishlagan bloklarni belgilang, ishlamaganini chuqurroq tekshiring.",
  "Bloklar alohida ishlab, birga ishlamasa — muammo ular orasidagi bog'lanishda (umumiy GND, quvvat yetishmasligi, pin to'qnashuvi).",
 ]),
 ("Oraliq nuqtalarni o'lchash", [
  "Sxemada nazorat nuqtalarini oldindan belgilang: bu yerda qancha kuchlanish kutilyapti.",
  "O'lchangan va kutilgan qiymatni yonma-yon yozing.",
  "Farq boshlangan joy — muammo shu yerda yoki undan oldin.",
  "Signal zanjirining boshidan oxirigacha yurib chiqish eng ishonchli usul.",
 ]),
 ("Vaqtga bog'liq nosozliklar", [
  "Ba'zi xatolar darhol chiqmaydi: bir necha daqiqadan keyin qizish, kuchlanish cho'kishi, kontakt bo'shashi.",
  "Shuning uchun uzoq muddat sinov (10-30 daqiqa) alohida o'tkaziladi.",
  "Vaqti-vaqti bilan chiqadigan xato eng qiyin turi: uni ushlash uchun sharoitni aniq yozib borish kerak.",
  "Ko'p hollarda sabab yomon kontakt bo'lib chiqadi — simlarni bosib ko'rish bilan tekshiriladi.",
 ]),
),

"Nosozlik topish: tizimli yondashuv": D(
 ("Tizimli yondashuv nima", [
  "Tasodifiy tekshirish o'rniga oldindan tuzilgan REJA bo'yicha ishlash.",
  "Reja: qaysi tartibda nima tekshiriladi va har birida nima kutiladi.",
  "Bu vaqtni tejaydi va bir joyni ikki marta tekshirishning oldini oladi.",
  "Muhandislikda aynan shunday ishlanadi va bu ko'nikma dasturlashda ham bir xil ishlaydi.",
 ]),
 ("Gipoteza va tekshiruv", [
  "1) Nosozlik belgisini aniq yozing: \"LED umuman yonmaydi\" yoki \"xira yonadi\".",
  "2) Sababi haqida GIPOTEZA tuzing: \"rezistor juda katta bo'lishi mumkin\".",
  "3) Gipotezani TEKSHIRADIGAN o'lchov o'ylab toping: rezistorni o'lchash yoki tokni o'lchash.",
  "4) O'lchang va xulosa chiqaring: gipoteza tasdiqlandimi.",
  "5) Tasdiqlanmasa — keyingi gipotezaga o'ting.",
  "Bu ilmiy usulning aynan o'zi va u har qanday sohada ishlaydi.",
 ]),
),

"Xatolik xabarlarini o'qish": D(
 ("Xato xabarini o'qish tartibi", [
  "Xabarning ENG BIRINCHISINI o'qing — qolganlari ko'pincha uning oqibati.",
  "Fayl nomi va QATOR RAQAMI ko'rsatiladi — avval o'sha qatorga qarang.",
  "Xato ko'rsatilgan qatorda emas, undan BIR QATOR YUQORIDA bo'lishi mumkin (masalan nuqta-vergul tushib qolgan).",
  "Xabarni tarjima qilib tushunishga urinish kerak, uni shunchaki o'tkazib yuborish emas.",
 ]),
 ("Eng ko'p uchraydigan xabarlar", [
  "\"expected ';' before ...\" — oldingi qatorda nuqta-vergul yo'q.",
  "\"'x' was not declared in this scope\" — o'zgaruvchi e'lon qilinmagan yoki nomi xato yozilgan.",
  "\"expected '}' at end of input\" — qavs yopilmagan.",
  "\"redefinition of 'x'\" — bir nom ikki marta e'lon qilingan.",
  "\"no matching function for call\" — funksiyaga noto'g'ri sondagi yoki turdagi parametr berilgan.",
  "\"Port not found\" yoki \"not in sync\" — bu kod xatosi emas, ulanish muammosi.",
 ]),
 ("Xatolarni kamaytirish", [
  "Kodni bo'lak-bo'lak yozib, har safar Verify bosish — xato faqat oxirgi yozilgan qismda bo'ladi.",
  "Qavslarni juft-juft yozish: ochganda darhol yopish, keyin ichini to'ldirish.",
  "Avtomatik formatlash (Ctrl+T) — noto'g'ri joylashgan qavs shunda darhol ko'rinadi.",
  "Xato xabarini tushunmasangiz — uni internetda qidirish oddiy va samarali usul.",
 ]),
),

# ============================================================ MIKROKONTROLLER
"Mikrokontroller nima: yangi tushuncha": D(
 ("Mikrokontroller nima", [
  "Mikrokontroller — bitta mikrosxemaga joylashtirilgan kichik kompyuter.",
  "Ichida: protsessor (hisoblaydi), xotira (dastur va ma'lumot saqlaydi), kirish-chiqish pinlari (tashqi dunyo bilan bog'lanadi).",
  "Kompyuterdan farqi: u BITTA dastur bajaradi, operatsion tizimi yo'q va quvvat berilishi bilan darhol ishlaydi.",
  "Arduino Uno dagi ATmega328P: 16 MHz, 32 KB flesh, 2 KB RAM, 20 pin.",
  "Solishtirish uchun oddiy telefon protsessori undan minglab barobar tez va million barobar ko'p xotiraga ega.",
 ]),
 ("Oddiy zanjirdan farqi", [
  "Oddiy zanjirda mantiq SIMLAR bilan belgilanadi: yangi xatti-harakat uchun sxemani qayta yig'ish kerak.",
  "Mikrokontrollerda mantiq DASTURDA: sxemani o'zgartirmasdan xatti-harakatni butunlay boshqa qilish mumkin.",
  "Bu eng katta afzallik: bitta sxema o'nlab turli vazifani bajarishi mumkin.",
  "Ikkinchi afzallik: vaqt bilan ishlash (kechikish, taymer, sanoq), xotira, murakkab mantiq.",
  "Kamchiligi: dastur yozish kerak va u ham xato qilishi mumkin.",
 ]),
),

"Mikrokontroller nima va nimasi bilan farq qiladi": D(
 ("Ichki tuzilishi", [
  "PROTSESSOR (CPU) — buyruqlarni bajaradi. Chastotasi 16 MHz — sekundiga 16 million amal.",
  "FLESH XOTIRA — dastur saqlanadi. Quvvat o'chsa ham saqlanib qoladi (32 KB).",
  "RAM — ish xotirasi, o'zgaruvchilar shu yerda. Quvvat o'chsa yo'qoladi (2 KB).",
  "EEPROM — sozlamalarni saqlash uchun kichik doimiy xotira (1 KB).",
  "PERIFERIYA — ADC, PWM generatori, taymerlar, UART, I2C, SPI.",
 ]),
 ("Nima uchun 2 KB RAM yetadi", [
  "Mikrokontroller katta ma'lumot bilan ishlamaydi — u sensor o'qiydi va chiqishni boshqaradi.",
  "Bitta int o'zgaruvchi 2 bayt, ya'ni 2 KB da 1000 ta int sig'adi.",
  "Lekin uzun matn (String) va katta massivlar xotirani tez to'ldiradi.",
  "Xotira tugasa dastur g'alati ishlay boshlaydi yoki qayta yuklanadi — buni topish qiyin.",
  "Shuning uchun matn o'rniga F() makrosi ishlatiladi: Serial.println(F(\"matn\")) — matn flesh xotirada qoladi.",
 ]),
 ("Boshqa platalar bilan solishtirish", [
  "Arduino Uno: 16 MHz, 2 KB RAM. Oddiy vazifalar uchun.",
  "ESP32: 240 MHz, 520 KB RAM, WiFi va Bluetooth. IoT uchun.",
  "Raspberry Pi: to'liq kompyuter, operatsion tizim bilan. Kamera, video, murakkab dasturlar uchun.",
  "Vazifaga qarab tanlanadi: LED miltillatish uchun ESP32 olish — resursni behuda sarflash.",
 ]),
),

"Birinchi blok: platani yoqish": D(
 ("Birinchi ulanish tartibi", [
  "1) USB kabelni plataga va kompyuterga ulang.",
  "2) Platadagi quvvat indikatori (ON yoki PWR) yonishi kerak.",
  "3) Kompyuter yangi qurilmani aniqlashi kerak.",
  "4) Dasturiy muhitda port ro'yxatida yangi port paydo bo'ladi.",
  "5) Plata turini tanlang.",
  "Indikator yonmasa — kabel faqat quvvat uchunmi yoki ma'lumot uchun hammi tekshiring: ba'zi arzon kabellarda ma'lumot simlari yo'q.",
 ]),
 ("Birinchi dastur", [
  "Birinchi dastur DOIM eng oddiysi bo'lishi kerak: ichki diodni miltillatish.",
  "Sababi: unda hech qanday tashqi sim yo'q, demak xato faqat ulanishda bo'lishi mumkin.",
  "Bu ishlagach, tashqi LED qo'shiladi.",
  "Har bosqichda faqat bitta yangi narsa qo'shish — nosozlik topishning asosiy qoidasi.",
 ]),
),

"Kompyuterga ulash va drayver": D(
 ("USB-Serial ko'prigi", [
  "Mikrokontroller USB bilan bevosita gaplasha olmaydi — orada maxsus mikrosxema turadi.",
  "Original Arduino'da bu ATmega16U2, arzon nusxalarda CH340 yoki CP2102.",
  "Bu mikrosxema USB signalini oddiy Serial (UART) signaliga aylantiradi.",
  "Har bir turi uchun O'Z DRAYVERI kerak — shuning uchun ba'zi platalar ulanganda kompyuter ularni ko'rmaydi.",
 ]),
 ("Drayver muammolarini hal qilish", [
  "Port ro'yxatda ko'rinmasa — drayver o'rnatilmagan.",
  "Plataga qarab drayverni aniqlang: CH340 (arzon nusxalar), CP2102 (ba'zi ESP32), FTDI.",
  "Drayver o'rnatilgandan keyin kompyuterni qayta yuklash kerak bo'lishi mumkin.",
  "Port ko'rinsa ham yuklash bo'lmasa: boshqa dastur portni band qilib turgan bo'lishi mumkin (Serial monitor ochiq qolgan).",
  "Kabelni almashtirib ko'rish — eng oson va eng ko'p yordam beradigan tekshiruv.",
 ]),
),

# ============================================================ BLOKLI DASTURLASH
"Blokli dasturlash muhiti (mBlock) bilan tanishuv": D(
 ("Muhit qismlari", [
  "BLOKLAR PANELI — chap tomonda, kategoriyalarga bo'lingan (Harakat, Ko'rinish, Boshqaruv, Sensorlar).",
  "ISH MAYDONI — o'rtada, bloklar shu yerga tortib olib kelinadi.",
  "QURILMA PANELI — plata ulanadi va tanlanadi.",
  "Bloklar rangi kategoriyaga mos: boshqaruv sariq, sensorlar ko'k, harakat to'q ko'k.",
  "Bloklar shakli ham ma'noli: shartga mos keladigan blok olti burchakli, qiymat qaytaradiganlari oval.",
 ]),
 ("Bloklarning afzalliklari", [
  "Sintaksis xatosi BO'LMAYDI: mos kelmaydigan bloklar shunchaki birlashmaydi.",
  "Nuqta-vergul, qavs va katta-kichik harf muammosi yo'q.",
  "Blok nomlari o'z tilida — bu boshlang'ich bosqichda muhim.",
  "Shuning uchun 5-6-sinfda blokdan boshlanadi va keyin matnli kodga o'tiladi.",
 ]),
 ("Cheklovlari", [
  "Katta dastur bloklarda juda uzun va tushunarsiz bo'lib ketadi.",
  "Hamma kutubxona qo'llab-quvvatlanmaydi.",
  "Ishlab chiqarishda matnli kod ishlatiladi, shuning uchun oxir-oqibat unga o'tish kerak.",
  "Bloklar — bu bosqich, maqsad emas.",
 ]),
),

"Blokli va matnli dasturlash: solishtirish": D(
 ("Bir vazifa — ikki ko'rinish", [
  "Blokli: <boshlanganda> <doim takrorla> <D9 ni yoq> <1 s kut> <D9 ni o'chir> <1 s kut>",
  "Matnli: void setup(){pinMode(9,OUTPUT);} void loop(){digitalWrite(9,HIGH);delay(1000);digitalWrite(9,LOW);delay(1000);}",
  "Mantiq AYNAN bir xil, faqat yozilishi boshqacha.",
  "\"boshlanganda\" bloki = setup(), \"doim takrorla\" bloki = loop().",
 ]),
 ("Har birining o'rni", [
  "Blokli: g'oyani tez sinash, boshlang'ich o'rganish, sintaksisdan chalg'imaslik.",
  "Matnli: katta loyihalar, kutubxonalar, aniq nazorat, kasbiy ish.",
  "Solishtirish mezoni: bir xil dastur bloklarda 15 ta blok, matnda 8 qator bo'lishi mumkin.",
  "Lekin murakkab dasturda nisbat teskari bo'ladi: 100 blok o'rniga 30 qator kod.",
 ]),
 ("O'tish qanday bo'ladi", [
  "Ko'p blokli muhitlarda \"kodni ko'rish\" tugmasi bor — u yig'ilgan blokning matnli ko'rinishini ko'rsatadi.",
  "Eng samarali usul: blokda yig'ib, keyin uning kod ko'rinishiga qarab, ikkalasini solishtirish.",
  "Keyingi bosqichda ayni vazifani matnda mustaqil yozib, blokli variant bilan tekshirish.",
  "Shu tartibda o'tish sezilmay va qiyinchiliksiz bo'ladi.",
 ]),
),

"Blok bilan tovush va harakatni birlashtirish": D(
 ("Bir vaqtda bir necha chiqishni boshqarish", [
  "Bloklar yuqoridan pastga KETMA-KET bajariladi — ular bir vaqtda ishlamaydi.",
  "\"Bir vaqtda\" ta'siri tez almashtirish bilan hosil qilinadi: LEDni yoqib, zummerni chalib, keyin motorni burish.",
  "Bu shunchalik tez sodir bo'ladiki, ko'z va quloq buni bir vaqtda deb qabul qiladi.",
  "Lekin \"kut\" bloki ishlaganda hamma narsa TO'XTAYDI — bu asosiy cheklov.",
 ]),
 ("Kutish blokisiz ishlash", [
  "Uzun kutish o'rniga taymer o'zgaruvchisi ishlatiladi: har aylanishda vaqt tekshiriladi.",
  "Bu matnli koddagi millis() usulining blokli varianti.",
  "Shunda tovush chalinayotganda ham sensorni o'qish va tugmani tekshirish mumkin bo'ladi.",
  "Bu tushuncha keyin matnli dasturlashda ham eng muhimlaridan biri bo'ladi.",
 ]),
),

# ============================================================ TOVUSH
"Tovush: chastota va baland-pastlik": D(
 ("Tovush qanday hosil bo'ladi", [
  "Tovush — havodagi bosim tebranishi. Biror jism tebransa, u havoni siqib-bo'shatadi.",
  "Bu siqilish to'lqin bo'lib tarqaladi va quloq pardasini tebratadi.",
  "Chastota — sekundiga necha marta tebranish. Gerts (Hz) da o'lchanadi.",
  "Inson eshitadigan oraliq: 20 Hz dan 20 000 Hz gacha. Yosh o'tgan sari yuqori chegara pasayadi.",
 ]),
 ("Chastota va nota", [
  "Chastota katta — tovush INGICHKA (baland). Kichik — YO'G'ON (past).",
  "Nota chastotalari: do 262, re 294, mi 330, fa 349, sol 392, lya 440, si 494, do2 523 Hz.",
  "Bir oktava yuqori nota chastotasi ROSA IKKI BARAVAR katta: lya 440, keyingi lya 880 Hz.",
  "Shuning uchun oktava — musiqadagi eng tabiiy bo'linish: quloq ikki barobar farqni \"bir xil nota\" deb eshitadi.",
  "Lya 440 Hz — xalqaro sozlash standarti, hamma cholg'u shunga sozlanadi.",
 ]),
 ("Balandlik va tembr", [
  "Tovush BALANDLIGI (qanchalik kuchli) chastota emas, TEBRANISH KENGLIGIGA bog'liq.",
  "Chastota — bu ingichka/yo'g'onlik (musiqada \"baland-past nota\").",
  "Bu ikkisi ko'pincha chalkashtiriladi — ularni aniq ajratish kerak.",
  "Tembr — bir xil notani skripka va pianino turlicha eshittiradi. Bu qo'shimcha chastotalar (obertonlar) tufayli.",
  "Passiv zummer faqat toza chastota beradi, shuning uchun uning tovushi \"quruq\" eshitiladi.",
 ]),
),

# ============================================================ KORPUS VA LOYIHA
"Prototipdan korpusli qurilmaga": D(
 ("Prototip va tayyor qurilma farqi", [
  "Prototip: breadboard, uzun simlar, ochiq elementlar. Maqsad — g'oyani sinash.",
  "Tayyor qurilma: mahkam montaj, korpus, ishonchli kontaktlar. Maqsad — uzoq va xavfsiz ishlash.",
  "Prototipdan tayyor qurilmaga o'tish alohida bosqich va u odatda kutilganidan ko'p vaqt oladi.",
  "Muhim qoida: prototip TO'LIQ ishlagandan keyingina korpusga o'tiladi.",
 ]),
 ("O'tish bosqichlari", [
  "1) Prototipni to'liq sinang va hamma kamchilikni tuzating.",
  "2) Sxemani yakuniy holda chizib oling.",
  "3) Komponentlarni joylashuvini rejalashtiring: nima qayerda turadi.",
  "4) Breadboard o'rniga makon platasiga kavsharlang yoki razyomlar bilan ulang.",
  "5) Korpusga joylashtiring va yana sinang.",
  "Har bosqichdan keyin qurilma hali ham ishlayotganini tekshirish shart.",
 ]),
),

"Qurilmani korpusga joylashtirish": D(
 ("Korpusni rejalashtirish", [
  "Avval hamma komponentni stolda korpusdagi kelajakdagi joyiga qo'yib ko'ring.",
  "Teshiklarni belgilang: USB, quvvat, tugmalar, indikatorlar, sensorlar.",
  "Sensorlar TASHQARIGA chiqarilishi kerak: harorat sensori korpus ichida korpus haroratini o'lchaydi.",
  "Isiydigan elementlar uchun havo teshigi qoldiring.",
  "Batareyani almashtirish va kodni qayta yuklash imkoni qolishi kerak.",
 ]),
 ("Mahkamlash", [
  "Plata korpus ichida QIMIRLAMASLIGI kerak: vint, issiq yelim yoki maxsus tayanchlar bilan.",
  "Har bir sim shunday bog'lansinki, tortilganda kontakt emas, bog'lam kuchni ko'tarsin.",
  "Breadboard simlari korpusda ishonchsiz — kavsharlash yoki razyom ishlatish kerak.",
  "Ochiq kontaktlar izolyatsiya lentasi yoki isituvchi naycha bilan yopiladi.",
  "Yopishdan OLDIN to'liq sinov o'tkazing.",
 ]),
 ("Material tanlash", [
  "Karton — tez prototip uchun, bir necha daqiqada kesiladi. Namlikka chidamsiz.",
  "Tayyor plastik quti — arzon va mustahkam, faqat teshik teshish kerak.",
  "Fanera yoki organik shisha — chiroyli, lekin asbob kerak.",
  "3D bosma — eng aniq va professional, lekin loyihalash va bosish vaqti oladi.",
  "Maktab loyihasi uchun tayyor plastik quti eng amaliy variant.",
 ]),
),

"Qurilmani loyihalash bosqichlari": D(
 ("To'liq sikl", [
  "1) MUAMMO: nima hal qilinadi va kimga kerak.",
  "2) TALABLAR: qurilma nima qilishi kerak, o'lchanadigan qilib yozilgan.",
  "3) YECHIM VARIANTLARI: kamida uchta, solishtirilgan.",
  "4) SXEMA VA KOMPONENTLAR: tanlangan va asoslangan.",
  "5) PROTOTIP: yig'ilgan va sinalgan.",
  "6) TUZATISH: kamchiliklar bartaraf etilgan.",
  "7) KORPUS VA MONTAJ: tayyor ko'rinishga keltirilgan.",
  "8) HUJJAT VA TAQDIMOT.",
 ]),
 ("Bosqichlarni o'tkazib yubormaslik", [
  "Eng ko'p uchraydigan xato — 1, 2, 3-bosqichni o'tkazib, darhol yig'ishga kirishish.",
  "Natijada qurilma yig'iladi, lekin u kerakli vazifani bajarmaydi yoki mos komponent tanlanmagan bo'ladi.",
  "Rejalashtirishga ketgan bir soat yig'ishda uch soatni tejaydi.",
  "Sikl chiziqli emas: sinovda topilgan muammo sizni 2 yoki 3-bosqichga qaytarishi mumkin. Bu normal.",
 ]),
),

"Elektr xavfsizligi: nima mumkin, nima mumkin emas": D(
 ("Nima uchun tok xavfli", [
  "Xavfli bo'lgan narsa kuchlanish emas, TOK. Tananing qarshiligi tokni belgilaydi.",
  "Quruq teri qarshiligi ~100 kOm, nam teri ~1 kOm — yuz barobar farq.",
  "1 mA — sezilarli. 10 mA — mushak qisqarishi, qo'lni tortib ololmaslik. 50 mA dan yuqori — hayot uchun xavfli.",
  "220 V va 1 kOm qarshilikda: I = 220 / 1000 = 220 mA — bu o'lim xavfi.",
  "5 V va 100 kOm qarshilikda: I = 0,05 mA — umuman sezilmaydi.",
  "Shuning uchun darsda 3,3-9 V bilan ishlash xavfsiz, 220 V esa taqiqlangan.",
 ]),
 ("Darsda majburiy qoidalar", [
  "220 V bilan ishlash faqat o'qituvchi qo'li bilan va faqat namoyish tarzida.",
  "Zanjirni o'zgartirishdan OLDIN quvvat uziladi.",
  "Ho'l qo'l bilan hech qanday elektr qurilmasiga tegilmaydi.",
  "Batareya qutblari bevosita tutashtirilmaydi.",
  "Qizigan komponent ushlanmaydi.",
  "Elektrolit kondensatorni teskari ulash taqiqlanadi (yorilishi mumkin).",
  "Lazer nuriga qaralmaydi.",
  "Buzilgan jihoz haqida darhol o'qituvchiga aytiladi.",
 ]),
 ("Yong'in xavfsizligi", [
  "Sim qizishining sababi — ortiqcha tok. Buni sezish uchun ishlayotgan sxemani vaqti-vaqti bilan tekshirish kerak.",
  "Hid (kuygan plastmassa hidi) — darhol quvvatni uzish signali.",
  "Tutun chiqsa — quvvat uziladi va o'qituvchi chaqiriladi. Suv quyilmaydi.",
  "Li-ion akkumulyator shishsa — unga tegilmaydi, o'qituvchi chaqiriladi.",
 ]),
),

"Komponentni to'g'ri tanlash: katalogdan": D(
 ("Katalogdan qidirish tartibi", [
  "1) Vazifani aniq yozing: nima o'lchanadi yoki nima boshqariladi.",
  "2) Kerakli oraliq va aniqlikni belgilang.",
  "3) Ta'minot kuchlanishini aniqlang: 3,3 V yoki 5 V.",
  "4) Interfeysni tanlang: analog, raqamli, I2C, SPI.",
  "5) Katalogdan shu shartlarga mos komponentlarni toping.",
  "6) Kamida ikkitasini solishtiring va tanlovni asoslang.",
 ]),
 ("Solishtirish jadvali", [
  "Ustunlar: parametr, 1-variant, 2-variant, qaysi biri afzal.",
  "Qatorlar: o'lchov oralig'i, aniqlik, ta'minot, tok, interfeys, narx, mavjudlik.",
  "Har bir qatorda qaysi variant yaxshiroq ekanini belgilang.",
  "Yakunda tanlov bir gapda asoslanadi: \"issiqxona uchun DHT22 tanlandi, chunki 1 daraja aniqlik muhim va DHT11 buni bermaydi\".",
 ]),
),

"Komponentni katalog (datasheet) bo'yicha tanlash": D(
 ("Datasheet tuzilishi", [
  "Birinchi sahifa — qisqacha tavsif va asosiy parametrlar. Ko'pincha shu yetadi.",
  "Absolute Maximum Ratings — MUTLAQ chegaralar. Ulardan oshsa komponent buziladi.",
  "Electrical Characteristics — normal ish sharoitidagi parametrlar.",
  "Pin Configuration — oyoqlar xaritasi.",
  "Typical Application — namunaviy ulanish sxemasi. Eng foydali qism.",
  "Grafiklar — parametrlarning harorat va kuchlanishga bog'liqligi.",
 ]),
 ("Nimaga birinchi qarash kerak", [
  "Ta'minot kuchlanishi: platangizga mos keladimi.",
  "Iste'mol toki: manbangiz yetadimi.",
  "O'lchov oralig'i: kerakli qiymatlarni qamrab oladimi.",
  "Aniqlik: vazifaga yetarlimi.",
  "Ish harorati: qurilma qayerda ishlaydi.",
  "Interfeys: qanday ulanadi va kutubxona bormi.",
  "Bu olti parametrni jadvalga chiqarish — datasheet bilan ishlashning asosiy ko'nikmasi.",
 ]),
),

"Multimetr: qarshilik va tokni o'lchash": D(
 ("Qarshilik o'lchash", [
  "Zanjirda kuchlanish BO'LMASLIGI kerak — quvvat uziladi.",
  "Element zanjirdan chiqariladi yoki bir oyog'i uziladi: aks holda parallel yo'llar natijani buzadi.",
  "Shchuplarni barmoq bilan ushlab turmang — tananing qarshiligi qo'shiladi.",
  "\"OL\" yoki \"1\" — qarshilik oraliqdan katta yoki zanjir uzilgan.",
  "Nol — qisqa tutashuv yoki oddiy o'tkazgich.",
 ]),
 ("Tok o'lchash", [
  "Zanjir UZILADI va multimetr o'sha joyga ketma-ket qo'yiladi.",
  "Qizil shchup mA (yoki 10A) uyasiga ko'chiriladi.",
  "O'lchov tugagach shchupni V uyasiga QAYTARISH shart — bu eng muhim odat.",
  "Tok rejimida multimetrni manbaga parallel ulash — qisqa tutashuv va predoxranitelning kuyishi.",
  "Motor tokini o'lchashda mA uyasi yetmasligi mumkin, 10A uyasi ishlatiladi.",
 ]),
 ("Ikkalasini bir zanjirda mashq qilish", [
  "LED zanjirini yig'ing: batareya, rezistor, LED.",
  "Avval quvvatsiz rezistorni chiqarib olib qarshiligini o'lchang.",
  "Keyin zanjirni yig'ib, tokni o'lchang.",
  "Om qonuni bilan hisoblang va o'lchov bilan solishtiring.",
  "Rezistorni boshqasiga almashtirib, tok qanday o'zgarishini kuzating.",
 ]),
),

"Taqdimot: o'z qurilmangni tushuntirish": D(
 ("Uch daqiqalik tuzilma", [
  "30 sekund — MUAMMO: nima uchun bu qurilma kerak.",
  "45 sekund — YECHIM: u nima qiladi va qanday ishlaydi.",
  "60 sekund — NAMOYISH: qurilma jonli ishlatib ko'rsatiladi.",
  "45 sekund — NATIJA VA CHEKLOVLAR: nima ishladi, nima ishlamadi.",
  "Namoyish — eng muhim qism va u hech qachon qisqartirilmaydi.",
 ]),
 ("Qanday gapirish kerak", [
  "Texnik atamani ishlatsangiz, uni bir gapda izohlang.",
  "\"Men shuni qildim\" emas, \"qurilma shuni qiladi\" deb gapiring — diqqat natijaga qaratiladi.",
  "Raqam bilan gapirish eng ishonchli: \"20 sinovdan 18 tasi to'g'ri chiqdi\".",
  "Kamchilikni ochiq ayting — bu ishonchni oshiradi, kamaytirmaydi.",
  "Matnni yod olmang, tezislar yozing va ular bo'yicha gapiring.",
 ]),
 ("Namoyishga tayyorgarlik", [
  "Kamida uch marta mashq qiling va vaqtni sekundomer bilan o'lchang.",
  "Zaxira reja: qurilma ishlamay qolsa oldindan yozilgan video ko'rsatiladi.",
  "Quvvat manbai, kabel va zaxira komponentlarni oldindan tayyorlab qo'ying.",
  "Namoyish paytida sozlash yoki tuzatish bilan shug'ullanmang — hammasi oldindan tayyor bo'lsin.",
 ]),
),

# ============================================================ ARDUINO LOYIHA
"Bir nechta sensorli tizim": D(
 ("Bir necha sensorni birlashtirish muammolari", [
  "PIN YETISHMASLIGI: har bir sensor pin talab qiladi. Yechim — I2C (bitta shinada bir necha qurilma).",
  "VAQT MASALASI: DHT22 sekundiga bir marta o'qiladi, HC-SR04 esa tez-tez. delay ishlatilsa ular bir-biriga xalaqit beradi.",
  "QUVVAT: sensorlar yig'indisi plata imkoniyatidan oshib ketishi mumkin.",
  "XALAQIT: bir sensor ishlaganda ikkinchisining ko'rsatkichi buzilishi mumkin (masalan motor shovqini).",
 ]),
 ("Yechim: har bir sensorga o'z ritmi", [
  "delay() o'rniga millis() ishlatiladi va har bir sensor uchun alohida taymer yuritiladi.",
  "Har bir sensor o'z oralig'ida o'qiladi: DHT22 — 2000 ms, masofa — 200 ms, fotorezistor — 50 ms.",
  "Natijalar o'zgaruvchilarda saqlanadi va kerak bo'lganda ishlatiladi.",
  "Chiqarish ham alohida ritmda bo'ladi (masalan sekundiga bir marta).",
  "Bu tuzilma katta loyihalarning asosi va uni bir marta o'rganish yetarli.",
 ]),
),

"Sensor qiymatlarini tahlil qilish": D(
 ("Xom qiymatdan xulosaga", [
  "Bitta o'lchov — shunchaki son. Xulosa chiqarish uchun kamida uch narsa kerak: TARIX, O'RTACHA va TENDENSIYA.",
  "O'rtacha — tasodifiy shovqinni yo'qotadi.",
  "Eng katta va eng kichik — o'zgarish diapazonini ko'rsatadi.",
  "Tendensiya — qiymat ortyaptimi yoki kamayyaptimi. Oxirgi va oldingi o'rtachani solishtirish bilan topiladi.",
 ]),
 ("Amaliy tahlil usullari", [
  "Siljuvchi o'rtacha: oxirgi N qiymatni massivda saqlab, ularning o'rtachasini hisoblash.",
  "Eksponensial silliqlash: yangi = a x o'lchov + (1-a) x eski. Xotira kam talab qiladi.",
  "Chetlarni tashlab yuborish: eng katta va eng kichikni olib tashlab, qolganining o'rtachasini olish.",
  "O'zgarish tezligi: (yangi - eski) / vaqt. Keskin o'zgarishni aniqlash uchun.",
  "Bu usullar keyin AI bosqichida \"belgi ajratish\" nomi bilan qaytadan uchraydi.",
 ]),
),

"Qurilmani yaxshilash: qo'shimcha imkoniyat": D(
 ("Nimani qo'shish kerakligini aniqlash", [
  "Yaxshilash tasodifiy emas, EHTIYOJDAN kelib chiqishi kerak.",
  "Foydalanuvchi (yoki sinfdosh) qurilmani ishlatib ko'rsin va qiynalgan joyini aytsin.",
  "Sinov jadvalidagi kamchiliklar ham manba bo'ladi.",
  "Har bir taklif uchun ikki savol: bu qancha vaqt oladi va u qanchalik foydali.",
  "Kam vaqt va ko'p foyda beradiganlari birinchi qilinadi.",
 ]),
 ("Tipik yaxshilashlar", [
  "Indikator qo'shish: qurilma ishlayotganini yoki xato borligini ko'rsatish.",
  "Sozlash imkoniyati: chegarani potensiometr yoki tugma bilan o'zgartirish.",
  "Xotira: sozlamalarni EEPROM ga saqlab, quvvat o'chsa ham yo'qotmaslik.",
  "Ekran qo'shish: qurilmani kompyuterdan mustaqil qilish.",
  "Xatolikka chidamlilik: sensor javob bermasa ham qurilma qotib qolmasin.",
 ]),
 ("Yaxshilashning chegarasi", [
  "Har bir yangi imkoniyat yangi xato manbai ham bo'ladi.",
  "Taqdimotga bir dars qolganda yangi funksiya QO'SHILMAYDI.",
  "Ishlaydigan sodda qurilma ishlamaydigan murakkab qurilmadan yaxshiroq.",
  "Qo'shilmagan g'oyalar hujjatda \"kelajakdagi rejalar\" bo'limiga yoziladi — bu ham natija.",
 ]),
),

"Simlarni tartibga solish": D(
 ("Nima uchun bu muhim", [
  "Chalkash simlar xatoni yashiradi va nosozlik topishni bir necha barobar sekinlashtiradi.",
  "Osilgan uzun sim tortilib kontaktni uzadi — vaqti-vaqti bilan chiqadigan eng yomon turdagi xato hosil bo'ladi.",
  "Tartibli sxemani suratga olib hujjatga qo'yish mumkin.",
  "Taqdimotda tartibli qurilma jiddiy taassurot qoldiradi.",
 ]),
 ("Amaliy usullar", [
  "Simni kerakli uzunlikda kesish — ortiqcha uzunlik faqat xalaqit beradi.",
  "Rang kodini saqlash: qizil plyus, qora GND, qolganlari signal.",
  "Bir yo'nalishdagi simlarni bog'lam qilib bog'lash (styajka yoki spiral naycha bilan).",
  "Quvvat va signal simlarini alohida yo'ldan yuritish — shovqin kamayadi.",
  "Har bir simning ikki uchiga bir xil belgi yopishtirish — keyin qaysi sim qayerga ketishi darhol ko'rinadi.",
 ]),
),

"Loyihani hujjatlashtirish": D(
 ("Hujjatning majburiy qismlari", [
  "Loyiha nomi, muallif, sana.",
  "Muammo va yechim — bir sahifada, sodda tilda.",
  "Komponentlar ro'yxati: nom, miqdor, taxminiy narx.",
  "Printsipial sxema: pin raqamlari bilan.",
  "Kod: izohlar bilan.",
  "Sinov natijalari jadvali.",
  "Kamchiliklar va kelajakdagi rejalar.",
 ]),
 ("Hujjatning sinovi", [
  "Asosiy mezon: boshqa jamoa shu hujjat bilan loyihani QAYTA yig'a oladimi.",
  "Sxemada pin raqamlari yo'q bo'lsa — hujjat yaroqsiz.",
  "Kalibrlash qiymatlari yozilmagan bo'lsa — qurilma boshqa nusxada ishlamaydi.",
  "Kutubxona nomlari va versiyalari ko'rsatilmagan bo'lsa — kod kompilyatsiya qilinmaydi.",
  "Hujjatni sinfdoshga berib tekshirtirish — eng ishonchli sinov.",
 ]),
),

# ============================================================ ESP32 LOYIHA
"WiFi va tarmoq asoslari (takrorlash va chuqurlashtirish)": D(
 ("Tarmoq qanday ishlaydi", [
  "Router — tarmoqning markazi. U har bir qurilmaga IP manzil beradi (DHCP orqali).",
  "IP manzil — tarmoqdagi qurilmaning raqamli manzili, masalan 192.168.1.42.",
  "Maska (255.255.255.0) — qaysi manzillar bir tarmoqda ekanini belgilaydi.",
  "Shlyuz (gateway) — tashqi dunyoga chiqish nuqtasi, odatda router manzili.",
  "DNS — sayt nomini IP manzilga aylantiruvchi xizmat.",
 ]),
 ("Portlar va protokollar", [
  "IP manzil uyning manzili bo'lsa, PORT — o'sha uydagi xona raqami.",
  "Bitta qurilmada bir necha xizmat ishlashi mumkin, har biri o'z portida.",
  "Standart portlar: HTTP — 80, HTTPS — 443, MQTT — 1883.",
  "Protokol — gaplashish qoidalari: HTTP so'rov-javob, MQTT esa obuna asosida ishlaydi.",
 ]),
 ("Signal kuchi", [
  "RSSI dBm da o'lchanadi va u MANFIY son bo'ladi.",
  "-30 dBm — juda kuchli (router yonida). -67 dBm — yaxshi. -80 dBm — kuchsiz. -90 dBm — deyarli yo'q.",
  "Devor, metall va suv signalni susaytiradi.",
  "WiFi.RSSI() bilan o'lchab, xonaning turli nuqtalarida signal kartasini tuzish mumkin.",
 ]),
),

"WiFi xatolarini topish va tuzatish": D(
 ("Ulanmaslik sabablari", [
  "Nom yoki parol xato — eng ko'p uchraydigan sabab. Katta-kichik harf ham muhim.",
  "5 GHz tarmoq: ESP32 faqat 2,4 GHz ni qo'llab-quvvatlaydi.",
  "Signal kuchsiz: routerga yaqinlashtirib sinab ko'ring.",
  "Router MAC filtri yoqilgan.",
  "Tarmoqda qurilmalar soni chegaraga yetgan.",
  "Parolda maxsus belgilar bor va ular kodda noto'g'ri yozilgan.",
 ]),
 ("Diagnostika tartibi", [
  "1) WiFi.status() qiymatini chiqaring — u xato turini ko'rsatadi.",
  "2) WiFi.scanNetworks() bilan tarmoq umuman ko'rinayotganini tekshiring.",
  "3) Ko'rinsa — RSSI ni qarang, kuchsiz bo'lsa masofani kamaytiring.",
  "4) Telefonni shu tarmoqqa ulab, parol to'g'riligini tekshiring.",
  "5) Ulangandan keyin ping qilib ko'ring.",
 ]),
 ("Aloqa uzilishiga chidamlilik", [
  "WiFi doim barqaror emas — dastur bunga tayyor bo'lishi kerak.",
  "loop ichida WiFi.status() muntazam tekshiriladi.",
  "Uzilgan bo'lsa WiFi.reconnect() chaqiriladi.",
  "Bir necha marta tiklanmasa ESP.restart() bilan qurilma qayta yuklanadi.",
  "Watchdog taymer qo'shiladi: dastur qotib qolsa u avtomatik qayta yuklaydi.",
  "Aloqa yo'q paytda ham qurilmaning asosiy vazifasi ishlashda davom etishi kerak.",
 ]),
),

"Vaqt bo'yicha avtomatlashtirish": D(
 ("Vaqt manbalari", [
  "millis() — plata yoqilganidan beri o'tgan vaqt. Quvvat o'chsa noldan boshlanadi.",
  "RTC moduli (DS3231) — haqiqiy sana va vaqtni saqlaydi, batareyasi bor.",
  "NTP (internet orqali) — ESP32 uchun eng qulay: tarmoqdan aniq vaqt olinadi.",
  "NTP afzalligi: qo'shimcha modul kerak emas va vaqt doim aniq bo'ladi.",
  "Kamchiligi: internet kerak. Shuning uchun ba'zan RTC bilan birga ishlatiladi.",
 ]),
 ("Jadval bo'yicha ishlash", [
  "Oddiy jadval: soat va daqiqani tekshirib, belgilangan vaqtda amalni bajarish.",
  "Muhim: amal bir daqiqa davomida ko'p marta bajarilib ketmasligi uchun bayroq qo'yiladi.",
  "Haftaning kunini hisobga olish: dayOfTheWeek() bilan dam olish kunlarini ajratish.",
  "Vaqt zonasi: NTP dan UTC keladi, mahalliy vaqtga aylantirish uchun siljish qo'shiladi (Toshkent uchun +5 soat).",
  "Yozgi vaqtga o'tish bo'lsa uni ham hisobga olish kerak.",
 ]),
),

"Tizimni sinovdan o'tkazish": D(
 ("Sinov turlari", [
  "FUNKSIONAL sinov: har bir talab bajarilyaptimi.",
  "CHEGARAVIY sinov: eng past va eng baland qiymatlarda nima bo'ladi.",
  "XATO sinovi: sensor uzilsa, WiFi yo'qolsa, quvvat cho'ksa qurilma nima qiladi.",
  "UZOQ MUDDAT sinovi: bir necha soat uzluksiz ishlatish.",
  "FOYDALANUVCHI sinovi: boshqa odam qo'llanma bilan qurilmani ishlata oladimi.",
 ]),
 ("Sinov protokoli", [
  "Har bir sinov uchun: nomi, qadamlar, kutilgan natija, haqiqiy natija, xulosa.",
  "Xulosa faqat \"o'tdi\" yoki \"o'tmadi\" bo'ladi — oraliq baho yo'q.",
  "O'tmagan sinovlar ro'yxat qilinadi va muhimlik bo'yicha tartiblanadi.",
  "Tuzatishdan keyin BUTUN protokol qaytariladi, faqat tuzatilgan joy emas.",
  "Bu protokol loyiha hujjatining eng qimmatli qismi bo'ladi.",
 ]),
),

"Tizimni sinash va nosozliklarni yo'qotish": D(
 ("Uzoq muddat sinovi", [
  "Ko'p xatolar faqat uzoq ishlaganda chiqadi va ularni qisqa sinovda topib bo'lmaydi.",
  "Xotira oqishi: har aylanishda ozgina xotira band qilinadi va bir necha soatda u tugaydi.",
  "millis() to'lib ketishi: taxminan 50 kundan keyin u nolga qaytadi. Ayirish orqali yozilgan kod bunga chidaydi.",
  "Sensor qizishi: uzoq ishlaganda ko'rsatkich suzib ketadi.",
  "Kontakt bo'shashi: qizish va sovish tsikllari simni bo'shatadi.",
 ]),
 ("Kuzatuv qo'yish", [
  "Dasturga hisoblagichlar qo'shing: necha marta qayta ulandi, necha xato bo'ldi, qancha vaqt ishladi.",
  "ESP.getFreeHeap() ni muntazam chiqaring — u kamayib borsa xotira oqishi bor.",
  "Muhim hodisalarni SD kartga yoki bulutga yozib boring.",
  "Sinov tugagach bu ma'lumotlar tahlil qilinadi va muammo manbai topiladi.",
 ]),
),

"Qurilma korpusi va yakuniy montaj": D(
 ("IoT qurilmasi korpusining talablari", [
  "ANTENNA: ESP32 antennasi metall bilan o'ralmasligi kerak — signal keskin susayadi.",
  "Plastik yoki karton korpus mos, metall qutiga solish esa WiFi ni deyarli o'chiradi.",
  "Antenna atrofida kamida 1 sm bo'sh joy qoldiring.",
  "SENSORLAR tashqarida bo'lsin: harorat va namlik sensori korpus ichida noto'g'ri o'lchaydi.",
  "USB razyomiga kirish qolishi kerak — kodni qayta yuklash uchun.",
 ]),
 ("Quvvat va issiqlik", [
  "ESP32 WiFi bilan ishlaganda sezilarli qiziydi — havo teshigi kerak.",
  "Batareyani almashtirish yoki zaryadlash imkoni qolsin.",
  "Quvvat razyomi mahkam o'rnatilsin — u eng ko'p tortiladigan joy.",
  "Yakuniy montajdan keyin signal kuchini (RSSI) qayta o'lchang: korpus uni qanchalik susaytirganini bilish kerak.",
 ]),
),

"Loyihani taqdim etish va himoya qilish": D(
 ("Texnik himoya tuzilishi", [
  "1) Muammo va uning ahamiyati.",
  "2) Yechim varianti va NIMA UCHUN aynan shu tanlangani.",
  "3) Tizim arxitekturasi: bloklar va ular orasidagi aloqa.",
  "4) Texnik yechimlar: qanday sensor, nima uchun shu chegara, qanday protokol.",
  "5) Jonli namoyish.",
  "6) O'lchangan natijalar: raqamlar bilan.",
  "7) Cheklovlar va kelajakdagi rejalar.",
 ]),
 ("Savollarga tayyorgarlik", [
  "Har bir texnik tanlovni asoslashga tayyor bo'ling: nima uchun bu sensor, nima uchun bu chegara.",
  "\"Boshqa qanday qilish mumkin edi\" savoliga javob tayyorlang — bu eng ko'p beriladigan savol.",
  "Cheklovlarni o'zingiz ayting: baholovchi ularni baribir topadi va oldindan aytilgani ishonch uyg'otadi.",
  "Bilmagan narsani \"bilmayman, lekin uni shunday tekshirish mumkin\" deb aytish — to'g'ri javob.",
  "Raqam bilan javob berish eng kuchli dalil: \"100 sinovdan 94 tasi to'g'ri ishladi\".",
 ]),
),

"Telegram bot: to'liq boshqaruv paneli": D(
 ("To'liq panel talablari", [
  "Boshqaruv: har bir ijro qurilmasi uchun buyruq.",
  "Kuzatuv: hamma sensor qiymatini bir xabarda ko'rsatish.",
  "Ogohlantirish: chegaradan oshganda avtomatik xabar.",
  "Sozlash: chegarani Telegram orqali o'zgartirish.",
  "Tarix: oxirgi hodisalar ro'yxati.",
  "Xavfsizlik: faqat ruxsat berilgan chat ID lar boshqara oladi.",
 ]),
 ("Interfeysni qulay qilish", [
  "Tugmali klaviatura matn yozishdan ancha qulay.",
  "/start buyrug'i doim yordam matnini va tugmalarni ko'rsatsin.",
  "Har bir buyruqqa TASDIQ javobi qaytarilsin — foydalanuvchi buyruq yetganini bilishi kerak.",
  "Xato buyruqqa tushunarli javob berilsin, jim qolmasin.",
  "Uzun ro'yxatlar bo'lsa ularni bo'lib yuborish kerak (Telegram xabar uzunligi cheklangan).",
 ]),
 ("Ishonchlilik", [
  "Bot so'rovlari 1,5-2 sekundda bir marta yuborilsin — tezroq bo'lsa Telegram cheklaydi.",
  "WiFi uzilsa bot qayta ulanishi kerak.",
  "Ogohlantirish xabarlari uchun minimal oraliq qo'yiladi, aks holda spam bo'ladi.",
  "Token kodda ochiq turadi — kodni ulashishdan oldin uni olib tashlash SHART.",
 ]),
),

# ============================================================ AI LOYIHA TAYYORGARLIGI
"Muammoni aniqlash va tadqiq qilish": D(
 ("Yaxshi muammo qanday bo'ladi", [
  "Aniq: kim, qayerda va qanday qiyinchilikka duch keladi.",
  "Tekshiriladigan: muammo hal bo'lganini o'lchash mumkin.",
  "Hal qilinadigan: mavjud jihoz va vaqt bilan uddalanadi.",
  "AI kerak bo'ladigan: oddiy if sharti bilan hal bo'ladigan muammoga model kerak emas.",
  "Yomon misol: \"aqlli uy yasash\". Yaxshi misol: \"ovoz buyrug'i bilan chiroqni yoqish, chunki qo'l band bo'lganda kalitga yetib bo'lmaydi\".",
 ]),
 ("Tadqiq qilish bosqichi", [
  "Muammo haqiqatan bormi — buni tekshirish kerak, taxmin qilish emas.",
  "Kim duch keladi va qanchalik tez-tez.",
  "Hozir bu qanday hal qilinadi va nima uchun bu yetarli emas.",
  "Shunga o'xshash tayyor yechimlar bormi va ularning kamchiligi nima.",
  "Bu ma'lumotlar hujjatga yoziladi va loyiha nima uchun kerakligini asoslaydi.",
 ]),
),

"Foydalanuvchi ehtiyojini o'rganish": D(
 ("Suhbat o'tkazish", [
  "Kamida 3-5 kishi bilan gaplashish kerak — bitta odam fikri yetarli emas.",
  "Ochiq savollar bering: \"Bu ishni qanday bajarasiz?\" — \"Sizga shu qurilma kerakmi?\" emas.",
  "Yopiq savol javobni oldindan taklif qiladi va natija noto'g'ri chiqadi.",
  "Odamlar nima QILISHINI kuzating, nima DEYISHINI emas — bu ikkisi ko'pincha farq qiladi.",
  "Javoblarni o'z so'zlari bilan yozib oling.",
 ]),
 ("Ehtiyojdan talabga o'tish", [
  "Ehtiyoj: \"qo'lim band bo'lganda chiroqni yoqolmayman\".",
  "Talab: \"qurilma 2 metr masofadan aytilgan buyruqni 1 sekund ichida taniy olsin\".",
  "Talab o'lchanadigan bo'lishi shart, aks holda uni tekshirib bo'lmaydi.",
  "Har bir talab ehtiyojdan kelib chiqishi kerak — asossiz talablar loyihani og'irlashtiradi.",
  "Talablarni muhimlik bo'yicha tartiblang: majburiy, kerakli, xohishli.",
 ]),
),

"Loyiha g'oyasini tanlash va rejalashtirish": D(
 ("G'oyalarni baholash", [
  "Kamida 5 g'oya o'ylab toping — birinchisi kamdan-kam eng yaxshisi bo'ladi.",
  "Baholash mezonlari: foydalilik, bajarilishi, mavjud jihoz bilan mosligi, vaqt, qiziqarliligi.",
  "Har bir mezonga 1 dan 5 gacha ball qo'ying va jamlang.",
  "Eng ko'p ball to'plagani tanlanadi, lekin \"bajarilishi\" past bo'lsa u chiqarib tashlanadi.",
  "Tanlov sababi bir gapda yoziladi.",
 ]),
 ("AI loyihasi uchun maxsus mezonlar", [
  "Ma'lumot yig'ish mumkinmi va u qancha vaqt oladi.",
  "Sinflar soni nechta — 2-4 optimal, 10 tasi maktab loyihasi uchun ko'p.",
  "Sinflar bir-biridan yetarlicha farq qiladimi — o'xshash sinflar ko'p ma'lumot talab qiladi.",
  "Mavjud sensor (kamera yoki mikrofon) shu vazifaga mos keladimi.",
  "Model mikrokontrollerga sig'adimi.",
 ]),
),

"Texnik topshiriq yozish": D(
 ("Texnik topshiriq tarkibi", [
  "Loyiha nomi va maqsadi.",
  "Muammo bayoni va foydalanuvchi.",
  "Funksional talablar: qurilma nima qiladi (raqamlangan ro'yxat).",
  "Texnik cheklovlar: quvvat, o'lchamlar, narx, ishlash muddati.",
  "Jihoz va dasturiy vositalar ro'yxati.",
  "Bosqichlar va vaqt rejasi.",
  "Muvaffaqiyat mezonlari: qanday natija olinsa loyiha bajarilgan hisoblanadi.",
 ]),
 ("Talablarni to'g'ri yozish", [
  "Yomon: \"qurilma tez ishlasin\". Yaxshi: \"javob vaqti 1 sekunddan oshmasin\".",
  "Yomon: \"aniq bo'lsin\". Yaxshi: \"20 sinovdan kamida 17 tasida to'g'ri javob bersin\".",
  "Har bir talab uchun uni QANDAY tekshirish mumkinligini o'ylab ko'ring.",
  "Tekshirib bo'lmaydigan talab — talab emas, xohish.",
  "Texnik topshiriq loyiha oxirida tekshirish ro'yxati bo'lib xizmat qiladi.",
 ]),
),

"Sxemani chizish": D(
 ("AI qurilmasi sxemasining xususiyati", [
  "Kamera va mikrofon platada bo'lgani uchun sxema odatda sodda bo'ladi.",
  "Asosiy e'tibor: quvvat, qo'shimcha sensorlar va ijro qurilmalari.",
  "Quvvat muhim: kamera ishlaganda tok sezilarli ortadi va manba yetarli bo'lishi kerak.",
  "Indikatorlar zarur: qurilma qachon tinglayotganini va qachon qaror qabul qilganini ko'rsatish.",
 ]),
 ("Sxemada ko'rsatilishi kerak bo'lgan narsalar", [
  "Har bir ulanishning aniq pin raqami.",
  "Quvvat manbai va uning kuchlanishi hamda toki.",
  "Sensorlarning joylashuvi (kamera qayerga qaraydi, mikrofon qayerda).",
  "Ijro qurilmalari va ular uchun kerakli tok.",
  "Umumiy GND — tashqi manba bo'lsa u albatta plata GND si bilan birlashtiriladi.",
 ]),
),

"Tasvirni belgilash va tayyorlash": D(
 ("Tasvir yig'ish qoidalari", [
  "Rasm qurilmaning O'Z kamerasi bilan olinishi kerak — boshqa kamera boshqa xususiyatga ega.",
  "Har bir sinf uchun kamida 50-100 rasm, yaxshisi ko'proq.",
  "Xilma-xillik shart: turli yorug'lik, turli burchak, turli masofa, turli fon.",
  "Faqat bir sharoitda olingan rasmlar bilan o'rgatilgan model boshqa sharoitda ishlamaydi.",
  "\"Fon\" yoki \"hech narsa\" sinfi ham yig'iladi.",
 ]),
 ("Belgilash tartibi", [
  "Tasnif uchun: har bir rasmga bitta sinf nomi qo'yiladi.",
  "Obyekt aniqlash uchun: har bir obyekt ramka bilan belgilanadi — bu ancha ko'p vaqt oladi.",
  "Sinf nomlari bir xil yoziladi: \"olma\" va \"Olma\" ikki xil sinf hisoblanadi.",
  "Shubhali rasmni belgilashdan ko'ra o'chirib tashlagan ma'qul.",
  "Belgilash tugagach ma'lumot 80/20 nisbatda bo'linadi.",
 ]),
 ("Rasmni tayyorlash", [
  "Rasm kichraytiriladi: 96x96 yoki 160x160 — mikrokontroller uchun katta rasm sig'maydi.",
  "Rangli yoki oq-qora tanlanadi: oq-qora model uch barobar kichik bo'ladi.",
  "Ko'p vazifalarda rang muhim emas va oq-qora yetarli.",
  "Rasm o'lchami va rangi keyin O'ZGARTIRILMASLIGI kerak — model shunga o'rgatilgan.",
 ]),
),

"AI modelini o'rgatish va integratsiya": D(
 ("O'rgatishdan qurilmagacha", [
  "1) Ma'lumot yig'ilgan va belgilangan.",
  "2) Impulse qurilgan: kirish bloki, belgi bloki, o'rgatish bloki.",
  "3) Model o'rgatilgan va aniqlik tekshirilgan.",
  "4) Quantized (int8) variant tanlanib, Arduino kutubxonasi yuklab olingan.",
  "5) Kutubxona IDE ga qo'shilgan va misol sinab ko'rilgan.",
  "6) Model kodi asosiy loyiha kodiga birlashtirilgan.",
 ]),
 ("Integratsiya muammolari", [
  "XOTIRA: model va loyiha kodi birga sig'masligi mumkin. Yechim — kichikroq model.",
  "VAQT: model ishlagan paytda boshqa vazifalar to'xtaydi. Yechim — FreeRTOS bilan alohida yadroga chiqarish.",
  "QUVVAT: model hisoblari tok sarfini oshiradi.",
  "ISHONCH: model past ishonch bersa qaror qabul qilinmasligi kerak — chegara qo'yiladi.",
  "BARQARORLIK: bir necha ketma-ket bashorat mos kelsagina qaror qabul qilish yolg'on ishlashni kamaytiradi.",
 ]),
),

"Boshqa loyihalarni baholash (peer review)": D(
 ("Baholash mezonlari", [
  "Muammo aniq qo'yilganmi va u haqiqatan mavjudmi.",
  "Yechim muammoga mos keladimi.",
  "Qurilma ishlaydimi — jonli namoyishda ko'rildimi.",
  "Natijalar raqam bilan berilganmi.",
  "Hujjat bilan loyihani qayta yig'ish mumkinmi.",
  "AI loyihasida qo'shimcha: ma'lumot xilma-xilmi, model haqiqiy sharoitda sinalganmi, axloqiy masalalar ko'rilganmi.",
 ]),
 ("Foydali fikr bildirish", [
  "Avval ishlagan narsani ayting — bu adolat va muallif nimani saqlash kerakligini biladi.",
  "Keyin ANIQ taklif bering: \"yaxshi emas\" emas, \"kamerani 10 sm pastroq qo'ysangiz fon soddalashadi va aniqlik ortadi\".",
  "Shaxsga emas, ishga baho beriladi.",
  "Savol shaklida bildirilgan fikr yaxshi qabul qilinadi: \"turli yorug'likda sinab ko'rdingizmi?\"",
  "O'z loyihangizga qo'llash mumkin bo'lgan g'oyani yozib oling — baholashning eng katta foydasi shu.",
 ]),
),

}
