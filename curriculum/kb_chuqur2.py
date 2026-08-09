# -*- coding: utf-8 -*-
"""
NAZARIYANI CHUQURLASHTIRISH — 2-qism: sun'iy intellekt va muhandislik.

Tuzilishi kb_chuqur.py bilan bir xil. Ikkalasi kb_chuqur.CHUQUR ichida
birlashtiriladi.
"""


def D(*bloklar):
    return [(sarlavha, list(bandlar)) for sarlavha, bandlar in bloklar]


CHUQUR2 = {

# ============================================================ AI ASOSLARI
"Sun'iy intellekt, mashinaviy o'rganish, TinyML": D(
 ("Uch tushuncha bir-birining ichida", [
  "Sun'iy intellekt (AI) — eng keng tushuncha: inson aqliy vazifalarini bajaradigan har qanday tizim. Shaxmat dasturi ham, qoidalar to'plami ham unga kiradi.",
  "Mashinaviy o'rganish (ML) — AI ning bir qismi: qoidalar YOZILMAYDI, ular ma'lumotdan TOPILADI.",
  "Chuqur o'rganish (Deep Learning) — ML ning bir qismi: ko'p qatlamli neyron tarmoqlar ishlatiladi.",
  "TinyML — chuqur o'rganishning eng kichik varianti: model mikrokontrollerga sig'adigan darajada kichraytiriladi.",
  "Ya'ni bular raqobatchi emas, bir-birining ichidagi doiralar: AI > ML > DL > TinyML.",
 ]),
 ("TinyML ning o'lchamlari", [
  "Oddiy kompyuterdagi model bir necha gigabayt bo'lishi mumkin. Mikrokontrollerda esa atigi bir necha yuz kilobayt xotira bor.",
  "XIAO ESP32S3 da 8 MB PSRAM bor — bu telefondagi xotiraning mingdan bir qismi.",
  "Shuning uchun model siqiladi: sonlar 32 bitdan 8 bitga tushiriladi, keraksiz bog'lanishlar olib tashlanadi.",
  "Natijada model 4-10 barobar kichrayadi va tezlashadi, aniqligi esa odatda 1-2 % gina tushadi.",
 ]),
 ("Nima uchun modelni qurilmada ishlatish kerak", [
  "Tezlik: javob 100 millisekunddan kam vaqtda keladi, internetga borib qaytish esa yarim sekund oladi.",
  "Maxfiylik: ovoz va tasvir qurilmadan CHIQMAYDI, hech qayerga yuborilmaydi.",
  "Mustaqillik: internet yo'q joyda ham ishlaydi.",
  "Arzonlik: bulut xizmatiga to'lov yo'q, tarmoq trafigi sarflanmaydi.",
 ]),
),

"SI, mashinaviy o'rganish va chuqur o'rganish": D(
 ("Farqni misolda ko'rish", [
  "Vazifa: rasmda mushuk bormi degan savolga javob berish.",
  "Klassik AI yondashuvi: dasturchi qoidalar yozadi — 'agar uchburchak quloq bo'lsa va mo'ylov bo'lsa'. Bu yondashuv amalda ishlamagan, chunki qoidalar cheksiz ko'p.",
  "Mashinaviy o'rganish: dasturchi qoida yozmaydi, minglab rasm ko'rsatadi va 'bu mushuk, bu emas' deb aytadi. Model qonuniyatni O'ZI topadi.",
  "Chuqur o'rganish: model ko'p qatlamli bo'ladi. Birinchi qatlam chiziqlarni, ikkinchisi shakllarni, uchinchisi quloq va ko'zni taniydi.",
 ]),
 ("Qaysi holatda qaysi yondashuv", [
  "Qoida aniq va oz bo'lsa — oddiy dastur yozgan ma'qul. Chegaradan oshsa signal berish uchun AI kerak emas.",
  "Qoidani so'z bilan tushuntirib bo'lmasa — mashinaviy o'rganish kerak. 'Bu ovoz — mening ovozim' degan qoidani yozib bo'lmaydi.",
  "Ma'lumot juda ko'p va murakkab bo'lsa (tasvir, video) — chuqur o'rganish.",
  "Muhim: AI ni har joyga tiqishtirish kerak emas. Oddiy if sharti yetadigan joyda model ishlatish — resursni behuda sarflash.",
 ]),
),

"An'anaviy dastur va o'rganuvchi model farqi": D(
 ("Ikki yondashuvning tuzilishi", [
  "An'anaviy dastur: KIRISH + QOIDA -> NATIJA. Qoidani odam yozadi.",
  "Mashinaviy o'rganish: KIRISH + NATIJA -> QOIDA. Qoidani mashina topadi.",
  "Ya'ni ML da biz javobni ko'rsatamiz, mashina esa javobga olib boradigan yo'lni o'zi qidiradi.",
  "Topilgan 'qoida' — bu model. U aslida ko'p sonli koeffitsientlar to'plami.",
 ]),
 ("Har birining kuchli va zaif tomoni", [
  "An'anaviy dastur: natijasi oldindan ma'lum, tushuntirish oson, xatoni topish oson. Lekin murakkab vazifalarda qoida yozib bo'lmaydi.",
  "Model: murakkab vazifani uddalaydi. Lekin nima uchun shunday javob berganini tushuntirish qiyin va u xato ham qilishi mumkin.",
  "Modelga ishonch DOIM 100 % bo'lmaydi. Shuning uchun natija bilan birga ehtimollik ham qaytariladi.",
  "Amaliy qoida: model ishonchi past bo'lsa (masalan 0,7 dan kam), qaror qabul qilmaslik va 'noaniq' deb javob berish to'g'riroq.",
 ]),
),

"Nazorat ostida va nazoratsiz o'rganish": D(
 ("Nazorat ostida o'rganish (supervised)", [
  "Har bir misolga TO'G'RI JAVOB birga beriladi: bu rasm — mushuk, bu — it.",
  "Model o'z javobini to'g'ri javob bilan solishtiradi va farqni kamaytirish tomonga sozlanadi.",
  "Maktab loyihalarining deyarli hammasi shu turga kiradi: ovoz buyruqlarini tanish, imo-ishorani tanish, buyumni tanish.",
  "Kamchiligi: har bir misolni QO'LDA belgilash kerak. Bu eng ko'p vaqt oladigan bosqich.",
 ]),
 ("Nazoratsiz o'rganish (unsupervised)", [
  "To'g'ri javob berilmaydi. Model ma'lumotning o'zidagi tuzilmani topadi.",
  "Asosiy vazifa — guruhlarga ajratish (klasterlash): o'xshash misollarni bir joyga to'plash.",
  "Anomaliya aniqlash ham shu turga kiradi: model 'normal' holatni o'rganadi va undan keskin farq qilgan holatni belgilaydi.",
  "Amaliy misol: motorning normal tebranishini o'rgatib, nosozlik boshlanganini oldindan aniqlash.",
 ]),
),

"Neyron tarmoq g'oyasi: oddiy tushuntirish": D(
 ("Bitta neyron nima qiladi", [
  "Neyron bir necha son qabul qiladi, har birini o'z og'irligiga ko'paytiradi va yig'indini hisoblaydi.",
  "Yig'indiga siljish (bias) qo'shiladi, keyin natija aktivatsiya funksiyasidan o'tkaziladi.",
  "Aktivatsiya funksiyasi qaror qabul qiladi: yig'indi yetarli katta bo'lsa neyron 'yonadi', aks holda tinch qoladi.",
  "Bu miya neyronining juda soddalashtirilgan modeli: u ham bir necha signalni yig'ib, chegaradan oshsa impuls yuboradi.",
 ]),
 ("Qatlamlar va o'rganish", [
  "Bitta neyron oz ish qiladi. Kuch — ularni QATLAM qilib joylashtirib, qatlamlarni ketma-ket ulashda.",
  "Kirish qatlami ma'lumotni qabul qiladi, yashirin qatlamlar uni bosqichma-bosqich qayta ishlaydi, chiqish qatlami javob beradi.",
  "O'rganish — bu og'irliklarni sozlash jarayoni. Boshida ular tasodifiy, keyin har xatodan keyin biroz to'g'rilanadi.",
  "Bu to'g'rilash minglab marta takrorlanadi. Har bir to'liq o'tish epoch deb ataladi.",
  "Model 'biladigan' hamma narsa aynan shu og'irliklar ichida saqlanadi — boshqa hech qanday qoida yo'q.",
 ]),
),

"TinyML: mikrokontrollerda model": D(
 ("Cheklovlar va ular bilan ishlash", [
  "Xotira: model va u ishlatadigan buffer birga mikrokontroller RAM iga sig'ishi kerak.",
  "Tezlik: 240 MHz protsessor telefon protsessoridan o'nlab barobar sekin.",
  "Quvvat: batareyada ishlaydigan qurilmada har bir hisob quvvat sarflaydi.",
  "Shuning uchun TinyML da model kichik va vazifa aniq bo'lishi kerak: 'har qanday narsani tanish' emas, 'to'rtta buyruqni ajratish'.",
 ]),
 ("Ish oqimi", [
  "1) Ma'lumot yig'ish — qurilmaning O'ZIDA, chunki model shu sensordan kelgan ma'lumotda ishlaydi.",
  "2) Belgilash — har bir bo'lakka to'g'ri sinf nomini qo'yish.",
  "3) Belgi ajratish — xom ma'lumotdan model uchun muhim xususiyatlarni chiqarish.",
  "4) O'rgatish — brauzerda (Edge Impulse) yoki kompyuterda.",
  "5) Siqish (kvantlash) — modelni mikrokontrollerga sig'adigan holga keltirish.",
  "6) Yuklash va sinash — qurilmada haqiqiy sharoitda tekshirish.",
  "Bu sikl bir marta emas, bir necha marta takrorlanadi: sinovda topilgan kamchilik ma'lumot yig'ishga qaytaradi.",
 ]),
),

"Ma'lumot (dataset) nima va nega muhim": D(
 ("Dataset tuzilishi", [
  "Dataset — modelni o'rgatish uchun yig'ilgan misollar to'plami. Har bir misolda kirish ma'lumoti va to'g'ri javob bo'ladi.",
  "Ovoz loyihasida bir misol — bu bir sekundlik yozuv va uning sinfi ('yoq', 'o'chir', 'fon').",
  "Imo-ishora loyihasida bir misol — bu ikki sekundlik akselerometr yozuvi va harakat nomi.",
  "Har bir sinf uchun kamida 50-100 misol kerak. Kamroq bo'lsa model qonuniyatni topa olmaydi.",
 ]),
 ("Ma'lumot sifati modeldan muhimroq", [
  "Yomon ma'lumot bilan eng yaxshi model ham yomon natija beradi. Yaxshi ma'lumot bilan oddiy model ham yaxshi ishlaydi.",
  "Xilma-xillik shart: turli odamlar, turli tezlik, turli fon shovqini bilan yozib olish kerak.",
  "Faqat bir o'quvchining ovozi bilan o'rgatilgan model boshqalarni tanimaydi — bu darsda ko'p uchraydigan xato.",
  "Muvozanat shart: bir sinfda 200, boshqasida 20 misol bo'lsa, model ko'p uchragan sinfga og'ib ketadi.",
  "'Fon' yoki 'hech narsa' sinfi ham SHART — usiz model har qanday shovqinni buyruq deb qabul qiladi.",
 ]),
),

"Ma'lumot sifati va muvozanati": D(
 ("Muvozanat nima uchun muhim", [
  "Model o'z xatosini kamaytirishga intiladi. Agar bir sinf 90 % ni tashkil qilsa, model doim shu sinfni aytib ham 90 % aniqlikka erishadi.",
  "Bunday model foydasiz bo'lsa ham, aniqlik ko'rsatkichi yuqori chiqadi — bu aldanishning eng ko'p uchraydigan sababi.",
  "Shuning uchun har bir sinfda taxminan TENG miqdorda misol bo'lishi kerak.",
  "Muvozanatni tekshirish oson: Edge Impulse ma'lumot sahifasida har bir sinfning ulushi ko'rsatiladi.",
 ]),
 ("Sifatni oshirish yo'llari", [
  "Yozib olish sharoitini haqiqiy ish sharoitiga yaqinlashtirish: qurilma qayerda ishlasa, o'sha yerda yozib olish.",
  "Turli holatlarni qamrab olish: sekin va tez harakat, baland va past ovoz, yorug' va qorong'i.",
  "Xato yozuvlarni o'chirish: tasodifan boshqa tovush kirib qolgan yozuv modelni chalg'itadi.",
  "Ma'lumotni ko'paytirish (augmentation): mavjud yozuvga biroz shovqin qo'shib yoki tezligini o'zgartirib yangi misol hosil qilish.",
 ]),
),

"Ma'lumot to'plash strategiyasi": D(
 ("Rejalashtirish bosqichi", [
  "Avval sinflar ro'yxati yoziladi: qurilma nechta holatni ajratishi kerak.",
  "Har bir sinf uchun necha misol kerakligi belgilanadi (kamida 50, yaxshisi 100+).",
  "Kim yozib beradi — kamida 3-5 xil odam bo'lsin, aks holda model faqat bir kishini taniydi.",
  "Yozib olish parametrlari qat'iy belgilanadi: chastota (masalan 100 Hz), davomiylik (2 sekund), sensor oralig'i.",
  "ENG MUHIMI: bu parametrlar butun yig'ish davomida O'ZGARMASLIGI kerak. O'zgarsa model noto'g'ri o'rganadi.",
 ]),
 ("Yig'ish va tekshirish", [
  "Yozib olishdan oldin bir necha sinov yozuvi qilinadi va ular ko'z bilan tekshiriladi.",
  "Grafik tekis chiziq bo'lsa — sensor ulanmagan. To'yingan bo'lsa — oraliq noto'g'ri tanlangan.",
  "Har 20-30 yozuvdan keyin oraliq tekshiruv o'tkaziladi, aks holda 100 ta yaroqsiz yozuv qilib qo'yish mumkin.",
  "Yig'ilgan ma'lumot darhol 80/20 nisbatda bo'linadi: 80 % o'rgatish uchun, 20 % tekshirish uchun.",
 ]),
),

"Ma'lumotni belgilash (labeling)": D(
 ("Belgilash qoidalari", [
  "Har bir misolga aniq bitta sinf nomi qo'yiladi. Nom qisqa va bir xil yoziladi: 'yoq' va 'Yoq' ikki xil sinf sifatida qabul qilinadi.",
  "Chegaradagi holatlar uchun qoida oldindan kelishiladi: yarim aytilgan so'z qaysi sinfga kiradi.",
  "Bir necha kishi belgilasa, ular bir xil qoidaga amal qilishi kerak — aks holda ma'lumot ziddiyatli bo'ladi.",
  "Shubhali misolni belgilashdan ko'ra O'CHIRIB tashlagan ma'qul: noto'g'ri belgi modelni buzadi.",
 ]),
 ("Belgilash — eng ko'p vaqt oladigan bosqich", [
  "Amalda AI loyihasining vaqtining 60-80 % i ma'lumot yig'ish va belgilashga ketadi, model o'rgatish esa bir necha daqiqa oladi.",
  "Bu o'quvchilar uchun kutilmagan bo'ladi va aynan shuni bir marta boshdan kechirish kerak.",
  "Edge Impulse da belgilash brauzerda qilinadi: yozuv tanlanadi, sinf nomi yoziladi va saqlanadi.",
  "Tasvir loyihalarida belgilash yanada og'ir: obyektni ramka bilan belgilash kerak.",
 ]),
),

"Belgi (feature) va sinf (class) tushunchasi": D(
 ("Belgi nima", [
  "Belgi (feature) — ma'lumotdan ajratilgan va model uchun ma'noli bo'lgan son.",
  "Xom akselerometr ma'lumoti 2 sekundda 600 ta son beradi. Model bularning hammasi bilan ishlashi qiyin.",
  "Shuning uchun ulardan belgilar chiqariladi: o'rtacha, eng katta, eng kichik, tebranish kengligi, chastota tarkibi.",
  "Yaxshi belgi sinflarni ajratadi. Agar ikki sinfda belgi qiymati bir xil bo'lsa, u belgi foydasiz.",
 ]),
 ("Sinf nima", [
  "Sinf (class) — model ajratadigan toifalardan biri. 'yoq', 'o'chir', 'fon' — uchta sinf.",
  "Sinflar bir-birini istisno qilishi kerak: bir misol faqat bitta sinfga tegishli.",
  "Sinflar soni ortgan sari model murakkablashadi va ko'proq ma'lumot talab qiladi.",
  "Maktab loyihasi uchun 2-4 sinf optimal. 10 sinf bilan ishlash uchun ma'lumot yig'ishga bir necha dars ketadi.",
 ]),
),

"Belgi ajratish (feature extraction)": D(
 ("Nima uchun xom ma'lumot yetarli emas", [
  "Xom ma'lumot juda ko'p sondan iborat va ularning ko'pi keraksiz.",
  "Belgi ajratish ma'lumotni siqadi: 600 ta sondan 30 ta ma'noli belgi qoladi.",
  "Natijada model kichrayadi, tez ishlaydi va kam ma'lumot bilan ham yaxshi o'rganadi.",
  "Bu bosqich TinyML da ayniqsa muhim, chunki mikrokontrollerda resurs cheklangan.",
 ]),
 ("Amaldagi belgi turlari", [
  "Vaqt sohasidagi belgilar: o'rtacha, standart og'ish, eng katta va eng kichik qiymat, RMS.",
  "Chastota sohasidagi belgilar: Fure o'zgartirishi orqali signal qanday chastotalardan iboratligini topish.",
  "Ovoz uchun MFCC ishlatiladi — bu inson qulog'i tovushni qanday eshitishiga moslashtirilgan belgi to'plami.",
  "Tasvir uchun belgi ajratishni odatda neyron tarmoqning o'zi bajaradi (konvolyutsion qatlamlar).",
  "Edge Impulse da belgi bloki tanlanadi va u belgilarning sinflarni qanchalik yaxshi ajratayotganini grafikda ko'rsatadi.",
 ]),
),

"O'rgatish va tekshirish to'plamlari": D(
 ("Nima uchun ma'lumot bo'linadi", [
  "Model o'rgatilgan ma'lumotda doim yaxshi natija beradi — u ularni ko'rgan.",
  "Haqiqiy savol: model KO'RMAGAN ma'lumotda qanday ishlaydi.",
  "Shuning uchun ma'lumot bo'linadi: 80 % o'rgatish uchun, 20 % tekshirish uchun.",
  "Tekshirish to'plami o'rgatishda MUTLAQO ishlatilmaydi — aks holda tekshiruv ma'nosini yo'qotadi.",
 ]),
 ("Natijalarni o'qish", [
  "O'rgatish aniqligi 98 %, tekshirish aniqligi 95 % — bu yaxshi model.",
  "O'rgatish 99 %, tekshirish 60 % — bu ortiqcha moslashuv (overfitting): model yodlab olgan.",
  "Ikkalasi ham 60 % — model yetarli o'rganmagan: ma'lumot kam yoki belgilar yomon tanlangan.",
  "Eng ishonchli tekshiruv esa — qurilmada haqiqiy sharoitda sinash. Brauzerdagi raqam bilan haqiqiy natija farq qilishi mumkin.",
 ]),
),

"Model o'rgatish jarayoni: qadamlar": D(
 ("O'rgatish ichida nima sodir bo'ladi", [
  "1) Boshida model og'irliklari TASODIFIY qiymatlarga to'ldiriladi — model hech narsa bilmaydi.",
  "2) Bir misol beriladi, model javob qaytaradi. Javob deyarli har doim noto'g'ri chiqadi.",
  "3) Xato hisoblanadi: model javobi va to'g'ri javob orasidagi farq.",
  "4) Og'irliklar shu xatoni kamaytirish tomonga BIROZ o'zgartiriladi.",
  "5) Bu hamma misol uchun takrorlanadi. Butun to'plamdan bir marta o'tish — bitta epoch.",
  "6) Epochlar takrorlanadi va xato asta-sekin kamayib boradi.",
 ]),
 ("Qachon to'xtatish kerak", [
  "Xato kamayishdan to'xtasa, davom etish foydasiz.",
  "Tekshirish aniqligi tusha boshlasa — bu overfitting boshlangani va o'rgatishni to'xtatish kerakligini bildiradi.",
  "Maktab loyihalarida odatda 30-100 epoch yetarli.",
  "Edge Impulse o'rgatish jarayonida grafik ko'rsatadi: ikki chiziq (o'rgatish va tekshirish) bir-biridan uzoqlasha boshlasa — to'xtatish vaqti keldi.",
 ]),
),

"O'rgatish parametrlari (epoch, learning rate)": D(
 ("Epoch — necha marta o'tish", [
  "Epoch — butun o'rgatish to'plamidan bir marta to'liq o'tish.",
  "Kam epoch: model yetarli o'rganmaydi (underfitting).",
  "Ko'p epoch: model ma'lumotni yodlab oladi (overfitting).",
  "Maktab loyihalari uchun boshlang'ich qiymat: 50 epoch. Keyin natijaga qarab sozlanadi.",
 ]),
 ("Learning rate — qadam kattaligi", [
  "Learning rate — har bir xatodan keyin og'irliklar qanchalik o'zgarishini belgilaydi.",
  "Juda katta bo'lsa: model to'g'ri javobdan sakrab o'tib ketadi va hech qachon barqarorlashmaydi.",
  "Juda kichik bo'lsa: o'rganish juda sekin boradi va epochlar yetmaydi.",
  "Standart qiymat 0,001 — ko'p holatda u yaxshi ishlaydi va uni o'zgartirish shart emas.",
  "Tog'dan pastga tushish o'xshatishi: qadam juda katta bo'lsa vodiydan sakrab o'tasiz, juda kichik bo'lsa hech qachon yetib bormaysiz.",
 ]),
),

"Ortiqcha moslashuv (overfitting) muammosi": D(
 ("Overfitting nima", [
  "Model o'rgatish misollarini YODLAB oladi, lekin umumiy qonuniyatni topa olmaydi.",
  "Belgisi: o'rgatish aniqligi juda yuqori (99 %), tekshirish aniqligi esa ancha past (60-70 %).",
  "O'xshatish: masalalar javobini yodlab olgan o'quvchi. Xuddi shu masalalarni yechadi, biroz o'zgartirilgan masalani esa yecha olmaydi.",
  "Qurilmada bu shunday ko'rinadi: sinfda ishlaydi, boshqa xonada yoki boshqa odam bilan ishlamaydi.",
 ]),
 ("Overfitting ni oldini olish", [
  "Ko'proq va XILMA-XIL ma'lumot yig'ish — bu eng samarali usul.",
  "Modelni soddalashtirish: qatlam va neyron sonini kamaytirish.",
  "Erta to'xtatish: tekshirish aniqligi tusha boshlaganda o'rgatishni to'xtatish.",
  "Dropout: o'rgatish paytida neyronlarning bir qismini tasodifiy o'chirib qo'yish. Bu modelni bitta yo'lga suyanmaslikka majbur qiladi.",
  "Ma'lumotni ko'paytirish (augmentation): mavjud misollarga kichik o'zgarishlar qo'shib yangi misol yasash.",
 ]),
),

"Overfitting va uni oldini olish": D(
 ("Ikki qarama-qarshi muammo", [
  "Underfitting — model juda sodda, hatto o'rgatish ma'lumotida ham yomon natija beradi.",
  "Overfitting — model juda murakkab, o'rgatish ma'lumotini yodlab olgan.",
  "To'g'ri holat ikkisining o'rtasida: model qonuniyatni topgan, lekin shovqinni yodlamagan.",
  "Buni faqat tekshirish to'plamidagi natija bo'yicha aniqlash mumkin.",
 ]),
 ("Amaliy tartib", [
  "1) Modelni o'rgating va ikki aniqlikni yozib oling.",
  "2) Farq 10 % dan katta bo'lsa — overfitting bor.",
  "3) Avval ma'lumotni ko'paytirishga urinib ko'ring — bu eng ishonchli yechim.",
  "4) Iloji bo'lmasa, model o'lchamini kamaytiring yoki dropout qo'shing.",
  "5) Har o'zgarishdan keyin qayta o'rgatib, natijani jadvalga yozing.",
  "Bu jadval loyiha hujjatining eng qimmatli qismi bo'ladi.",
 ]),
),

"Aniqlik, chalkashlik matritsasi, F1": D(
 ("Aniqlik yolg'iz yetarli emas", [
  "Aniqlik (accuracy) — to'g'ri javoblar ulushi. Oddiy, lekin aldashi mumkin.",
  "Misol: 95 % holatda 'hech narsa yo'q' bo'lsa, doim 'yo'q' deydigan model 95 % aniqlik beradi — foydasiz bo'lsa ham.",
  "Shuning uchun qo'shimcha ko'rsatkichlar kerak.",
  "Precision (aniqlik) — model 'ha' degan holatlarning nechtasi haqiqatan 'ha' bo'lgan.",
  "Recall (to'liqlik) — haqiqiy 'ha' holatlarning nechtasini model topa olgan.",
  "F1 — precision va recall ning muvozanatli birlashmasi. Bitta son bilan umumiy sifatni ko'rsatadi.",
 ]),
 ("Chalkashlik matritsasini o'qish", [
  "Bu jadvalning qatorlari — haqiqiy sinf, ustunlari — model javobi.",
  "Diagonaldagi sonlar — to'g'ri javoblar. Ular qancha katta bo'lsa shuncha yaxshi.",
  "Diagonaldan tashqaridagi sonlar — xatolar va ular qaysi sinf qaysi bilan ADASHTIRILGANINI ko'rsatadi.",
  "Bu eng foydali ma'lumot: agar 'yoq' va 'o'chir' bir-biri bilan adashsa, demak bu ikki so'z uchun ko'proq ma'lumot kerak.",
  "Ya'ni matritsa nafaqat baho qo'yadi, balki nima qilish kerakligini ham aytadi.",
 ]),
),

"Chalkashlik matritsasi (confusion matrix)": D(
 ("Jadvalni tuzish", [
  "Uch sinfli model uchun matritsa 3x3 bo'ladi.",
  "Har bir katakda: haqiqiy sinf X bo'lgan va model Y deb aytgan misollar soni.",
  "Yaxshi modelda deyarli hamma son diagonalda to'planadi.",
  "Edge Impulse o'rgatish tugagach bu jadvalni avtomatik chizadi.",
 ]),
 ("Xulosa chiqarish", [
  "Bir sinf doim boshqasiga adashtirilsa — bu ikki sinf bir-biriga juda o'xshash yoki ma'lumot yetarli emas.",
  "Bitta sinfda natija yomon bo'lsa — o'sha sinf uchun ko'proq va xilma-xil misol yig'ish kerak.",
  "'Fon' sinfi boshqa sinflarga aralashsa — fon yozuvlari yetarli xilma-xil emas.",
  "Har bir tuzatishdan keyin matritsa qayta chizilib, avvalgisi bilan solishtiriladi. Yaxshilanish shunda ko'rinadi.",
 ]),
),

"Model turini tanlash": D(
 ("Vazifaga qarab tanlash", [
  "Tasnif (classification) — javob toifalardan biri: 'yoq', 'o'chir', 'fon'. Maktab loyihalarining ko'pi shunday.",
  "Regressiya — javob son: harorat bashorati, masofa qiymati.",
  "Anomaliya aniqlash — 'normal' dan farq qilgan holatni topish. Nosozlikni oldindan aniqlashda ishlatiladi.",
  "Obyekt aniqlash — tasvirdagi buyumni topib, uning JOYINI ham ko'rsatish.",
 ]),
 ("Model o'lchamini tanlash", [
  "Kichik model: tez ishlaydi, kam xotira oladi, lekin murakkab vazifani uddalamaydi.",
  "Katta model: aniqroq, lekin mikrokontrollerga sig'masligi mumkin.",
  "Edge Impulse har bir variant uchun taxminiy xotira va kechikishni oldindan ko'rsatadi — tanlashdan oldin shunga qarash kerak.",
  "Qoida: eng kichik modeldan boshlang. Aniqlik yetmasa, keyin kattalashtiring.",
 ]),
),

"Modelni siqish (quantization) nima uchun kerak": D(
 ("Kvantlash nima qiladi", [
  "Model ichidagi sonlar odatda 32 bitli kasrli (float32) formatda saqlanadi.",
  "Kvantlash ularni 8 bitli butun songa (int8) aylantiradi.",
  "Natija: model 4 barobar kichrayadi va hisoblash sezilarli tezlashadi.",
  "Aniqlik esa odatda atigi 1-2 % ga tushadi — bu almashish deyarli har doim foydali.",
 ]),
 ("Nima uchun bu ishlaydi", [
  "Neyron tarmoq og'irliklarida juda yuqori aniqlik shart emas: 0,7134 va 0,71 amalda bir xil natija beradi.",
  "Mikrokontrollerda butun sonlar bilan hisoblash kasrli sonlarga qaraganda ancha tez bajariladi.",
  "Ba'zi protsessorlarda umuman kasrli sonlar bloki yo'q — ularda float bilan ishlash o'nlab barobar sekin.",
  "Shuning uchun TinyML da kvantlash tanlov emas, deyarli majburiy bosqich.",
 ]),
),

"Modelni siqish va kvantlash": D(
 ("Amaliy bosqichlar", [
  "Edge Impulse Deployment sahifasida ikki variant beriladi: Quantized (int8) va Unoptimized (float32).",
  "Har biri uchun xotira sarfi va kechikish ko'rsatiladi — ularni yozib olib solishtirish kerak.",
  "Quantized variant tanlanadi va ZIP kutubxona yuklab olinadi.",
  "IDE ga qo'shiladi: Sketch > Include Library > Add .ZIP Library.",
 ]),
 ("Natijani o'lchash", [
  "Ikkala variantni ham qurilmaga yuklab, bir xil sinovdan o'tkazish kerak.",
  "O'lchanadigan ko'rsatkichlar: model hajmi, RAM sarfi, bitta bashoratga ketgan vaqt (latency), aniqlik.",
  "Jadval tuziladi va kvantlash nimani yutgani hamda nimani yo'qotgani aniq ko'rinadi.",
  "Bu jadval loyiha himoyasida eng kuchli dalil bo'ladi: raqam bilan asoslangan tanlov.",
 ]),
),

"Xotira va tezlik cheklovlari": D(
 ("Cheklovlarni o'lchash", [
  "Flash xotira — dastur va model saqlanadigan joy. Model hajmi shunga sig'ishi kerak.",
  "RAM — ish paytida ishlatiladigan xotira. Model buferlari va sensor ma'lumoti shu yerda turadi.",
  "Kechikish (latency) — bitta bashorat uchun ketadigan vaqt. U natija bilan birga chiqariladi.",
  "ESP.getFreeHeap() bilan bo'sh RAM ni dastur ichida o'lchash mumkin.",
 ]),
 ("Cheklovga sig'dirish yo'llari", [
  "Model o'lchamini kamaytirish (kamroq qatlam, kamroq neyron).",
  "Kvantlash qo'llash — 4 barobar yutuq.",
  "Kirish ma'lumotini kichraytirish: tasvirni 160x160 emas, 96x96 qilish.",
  "Belgi ajratishni soddalashtirish: kamroq belgi — kichikroq model.",
  "Sinflar sonini kamaytirish: 10 sinf o'rniga eng kerakli 3 tasini qoldirish.",
 ]),
),

"Modelni qurilmaga yuklash": D(
 ("Yuklash tartibi", [
  "1) Edge Impulse da Deployment > Arduino library tanlanadi.",
  "2) Quantized (int8) varianti tanlanib, ZIP fayl yuklab olinadi.",
  "3) Arduino IDE: Sketch > Include Library > Add .ZIP Library.",
  "4) File > Examples ichida loyiha nomi bilan misollar paydo bo'ladi — ishni shulardan boshlash kerak.",
  "5) Board sozlamalari tekshiriladi: XIAO_ESP32S3 va PSRAM yoqilgan bo'lishi shart.",
 ]),
 ("Ko'p uchraydigan xatolar", [
  "PSRAM o'chiq qolsa kamera ishlamaydi va dastur ishga tushmaydi.",
  "Eski model kutubxonasi o'chirilmasa, IDE ikkisini aralashtiradi — yangisini qo'shishdan oldin eskisini o'chirish kerak.",
  "Xotira yetmasa kompilyatsiya paytida 'region overflowed' xatosi chiqadi. Yechim: kichikroq model.",
  "Serial tezligi 115200 qilinmasa monitorda ma'nosiz belgilar chiqadi.",
 ]),
),

"Modelni qurilmaga joylash": D(
 ("Kodda modelni ishlatish", [
  "Kutubxona ulanadi: #include <loyiha_nomi_inferencing.h>",
  "Sensor ma'lumoti signal tuzilmasiga to'ldiriladi — u modelning kirishi.",
  "run_classifier() chaqiriladi va natija ei_impulse_result_t tuzilmasida qaytadi.",
  "Natijada har bir sinf uchun ehtimollik bo'ladi: yig'indisi 1 ga teng.",
 ]),
 ("Qaror qabul qilish", [
  "Eng katta ehtimollikli sinf tanlanadi, lekin u CHEGARADAN yuqori bo'lishi kerak.",
  "Chegara odatda 0,7-0,8 qilib olinadi. Undan past bo'lsa 'noaniq' deb javob berilgani ma'qul.",
  "Chegarasiz tizim har qanday shovqinga javob beradi va foydalanuvchini bezdiradi.",
  "Qo'shimcha filtr: bir necha ketma-ket bashorat bir xil chiqsagina qaror qabul qilish.",
 ]),
),

"Modelni qurilmaga yuklash va sinash": D(
 ("Sinov rejasi", [
  "Sinov brauzerdagi natijaga emas, HAQIQIY sharoitdagi natijaga qaraladi.",
  "Har bir sinf uchun kamida 20 marta sinov o'tkaziladi va to'g'ri javoblar sanaladi.",
  "Sinov turli sharoitda takrorlanadi: turli odam, turli masofa, turli fon shovqini.",
  "Natijalar jadvalga yoziladi — bu haqiqiy chalkashlik matritsasi bo'ladi.",
 ]),
 ("Natijani tahlil qilish", [
  "Brauzerdagi aniqlik 95 %, qurilmada esa 70 % chiqishi normal holat.",
  "Sabab odatda bitta: yig'ilgan ma'lumot haqiqiy sharoitga o'xshamagan.",
  "Yechim: sinovda xato bo'lgan holatlarni YOZIB OLIB, ularni datasetga qo'shish va qayta o'rgatish.",
  "Bu sikl 2-3 marta takrorlansa natija sezilarli yaxshilanadi. Aynan shu — haqiqiy AI ishi.",
 ]),
),

"Modelni o'rgatish va aniqlikni ko'rish": D(
 ("O'rgatishni ishga tushirish", [
  "Edge Impulse: Create impulse -> belgi bloki -> o'rgatish bloki tanlanadi.",
  "Parametrlar qo'yiladi: epoch soni, learning rate, model o'lchami.",
  "Start training bosiladi va jarayon brauzerda kuzatiladi.",
  "O'rgatish odatda 1-5 daqiqa oladi — bu o'quvchilar kutmagan darajada tez bo'ladi.",
 ]),
 ("Natijani o'qish", [
  "Accuracy — umumiy aniqlik foizi.",
  "Loss — xato o'lchovi, u kichik bo'lishi kerak.",
  "Chalkashlik matritsasi — qaysi sinf qaysi bilan adashgani.",
  "On-device performance — modelning qurilmadagi taxminiy xotira sarfi va kechikishi.",
  "Bu to'rt ko'rsatkich birga o'qiladi: faqat aniqlikka qarash yetarli emas.",
 ]),
),

"Modelni o'rgatish va sozlash": D(
 ("Sozlash siklini boshqarish", [
  "Har safar FAQAT BITTA parametr o'zgartiriladi va natija yoziladi.",
  "Bir vaqtda ikkitasini o'zgartirsangiz, qaysi biri yordam berganini bilib bo'lmaydi.",
  "Jadval yuritiladi: nima o'zgartirildi, o'rgatish aniqligi, tekshirish aniqligi, model hajmi.",
  "3-5 urinishdan keyin eng yaxshi variant aniq ko'rinadi.",
 ]),
 ("Nimadan boshlash kerak", [
  "1-navbat: ma'lumotni ko'paytirish va muvozanatlash — bu eng katta ta'sir beradi.",
  "2-navbat: belgi blokini almashtirish yoki uning parametrlarini sozlash.",
  "3-navbat: epoch sonini oshirish yoki kamaytirish.",
  "4-navbat: model o'lchamini o'zgartirish.",
  "Learning rate ni oxirida va faqat kerak bo'lsa tegish kerak — standart qiymat odatda yaxshi ishlaydi.",
 ]),
),

"Modelni yaxshilash sikli": D(
 ("Sikl bosqichlari", [
  "Yig'ish -> belgilash -> o'rgatish -> sinash -> XATONI TAHLIL QILISH -> yana yig'ish.",
  "Sikl to'xtaydigan joy — natija maqsadga yetganda, mukammal bo'lganda emas.",
  "Har bir aylanishda maqsad aniq bo'lishi kerak: 'aniqlikni 70 dan 85 % ga ko'tarish'.",
 ]),
 ("Xatoni tahlil qilish — eng muhim bosqich", [
  "Model qaysi holatlarda xato qilayotganini YOZIB BORISH kerak.",
  "Xatolar odatda guruhlanadi: masalan hamma xato tez aytilgan buyruqlarda bo'ladi.",
  "Guruh topilgach, aynan o'sha holatdan ko'proq ma'lumot yig'iladi.",
  "Tasodifiy ko'proq ma'lumot yig'ish samarasiz — maqsadli yig'ish esa tez natija beradi.",
 ]),
),

"Modelni yaxshilash: ko'proq ma'lumot": D(
 ("Ma'lumot miqdorining ta'siri", [
  "Ko'p hollarda modelni yaxshilashning eng samarali yo'li — ko'proq ma'lumot.",
  "Sinf uchun 20 misoldan 100 misolga o'tish aniqlikni 20-30 % ga oshirishi mumkin.",
  "100 dan 200 ga o'tish esa ancha kam yaxshilanish beradi — bu tabiiy holat.",
  "Ya'ni foyda boshida katta, keyin kamayadi. Buni bilib, qachon to'xtashni belgilash kerak.",
 ]),
 ("Sifat miqdordan muhim", [
  "1000 ta bir xil sharoitda yozilgan misol 100 ta xilma-xil misoldan yomonroq natija beradi.",
  "Yangi ma'lumot yig'ishda qidiriladigan narsa — MODEL KO'RMAGAN holatlar.",
  "Sinovda xato bo'lgan holatlarni yozib olib datasetga qo'shish eng tez yaxshilanishni beradi.",
  "Har qo'shimchadan keyin qayta o'rgatib, natijani oldingisi bilan solishtirish shart.",
 ]),
),

"Edge Impulse platformasi bilan tanishuv": D(
 ("Platformaning bo'limlari", [
  "Data acquisition — ma'lumot yig'ish va belgilash.",
  "Impulse design — ish oqimini qurish: kirish bloki, belgi bloki, o'rgatish bloki.",
  "Feature explorer — belgilarning sinflarni qanchalik yaxshi ajratayotganini grafikda ko'rish.",
  "Model testing — tekshirish to'plamida modelni sinash.",
  "Deployment — modelni kutubxona sifatida yuklab olish.",
 ]),
 ("Qurilmani ulash", [
  "Edge Impulse CLI o'rnatiladi yoki brauzer orqali ulanish ishlatiladi.",
  "Qurilma ulangach, u ma'lumot yig'ish sahifasida ko'rinadi.",
  "Yozib olish parametrlari (chastota, davomiylik) shu yerda qo'yiladi.",
  "Yozib olingan har bir namuna darhol grafikda ko'rinadi — buni har safar ko'z bilan tekshirish kerak.",
 ]),
),

"Edge Impulse: to'liq ish oqimi": D(
 ("Boshdan oxirigacha bosqichlar", [
  "1) Loyiha yaratish va qurilmani ulash.",
  "2) Har bir sinf uchun ma'lumot yig'ish (kamida 50-100 misol), 'fon' sinfini unutmaslik.",
  "3) Ma'lumotni 80/20 nisbatda bo'lish.",
  "4) Impulse qurish: kirish bloki -> belgi bloki -> o'rgatish bloki.",
  "5) Belgilarni hisoblash va Feature explorer da sinflar ajralayotganini tekshirish.",
  "6) Modelni o'rgatish va natijani tahlil qilish.",
  "7) Model testing bilan tekshirish to'plamida sinash.",
  "8) Deployment: Quantized (int8) Arduino kutubxonasini yuklab olish.",
  "9) IDE ga qo'shib, qurilmada haqiqiy sharoitda sinash.",
 ]),
 ("Har bosqichda tekshirish nuqtasi", [
  "Ma'lumotdan keyin: sinflar muvozanatlimi, grafiklar to'g'rimi.",
  "Belgilardan keyin: Feature explorer da sinflar alohida to'plamlar hosil qilayaptimi.",
  "O'rgatishdan keyin: ikki aniqlik orasidagi farq 10 % dan kammi.",
  "Yuklashdan keyin: qurilmada haqiqiy aniqlik qancha.",
  "Bosqich o'tmasa, keyingisiga o'tish ma'nosiz — muammoni shu yerda hal qilish kerak.",
 ]),
),

"Obyektni aniqlash (object detection) haqida": D(
 ("Tasnif va obyekt aniqlash farqi", [
  "Tasnif: 'bu rasmda mushuk bor' deb aytadi, lekin qayerdaligini bilmaydi.",
  "Obyekt aniqlash: buyumni topadi VA uning joyini ramka bilan ko'rsatadi.",
  "Bir rasmda bir necha obyektni ham topa oladi va ularni sanay oladi.",
  "Shuning uchun u sanash, saralash va kuzatish vazifalari uchun kerak.",
 ]),
 ("Cheklovlar", [
  "Obyekt aniqlash modeli tasnif modelidan ancha katta va sekin.",
  "Ma'lumot belgilash ham og'irroq: har bir obyektni qo'lda ramkaga olish kerak.",
  "Mikrokontrollerda odatda FOMO kabi soddalashtirilgan variant ishlatiladi: u obyektning markazini topadi, aniq ramkani emas.",
  "Maktab loyihasi uchun bu yetarli: buyum bor-yo'qligini va taxminiy joyini bilish ko'p vazifalarga kifoya qiladi.",
 ]),
),

"AI axloqi: ma'lumot va maxfiylik": D(
 ("Ma'lumot yig'ishdagi javobgarlik", [
  "Odamning ovozi, tasviri yoki harakati — bu shaxsiy ma'lumot.",
  "Yozib olishdan oldin ROZILIK so'ralishi kerak. Bu qoida maktab loyihasida ham amal qiladi.",
  "Ma'lumot faqat aytilgan maqsad uchun ishlatiladi va boshqa maqsadga o'tkazilmaydi.",
  "Loyiha tugagach, kerak bo'lmagan ma'lumot o'chiriladi.",
 ]),
 ("TinyML ning maxfiylik afzalligi", [
  "Model qurilmada ishlaganda ma'lumot hech qayerga yuborilmaydi.",
  "Kamera tasvirni ko'radi, qaror qabul qiladi va tasvirni o'chiradi — u saqlanmaydi ham, uzatilmaydi ham.",
  "Bu bulutga yuboradigan tizimlardan jiddiy afzallik.",
  "Loyihani taqdim qilishda buni alohida aytish kerak: bu texnik emas, AXLOQIY afzallik.",
 ]),
),

"AI axloqi: xolislik, maxfiylik, mas'uliyat": D(
 ("Xolislik (bias) muammosi", [
  "Model faqat ko'rgan ma'lumotidan o'rganadi. Ma'lumot bir tomonlama bo'lsa, model ham bir tomonlama bo'ladi.",
  "Misol: faqat o'g'il bolalar ovozi bilan o'rgatilgan model qiz bolalarni yomon taniydi.",
  "Bu model 'yomon' bo'lgani uchun emas — unga shunday ma'lumot berilgani uchun.",
  "Yechim texnik emas, tashkiliy: ma'lumot yig'ishda xilma-xillikni ataylab ta'minlash.",
 ]),
 ("Mas'uliyat", [
  "Model xato qilsa, javobgarlik modelda emas — uni yaratgan va ishlatgan odamda.",
  "Shuning uchun muhim qarorlarda (sog'liq, xavfsizlik) model yolg'iz qaror qabul qilmasligi kerak.",
  "Har bir AI qurilmada 'nima bo'lsa nima qilamiz' rejasi bo'lishi kerak: model ishlamay qolsa tizim xavfsiz holatga o'tsin.",
  "Loyiha hujjatida modelning CHEKLOVLARINI yozish — bu kuchsizlik emas, professional yondashuvning belgisi.",
 ]),
),

}
