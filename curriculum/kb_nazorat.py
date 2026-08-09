# -*- coding: utf-8 -*-
"""5-8-sinf: chorak kirish, nazorat-musobaqa va loyiha darslari uchun kontent.

Nazoratlar 0-4 dasturidagi RoboRace uslubida: har birining NOMI va aniq,
o'lchanadigan baholash mezoni bor. Baho taxmin bilan emas, sekundomer va
tekshirish ro'yxati bilan qo'yiladi.
"""


def K(amaliy, nazariya, qollanma, savol=(), xato=None):
    """Chorak kirish darsi."""
    return {"amaliy": amaliy, "nazariya": list(nazariya), "qollanma": qollanma,
            "savol": [list(s) for s in savol], "xato": xato}


def NZ(nom, vazifa, talablar, mezon, qollanma, vaqt=None):
    """Nazorat-musobaqa. mezon = [(baho, shart), ...]"""
    return {"nom": nom, "vazifa": vazifa, "talablar": list(talablar),
            "mezon": [list(m) for m in mezon], "qollanma": qollanma, "vaqt": vaqt}


def LY(nom, talablar, mezon, qollanma):
    """Chorak loyihasi. mezon = [(band, ball), ...] — jami 100 ball."""
    return {"nom": nom, "talablar": list(talablar),
            "mezon": [list(m) for m in mezon], "qollanma": qollanma}


