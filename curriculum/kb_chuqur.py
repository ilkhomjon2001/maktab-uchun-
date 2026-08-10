# -*- coding: utf-8 -*-
"""
NAZARIYANI CHUQURLASHTIRISH — 1-qism: elektronika asoslari.

kb_y*.py da har mavzu uchun 4 band nazariya bor. Komponentli darslarda
pasport.py qo'shimcha 13 band beradi, dasturlash darslarida esa kb_kod.py.
Qolgan mavzular (elektronika nazariyasi, AI tushunchalari, muhandislik
bosqichlari) uchun QO'SHIMCHA nazariya bloklari shu yerda.

Har bir yozuv: mavzu -> [(blok sarlavhasi, [bandlar]), ...]
Bu bloklar 5.2 dan KEYIN, savol blokidan OLDIN qo'shiladi.
"""


def D(*bloklar):
    return [(sarlavha, list(bandlar)) for sarlavha, bandlar in bloklar]


_ASOS = {

# ============================================================ OM QONUNI
"Tok, kuchlanish, qarshilik va Om qonuni": D(
 ("Uchta kattalik va ularning birliklari", [
  "Kuchlanish (U) — voltda (V) o'lchanadi. Bu zaryadni harakatlantiruvchi elektr bosimi. Suv quvurida bosimga o'xshaydi.",
  "Tok (I) — amperda (A) o'lchanadi. Bu bir sekundda kesim orqali o'tgan zaryad miqdori. Quvurdagi suv oqimiga o'xshaydi.",
  "Qarshilik (R) — omda (Om) o'lchanadi. Bu materialning tokga to'sqinligi. Quvurning torayishiga o'xshaydi.",
  "Kichik birliklar: 1 mA = 0,001 A; 1 mV = 0,001 V. Katta birliklar: 1 kOm = 1000 Om; 1 MOm = 1 000 000 Om.",
  "Arduino bilan ishlaganda ko'pincha milliamperlar bilan ish ko'riladi: LED 20 mA, plata pini maksimum 40 mA, USB porti 500 mA beradi.",
 ]),
 ("Formulani uch ko'rinishda ishlatish", [
  "Asosiy shakl: U = I x R — tok va qarshilik ma'lum bo'lsa kuchlanish topiladi.",
  "Ikkinchi shakl: I = U / R — kuchlanish va qarshilik ma'lum bo'lsa tok topiladi. Rezistor tanlashda eng ko'p ishlatiladigan shakl.",
  "Uchinchi shakl: R = U / I — kerakli tokni olish uchun qanday rezistor kerakligini topadi.",
  "Uchburchak usuli: yuqorida U, pastda I va R. Topilishi kerak bo'lgan harfni barmoq bilan yopsangiz, qolgan ikkitasi formulani ko'rsatadi.",
 ]),
 ("Ishlangan misollar", [
  "Misol 1: 9 V batareyaga 470 Om rezistor ulandi. I = 9 / 470 = 0,019 A = 19 mA.",
  "Misol 2: Zanjirda 12 mA tok oqmoqda, rezistor 220 Om. U = 0,012 x 220 = 2,64 V.",
  "Misol 3: 5 V manbadan LEDga 20 mA berish kerak. LEDda 2 V tushadi, demak rezistorda 3 V qoladi. R = 3 / 0,02 = 150 Om.",
  "Eng ko'p uchraydigan xato: mA ni A ga aylantirmaslik. 20 mA ni formulaga 20 deb qo'yish natijani 1000 marta noto'g'ri qiladi.",
 ]),
),

"Om qonuni va hisoblash": D(
 ("Formulaning uch shakli", [
  "U = I x R, I = U / R, R = U / I — uchtasi bir formulaning uch ko'rinishi.",
  "Qaysi shakl kerakligi savolga bog'liq: nomalum kattalik qaysi bo'lsa, o'sha chap tomonga chiqariladi.",
  "Birliklar doim asosiy shaklda bo'lishi kerak: volt, amper, om. Milliamperni amperga aylantirish uchun 1000 ga bo'linadi.",
 ]),
 ("Bog'liqlikning ma'nosi", [
  "Kuchlanish ikki barobar oshsa, qarshilik o'zgarmasa — tok ham ikki barobar oshadi. Bu to'g'ri proporsionallik.",
  "Qarshilik ikki barobar oshsa, kuchlanish o'zgarmasa — tok ikki barobar kamayadi. Bu teskari proporsionallik.",
  "Qarshilik nolga yaqinlashsa tok cheksiz ortishga intiladi — bu qisqa tutashuv va u xavfli holat.",
  "Shuning uchun LEDga rezistorsiz kuchlanish berish mumkin emas: LEDning o'z qarshiligi juda kichik va tok uni kuydiradi.",
 ]),
 ("Mashq qilish tartibi", [
  "Har bir masalada avval nima berilgani va nima topilishi kerakligi yozib olinadi.",
  "Keyin birliklar tekshiriladi va hammasi V, A, Om ga keltiriladi.",
  "Natija chiqqach, u mantiqan to'g'rimi degan savol beriladi: 5 V manbada 10 A tok chiqsa, demak xato bor.",
 ]),
),

"Om qonuni: mashqlar": D(
 ("Mashqlarni yechish tartibi", [
  "1-qadam: berilganlarni yozish va birliklarni asosiy shaklga keltirish (mA -> A, kOm -> Om).",
  "2-qadam: qaysi kattalik noma'lumligiga qarab formulaning kerakli shaklini tanlash.",
  "3-qadam: hisoblash va natijani baholash — javob mantiqiy oraliqdami.",
  "4-qadam: imkoni bo'lsa zanjirni yig'ib, multimetr bilan tekshirish. Hisob va o'lchov 10 % gacha farq qilishi normal (rezistor bardoshi).",
 ]),
 ("Namunaviy masalalar va javoblari", [
  "5 V manba, 1 kOm rezistor. Tok qancha? I = 5 / 1000 = 0,005 A = 5 mA.",
  "Tok 25 mA, kuchlanish 3 V. Qarshilik qancha? R = 3 / 0,025 = 120 Om.",
  "Rezistor 330 Om, undan 15 mA tok oqmoqda. Undagi kuchlanish? U = 0,015 x 330 = 4,95 V.",
  "9 V manbaga qaysi rezistor ulansa 10 mA tok oqadi? R = 9 / 0,01 = 900 Om, amalda 1 kOm olinadi.",
  "Teskari masala: 220 Om rezistorga 5 V berilsa nima bo'ladi? I = 5/220 = 22,7 mA — bu LED uchun me'yorga yaqin.",
 ]),
),

"Om qonuni va quvvat: takrorlash": D(
 ("Quvvat formulasi va uning uch shakli", [
  "P = U x I — quvvat vattda (Vt) o'lchanadi. Bu vaqt birligida sarflanadigan energiya.",
  "Om qonunini qo'yib boshqa shakllar chiqadi: P = I2 x R va P = U2 / R.",
  "Ikkinchi shakl muhim: tok ikki barobar oshsa, quvvat TO'RT barobar oshadi. Shuning uchun ortiqcha tok tez qizdiradi.",
 ]),
 ("Rezistorning quvvat bardoshi", [
  "Maktab to'plamidagi rezistorlar odatda 0,25 Vt ga mo'ljallangan.",
  "Misol: 220 Om rezistordan 20 mA tok o'tsa, P = 0,02^2 x 220 = 0,088 Vt — bu 0,25 Vt dan ancha kam, xavfsiz.",
  "Agar shu rezistorga 5 V to'g'ridan-to'g'ri berilsa: P = 25 / 220 = 0,11 Vt — hali ham normal.",
  "Lekin 10 Om rezistorga 5 V berilsa: P = 25 / 10 = 2,5 Vt — bu bardoshdan 10 barobar ko'p, rezistor qizib kuyadi.",
  "Amaliy qoida: rezistor barmoq bilan ushlab bo'lmaydigan darajada qizisa, quvvat bardoshi yetmayapti.",
 ]),
),

"Elektr quvvati: P = U x I": D(
 ("Quvvat nima va nima uchun kerak", [
  "Quvvat — energiyaning sarflanish TEZLIGI. 100 Vt lampa 1 sekundda 100 joul energiya sarflaydi.",
  "P = U x I: kuchlanish 5 V, tok 2 A bo'lsa quvvat 10 Vt.",
  "Quvvat oxir-oqibat ISSIQLIKKA aylanadi (yoki yorug'lik, harakatga). Shuning uchun ko'p quvvat sarflaydigan element qiziydi.",
 ]),
 ("Amaliy hisoblar", [
  "Arduino Uno USB dan 500 mA gacha oladi: P = 5 x 0,5 = 2,5 Vt.",
  "Servo motor harakatda 250 mA tortadi: P = 5 x 0,25 = 1,25 Vt — bu USB quvvatining yarmi.",
  "Uchta servo bir vaqtda ishlasa 750 mA kerak — USB yetmaydi va plata qayta yuklanadi. Yechim: alohida quvvat manbai.",
  "Uy jihozlari: choynak 2000 Vt, muzlatgich 150 Vt, LED lampa 10 Vt, telefon zaryadlagichi 10 Vt.",
 ]),
),

"Energiya va iste'mol: kilovatt-soat": D(
 ("Quvvat va energiya farqi", [
  "Quvvat (Vt) — TEZLIK. Energiya (Vt x soat) — jami SARF. Bu tezlik va bosib o'tilgan yo'l kabi farq qiladi.",
  "1 kVt x soat = 1000 vattlik jihozning 1 soat ishlashi.",
  "Hisoblash: energiya (kVt x s) = quvvat (Vt) x vaqt (soat) / 1000.",
 ]),
 ("Kundalik misollar", [
  "2000 Vt choynak har kuni 15 daqiqa ishlasa: 2000 x 0,25 / 1000 = 0,5 kVt x s kuniga, oyiga 15 kVt x s.",
  "10 Vt LED lampa kuniga 6 soat: 10 x 6 / 1000 = 0,06 kVt x s kuniga, oyiga 1,8 kVt x s.",
  "Xuddi shu vazifani bajaradigan 100 Vt cho'g'lanma lampa oyiga 18 kVt x s sarflaydi — o'n barobar ko'p.",
  "Xulosa: LED lampaga o'tish yoritishga ketadigan to'lovni o'n barobar kamaytiradi. Bu hisob-kitob AI va IoT loyihalarida ham kerak bo'ladi.",
 ]),
),

# ============================================================ ZANJIR TURLARI
"Ketma-ket va parallel ulanish": D(
 ("Ketma-ket ulanish qonuniyatlari", [
  "Tok hamma element orqali BIR XIL oqadi: I = I1 = I2 = I3.",
  "Kuchlanish elementlar orasida BO'LINADI: U = U1 + U2 + U3.",
  "Qarshiliklar QO'SHILADI: R = R1 + R2 + R3.",
  "Bitta element uzilsa — butun zanjir o'chadi. Eski yangi yil gulchambari shu prinsipda ishlagan va bitta lampa kuysa hammasi o'chgan.",
 ]),
 ("Parallel ulanish qonuniyatlari", [
  "Kuchlanish hamma shoxda BIR XIL: U = U1 = U2 = U3.",
  "Tok shoxlar orasida BO'LINADI: I = I1 + I2 + I3.",
  "Umumiy qarshilik teskari yig'indi orqali topiladi: 1/R = 1/R1 + 1/R2. Ikki bir xil rezistor uchun natija yarmiga teng.",
  "Umumiy qarshilik doim eng KICHIK rezistordan ham kichik chiqadi — bu boshda g'alati tuyuladi, lekin tokga qo'shimcha yo'l ochilgani uchun shunday.",
  "Bitta shox uzilsa qolganlari ishlayveradi. Uydagi rozetkalar aynan shuning uchun parallel ulanadi.",
 ]),
),

"Parallel ulanish qonuniyatlari": D(
 ("Formulalar va hisob", [
  "Ikki rezistor uchun qulay shakl: R = (R1 x R2) / (R1 + R2).",
  "Misol: 1 kOm va 1 kOm parallel -> R = 1000000 / 2000 = 500 Om.",
  "Misol: 1 kOm va 2 kOm parallel -> R = 2000000 / 3000 = 667 Om.",
  "Uch bir xil rezistor parallel bo'lsa umumiy qarshilik uchdan biriga teng bo'ladi.",
 ]),
 ("Nima uchun bu muhim", [
  "Ikki LEDni parallel ulasangiz har biriga alohida rezistor kerak — aks holda ular kuchlanish farqi tufayli teng bo'lmagan yorug'lik beradi.",
  "Parallel ulanishda umumiy tok ortadi: 20 mA li ikki LED birga 40 mA tortadi, plata pini chegarasi esa 40 mA.",
  "Uydagi bir rozetkaga ko'p jihoz ulansa tok yig'iladi va sim qiziydi — bu yong'inning eng ko'p uchraydigan sababi.",
 ]),
),

"Parallel zanjirda tok qanday taqsimlanadi": D(
 ("Tok taqsimlanish qoidasi", [
  "Har bir shoxdagi tok o'sha shoxning qarshiligiga TESKARI proporsional: qarshilik kichik bo'lsa tok ko'p oqadi.",
  "Formula: I1 = U / R1, I2 = U / R2. Kuchlanish ikkalasida bir xil bo'lgani uchun hisob oson.",
  "Misol: 5 V manba, shoxlar 100 Om va 500 Om. I1 = 50 mA, I2 = 10 mA. Umumiy tok 60 mA.",
  "Ya'ni tok doim eng oson yo'ldan ko'proq oqadi — xuddi suv keng quvurdan ko'proq oqqani kabi.",
 ]),
 ("Qisqa tutashuv nima uchun xavfli", [
  "Qisqa tutashuv — bu qarshiligi deyarli nolga teng parallel shox.",
  "Om qonuni bo'yicha shu shoxdagi tok juda katta bo'ladi va butun tok o'sha yo'ldan oqadi.",
  "Natijada sim qiziydi, batareya tez bo'shaydi yoki qiziydi, plata shikastlanadi.",
  "Shuning uchun zanjirni yig'ishdan oldin sim uchlarining tegib turmaganini ko'z bilan tekshirish odat bo'lishi kerak.",
 ]),
),

"Ketma-ket, parallel va kuchlanish bo'luvchi": D(
 ("Kuchlanish bo'luvchining ishlashi", [
  "Ikki rezistor ketma-ket ulansa, ular orasidagi nuqtadan manba kuchlanishining bir qismi olinadi.",
  "Formula: Uchiqish = Ukirish x R2 / (R1 + R2), bu yerda R2 — pastki (GND tomondagi) rezistor.",
  "Misol: 5 V, R1 = 1 kOm, R2 = 1 kOm -> chiqishda 2,5 V, ya'ni yarmi.",
  "Misol: 5 V, R1 = 1 kOm, R2 = 2 kOm -> chiqishda 3,33 V. Aynan shu nisbat 5 V ni ESP32 uchun 3,3 V ga tushirishda ishlatiladi.",
 ]),
 ("Bo'luvchining chegarasi", [
  "Bo'luvchi faqat O'LCHOV signali uchun. Undan quvvat olish mumkin emas: yuklama ulansa chiqish kuchlanishi tushib ketadi.",
  "Sabab: yuklama R2 ga parallel bo'ladi va umumiy qarshilikni kamaytiradi.",
  "Shuning uchun motor yoki servoni bo'luvchidan quvvatlash mumkin emas — buning uchun stabilizator kerak.",
  "Fotorezistor va termistor sxemasi ham bo'luvchi: pastki rezistor doimiy, yuqorigisi esa sensorning o'zgaruvchan qarshiligi.",
 ]),
),

"Zanjir, tok, kuchlanish: takrorlash": D(
 ("Uch tushunchani bir sxemada ko'rish", [
  "Yopiq zanjir — tok aylanib yuradigan uzluksiz yo'l. Yo'l uzilsa tok to'xtaydi.",
  "Kuchlanish manbada hosil bo'ladi va zanjir bo'ylab elementlarda TAQSIMLANADI.",
  "Tok esa butun ketma-ket zanjirda bir xil bo'ladi — u yo'lda 'sarflanmaydi', faqat energiya sarflanadi.",
  "Ko'p uchraydigan noto'g'ri tasavvur: 'tok LEDda tugaydi'. Aslida LEDdan chiqqan tok manbaga qaytadi, faqat energiyasining bir qismini yorug'likka bergan bo'ladi.",
 ]),
 ("Multimetr bilan tekshirish tartibi", [
  "Kuchlanish PARALLEL o'lchanadi: shchuplar element ikki uchiga tegiziladi, zanjir uzilmaydi.",
  "Tok KETMA-KET o'lchanadi: zanjir uziladi va multimetr shu uzilgan joyga qo'yiladi.",
  "Qarshilik faqat KUCHLANISHSIZ zanjirda o'lchanadi, element esa zanjirdan chiqarib olinadi.",
  "Eng ko'p uchraydigan xato: tok rejimidagi multimetrni batareyaga parallel ulash. Bu qisqa tutashuv bo'ladi va asbob predoxraniteli kuyadi.",
 ]),
),

# ============================================================ KOMPONENTLAR
"Kondensator va vaqt": D(
 ("Kondensator nima qiladi", [
  "Kondensator ichida ikki metall plastina va ular orasida izolyator bor. U zaryadni VAQTINCHA to'playdi.",
  "Sig'imi faradda (F) o'lchanadi, lekin farad juda katta birlik. Amalda mikrofarad (mkF), nanofarad (nF) va pikofarad (pF) ishlatiladi.",
  "1 mkF = 0,000001 F. Maktab to'plamlarida 100 nF, 10 mkF va 100 mkF ko'p uchraydi.",
  "Elektrolit kondensatorda QUTB bor: uzun oyoq plyus, korpusdagi chiziq minusni ko'rsatadi. Teskari ulansa shishib yorilishi mumkin.",
  "Keramik kondensatorda qutb yo'q, istalgan tomonga ulanadi.",
 ]),
 ("Zaryadlanish va bo'shash vaqti", [
  "Kondensator bir zumda to'lmaydi: rezistor orqali ulansa u ASTA-SEKIN zaryadlanadi.",
  "Vaqt doimiysi: t = R x C. Bu vaqtda kondensator to'liq kuchlanishning 63 % iga yetadi.",
  "To'liq zaryadlanish taxminan 5 x t vaqt oladi.",
  "Misol: R = 10 kOm, C = 100 mkF -> t = 10000 x 0,0001 = 1 sekund. To'lishi ~5 sekund.",
  "Shu tufayli kondensator vaqt hosil qiluvchi element sifatida ishlatiladi: kechikish, filtr, taymer.",
 ]),
 ("Amalda qayerda ishlatiladi", [
  "Quvvat liniyasidagi silliqlash: motor ishga tushganda kuchlanish cho'kadi, kondensator shu lahzada zaxira zaryadni beradi va plata qayta yuklanmaydi.",
  "Shuning uchun servo yoki motor bilan ishlaganda quvvat liniyasiga 100-470 mkF kondensator qo'yiladi.",
  "Shovqin filtri: mikrosxema oyoqlari yoniga 100 nF kondensator qo'yilsa yuqori chastotali xalaqit yo'qoladi.",
 ]),
),

"Kondensator va RC zanjir": D(
 ("RC zanjir tuzilishi", [
  "RC zanjir — ketma-ket ulangan rezistor va kondensator. Eng oddiy vaqt hosil qiluvchi sxema.",
  "Zaryadlanish egri chizig'i: boshida tez ko'tariladi, keyin sekinlashadi va asta to'liq kuchlanishga yaqinlashadi.",
  "Bo'shash ham xuddi shunday: boshida tez tushadi, keyin sekinlashadi.",
  "Vaqt doimiysi t = R x C zanjirning 'tezligini' belgilaydi.",
 ]),
 ("Hisob va o'lchov", [
  "t vaqtdan keyin kuchlanish 63 %; 2t da 86 %; 3t da 95 %; 5t da amalda 100 % deb qabul qilinadi.",
  "Misol: 100 kOm va 10 mkF -> t = 100000 x 0,00001 = 1 sekund.",
  "Multimetr bilan kuzatish: kondensatorga parallel ulanib, zaryadlanish paytida raqamlar qanday sekinlashib borishini ko'rish mumkin.",
  "Arduino bilan aniqroq: analogRead bilan har 10 ms da o'lchab, qiymatlarni Serial Plotter'da grafik qilib chizish.",
 ]),
),

"RC zanjir va vaqt doimiysi": D(
 ("Vaqt doimiysining ma'nosi", [
  "t = R x C formulasida R omda, C faradda bo'lsa natija sekundda chiqadi.",
  "Qarshilik oshsa vaqt uzayadi (tok kam oqadi, kondensator sekin to'ladi).",
  "Sig'im oshsa ham vaqt uzayadi (to'ldirish kerak bo'lgan zaryad ko'p).",
  "Ikkalasini o'zgartirib, kerakli kechikishni olish mumkin — bu taymer sxemalarining asosi.",
 ]),
 ("Amaliy qo'llanishlar", [
  "Tugma sakrashini (bounce) apparat yo'li bilan yo'qotish: tugmaga parallel 100 nF kondensator qo'yiladi.",
  "Sekin yonadigan chiroq: LED zanjiriga RC qo'shilsa yorug'lik asta ko'tariladi.",
  "Signal filtri: yuqori chastotali shovqin kondensator orqali GND ga o'tib ketadi va foydali sekin signal qoladi.",
  "Dasturiy o'xshashi — eksponensial silliqlash: yangi = a x o'lchov + (1-a) x eski. Bu RC filtrning kodda yozilgan varianti.",
 ]),
),

"NPN va PNP tranzistorlar farqi": D(
 ("Ikki turning ishlash farqi", [
  "NPN tranzistor bazaga MUSBAT signal berilganda ochiladi. U yuklamaning GND tomoniga qo'yiladi (past tomon kaliti).",
  "PNP tranzistor bazaga MANFIY (past) signal berilganda ochiladi. U yuklamaning plyus tomoniga qo'yiladi (yuqori tomon kaliti).",
  "Maktab loyihalarida deyarli doim NPN ishlatiladi: uni Arduino bilan boshqarish osonroq va mantiq to'g'ridan-to'g'ri.",
  "Keng tarqalgan turlar: NPN — BC547, 2N2222, S8050. PNP — BC557, 2N2907, S8550.",
 ]),
 ("Uch oyoq va ularning vazifasi", [
  "Baza (B) — boshqaruv oyog'i. Unga kichik tok (1-2 mA) beriladi va u albatta rezistor orqali ulanadi (odatda 1 kOm).",
  "Kollektor (C) — yuklama ulanadigan oyoq.",
  "Emitter (E) — NPN da GND ga, PNP da plyusga ulanadi.",
  "Kuchaytirish koeffitsienti (hFE): 100 bo'lsa, bazadagi 1 mA kollektorda 100 mA gacha tokni o'tkazadi.",
  "Oyoqlar tartibi korpusga qarab farq qiladi — datasheetga qarash yoki multimetrning tranzistor rejimida tekshirish kerak.",
 ]),
 ("Nima uchun tranzistor kerak", [
  "Arduino pini 40 mA beradi, motor esa 300 mA tortadi. Tranzistor kichik boshqaruv toki bilan katta tokni o'tkazadi.",
  "Ya'ni tranzistor — bu elektron kalit: qo'l bilan bosiladigan tugmaning o'rniga dastur boshqaradigan tugma.",
  "Induktiv yuklama (motor, rele) bilan ishlaganda tranzistorga parallel himoya diodi SHART, aks holda teskari kuchlanish uni teshadi.",
 ]),
),

"Kondensator, diod, tranzistor": D(
 ("Uch komponentning vazifasi", [
  "Kondensator — zaryadni vaqtincha to'playdi. Vazifasi: quvvatni silliqlash, shovqinni yo'qotish, vaqt hosil qilish.",
  "Diod — tokni faqat bir tomonga o'tkazadi. Vazifasi: himoya, to'g'rilash, teskari ulanishdan saqlash.",
  "Tranzistor — kichik tok bilan katta tokni boshqaradi. Vazifasi: kalit yoki kuchaytirgich.",
 ]),
 ("Diodning muhim xususiyatlari", [
  "Diodda to'g'ri yo'nalishda 0,7 V atrofida kuchlanish tushadi (kremniy diod uchun).",
  "Korpusdagi halqa KATOD (minus) tomonini ko'rsatadi.",
  "Himoya diodi motor yoki relega PARALLEL va TESKARI qutblab ulanadi: katod plyusga qaraydi.",
  "Nima uchun: g'altakdan tok to'satdan uzilsa, u o'zida yuz voltli teskari kuchlanish hosil qiladi. Diod bu kuchlanishga yo'l ochib beradi va tranzistorni saqlaydi.",
  "Keng tarqalgan turlar: 1N4007 (quvvat uchun), 1N4148 (signal uchun), Shottki diodlar (tez va kam tushishli).",
 ]),
),

"Yarimo'tkazgich nima va nega u elektronikani o'zgartirdi": D(
 ("O'tkazgich, izolyator va yarimo'tkazgich", [
  "O'tkazgich (mis, alyuminiy) tokni yaxshi o'tkazadi: ichida erkin elektronlar juda ko'p.",
  "Izolyator (rezina, shisha, plastmassa) o'tkazmaydi: elektronlar atomga mahkam bog'langan.",
  "Yarimo'tkazgich (kremniy, germaniy) o'rtada turadi va eng muhimi — SHAROITGA QARAB o'zgaradi.",
  "Uni harorat, yorug'lik yoki tashqi kuchlanish bilan o'tkazuvchan yoki o'tkazmaydigan holatga keltirish mumkin. Mana shu boshqariluvchanlik butun zamonaviy elektronikaning asosi.",
 ]),
 ("Legirlash va p-n o'tish", [
  "Toza kremniyga boshqa element atomlari qo'shiladi — bu legirlash deb ataladi.",
  "Ortiqcha elektron beruvchi qo'shimcha n-tur materialni hosil qiladi, elektron yetishmovchiligi esa p-tur materialni.",
  "Ikki turning tutashgan joyi p-n o'tish deyiladi va u tokni faqat bir tomonga o'tkazadi. Diod aynan shu.",
  "Uch qatlam qo'yilsa tranzistor chiqadi: o'rtadagi yupqa qatlam kalit vazifasini bajaradi.",
 ]),
 ("Nima uchun bu inqilob bo'ldi", [
  "Yarimo'tkazgichdan oldin xuddi shu ishni elektron lampalar bajargan: ular lampochkadek katta bo'lgan, qizigan va tez kuygan.",
  "Birinchi kompyuterlar shuning uchun butun xonani egallagan va kunlab ishlab, keyin lampalarini almashtirishga to'xtagan.",
  "Tranzistor kichik, sovuq va uzoq ishlaydi. Bugun bitta protsessorga milliardlab tranzistor sig'adi.",
  "Sizning qo'lingizdagi Arduino platasi 1960-yillardagi butun bir xonalik kompyuterdan kuchliroq.",
 ]),
),

# ============================================================ O'LCHOV
"Multimetr bilan o'lchashni eslash": D(
 ("Uch rejim va ularning ulanishi", [
  "Kuchlanish (V) — PARALLEL ulanadi, zanjir uzilmaydi. Qora shchup GND ga, qizil o'lchanadigan nuqtaga.",
  "Tok (A) — KETMA-KET ulanadi, zanjir uziladi va multimetr shu joyga qo'yiladi. Shchup uyasi ham almashtiriladi.",
  "Qarshilik (Om) — faqat KUCHLANISHSIZ zanjirda, element esa zanjirdan chiqarib olinadi.",
  "Uzilishni tekshirish (signalli rejim) — sim butunligini tekshirishning eng tez usuli: ulangan bo'lsa asbob signal beradi.",
 ]),
 ("O'lchash madaniyati", [
  "Avval oraliqni katta qilib qo'yib, keyin kichraytirish kerak — noma'lum kuchlanishni kichik oraliqda o'lchash asbobni shikastlaydi.",
  "Har o'lchovdan oldin shchup qaysi uyada turganini tekshirish odat bo'lishi kerak: tok uyasida qolgan shchup bilan kuchlanish o'lchash — qisqa tutashuv.",
  "Natija yozib olinadi: qaysi nuqta, qanday rejim, qanday qiymat. Yozilmagan o'lchov keyin ishga yaramaydi.",
  "Hisob va o'lchov 5-10 % farq qilishi normal: rezistorda 5 % bardosh bor, batareya kuchlanishi ham nominaldan farq qiladi.",
 ]),
),

"Multimetr bilan o'lchash amaliyoti": D(
 ("O'lchash bosqichlari", [
  "1) Zanjirni yig'ing va ko'z bilan tekshiring: qisqa tutashuv yo'qmi, qutblar to'g'rimi.",
  "2) Manba kuchlanishini o'lchang — u kutilgan qiymatga yaqinmi.",
  "3) Har bir elementdagi kuchlanish tushishini alohida o'lchang.",
  "4) Zanjirni uzib, tokni o'lchang.",
  "5) Natijalarni jadvalga yozing va Om qonuni bo'yicha hisoblangan qiymat bilan solishtiring.",
 ]),
 ("Kutilgan natijalar", [
  "Ketma-ket zanjirda barcha kuchlanish tushishlari yig'indisi manba kuchlanishiga TENG bo'lishi kerak (Kirxgof qonuni).",
  "Agar yig'indi manbadan kam chiqsa — o'lchamagan element bor yoki kontakt yomon.",
  "Parallel zanjirda shoxlardagi toklar yig'indisi umumiy tokka teng bo'ladi.",
  "LEDdagi kuchlanish tushishi doim 2 V atrofida qoladi — rezistorni o'zgartirsangiz ham u deyarli o'zgarmaydi. Bu diodning xususiyati.",
 ]),
),

"Sensorni kalibrlash": D(
 ("Kalibrlash nima va nima uchun kerak", [
  "Sensor xom qiymat beradi (masalan 0 dan 1023 gacha son). Bu son o'z-o'zicha gradus yoki foizni anglatmaydi.",
  "Kalibrlash — xom qiymatni HAQIQIY o'lchov birligiga bog'lash jarayoni.",
  "Har bir nusxa biroz boshqacha: bir xil ikki fotorezistor bir xil yorug'likda 30-50 birlik farq qilishi mumkin.",
  "Shuning uchun internetdan olingan tayyor koeffitsient odatda ishlamaydi — uni har bir sensor uchun o'zingiz topasiz.",
 ]),
 ("Ikki nuqtali kalibrlash tartibi", [
  "1) Sensorni ma'lum PAST holatga qo'ying (masalan termistorni muzli suvga — 0 daraja) va xom qiymatni yozing.",
  "2) Ma'lum BALAND holatga qo'ying (iliq suv, termometr bilan o'lchangan) va xom qiymatni yozing.",
  "3) Ikki nuqta orasidagi chiziqni chizing: map(xom, xomPast, xomBaland, haqPast, haqBaland).",
  "4) Uchinchi, O'RTA nuqtada tekshiring — bu kalibrlash to'g'ri chiqqanini isbotlaydi.",
  "Agar uchinchi nuqtada xato katta bo'lsa, sensor CHIZIQSIZ demakdir va ko'proq nuqta yoki formula kerak bo'ladi.",
 ]),
),

"Sensorli qurilmani sozlash (kalibrlash)": D(
 ("Chegarani to'g'ri tanlash", [
  "Chegara — qurilma qaror qabul qiladigan qiymat. U tajriba yo'li bilan topiladi, taxmin bilan emas.",
  "Tartib: sensorni haqiqiy ish sharoitida qo'yib, qiymatni bir necha daqiqa kuzating va eng past hamda eng baland qiymatni yozib oling.",
  "Chegara shu ikki qiymat oralig'ida, lekin chetlaridan uzoqroqda tanlanadi.",
  "Muhit o'zgarsa (kun/tun, yoz/qish) chegarani qayta tekshirish kerak.",
 ]),
 ("Gisterezis — titrashni yo'qotish", [
  "Bitta chegara ishlatilsa, qiymat chegara atrofida turganda qurilma tez-tez yoqilib-o'chib turadi.",
  "Yechim: IKKI chegara qo'yish. Masalan 350 dan past bo'lsa yoq, 450 dan yuqori bo'lsa o'chir.",
  "Ikki chegara orasidagi oraliqda qurilma o'z holatini SAQLAYDI va hech narsa o'zgarmaydi.",
  "Bu usul konditsioner, muzlatgich va termostatlarning hammasida ishlatiladi.",
 ]),
),

"Sensorlarni kalibrlash va aniqlik": D(
 ("Aniqlik, qadam va takrorlanuvchanlik", [
  "Aniqlik (accuracy) — ko'rsatkich haqiqiy qiymatga qanchalik yaqin. DHT22 uchun bu +-0,5 daraja.",
  "Qadam (rezolyutsiya) — sensor sezadigan eng kichik o'zgarish. DHT22 uchun 0,1 daraja.",
  "Takrorlanuvchanlik — bir xil sharoitda qayta o'lchaganda bir xil natija chiqishi.",
  "Bu uchtasi boshqa-boshqa narsa: sensor 0,1 daraja qadam bilan ko'rsatishi, lekin 2 daraja xato qilishi mumkin.",
 ]),
 ("Xatoni kamaytirish usullari", [
  "O'rtachalash: bitta o'lchov o'rniga 10-32 ta o'lchov olib, o'rtachasini hisoblash tasodifiy shovqinni sezilarli kamaytiradi.",
  "Isinishni kutish: ko'p sensorlar yoqilgandan keyin barqarorlashishi uchun vaqt talab qiladi (PIR 40 sekund, MQ-2 bir necha daqiqa).",
  "Etalon bilan solishtirish: uy termometri yoki multimetr kabi ishonchli asbob bilan yonma-yon o'lchash.",
  "Sharoitni hisobga olish: quyosh nuri, isitgich oqimi va vibratsiya ko'rsatkichni buzadi.",
 ]),
),

"Analog va raqamli signal": D(
 ("Ikki turdagi signal", [
  "Analog signal UZLUKSIZ o'zgaradi va oraliqdagi istalgan qiymatni olishi mumkin: 0 V, 1,37 V, 2,84 V.",
  "Raqamli signal faqat IKKI holatga ega: past (0) yoki yuqori (1). Oraliq qiymat yo'q.",
  "Tabiatdagi hamma narsa analog: harorat, tovush, yorug'lik. Kompyuter esa faqat raqamlar bilan ishlaydi.",
  "Shuning uchun har bir sensorli tizimda analogdan raqamliga aylantirish bosqichi bo'ladi.",
 ]),
 ("ADC — aylantirish qanday boradi", [
  "ADC kirish kuchlanishini o'lchab, uni butun songa aylantiradi.",
  "Arduino Uno da ADC 10 bitli: 0-5 V oralig'i 1024 pog'onaga bo'linadi. Bir pog'ona 5/1024 = 4,9 mV.",
  "ESP32 da ADC 12 bitli: 4096 pog'ona, kirish esa 0-3,3 V.",
  "Ya'ni ADC har doim yaxlitlaydi: 2,4405 V ham, 2,4430 V ham bir xil songa aylanishi mumkin. Bu aylantirish xatosi va undan qochib bo'lmaydi.",
  "Ko'proq bit — aniqroq aylantirish, lekin sekinroq va qimmatroq.",
 ]),
),

"Analog va raqamli dunyo o'rtasidagi farq": D(
 ("Nima uchun aylantirish kerak", [
  "Dunyodagi kattaliklar uzluksiz o'zgaradi, mikrokontroller esa faqat 0 va 1 bilan ishlaydi.",
  "Sensor fizik kattalikni ANALOG elektr signalga aylantiradi, ADC esa uni RAQAMGA aylantiradi.",
  "Teskari yo'nalish ham bor: DAC raqamni analog kuchlanishga aylantiradi (tovush chiqarishda ishlatiladi).",
  "PWM esa uchinchi yo'l: haqiqiy analog emas, lekin tez yoqib-o'chirish orqali analog ta'sirini beradi.",
 ]),
 ("Raqamli signalning afzalligi", [
  "Analog signal uzun simda susayadi va shovqin qo'shiladi — asl qiymatni tiklab bo'lmaydi.",
  "Raqamli signalda esa faqat 0 va 1 ni ajratish kerak, shuning uchun shovqin bo'lsa ham qiymat aynan tiklanadi.",
  "Shu sababli DHT22 kabi zamonaviy sensorlar o'lchashni O'ZI bajaradi va natijani tayyor raqam sifatida uzatadi.",
  "Musiqa, foto va video ham xuddi shu sababdan raqamli formatga o'tgan: nusxa ko'chirilganda sifat yo'qolmaydi.",
 ]),
),

"Quvvat manbalari va xavfsizlik": D(
 ("Manbalar va ularning imkoniyati", [
  "USB porti: 5 V, 500 mA (USB 2.0). Arduino va bir necha LED uchun yetadi, motorlar uchun yetmaydi.",
  "Kron batareya (9 V): sig'imi juda kam (500 mAh), motor yoki servo uchun mos emas. Faqat oz tok tortadigan sxemalar uchun.",
  "AA batareya bloki (4 x 1,5 V = 6 V): sig'imi 2000 mAh, motorlar uchun mos.",
  "Li-ion akkumulyator (3,7 V): sig'imi katta, qayta zaryadlanadi, lekin himoya sxemasi bo'lishi shart.",
  "Adapter (12 V, 2 A): eng barqaror manba, lekin qurilma ko'chma bo'lmaydi.",
 ]),
 ("Xavfsizlik qoidalari", [
  "220 V bilan ishlash faqat o'qituvchi nazoratida va faqat namoyish tarzida bo'ladi. O'quvchilar 220 V ga tegmaydi.",
  "Qutbni almashtirmaslik: plyus va minusni teskari ulash ko'p modullarni bir zumda ishdan chiqaradi.",
  "Zanjirni faqat KUCHLANISHSIZ holatda o'zgartirish: avval quvvatni uzish, keyin sim ulash.",
  "Umumiy GND qoidasi: tashqi manba ishlatilsa, uning GND si albatta plata GND si bilan birlashtiriladi.",
  "Qizigan komponentni ushlamaslik: rezistor va stabilizator 80 darajagacha qizishi mumkin.",
 ]),
),

"Kodni saqlash va tartibga solish": D(
 ("Ish faylini tartibda saqlash", [
  "Har bir loyihaga alohida papka: sketch, sxema rasmi va qisqa izoh bir joyda tursin.",
  "Fayl nomi ma'noli bo'lsin: 'tungi_chiroq_v2' — 'sketch_apr12a' emas.",
  "Ishlaydigan variant topilgach, uni nusxalab saqlab qo'yish kerak. Keyingi o'zgartirish buzsa, qaytish joyi bo'ladi.",
  "Versiyani nomga qo'shish eng oddiy usul: v1, v2, v3. Har birida nima o'zgargani izohda yoziladi.",
 ]),
 ("Ish daftari (logbook)", [
  "Har darsda yoziladi: sana, mavzu, nima yig'ildi, qanday natija chiqdi, qanday xato bo'ldi va u qanday tuzatildi.",
  "Xato yozilishi natijadan ham muhimroq: bir marta uchragan xato ikkinchi marta tez topiladi.",
  "O'lchov qiymatlari ham yoziladi — kalibrlash uchun ular keyin kerak bo'ladi.",
  "Chorak oxirida daftar loyihani hujjatlashtirish uchun tayyor manba bo'ladi.",
 ]),
),

}


