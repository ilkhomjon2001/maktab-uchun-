# -*- coding: utf-8 -*-
"""
NAZARIYANI CHUQURLASHTIRISH — 5-qism: zanjir turlari, montaj, sxema tili,
diod, kondensator, tranzistor, motor va sensor asoslari.

Tuzilishi kb_chuqur.py bilan bir xil.
"""


def D(*bloklar):
    return [(sarlavha, list(bandlar)) for sarlavha, bandlar in bloklar]


CHUQUR5 = {

# ============================================================ ZANJIR TURLARI
"Ketma-ket ulanish qonuniyatlari": D(
 ("Uchta qonuniyat", [
  "TOK: hamma element orqali bir xil oqadi. I = I1 = I2 = I3.",
  "KUCHLANISH: elementlar orasida bo'linadi. U = U1 + U2 + U3 (Kirxgofning ikkinchi qonuni).",
  "QARSHILIK: oddiy qo'shiladi. R = R1 + R2 + R3.",
  "Sabab oddiy: tok uchun yagona yo'l bor, shuning uchun u hamma joyda bir xil. Har bir element esa o'z ulushidagi energiyani oladi.",
 ]),
 ("Kuchlanish qanday taqsimlanadi", [
  "Kuchlanish qarshilikka TO'G'RI proporsional taqsimlanadi: katta rezistorga ko'proq kuchlanish tushadi.",
  "Misol: 9 V, rezistorlar 100 va 200 Om. Umumiy R = 300 Om, I = 0,03 A.",
  "Birinchi rezistorda: U = 0,03 x 100 = 3 V. Ikkinchisida: U = 0,03 x 200 = 6 V. Yig'indi 9 V.",
  "Ya'ni qarshilik ikki barobar katta bo'lsa, unga tushadigan kuchlanish ham ikki barobar katta.",
 ]),
 ("Amaliy oqibatlari", [
  "Bitta element uzilsa butun zanjir o'chadi — bu ham kamchilik, ham foyda (xavfsizlik zanjirlarida ataylab shunday qilinadi).",
  "Ikki LEDni ketma-ket ulash mumkin, lekin manba kuchlanishi ularning tushishlari yig'indisidan katta bo'lishi kerak: 2 + 2 = 4 V, demak 5 V yetadi, 3,3 V yetmaydi.",
  "Batareyalarni ketma-ket ulash kuchlanishni oshiradi: to'rtta AA = 6 V. Sig'im esa o'zgarmaydi.",
  "Eski yangi yil gulchambarlari ketma-ket ulangan — shuning uchun bitta lampa kuysa hammasi o'chgan.",
 ]),
),

"Ketma-ket zanjirda tok hamma joyda bir xil": D(
 ("Nima uchun tok bir xil", [
  "Ketma-ket zanjirda tok uchun BITTA yo'l bor — u boshqa tomonga bura olmaydi.",
  "Zaryad hech qayerda to'planib qolmaydi va yo'qolmaydi: kesimga kirgan zaryad shuncha miqdorda chiqadi.",
  "Bu zaryadning saqlanish qonuni — fizikaning eng asosiy qonunlaridan biri.",
  "Ko'p uchraydigan noto'g'ri tasavvur: \"birinchi LED tokning bir qismini sarflaydi va ikkinchisiga kamroq yetadi\". Aslida TOK sarflanmaydi, ENERGIYA sarflanadi.",
 ]),
 ("Tajribada isbotlash", [
  "Zanjirni yig'ing: batareya, rezistor, LED, ikkinchi rezistor.",
  "Tokni zanjirning uch xil nuqtasida o'lchang: batareyadan keyin, LEDdan keyin, batareyaga qaytishdan oldin.",
  "Uch o'lchov ham bir xil chiqadi (o'lchov xatosi doirasida).",
  "Bu tajriba nazariyani hech qanday tushuntirishdan ko'ra ishonchliroq isbotlaydi.",
 ]),
),

"Ketma-ket zanjirda kuchlanish taqsimoti": D(
 ("Taqsimot qoidasi", [
  "Har bir elementga tushadigan kuchlanish: Ui = I x Ri.",
  "Yoki to'g'ridan-to'g'ri: Ui = Umanba x Ri / Rumumiy.",
  "Misol: 12 V, rezistorlar 1 kOm va 3 kOm. Birinchisida 12 x 1/4 = 3 V, ikkinchisida 12 x 3/4 = 9 V.",
  "Yig'indi doim manba kuchlanishiga teng bo'ladi — bu tekshirish uchun eng oson usul.",
 ]),
 ("LED ketma-ket zanjirda", [
  "LED oddiy rezistor emas: undagi tushish deyarli o'zgarmas (qizil ~2 V, ko'k ~3 V).",
  "Shuning uchun 5 V manbada qizil LED va rezistor bo'lsa: LEDda 2 V, rezistorda qolgan 3 V.",
  "Rezistorni 220 dan 470 Om ga o'zgartirsangiz — LEDdagi kuchlanish deyarli o'zgarmaydi, faqat TOK kamayadi va LED xiralashadi.",
  "Bu tajriba LEDning Om qonuniga bo'ysunmasligini eng aniq ko'rsatadi.",
 ]),
),

"Ketma-ket zanjirni o'lchab tekshirish": D(
 ("O'lchov rejasi", [
  "1) Manba kuchlanishini o'lchang.",
  "2) Har bir element ustidagi kuchlanish tushishini alohida o'lchang.",
  "3) Tushishlar yig'indisini hisoblab, manba kuchlanishi bilan solishtiring.",
  "4) Zanjirni uzib, tokni ikki xil nuqtada o'lchang.",
  "5) Om qonuni bo'yicha hisoblangan qiymatlar bilan solishtiring.",
 ]),
 ("Natijalarni o'qish", [
  "Tushishlar yig'indisi manbadan KAM chiqsa — o'lchanmagan element yoki yomon kontakt bor (kontaktda ham kuchlanish tushadi).",
  "Bitta elementda manba kuchlanishining hammasi tushsa — o'sha element uzilgan.",
  "Bitta elementda nol tushsa — u qisqa tutashgan yoki oddiy sim.",
  "Ikki nuqtadagi tok farq qilsa — o'lchov xatosi yoki zanjirda parallel shox bor.",
 ]),
),

"Parallel zanjirda kuchlanish bir xil": D(
 ("Nima uchun kuchlanish bir xil", [
  "Parallel ulangan elementlarning IKKI UCHI ham bir xil nuqtalarga ulangan.",
  "Kuchlanish esa ikki nuqta orasidagi farq — nuqtalar bir xil bo'lsa farq ham bir xil.",
  "Shuning uchun U = U1 = U2 = U3, elementlarning qarshiligi qanday bo'lishidan qat'i nazar.",
  "Tok esa aksincha bo'linadi: I = I1 + I2 + I3 (Kirxgofning birinchi qonuni).",
 ]),
 ("Umumiy qarshilik", [
  "Formula: 1/R = 1/R1 + 1/R2 + 1/R3.",
  "Ikki rezistor uchun qulayroq shakl: R = R1 x R2 / (R1 + R2).",
  "Ikki bir xil rezistor parallel — natija yarmi. Uchta bir xil — uchdan biri.",
  "Umumiy qarshilik DOIM eng kichik rezistordan ham kichik chiqadi: tokga qo'shimcha yo'l ochilgan.",
 ]),
 ("Nima uchun rozetkalar parallel ulanadi", [
  "Har bir jihozga to'liq 220 V kerak — parallel ulanishda hammasi bir xil kuchlanish oladi.",
  "Bir jihozni o'chirsangiz qolganlari ishlayveradi.",
  "Kamchiligi: har bir yangi jihoz umumiy tokni oshiradi. Ko'p jihoz ulansa sim qiziydi.",
  "Shuning uchun uy shchitida avtomat o'chirgich turadi — u umumiy tok chegaradan oshsa zanjirni uzadi.",
 ]),
),

"Parallel zanjirni o'lchab tekshirish": D(
 ("O'lchov rejasi", [
  "1) Har bir shoxdagi kuchlanishni o'lchang — hammasi bir xil chiqishi kerak.",
  "2) Har bir shoxdagi tokni alohida o'lchang (shoxni uzib).",
  "3) Umumiy tokni manba yonida o'lchang.",
  "4) Shox toklarining yig'indisini umumiy tok bilan solishtiring.",
  "5) Umumiy qarshilikni hisoblab, U/I nisbati bilan tekshiring.",
 ]),
 ("Kutilgan natijalar", [
  "Kuchlanishlar bir xil (0,05 V gacha farq normal — simlardagi tushish).",
  "Shox toklari yig'indisi umumiy tokka teng.",
  "Kichik qarshilikli shoxda tok ko'proq oqadi.",
  "Umumiy qarshilik eng kichik shoxdan ham kichik chiqadi — bu ko'pchilikni hayratda qoldiradi va aynan shuning uchun tajribada ko'rsatish kerak.",
 ]),
),

"Aralash (ketma-ket + parallel) ulanish": D(
 ("Tahlil qilish tartibi", [
  "1) Sxemani ko'zdan kechirib, parallel guruhlarni topib belgilang.",
  "2) Har bir parallel guruhni BITTA ekvivalent rezistor bilan almashtiring.",
  "3) Endi zanjir sof ketma-ket bo'ladi — qarshiliklarni qo'shing.",
  "4) Umumiy tokni toping: I = U / Rumumiy.",
  "5) Orqaga qayting: har bir guruhdagi kuchlanish va toklarni hisoblang.",
 ]),
 ("Ishlangan misol", [
  "Manba 12 V. R1 = 100 Om ketma-ket, keyin R2 = 200 Om va R3 = 200 Om parallel.",
  "Parallel guruh: R23 = 200 x 200 / 400 = 100 Om.",
  "Umumiy: R = 100 + 100 = 200 Om. Tok: I = 12 / 200 = 0,06 A = 60 mA.",
  "R1 da: U = 0,06 x 100 = 6 V. Parallel guruhda ham 6 V qoladi.",
  "Har bir parallel rezistorda: I = 6 / 200 = 0,03 A = 30 mA. Ikkalasi 60 mA — umumiy tokka teng.",
 ]),
),

"Murakkab zanjirni tahlil qilish": D(
 ("Tahlil usullari", [
  "Soddalashtirish: parallel va ketma-ket guruhlarni bosqichma-bosqich bitta rezistorga keltirish.",
  "Kirxgofning birinchi qonuni: tugunga kirgan tok undan chiqqan tokka teng.",
  "Kirxgofning ikkinchi qonuni: yopiq halqada kuchlanishlar yig'indisi nolga teng.",
  "Bu ikki qonun har qanday zanjirni yechishga yetadi, faqat tenglamalar soni ortadi.",
 ]),
 ("Amaliy maslahatlar", [
  "Sxemani qayta chizing: chalkash chizilgan zanjir soddalashtirilgandan keyin oddiy ko'rinishi mumkin.",
  "Bir xil nuqtaga ulangan simlarni belgilang — ular bitta tugun hisoblanadi.",
  "Har bosqichda oraliq natijani yozib boring.",
  "Yechim tugagach tekshiring: hamma tushishlar yig'indisi manbaga tengmi, hamma toklar tugunlarda mos keladimi.",
  "Eng ishonchli tekshiruv — zanjirni yig'ib multimetr bilan o'lchash.",
 ]),
),

"Kuchlanish bo'luvchi": D(
 ("Ishlash prinsipi", [
  "Ikki rezistor ketma-ket ulanadi va ular orasidagi nuqtadan chiqish olinadi.",
  "Formula: Uchiqish = Ukirish x R2 / (R1 + R2), bu yerda R2 — GND tomondagi rezistor.",
  "Ya'ni chiqish kuchlanishi pastki rezistorning umumiy qarshilikdagi ULUSHIGA teng.",
  "Ikki bir xil rezistor — chiqishda yarmi. R2 katta bo'lsa — chiqish ko'proq.",
 ]),
 ("Hisob misollari", [
  "5 V, R1 = 1 kOm, R2 = 1 kOm: chiqish 2,5 V.",
  "5 V, R1 = 1 kOm, R2 = 2 kOm: chiqish 3,33 V. Aynan shu nisbat 5 V ni ESP32 uchun moslashtiradi.",
  "5 V, R1 = 10 kOm, R2 = 1 kOm: chiqish 0,45 V.",
  "9 V, R1 = 4,7 kOm, R2 = 10 kOm: chiqish 6,1 V.",
 ]),
 ("Muhim cheklov", [
  "Bo'luvchi faqat O'LCHOV signali uchun. Undan quvvat olish mumkin emas.",
  "Yuklama ulansa u R2 ga parallel bo'ladi, umumiy qarshilik kamayadi va chiqish kuchlanishi tushib ketadi.",
  "Qoida: yuklama qarshiligi R2 dan kamida 10 barobar katta bo'lishi kerak.",
  "Motor yoki servoni bo'luvchidan quvvatlash mumkin emas — buning uchun stabilizator kerak.",
 ]),
),

"Kuchlanish bo'luvchi: nazariya": D(
 ("Formulaning kelib chiqishi", [
  "Ketma-ket zanjirda tok bir xil: I = U / (R1 + R2).",
  "R2 dagi kuchlanish: U2 = I x R2 = U x R2 / (R1 + R2).",
  "Ya'ni formula Om qonunidan to'g'ridan-to'g'ri kelib chiqadi, uni yodlash shart emas.",
  "Nisbat muhim, mutlaq qiymat emas: 1 kOm + 1 kOm ham, 10 kOm + 10 kOm ham yarmini beradi.",
 ]),
 ("Qiymatlarni tanlash", [
  "Juda kichik qarshilik (masalan 10 + 10 Om) — bo'luvchi ko'p tok tortadi va isrof bo'ladi.",
  "Juda katta qarshilik (masalan 1 + 1 MOm) — shovqinga sezgir bo'ladi va yuklama ta'siri kuchayadi.",
  "Optimal oraliq: 1 kOm dan 100 kOm gacha.",
  "Batareyali qurilmada kattaroq qiymat olinadi — tok tejaladi.",
 ]),
),

"Kuchlanish bo'luvchi: amaliy o'lchov": D(
 ("O'lchov mashqi", [
  "Uch xil nisbatdagi bo'luvchi yig'ing: 1:1, 1:2, 1:9.",
  "Har biri uchun chiqish kuchlanishini avval hisoblang, keyin o'lchang.",
  "Natijalarni jadvalga yozing: R1, R2, hisoblangan, o'lchangan, farq (%).",
  "Farq odatda 5 % dan kam bo'ladi — bu rezistor bardoshidan kelib chiqadi.",
 ]),
 ("Yuklama ta'sirini ko'rsatish", [
  "Bo'luvchi chiqishiga LED (rezistor bilan) ulang va kuchlanishni qayta o'lchang.",
  "Kuchlanish sezilarli tushadi — bu yuklamaning ta'siri.",
  "Endi bo'luvchi rezistorlarini 10 barobar kichikroq qilib (masalan 1 kOm o'rniga 100 Om) qayta sinang: tushish kamayadi.",
  "Xulosa: bo'luvchi qarshiligi yuklamadan ancha kichik bo'lsa u barqarorroq ishlaydi, lekin ko'proq tok sarflaydi.",
 ]),
),

"Kuchlanish bo'luvchi va sensor ulash": D(
 ("Sensorni bo'luvchi sifatida ulash", [
  "Fotorezistor va termistor — bu O'ZGARUVCHAN QARSHILIK. Ularni to'g'ridan-to'g'ri o'lchab bo'lmaydi.",
  "Plata faqat KUCHLANISHNI o'qiy oladi, qarshilikni emas.",
  "Shuning uchun sensor doimiy rezistor bilan bo'luvchi hosil qiladi va o'rtadagi nuqta o'qiladi.",
  "Sensor qarshiligi o'zgargani sari bo'luvchining nisbati o'zgaradi va chiqish kuchlanishi ham o'zgaradi.",
 ]),
 ("Doimiy rezistorni tanlash", [
  "Qoida: doimiy rezistor sensor qarshiligining O'RTA qiymatiga yaqin bo'lishi kerak.",
  "Fotorezistor xonada 5-20 kOm — shuning uchun 10 kOm olinadi.",
  "Termistor 25 °C da 10 kOm — u ham 10 kOm bilan juftlanadi.",
  "Noto'g'ri tanlansa sezgirlik yo'qoladi: qiymat oraliqning bir chetiga siqilib qoladi.",
 ]),
 ("Ulanish tartibi va uning ta'siri", [
  "Variant A: 5V -> sensor -> (chiqish) -> rezistor -> GND. Sensor qarshiligi kamaysa chiqish OSHADI.",
  "Variant B: 5V -> rezistor -> (chiqish) -> sensor -> GND. Sensor qarshiligi kamaysa chiqish KAMAYADI.",
  "Ikkalasi ham to'g'ri, faqat mantiq teskari bo'ladi.",
  "Qaysi variant ishlatilganini bilish shart, aks holda dasturda chegara noto'g'ri qo'yiladi.",
 ]),
),

# ============================================================ MONTAJ VA SXEMA
"Breadboard tuzilishi: qaysi teshiklar o'zaro bog'langan": D(
 ("Ichki ulanishlar", [
  "Chetdagi uzun qatorlar (+ va - belgili) — QUVVAT SHINALARI. Ular butun uzunlik bo'ylab bog'langan.",
  "O'rtadagi qisqa qatorlar — 5 tadan teshik gorizontal bog'langan.",
  "O'rtadagi ariq (chuqurcha) chap va o'ng tomonni AJRATADI — ular bog'lanmagan.",
  "Ariq bejiz emas: mikrosxemaning ikki qator oyog'i shu ariq ustiga qo'yiladi va ular tutashib ketmaydi.",
  "Ba'zi breadboardlarda quvvat shinalari o'rtadan uzilgan — buni multimetrning signalli rejimi bilan tekshirish kerak.",
 ]),
 ("Ichida nima bor", [
  "Har bir 5 teshikli qator ostida metall prujina (klipsa) turadi.",
  "Sim yoki oyoq kiritilganda prujina uni siqib ushlaydi va kontakt hosil qiladi.",
  "Shuning uchun kavsharlash kerak emas va sxemani istagancha o'zgartirish mumkin.",
  "Kamchiligi: prujina vaqt o'tishi bilan bo'shashadi va kontakt ishonchsiz bo'lib qoladi.",
  "Yana bir cheklov: breadboard katta tokka (2 A dan ortiq) mo'ljallanmagan.",
 ]),
),

"Breadboard: ichki ulanishlar xaritasi": D(
 ("Xaritani o'zingiz tuzish", [
  "Multimetrni signalli rejimga qo'ying.",
  "Bir teshikka bitta shchupni, qo'shnisiga ikkinchisini tegizing: signal chiqsa — bog'langan.",
  "Shu yo'l bilan gorizontal qator, vertikal ustun va quvvat shinalarini tekshiring.",
  "Natijani qog'ozda xarita qilib chizing — bu keyin har bir yig'ishda kerak bo'ladi.",
  "Ariqning ikki tomonini ham tekshiring: ular bog'lanmagan bo'lishi kerak.",
 ]),
 ("Xaritadan foydalanish", [
  "Bir qatorga ikki komponent oyog'ini qo'ysangiz — ular ULANGAN bo'ladi.",
  "Ularni ajratish uchun har birini alohida qatorga qo'yish kerak.",
  "Bu eng ko'p uchraydigan xato: ikki oyoq tasodifan bir qatorga tushib qoladi va qisqa tutashuv hosil bo'ladi.",
  "Yig'ishdan oldin sxemani qog'ozda breadboard katakchalari bilan chizib chiqish bu xatoning oldini oladi.",
 ]),
),

"Breadboard va montaj qoidalari": D(
 ("Montaj tartibi", [
  "1) Avval quvvat shinalarini ulang: 5V va GND ni chetdagi qatorlarga.",
  "2) Katta komponentlarni (mikrosxema, modul) joylashtiring.",
  "3) Keyin kichiklarni (rezistor, LED) qo'shing.",
  "4) Oxirida simlarni torting.",
  "5) Quvvatni ENG OXIRIDA bering.",
 ]),
 ("Tartib qoidalari", [
  "Simlar qisqa va yassi bo'lsin — osilgan uzun simlar uzilib ketadi va xatoni yashiradi.",
  "Rang bilan belgilang: qizil — plyus, qora yoki ko'k — GND, boshqa ranglar — signal.",
  "Simlar komponent ustidan o'tmasin — ular komponentni ko'rishga xalaqit beradi.",
  "Bo'sh joy qoldiring: zich yig'ilgan sxemani tekshirish qiyin.",
  "Ishdan keyin sxemani suratga oling — keyingi darsda qayta yig'ish osonlashadi.",
 ]),
),

"Montaj madaniyati: toza va tushunarli yig'ish": D(
 ("Nima uchun tartib muhim", [
  "Tartibli sxemada xato bir necha barobar tez topiladi.",
  "Boshqa odam (yoki bir haftadan keyingi o'zingiz) sxemani tushuna oladi.",
  "Tasodifiy qisqa tutashuv ehtimoli kamayadi.",
  "Sxemani suratga olib hujjatga qo'yish mumkin bo'ladi.",
 ]),
 ("Tartib mezonlari", [
  "Simlar to'g'ri burchak ostida buriladi, chalkashmaydi.",
  "Bir xil vazifadagi simlar bir xil rangda.",
  "Komponentlar bir yo'nalishda joylashtiriladi (masalan rezistorlarning yozuvlari bir tomonga qaragan).",
  "Quvvat simlari signal simlaridan alohida yo'lda yuradi.",
  "Baholash usuli: sxemani boshqa juftlikka ko'rsatib, ular uni tushuna oladimi degan savol.",
 ]),
),

"Zanjir va sxema tili": D(
 ("Nima uchun shartli belgilar kerak", [
  "Haqiqiy komponentlarni chizish uzoq va noaniq: har bir rezistor har xil ko'rinadi.",
  "Shartli belgi esa bir xil va butun dunyoda tushunarli — bu texnik TIL.",
  "Sxema komponentning qanday ko'rinishini emas, uning VAZIFASINI va ULANISHINI ko'rsatadi.",
  "Shuning uchun sxemada komponentlarning haqiqiy joylashuvi aks etmasligi mumkin.",
 ]),
 ("Asosiy belgilar", [
  "Batareya — uzun va kalta chiziqlar juftligi (uzun = plyus).",
  "Rezistor — to'g'ri to'rtburchak yoki zigzag chiziq.",
  "LED — uchburchak va chiziq, yonida ikki strelka (nur chiqishi).",
  "Diod — uchburchak va chiziq (strelkasiz).",
  "Kondensator — ikki parallel chiziq (elektrolitda biri egri).",
  "Kalit — uzilgan chiziq va uni tutashtiruvchi tayoqcha.",
  "GND — pastga qaragan uch chiziq yoki uchburchak.",
  "Simlarning kesishuvi: nuqta bor bo'lsa ulangan, nuqtasiz bo'lsa shunchaki ustidan o'tgan.",
 ]),
),

"Sxema chizish: belgilar tili": D(
 ("Sxema chizish qoidalari", [
  "Kuchlanish yuqoridan pastga: plyus tepada, GND pastda.",
  "Signal chapdan o'ngga: kirish chapda, chiqish o'ngda.",
  "Simlar faqat gorizontal va vertikal chiziladi, qiyshiq emas.",
  "Har bir komponentga belgi va qiymat yoziladi: R1 220 Om, C1 100 nF, D1 1N4007.",
  "Sxema imkon qadar kam kesishuvli bo'lsin — bu o'qishni osonlashtiradi.",
 ]),
 ("Sxemani tekshirish", [
  "Har bir komponentning ikki oyog'i ham biror joyga ulanganini tekshiring.",
  "Manbadan boshlab halqani barmoq bilan yurib chiqing va manbaga qayting.",
  "Kesishuvlarda nuqta bor-yo'qligini aniq belgilang — bu eng ko'p chalkashlik tug'diradigan joy.",
  "Sxemani boshqa o'quvchiga berib, u shu bo'yicha zanjirni yig'a olsa — sxema to'g'ri chizilgan.",
 ]),
),

"Printsipial sxemani o'qish": D(
 ("O'qish tartibi", [
  "1) Manbani toping: kuchlanishi qancha, plyus va GND qayerda.",
  "2) Signal yo'lini kuzating: kirishdan chiqishgacha.",
  "3) Har bir komponentning vazifasini aniqlang.",
  "4) Qiymatlarni yozib oling: rezistorlar, kondensatorlar.",
  "5) Kritik joylarni belgilang: qutbli komponentlar, mos kelmaydigan kuchlanishlar.",
 ]),
 ("Sxemadan breadboardga o'tish", [
  "Sxema joylashuvni ko'rsatmaydi — uni o'zingiz o'ylab topasiz.",
  "Avval sxemadagi har bir tugunga (bog'langan nuqtalar guruhiga) breadboardda bitta qator ajrating.",
  "Keyin komponentlarni shu qatorlarga ulang.",
  "Har bir ulanishni sxemada belgilab boring — shunda hech biri qolib ketmaydi.",
  "Yig'ilgach, sxema bo'yicha qaytadan tekshirib chiqing.",
 ]),
),

"O'z sxemangni qog'ozda chizish": D(
 ("Loyihalash tartibi", [
  "1) Qurilma nima qilishini bir gapda yozing.",
  "2) Kerakli komponentlarni ro'yxat qiling.",
  "3) Blok sxemani chizing: manba, kirish, boshqaruv, chiqish.",
  "4) Har bir blokni komponentlar bilan to'ldiring.",
  "5) Qiymatlarni hisoblang (rezistorlar, kondensatorlar).",
  "6) Tekshiring va faqat keyin yig'ing.",
 ]),
 ("Ko'p uchraydigan xatolar", [
  "Rezistorni unutish — LED to'g'ridan-to'g'ri ulanadi.",
  "GND ni ulamaslik — zanjir yopilmaydi.",
  "Qutbli komponentni teskari chizish.",
  "Kesishuvda nuqta qo'yish yoki qo'ymaslikni chalkashtirish.",
  "Qiymatlarni yozmaslik — sxema keyin ishga yaramaydi.",
 ]),
),

"Sxemani chizish: o'z zanjiringni qog'ozda": D(
 ("Chizmadan yig'ishga", [
  "Chizma tugagach, uni boshqa o'quvchiga berib tekshirtiring — u tushuna oladimi.",
  "Keyin chizma bo'yicha zanjirni yig'ing va CHIZMANI o'zgartirmasdan ishlating.",
  "Yig'ishda muammo chiqsa — bu chizmada kamchilik borligini bildiradi, uni chizmada tuzating.",
  "Yakuniy chizma ish daftariga tozalab ko'chiriladi.",
 ]),
 ("Chizmani hujjat sifatida saqlash", [
  "Sana, muallif va qurilma nomi yoziladi.",
  "Komponentlar ro'yxati alohida jadvalda beriladi.",
  "O'lchangan qiymatlar chizma yoniga yoziladi.",
  "Keyingi versiyada nima o'zgargani belgilanadi.",
  "Bu odat chorak loyihasini hujjatlashtirishda katta vaqt tejaydi.",
 ]),
),

"Sxema bo'yicha yig'ish mashqi": D(
 ("Mashq tartibi", [
  "O'qituvchi tayyor sxema beradi, o'quvchilar uni gapirmasdan yig'adi.",
  "Yig'ilgandan keyin juftliklar sxemalarini almashtirib tekshiradi.",
  "Xato topilsa, u sxemada belgilanadi va tuzatiladi.",
  "Oxirida zanjirga quvvat beriladi va ishlashi tekshiriladi.",
 ]),
 ("Baholash mezonlari", [
  "Sxemaga to'liq mos kelishi (hamma ulanish o'z joyida).",
  "Qutblarning to'g'riligi.",
  "Montaj tozaligi: simlar qisqa, ranglar tartibli.",
  "Vaqt: mashq takrorlangan sari yig'ish tezlashishi kerak.",
  "Ishlashi: quvvat berilganda kutilgan natija chiqishi.",
 ]),
),

"Zanjir elementlari va ularning shartli belgilari": D(
 ("Belgilarni guruhlab yodlash", [
  "MANBALAR: batareya, akkumulyator, quvvat manbai, GND.",
  "PASSIV ELEMENTLAR: rezistor, kondensator, g'altak, potensiometr.",
  "YARIMO'TKAZGICHLAR: diod, LED, stabilitron, tranzistor, fotorezistor.",
  "BOSHQARUV: kalit, tugma, rele.",
  "ISTE'MOLCHILAR: lampochka, motor, zummer.",
  "Guruhlab yodlash alohida-alohida yodlashdan ancha samarali.",
 ]),
 ("Belgilarni tanish mashqi", [
  "Kartochkalar tayyorlang: bir tomonda belgi, ikkinchisida nom.",
  "Juftlikda ishlang: bittasi belgini ko'rsatadi, ikkinchisi nomini aytadi.",
  "Keyin teskari: nom aytiladi, belgi chiziladi.",
  "Vaqt bilan sinov: 15 belgini necha soniyada tanib olish mumkin.",
  "Eng foydali mashq: tayyor sxemadagi hamma belgini nomlab chiqish.",
 ]),
),

# ============================================================ DIOD
"Diod: tok faqat bir tomonga": D(
 ("Diodning asosiy xususiyati", [
  "Diod tokni faqat BIR yo'nalishda o'tkazadi: anoddan katodga.",
  "Teskari yo'nalishda u deyarli o'tkazmaydi (juda kichik sizib chiqish toki qoladi).",
  "Korpusdagi halqa KATOD tomonini ko'rsatadi.",
  "Sxemadagi belgida uchburchakning uchi tok yo'nalishini ko'rsatadi, chiziq esa katod.",
 ]),
 ("Kuchlanish tushishi", [
  "To'g'ri yo'nalishda diodda 0,6-0,7 V tushadi (kremniy diod).",
  "Germaniy diodda 0,3 V, Shottki diodda 0,2-0,4 V.",
  "Bu tushish deyarli o'zgarmas: tok ikki barobar oshsa ham tushish ozgina o'zgaradi.",
  "Shuning uchun diod Om qonuniga bo'ysunmaydi — u chiziqsiz element.",
 ]),
 ("Teskari kuchlanish chegarasi", [
  "Har bir diodning maksimal teskari kuchlanishi bor (1N4007 uchun 1000 V).",
  "Undan oshsa diod \"teshiladi\" va ikki tomonga o'tkaza boshlaydi — ya'ni buziladi.",
  "Maksimal to'g'ri tok ham cheklangan: 1N4007 uchun 1 A.",
  "Diod tanlashda ikkala chegarani ham tekshirish kerak.",
 ]),
),

"Diod: p-n o'tish": D(
 ("p-n o'tish qanday hosil bo'ladi", [
  "Kremniyga bir tomondan ortiqcha elektron beruvchi qo'shimcha kiritiladi — bu n-tur.",
  "Ikkinchi tomondan elektron yetishmovchiligi (\"kovak\") hosil qiluvchi qo'shimcha — bu p-tur.",
  "Ular tutashgan chegarada elektronlar va kovaklar bir-birini to'ldiradi va erkin zaryadsiz qatlam hosil bo'ladi.",
  "Bu qatlam \"to'siq\" vazifasini bajaradi va tokni o'tkazmaydi.",
 ]),
 ("Nima uchun tok bir tomonga o'tadi", [
  "Anodga plyus berilsa (to'g'ri qutblash): to'siq torayadi va 0,7 V dan keyin butunlay yo'qoladi — tok oqadi.",
  "Anodga minus berilsa (teskari qutblash): to'siq kengayadi va tok o'tmaydi.",
  "Aynan shu asimmetriya butun yarimo'tkazgich elektronikasining asosi.",
  "Tranzistor — bu ikki p-n o'tishning ketma-ket birlashmasi.",
  "LED ham p-n o'tish, faqat unda elektron va kovak birlashganda energiya YORUG'LIK sifatida chiqadi.",
 ]),
),

"Diodni tekshirish va to'g'ri qutblash": D(
 ("Multimetr bilan tekshirish", [
  "Multimetrni DIOD rejimiga qo'ying (uchburchak va chiziq belgisi).",
  "Qizil shchupni anodga, qorasini katodga tegizing: ekranda 0,5-0,7 V chiqishi kerak.",
  "Shchuplarni almashtiring: ekranda \"OL\" yoki \"1\" chiqishi kerak (o'tkazmaydi).",
  "Ikkala tomonda ham 0 chiqsa — diod teshilgan (qisqa tutashgan).",
  "Ikkala tomonda ham OL chiqsa — diod uzilgan.",
 ]),
 ("Qutbni aniqlash", [
  "Korpusdagi halqa (odatda oq yoki kulrang) — KATOD.",
  "Halqa ko'rinmasa yoki shubha bo'lsa — multimetrning diod rejimi bilan aniqlanadi: qiymat chiqqan holatda qizil shchup anodda.",
  "LEDda uzun oyoq — anod, korpusning yassi qirrasi tomonidagi kalta oyoq — katod.",
  "Elektrolit kondensatorda esa aksincha: korpusdagi chiziq MINUS tomonni ko'rsatadi. Bu ikkisini chalkashtirmaslik kerak.",
 ]),
),

"Diod va himoya": D(
 ("Teskari qutbdan himoya", [
  "Zanjir kirishiga ketma-ket diod qo'yilsa, manba teskari ulanganda tok umuman o'tmaydi.",
  "Afzalligi: juda oddiy, bitta komponent.",
  "Kamchiligi: to'g'ri ulanganda ham 0,7 V yo'qoladi (Shottki diodda 0,3 V).",
  "9 V manbada bu sezilmaydi, 3,3 V manbada esa sezilarli.",
 ]),
 ("Induktiv yuklamadan himoya", [
  "Motor va rele g'altagi — induktiv yuklama. Tok uzilganda ular o'zida yuqori teskari kuchlanish hosil qiladi.",
  "Bu kuchlanish 100 voltdan oshishi mumkin va tranzistorni teshib yuboradi.",
  "Yechim: yuklamaga PARALLEL va TESKARI qutblangan diod (katod plyusga qaragan).",
  "Bu diod \"flyback\" yoki \"o'chiruvchi\" diod deb ataladi. U teskari kuchlanish uchun yo'l ochib beradi.",
  "Diodsiz sxema bir necha marta ishlab, keyin buziladi — bu eng ko'p uchraydigan \"tushunarsiz\" nosozlik.",
 ]),
),

"Diod bilan zanjirni himoyalash": D(
 ("Himoya sxemalari", [
  "Ketma-ket diod — teskari qutbdan saqlaydi, lekin kuchlanish yo'qotadi.",
  "Parallel diod (teskari qutblangan) — teskari ulanganda qisqa tutashuv hosil qilib, predoxranitelni kuydiradi va sxemani saqlaydi.",
  "Flyback diod — induktiv yuklama yonida, majburiy.",
  "Stabilitron — kuchlanish chegaradan oshsa ortiqchasini GND ga o'tkazadi.",
  "MOSFET bilan himoya — kuchlanish yo'qotmaydi, lekin murakkabroq.",
 ]),
 ("Diod tanlash", [
  "Maksimal tok yuklamadan kamida 1,5 barobar katta bo'lishi kerak.",
  "Maksimal teskari kuchlanish manbadan kamida 2 barobar katta.",
  "Tez ishlash kerak bo'lsa (PWM bilan) — Shottki yoki tez diod (1N4148 kabi).",
  "Keng tarqalganlari: 1N4007 (1 A, 1000 V), 1N4148 (0,2 A, tez), 1N5819 (Shottki, 1 A).",
 ]),
),

"Diod ko'prigi: o'zgaruvchan tokni to'g'rilash": D(
 ("Ko'prik sxemasi", [
  "To'rtta diod romb shaklida ulanadi. Ikki uchiga o'zgaruvchan tok beriladi, qolgan ikkisidan o'zgarmas olinadi.",
  "Kirish signalining musbat yarim to'lqinida ikki diod ochiladi, manfiy yarim to'lqinda boshqa ikkitasi.",
  "Natijada chiqishda tok DOIM bir tomonga oqadi — manfiy yarim to'lqin \"ag'darib\" qo'yiladi.",
  "Bu to'liq to'lqinli to'g'rilash deb ataladi.",
 ]),
 ("Silliqlash", [
  "To'g'rilangandan keyin kuchlanish hali ham \"pulsatsiya\" qiladi — u noldan maksimumgacha tebranadi.",
  "Chiqishga katta kondensator (1000 mkF va undan ko'p) qo'yiladi.",
  "Kondensator maksimumda zaryadlanadi va pasayish paytida zaryadni beradi — natijada kuchlanish tekislanadi.",
  "Keyin stabilizator (7805 kabi) qo'yilsa aniq 5 V olinadi.",
  "Har bir telefon zaryadlagichi ichida aynan shu zanjir bor.",
 ]),
),

"Stabilitron: kuchlanishni ushlab turish": D(
 ("Stabilitron qanday ishlaydi", [
  "Stabilitron TESKARI qutblab ulanadi — bu oddiy dioddan asosiy farqi.",
  "Teskari kuchlanish belgilangan qiymatga (stabilizatsiya kuchlanishiga) yetganda u tokni o'tkaza boshlaydi.",
  "Shundan keyin kuchlanish deyarli o'zgarmaydi: tok oshsa ham stabilitronda kuchlanish bir xil qoladi.",
  "Shuning uchun u chiqish kuchlanishini belgilangan darajada ushlab turadi.",
 ]),
 ("Sxema va hisob", [
  "Stabilitron ketma-ket rezistor bilan ishlatiladi — usiz u kuyadi.",
  "Rezistor ortiqcha kuchlanishni o'ziga oladi va tokni cheklaydi.",
  "Hisob: R = (Ukirish - Ustab) / (Iyuklama + Istab). Istab odatda 5-10 mA olinadi.",
  "Misol: 12 V dan 5,1 V olish, yuklama 20 mA. R = (12 - 5,1) / 0,03 = 230 Om, amalda 220 Om.",
  "Kamchiligi: rezistorda quvvat isrof bo'ladi. Shuning uchun katta tokda stabilizator mikrosxemasi ishlatiladi.",
 ]),
),

"Optopara va IK juftlik": D(
 ("Optopara tuzilishi", [
  "Ichida ikki element bor: infraqizil LED va fototranzistor (yoki fotodiod).",
  "Ular bir korpusda, lekin ELEKTR JIHATDAN butunlay ajratilgan — orasida faqat yorug'lik o'tadi.",
  "LEDga tok berilsa u yonadi, fototranzistor esa yorug'likni sezib ochiladi.",
  "Natijada bir zanjirdagi signal ikkinchi zanjirga uzatiladi, lekin ular bir-biriga elektr jihatdan ulanmagan.",
 ]),
 ("Nima uchun kerak", [
  "Yuqori kuchlanishli qismni past kuchlanishli boshqaruvdan ajratish (rele modullarida shunday).",
  "Kuchli shovqinli muhitda signalni himoyalash.",
  "Turli GND darajalaridagi qurilmalarni bog'lash.",
  "Xavfsizlik: 220 V tomondagi nosozlik boshqaruv platasiga o'tmaydi.",
 ]),
 ("IK juftlik (chiqarish va qabul qilish)", [
  "Alohida IK LED va fototranzistor juftligi — masofadan sezish uchun.",
  "To'siq rejimi: LED va qabul qilgich qarama-qarshi, orasidan o'tgan buyum signalni uzadi.",
  "Aks-sado rejimi: ikkalasi yonma-yon, buyumdan qaytgan nur o'lchanadi. Chiziq bo'ylab yuruvchi robotda shunday.",
  "Quyosh nuri xalaqit beradi — shuning uchun signal modulyatsiya qilinadi (38 kHz) yoki qora korpus ishlatiladi.",
 ]),
),

# ============================================================ KONDENSATOR
"Kondensator: zaryad to'plovchi idish": D(
 ("Kondensator nima qiladi", [
  "Ikki metall plastina va ular orasidagi izolyator (dielektrik).",
  "Kuchlanish berilganda bir plastinada elektronlar to'planadi, ikkinchisida yetishmaydi.",
  "Manba uzilsa ham bu zaryad saqlanadi — kondensator uni ushlab turadi.",
  "Zanjir ulansa zaryad oqib chiqadi va kondensator bo'shaydi.",
  "Ya'ni kondensator — bu juda kichik va juda tez ishlaydigan batareya.",
 ]),
 ("Batareyadan farqi", [
  "Batareya kimyoviy reaksiya bilan ishlaydi, kondensator esa faqat elektr maydoni bilan.",
  "Kondensator ancha kam energiya saqlaydi, lekin uni juda TEZ beradi va oladi.",
  "Batareya minglab marta zaryadlanadi, kondensator esa millionlab marta.",
  "Shuning uchun kondensator energiya saqlash uchun emas, tez o'zgarishlarni silliqlash uchun ishlatiladi.",
 ]),
),

"Kondensator: tuzilishi va sig'imi": D(
 ("Sig'im nimaga bog'liq", [
  "Sig'im (C) faradda o'lchanadi. Formula: C = e x S / d.",
  "S — plastinalar yuzasi: katta bo'lsa sig'im katta.",
  "d — plastinalar orasidagi masofa: kichik bo'lsa sig'im katta.",
  "e — dielektrik xususiyati: material qanchalik yaxshi bo'lsa sig'im shuncha katta.",
  "Shuning uchun katta sig'imli kondensatorlar plastinalarni rulon qilib o'raydi — yuzani oshirish uchun.",
 ]),
 ("Birliklar va qiymatlar", [
  "1 F juda katta birlik. Amalda: 1 mkF = 0,000001 F, 1 nF = 0,001 mkF, 1 pF = 0,001 nF.",
  "Keramik kondensatorlar: 10 pF dan 1 mkF gacha. Qutbsiz.",
  "Elektrolit kondensatorlar: 1 mkF dan 10 000 mkF gacha. QUTBLI.",
  "Kodni o'qish: keramikda \"104\" = 10 va to'rtta nol = 100 000 pF = 100 nF = 0,1 mkF.",
  "\"223\" = 22 va uchta nol = 22 000 pF = 22 nF.",
 ]),
 ("Ishchi kuchlanish", [
  "Har bir kondensatorda maksimal kuchlanish yozilgan: 16 V, 25 V, 50 V.",
  "Undan oshsa dielektrik teshiladi va kondensator ishdan chiqadi (elektrolit shishib yorilishi mumkin).",
  "Qoida: ishchi kuchlanish zanjirdagidan kamida 1,5-2 barobar katta bo'lsin.",
  "5 V zanjirda 10 V yoki 16 V li kondensator olinadi.",
 ]),
),

"Kondensator turlari va tanlash": D(
 ("Asosiy turlar", [
  "Keramik: kichik sig'im (pF-mkF), qutbsiz, arzon, tez. Shovqin filtri uchun eng ko'p ishlatiladi.",
  "Elektrolit: katta sig'im (mkF-mF), QUTBLI, quvvat silliqlash uchun.",
  "Tantal: elektrolitga o'xshash, lekin kichikroq va ishonchliroq, qimmatroq.",
  "Plyonkali: barqaror, aniq sxemalar uchun.",
  "Superkondensator: juda katta sig'im (faradlarda), zaxira quvvat uchun.",
 ]),
 ("Qaysi holatda qaysi tur", [
  "Mikrosxema oyoqlari yonida shovqin filtri — 100 nF keramik.",
  "Quvvat liniyasini silliqlash — 100-470 mkF elektrolit.",
  "Motor ishga tushganda kuchlanish cho'kishiga qarshi — 470-1000 mkF elektrolit.",
  "Tugma sakrashini yo'qotish — 100 nF keramik.",
  "RC taymer — 1-100 mkF, aniqlik kerak bo'lsa plyonkali.",
 ]),
 ("Qutbga e'tibor", [
  "Elektrolit kondensatorda korpusdagi CHIZIQ va kalta oyoq — MINUS.",
  "Teskari ulansa u qiziydi, shishadi va yorilishi mumkin.",
  "Bu darsda ko'z himoyasi kerak bo'ladigan kam sonli holatlardan biri.",
  "Keramikda qutb yo'q — istalgan tomonga ulanadi.",
 ]),
),

"Kondensatorni zaryadlash va bo'shatish": D(
 ("Zaryadlanish jarayoni", [
  "Rezistor orqali ulangan kondensator bir zumda emas, ASTA to'ladi.",
  "Boshida tok katta (kondensator bo'sh), keyin kondensator to'lgani sari tok kamayadi.",
  "Vaqt doimiysi: t = R x C. Shu vaqtda kondensator manba kuchlanishining 63 % iga yetadi.",
  "5t vaqtdan keyin amalda to'liq zaryadlangan deb hisoblanadi.",
  "Misol: R = 10 kOm, C = 100 mkF -> t = 1 sekund, to'lishi ~5 sekund.",
 ]),
 ("Bo'shash jarayoni", [
  "Manba uzilib, kondensator rezistor orqali GND ga ulansa u bo'sha boshlaydi.",
  "Bo'shash ham eksponensial: t vaqtda 37 % qoladi, 5t da amalda nol.",
  "Zaryadlash va bo'shash vaqti bir xil rezistor bilan bir xil bo'ladi.",
  "Turli rezistor ishlatilsa (diod orqali) — tez zaryadlanib, sekin bo'shaydigan sxema olinadi.",
 ]),
 ("Tajribada ko'rish", [
  "LED va katta kondensator (1000 mkF) bilan: manba uzilganda LED bir necha sekund yonib turadi.",
  "Multimetrni kondensatorga parallel ulab, zaryadlanish paytida raqamlarning sekinlashib borishini kuzatish mumkin.",
  "R yoki C ni ikki barobar oshiring — vaqt ham ikki barobar uzayadi.",
  "XAVFSIZLIK: katta kondensator zaryadni uzoq saqlaydi. Ishdan keyin uni rezistor orqali bo'shatish kerak.",
 ]),
),

"RC zanjir: vaqtni sanash": D(
 ("RC bilan vaqt hosil qilish", [
  "RC zanjir — eng oddiy taymer. Vaqt R va C qiymatlari bilan belgilanadi.",
  "t = R x C (R omda, C faradda, natija sekundda).",
  "Kerakli kechikishni olish uchun ikki qiymatdan birini o'zgartirish yetadi.",
  "Misol: 5 sekundlik kechikish uchun 100 kOm va 50 mkF (yoki 50 kOm va 100 mkF).",
 ]),
 ("Amaliy qo'llanishlar", [
  "Sekin yonadigan va sekin o'chadigan chiroq.",
  "Tugma sakrashini apparat yo'li bilan yo'qotish.",
  "Avtomatik o'chadigan yoritgich (koridor chirog'i).",
  "Signal filtri: tez shovqin kondensator orqali GND ga o'tib ketadi.",
  "Dasturiy o'xshashi — eksponensial silliqlash: yangi = a x o'lchov + (1-a) x eski.",
 ]),
),

"Motorni himoyalash: diod va kondensator": D(
 ("Motor nima uchun xavfli", [
  "Motor g'altagi — induktivlik. Tok to'satdan uzilganda u o'zida yuqori teskari kuchlanish hosil qiladi.",
  "Bu kuchlanish 100 voltdan oshishi mumkin va tranzistorni yoki plata pinini teshib yuboradi.",
  "Bundan tashqari motor cho'tkalari uchqun chiqaradi va bu radio shovqin hosil qiladi.",
  "Uchinchi muammo: ishga tushishda motor katta tok tortadi va kuchlanish cho'kadi.",
 ]),
 ("Uch himoya elementi", [
  "FLYBACK DIOD: motorga parallel, teskari qutblangan (katod plyusga). Teskari kuchlanishga yo'l ochadi. MAJBURIY.",
  "KERAMIK KONDENSATOR (100 nF): motor uchlariga parallel. Uchqundan chiqadigan shovqinni yo'qotadi.",
  "ELEKTROLIT KONDENSATOR (470-1000 mkF): quvvat liniyasiga. Ishga tushish paytidagi cho'kishni to'ldiradi.",
  "Uchtasi birga qo'yilsa motorli sxema ishonchli va uzoq ishlaydi.",
 ]),
),

# ============================================================ TRANZISTOR
"Tranzistor: kichik tok katta tokni boshqaradi": D(
 ("Tranzistorning asosiy g'oyasi", [
  "Tranzistor — elektron KALIT: bazaga berilgan kichik tok kollektor orqali katta tokni o'tkazadi.",
  "Kuchaytirish koeffitsienti (hFE yoki beta): 100 bo'lsa, bazadagi 1 mA kollektorda 100 mA gacha ruxsat beradi.",
  "Bu qo'l bilan bosiladigan tugmaning elektron o'rnini bosuvchisi — faqat uni DASTUR boshqaradi.",
  "Suv analogiyasi: baza — kran tutqichi, kollektor-emitter — quvur. Kichik kuch bilan katta oqim boshqariladi.",
 ]),
 ("Nima uchun kerak", [
  "Arduino pini maksimum 40 mA beradi (xavfsizi 20 mA).",
  "Motor 300 mA, rele 80 mA, LED lenta 500 mA tortadi.",
  "Ularni to'g'ridan-to'g'ri pinga ulash pinni, ba'zan butun platani ishdan chiqaradi.",
  "Tranzistor bu muammoni hal qiladi: pin faqat 1-2 mA beradi, katta tok esa alohida manbadan oqadi.",
 ]),
),

"Tranzistor tuzilishi va oyoqlari": D(
 ("Uchta oyoq", [
  "BAZA (B) — boshqaruv oyog'i. Unga rezistor orqali kichik tok beriladi.",
  "KOLLEKTOR (C) — katta tok kiradigan oyoq, yuklama shu yerga ulanadi.",
  "EMITTER (E) — tok chiqadigan oyoq, NPN da GND ga ulanadi.",
  "Sxemadagi belgida emitterda strelka bor: NPN da u tashqariga, PNP da ichkariga qaragan.",
 ]),
 ("Oyoqlarni aniqlash", [
  "Oyoqlar tartibi korpus turiga bog'liq va universal emas.",
  "BC547 (TO-92 korpus, yozuvli tomon o'zimizga qaragan): chapdan o'ngga C, B, E.",
  "2N2222 da tartib boshqacha: E, B, C.",
  "Shuning uchun datasheetga qarash yoki multimetrning \"hFE\" rejimida tekshirish kerak.",
  "Multimetrning diod rejimi bilan ham aniqlash mumkin: baza ikki oyoq bilan ham diod kabi o'tkazadi.",
 ]),
 ("Asosiy parametrlar", [
  "Ic max — maksimal kollektor toki (BC547 uchun 100 mA, TIP120 uchun 5 A).",
  "Uce max — maksimal kuchlanish (BC547 uchun 45 V).",
  "hFE — kuchaytirish koeffitsienti (BC547 uchun 110-800).",
  "P max — maksimal quvvat (BC547 uchun 500 mVt).",
  "Motor uchun BC547 yetmaydi — TIP120 yoki MOSFET kerak bo'ladi.",
 ]),
),

"Tranzistor kalit sifatida": D(
 ("Kalit rejimi nima", [
  "Tranzistor ikki holatda ishlatiladi: butunlay YOPIQ yoki butunlay OCHIQ.",
  "Oraliq holat (kuchaytirgich rejimi) bu yerda ishlatilmaydi — u ko'p issiqlik chiqaradi.",
  "Ochiq holatda kollektor-emitter orasida atigi 0,2-0,3 V tushadi — deyarli sim kabi.",
  "Yopiq holatda tok deyarli nol.",
 ]),
 ("Baza rezistorini hisoblash", [
  "Kollektor toki Ic ma'lum bo'lsin (masalan 200 mA motor).",
  "Kerakli baza toki: Ib = Ic / hFE. Ishonchli ochilishi uchun 5-10 barobar zaxira olinadi.",
  "Ib = 0,2 / 100 x 5 = 0,01 A = 10 mA.",
  "Baza rezistori: R = (Upin - 0,7) / Ib = (5 - 0,7) / 0,01 = 430 Om.",
  "Amalda 1 kOm olinadi — bu ko'p holatda yetarli va pinni ham himoyalaydi.",
 ]),
),

"Tranzistor kalit rejimida": D(
 ("To'liq ochilish (to'yinish)", [
  "Tranzistor to'liq ochilishi uchun bazaga yetarli tok berilishi kerak.",
  "Yetarli tok berilmasa u yarim ochiq qoladi: yuklama to'liq ishlamaydi va tranzistor QIZIYDI.",
  "Bu eng ko'p uchraydigan xato: motor sekin aylanadi va tranzistor qo'lni kuydiradi.",
  "Yechim: baza rezistorini kichraytirish yoki kuchliroq tranzistor (Darlington) olish.",
 ]),
 ("Isishni tekshirish", [
  "To'g'ri ishlaydigan kalit rejimidagi tranzistor deyarli QIZIMAYDI.",
  "Qizisa — u yarim ochiq holatda ishlayapti va sxemani qayta ko'rish kerak.",
  "Quvvatni hisoblash: P = Uce x Ic. To'liq ochiq holatda Uce = 0,3 V, demak P kichik.",
  "Yarim ochiq holatda Uce = 2,5 V bo'lishi mumkin — quvvat 8 barobar ortadi va tranzistor kuyadi.",
 ]),
),

"Tranzistor kalit: takrorlash va mustahkamlash": D(
 ("Sxemani yig'ish tartibi", [
  "1) Emitterni GND ga ulang.",
  "2) Yuklamani (LED, motor) plyus va kollektor orasiga qo'ying.",
  "3) Bazaga 1 kOm rezistor orqali boshqaruv signalini bering.",
  "4) Induktiv yuklama bo'lsa flyback diodni unutmang.",
  "5) Tekshiring: baza signalisiz yuklama ishlamasligi kerak.",
 ]),
 ("Tipik xatolar", [
  "Baza rezistorini unutish — bazaga katta tok oqadi va tranzistor kuyadi.",
  "Emitterni GND ga ulamaslik — sxema umuman ishlamaydi.",
  "Kollektor va emitterni almashtirish — tranzistor kuchsiz ishlaydi yoki umuman ishlamaydi.",
  "Motorda diodni unutish — tranzistor bir necha marta ishlagandan keyin buziladi.",
  "Kuchsiz tranzistor tanlash — u qiziydi va yuklamani to'liq tortmaydi.",
 ]),
),

"Tranzistor bilan motorni yoqish": D(
 ("To'liq sxema", [
  "Motor bir uchi tashqi manba plyusiga, ikkinchi uchi tranzistor kollektoriga.",
  "Tranzistor emitteri GND ga (tashqi manba GND si va plata GND si BIRLASHTIRILADI).",
  "Baza plata pinidan 1 kOm rezistor orqali.",
  "Motorga parallel 1N4007 diod, teskari qutblangan.",
  "Motor uchlariga parallel 100 nF keramik kondensator (shovqinga qarshi).",
 ]),
 ("Tranzistor tanlash", [
  "Kichik motor (100-200 mA): BC547 yetadi, lekin chegarada.",
  "O'rtacha motor (200-500 mA): BD139 yoki 2N2222.",
  "Kuchli motor (0,5-5 A): TIP120 (Darlington) yoki MOSFET IRLZ44N.",
  "MOSFET afzalligi: boshqaruv uchun tok deyarli kerak emas va u kamroq qiziydi.",
  "MOSFET tanlashda \"logic level\" turini olish kerak — u 5 V bilan to'liq ochiladi.",
 ]),
),

"Signalni tranzistor bilan kuchaytirish": D(
 ("Kuchaytirgich rejimi", [
  "Kalit rejimidan farqi: tranzistor oraliq holatda ishlaydi va chiqish signali kirishga proporsional bo'ladi.",
  "Bazaga kichik o'zgaruvchan signal beriladi, kollektorda esa u kuchaytirilgan holda chiqadi.",
  "Kuchaytirish koeffitsienti rezistorlar nisbati bilan belgilanadi.",
  "Bu rejimda tranzistor doim tok o'tkazib turadi va qiziydi.",
 ]),
 ("Amaldagi qo'llanishlar", [
  "Mikrofon signalini kuchaytirish (u millivoltlarda bo'ladi).",
  "Sensor signalini plata o'qiy oladigan darajaga ko'tarish.",
  "Zummerni kuchliroq chalish.",
  "Amalda esa hozir bu vazifalar uchun tayyor mikrosxemalar (operatsion kuchaytirgichlar) ishlatiladi — ular aniqroq va sozlash osonroq.",
 ]),
),

# ============================================================ MOTOR
"Motor tezligini o'zgartirish": D(
 ("Tezlikni boshqarish usullari", [
  "Kuchlanishni o'zgartirish: motor sekinlashadi, lekin momenti ham kamayadi va u past kuchlanishda umuman aylanmay qolishi mumkin.",
  "Rezistor qo'shish: eng yomon usul — energiya rezistorda issiqlikka aylanadi va isrof bo'ladi.",
  "PWM: eng yaxshi usul. Motor to'liq kuchlanishda, lekin qisqa impulslar bilan quvvatlanadi.",
  "PWM da o'rtacha quvvat o'zgaradi, lekin har bir impulsda motor to'liq momentga ega bo'ladi.",
 ]),
 ("PWM ning xususiyatlari", [
  "PWM chastotasi muhim: juda past bo'lsa motor titraydi va chiyillaydi.",
  "Arduino'ning standart PWM chastotasi 490 Hz — bu eshitiladi.",
  "20 kHz dan yuqori chastota quloqqa eshitilmaydi, lekin uni sozlash uchun qo'shimcha kod kerak.",
  "Motor past PWM da (60 dan kam) umuman aylanmaydi — ishga tushish momenti yetmaydi. Bu normal.",
  "Yechim: ishga tushirishda qisqa vaqt 255 berib \"turtki\" berish, keyin kerakli tezlikka tushirish.",
 ]),
),

"Motorning aylanish yo'nalishini o'zgartirish": D(
 ("Yo'nalish nimaga bog'liq", [
  "DC motorda yo'nalish tok yo'nalishiga bog'liq: qutbni almashtirsangiz motor teskari aylanadi.",
  "Bitta tranzistor bilan buni qilib bo'lmaydi — u faqat yoqadi va o'chiradi.",
  "Ikki qutbni almashtirish uchun H-KO'PRIK kerak.",
  "Qo'lda esa DPDT kalit bilan almashtirish mumkin — bu eng oddiy variant.",
 ]),
 ("Amaliy jihatlar", [
  "Yo'nalishni to'satdan almashtirish katta tok tortadi (motor hali inersiya bilan aylanayotgan bo'ladi).",
  "Shuning uchun dasturda avval to'xtatib, 100-200 ms kutib, keyin teskari yo'nalish berish kerak.",
  "Aks holda kuchlanish cho'kadi va plata qayta yuklanadi.",
  "Robotlarda ikki motor teskari yo'nalishda aylantirilsa robot joyida buriladi.",
 ]),
),

"Motor yo'nalishini o'zgartirish: H-ko'prik g'oyasi": D(
 ("H-ko'prik tuzilishi", [
  "To'rtta kalit \"H\" harfi shaklida joylashadi, motor esa o'rtadagi ko'ndalang chiziqda.",
  "Kalitlarni S1 (chap yuqori), S2 (o'ng yuqori), S3 (chap past), S4 (o'ng past) deb belgilaymiz.",
  "S1 va S4 ochiq: tok chapdan o'ngga oqadi — motor bir tomonga aylanadi.",
  "S2 va S3 ochiq: tok o'ngdan chapga oqadi — motor teskari aylanadi.",
  "S3 va S4 ochiq: motor uchlari qisqa tutashadi — keskin TORMOZLANADI.",
  "Hammasi yopiq: motor bo'sh aylanib to'xtaydi (inersiya bilan).",
 ]),
 ("Xavfli holat", [
  "Bir ustundagi ikki kalit (masalan S1 va S3) bir vaqtda ochilsa — manba qisqa tutashadi.",
  "Bu \"shoot-through\" deb ataladi va sxemani bir zumda ishdan chiqaradi.",
  "Shuning uchun tayyor drayverlarda (L298N, L293D) bunga qarshi ichki himoya bor.",
  "O'zi yig'ilgan H-ko'prikda dasturda ehtiyot bo'lish kerak: yo'nalishni almashtirishdan oldin hamma kalitni o'chirish.",
 ]),
),

"Motor tezligini boshqarish": D(
 ("PWM bilan boshqarish", [
  "analogWrite(pin, 0..255) — 0 to'xtagan, 255 to'liq tezlik.",
  "Motor odatda 60-80 dan past PWM da aylanmaydi — bu ishga tushish momenti yetmasligidan.",
  "Shuning uchun foydali oraliq 80 dan 255 gacha bo'ladi.",
  "map() bilan potensiometrni shu oraliqqa moslashtirish qulay: map(pot, 0, 1023, 80, 255).",
 ]),
 ("Ikki motorni moslash", [
  "Ikki bir xil motor bir xil PWM da BIR XIL tezlikda aylanmaydi — ishlab chiqarish farqi.",
  "Robot to'g'ri yurmasa, bir tomonga bir oz kamroq PWM berish kerak (masalan chapga 200, o'ngga 190).",
  "Koeffitsientni tajriba yo'li bilan topish kerak: robotni to'g'ri chiziq bo'ylab yuborib, og'ishini o'lchash.",
  "Aniqroq yechim — enkoder bilan teskari bog'lanish, lekin bu ancha murakkab.",
 ]),
),

# ============================================================ SENSOR
"Sensor tushunchasi va turlari": D(
 ("Sensor nima qiladi", [
  "Sensor fizik kattalikni ELEKTR signalga aylantiradi.",
  "Kirish: harorat, yorug'lik, masofa, harakat, tovush, bosim, namlik.",
  "Chiqish: kuchlanish, qarshilik, tok yoki raqamli kod.",
  "Plata faqat kuchlanishni o'lchay oladi — shuning uchun har bir sensor oxir-oqibat kuchlanishga keltiriladi.",
 ]),
 ("Chiqish turi bo'yicha tasnif", [
  "QARSHILIKLI: fotorezistor, termistor. Ular bo'luvchi bilan ulanadi.",
  "KUCHLANISHLI: ba'zi harorat sensorlari (LM35), joystik, potensiometr. To'g'ridan-to'g'ri analog pinga.",
  "RAQAMLI (0/1): PIR, reed, tilt, tugma. Raqamli pinga.",
  "PROTOKOLLI: DHT22, BMP280, MPU6050. Ular o'zi hisoblab, tayyor raqam beradi. Kutubxona kerak.",
  "CHASTOTALI: TCS3200 rang sensori. Impuls davomiyligi o'lchanadi.",
 ]),
 ("Sensor tanlash mezonlari", [
  "O'lchov oralig'i kerakli oraliqni qamrab olishi kerak.",
  "Aniqlik vazifaga yetarli bo'lishi kerak (o'ta aniq sensor qimmat va ko'pincha keraksiz).",
  "Ta'minot kuchlanishi plataga mos kelishi kerak.",
  "Javob tezligi: PIR sekin, Hall datchigi juda tez.",
  "Interfeys: bo'sh pinlaringiz yetadimi.",
 ]),
),

"Analog va raqamli sensor farqi": D(
 ("Analog sensor", [
  "Chiqishi uzluksiz o'zgaradi va oraliqdagi istalgan qiymatni olishi mumkin.",
  "Misollar: fotorezistor, termistor, potensiometr, mikrofon moduli.",
  "Plata uni ADC orqali raqamga aylantiradi.",
  "Afzalligi: oddiy, arzon, kutubxona kerak emas.",
  "Kamchiligi: shovqinga sezgir, kalibrlash kerak, uzun simda signal buziladi.",
 ]),
 ("Raqamli sensor", [
  "Ichida o'z mikrosxemasi bor: u o'lchaydi, hisoblaydi va TAYYOR raqam yuboradi.",
  "Misollar: DHT22, BMP280, MPU6050, DS18B20.",
  "Afzalligi: aniq, kalibrlangan, shovqinga chidamli, natija darhol foydali birlikda (gradus, foiz).",
  "Kamchiligi: qimmatroq, kutubxona kerak, o'qish tezligi cheklangan.",
  "Muhim: raqamli sensorni analogRead bilan o'qib bo'lmaydi — u ma'nosiz qiymat beradi.",
 ]),
 ("Qaysi holatda qaysi tur", [
  "Nisbiy qiymat yetarli bo'lsa (yorug' / qorong'i) — analog sensor arzonroq.",
  "Aniq son kerak bo'lsa (23,5 gradus) — raqamli sensor.",
  "Juda tez o'zgarishlarni ushlash kerak bo'lsa — analog (raqamlisi sekin bo'lishi mumkin).",
  "Uzun simda uzatish kerak bo'lsa — raqamli (analog signal yo'lda buziladi).",
 ]),
),

"Yorug'lik sensorli zanjir": D(
 ("Platasiz yorug'lik sensori", [
  "Fotorezistor va tranzistor bilan plataSIZ ham avtomatik chiroq yasash mumkin.",
  "Sxema: fotorezistor va rezistor bo'luvchi hosil qiladi, o'rta nuqta tranzistor bazasiga ulanadi.",
  "Qorong'ida fotorezistor qarshiligi ortadi, baza kuchlanishi o'zgaradi va tranzistor ochiladi.",
  "Tranzistor LEDni yoqadi.",
 ]),
 ("Sezgirlikni sozlash", [
  "Bo'luvchidagi doimiy rezistor o'rniga potensiometr qo'yilsa, chegarani qo'l bilan sozlash mumkin.",
  "Potensiometrni burab, chiroq qaysi yorug'likda yonishini tanlanadi.",
  "Kamchiligi: chegara atrofida chiroq titraydi (gisterezis yo'q).",
  "Buni tuzatish uchun teskari bog'lanish kerak — bu esa dasturiy yechimni (plata) afzal qilib qo'yadi.",
  "Aynan shu tajriba plata nima uchun kerakligini eng yaxshi tushuntiradi.",
 ]),
),

"Sensor + ijro qurilmasi: avtomat qurish": D(
 ("Avtomatik tizim tuzilishi", [
  "Har qanday avtomat uch qismdan iborat: SEZISH, QAROR, HARAKAT.",
  "Sezish — sensor (fotorezistor, termistor, tugma).",
  "Qaror — chegarani solishtirish (tranzistor yoki dastur).",
  "Harakat — ijro qurilmasi (LED, motor, zummer, rele).",
  "Bu tuzilma sovutgichdan tortib kosmik kemagacha hamma joyda bir xil.",
 ]),
 ("Platasiz va plata bilan", [
  "Platasiz avtomat: sensor -> tranzistor -> yuklama. Oddiy, arzon, lekin faqat bitta oddiy qoida bajaradi.",
  "Plata bilan: chegarani dasturda o'zgartirish, gisterezis qo'shish, bir necha sensorni birlashtirish, vaqt hisobga olish mumkin.",
  "Shuning uchun murakkab mantiq kerak bo'lsa plata afzal.",
  "Lekin oddiy vazifada platasiz yechim ishonchliroq: kamroq element, kamroq nosozlik nuqtasi.",
 ]),
),

"Ikki sensorli zanjir: birgalikda ishlash": D(
 ("Ikki sensorni birlashtirish mantiqi", [
  "VA mantiqi: ikkala shart ham bajarilsa harakat bo'ladi. Zanjirda bu KETMA-KET ulanish.",
  "YOKI mantiqi: bitta shart yetadi. Zanjirda bu PARALLEL ulanish.",
  "Misol (VA): chiroq faqat qorong'i BO'LSA VA harakat bo'lganda yonadi.",
  "Misol (YOKI): signal eshik ochilganda YOKI oyna ochilganda chiqadi.",
 ]),
 ("Amaliy yig'ish", [
  "VA uchun: ikki sensor kaliti ketma-ket ulanadi — ikkalasi ham ulansagina tok oqadi.",
  "YOKI uchun: ikki sensor kaliti parallel ulanadi — bittasi ulansa yetadi.",
  "Analog sensorlarda esa har biri o'z tranzistorini boshqaradi va ular ketma-ket/parallel ulanadi.",
  "Bu tajriba mantiqiy amallarni fizik zanjirda ko'rsatadi — dasturlashga o'tishda juda foydali.",
 ]),
),

"Ikki sensorli avtomat": D(
 ("Loyihalash tartibi", [
  "1) Qaysi ikki sensor ishlatilishini va ularning vazifasini yozing.",
  "2) Mantiqni aniqlang: VA yoki YOKI.",
  "3) Rostlik jadvalini to'ldiring: to'rt holat va har biriga natija.",
  "4) Sxemani chizing.",
  "5) Yig'ing va to'rt holatning hammasini sinab ko'ring.",
 ]),
 ("Sinov rejasi", [
  "Har bir sensorni alohida sinang: u yolg'iz ishlaydimi.",
  "Keyin to'rt kombinatsiyani ketma-ket sinang: 00, 01, 10, 11.",
  "Natijalarni rostlik jadvaliga yozing va kutilgan bilan solishtiring.",
  "Farq bo'lsa — mantiq noto'g'ri yig'ilgan (ketma-ket o'rniga parallel yoki aksincha).",
 ]),
),

"Haroratli signalizatsiya": D(
 ("Platasiz harorat signalizatsiyasi", [
  "Termistor va rezistor bo'luvchi hosil qiladi, o'rta nuqta tranzistor bazasiga ulanadi.",
  "Harorat oshsa termistor qarshiligi kamayadi, baza kuchlanishi o'zgaradi va tranzistor ochiladi.",
  "Tranzistor zummerni yoqadi.",
  "Chegarani sozlash uchun bo'luvchida potensiometr ishlatiladi.",
 ]),
 ("Kalibrlash", [
  "Termometr bilan yonma-yon qo'yib, potensiometrni burab kerakli haroratda ishga tushishini sozlang.",
  "Sinov: termistorni barmoq bilan isitib, signal chiqishini tekshiring.",
  "Sovutish uchun sovuq metall buyum tegizib ko'ring.",
  "Ishga tushish va o'chish harorati orasida farq bo'lishi kerak, aks holda signal titraydi.",
 ]),
),

"Tovush datchigi": D(
 ("Mikrofon moduli tuzilishi", [
  "Elektret mikrofon: ichida juda yupqa membrana bor, tovush uni tebratadi.",
  "Tebranish sig'imni o'zgartiradi va kichik o'zgaruvchan kuchlanish hosil bo'ladi.",
  "Signal juda kuchsiz (millivoltlarda), shuning uchun modulda kuchaytirgich bor.",
  "Modulda ikki chiqish: AO (analog, tovush kuchi) va DO (raqamli, chegaradan oshganda).",
  "Moduldagi potensiometr faqat DO chegarasini sozlaydi, AO ga ta'sir qilmaydi.",
 ]),
 ("Tovushni to'g'ri o'lchash", [
  "Bir marta o'qish YETARLI EMAS: tovush tebranish, tasodifan nol nuqtaga tushib qolish mumkin.",
  "To'g'ri usul: 50 ms davomida ko'p marta o'qib, eng katta va eng kichik qiymatni topish.",
  "Ularning farqi — tovush kuchi (tebranish kengligi).",
  "Tinch holatda AO da ~512 (o'rta nuqta) turadi va tovushda shu nuqta atrofida tebranadi.",
 ]),
),

}