# ==================================================================== KIRISH
KIRISH = {
"Kurs bilan tanishuv, elektr xavfsizligi, ish o'rnini tashkil qilish": K(
 "To'plamni ro'yxat bo'yicha tekshirish va xavfsizlik qoidalarini imzolash",
 ["Chorak davomida elektr zanjiri, LED, rezistor, tugma va sxema tili o'rganiladi.",
  "Uch qat'iy qoida: rozetkaga tegilmaydi; batareya qutblari tutashtirilmaydi; sxema o'zgartirilishidan oldin quvvat uziladi.",
  "Ish o'rni tartibi: komponentlar qutida, simlar bir joyda, ish tugagach hammasi joyiga qo'yiladi.",
  "Chorak oxirida har o'quvchi korpusli, ishlaydigan qo'l chirog'ini mustaqil yig'adi."],
 "Xavfsizlik qoidalarini o'quvchilar imzolab tasdiqlasin — bu rasmiy shakl mas'uliyat hissini oshiradi va yil davomida havola qilib turish mumkin."),

"Nima uchun o'lchaymiz: taxmin va aniqlik farqi": K(
 "Bir zanjirni avval ko'z bilan baholab, keyin multimetr bilan o'lchab, farqni yozish",
 ["Taxmin tez, lekin noaniq. O'lchov sekinroq, lekin raqam beradi va uni tekshirib bo'ladi.",
  "Muhandislik qarori taxminga emas, o'lchovga tayanadi: \"chiroq xira\" emas, \"tok 8 mA, kerakli qiymat 15 mA\".",
  "Chorak davomida multimetr, Om qonuni, kuchlanish bo'luvchi va nosozlik topish o'rganiladi.",
  "Chorak oxirida yorug'lik rostlagichli chiroq yasaladi."],
 "Boshida o'quvchilarga zanjirdagi kuchlanishni taxmin qildiring va yozdiring, keyin o'lchating. Farq o'lchovning zarurligini gapirmasdan isbotlaydi."),

"Komponent nima: har birining o'z vazifasi bor": K(
 "To'plamdagi 20 komponentni ko'rib chiqib, nomlari bilan jadval tuzish",
 ["Har komponentning bitta aniq vazifasi bor: rezistor cheklaydi, kondensator to'playdi, diod bir tomonga o'tkazadi.",
  "Murakkab qurilma — bu ko'p komponentning birgalikda ishlashi. Har biri o'z vazifasini bajaradi.",
  "Chorak davomida kondensator, diod, tranzistor, RGB LED, 7-segment, zummer, motor va rele o'rganiladi.",
  "Chorak oxirida qorong'ida o'zi yonadigan avtomatik tungi chiroq yasaladi."],
 "Komponentlarni qo'lga olib ko'rish uchun vaqt bering. Jismoniy tanishuv keyingi mavhum tushunchalarga asos bo'ladi."),

"Sensor nima: fizik kattalikni elektr signalga aylantirish": K(
 "Uch sensorni sinab, ularning javobini kuzatish va jadvalga yozish",
 ["Sensor fizik kattalikni (yorug'lik, harorat, magnit) elektr signalga aylantiradi.",
  "Sezish - qaror - ijro: har avtomatik tizim shu uch bo'g'indan iborat. Bu chorakning asosiy g'oyasi.",
  "Chorak davomida 10 dan ortiq sensor turi o'rganiladi va ular bilan avtomat zanjirlar yig'iladi.",
  "Chorak oxirida sensor, tovush va yorug'likdan iborat signalizatsiya qurilmasi yasaladi."],
 "Sezish - qaror - ijro uchligini doskaga yozib qo'ying va chorak davomida har zanjirda shu uchtasini ko'rsatib boring."),

"Kurs bilan tanishuv, xavfsizlik va ish o'rni madaniyati": K(
 "Ish o'rnini standart bo'yicha tashkil qilib, xavfsizlik testini bajarish",
 ["6-sinf kursi 5-sinfdan chuqurroq: formulalar, hisoblash va datasheet bilan ishlash qo'shiladi.",
  "Xavfsizlik qoidalari o'zgarmaydi, lekin ularga sabab qo'shiladi: nima uchun aynan shunday.",
  "Ish o'rni madaniyati: toza montaj, komponentlarni tartibda saqlash, protokol yuritish.",
  "Chorak oxirida uch rejimli chiroq yasaladi — bu aralash ulanishni amalda talab qiladi."],
 "6-sinfda qoidalarga sabab qo'shing: \"mumkin emas\" emas, \"chunki tok shu yo'ldan o'tadi va sim qiziydi\". Bu yoshda sabab bilan tushuntirish ancha samarali."),

"O'lchov asboblari va o'lchash madaniyati": K(
 "Multimetrni tekshirib, uning aniqligini pasportdagi ma'lumot bilan solishtirish",
 ["O'lchov madaniyati: to'g'ri rejim, to'g'ri chegara, to'g'ri ulanish va natijani birlik bilan yozish.",
  "Har o'lchovning noaniqligi bor. Natija ± bilan yoziladi: 4,72 ± 0,05 V.",
  "Chorak davomida Om qonuni, quvvat, energiya va murakkab zanjir tahlili o'rganiladi.",
  "Chorak oxirida batareya sinovchi qurilma yasaladi — u yuklamali sinov tamoyilini amalda ko'rsatadi."],
 "Multimetr pasportini (yoki korpusdagi ma'lumotni) topib, aniqlik ko'rsatkichini birgalikda o'qing. Bu asbobga ongli munosabatni shakllantiradi."),

"Yarimo'tkazgich nima va nega u elektronikani o'zgartirdi": K(
 "Diod, tranzistor va mikrosxemani ko'rib chiqib, o'lchamlarini solishtirish",
 ["Yarimo'tkazgich — o'tkazgich ham, izolyator ham bo'lmagan modda (kremniy). Uning o'tkazuvchanligini boshqarish mumkin.",
  "Aynan shu boshqarish imkoniyati diod va tranzistorni yaratdi, ular esa butun zamonaviy elektronikani.",
  "Lampali kompyuter xona hajmida edi, tranzistorli esa cho'ntakka sig'adi. Farq million martaga yaqin.",
  "Chorak davomida kondensator, diod, stabilitron, tranzistor, rele va optopara o'rganiladi."],
 "Lampa va tranzistor o'lchamini solishtiring (rasm yoki eski radio detali bilan). Bu texnologiya rivojining eng ko'rgazmali misoli."),

"Sensor va ijro qurilmasi: avtomatik tizim g'oyasi": K(
 "Tayyor avtomatik qurilmani ko'rib, uning uch bo'g'inini aniqlash",
 ["Avtomatik tizim uch bo'g'indan iborat: sezish (sensor), qaror (boshqaruv), ijro (motor, LED, rele).",
  "Teskari bog'lanish tizimni \"aqlli\" qiladi: natija o'lchanadi va boshqaruvga qaytariladi.",
  "Chorak davomida sensorlar, DC va servo motor, H-ko'prik va qadamli motor o'rganiladi.",
  "Chorak oxirida platasiz, elektron avtomatik sug'orish tizimi yasaladi."],
 "Sinfdagi yoki uydagi avtomatik qurilmalarni (muzlatgich, dazmol, avtomatik eshik) tahlil qildiring: har birida uch bo'g'inni topsin."),

"Kurs rejasi, xavfsizlik, jihoz bilan tanishuv": K(
 "To'plamni tekshirib, kurs rejasi va baholash mezonlari bilan tanishish",
 ["7-sinf kursi jadal: 1-chorakda butun elektronika asoslari, keyingi uch chorakda Arduino to'liq o'rganiladi.",
  "Tezlik yuqori bo'lgani uchun mustaqil ish va uyga vazifa hal qiluvchi ahamiyatga ega.",
  "Xavfsizlik qoidalari va ish o'rni tartibi birinchi darsdan qat'iy talab qilinadi.",
  "Yil oxirida aqlli uy maketi — sensor, ekran va ijro qurilmasidan iborat to'liq tizim yasaladi."],
 "Kurs tezligini ochiq ayting va uyga vazifa nima uchun majburiy ekanini tushuntiring. Bir yilda Arduino'ni tugatish mustaqil ishsiz mumkin emas."),

"Mikrokontroller nima va u nimasi bilan oddiy zanjirdan farq qiladi": K(
 "Bir xil vazifani zanjir bilan va Arduino bilan bajarib, farqni jadvalga yozish",
 ["Oddiy zanjirda mantiq SIMLAR bilan belgilanadi, mikrokontrollerda esa DASTUR bilan.",
  "Shuning uchun bir xil apparat bilan butunlay boshqa qurilma yasash mumkin — faqat dastur almashtiriladi.",
  "Arduino Uno: 32 KB dastur xotirasi, 16 MHz, 14 raqamli va 6 analog pin.",
  "Chorak davomida dastur tuzilishi, o'zgaruvchi, sikl, shart va Serial monitor o'rganiladi."],
 "Bitta plataga ikki xil dastur yuklab ko'rsating — bir xil apparat, butunlay boshqa qurilma. Bu chorakning asosiy g'oyasini bir zumda ochadi."),

"Analog va raqamli dunyo o'rtasidagi farq": K(
 "Bir hodisani analog va raqamli usulda o'lchab, natijalarni solishtirish",
 ["Raqamli signal ikki holatga ega, analog signal esa uzluksiz o'zgaradi.",
  "Tabiat analog: harorat, yorug'lik, tovush — hammasi uzluksiz. Kompyuter esa raqamli.",
  "ADC ikkisini bog'laydi: analog kuchlanishni raqamga aylantiradi. Arduino da 1024 daraja.",
  "Chorak davomida analogRead, PWM, map va 8 dan ortiq sensor o'rganiladi."],
 "Analogdan raqamliga o'tishdagi yo'qotishni ko'rsating: 1024 daraja ko'p tuyuladi, lekin u baribir chegara. Bu tushuncha muhim."),

"Harakat va ma'lumot ko'rsatish: qurilmani to'liq qilish": K(
 "Tayyor qurilmani ko'rib, uning kirish, qayta ishlash va chiqish qismlarini ajratish",
 ["To'liq qurilma uch qismdan iborat: kirish (sensor, tugma), qayta ishlash (dastur), chiqish (motor, ekran, tovush).",
  "Shu paytgacha kirish qismi o'rganildi. Bu chorakda chiqish qismi to'ldiriladi.",
  "Chorak davomida servo, DC va qadamli motor, L298N, zummer, LCD, 7-segment va IR pult o'rganiladi.",
  "Chorak oxirida aqlli uy maketi — barcha o'rganilganlarni birlashtiradigan loyiha yasaladi."],
 "Yil davomida yig'ilgan bilimlarning bir tizimga birlashishini ko'rsating. Bu chorak — barcha qismlarni bir joyga keltirish vaqti."),

"Kurs rejasi, xavfsizlik, jihoz va dasturiy muhit": K(
 "Jihozni tekshirib, IDE ni sozlab, birinchi dasturni yuklash",
 ["8-sinf 1-yil kursi eng jadal: 2 chorakda elektronika va Arduino, keyin ESP32 va IoT.",
  "Birinchi darsdayoq dasturiy muhit sozlanadi — bu vaqt tejaydi va darhol ishga kirishishga imkon beradi.",
  "Xavfsizlik qoidalari qisqa, lekin qat'iy: past kuchlanish bilan ishlaymiz, 220 V faqat o'qituvchi namoyishida.",
  "Yil oxirida IoT ob-havo stansiyasi — sensor, bulut va Telegram bilan ishlaydigan to'liq tizim yasaladi."],
 "Birinchi darsda IDE sozlash va muvaffaqiyatli yuklashni ta'minlang. Texnik to'siqlar boshida hal qilinsa, keyingi darslar ancha samarali o'tadi."),

"Kutubxonalar va tayyor modullar bilan ishlash": K(
 "Ikki kutubxonani o'rnatib, misollari bilan ishlash",
 ["Kutubxona — boshqalar yozgan tayyor kod. U murakkab ishni bir necha buyruqqa qisqartiradi.",
  "Modul — sensor va uning yordamchi sxemasi bir platada. Bu ulashni ancha osonlashtiradi.",
  "Yangi kutubxona bilan ishlashni doim MISOLDAN boshlash kerak — hujjatni o'qishdan tezroq va ishonchliroq.",
  "Chorak davomida 10 dan ortiq modul va kutubxona o'rganiladi."],
 "\"Misoldan boshlash\" qoidasini o'rnating. Bu ko'nikma butun muhandislik faoliyatida ishlaydi va vaqtni juda tejaydi."),

"ESP32 nima: Arduino'dan farqi va imkoniyatlari": K(
 "Ikki platani solishtirib, imkoniyatlar jadvalini to'ldirish",
 ["ESP32: 240 MHz ikki yadro, 520 KB SRAM, WiFi va Bluetooth o'rnatilgan.",
  "Arduino Uno: 16 MHz, 2 KB SRAM, simsiz aloqa yo'q.",
  "Eng muhim amaliy farq — mantiq darajasi: ESP32 3.3 V, Arduino 5 V. Bu barcha sxemalarga ta'sir qiladi.",
  "Chorak davomida ESP32 pinlari, OLED ekran, WiFi va veb-server o'rganiladi."],
 "3.3 V masalasini birinchi darsdan qattiq ta'kidlang. Bu chorakda eng ko'p modul kuyadigan sabab va uni oldini olish mumkin."),

"IoT nima va u kundalik hayotda qayerda ishlatiladi": K(
 "Atrofdagi IoT qurilmalarini topib, ularning tuzilmasini tahlil qilish",
 ["IoT (Internet of Things) — internetga ulangan va ma'lumot almashadigan qurilmalar tizimi.",
  "Misollar: aqlli soat, aqlli rozetka, navigatsiya, shahar transport tizimi, issiqxona nazorati.",
  "IoT tizimi uch qismdan: qurilma (sensor va ijro), aloqa (WiFi, mobil tarmoq), bulut (saqlash va tahlil).",
  "Chorak davomida SD kart, RTC, HTTP, bulut, Telegram, MQTT, BLE va deep sleep o'rganiladi."],
 "O'quvchilardan uyidagi internetga ulangan qurilmalarni sanashni so'rang. Ro'yxat kutilganidan uzun chiqadi va mavzuni yaqin qiladi."),

"O'tgan yilni eslash va yangi yil rejasi": K(
 "O'tgan yildagi asosiy zanjirlarni xotiradan yig'ib, bilimni tekshirish",
 ["Yozgi tanaffusdan keyin ko'nikmalar susayadi — bu normal, ularni qayta tiklash kerak.",
  "Bu yil elektronika takrorlanadi va uning ustiga BLOKLI DASTURLASH qo'shiladi.",
  "Blokli dasturlashda buyruqlar bloklardan yig'iladi — sintaksis xatosi bo'lmaydi va mantiqqa e'tibor qaratiladi.",
  "Yil oxirida o'quvchi o'zi tanlagan aqlli qurilmani mustaqil yasaydi."],
 "Bilimni tekshirish uchun kichik amaliy topshiriq bering, test emas. Qo'l bilan yig'ish nimani unutganini aniq ko'rsatadi."),

"Dastur nima: kompyuterga beriladigan aniq buyruqlar": K(
 "Kundalik amalni (choy damlash) aniq qadamlarga bo'lib yozish",
 ["Dastur — buyruqlarning aniq ketma-ketligi. Kompyuter faqat aytilganini bajaradi, taxmin qilmaydi.",
  "Shuning uchun buyruqlar aniq bo'lishi kerak: \"suvni qizdir\" emas, \"suvni 100 darajagacha qizdir\".",
  "Qadamlar tartibi natijani belgilaydi — bir xil qadamlar boshqa tartibda boshqa natija beradi.",
  "Chorak davomida sikl, o'zgaruvchi, PWM, zummer, servo va motor bloklari o'rganiladi."],
 "\"Choy damlash algoritmi\" mashqini bajaring: o'quvchilar yozgan qadamlarni aynan bajarib ko'rsating. Tushirib qoldirilgan qadamlar kulgili va yodda qoladigan natija beradi."),

"Sensor va dastur: qurilma atrofni sezishi": K(
 "Uch sensorni ulab, qiymatlarini kuzatish",
 ["Sensorsiz qurilma faqat oldindan yozilgan ishni bajaradi. Sensor bilan u atrofga javob bera oladi.",
  "Bu chorakning asosiy bloki — SHART: agar sensor qiymati shundan katta bo'lsa, u holda shuni qil.",
  "Chorak davomida tugma, potensiometr, fotorezistor, termistor, ultratovush, PIR va namlik sensorlari o'rganiladi.",
  "Chorak oxirida aqlli gulzor yasaladi — tuproq quruq bo'lsa signal beradi."],
 "Sensorsiz va sensorli qurilma farqini ko'rsating: birinchisi ko'r, ikkinchisi ko'radi. Bu solishtirish chorakning maqsadini aniq qo'yadi."),

"Loyiha nima: g'oyadan ishlaydigan qurilmagacha": K(
 "Loyiha g'oyalarini o'ylab topib, ularni mezon bo'yicha baholash",
 ["Loyiha g'oyadan boshlanadi, lekin g'oyaning o'zi yetarli emas — uni bosqichma-bosqich amalga oshirish kerak.",
  "Bosqichlar: g'oya, reja, komponentlarni tanlash, yig'ish, dasturlash, sinash, tuzatish, taqdimot.",
  "Yaxshi g'oya mezonlari: real muammoni hal qiladi, mavjud jihoz bilan bajariladi, vaqtga ulguriladi.",
  "Chorak davomida LCD, IR pult, rele, algoritm chizish va korpus yasash o'rganiladi."],
 "G'oyalarni baholash mezonlarini birgalikda tuzing. O'quvchilar ko'pincha juda katta g'oya tanlaydi va uni ulgurmaydi — mezon bu muammoni oldini oladi."),

"O'tgan yilni eslash va mikrokontroller g'oyasi": K(
 "O'tgan yildagi zanjirlarni tiklab, mikrokontrollerli variantini ko'rish",
 ["Elektronika asoslari takrorlanadi: Om qonuni, bo'luvchi, tranzistor, rele.",
  "Bu yilning asosiy yangiligi — MATNLI dasturlash (Arduino IDE).",
  "Matnli dasturlash blokli dasturlashdan farq qiladi: sintaksis qat'iy, lekin imkoniyatlar cheksiz.",
  "Yil oxirida aqlli uy maketi — to'liq tizim yasaladi."],
 "Matnli dasturlashga o'tish sababini asoslang: barcha kutubxonalar, misollar va professional ishlar matnli kodda. Bu qadam zarur."),

"Dastur mantiqi: ketma-ketlik, shart, takrorlash": K(
 "Uch asosiy konstruksiyani kundalik hayotdan misollar bilan izohlash",
 ["Har qanday dastur uch konstruksiyadan tuziladi: ketma-ketlik, shart (tanlov) va takrorlash (sikl).",
  "Bu 1966-yilda isbotlangan: shu uchtasi bilan istalgan algoritmni yozish mumkin.",
  "Kundalik misollar: retsept — ketma-ketlik; \"yomg'ir yog'sa soyabon ol\" — shart; \"toza bo'lguncha yuv\" — takrorlash.",
  "Chorak davomida o'zgaruvchi, for, while, if, mantiqiy amallar, funksiya va massiv o'rganiladi."],
 "Uch konstruksiya yetarli ekanini ayting — bu chuqur va ta'sirchan fakt, dasturlashni tartibli tizim sifatida ko'rsatadi."),

"Atrofni o'lchash: sensorlar bilan ishlash": K(
 "Analog va raqamli sensorlarni ulab, qiymatlarini Serial Plotter'da kuzatish",
 ["Sensor fizik kattalikni elektr signalga aylantiradi, ADC esa uni raqamga.",
  "Analog sensor uzluksiz qiymat beradi, raqamli sensor esa tayyor raqam yoki ikki holat.",
  "Har sensorni ishlatishdan oldin KALIBRLASH kerak — tayyor chegara ishlamaydi.",
  "Chorak davonida analogRead, map, PWM, fotorezistor, termistor, DHT22, HC-SR04 va PIR o'rganiladi."],
 "Kalibrlash talabini birinchi darsdan qo'ying. Bu chorakda eng ko'p takrorlanadigan va eng muhim ko'nikma."),

"Qurilmani to'liq qilish: sezish, qaror, harakat": K(
 "Tayyor qurilmani uch bo'g'inga ajratib tahlil qilish",
 ["To'liq qurilma: sezish (sensor) - qaror (dastur) - harakat (ijro qurilmasi).",
  "Shu paytgacha sezish va qaror o'rganildi. Bu chorakda harakat qismi to'ldiriladi.",
  "Chorak davomida servo, DC va qadamli motor, L298N, zummer, LCD, 7-segment va IR pult o'rganiladi.",
  "Chorak oxirida aqlli uy maketi — to'liq tizim yasaladi."],
 "Uch bo'g'in tuzilmasini yana bir bor mustahkamlang — bu robototexnikaning universal tuzilmasi va keyingi yillarda ham ishlatiladi."),

"ESP32: Arduino'dan keyingi qadam": K(
 "ESP32 ni ulab, birinchi dasturni yuklash va imkoniyatlarini solishtirish",
 ["ESP32 — Arduino'dan 15 marta tez, 260 marta ko'p xotirali va WiFi bilan.",
  "Lekin u murakkabroq: 3.3 V mantiq, cheklangan pinlar, boot muammolari.",
  "Chorak davomida pinlar, ADC, PWM, touch, I2C, SPI, OLED, SD kart, RTC va deep sleep o'rganiladi.",
  "Chorak oxirida ma'lumot yozib boruvchi qurilma (data logger) yasaladi."],
 "Kuch va murakkablik birga kelishini ayting — bu texnologiyada umumiy qonuniyat va uni oldindan bilish tayyorgarlik beradi."),

"Internetga ulangan qurilma nima beradi": K(
 "IoT qurilmalarini tahlil qilib, ularning arxitekturasini chizish",
 ["Internetga ulangan qurilma uch narsani beradi: uzoqdan kuzatish, uzoqdan boshqarish va ma'lumot to'plash.",
  "Ma'lumot to'plash eng qimmatlisi: uzoq muddatli ma'lumot qonuniyatlarni ochadi va bashorat qilishga imkon beradi.",
  "Chorak davomida WiFi, veb-server, HTML, AJAX, HTTP client, bulut, Telegram, MQTT va BLE o'rganiladi.",
  "Chorak oxirida IoT monitoring tizimi yasaladi."],
 "Uzoq muddatli ma'lumotning qiymatini ta'kidlang — bir kunlik grafik kam narsa aytadi, bir oylik grafik esa qonuniyatni ochadi."),

"Sun'iy intellekt nima va u qanday \"o'rganadi\"": K(
 "SI ishlatiladigan kundalik qurilmalarni topib, ular qanday ishlashini muhokama qilish",
 ["Sun'iy intellekt — inson aqliy vazifalarini bajaruvchi tizimlar sohasi.",
  "Mashinaviy o'rganishda qoidalar qo'lda yozilmaydi — model ularni MA'LUMOTDAN topadi.",
  "\"O'rganish\" — bu model parametrlarini ma'lumotga moslash jarayoni. Sehr yo'q, faqat matematika va ko'p hisob.",
  "Chorak davomida dataset, belgi, sinf, Edge Impulse, model o'rgatish va baholash o'rganiladi."],
 "\"Sehr yo'q, matematika bor\" fikrini boshidan o'rnating. SI haqidagi mifologik tasavvurni buzish — bu chorakning muhim vazifasi."),

"Kamera va mikrofon: qurilma ko'radi va eshitadi": K(
 "XIAO platasini ulab, kamera va mikrofonni sinab ko'rish",
 ["Bu chorakda qurilma yangi sezgi organlariga ega bo'ladi: ko'rish va eshitish.",
  "Tasvir va ovoz — juda katta hajmli ma'lumot. Shuning uchun ularni to'g'ridan-to'g'ri emas, belgilar ko'rinishida qayta ishlanadi.",
  "TinyML ning kuchi shunda: butun tasvirni bulutga yubormasdan, qurilmaning o'zi qaror qabul qiladi.",
  "Chorak oxirida ko'radigan yoki eshitadigan yakuniy AI loyihasi yasaladi."],
 "Ma'lumot hajmini raqamlarda ko'rsating: 96x96 rasm 27 KB, bir sekundlik ovoz 32 KB. Cheklovni his qilish yechimlarni tushunarli qiladi."),

"Kurs rejasi va muhandislik yondashuvi": K(
 "Kurs rejasi bilan tanishib, yakuniy loyiha talablarini muhokama qilish",
 ["8-sinf 2-yil kursi — muhandislik darajasi: o'lchov aniqligi, resurs byudjeti, arxitektura va hujjat.",
  "Muhandislik yondashuvi: har qaror asoslanadi, har natija o'lchanadi, har ish hujjatlashtiriladi.",
  "Chorak davomida ikki yadro, ADC/DAC, INA219, BMP280, HX711, filtrlash va FreeRTOS o'rganiladi.",
  "Yil oxirida AI integratsiyalangan IoT qurilmasi — yakuniy muhandislik loyihasi bajariladi."],
 "Muhandislik va havaskorlik farqini aniq qo'ying: havaskor \"ishladi\" desa yetadi, muhandis \"qanday sharoitda, qanday aniqlik bilan\" deb javob beradi."),

"Tizim sifatida loyihalash: qurilma, tarmoq, interfeys": K(
 "Mavjud IoT tizimini uch qatlamga ajratib tahlil qilish",
 ["IoT tizimi uch qatlamdan iborat: qurilma (sensor va ijro), tarmoq (aloqa va protokol), interfeys (foydalanuvchi ko'radigan qism).",
  "Har qatlam alohida loyihalanadi va sinaladi, keyin birlashtiriladi.",
  "Qatlamlarni ajratish tizimni o'zgartirishni osonlashtiradi: bir qatlam almashtirilsa qolganlari o'zgarmaydi.",
  "Chorak davomida API, JSON, HTTP, bulut, MQTT, BLE, xavfsizlik va OTA o'rganiladi."],
 "Qatlamlarga bo'lish g'oyasini ta'kidlang — bu murakkab tizimlarni boshqarishning universal usuli va dasturlashda ham, tarmoqda ham ishlaydi."),

"Sun'iy intellekt: nazariya va qurilmadagi amaliyot": K(
 "SI ning nazariy asoslarini va amaliy cheklovlarini solishtirish",
 ["Bu chorakda SI nazariyasi chuqurroq o'rganiladi: neyron tarmoq, o'rgatish turlari, baholash ko'rsatkichlari.",
  "Amaliyot esa mikrokontroller cheklovlari doirasida: kilobaytlar xotira, millisekundlar vaqt.",
  "Nazariya va amaliyot orasidagi masofani ko'rish muhim: kitobdagi model bilan qurilmadagi model juda farq qiladi.",
  "Chorak oxirida anomaliya aniqlovchi tizim yasaladi — bu sanoatda keng qo'llaniladigan real vazifa."],
 "Nazariya va amaliyot farqini ochiq ko'rsating: bulutdagi model gigabayt, qurilmadagi 100 kilobayt. Bu cheklov muhandislik ijodkorligini talab qiladi."),

"Muhandislik sikli: muammo, yechim, prototip, sinov, himoya": K(
 "Muhandislik siklining bosqichlarini o'rganib, yakuniy loyiha rejasini tuzish",
 ["Muhandislik sikli: muammoni aniqlash, tadqiq qilish, yechim variantlari, loyihalash, prototip, sinov, yaxshilash, hujjat, himoya.",
  "Sikl bir yo'nalishli emas — sinov natijasiga qarab oldingi bosqichlarga qaytiladi.",
  "Eng ko'p uchraydigan xato: muammoni tadqiq qilmasdan darhol yechim qurishga kirishish.",
  "Bu chorak butunlay yakuniy loyihaga bag'ishlanadi: har dars siklning bir bosqichi."],
 "Sikl chizmasini sinf devoriga osib qo'ying va har darsda qaysi bosqichda ekaningizni ko'rsating. Bu chorak davomida yo'nalishni saqlaydi."),
}


