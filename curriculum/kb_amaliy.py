# -*- coding: utf-8 -*-
"""
AMALIY ISHNI TEMIRGA BOG'LASH.

Bazadagi ba'zi mavzularning amaliy ishi faqat qog'ozda bajarilar edi:
jadval to'ldirish, hisoblash, misol topish. Bu mavzular nazariy bo'lgani
uchun shunday chiqqan.

Bu yerda o'sha amaliy ishlar QAYTA yozilgan: har birida qog'ozdagi qism
saqlanadi, lekin u endi YIG'ILGAN SXEMA yoki QURILMA ustida bajariladi va
hisob o'lchov bilan tekshiriladi.

Kalit — sillabusdagi mavzu satri. Qiymat — amaliy ishning yangi matni.
Bu kb_5_8 dagi "amaliy" maydonidan USTUN turadi.
"""

AMALIY = {

# ============================================================ ELEKTRONIKA
"Elektr xavfsizligi: nima mumkin, nima mumkin emas":
    "Xavfsizlik plakatini to'ldirib, keyin uni AMALDA sinash: batareya, "
    "rezistor va LEDdan to'g'ri zanjir yig'ish, so'ng o'qituvchi nazoratida "
    "qisqa tutashuvni bir lahza hosil qilib, simning qizishini qo'l bilan "
    "sezish va nima uchun bu taqiqlanishini yozib olish",

"Atom, elektron va zaryad":
    "Atom modelini chizib, keyin uni tajribada ko'rish: ishqalangan shar bilan "
    "qog'oz parchalarini tortish, so'ng multimetr bilan mis sim va plastmassa "
    "qarshiligini o'lchab, o'tkazgichda elektronlar erkin, izolyatorda esa "
    "bog'langanini raqam bilan isbotlash",

"Zanjir elementlari va ularning shartli belgilari":
    "15 ta shartli belgini o'rganib, keyin har biri uchun HAQIQIY komponentni "
    "to'plamdan topib yoniga qo'yish; so'ng o'qituvchi bergan sxema bo'yicha "
    "zanjirni breadboardda yig'ish va u ishlaganini LED bilan tasdiqlash",

"Rezistor nominalini hisoblash mashqlari":
    "20 ta rangli kodni o'qib qiymatini aytish, keyin HAR BIRINI multimetr "
    "bilan o'lchab tekshirish; hisob va o'lchov farqini jadvalga yozib, "
    "rezistor bardoshi (5 %) chegarasidan chiqmaganini aniqlash",

"Kuchlanish bo'luvchi: nazariya":
    "Uch xil nisbatdagi bo'luvchini hisoblab, keyin har birini breadboardda "
    "yig'ib multimetr bilan chiqish kuchlanishini o'lchash; hisob va o'lchov "
    "jadvalini solishtirib, 5 V ni 3,3 V ga tushiradigan nisbatni topish",

"Elektr quvvati: P = U x I":
    "Uch xil rezistorda ajraladigan quvvatni hisoblab, keyin zanjirni yig'ib "
    "multimetr bilan tok va kuchlanishni o'lchash; hisoblangan quvvatni "
    "o'lchov bilan solishtirib, qaysi rezistor sezilarli qizishini qo'l bilan "
    "tekshirish",

"Energiya va iste'mol: kilovatt-soat":
    "Uy jihozlarining quvvatini yozib olib oylik to'lovni hisoblash, keyin "
    "AYNI hisobni o'z sxemangizga qo'llash: LED va motorli zanjirning tokini "
    "multimetr bilan o'lchab, qurilma batareyada necha soat ishlashini "
    "hisoblash va uni amalda tekshirish",

"Komponentni to'g'ri tanlash: katalogdan":
    "Berilgan vazifa uchun katalogdan mos komponent tanlab asoslash, keyin "
    "tanlangan komponentni HAQIQATDA ulab sinash: u vazifani bajaradimi, "
    "chegaralari yetadimi — natijani jadvalga yozish",

"Komponentni katalog (datasheet) bo'yicha tanlash":
    "Uch komponentning datasheetini o'qib parametrlarini jadvalga chiqarish, "
    "keyin har birini ulab, datasheetdagi kamida ikkita qiymatni (ta'minot "
    "kuchlanishi va iste'mol toki) multimetr bilan o'lchab tasdiqlash",

"Rang aralashtirish: qizil + yashil + ko'k":
    "RGB LEDni uch PWM pinga ulab, uch rangni turli kombinatsiyalarda yoqish "
    "va hosil bo'lgan ranglar jadvalini tuzish; har bir rang uchun PWM "
    "qiymatlarini yozib, telefon ekranidagi rang bilan solishtirish",

"Tovush: chastota va baland-pastlik":
    "Passiv zummerni ulab, tone() bilan turli chastotalarni berish va qaysi "
    "notaga to'g'ri kelishini jadvalga yozish; chastotani ikki barobar "
    "oshirib, tovush aynan bir oktava ko'tarilishini quloq bilan tekshirish",

"analogRead va analog signal":
    "Potensiometr, fotorezistor va termistorni A0-A2 ga ulab, uchala manbaning "
    "qiymat oralig'ini aniqlash; har biri uchun eng past va eng baland "
    "qiymatni yozib, multimetr ko'rsatgan kuchlanish bilan solishtirish",

# ============================================================ BLOKLI DASTURLASH
"Blokli dasturlash muhiti (mBlock) bilan tanishuv":
    "mBlock muhitini ochib interfeys qismlari bilan tanishish, keyin darhol "
    "plataga LED ulab, birinchi blokli dasturni yig'ish va yuklab, chiroqni "
    "miltillatishga erishish",

"Blokli va matnli dasturlash: solishtirish":
    "Bir xil vazifani (uch LEDli svetofor) avval blokli, keyin matnli usulda "
    "bajarib, ikkala dasturni AYNI sxemada ishlatish; blok soni va kod "
    "qatorlari sonini sanab, qaysi holatda qaysi usul qulayligini aniqlash",

# ============================================================ SUN'IY INTELLEKT
"Sun'iy intellekt, mashinaviy o'rganish, TinyML":
    "Uch tushunchani jadvalda ajratish, keyin ularni qurilmada ko'rish: avval "
    "oddiy if sharti bilan yorug'lik chegarasini aniqlaydigan dastur yozish, "
    "so'ng tayyor TinyML modelini yuklab, ikkalasining javob vaqti va xotira "
    "sarfini o'lchab solishtirish",

"SI, mashinaviy o'rganish va chuqur o'rganish":
    "Uch tushunchani misollar bilan ajratib tarixiy rivojlanishini chizish, "
    "keyin qurilmada tajriba: bitta vazifani (qorong'ilikni aniqlash) qoida "
    "bilan va model bilan hal qilib, qaysi holatda qaysi yondashuv soddaroq "
    "ekanini raqam bilan ko'rsatish",

"An'anaviy dastur va o'rganuvchi model farqi":
    "Bir vazifani ikki usulda hal qilish: avval fotorezistor uchun qo'lda "
    "chegara yozish, keyin bir necha yorug'lik namunasini yig'ib model "
    "o'rgatish; ikkala yechimni bir sxemada sinab, aniqligini solishtirish",

"Nazorat ostida va nazoratsiz o'rganish":
    "Ikki turdagi o'rganishga misollar topib jadval tuzish, keyin MPU6050 dan "
    "ma'lumot yig'ib ikkalasini sinash: belgilangan imo-ishoralarni tasniflash "
    "(nazorat ostida) va normal harakatdan chetlashishni aniqlash (anomaliya)",

"Neyron tarmoq g'oyasi: oddiy tushuntirish":
    "Bitta neyron ishlashini qog'ozda hisoblab tarmoq tuzilmasini chizish, "
    "keyin uni temirda modellashtirish: ikki fotorezistorni ulab, ularning "
    "qiymatlarini og'irliklarga ko'paytirib yig'ish va yig'indi chegaradan "
    "oshganda LED yoqadigan dastur yozish — bu bitta neyronning aynan o'zi",

"Belgi (feature) va sinf (class) tushunchasi":
    "Berilgan vazifalar uchun belgilar va sinflarni aniqlab jadval tuzish, "
    "keyin MPU6050 ni ulab ikki harakat uchun ma'lumot yig'ish va o'rtacha, "
    "eng katta hamda tebranish kengligi belgilarini hisoblab, ular ikki "
    "sinfni ajratayotganini raqam bilan ko'rsatish",

"Model o'rgatish jarayoni: qadamlar":
    "To'liq ML ish oqimini rejalashtirish, keyin darhol amalda bajarish: "
    "qurilmadan ikki sinf uchun 20 tadan namuna yig'ib, Edge Impulse'da "
    "o'rgatish va aniqlikni ko'rish — bosqichlarni o'z ma'lumotingizda "
    "boshdan oxirigacha o'tish",

"O'rgatish va tekshirish to'plamlari":
    "Ma'lumotni 80/20 nisbatda bo'lib har to'plamning vazifasini tushunish, "
    "keyin tajriba: ataylab hammasini o'rgatishga berib model tuzish va uning "
    "qurilmadagi haqiqiy natijasi brauzerdagi raqamdan qanchalik farq "
    "qilishini o'lchash",

"Aniqlik, chalkashlik matritsasi, F1":
    "Turli ko'rsatkichlarni hisoblab ma'nosini tahlil qilish, keyin o'z "
    "modelingizni qurilmada har sinf uchun 20 martadan sinab, HAQIQIY "
    "chalkashlik matritsasini qo'lda to'ldirish va uni brauzerdagi jadval "
    "bilan solishtirish",

"Obyektni aniqlash (object detection) haqida":
    "Tasnif va obyekt aniqlash farqini misollarda tahlil qilish, keyin "
    "kamerali plata bilan ikkalasini sinab ko'rish: bir xil sahnada tasnif "
    "modeli nima deydi va obyekt aniqlash modeli nima ko'rsatadi — natijani "
    "va kechikish vaqtini yozib olish",

}