# 2-qism (AI va muhandislik) alohida faylda — bu fayl juda kattalashib
# ketmasligi uchun. Ikkalasi shu yerda birlashtiriladi.
from kb_chuqur2 import CHUQUR2 as _AI
from kb_chuqur3 import CHUQUR3 as _MUH, KIRISH_YO
from kb_chuqur4 import CHUQUR4 as _ELEK
from kb_chuqur5 import CHUQUR5 as _ZANJIR
from kb_chuqur6 import CHUQUR6 as _QOLGAN

CHUQUR = dict(_ASOS)
for _manba in (_AI, _MUH, _ELEK, _ZANJIR, _QOLGAN):
    for _k, _v in _manba.items():
        if _k in CHUQUR:
            raise ValueError("kb_chuqur: kalit ikki faylda takrorlangan: " + _k)
        CHUQUR[_k] = _v


if __name__ == "__main__":
    print("chuqurlashtirilgan mavzu:", len(CHUQUR))
    print("qo'shimcha blok:", sum(len(v) for v in CHUQUR.values()))
    print("qo'shimcha band:", sum(len(b) for v in CHUQUR.values() for _, b in v))
    print("kirish yo'nalishlari:", len(KIRISH_YO),
          "| band:", sum(len(b) for v in KIRISH_YO.values() for _, b in v))