# =================================================================== NAZORAT
NAZORAT = {
"Berilgan sxema bo'yicha zanjirni mustaqil yig'ish va ishlatish": NZ(
 "CircuitSpeed",
 "Har o'quvchi konvertdan sxema oladi va uni breadboardda mustaqil yig'adi. Sxemada LED, rezistor, tugma va kalit bo'ladi.",
 ["Sxema o'qiladi va komponentlar tanlanadi", "Zanjir breadboardda yig'iladi",
  "Quvvat ulanadi va ishlashi tekshiriladi", "O'qituvchiga ko'rsatiladi"],
 [("5", "3 daqiqagacha yig'ib, zanjir birinchi urinishda ishlaydi"),
  ("4", "5 daqiqagacha yig'ib, zanjir ishlaydi (bir marta tuzatish bilan)"),
  ("3", "8 daqiqagacha yig'ib, zanjir ishlaydi"),
  ("2", "Zanjir yig'ilgan, lekin ishlamaydi yoki 8 daqiqadan oshgan"),
  ("Bajarilmadi", "Sxemani o'qiy olmadi yoki zanjir yig'ilmadi")],
 "Sekundomerni ochiq ishlating va vaqtni doskaga yozib boring. Vaqt mezoni musobaqa hissini beradi, lekin shoshilish xatoga olib kelishini ham ko'rsatadi.",
 vaqt=480),

"Zanjirni yig'ib, uch nuqtada o'lchash va Om qonuni bilan tekshirish": NZ(
 "OhmCheck",
 "Berilgan sxema yig'iladi, uch nuqtada kuchlanish va bir joyda tok o'lchanadi, natija Om qonuni bilan tekshiriladi.",
 ["Zanjir yig'iladi", "Uch nuqtada kuchlanish o'lchanadi va yoziladi",
  "Tok o'lchanadi", "Om qonuni bilan hisoblanadi va o'lchov bilan solishtiriladi"],
 [("5", "Barcha o'lchovlar to'g'ri, hisob mos keladi (farq 10% dan kam), birlik yozilgan"),
  ("4", "O'lchovlar to'g'ri, hisobda bitta kichik xato"),
  ("3", "O'lchovlar to'g'ri, lekin hisob bajarilmagan yoki xato"),
  ("2", "O'lchovlarda xato bor (noto'g'ri ulanish yoki rejim)"),
  ("Bajarilmadi", "Multimetrni to'g'ri ishlata olmadi")],
 "O'lchov protokolini oldindan tarqating — o'quvchi faqat qiymatlarni to'ldiradi. Bu baholashni bir xil va adolatli qiladi.",
 vaqt=900),

"Berilgan komponentlarni tanib, vazifasini tushuntirish va zanjirga qo'shish": NZ(
 "ComponentQuiz",
 "O'quvchiga 8 komponent beriladi. Har birini tanib, nomini, vazifasini aytadi va bittasini zanjirga qo'shib ishlatadi.",
 ["8 komponent tanib, nomlanadi", "Har birining vazifasi aytiladi",
  "Qutbli komponentlar ajratiladi", "Bitta komponent zanjirga qo'shilib ishlatiladi"],
 [("5", "8 tadan 8 tasi to'g'ri tanildi va zanjir ishladi"),
  ("4", "7 tasi to'g'ri, zanjir ishladi"),
  ("3", "5-6 tasi to'g'ri yoki zanjir yordam bilan ishladi"),
  ("2", "3-4 tasi to'g'ri"),
  ("Bajarilmadi", "3 tadan kam komponent tanildi")],
 "Komponentlarni konvertlarga oldindan solib qo'ying — har o'quvchiga bir xil to'plam. Bu baholashni taqqoslanadigan qiladi.",
 vaqt=600),

"Sensorli zanjirni yig'ib, ishlash tamoyilini tushuntirish": NZ(
 "SensorLogic",
 "Sensorli avtomatik zanjir yig'iladi va o'quvchi uning sezish - qaror - ijro bo'g'inlarini ko'rsatib tushuntiradi.",
 ["Sensor bo'luvchiga to'g'ri ulanadi", "Tranzistorli boshqaruv yig'iladi",
  "Ijro qurilmasi ulanadi va zanjir ishlaydi", "Uch bo'g'in og'zaki tushuntiriladi"],
 [("5", "Zanjir ishlaydi va uch bo'g'in aniq tushuntirildi"),
  ("4", "Zanjir ishlaydi, tushuntirish qisman"),
  ("3", "Zanjir yordam bilan ishladi"),
  ("2", "Zanjir yig'ilgan, lekin ishlamadi"),
  ("Bajarilmadi", "Sensor to'g'ri ulanmadi")],
 "Tushuntirishni alohida baholang — ishlaydigan zanjir yig'ish va uni tushunish har xil narsa. Ikkinchisi muhimroq.",
 vaqt=900),

"Sxema bo'yicha aralash ulanishli zanjir yig'ish": NZ(
 "MixedCircuit",
 "Ketma-ket va parallel qismlari bor aralash zanjir sxema bo'yicha yig'iladi va tekshiriladi.",
 ["Sxema tahlil qilinadi va qismlarga ajratiladi", "Zanjir yig'iladi",
  "Umumiy qarshilik hisoblanadi va o'lchanadi", "Natijalar solishtiriladi"],
 [("5", "10 daqiqagacha yig'ildi, hisob va o'lchov 10% ichida mos"),
  ("4", "15 daqiqagacha yig'ildi va ishladi, hisobda kichik xato"),
  ("3", "Zanjir ishladi, hisob bajarilmadi"),
  ("2", "Zanjir ishlamadi yoki tuzilma noto'g'ri"),
  ("Bajarilmadi", "Sxemani qismlarga ajrata olmadi")],
 "Sxemani qismlarga ajratish qadamini alohida so'rang — bu aralash zanjir bilan ishlashning kalit ko'nikmasi.",
 vaqt=900),

"Zanjirni o'lchash, hisoblash va natijalarni solishtirish": NZ(
 "MeasureMaster",
 "Berilgan zanjirda barcha kattaliklar o'lchanadi va hisoblanadi, farq foizda ko'rsatiladi.",
 ["Barcha nuqtalarda kuchlanish o'lchanadi", "Toklar o'lchanadi yoki hisoblanadi",
  "Quvvat hisoblanadi", "Hisob va o'lchov farqi foizda beriladi"],
 [("5", "Barcha o'lchovlar to'g'ri, quvvat hisoblangan, farq foizda ko'rsatilgan"),
  ("4", "O'lchovlar to'g'ri, quvvat yoki foiz hisoblanmagan"),
  ("3", "Asosiy o'lchovlar to'g'ri, hisobda xatolar bor"),
  ("2", "O'lchovlarda usul xatosi (noto'g'ri ulanish)"),
  ("Bajarilmadi", "O'lchovlar bajarilmadi")],
 "Farqni foizda ko'rsatishni talab qiling — bu o'lchov madaniyatining muhim qismi va boshqa fanlarda ham kerak bo'ladi.",
 vaqt=900),

"Tranzistorli yoki releli boshqaruv zanjirini yig'ish": NZ(
 "SwitchBuild",
 "Tranzistor yoki rele bilan boshqariladigan zanjir yig'iladi, himoya elementlari to'g'ri qo'yiladi.",
 ["Baza rezistori hisoblanadi va qo'yiladi", "Zanjir yig'iladi",
  "Flyback diod to'g'ri yo'nalishda qo'yiladi", "To'yinish holati o'lchov bilan tekshiriladi"],
 [("5", "Zanjir ishlaydi, diod to'g'ri, to'yinish tekshirilgan (0,2 V)"),
  ("4", "Zanjir ishlaydi, himoya bor, to'yinish tekshirilmagan"),
  ("3", "Zanjir ishlaydi, lekin flyback diod yo'q yoki noto'g'ri"),
  ("2", "Zanjir ishlamaydi yoki baza rezistori yo'q"),
  ("Bajarilmadi", "Tranzistor oyoqlarini aniqlay olmadi")],
 "Flyback diodni alohida band sifatida baholang — uni unutish jihozni buzadi va bu odat sifatida shakllanishi kerak.",
 vaqt=900),

"Sensorli avtomatik zanjirni loyihalash va yig'ish": NZ(
 "AutoDesign",
 "Berilgan vazifa uchun o'quvchi sxemani O'ZI loyihalaydi, chizadi va yig'adi.",
 ["Vazifa tahlil qilinadi va sxema chiziladi", "Komponentlar tanlanadi va asoslanadi",
  "Zanjir yig'iladi va sozlanadi", "Ishlashi namoyish qilinadi"],
 [("5", "Sxema mustaqil chizildi, zanjir ishlaydi, tanlov asoslandi"),
  ("4", "Sxema chizildi, zanjir ishlaydi, asoslash to'liq emas"),
  ("3", "Yordam bilan sxema chizildi va zanjir ishladi"),
  ("2", "Sxema chizildi, lekin zanjir ishlamadi"),
  ("Bajarilmadi", "Sxema chizilmadi")],
 "Bu birinchi mustaqil loyihalash nazorati. Sxema chizishni alohida va yuqori baholang — yig'ish emas, loyihalash asosiy ko'nikma.",
 vaqt=1200),

"Sxema bo'yicha zanjir yig'ish, o'lchash va hisoblash": NZ(
 "ElectroSprint",
 "Jadal kurs yakuni: zanjir yig'iladi, o'lchanadi, hisoblanadi va natija asoslanadi.",
 ["Zanjir sxema bo'yicha yig'iladi", "Uch kattalik o'lchanadi",
  "Om qonuni va quvvat hisoblanadi", "Natijalar solishtiriladi va izohlanadi"],
 [("5", "12 daqiqagacha bajarildi, o'lchov va hisob to'liq mos"),
  ("4", "15 daqiqagacha bajarildi, kichik xato bilan"),
  ("3", "Bajarildi, lekin hisobda jiddiy xato yoki vaqtdan oshgan"),
  ("2", "Zanjir ishladi, o'lchov yoki hisob bajarilmadi"),
  ("Bajarilmadi", "Zanjir ishlamadi")],
 "7-sinfda tezlik muhim — kurs jadal va vaqt boshqarish ko'nikmasi ham baholanadi. Lekin aniqlikni tezlikdan yuqori qo'ying.",
 vaqt=900),

"Berilgan vazifa bo'yicha dastur yozib, sxemani yig'ish": NZ(
 "CodeAndBuild",
 "Vazifa beriladi (masalan: tugma bosilganda LEDlar navbat bilan yonsin). O'quvchi sxemani yig'ib, dasturni yozadi.",
 ["Sxema yig'iladi", "Dastur mustaqil yoziladi",
  "Dastur yuklanadi va ishlaydi", "Kod izohlanadi va tushuntiriladi"],
 [("5", "20 daqiqagacha to'liq ishladi, kod toza va izohli"),
  ("4", "To'liq ishladi, kod izohsiz yoki tartibsiz"),
  ("3", "Qisman ishladi yoki yordam bilan tugatildi"),
  ("2", "Sxema yig'ildi, dastur ishlamadi"),
  ("Bajarilmadi", "Dastur yuklanmadi")],
 "Kod sifatini alohida baholang: nom berish, izoh, tartib. \"Ishlaydigan, lekin o'qib bo'lmaydigan kod\" — bu chala natija.",
 vaqt=1500),

"Sensor qiymatini o'qib, shartga qarab ijro qurilmasini boshqarish": NZ(
 "SensorControl",
 "Sensor o'qiladi, chegara kalibrlanadi va shartga qarab ijro qurilmasi boshqariladi.",
 ["Sensor ulanadi va qiymatlari kuzatiladi", "Chegara o'lchov asosida tanlanadi",
  "Shart yozilib, ijro qurilmasi boshqariladi", "Gisterezis qo'shiladi"],
 [("5", "Tizim ishlaydi, chegara kalibrlangan, gisterezis bor"),
  ("4", "Tizim ishlaydi, chegara kalibrlangan, gisterezis yo'q"),
  ("3", "Tizim ishlaydi, lekin chegara taxminan tanlangan"),
  ("2", "Sensor o'qildi, lekin boshqaruv ishlamadi"),
  ("Bajarilmadi", "Sensor qiymatlari olinmadi")],
 "Kalibrlash va gisterezisni alohida band qiling — bular sensorli tizimni ishonchli qiladigan ikki asosiy narsa.",
 vaqt=1500),

"Ijro qurilmasi va ekranli tizimni yig'ib, dasturlash": NZ(
 "ActuatorDisplay",
 "Servo yoki motor va LCD ekranli tizim yig'ilib, dasturlanadi.",
 ["Ijro qurilmasi to'g'ri ulanadi (alohida quvvat, umumiy GND)", "Ekran ulanadi va ishga tushiriladi",
  "Dastur yozilib, ikkalasi birga ishlaydi", "Ekran maketi rejalangan"],
 [("5", "Tizim to'liq ishlaydi, quvvat to'g'ri, ekran tartibli"),
  ("4", "Tizim ishlaydi, ekran maketi rejalanmagan"),
  ("3", "Qismlar alohida ishlaydi, birga ishlashda muammo"),
  ("2", "Bir qism ishlamadi"),
  ("Bajarilmadi", "Tizim yig'ilmadi")],
 "Alohida quvvat va umumiy GND ni alohida band qiling — bu yil davomida eng ko'p takrorlangan va eng ko'p unutiladigan qoida.",
 vaqt=1500),

"Dastur va sxemani birga yig'ib, berilgan vazifani bajarish": NZ(
 "BuildAndCode",
 "Jadal kurs yakuni: berilgan vazifa uchun sxema va dastur birga bajariladi.",
 ["Vazifa tahlil qilinadi va reja tuziladi", "Sxema yig'iladi",
  "Dastur yoziladi va yuklanadi", "Tizim sinaladi va tuzatiladi"],
 [("5", "25 daqiqagacha to'liq ishladi, kod toza"),
  ("4", "To'liq ishladi, kod tartibsiz yoki vaqtdan biroz oshgan"),
  ("3", "Qisman ishladi"),
  ("2", "Sxema yoki dasturdan biri tayyor"),
  ("Bajarilmadi", "Vazifa bajarilmadi")],
 "Rejalashtirish qadamini talab qiling: darhol yig'ishga kirishgan o'quvchi ko'proq vaqt yo'qotadi. Buni baholash orqali ko'rsating.",
 vaqt=1500),

"Ko'p komponentli tizimni yig'ib dasturlash": NZ(
 "SystemAssembly",
 "To'rt va undan ortiq komponentli tizim yig'ilib, dasturlanadi va sinaladi.",
 ["Komponentlar bittalab qo'shilib sinaladi", "Barcha komponentlar birga ishlaydi",
  "Kod funksiyalarga bo'lingan", "Tizim sinov ro'yxati bo'yicha tekshirilgan"],
 [("5", "Barcha komponentlar ishlaydi, kod funksiyalarga bo'lingan, sinov o'tkazilgan"),
  ("4", "Barchasi ishlaydi, kod bo'linmagan"),
  ("3", "Ko'pchiligi ishlaydi, bittasida muammo"),
  ("2", "Yarmi ishlaydi"),
  ("Bajarilmadi", "Tizim yig'ilmadi")],
 "\"Bittalab qo'shish\" usulini kuzatib boring va baholang — hammasini birdan yig'ib ishlamay qolgan o'quvchi ko'p vaqt yo'qotadi.",
 vaqt=1800),

"ESP32'da veb-server orqali qurilmani boshqarish": NZ(
 "WebControl",
 "ESP32 da veb-server ishga tushiriladi va brauzerdan qurilma boshqariladi.",
 ["WiFi ga ulanadi va IP olinadi", "Veb-server ishga tushadi",
  "Brauzerdan qurilma boshqariladi", "Sensor qiymati sahifada ko'rsatiladi"],
 [("5", "Boshqaruv va ko'rsatish ishlaydi, sahifa telefonda ham qulay"),
  ("4", "Boshqaruv va ko'rsatish ishlaydi"),
  ("3", "Faqat boshqaruv yoki faqat ko'rsatish ishlaydi"),
  ("2", "WiFi ga ulandi, lekin sahifa ochilmadi"),
  ("Bajarilmadi", "WiFi ga ulanmadi")],
 "Telefonda ochib sinashni talab qiling — bu real foydalanish sharoiti va meta viewport masalasini amalda ko'rsatadi.",
 vaqt=1800),

"IoT tizimini yig'ib, ma'lumotni uzoqdan ko'rsatish": NZ(
 "IoTBuild",
 "Sensor ma'lumoti to'planib, bulutga yoki Telegram'ga yuboriladi va uzoqdan ko'riladi.",
 ["Sensor o'qiladi va tekshiriladi", "Aloqa o'rnatiladi (bulut yoki Telegram)",
  "Ma'lumot muntazam yuboriladi", "Uzoqdan ko'rish namoyish qilinadi"],
 [("5", "Tizim ishlaydi, qayta ulanish mantiqi bor, ma'lumot muntazam keladi"),
  ("4", "Tizim ishlaydi, qayta ulanish yo'q"),
  ("3", "Ma'lumot yuborildi, lekin uzuq-yuluq"),
  ("2", "Aloqa o'rnatildi, ma'lumot yuborilmadi"),
  ("Bajarilmadi", "Aloqa o'rnatilmadi")],
 "Qayta ulanish mantiqini alohida band qiling — uzoq ishlaydigan IoT tizimida aloqa albatta uziladi va tiklanish bo'lishi shart.",
 vaqt=1800),

"Zanjirni yig'ib, blokli dastur bilan LEDni yoqish": NZ(
 "FirstBlock",
 "Zanjir yig'ilib, blokli dastur bilan LED boshqariladi.",
 ["Zanjir to'g'ri yig'iladi (rezistor bilan)", "Plata ulanadi va port tanlanadi",
  "Blokli dastur yig'iladi", "Dastur yuklanadi va ishlaydi"],
 [("5", "10 daqiqagacha bajarildi, dastur mustaqil yig'ildi"),
  ("4", "15 daqiqagacha bajarildi"),
  ("3", "Yordam bilan bajarildi"),
  ("2", "Zanjir yig'ildi, dastur ishlamadi"),
  ("Bajarilmadi", "Bajarilmadi")],
 "Bu birinchi dasturlash nazorati — muvaffaqiyat hissi muhim. Vaqt mezonini yumshoq qo'ying va ko'proq yordam bering.",
 vaqt=900),

"Berilgan vazifani blokli dastur bilan bajarish": NZ(
 "BlockChallenge",
 "Vazifa beriladi (masalan: uch LED navbat bilan, keyin melodiya). Blokli dastur bilan bajariladi.",
 ["Vazifa tahlil qilinadi", "Bloklar to'g'ri tartibda yig'iladi",
  "Sikl va o'zgaruvchi ishlatiladi", "Dastur ishlaydi va tushuntiriladi"],
 [("5", "Vazifa to'liq bajarildi, sikl ishlatildi, dastur tartibli"),
  ("4", "Vazifa bajarildi, sikl ishlatilmadi (bloklar nusxalandi)"),
  ("3", "Vazifa qisman bajarildi"),
  ("2", "Dastur yig'ildi, lekin ishlamadi"),
  ("Bajarilmadi", "Bajarilmadi")],
 "Sikl ishlatilganini alohida baholang — bloklarni nusxalash bilan ham natija chiqadi, lekin bu chorakning maqsadi sikl tushunchasi.",
 vaqt=1200),

"Sensorni o'qib, shartga qarab qurilmani boshqarish": NZ(
 "SensorBlock",
 "Sensor blokli dasturda o'qilib, shart bloki bilan qurilma boshqariladi.",
 ["Sensor ulanadi va qiymat ko'riladi", "Chegara o'lchov asosida tanlanadi",
  "Shart bloki bilan boshqaruv yoziladi", "Tizim sinaladi"],
 [("5", "Tizim ishlaydi, chegara o'lchov asosida tanlangan"),
  ("4", "Tizim ishlaydi, chegara taxminan tanlangan"),
  ("3", "Yordam bilan ishladi"),
  ("2", "Sensor o'qildi, boshqaruv ishlamadi"),
  ("Bajarilmadi", "Sensor qiymatlari olinmadi")],
 "Chegarani o'lchov asosida tanlashni talab qiling — taxminiy chegara bilan tizim ishlashi mumkin, lekin bu tasodif.",
 vaqt=1200),

"O'z loyihangni mustaqil yig'ib, dasturlab ko'rsatish": NZ(
 "ProjectDemo",
 "O'quvchi o'zi tanlagan qurilmani yig'adi, dasturlaydi va ishlatib ko'rsatadi.",
 ["Loyiha rejasi ko'rsatiladi", "Qurilma yig'iladi va ishlaydi",
  "Dastur tushuntiriladi", "Savollarga javob beriladi"],
 [("5", "Qurilma ishlaydi, reja bor, dastur to'liq tushuntirildi"),
  ("4", "Qurilma ishlaydi, tushuntirish qisman"),
  ("3", "Qurilma qisman ishlaydi"),
  ("2", "Qurilma yig'ilgan, ishlamaydi"),
  ("Bajarilmadi", "Loyiha tayyorlanmadi")],
 "Tushuntirishni yig'ish bilan teng baholang: o'zi yasagan qurilmani tushuntira olmaslik — bu ko'chirib olishning belgisi.",
 vaqt=1800),

"Sxemani yig'ib, matnli dastur yozish": NZ(
 "TextCode",
 "Sxema yig'ilib, matnli Arduino kodi mustaqil yoziladi.",
 ["Sxema yig'iladi", "Kod matnli ko'rinishda yoziladi",
  "Kompilyatsiya xatolari mustaqil tuzatiladi", "Dastur ishlaydi"],
 [("5", "20 daqiqagacha ishladi, kod izohli va tartibli"),
  ("4", "Ishladi, kod izohsiz"),
  ("3", "Yordam bilan xatolar tuzatildi"),
  ("2", "Kod yozildi, lekin kompilyatsiya bo'lmadi"),
  ("Bajarilmadi", "Kod yozilmadi")],
 "Kompilyatsiya xatolarini mustaqil tuzatishni alohida baholang — bu matnli dasturlashning eng muhim boshlang'ich ko'nikmasi.",
 vaqt=1500),

"Shart va sikl ishlatilgan dastur yozish": NZ(
 "LogicCode",
 "Shart, sikl va o'zgaruvchi ishlatilgan dastur mustaqil yoziladi.",
 ["Algoritm qog'ozda yoziladi", "Kod yozilib, sikl va shart ishlatiladi",
  "Dastur ishlaydi va sinaladi", "Kod tushuntiriladi"],
 [("5", "Ishladi, sikl va shart to'g'ri ishlatildi, algoritm chizilgan"),
  ("4", "Ishladi, algoritm chizilmagan"),
  ("3", "Qisman ishladi yoki mantiqda xato bor"),
  ("2", "Kod yozildi, ishlamadi"),
  ("Bajarilmadi", "Bajarilmadi")],
 "Algoritmni qog'ozda yozishni majburiy band qiling — rejasiz kod yozish bu yoshdagi eng ko'p vaqt yo'qotadigan odat.",
 vaqt=1500),

"Sensor qiymatiga qarab ishlaydigan dastur yozish": NZ(
 "AnalogLogic",
 "Analog sensor o'qilib, map va shart bilan ijro qurilmasi boshqariladi.",
 ["Sensor kalibrlanadi va qiymatlar yoziladi", "map va constrain ishlatiladi",
  "Shart bilan boshqaruv amalga oshiriladi", "Tizim sinaladi va sozlanadi"],
 [("5", "Tizim ishlaydi, kalibrlash hujjatlashtirilgan, constrain bor"),
  ("4", "Tizim ishlaydi, kalibrlash yozilmagan"),
  ("3", "Ishlaydi, lekin chegaralar taxminan"),
  ("2", "Sensor o'qildi, boshqaruv ishlamadi"),
  ("Bajarilmadi", "Bajarilmadi")],
 "Kalibrlash yozuvini talab qiling — bu sensorli tizimda eng ko'p e'tibordan chetda qoladigan, lekin eng muhim qadam.",
 vaqt=1500),

"Ko'p komponentli qurilmani yig'ib dasturlash": NZ(
 "FullDevice",
 "Sensor, ijro qurilmasi va ekrandan iborat to'liq qurilma yig'ilib dasturlanadi.",
 ["Komponentlar bittalab qo'shilib sinaladi", "Barchasi birga ishlaydi",
  "Kod funksiyalarga bo'lingan", "millis() bilan vaqt boshqariladi"],
 [("5", "To'liq ishlaydi, kod funksiyalarga bo'lingan, millis ishlatilgan"),
  ("4", "To'liq ishlaydi, delay bilan"),
  ("3", "Ko'pchiligi ishlaydi"),
  ("2", "Yarmi ishlaydi"),
  ("Bajarilmadi", "Yig'ilmadi")],
 "millis() ishlatilganini alohida baholang — delay bilan ham ishlaydi, lekin ko'p komponentli tizimda bu chegara yaratadi.",
 vaqt=1800),

"ESP32'da sensor o'qib, OLED'da ko'rsatish": NZ(
 "OledMonitor",
 "ESP32 ga sensor va OLED ulanib, qiymat ekranda ko'rsatiladi.",
 ["Sensor 3.3 V mosligini hisobga olib ulanadi", "OLED I2C bilan ishga tushadi",
  "Qiymat ekranda yangilanadi", "Ekran maketi rejalangan va o'lchov birligi bor"],
 [("5", "Ishlaydi, ekran tartibli, yangilash chastotasi boshqarilgan"),
  ("4", "Ishlaydi, ekran rejalanmagan"),
  ("3", "Ishlaydi, lekin ekran miltillaydi"),
  ("2", "Sensor yoki ekrandan biri ishlamadi"),
  ("Bajarilmadi", "Bajarilmadi")],
 "3.3 V moslikni birinchi band qilib tekshiring — noto'g'ri ulash modulni buzadi va nazorat davomida buni oldini olish kerak.",
 vaqt=1800),

"WiFi orqali ma'lumot yuboradigan va boshqariladigan tizim": NZ(
 "WiFiSystem",
 "Ikki tomonlama tizim: sensor ma'lumoti yuboriladi va qurilma uzoqdan boshqariladi.",
 ["WiFi ga ulanish va qayta ulanish mantiqi", "Ma'lumot muntazam yuboriladi",
  "Uzoqdan boshqaruv ishlaydi", "Xavfsizlik (parol yoki ID tekshiruvi) bor"],
 [("5", "Ikki tomonlama ishlaydi, qayta ulanish va himoya bor"),
  ("4", "Ikki tomonlama ishlaydi, himoya yo'q"),
  ("3", "Faqat bir tomon ishlaydi"),
  ("2", "Aloqa bor, lekin beqaror"),
  ("Bajarilmadi", "Aloqa o'rnatilmadi")],
 "Xavfsizlikni alohida band qiling — himoyasiz tizim ishlaydi, lekin u tayyor mahsulot emas. Bu farqni baholash orqali o'rgating.",
 vaqt=1800),

"Imo-ishora tanuvchi modelni o'rgatib, qurilmada ishlatish": NZ(
 "GestureML",
 "Uch imo-ishora uchun model o'rgatilib, qurilmaga joylanadi va real vaqtda sinaladi.",
 ["Har sinf uchun kamida 30 namuna yig'ilgan", "Model o'rgatilgan va chalkashlik matritsasi tahlil qilingan",
  "Model qurilmaga joylangan", "Real aniqlik 20 urinishda sanab o'lchangan"],
 [("5", "Real aniqlik 80% dan yuqori, matritsa tahlil qilingan"),
  ("4", "Real aniqlik 60-80%"),
  ("3", "Real aniqlik 40-60% yoki model qurilmada ishlaydi lekin o'lchanmagan"),
  ("2", "Model o'rgatildi, qurilmaga joylanmadi"),
  ("Bajarilmadi", "Ma'lumot yig'ilmadi")],
 "Real aniqlikni sanab o'lchashni majburiy qiling — platformadagi foiz real ishlashni ko'rsatmaydi va bu farq muhim tushuncha.",
 vaqt=2400),

"Ovoz yoki tasvir tanuvchi tizimni ishga tushirish": NZ(
 "SenseAI",
 "Ovoz yoki tasvir tanuvchi model o'rgatilib, qurilmada ishlatiladi.",
 ["Dataset yig'ilgan, \"boshqa\" sinfi ham bor", "Model o'rgatilgan va kvantlangan",
  "Qurilmada ishlaydi va bashorat vaqti o'lchangan", "Chegara bilan filtrlash bor"],
 [("5", "Ishlaydi, real aniqlik 75% dan yuqori, bashorat vaqti o'lchangan"),
  ("4", "Ishlaydi, aniqlik 60-75%"),
  ("3", "Ishlaydi, lekin aniqlik past yoki o'lchanmagan"),
  ("2", "Model o'rgatildi, qurilmada ishlamadi"),
  ("Bajarilmadi", "Bajarilmadi")],
 "\"Boshqa\" sinfini alohida band qiling — usiz tizim har tovushni buyruq deb tanidi va amalda ishlatib bo'lmaydi.",
 vaqt=2400),

"Ko'p sensorli o'lchov tizimini yig'ib, ma'lumotni yozib borish": NZ(
 "DataStation",
 "Uch va undan ortiq sensorli o'lchov tizimi yig'ilib, ma'lumot vaqt bilan yoziladi.",
 ["Sensorlar kalibrlangan va hujjatlashtirilgan", "Ma'lumot vaqt belgisi bilan yoziladi",
  "Filtrlash qo'llanilgan", "Fayl formati (CSV) to'g'ri va o'qiladi"],
 [("5", "Tizim ishlaydi, kalibrlash hujjati bor, filtrlash qo'llangan"),
  ("4", "Tizim ishlaydi, filtrlash yo'q"),
  ("3", "Ma'lumot yoziladi, lekin vaqt belgisi yo'q yoki format noto'g'ri"),
  ("2", "Sensorlar ishlaydi, yozish ishlamaydi"),
  ("Bajarilmadi", "Bajarilmadi")],
 "Yozilgan faylni kompyuterda ochib tekshiring — close() unutilgan bo'lsa fayl bo'sh chiqadi va bu darhol ko'rinadi.",
 vaqt=2400),

"To'liq IoT tizimini yig'ib, uzoqdan boshqarish": NZ(
 "IoTSystem",
 "Uch qatlamli (qurilma, tarmoq, interfeys) to'liq IoT tizimi yig'iladi.",
 ["Arxitektura chizmasi tayyorlangan", "Qurilma ma'lumot yuboradi va buyruq qabul qiladi",
  "Interfeys (veb yoki Telegram) ishlaydi", "Xavfsizlik va qayta ulanish mantiqi bor"],
 [("5", "Tizim to'liq ishlaydi, arxitektura chizilgan, himoya va tiklanish bor"),
  ("4", "Tizim ishlaydi, himoya yoki tiklanish yo'q"),
  ("3", "Asosiy funksiya ishlaydi, tizim beqaror"),
  ("2", "Qismlar alohida ishlaydi"),
  ("Bajarilmadi", "Tizim yig'ilmadi")],
 "Arxitektura chizmasini talab qiling — 8-sinf darajasida tizimni ko'ra olish yig'a olishdan muhimroq ko'nikma.",
 vaqt=2400),

"Model o'rgatib, qurilmaga joylash va aniqligini o'lchash": NZ(
 "MLDeploy",
 "Model to'liq sikl bo'yicha o'rgatilib, kvantlanadi, joylanadi va o'lchanadi.",
 ["Dataset muvozanatli va hujjatlashtirilgan", "Model o'rgatilgan, overfitting tekshirilgan",
  "Kvantlangan va resurs sarfi o'lchangan", "Real aniqlik, precision va recall hisoblangan"],
 [("5", "To'liq sikl bajarildi, barcha ko'rsatkichlar o'lchangan va tahlil qilingan"),
  ("4", "Model ishlaydi, ko'rsatkichlar qisman o'lchangan"),
  ("3", "Model qurilmada ishlaydi, o'lchov yo'q"),
  ("2", "Model o'rgatildi, joylanmadi"),
  ("Bajarilmadi", "Bajarilmadi")],
 "Precision va recall ni talab qiling — 8-sinf darajasida faqat aniqlik yetarli emas va bu farqni tushunish muhim.",
 vaqt=2400),

"Loyihani texnik topshiriq bo'yicha bajarib, himoya qilish": NZ(
 "EngineeringDefense",
 "Yakuniy loyiha texnik topshiriq talablari bo'yicha bajarilib, himoya qilinadi.",
 ["TZ dagi har talab tekshiriladi va natija ko'rsatiladi", "Qurilma ishlaydi va namoyish qilinadi",
  "Texnik hujjat to'liq", "Savollarga asoslangan javob beriladi"],
 [("5", "TZ talablari bajarilgan, hujjat to'liq, himoya ishonchli"),
  ("4", "Talablarning ko'pchiligi bajarilgan, hujjat to'liq"),
  ("3", "Qurilma ishlaydi, lekin hujjat to'liq emas"),
  ("2", "Qurilma qisman ishlaydi"),
  ("Bajarilmadi", "Loyiha tayyorlanmadi")],
 "Baholashni TZ talablari bo'yicha bandma-band bajaring. Bu obyektiv, munozarasiz va real muhandislik amaliyotiga mos.",
 vaqt=2700),
}


