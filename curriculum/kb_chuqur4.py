# -*- coding: utf-8 -*-
"""
NAZARIYANI CHUQURLASHTIRISH — 4-qism: elektronika asoslari (5-6-sinf, platasiz).

Bu darslarda plata ishlatilmaydi, shuning uchun pasport.py ham, kb_kod.py ham
ularga qo'shimcha bermaydi. Ayni paytda aynan shu darslar butun kursning
poydevori — nazariya eng chuqur bo'lishi kerak bo'lgan joy shu yer.

Tuzilishi kb_chuqur.py bilan bir xil.
"""


def D(*bloklar):
    return [(sarlavha, list(bandlar)) for sarlavha, bandlar in bloklar]


CHUQUR4 = {

# ============================================================ ELEKTR ASOSLARI
"Elektr toki nima: zaryadning harakati": D(
 ("Zaryad va uning harakati", [
  "Har bir atomda musbat zaryadli yadro va uning atrofida manfiy zaryadli elektronlar bor.",
  "Metallarda tashqi elektronlar o'z atomiga mahkam bog'lanmagan — ular kristall panjara bo'ylab erkin ko'chib yuradi.",
  "Tok — mana shu erkin elektronlarning TARTIBLI, bir tomonga yo'naltirilgan harakati.",
  "Tokning yo'qligida ham elektronlar harakatlanadi, lekin tartibsiz: har biri o'z tomoniga. Umumiy natija nolga teng.",
  "Kuchlanish qo'llanilganda esa bu tartibsiz harakat ustiga umumiy yo'nalish qo'shiladi va zanjirda tok paydo bo'ladi.",
 ]),
 ("Tokning kattaligi va o'lchov birligi", [
  "Tok kuchi (I) amperda o'lchanadi. 1 amper — kesim orqali sekundiga 1 kulon zaryad o'tishi.",
  "1 kulon — taxminan 6 240 000 000 000 000 000 ta elektron. Ya'ni 1 A da sekundiga shuncha elektron o'tadi.",
  "Maktab sxemalarida toklar kichik: LED 20 mA, zummer 30 mA, servo 250 mA.",
  "Uy jihozlarida kattaroq: lampochka 0,5 A, choynak 9 A.",
  "Inson uchun xavfli chegara — 10 mA dan boshlanadi, shuning uchun 220 V bilan ishlash taqiqlanadi.",
 ]),
 ("Kutilmagan haqiqat: elektronlar sekin harakatlanadi", [
  "Chiroq kalitini bosganda lampa DARHOL yonadi — bu elektronlar tez uchgani uchun emas.",
  "Elektronlarning haqiqiy o'rtacha tezligi juda kichik: soatiga bir necha santimetr.",
  "Tez tarqaladigan narsa — elektr MAYDONI, u yorug'lik tezligiga yaqin tezlikda o'tadi.",
  "Suv to'la quvurga o'xshaydi: bir uchidan suv qo'ysangiz, ikkinchi uchidan darhol chiqadi, garchi aynan o'sha suv tomchisi hali yetib bormagan bo'lsa ham.",
 ]),
),

"Elektr toki: zaryadning yo'naltirilgan harakati": D(
 ("Tokning shartli va haqiqiy yo'nalishi", [
  "Shartli (texnik) yo'nalish: tok PLYUSDAN MINUSGA oqadi deb qabul qilingan. Hamma sxemalarda shunday chiziladi.",
  "Haqiqiy yo'nalish: elektronlar manfiy zaryadli, shuning uchun ular MINUSDAN PLYUSGA harakatlanadi.",
  "Bu qarama-qarshilik tarixiy: shartli yo'nalish elektron kashf qilinishidan oldin belgilangan va o'zgartirilmagan.",
  "Amalda bu hech narsani buzmaydi: hisob va sxemalar shartli yo'nalish bo'yicha to'g'ri chiqadi.",
 ]),
 ("Tok turlari", [
  "O'zgarmas tok (DC) — yo'nalishi doim bir xil. Batareya, akkumulyator, USB shunday tok beradi.",
  "O'zgaruvchan tok (AC) — yo'nalishi sekundiga 50 marta almashadi. Rozetkadagi tok shunday.",
  "Elektronika deyarli har doim DC bilan ishlaydi, shuning uchun adapter AC ni DC ga aylantirib beradi.",
  "Sxemada DC to'g'ri chiziq bilan, AC esa to'lqinsimon chiziq bilan belgilanadi.",
 ]),
),

"Kuchlanish: zaryadni harakatlantiruvchi kuch": D(
 ("Kuchlanishning fizik ma'nosi", [
  "Kuchlanish (U) — zanjirning ikki nuqtasi orasidagi zaryadlar farqi natijasida hosil bo'lgan itaruvchi kuch.",
  "1 volt — 1 kulon zaryadni ko'chirishda 1 joul energiya sarflanishini bildiradi.",
  "Kuchlanish DOIM IKKI NUQTA ORASIDA o'lchanadi. \"Shu simda 5 volt\" degan gap to'liq emas — nimaga nisbatan degan savol qoladi.",
  "Shuning uchun sxemada GND (yer) nuqtasi tanlanadi va hamma kuchlanish shunga nisbatan sanaladi.",
 ]),
 ("Amaldagi kuchlanishlar", [
  "AA batareya — 1,5 V. To'rttasi ketma-ket ulansa 6 V.",
  "Kron batareya — 9 V. Li-ion akkumulyator — 3,7 V (to'la zaryadda 4,2 V).",
  "USB port — 5 V. Arduino Uno mantiq darajasi — 5 V, ESP32 — 3,3 V.",
  "Rozetka — 220 V. Bu maktab darslarida ISHLATILMAYDI.",
  "Statik zaryad esa minglab volt bo'lishi mumkin, lekin toki juda kichik — shuning uchun u xavfli emas, faqat mikrosxemalarni shikastlashi mumkin.",
 ]),
 ("Suv analogiyasi va uning chegarasi", [
  "Kuchlanish — bosim, tok — oqim tezligi, qarshilik — quvurning torayishi.",
  "Bak baland turgan bo'lsa bosim katta (kuchlanish), quvur keng bo'lsa oqim ko'p (tok).",
  "Analogiyaning chegarasi: suv quvurdan chiqib ketishi mumkin, elektronlar esa zanjirdan chiqmaydi — ular yopiq halqa bo'ylab aylanadi.",
  "Shuning uchun zanjir albatta YOPIQ bo'lishi kerak, aks holda tok umuman oqmaydi.",
 ]),
),

"Tok, kuchlanish, qarshilik: asosiy kattaliklar": D(
 ("Uch kattalik va ularning bog'liqligi", [
  "Kuchlanish (U, volt) — sabab. U tokni harakatga keltiradi.",
  "Tok (I, amper) — natija. U kuchlanish ta'sirida paydo bo'ladi.",
  "Qarshilik (R, om) — to'sqinlik. U tokni cheklaydi.",
  "Om qonuni bu uchtasini bog'laydi: I = U / R. Kuchlanish ortsa tok ortadi, qarshilik ortsa tok kamayadi.",
 ]),
 ("Birliklar va ularning nisbatlari", [
  "Tok: 1 A = 1000 mA = 1 000 000 mkA. Maktab sxemalarida odatda mA ishlatiladi.",
  "Kuchlanish: 1 V = 1000 mV. Sensor signallari ko'pincha millivoltlarda bo'ladi.",
  "Qarshilik: 1 kOm = 1000 Om, 1 MOm = 1 000 000 Om. Rezistorlarda 220 Om, 1 kOm, 10 kOm eng ko'p uchraydi.",
  "Hisoblashda hamma qiymat asosiy birlikka (V, A, Om) keltiriladi — bu eng ko'p uchraydigan xatoning oldini oladi.",
 ]),
 ("Har birini qanday o'lchash kerak", [
  "Kuchlanish — multimetrni element ikki uchiga PARALLEL tegizib. Zanjir uzilmaydi.",
  "Tok — zanjirni UZIB, multimetrni o'sha uzilgan joyga KETMA-KET qo'yib.",
  "Qarshilik — quvvatni uzib, elementni zanjirdan chiqarib olib.",
  "Bu uch usulni chalkashtirish eng ko'p uchraydigan xato: tok rejimidagi multimetrni batareyaga parallel ulash predoxranitelni kuydiradi.",
 ]),
),

"Atom, elektron va zaryad": D(
 ("Atom tuzilishi", [
  "Atom markazida yadro: musbat zaryadli protonlar va zaryadsiz neytronlar.",
  "Yadro atrofida manfiy zaryadli elektronlar qatlamlar bo'ylab joylashgan.",
  "Oddiy holatda proton va elektron soni teng, shuning uchun atom umumiy zaryadsiz (neytral).",
  "Elektron yo'qotgan atom musbat, ortiqcha elektron olgan atom manfiy ion bo'ladi.",
 ]),
 ("Nima uchun metall tokni o'tkazadi", [
  "Metall atomlarining eng tashqi elektronlari yadroga kuchsiz bog'langan.",
  "Kristall panjarada bu elektronlar o'z atomini tashlab, umumiy \"elektron bulut\" hosil qiladi.",
  "Shuning uchun metallda erkin zaryad tashuvchilar juda ko'p va u tokni yaxshi o'tkazadi.",
  "Rezinada esa elektronlar atomga mahkam bog'langan va deyarli erkin zaryad yo'q — shuning uchun u izolyator.",
  "Yarimo'tkazgichda (kremniy) erkin elektron kam, lekin qo'shimcha ta'sir (harorat, yorug'lik, kuchlanish) bilan ularning sonini boshqarish mumkin.",
 ]),
 ("Statik zaryad", [
  "Ikki jism ishqalanganda birining elektronlari ikkinchisiga o'tadi va ular qarama-qarshi zaryadlanadi.",
  "Zaryadlangan shar qog'oz parchalarini tortadi, chunki u qog'ozdagi zaryadlarni siljitadi.",
  "Statik zaryad minglab volt bo'lishi mumkin, lekin zaryad miqdori juda kichik — shuning uchun u odam uchun xavfli emas.",
  "Lekin mikrosxemalar uchun xavfli: statik razryad ichkarisidagi yupqa qatlamni teshib yuborishi mumkin. Shuning uchun platani chetlaridan ushlash kerak.",
 ]),
),

"O'tkazgich va izolyator: qaysi materialdan tok o'tadi": D(
 ("Materiallarning qarshiligi", [
  "Kumush — eng yaxshi o'tkazgich, lekin qimmat. Mis — eng ko'p ishlatiladigani.",
  "Alyuminiy misdan yomonroq o'tkazadi, lekin yengil va arzon — shuning uchun yuqori voltli liniyalarda ishlatiladi.",
  "Oltin zanglamaydi, shuning uchun razyom kontaktlariga qoplanadi.",
  "Izolyatorlar: rezina, plastmassa, shisha, chinni, quruq yog'och, havo.",
  "Solishtirish uchun: mis qarshiligi shishanikidan taxminan 10 000 000 000 000 000 000 000 marta kichik.",
 ]),
 ("Chegaradagi holatlar", [
  "Toza suv tokni deyarli o'tkazmaydi. Lekin unda tuz erisa — ionlar paydo bo'ladi va u yaxshi o'tkazgichga aylanadi.",
  "Aynan shuning uchun ho'l qo'l bilan elektr jihozini ushlash xavfli: terining namligi va tuzi qarshilikni keskin kamaytiradi.",
  "Quruq teri qarshiligi ~100 kOm, nam teri esa ~1 kOm bo'lishi mumkin — bu yuz barobar farq.",
  "Havo ham izolyator, lekin kuchlanish juda katta bo'lsa u \"teshiladi\" va uchqun chiqadi. Chaqmoq — aynan shu hodisa.",
 ]),
),

"Batareya — tok manbai, musbat va manfiy qutb": D(
 ("Batareya ichida nima sodir bo'ladi", [
  "Batareya ichida ikki xil metall (elektrod) va elektrolit bor.",
  "Kimyoviy reaksiya natijasida bir elektrodda elektronlar to'planadi (minus qutb), ikkinchisida yetishmaydi (plyus qutb).",
  "Bu farq kuchlanish hosil qiladi. Zanjir ulanganda elektronlar minusdan plyusga oqa boshlaydi.",
  "Ya'ni batareya elektronlarni \"yaratmaydi\" — u ularni harakatlantirish uchun energiya beradi. Elektronlar simning o'zida allaqachon bor.",
  "Reaksiya davom etgan sari elektrodlar sarflanadi va batareya \"o'ladi\".",
 ]),
 ("Qutblarni aniqlash va qoidalar", [
  "Batareyada plyus tomon do'ppayib chiqqan, minus tomon yassi bo'ladi.",
  "Sxemada uzun chiziq — plyus, kalta va yo'g'on chiziq — minus.",
  "Simlarda qizil odatda plyus, qora minus. Lekin bu majburiy standart emas — tekshirish kerak.",
  "Qutbni teskari ulash: LED shunchaki yonmaydi (zarari yo'q), lekin ko'p modullar va mikrosxemalar bir zumda ishdan chiqadi.",
  "Batareyaning ikki qutbini bevosita ulash — qisqa tutashuv. Batareya qiziydi, oqishi yoki yorilishi mumkin.",
 ]),
),

"Batareya kuchlanishi: yangi va eski batareya": D(
 ("Kuchlanish qanday tushadi", [
  "Yangi AA batareya 1,5-1,6 V beradi. Ishlatilgan sari kuchlanish asta tushadi.",
  "1,2 V ga tushganda ko'p qurilmalar ishlashdan to'xtaydi, garchi batareyada energiya hali qolgan bo'lsa ham.",
  "0,9 V — batareya butunlay bo'shagan deb hisoblanadi.",
  "Muhim: kuchlanish YUKSIZ o'lchanganda deyarli normal ko'rinadi. Haqiqiy holatni bilish uchun uni yuk ostida o'lchash kerak.",
 ]),
 ("Sig'im va uning ma'nosi", [
  "Sig'im mAh (milliamper-soat) da o'lchanadi. AA batareya ~2000 mAh.",
  "Ma'nosi: 100 mA tortadigan qurilma taxminan 20 soat ishlaydi (2000 / 100 = 20).",
  "Lekin bu taxminiy: katta tok tortilganda haqiqiy sig'im kamayadi.",
  "Turlari: alkalin (arzon, bir martalik), litiy (qimmat, uzoq), NiMH akkumulyator (qayta zaryadlanadi, 1,2 V).",
  "Akkumulyator kuchlanishi 1,2 V — bu oddiy batareyadan past va ba'zi qurilmalar unda ishlamaydi.",
 ]),
),

"Batareyaning ichki qarshiligi: nega kuchlanish cho'kadi": D(
 ("Ichki qarshilik nima", [
  "Batareya ideal manba emas: uning ichida ham qarshilik bor (elektrolit va elektrodlar qarshiligi).",
  "Yangi AA batareyada bu ~0,15 Om, eski batareyada esa bir necha om bo'lishi mumkin.",
  "Tok oqqanda bu ichki qarshilikda ham kuchlanish tushadi va tashqi zanjirga kamroq qoladi.",
  "Formulasi: U(tashqi) = EYuK - I x R(ichki).",
 ]),
 ("Amaldagi oqibatlari", [
  "Misol: 1,5 V batareya, ichki qarshilik 0,5 Om. 200 mA tok oqsa: 1,5 - 0,2 x 0,5 = 1,4 V qoladi.",
  "Servo yoki motor ishga tushganda tok keskin ortadi va kuchlanish bir lahzaga cho'kadi.",
  "Shu lahzada plata qayta yuklanib ketishi mumkin — bu \"brownout\" deb ataladi.",
  "Yechim: quvvat liniyasiga 100-470 mkF kondensator qo'yish (u shu lahzada zaxira zaryad beradi) yoki motorni alohida manbadan quvvatlash.",
  "Eski batareyada ichki qarshilik katta — shuning uchun u yuksiz 1,4 V ko'rsatib, yuk ostida darhol cho'kadi.",
 ]),
),

"Tok manbalari: batareya, akkumulyator, adapter": D(
 ("Manbalarni solishtirish", [
  "Alkalin batareya: arzon, uzoq saqlanadi, lekin bir martalik. AA — 1,5 V, 2000 mAh.",
  "NiMH akkumulyator: 1000 martagacha zaryadlanadi, lekin kuchlanishi 1,2 V va o'zi asta bo'shaydi.",
  "Li-ion akkumulyator: sig'imi katta, kuchlanishi 3,7 V, lekin himoya sxemasi SHART — aks holda yong'in xavfi bor.",
  "Adapter: barqaror, cheksiz, lekin qurilma ko'chma bo'lmaydi va rozetkaga bog'liq.",
  "Powerbank: 5 V beradi, qulay, lekin tok kam bo'lsa o'zi o'chib qoladi.",
 ]),
 ("Manbani to'g'ri tanlash", [
  "Avval qurilmaning eng katta tokini hisoblang: hamma element bir vaqtda ishlaganda qancha tortadi.",
  "Keyin manba shu tokdan kamida 1,5 barobar ko'proq bera olishi kerak.",
  "Ishlash muddatini hisoblang: sig'im (mAh) / o'rtacha tok (mA) = soat.",
  "Motor va servo bor bo'lsa ular ALOHIDA manbadan quvvatlanadi, plata bilan faqat GND birlashtiriladi.",
  "Yig'ilgan qurilmada manba kuchlanishini yuk ostida multimetr bilan tekshirish odat bo'lishi kerak.",
 ]),
),

"Yopiq va ochiq zanjir": D(
 ("Zanjir yopiq bo'lishi shart", [
  "Tok faqat YOPIQ halqada oqadi: manbadan chiqib, elementlardan o'tib, manbaga qaytadi.",
  "Halqaning istalgan joyi uzilsa tok butunlay to'xtaydi — LED ham, motor ham ishlamaydi.",
  "Kalit aynan shu prinsipda ishlaydi: u halqani ataylab uzadi va ulaydi.",
  "Sxemani tekshirishda barmoq bilan halqa bo'ylab yurib chiqish kerak: manbadan boshlab, yana manbaga qaytish.",
 ]),
 ("Nima uchun zanjir ochiq qolishi mumkin", [
  "Sim teshikka to'liq kirmagan (breadboardda eng ko'p uchraydigan sabab).",
  "Kontakt oksidlangan yoki iflos.",
  "Sim ichidan uzilgan — tashqi ko'rinishi butun, lekin ichi uzuq. Multimetrning signalli rejimi buni topadi.",
  "Komponent kuygan (LED, rezistor).",
  "Batareya bo'shagan yoki kontakt prujinasi bosilib qolgan.",
 ]),
),

"Birinchi zanjir: batareya va lampochka": D(
 ("Eng oddiy zanjirning uch qismi", [
  "MANBA — energiya beradi (batareya).",
  "ISTE'MOLCHI — energiyani foydali ishga aylantiradi (lampochka, LED, motor).",
  "O'TKAZGICH — ularni bog'laydi (sim).",
  "To'rtinchi ixtiyoriy qism — BOSHQARUV (kalit).",
  "Bu tuzilma har qanday elektr qurilmada, eng oddiysidan tortib kompyutergacha, saqlanadi.",
 ]),
 ("Zanjirni yig'ish tartibi", [
  "1) Avval sxemani qog'ozda chizing va halqani barmoq bilan tekshiring.",
  "2) Manbani OXIRIDA ulang — hamma element joyiga qo'yilgandan keyin.",
  "3) Qutblarni tekshiring: LEDning uzun oyog'i plyus tomonga.",
  "4) Rezistorni unutmang: LEDga to'g'ridan-to'g'ri kuchlanish berilmaydi.",
  "5) Ishlamasa — bosqichma-bosqich tekshiring, hammasini birdan qayta yig'manг.",
 ]),
),

"Vklyuchatel: holatni saqlaydigan kalit": D(
 ("Kalit turlari", [
  "Tugma (tact switch) — faqat bosilib turganda ulaydi, qo'yib yuborilsa uziladi.",
  "Vklyuchatel (toggle/slide switch) — bir marta o'zgartirilsa HOLATNI SAQLAYDI.",
  "Bu farq muhim: chiroq uchun vklyuchatel kerak, qo'ng'iroq uchun tugma.",
  "Kontakt turlari: NO (normally open — odatda uzuq), NC (normally closed — odatda ulangan).",
 ]),
 ("Kontakt sxemalari", [
  "SPST — bitta zanjirni ulaydi/uzadi. Eng oddiy kalit.",
  "SPDT — bitta kirishni ikki chiqishdan biriga ulaydi (o'tkazgich kalit).",
  "DPDT — ikki zanjirni bir vaqtda almashtiradi. Motor yo'nalishini o'zgartirishda ishlatiladi.",
  "Kalit parametrlari: maksimal kuchlanish va tok. 250 V / 3 A yozuvi shuni bildiradi.",
  "Chegaradan oshiq tok o'tkazilsa kontakt kuyib yopishib qoladi.",
 ]),
),

"Qisqa tutashuv: nima va nega xavfli": D(
 ("Qisqa tutashuv nima", [
  "Qisqa tutashuv — manba ikki qutbining qarshiliksiz (yoki juda kichik qarshilikli) yo'l bilan tutashishi.",
  "Om qonuni bo'yicha: R nolga yaqinlashsa, I = U / R juda katta bo'ladi.",
  "1,5 V batareya va 0,1 Om qarshilikda tok 15 A ga yetadi — bu normal ish tokidan yuz barobar ko'p.",
  "Bu tokning hammasi issiqlikka aylanadi: sim qiziydi, izolyatsiya eriydi, batareya shishadi.",
 ]),
 ("Eng ko'p uchraydigan sabablari", [
  "Breadboardda ochiq sim uchi qo'shni qatorga tegib turishi.",
  "LED yoki rezistor oyoqlari bir-biriga tegishi.",
  "5V va GND simlarini bir qatorga qo'yib yuborish.",
  "Kavsharlashda ortiqcha qalay ikki yo'lakni tutashtirib qo'yishi.",
  "Modulni teskari ulash.",
 ]),
 ("Oldini olish va belgilari", [
  "Quvvat berishdan OLDIN ko'z bilan tekshirish — eng samarali usul.",
  "Multimetrning signalli rejimida 5V va GND orasini tekshirish: signal chiqsa qisqa tutashuv bor.",
  "Belgilari: plata qiziydi, USB port o'chadi, batareya tez bo'shaydi, hidlanadi.",
  "Shubha bo'lsa darhol quvvatni uzish va sababni topmaguncha qayta yoqmaslik.",
 ]),
),

"Qisqa tutashuv va himoya (predoxranitel)": D(
 ("Predoxranitel qanday ishlaydi", [
  "Predoxranitel ichida nozik metall sim bor. U belgilangan tokda eriydi va zanjirni uzadi.",
  "Nominal tokda u qizib turadi, lekin erimaydi. Tok chegaradan oshsa bir necha millisekundda uziladi.",
  "Turlari: tez ishlaydigan (F) va sekin ishlaydigan (T — motor kabi ishga tushishda tok tortadigan yuklamalar uchun).",
  "Predoxranitel BIR MARTALIK — kuygandan keyin almashtiriladi. Uni sim bilan bog'lab qo'yish o'ta xavfli.",
 ]),
 ("Boshqa himoya usullari", [
  "Qayta tiklanadigan predoxranitel (PTC, polyfuse): qizib qarshiligini oshiradi, sovigach o'zi tiklanadi. Arduino USB portida shu turgan.",
  "Avtomatik o'chirgich — uy elektr shchitida ishlatiladi, tugmasi bilan qayta yoqiladi.",
  "Tok cheklovchi sxema — quvvat manbaida elektron himoya.",
  "Dasturiy himoya: INA219 bilan tokni o'lchab, chegaradan oshsa relени uzish.",
 ]),
),

# ============================================================ MULTIMETR
"Multimetr bilan tanishuv: rejimlar va xavfsizlik": D(
 ("Asosiy rejimlar", [
  "V= (yoki DCV) — o'zgarmas kuchlanish. Batareya va plata uchun aynan shu ishlatiladi.",
  "V~ (ACV) — o'zgaruvchan kuchlanish, rozetka uchun. Darsda ishlatilmaydi.",
  "A= (DCA) — o'zgarmas tok. Shchup uyasini ALMASHTIRISH kerak.",
  "Om — qarshilik. Faqat kuchlanishsiz zanjirda.",
  "Signalli rejim (diod belgisi yoki tovush belgisi) — uzilishni tekshirish. Eng ko'p ishlatiladigan rejim.",
  "Diod rejimi — diod va LEDni tekshirish, qutbini aniqlash.",
 ]),
 ("Shchup uyalari", [
  "COM — qora shchup, doim shu yerda turadi.",
  "V/Om/mA — qizil shchup, kuchlanish va qarshilik uchun.",
  "10A (yoki 20A) — alohida uya, katta tok o'lchash uchun.",
  "ENG XAVFLI XATO: shchup tok uyasida turganda kuchlanish o'lchashga urinish. Bu qisqa tutashuv bo'ladi va predoxranitel kuyadi.",
  "Shuning uchun har o'lchovdan oldin shchup qaysi uyada turganini ko'rish odat bo'lishi kerak.",
 ]),
 ("Oraliqni tanlash", [
  "Avtomatik oraliqli (auto range) multimetrda oraliq o'zi tanlanadi.",
  "Qo'lda tanlanadiganda: avval eng KATTA oraliqni qo'yib, keyin kichraytirish kerak.",
  "Ekranda \"1\" yoki \"OL\" chiqsa — qiymat oraliqdan katta, oraliqni oshirish kerak.",
  "Qiymat 0,00 chiqsa — oraliq juda katta, kichraytirilsa aniqroq bo'ladi.",
 ]),
),

"Multimetr tuzilishi va xavfsizlik qoidalari": D(
 ("Ichida nima bor", [
  "Multimetr asosan KUCHLANISH o'lchagichdir. Qolgan hamma o'lchov shunga keltiriladi.",
  "Tok o'lchashda ichkarida juda kichik qarshilikli shunt rezistor bor: undagi kuchlanish tushishi o'lchanadi va tok hisoblanadi.",
  "Qarshilik o'lchashda multimetr o'zi kichik tok beradi va hosil bo'lgan kuchlanishni o'lchaydi.",
  "Shuning uchun qarshilik o'lchashda zanjirda begona kuchlanish bo'lmasligi kerak — u natijani buzadi.",
 ]),
 ("Xavfsizlik qoidalari", [
  "Zanjirga kuchlanish berilganda qarshilik O'LCHANMAYDI.",
  "Tok rejimida multimetr hech qachon manbaga PARALLEL ulanmaydi.",
  "O'lchovdan keyin rejimni V= holatiga qaytarib qo'yish odat bo'lishi kerak — keyingi safar xato qilish ehtimoli kamayadi.",
  "Shchup uchlari yalang'och — ikki qo'shni kontaktni tasodifan tutashtirib yubormaslik uchun ehtiyot bo'lish kerak.",
  "220 V o'lchash darsda bajarilmaydi.",
 ]),
),

"Multimetr: kuchlanishni o'lchash": D(
 ("O'lchash tartibi", [
  "1) Rejimni V= (DCV) ga qo'ying.",
  "2) Qora shchup COM uyasida, qizil shchup V uyasida.",
  "3) Qora shchupni GND (minus) ga, qizilni o'lchanadigan nuqtaga tegizing.",
  "4) Zanjir ISHLAB TURGAN holatda o'lchanadi — uni uzish shart emas.",
  "Qiymat manfiy chiqsa — shchuplar almashtirilgan, zarari yo'q.",
 ]),
 ("Nimani o'lchash foydali", [
  "Batareya kuchlanishi — yuksiz va yuk ostida alohida. Farq ichki qarshilikni ko'rsatadi.",
  "Har bir element ustidagi kuchlanish tushishi. Ketma-ket zanjirda ularning yig'indisi manba kuchlanishiga teng bo'lishi kerak.",
  "LEDdagi tushish — qizil uchun ~2 V, ko'k uchun ~3 V. Rezistorni o'zgartirsangiz ham u deyarli o'zgarmaydi.",
  "Kuchlanish bo'luvchi chiqishi — hisoblangan qiymat bilan solishtiriladi.",
  "Plata pinidagi kuchlanish — HIGH bo'lsa ~5 V, LOW bo'lsa ~0 V.",
 ]),
),

"Kuchlanishni o'lchash (Volt)": D(
 ("Kuchlanish ikki nuqta orasida o'lchanadi", [
  "Bitta shchup bilan kuchlanish o'lchab bo'lmaydi — u DOIM farq sifatida o'lchanadi.",
  "Odatda qora shchup GND da qoldiriladi va qizil shchup bilan turli nuqtalar tekshiriladi.",
  "Shunda o'lchangan qiymat \"GND ga nisbatan\" kuchlanish bo'ladi — sxemada ham shunday belgilanadi.",
  "Element ustidagi tushishni o'lchash uchun esa shchuplar aynan o'sha elementning ikki uchiga qo'yiladi.",
 ]),
 ("Kirxgofning kuchlanish qonuni", [
  "Yopiq halqa bo'ylab hamma kuchlanish tushishlari yig'indisi manba kuchlanishiga teng.",
  "Misol: 9 V batareya, ikki rezistor ketma-ket. Birida 6 V, ikkinchisida 3 V tushsa — yig'indi 9 V.",
  "Bu qonun sxemani tekshirishda juda foydali: yig'indi mos kelmasa, demak o'lchanmagan element yoki yomon kontakt bor.",
  "Amaliy tekshiruv: har bir element ustidagi tushishni o'lchab, jadvalga yozib, yig'indisini hisoblash.",
 ]),
),

"Kuchlanishni o'lchash amaliyoti": D(
 ("Nimalarni o'lchab ko'rish kerak", [
  "Yangi va eski batareya — farqni raqamda ko'rish.",
  "Ketma-ket ulangan ikki batareya — kuchlanish qo'shilishini tasdiqlash.",
  "Parallel ulangan ikki batareya — kuchlanish o'zgarmasligini ko'rish.",
  "Ketma-ket zanjirdagi har bir rezistor — taqsimotni ko'rish.",
  "LED ustidagi tushish — u deyarli doim 2 V atrofida qolishini tekshirish.",
 ]),
 ("Natijani baholash", [
  "Hisoblangan va o'lchangan qiymat 5-10 % farq qilishi normal: rezistor bardoshi 5 %, batareya kuchlanishi nominaldan farq qiladi.",
  "Farq 30 % dan ko'p bo'lsa — sxemada yoki hisobda xato bor.",
  "Nol chiqsa — kontakt yo'q yoki element qisqa tutashgan.",
  "Manba kuchlanishiga teng chiqsa — element uzilgan (butun kuchlanish shunga tushyapti).",
 ]),
),

"Tokni o'lchash (Amper): zanjirni uzib ulash": D(
 ("Nima uchun zanjir uziladi", [
  "Multimetr tokni o'lchash uchun tok UNING ICHIDAN o'tishi kerak.",
  "Shuning uchun u zanjirga KETMA-KET qo'yiladi: zanjir uziladi va multimetr o'sha bo'shliqni to'ldiradi.",
  "Tok rejimida multimetrning ichki qarshiligi juda kichik (deyarli sim) — shuning uchun uni parallel ulash qisqa tutashuv bo'ladi.",
  "Kuchlanish rejimida esa aksincha: ichki qarshilik juda katta, shuning uchun u parallel ulanadi va zanjirga xalaqit bermaydi.",
 ]),
 ("O'lchash tartibi", [
  "1) Quvvatni uzing.",
  "2) Zanjirni kerakli joyda uzing (masalan rezistor va LED orasida).",
  "3) Qizil shchupni mA (yoki 10A) uyasiga ko'chiring, rejimni A= ga qo'ying.",
  "4) Shchuplarni uzilgan ikki uchga tegizing.",
  "5) Quvvatni yoqing va qiymatni o'qing.",
  "6) O'lchov tugagach shchupni V uyasiga QAYTARING — bu eng muhim odat.",
 ]),
),

"Tokni o'lchash amaliyoti": D(
 ("Nimalarni o'lchash foydali", [
  "LED zanjiridagi tok — rezistorni o'zgartirib, tok qanday o'zgarishini kuzatish.",
  "Ketma-ket zanjirda ikki nuqtada tok — u hamma joyda BIR XIL ekanini tasdiqlash.",
  "Parallel zanjirda umumiy tok va har bir shoxdagi tok — yig'indi umumiy tokka tengligini tekshirish.",
  "Motor tokini bo'sh yurishda va valini barmoq bilan ushlab turganda — farq bir necha barobar chiqadi.",
 ]),
 ("Xatolardan saqlanish", [
  "Shchup tok uyasida qolib, keyin kuchlanish o'lchashga urinish — predoxranitel kuyadi. Bu eng ko'p uchraydigan xato.",
  "10A uyasi odatda himoyalanmagan — unda 10 A dan ko'p tok o'lchash multimetrni buzadi.",
  "Motor tokini o'lchashda mA uyasi yetmasligi mumkin (u odatda 200 mA gacha) — 10A uyasini ishlatish kerak.",
  "O'lchov paytida shchuplarni mahkam ushlash: kontakt uzilsa qiymat sakraydi.",
 ]),
),

"Qarshilikni o'lchash (Om)": D(
 ("O'lchash shartlari", [
  "Zanjirda KUCHLANISH BO'LMASLIGI kerak — quvvat uziladi.",
  "Element zanjirdan CHIQARIB olinadi yoki kamida bir oyog'i uziladi.",
  "Sabab: zanjirdagi boshqa elementlar parallel yo'l hosil qiladi va natija noto'g'ri chiqadi.",
  "Barmoq bilan ikkala shchupni ushlab turmang — tananing qarshiligi natijaga qo'shiladi.",
 ]),
 ("Natijani o'qish", [
  "\"1\" yoki \"OL\" — qarshilik oraliqdan katta yoki zanjir uzilgan.",
  "0 ga yaqin — qisqa tutashuv yoki o'tkazgich.",
  "Rezistorda o'lchangan qiymat nominaldan 5 % gacha farq qilishi normal.",
  "Fotorezistor va termistorni o'lchab, ularga ta'sir qilib (yopish, isitish) qarshilik o'zgarishini ko'rish mumkin — bu sensor prinsipini eng aniq ko'rsatadigan tajriba.",
 ]),
),

"Qarshilikni o'lchash amaliyoti": D(
 ("Amaliy mashqlar", [
  "10 ta rezistorni rangli kod bo'yicha o'qib, keyin o'lchab, farqni jadvalga yozish.",
  "Ikki rezistorni ketma-ket ulab o'lchash — qiymatlar qo'shilishini tasdiqlash.",
  "Ikki bir xil rezistorni parallel ulab o'lchash — natija yarmiga tengligini ko'rish.",
  "Fotorezistorni yorug'da va qo'l bilan yopib o'lchash — qarshilik o'nlab barobar o'zgaradi.",
  "Termistorni barmoq bilan isitib o'lchash — qarshilik kamayishini kuzatish.",
  "Simning ikki uchini o'lchash — deyarli 0 Om chiqadi (o'tkazgich).",
 ]),
),

"O'lchov aniqligi va xatolik": D(
 ("Xatolik turlari", [
  "Asbob xatosi: multimetr pasportida yozilgan, masalan ±0,5 % + 2 birlik.",
  "Element bardoshi: rezistorda 5 % (oltin halqa) yoki 1 % (jigarrang halqa).",
  "Kontakt xatosi: yomon kontakt qo'shimcha qarshilik hosil qiladi.",
  "Harorat ta'siri: qizigan element qarshiligini o'zgartiradi.",
  "Odam xatosi: noto'g'ri rejim, noto'g'ri oraliq, noto'g'ri o'qish.",
 ]),
 ("Xatolikni kamaytirish", [
  "Bir o'lchovga ishonmaslik: 3-5 marta o'lchab, o'rtachasini olish.",
  "Shchuplarni mahkam va toza kontaktga tegizish.",
  "Oraliqni to'g'ri tanlash: qiymat oraliqning o'rtasida bo'lgani aniqroq.",
  "Natijani hisob bilan solishtirish: katta farq bo'lsa sababini izlash.",
  "Xatolikni hisoblash: (o'lchangan - hisoblangan) / hisoblangan x 100 %.",
 ]),
),

"O'lchov xatoligi: nega qiymat biroz farq qiladi": D(
 ("Farqning sabablari", [
  "Rezistor nominali ideal emas: 220 Om yozilgan rezistor amalda 214 yoki 227 Om bo'lishi mumkin.",
  "Batareya kuchlanishi 1,5 V emas, 1,47 yoki 1,53 V bo'ladi va yuk ostida yana o'zgaradi.",
  "Simlar va kontaktlarda ham kichik qarshilik bor.",
  "Multimetrning o'zi ham zanjirga ta'sir qiladi (kuchlanish rejimida oz, tok rejimida sezilarli).",
 ]),
 ("Qachon xavotirlanish kerak", [
  "5-10 % farq — normal, hech narsa qilish shart emas.",
  "10-25 % farq — sababni tekshirish kerak: kontakt, batareya holati, rezistor bardoshi.",
  "25 % dan ko'p — sxemada yoki hisobda xato bor.",
  "Muhim ko'nikma: farqni yashirmaslik, uni yozib qo'yish va sababini tushuntirishga urinish. Muhandislikda aynan shu qadrlanadi.",
 ]),
),

# ============================================================ REZISTOR
"Rezistor: vazifasi va rangli kodi": D(
 ("Rezistorning vazifasi", [
  "Rezistor tokni CHEKLAYDI — u zanjirga qo'shimcha qarshilik qo'shadi.",
  "LED bilan ishlatilishining sababi: LEDning o'z qarshiligi juda kichik va rezistorsiz tok uni kuydiradi.",
  "Ikkinchi vazifasi — kuchlanish bo'luvchi hosil qilish (sensorlarni ulashda).",
  "Uchinchi vazifasi — tortuvchi rezistor: pin holatini aniq ushlab turish.",
  "Rezistorda energiya issiqlikka aylanadi, shuning uchun uning quvvat bardoshi bor (odatda 0,25 Vt).",
 ]),
 ("Rangli kodni o'qish", [
  "4 halqali rezistor: 1-halqa — birinchi raqam, 2-halqa — ikkinchi raqam, 3-halqa — nechta nol, 4-halqa — bardosh.",
  "Ranglar: qora 0, jigarrang 1, qizil 2, to'q sariq 3, sariq 4, yashil 5, ko'k 6, binafsha 7, kulrang 8, oq 9.",
  "Bardosh: oltin ±5 %, kumush ±10 %, jigarrang ±1 %.",
  "Misol: qizil-qizil-jigarrang-oltin = 2, 2, bitta nol = 220 Om ±5 %.",
  "Misol: jigarrang-qora-to'q sariq = 1, 0, uchta nol = 10 000 Om = 10 kOm.",
  "Misol: sariq-binafsha-qizil = 4, 7, ikkita nol = 4700 Om = 4,7 kOm.",
  "Qaysi tomondan o'qishni bilish uchun: bardosh halqasi (oltin yoki kumush) doim OXIRIDA turadi.",
 ]),
),

"Rezistor va rangli kod": D(
 ("Standart qiymatlar (E12 qatori)", [
  "Rezistorlar istalgan qiymatda ishlab chiqarilmaydi — standart qator bor.",
  "E12 qatori: 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82 va ularning 10 karrali qiymatlari.",
  "Shuning uchun 220 Om, 470 Om, 1 kOm, 4,7 kOm, 10 kOm eng ko'p uchraydi.",
  "Hisobda 150 Om chiqsa, amalda eng yaqin standart qiymat (150 yoki 180 Om) olinadi.",
  "Kerakli qiymat topilmasa, ikkitasini ketma-ket yoki parallel ulash mumkin.",
 ]),
 ("Amaliy maslahatlar", [
  "Rangni ajratish qiyin bo'lsa (jigarrang va qizil ko'pincha adashtiriladi) — multimetr bilan tekshirish kerak.",
  "Eski rezistorlarda ranglar so'lib ketgan bo'lishi mumkin — faqat o'lchov ishonchli.",
  "Rezistorda qutb yo'q, istalgan tomonga ulanadi.",
  "Saqlashda ularni qiymati bo'yicha ajratib qo'yish kerak — aks holda har safar o'lchashga to'g'ri keladi.",
 ]),
),

"Rezistor: rangli halqalarni o'qish": D(
 ("5 halqali rezistorlar", [
  "Aniq (1 %) rezistorlarda 5 halqa bo'ladi: uchta raqam, keyin ko'paytiruvchi, keyin bardosh.",
  "Misol: jigarrang-qora-qora-qora-jigarrang = 1, 0, 0, nolsiz = 100 Om ±1 %.",
  "Misol: qizil-qizil-qora-jigarrang-jigarrang = 2, 2, 0, bitta nol = 2200 Om = 2,2 kOm ±1 %.",
  "5 halqalilarni 4 halqali deb o'qish eng ko'p uchraydigan xato — halqalar sonini avval sanash kerak.",
 ]),
 ("Mashq qilish usuli", [
  "Juftlikda ishlash: bittasi rezistorni ko'rsatadi, ikkinchisi qiymatini aytadi, keyin multimetr bilan tekshiriladi.",
  "Teskari mashq ham foydali: berilgan qiymatga (masalan 3,3 kOm) qaysi ranglar kerakligini aytish.",
  "Vaqt bilan mashq qilish: 20 ta rezistorni necha daqiqada to'g'ri o'qish mumkin.",
  "Bu ko'nikma keyin har bir darsda kerak bo'ladi, shuning uchun uni avtomatizmga yetkazish kerak.",
 ]),
),

"Rezistor nominalini o'lchab, rangli kod bilan solishtirish": D(
 ("Solishtirish jadvali", [
  "Har bir rezistor uchun uch ustun: ranglar, kod bo'yicha qiymat, o'lchangan qiymat.",
  "To'rtinchi ustun — farq foizda: (o'lchangan - nominal) / nominal x 100.",
  "Bu farq bardosh halqasida yozilgan chegaradan (5 % yoki 1 %) oshmasligi kerak.",
  "Oshgan bo'lsa — rezistor buzilgan yoki rangni noto'g'ri o'qigan bo'lishingiz mumkin.",
 ]),
 ("Xulosa chiqarish", [
  "Ko'p rezistorda o'lchangan qiymat nominaldan bir tomonga og'adi — bu ishlab chiqarish xususiyati.",
  "Bardosh chegarasi ishlab chiqaruvchining KAFOLATI: qiymat shu oraliqda bo'lishiga kafolat beriladi.",
  "Shuning uchun aniq sxemalarda 1 % li rezistorlar ishlatiladi, oddiy sxemalarda esa 5 % yetarli.",
  "LED zanjirida 5 % farq umuman sezilmaydi, kuchlanish bo'luvchida esa sezilishi mumkin.",
 ]),
),

"Rezistor nominalini hisoblash mashqlari": D(
 ("LED uchun rezistor hisoblash", [
  "Formula: R = (Umanba - Uled) / I.",
  "5 V va qizil LED (2 V), 20 mA: R = 3 / 0,02 = 150 Om. Amalda 220 Om olinadi.",
  "5 V va ko'k LED (3,2 V), 20 mA: R = 1,8 / 0,02 = 90 Om. Amalda 100 Om.",
  "9 V va qizil LED, 20 mA: R = 7 / 0,02 = 350 Om. Amalda 390 Om.",
  "3,3 V va qizil LED, 10 mA: R = 1,3 / 0,01 = 130 Om. Amalda 150 Om.",
  "Qoida: hisoblangan qiymatdan KATTAROQ standart rezistor olinadi — bu xavfsizroq.",
 ]),
 ("Teskari masalalar", [
  "Berilgan rezistor bilan qancha tok oqadi: I = (Umanba - Uled) / R.",
  "5 V, 220 Om, qizil LED: I = 3 / 220 = 0,0136 A = 13,6 mA. Bu me'yorda.",
  "5 V, 100 Om: I = 3 / 100 = 30 mA. Bu chegaradan yuqori, LED umri qisqaradi.",
  "5 V, 1 kOm: I = 3 / 1000 = 3 mA. LED yonadi, lekin xira.",
 ]),
),

"Quvvatni hisoblab rezistor tanlash": D(
 ("Quvvat bardoshini hisoblash", [
  "Rezistorda ajraladigan quvvat: P = I2 x R yoki P = U2 / R.",
  "Maktab to'plamidagi rezistorlar odatda 0,25 Vt ga mo'ljallangan.",
  "Xavfsizlik uchun hisoblangan quvvat bardoshning yarmidan oshmasligi kerak.",
  "Misol: 220 Om, 20 mA. P = 0,0004 x 220 = 0,088 Vt — 0,25 Vt dan ancha kam, xavfsiz.",
  "Misol: 100 Om, 5 V. P = 25 / 100 = 0,25 Vt — bu aynan chegara, rezistor sezilarli qiziydi.",
  "Misol: 10 Om, 5 V. P = 25 / 10 = 2,5 Vt — bardoshdan 10 barobar ko'p, rezistor kuyadi.",
 ]),
 ("Amaliy belgilar", [
  "Rezistorning quvvat bardoshi uning O'LCHAMIDAN bilinadi: 0,25 Vt kichik, 1 Vt ancha yo'g'on.",
  "Ishlayotgan rezistorni barmoq bilan tekshirish: iliq bo'lsa normal, ushlab bo'lmaydigan darajada issiq bo'lsa bardosh yetmayapti.",
  "Yechim: kattaroq bardoshli rezistor olish yoki ikkitasini parallel ulash (har biriga tokning yarmi tushadi).",
  "Rangi qorayib, hidlanib qolgan rezistor qiymatini o'zgartirgan bo'ladi — u almashtiriladi.",
 ]),
),

"Om qonuni: U = I x R": D(
 ("Formulaning uch shakli", [
  "U = I x R — tok va qarshilik ma'lum bo'lsa kuchlanish topiladi.",
  "I = U / R — kuchlanish va qarshilik ma'lum bo'lsa tok topiladi.",
  "R = U / I — kerakli tokni olish uchun qanday qarshilik kerakligi topiladi.",
  "Uchburchak usuli: yuqorida U, pastda I va R. Topilishi kerak bo'lgan harfni yopsangiz, qolgan ikkitasi formulani ko'rsatadi.",
 ]),
 ("Bog'liqlikning ma'nosi", [
  "Kuchlanish ikki barobar oshsa (qarshilik o'zgarmasa) — tok ham ikki barobar ortadi.",
  "Qarshilik ikki barobar oshsa (kuchlanish o'zgarmasa) — tok ikki barobar kamayadi.",
  "Qarshilik nolga intilsa tok cheksiz ortadi — bu qisqa tutashuv.",
  "Qarshilik cheksizga intilsa tok nolga tushadi — bu zanjirning uzilishi.",
 ]),
 ("Birliklarga e'tibor", [
  "Formulaga qiymatlar V, A va Om da qo'yiladi.",
  "20 mA ni 20 deb qo'yish natijani 1000 marta xato qiladi — bu eng ko'p uchraydigan xato.",
  "1 kOm ni 1 deb qo'yish ham xuddi shunday xatoga olib keladi.",
  "Odat: hisobdan oldin hamma qiymatni asosiy birlikka aylantirib yozib olish.",
 ]),
),

"Om qonuni: formula va ma'nosi": D(
 ("Qonun qanday kashf qilingan", [
  "Georg Om 1827-yilda turli uzunlikdagi simlarda tokni o'lchab, bog'liqlikni topgan.",
  "U kuchlanish va tok TO'G'RI proporsional ekanini aniqlagan: biri ikki barobar oshsa ikkinchisi ham.",
  "Proporsionallik koeffitsienti materialning xususiyati bo'lib chiqdi — u qarshilik deb ataldi.",
  "Qonun faqat \"om materiallari\" uchun to'g'ri: metallar va rezistorlar uchun. Diod va LED bunga bo'ysunmaydi.",
 ]),
 ("Nima uchun LED Om qonuniga bo'ysunmaydi", [
  "Rezistorda kuchlanish va tok chiziqli bog'langan: kuchlanish ikki barobar oshsa tok ham.",
  "LEDda esa 1,8 V gacha tok deyarli nol, keyin esa keskin ko'tarilib ketadi.",
  "Shuning uchun LEDga to'g'ridan-to'g'ri kuchlanish berish xavfli: kichik kuchlanish o'zgarishi tokni bir necha barobar oshiradi.",
  "Yechim: ketma-ket rezistor. Endi tokni rezistor belgilaydi va u Om qonuniga bo'ysunadi.",
  "Aynan shuning uchun LED uchun \"kuchlanish\" emas, \"tok\" beriladi deb aytiladi.",
 ]),
),

"Om qonuni bilan hisoblash mashqlari": D(
 ("Masala yechish tartibi", [
  "1) Berilganlarni yozib oling va birliklarni tekshiring.",
  "2) Nima topilishi kerakligini aniqlang.",
  "3) Formulaning mos shaklini tanlang.",
  "4) Hisoblang.",
  "5) Natijani baholang: u mantiqiy oraliqdami.",
  "6) Imkoni bo'lsa zanjirni yig'ib o'lchab tekshiring.",
 ]),
 ("Namunaviy masalalar", [
  "6 V manba, 300 Om rezistor. Tok? I = 6 / 300 = 0,02 A = 20 mA.",
  "Tok 50 mA, rezistor 100 Om. Kuchlanish? U = 0,05 x 100 = 5 V.",
  "Kuchlanish 12 V, tok 30 mA. Qarshilik? R = 12 / 0,03 = 400 Om.",
  "1,5 V batareya va 15 Om lampochka. Tok? I = 1,5 / 15 = 0,1 A = 100 mA.",
  "Zanjirda 4,5 V va 22 mA. Qarshilik? R = 4,5 / 0,022 = 204 Om, amalda 220 Om.",
 ]),
),

"Om qonuni masalalari yechish": D(
 ("Murakkabroq masalalar", [
  "Ketma-ket ikki rezistor (100 va 200 Om), manba 9 V. Umumiy R = 300 Om, tok = 0,03 A. Birinchi rezistorda 3 V, ikkinchisida 6 V tushadi.",
  "Parallel ikki rezistor (200 va 200 Om), manba 6 V. Har birida 6 V, har birida 30 mA, umumiy tok 60 mA. Umumiy R = 100 Om.",
  "LED (2 V, 20 mA) 9 V manbaga ulanadi. Rezistorda 7 V tushishi kerak: R = 7 / 0,02 = 350 Om, amalda 390 Om.",
  "Ikki LED ketma-ket (har biri 2 V) 9 V manbada: rezistorda 5 V, R = 5 / 0,02 = 250 Om, amalda 270 Om.",
 ]),
 ("Xatolarni tekshirish usuli", [
  "Javob mantiqiymi: 5 V manbada 10 A tok chiqsa, demak xato bor.",
  "Birliklar tekshiruvi: agar javob \"0,00002 A\" chiqsa, uni mA ga aylantirib (0,02 mA) mantiqiyligini baholash osonroq.",
  "Teskari hisob: topilgan qiymatni formulaga qo'yib, berilgan qiymat chiqishini tekshirish.",
  "Amaliy tekshiruv: zanjirni yig'ib o'lchash — bu eng ishonchli usul.",
 ]),
),

}