# ==================================================================== LOYIHA
LOYIHA = {
"Qo'l chirog'i: korpusli, tugmali, ishlaydigan qurilma": LY(
 "Qo'l chirog'i",
 ["Kamida 2 ta LED, har biriga o'z rezistori", "Kalit yoki tugma bilan boshqariladi",
  "Batareya joyi almashtiriladigan", "Karton yoki plastik korpus", "Qo'lda ushlash qulay"],
 [("Zanjir ishlaydi", 30), ("Rezistorlar to'g'ri hisoblangan", 15),
  ("Korpus mustaqil va ishlashga qulay", 20), ("Batareya almashtiriladigan", 10),
  ("Toza montaj", 15), ("Taqdimot", 10)],
 "Korpusni karton bilan yasashga ruxsat bering — maqsad chiroyli emas, ishlaydigan va o'ylab qilingan konstruksiya."),

"Yorug'lik rostlagichli chiroq (potensiometrli)": LY(
 "Rostlanadigan chiroq",
 ["Potensiometr bilan yorqinlik silliq o'zgaradi", "Kamida 3 ta LED",
  "Rezistorlar hisoblab tanlangan", "Korpus va boshqaruv tugmasi tashqarida", "O'lchov protokoli"],
 [("Yorqinlik silliq o'zgaradi", 30), ("Hisob va o'lchov protokoli", 20),
  ("Korpus va ergonomika", 20), ("Toza montaj", 15), ("Taqdimot", 15)],
 "O'lchov protokolini majburiy qiling — bu chorak o'lchovga bag'ishlangan va loyiha ham shuni aks ettirishi kerak."),

"Avtomatik tungi chiroq: qorong'ida o'zi yonadi": LY(
 "Tungi chiroq",
 ["Fotorezistor bilan qorong'ida avtomatik yonadi", "Sezgirlik potensiometr bilan sozlanadi",
  "Tranzistorli boshqaruv", "Miltillamaydi (sensor chiroqdan uzoqda)", "Korpus"],
 [("Avtomatik ishlaydi", 30), ("Sezgirlik sozlanadi", 15),
  ("Miltillash yo'q", 15), ("Korpus va joylashuv o'ylangan", 20), ("Taqdimot", 20)],
 "Miltillash muammosini alohida baholang — uni hal qilish uchun sensor joylashuvini o'ylash kerak va bu muhandislik qarori."),

"Signalizatsiya qurilmasi: sensor + tovush + yorug'lik": LY(
 "Signalizatsiya",
 ["Sensor (reed, PIR yoki fotorezistor) bilan ishga tushadi", "Tovush va yorug'lik signali",
  "Yoqish/o'chirish kaliti", "Sezgirlik sozlanadi", "Korpus"],
 [("Sensor ishga tushiradi", 25), ("Tovush va yorug'lik ishlaydi", 20),
  ("Sozlash imkoniyati", 15), ("Korpus va o'rnatish", 20), ("Taqdimot", 20)],
 "Sensor turini o'quvchi o'zi tanlasin va tanlovini asoslasin — bu chorak yakunida komponent tanlash ko'nikmasini tekshiradi."),

"Uch rejimli chiroq: kuchsiz, o'rtacha, kuchli": LY(
 "Uch rejimli chiroq",
 ["Kalit bilan uch rejim tanlanadi", "Har rejimda LEDlar boshqacha ulanadi (ketma-ket/parallel/aralash)",
  "Har rejimdagi tok o'lchanib hujjatlashtirilgan", "Korpus"],
 [("Uch rejim ishlaydi", 30), ("Ulanish sxemasi to'g'ri va chizilgan", 20),
  ("O'lchov jadvali", 15), ("Korpus", 20), ("Taqdimot", 15)],
 "Har rejimdagi tokni o'lchashni talab qiling — bu ketma-ket va parallel ulanish farqini raqamlarda ko'rsatadi."),

"Batareya sinovchi qurilma": LY(
 "Batareya sinovchi",
 ["Batareya kuchlanishi ko'rsatiladi", "Yuklamali sinov rejimi bor",
  "Uch daraja ko'rsatkichi (yaxshi/o'rtacha/yaroqsiz)", "Turli batareya o'lchamlariga mos", "Korpus"],
 [("Kuchlanish o'lchanadi", 25), ("Yuklamali sinov ishlaydi", 25),
  ("Ko'rsatkich aniq va tushunarli", 15), ("Korpus va kontaktlar", 20), ("Taqdimot", 15)],
 "Yuklamali sinovni alohida baholang — bu chorakda o'rganilgan ichki qarshilik tushunchasining amaliy qo'llanishi."),

"Avtomatik yoritish tizimi": LY(
 "Avtomatik yoritish",
 ["Fotorezistor va harakat datchigi birga ishlatiladi", "Tranzistor yoki rele bilan boshqaruv",
  "Ikki shart mantiqi (VA yoki YOKI) asoslangan", "Sozlash imkoniyati", "Korpus"],
 [("Ikki sensorli mantiq ishlaydi", 30), ("Mantiq tanlovi asoslangan", 15),
  ("Boshqaruv va himoya to'g'ri", 20), ("Korpus va o'rnatish", 20), ("Taqdimot", 15)],
 "Mantiq tanlovini (VA yoki YOKI) asoslashni talab qiling — bu chorak mantiq amallariga bag'ishlangan va tanlov ongli bo'lishi kerak."),

"Avtomatik sug'orish tizimi (elektron, platasiz)": LY(
 "Sug'orish tizimi",
 ["Tuproq namligi sensori bilan ishga tushadi", "Nasos yoki klapan rele orqali boshqariladi",
  "Chegara sozlanadi", "Xavfsizlik: nasos ishlash vaqti cheklangan", "Suvga chidamli montaj"],
 [("Avtomatik ishlaydi", 30), ("Chegara sozlanadi va kalibrlangan", 15),
  ("Nasos vaqti cheklangan", 15), ("Suv va elektr xavfsizligi", 20), ("Taqdimot", 20)],
 "Nasos ishlash vaqtining cheklovini majburiy qiling — sensor buzilsa nasos to'xtovsiz ishlaydi va bu real xavf."),

"Elektron reaksiya o'yini (platasiz, tranzistorli)": LY(
 "Reaksiya o'yini",
 ["Tasodifiy vaqtdan keyin signal beradi", "Ikki o'yinchi tugmasi",
  "Kim birinchi bosgani ko'rsatiladi", "Faqat elektronika, mikrokontrollersiz", "Korpus"],
 [("O'yin ishlaydi", 30), ("G'olibni aniqlash to'g'ri", 20),
  ("Sxema mustaqil loyihalangan", 20), ("Korpus", 15), ("Taqdimot", 15)],
 "Mikrokontrollersiz cheklovni saqlang — bu 1-chorak yakuni va faqat elektronika bilan mantiq qurish ko'nikmasini tekshiradi."),

"Reaksiya tezligi o'yini (Arduino'da)": LY(
 "Reaksiya o'yini (Arduino)",
 ["Tasodifiy kutish vaqti", "Reaksiya vaqti millisekundda o'lchanadi",
  "Natija Serial monitorda yoki ekranda", "Eng yaxshi natija saqlanadi", "Uch urinish o'rtachasi"],
 [("O'yin ishlaydi", 25), ("Vaqt aniq o'lchanadi", 20),
  ("Natija saqlanadi va ko'rsatiladi", 20), ("Kod toza va izohli", 20), ("Taqdimot", 15)],
 "Kod sifatini yuqori baholang (20 ball) — bu birinchi Arduino loyihasi va kod madaniyatini shu yerda o'rnatish kerak."),

"Oddiy ob-havo stansiyasi": LY(
 "Ob-havo stansiyasi",
 ["Kamida 2 ta sensor (harorat, namlik yoki yorug'lik)", "Qiymatlar Serial monitorda ko'rsatiladi",
  "Sensorlar kalibrlangan", "Chegaradan oshganda ogohlantirish", "Kod funksiyalarga bo'lingan"],
 [("Sensorlar ishlaydi", 25), ("Kalibrlash hujjati", 15),
  ("Ogohlantirish ishlaydi", 20), ("Kod tuzilmasi", 20), ("Taqdimot", 20)],
 "Kalibrlash hujjatini talab qiling — bu chorak sensorlarga bag'ishlangan va kalibrlash uning asosiy ko'nikmasi."),

"Aqlli uy maketi: sensor, ekran, ijro qurilmasi": LY(
 "Aqlli uy maketi",
 ["Kamida 2 sensor, 1 ekran va 2 ijro qurilmasi", "Avtomatik va qo'lda rejimlar",
  "IR pult bilan boshqarish", "Karton uy maketi", "To'liq hujjat: sxema, BOM, izohli kod"],
 [("Tizim to'liq ishlaydi", 30), ("Ikki rejim ishlaydi", 15),
  ("Maket va montaj sifati", 15), ("Hujjat to'liqligi", 20), ("Taqdimot va himoya", 20)],
 "Hujjatga 20 ball bering — bu yil yakuni va hujjatlashtirish ko'nikmasi keyingi yillarda hal qiluvchi bo'ladi."),

"Yorug'lik va tovushli reaksiya o'yini": LY(
 "Reaksiya o'yini (yorug'lik va tovush)",
 ["Yorug'lik va tovush signallari", "Ikki o'yinchi rejimi",
  "Ball hisobi va g'olib aniqlanadi", "Reaksiya vaqti o'lchanadi", "Kod funksiyalarga bo'lingan"],
 [("O'yin to'liq ishlaydi", 30), ("Ball hisobi to'g'ri", 20),
  ("Kod tuzilmasi va izohlar", 25), ("Korpus", 10), ("Taqdimot", 15)],
 "Kod tuzilmasiga 25 ball — 8-sinf jadal kursida kod sifatini boshidan yuqori talab qilish kerak."),

"Kirish nazorati tizimi (RFID + servo qulf)": LY(
 "Kirish nazorati",
 ["RFID kartani o'qiydi (3.3 V ga to'g'ri ulangan)", "Ruxsat berilgan kartalar ro'yxati",
  "Servo qulfni ochadi va yopadi", "Ekranda holat ko'rsatiladi", "Ruxsatsiz urinish qayd etiladi"],
 [("Tizim ishlaydi", 30), ("Kartalar ro'yxati va tekshiruv", 20),
  ("Qulf mexanizmi", 15), ("Ekran va qayd", 15), ("Taqdimot va xavfsizlik tahlili", 20)],
 "Xavfsizlik tahlilini talab qiling: UID nusxalanishi mumkinligini o'quvchi bilishi va aytishi kerak. Bu halol muhandislik."),

"Veb orqali boshqariladigan yoritish tizimi": LY(
 "Veb yoritish tizimi",
 ["Brauzerdan kamida 3 kanal boshqariladi", "Sahifa telefonda ham qulay",
  "Yorqinlik PWM bilan sozlanadi", "Holat sahifada ko'rsatiladi", "Statik IP yoki qulay manzil"],
 [("Boshqaruv ishlaydi", 30), ("Interfeys qulayligi", 20),
  ("Yorqinlik sozlanadi", 15), ("Barqarorlik va qayta ulanish", 20), ("Taqdimot", 15)],
 "Telefonda sinashni majburiy qiling — bu real foydalanish sharoiti va interfeys sifatini darhol ko'rsatadi."),

"IoT ob-havo stansiyasi: sensor, bulut, Telegram": LY(
 "IoT ob-havo stansiyasi",
 ["Kamida 2 sensor, ma'lumot bulutga yuboriladi", "Telegram orqali so'rov va ogohlantirish",
  "SD kartga zaxira yozuv", "Qayta ulanish mantiqi", "Batareya yoki quvvat hisobi"],
 [("Tizim to'liq ishlaydi", 25), ("Bulut va Telegram ishlaydi", 20),
  ("Zaxira yozuv va tiklanish", 20), ("Hujjat va quvvat hisobi", 20), ("Taqdimot", 15)],
 "Zaxira yozuvni alohida baholang — aloqa uzilganda ma'lumot yo'qolmasligi IoT tizimining sifat belgisi."),

"Miltillovchi chiroq: o'z ritmingda": LY(
 "Miltillovchi chiroq",
 ["Kamida 3 LED, o'z ritmi bilan miltillaydi", "Blokli dastur bilan yozilgan",
  "Sikl ishlatilgan", "Ritm o'quvchi tomonidan o'ylab topilgan", "Korpus"],
 [("Ishlaydi va yuklangan", 30), ("Sikl ishlatilgan", 20),
  ("Ijodkorlik (o'ziga xos ritm)", 20), ("Korpus", 15), ("Taqdimot", 15)],
 "Ijodkorlikni alohida baholang — bu birinchi dasturlash loyihasi va o'z g'oyasini kiritish motivatsiya beradi."),

"Musiqali yoritgich: tovush va rang birga": LY(
 "Musiqali yoritgich",
 ["Melodiya chalinadi (kamida 8 nota)", "RGB LED rang o'zgartiradi",
  "Tovush va rang o'zaro bog'langan", "Blokli dastur, sikl va o'zgaruvchi bilan", "Korpus"],
 [("Melodiya va rang ishlaydi", 30), ("Ular o'zaro bog'langan", 20),
  ("Dastur tartibli", 20), ("Korpus", 15), ("Taqdimot", 15)],
 "Tovush va rangning bog'lanishini talab qiling — bu ikki qurilmani birga boshqarish ko'nikmasini tekshiradi."),

"Aqlli gulzor: quruq bo'lsa signal beradi": LY(
 "Aqlli gulzor",
 ["Tuproq namligi sensori kalibrlangan", "Quruq bo'lsa tovush va yorug'lik signali",
  "Chegara sozlanadi", "Sensor davriy o'lchaydi (doimiy quvvatsiz)", "Gulzorga o'rnatiladigan konstruksiya"],
 [("Avtomatik ishlaydi", 30), ("Kalibrlash bajarilgan", 20),
  ("Davriy o'lchash", 15), ("Konstruksiya", 20), ("Taqdimot", 15)],
 "Davriy o'lchashni alohida baholang — bu sensor umrini uzaytiradi va o'quvchilar buni real muammo sifatida ko'radi."),

"Yakuniy loyiha: o'zi tanlagan aqlli qurilma": LY(
 "Yakuniy loyiha (5-sinf)",
 ["G'oya o'quvchi tomonidan tanlangan va asoslangan", "Kamida 1 sensor va 1 ijro qurilmasi",
  "Blokli dastur, shart va sikl bilan", "Algoritm chizmasi", "Korpus va qo'llanma"],
 [("Qurilma ishlaydi", 25), ("G'oya asoslangan", 15), ("Algoritm chizmasi", 15),
  ("Korpus va qo'llanma", 20), ("Taqdimot va himoya", 25)],
 "Taqdimotga 25 ball bering — yil yakunida o'z ishini tushuntira olish qurilmani yasashdan kam ahamiyatli emas."),

"Svetofor maketi: uch chiroq, to'g'ri ketma-ketlik": LY(
 "Svetofor maketi",
 ["Uch chiroq to'g'ri ketma-ketlikda", "Piyodalar tugmasi qo'shilgan",
  "Matnli kod, izohli", "Vaqtlar o'zgaruvchilarda saqlangan", "Maket va korpus"],
 [("Sikl to'g'ri ishlaydi", 30), ("Piyodalar tugmasi", 15),
  ("Kod tuzilmasi va izohlar", 25), ("Maket", 15), ("Taqdimot", 15)],
 "Vaqtlarni o'zgaruvchilarga chiqarishni talab qiling — bu \"sehrli raqamlar\" muammosining amaliy yechimi."),

"Elektron o'yin: reaksiya va ball hisobi": LY(
 "Elektron o'yin",
 ["O'yin mantiqi aniq va tushunarli", "Ball hisobi va saqlanishi",
  "Bir necha daraja yoki rejim", "Kod funksiyalarga bo'lingan", "Massiv ishlatilgan"],
 [("O'yin ishlaydi", 25), ("Ball hisobi to'g'ri", 20),
  ("Funksiya va massiv ishlatilgan", 25), ("Korpus", 10), ("Taqdimot", 20)],
 "Funksiya va massiv ishlatilganini alohida baholang — bu chorakning asosiy texnik maqsadlari."),

"Ob-havo stansiyasi: harorat, namlik, yorug'lik": LY(
 "Ob-havo stansiyasi",
 ["Uch sensor: harorat, namlik, yorug'lik", "Barchasi kalibrlangan va hujjatlashtirilgan",
  "Qiymatlar ekranda ko'rsatiladi", "Filtrlash (o'rtacha yoki mediana)", "Chegaradan oshganda ogohlantirish"],
 [("Uch sensor ishlaydi", 25), ("Kalibrlash hujjati", 20),
  ("Filtrlash qo'llanilgan", 20), ("Ekran va ogohlantirish", 20), ("Taqdimot", 15)],
 "Filtrlashni talab qiling — xom sensor qiymatlari tebranadi va buni hal qilish real muhandislik vazifasi."),

"Aqlli uy maketi: to'liq tizim": LY(
 "Aqlli uy (6-sinf)",
 ["Kamida 3 sensor va 3 ijro qurilmasi", "LCD ekran va IR pult",
  "Avtomatik va qo'lda rejim", "Kod modullarga bo'lingan, millis ishlatilgan", "To'liq hujjat: sxema, BOM, kod"],
 [("Tizim to'liq ishlaydi", 25), ("Ikki rejim va pult", 20),
  ("Kod tuzilmasi", 20), ("Hujjat", 20), ("Taqdimot va himoya", 15)],
 "Kod tuzilmasi va hujjatga 40 ball birga — 6-sinf yakunida texnik madaniyat qurilmadan kam muhim emas."),

"Ma'lumot yozib boruvchi qurilma (data logger)": LY(
 "Data logger",
 ["Kamida 2 sensor, RTC bilan vaqt belgisi", "SD kartga CSV formatda yozadi",
  "OLED ekranda joriy holat", "Deep sleep bilan quvvat tejash", "Batareya muddati hisoblangan"],
 [("Yozish to'g'ri ishlaydi", 25), ("Vaqt belgisi va format", 20),
  ("Ekran va holat", 15), ("Quvvat tejash va hisob", 25), ("Taqdimot", 15)],
 "Quvvat hisobiga 25 ball — bu ESP32 chorakning asosiy yangi ko'nikmasi va real loyihalarda hal qiluvchi."),

"IoT monitoring tizimi": LY(
 "IoT monitoring",
 ["Sensor ma'lumoti bulutga yuboriladi", "Veb-panel yoki Telegram interfeysi",
  "Ogohlantirish tizimi (chegara bilan)", "Qayta ulanish va zaxira", "Xavfsizlik: parol yoki ID tekshiruvi"],
 [("Tizim ishlaydi", 25), ("Interfeys sifati", 20),
  ("Ogohlantirish mantiqi", 20), ("Barqarorlik va himoya", 20), ("Taqdimot", 15)],
 "Barqarorlikni 24 soatlik sinov bilan tekshiring — IoT tizimida bu eng muhim va eng ko'p e'tibordan chetda qoladigan sifat."),

"Imo-ishora bilan boshqariladigan qurilma": LY(
 "Imo-ishora boshqaruvi",
 ["Kamida 3 imo-ishora tanuvchi model", "Har sinf uchun 30+ namuna, turli odamlardan",
  "Model qurilmada ishlaydi", "Tanilgan imo-ishora qurilmani boshqaradi", "Real aniqlik o'lchangan va hujjatlashtirilgan"],
 [("Model ishlaydi", 25), ("Dataset sifati", 20),
  ("Boshqaruv ishlaydi", 20), ("Aniqlik o'lchovi va tahlil", 20), ("Taqdimot", 15)],
 "Dataset sifatiga 20 ball — ML loyihasida ma'lumot sifati model turidan muhimroq va buni baholash orqali ko'rsatish kerak."),

"Yakuniy AI loyihasi: ko'radigan yoki eshitadigan qurilma": LY(
 "Yakuniy AI loyihasi (7-sinf)",
 ["Ovoz yoki tasvir tanuvchi model", "\"Boshqa\" sinfi bilan dataset",
  "Model kvantlangan va qurilmada ishlaydi", "Natija amaliy harakatga aylantiriladi", "AI axloqi tahlil qilingan"],
 [("Tizim ishlaydi", 25), ("Dataset va model sifati", 20),
  ("Amaliy qo'llash", 20), ("Axloqiy tahlil va hujjat", 20), ("Taqdimot va himoya", 15)],
 "Axloqiy tahlilni majburiy band qiling — AI loyihasida bu texnik sifat kabi muhim va o'quvchilar buni o'rganishi kerak."),

"Muhandislik o'lchov stansiyasi": LY(
 "O'lchov stansiyasi",
 ["Kamida 4 sensor (harorat, bosim, tok, og'irlik)", "Barchasi etalon bilan kalibrlangan",
  "Filtrlash va aniqlik tahlili", "SD kartga yozish va OLED ko'rsatish", "O'lchov noaniqligi hisoblangan"],
 [("Tizim ishlaydi", 20), ("Kalibrlash hujjati", 25),
  ("Filtrlash va aniqlik tahlili", 20), ("Yozish va ko'rsatish", 20), ("Taqdimot", 15)],
 "Kalibrlashga 25 ball — bu chorak o'lchov aniqligiga bag'ishlangan va bu ko'nikma har qanday muhandislikda asosiy."),

"Aqlli uy IoT tizimi: bir nechta qurilma": LY(
 "Aqlli uy IoT",
 ["Kamida 2 mustaqil qurilma, o'zaro aloqa bilan", "MQTT yoki ESP-NOW protokoli",
  "Markaziy interfeys (veb yoki Telegram)", "Arxitektura chizmasi va mavzular tuzilmasi", "Xavfsizlik va OTA"],
 [("Tizim ishlaydi", 25), ("Arxitektura va protokol", 20),
  ("Interfeys", 15), ("Xavfsizlik va OTA", 20), ("Hujjat va taqdimot", 20)],
 "Arxitektura chizmasini talab qiling — ko'p qurilmali tizimda uni ko'ra olmasdan boshqarib bo'lmaydi."),

"Anomaliya aniqlovchi tizim (nosozlikni oldindan sezish)": LY(
 "Anomaliya aniqlash",
 ["Normal holat ma'lumoti yig'ilgan", "Anomaliya aniqlash modeli o'rgatilgan",
  "Qurilmada real vaqtda ishlaydi", "Yolg'on signal darajasi o'lchangan", "Ogohlantirish tizimi"],
 [("Model ishlaydi", 25), ("Dataset va usul tanlovi asoslangan", 20),
  ("Yolg'on signal tahlili", 20), ("Ogohlantirish tizimi", 15), ("Hujjat va taqdimot", 20)],
 "Yolg'on signal darajasini o'lchashni talab qiling — anomaliya aniqlashda bu asosiy sifat ko'rsatkichi va uni bilmasdan tizim foydasiz."),

"Yakuniy loyiha: AI integratsiyalangan IoT qurilmasi": LY(
 "Yakuniy muhandislik loyihasi",
 ["Texnik topshiriq yozilgan va bajarilgan", "AI modeli va IoT aloqasi birga ishlaydi",
  "Tizim arxitekturasi hujjatlashtirilgan", "Sinov natijalari raqamlar bilan", "Foydalanuvchi qo'llanmasi va texnik hujjat"],
 [("TZ talablari bajarilgan", 25), ("AI va IoT integratsiyasi", 20),
  ("Sinov natijalari va tahlil", 20), ("Hujjat to'liqligi", 20), ("Himoya", 15)],
 "Baholashni TZ bandlari bo'yicha bajaring. Bu 8 yillik dasturning yakuni — talablarga muvofiqlikni baholash professional amaliyotga to'liq mos keladi."),
}
