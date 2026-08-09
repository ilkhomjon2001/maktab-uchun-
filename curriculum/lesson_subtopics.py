# -*- coding: utf-8 -*-
"""
Har bir STEAM tema uchun KETMA-KET sub-mavzular (aspektlar).

MUAMMO: bir chorakda bitta tema 15 martagacha takrorlanadi (masalan "Richag qonuni"
1-sinf 1-chorakda 5 ta model bilan). Agar hammasida bir xil nazariya bo'lsa, bola
bir narsani qayta-qayta eshitadi.

YECHIM: har bir tema uchun sub-mavzular ro'yxati. Dars tartibi bo'yicha (sinf ichida,
yil davomida) har safar KEYINGI sub-mavzu olinadi — 1-dars richagning tayanch nuqtasini,
2-dars kuch yelkasini, 3-dars richag toifalarini o'rganadi va h.k.

Har bir sub-mavzu:
  fokus   - shu darsning aniq mavzusi (5.2 sarlavhasi va maqsadga tushadi)
  savol   - darsni ochuvchi savol (5.1 ga qo'shiladi) — har darsda boshqacha
  asosiy  - 5.2 ning asosiy bandlari (sodda, tushunarli tilda — barcha sinf uchun)
  chuqur  - 2-4-sinf uchun qo'shimcha chuqurroq band (ixtiyoriy)
  tajriba - 6.2 "Modelni sinash" dagi ANIQ sinov (har darsda boshqacha)
  uyga    - shu darsga xos uyga vazifa
"""

SUBTOPICS = {}

# ---------------------------------------------------------------------------
# RICHAG (9 ta)
# ---------------------------------------------------------------------------
SUBTOPICS["richag"] = [
    {
        "fokus": "Richag va tayanch nuqtasi",
        "savol": "Nega uzun tayoq bilan og'ir toshni qo'zg'atish osonroq?",
        "asosiy": [
            "Richag — tayanch nuqtasi atrofida aylanadigan qattiq tayoq yoki qism.",
            "Tayanch nuqtasi (fulcrum) — richag tiralib turadigan joy; usiz richag ishlamaydi.",
            "Kundalik misollar: eshik dastagi, teeter-totter, qaychi.",
        ],
        "chuqur": "Tayanch nuqtasi richagning \"o'qi\" vazifasini bajaradi — barcha aylanish shu nuqta atrofida sodir bo'ladi.",
        "tajriba": "Modeldagi tayanch nuqtasini topib, uni barmoq bilan ushlab turgan holda richagni aylantirib ko'rish.",
        "uyga": "Uyingizda tayanch nuqtasi bor 2 ta narsani toping (masalan, qaychi, eshik) va tayanch nuqtasi qayerdaligini belgilab chizing.",
    },
    {
        "fokus": "Kuch yelkasi va yuk yelkasi",
        "savol": "Richagning qaysi joyiga bosgan ma'qul — tayanchga yaqinmi yoki uzoqmi?",
        "asosiy": [
            "Kuch yelkasi — tayanch nuqtasidan biz bosayotgan joygacha bo'lgan masofa.",
            "Yuk yelkasi — tayanch nuqtasidan yukgacha bo'lgan masofa.",
            "Kuch yelkasi uzunroq bo'lsa, kamroq kuch sarflanadi.",
        ],
        "chuqur": "Muvozanat sharti: kuch x kuch yelkasi = yuk x yuk yelkasi.",
        "tajriba": "Richagning turli joyiga (tayanchga yaqin va uzoq) bosib ko'rish va qaysi biri osonroq ekanini taqqoslash.",
        "uyga": "Qaychi bilan qattiq narsani kesganda uni qaychining qaysi qismiga (uchiga yoki tayanchga yaqin joyiga) qo'yish kerakligini sinab ko'ring va sababini yozing.",
    },
    {
        "fokus": "Tayanch nuqtasini siljitish",
        "savol": "Agar tayanch nuqtasini boshqa joyga ko'chirsak, nima o'zgaradi?",
        "asosiy": [
            "Tayanch nuqtasi yukga yaqinlashtirilsa — ko'tarish osonlashadi.",
            "Tayanch nuqtasi kuchga yaqinlashtirilsa — ko'tarish qiyinlashadi, lekin yuk balandroq ko'tariladi.",
            "Demak, tayanch nuqtasining joyi mexanizm \"kuchli\" yoki \"tez\" bo'lishini belgilaydi.",
        ],
        "chuqur": "Bu — muhandislikdagi asosiy murosalardan biri: kuch yutug'i evaziga masofa (yoki tezlik) yo'qotiladi.",
        "tajriba": "Iloji bo'lsa tayanch nuqtasini bir necha teshik surib mahkamlash va ko'tarish qanchalik osonlashganini kuzatish.",
        "uyga": "Teeter-totterda katta odam va kichik bola muvozanatda o'tirishi uchun kim qayerga o'tirishi kerakligini chizib tushuntiring.",
    },
    {
        "fokus": "1-toifa richag (tayanch o'rtada)",
        "savol": "Qaychi va teeter-totterning umumiy tomoni nima?",
        "asosiy": [
            "1-toifa richagda tayanch nuqtasi kuch bilan yuk ORASIDA joylashadi.",
            "Bosganda yuk qarama-qarshi tomonga harakatlanadi.",
            "Misollar: teeter-totter, qaychi, mixchiqargich.",
        ],
        "chuqur": "1-toifa richag ham kuchni oshirishi, ham harakat yo'nalishini teskari qilishi mumkin.",
        "tajriba": "Modelda tayanch, kuch va yuk qayerda joylashganini aniqlab, u 1-toifa richagga to'g'ri kelishini tekshirish.",
        "uyga": "Uydan 1-toifa richagga (tayanch o'rtada) mos 1 ta narsa toping va chizib, uchala nuqtani belgilang.",
    },
    {
        "fokus": "2-toifa richag (yuk o'rtada)",
        "savol": "G'ildirakli aravada yuk qayerda turadi — qo'lda yoki g'ildirakda?",
        "asosiy": [
            "2-toifa richagda yuk kuch bilan tayanch ORASIDA joylashadi.",
            "Bunday richag har doim kuchni oshiradi — og'ir yukni yengil ko'tarish mumkin.",
            "Misollar: g'ildirakli arava, yong'oq chaqqich, shishani ochgich.",
        ],
        "chuqur": "2-toifa richagda kuch yelkasi doim yuk yelkasidan uzun bo'ladi, shuning uchun mexanik yutuq har doim 1 dan katta.",
        "tajriba": "Modelga yuk qo'yib, uni ko'tarish uchun qancha kuch kerakligini his qilish; keyin yukni boshqa joyga surib qayta sinash.",
        "uyga": "G'ildirakli aravaga yukni old tomonga va orqa tomonga qo'yib ko'rgan holda (yoki tasavvur qilib) qaysi holatda ko'tarish osonroq ekanini yozing.",
    },
    {
        "fokus": "3-toifa richag (kuch o'rtada)",
        "savol": "Pinset bilan kichik narsani olayotganda barmoq qayerga bosadi?",
        "asosiy": [
            "3-toifa richagda kuch yuk bilan tayanch ORASIDA joylashadi.",
            "Bunday richag kuchni oshirmaydi, lekin harakatni TEZ va KENG qiladi.",
            "Misollar: pinset, baliq qarmog'i, inson qo'li (tirsak bo'g'imi).",
        ],
        "chuqur": "Uch toifa richag muhandisga tanlov beradi: kuch kerakmi (2-toifa) yoki tezlik kerakmi (3-toifa).",
        "tajriba": "Modelning uchidagi qism qanchalik tez va uzoq harakatlanishini kuzatib, kuch qo'yilgan joy bilan solishtirish.",
        "uyga": "Qo'lingizni tirsakdan bukib, u qaysi toifa richagga o'xshashini tushuntirib yozing.",
    },
    {
        "fokus": "Ikki richag birga ishlaganda",
        "savol": "Ombur yoki qaychi aslida nechta richagdan iborat?",
        "asosiy": [
            "Ombur va qaychi — ikkita richag bitta umumiy tayanch nuqtasida birlashtirilgan.",
            "Ikki tomondan bosilganda kuch ikki barobar samarali ishlaydi.",
            "Shuning uchun ombur bilan qattiq simni ham kesish mumkin.",
        ],
        "chuqur": "Ikki richag simmetrik ishlaganda ularning momentlari qo'shiladi — bu \"kuchlar juftligi\" deb ataladi.",
        "tajriba": "Modelning ikkala qo'lini birga siqib, keyin faqat bitta tomonini bosib ko'rish va farqni sezish.",
        "uyga": "Ikki richagdan tashkil topgan 2 ta asbob toping (masalan, ombur, qaychi) va rasmini chizing.",
    },
    {
        "fokus": "Richag va muvozanat (tarozi tamoyili)",
        "savol": "Tarozi qanday qilib narsaning og'irligini aniqlaydi?",
        "asosiy": [
            "Tarozi — ikki tomoni teng bo'lgan richag; muvozanatda ikkala tomon momenti teng bo'ladi.",
            "Bir tomonga og'irroq narsa qo'yilsa, u tomon pastga tushadi.",
            "Yelkalarni o'zgartirib, kichik tosh bilan katta yukni ham muvozanatlash mumkin.",
        ],
        "chuqur": "Qadimgi bezmen tarozilar aynan shu tamoyilda ishlagan: kichik toshni uzoqroqqa surib, og'irroq yukni o'lchashgan.",
        "tajriba": "Modelning ikki tomoniga turli og'irlikdagi detallar qo'yib, muvozanat holatini topishga harakat qilish.",
        "uyga": "Uyda ikkita turli og'irlikdagi narsani chizg'ich va qalam yordamida muvozanatlashga harakat qiling va natijani yozing.",
    },
    {
        "fokus": "Mexanik yutuq — richag necha marta yordam beradi",
        "savol": "Richag kuchimizni necha marta kuchaytira oladi?",
        "asosiy": [
            "Mexanik yutuq — richag kuchni necha marta oshirishini ko'rsatuvchi son.",
            "U kuch yelkasini yuk yelkasiga bo'lish orqali topiladi (masalan, 60 sm / 20 sm = 3 marta).",
            "Yutuq katta bo'lsa kuch kam sarflanadi, lekin qo'lni uzoqroq harakatlantirish kerak bo'ladi.",
        ],
        "chuqur": "Energiya bekorga paydo bo'lmaydi: kuchdan yutgan narsamizni masofadan yo'qotamiz — bu energiya saqlanishi qonunining ko'rinishi.",
        "tajriba": "Model yelkalarini o'lchab (yoki teshiklarni sanab), taxminiy mexanik yutuqni hisoblash va sinab ko'rish.",
        "uyga": "Uyingizdagi bitta richagli asbobning yelkalarini o'lchab, mexanik yutug'ini taxminan hisoblang.",
    },
]

# ---------------------------------------------------------------------------
# TISHLI G'ILDIRAK (5 ta)
# ---------------------------------------------------------------------------
SUBTOPICS["tishli"] = [
    {
        "fokus": "Tishli g'ildirak va tishlarning ulanishi",
        "savol": "Nima uchun tishli g'ildiraklarda tishchalar bor?",
        "asosiy": [
            "Tishli g'ildirak — chetida tishchalari bo'lgan aylanuvchi detal.",
            "Tishchalar bir-biriga kirib, sirg'almasdan harakatni uzatadi.",
            "Silliq g'ildiraklar sirg'anib ketishi mumkin, tishlilar esa aniq ishlaydi.",
        ],
        "chuqur": "Tishlarning shakli maxsus hisoblangan — ular tekis va shovqinsiz kirishishi uchun.",
        "tajriba": "Ikkita tishlini qo'lda ulab, birini aylantirib, ikkinchisining ham aylanishini kuzatish.",
        "uyga": "Uyda tishli g'ildirak ishlatiladigan narsani toping (velosiped, soat) va nechta tishlisi borligini kuzating.",
    },
    {
        "fokus": "Katta va kichik g'ildirak — tezlik farqi",
        "savol": "Katta g'ildirak tezroq aylanadimi yoki kichigi?",
        "asosiy": [
            "Kichik g'ildirak ko'proq aylanadi — u tezroq.",
            "Katta g'ildirak sekinroq aylanadi, lekin ko'proq kuch beradi.",
            "Demak tishli uzatma tezlikni kuchga, kuchni tezlikka almashtira oladi.",
        ],
        "chuqur": "Bu almashinuv bekorga emas: tezlikdan yutsak kuchdan yo'qotamiz va aksincha.",
        "tajriba": "Kichik g'ildirakni bir marta aylantirib, katta g'ildirak necha marta aylanishini sanash.",
        "uyga": "Velosipedda \"yengil\" va \"og'ir\" uzatma qachon ishlatilishini (qiyalikka chiqishda yoki tekis yo'lda) yozing.",
    },
    {
        "fokus": "Aylanish yo'nalishi",
        "savol": "Ikki tishli ulanganda ikkalasi ham bir tomonga aylanadimi?",
        "asosiy": [
            "Ulangan ikki tishli g'ildirak QARAMA-QARSHI tomonga aylanadi.",
            "Uchinchi g'ildirak qo'shilsa, birinchi va uchinchisi bir tomonga aylanadi.",
            "Kerakli yo'nalishni olish uchun g'ildiraklar sonini tanlash mumkin.",
        ],
        "chuqur": "O'rtaga qo'yiladigan qo'shimcha g'ildirak (idler gear) faqat yo'nalishni o'zgartiradi, tezlikka ta'sir qilmaydi.",
        "tajriba": "Uch tishlini ketma-ket ulab, birinchisini aylantirish va har birining yo'nalishini strelka bilan belgilash.",
        "uyga": "Ikki va uch tishli g'ildirak ulanishini chizib, har birining aylanish yo'nalishini strelka bilan ko'rsating.",
    },
    {
        "fokus": "Uzatma nisbati — tishlarni sanash",
        "savol": "Bir g'ildirak ikkinchisidan necha marta tez aylanishini oldindan bilish mumkinmi?",
        "asosiy": [
            "Uzatma nisbati — ikki g'ildirak tishlari sonining nisbati.",
            "Masalan 24 tishli va 8 tishli bo'lsa, nisbat 3:1 — kichigi 3 marta tez aylanadi.",
            "Tishlarni sanab, natijani oldindan bashorat qilish mumkin.",
        ],
        "chuqur": "Uzatma nisbati moment (kuch) uchun teskari ishlaydi: tezlik 3 marta oshsa, moment 3 marta kamayadi.",
        "tajriba": "Modeldagi ikkala g'ildirakning tishlarini sanab, nisbatni hisoblash va aylantirib tekshirish.",
        "uyga": "Ikki tishli g'ildirak rasmini chizib, tishlar sonini yozing va uzatma nisbatini hisoblang.",
    },
    {
        "fokus": "Uzatma zanjiri (bir necha g'ildirak ketma-ket)",
        "savol": "Bir nechta tishlini ketma-ket ulasak nima bo'ladi?",
        "asosiy": [
            "Bir nechta g'ildirak ketma-ket ulansa, uzatma zanjiri hosil bo'ladi.",
            "Har bir bosqichda tezlik yoki kuch yana o'zgaradi.",
            "Shu yo'l bilan juda katta tezlik farqiga erishish mumkin.",
        ],
        "chuqur": "Kompound uzatmada umumiy nisbat har bir bosqich nisbatlarining ko'paytmasiga teng (masalan 3:1 va 2:1 = 6:1).",
        "tajriba": "Uch-to'rt g'ildirakli zanjirni aylantirib, boshi va oxiridagi tezlik farqini kuzatish.",
        "uyga": "Soat ichida nima uchun ko'p tishli g'ildirak borligini o'ylab, taxminingizni yozing.",
    },
]

# ---------------------------------------------------------------------------
# SHKIV (2 ta)
# ---------------------------------------------------------------------------
SUBTOPICS["shkiv"] = [
    {
        "fokus": "Shkiv kuch yo'nalishini o'zgartiradi",
        "savol": "Bayroqni yuqoriga ko'tarish uchun arqonni qaysi tomonga tortamiz?",
        "asosiy": [
            "Shkiv — tros yoki tasma o'tadigan aylanuvchi g'ildirak.",
            "Tros shkiv ustidan o'tsa, pastga tortganda yuk yuqoriga ko'tariladi.",
            "Ya'ni shkiv kuchning YO'NALISHINI o'zgartiradi.",
        ],
        "chuqur": "Bitta qo'zg'almas shkiv kuchni kamaytirmaydi — u faqat qulaylik uchun yo'nalishni o'zgartiradi.",
        "tajriba": "Trosni pastga tortib, yukning yuqoriga chiqishini kuzatish va kuch qanchalik kerakligini his qilish.",
        "uyga": "Bayroq ustuni yoki parda mexanizmini kuzatib, shkiv qayerda joylashganini chizing.",
    },
    {
        "fokus": "Bir nechta shkiv — kuchni kamaytirish",
        "savol": "Og'ir yukni yanada osonroq ko'tarishning yo'li bormi?",
        "asosiy": [
            "Bir nechta shkiv birga ishlatilsa, kerakli tortish kuchi kamayadi.",
            "Ikki shkiv bilan yukning yarmi kuch bilan ko'tarish mumkin.",
            "Lekin buning evaziga trosni ikki barobar uzunroq tortish kerak bo'ladi.",
        ],
        "chuqur": "Mexanik yutuq shkivlar soniga teng bo'ladi — bu \"block and tackle\" tizimi deb ataladi.",
        "tajriba": "Bir shkivli va ikki shkivli variantda bir xil yukni ko'tarib, kuch farqini taqqoslash.",
        "uyga": "Qurilish kranida nechta shkiv borligini rasmdan sanab ko'ring va nima uchun ko'p ekanini yozing.",
    },
]

# ---------------------------------------------------------------------------
# KRIVOSHIP / AYLANMA -> TEBRANMA (18 ta)
# ---------------------------------------------------------------------------
SUBTOPICS["krivoship"] = [
    {
        "fokus": "Aylanma va tebranma harakat farqi",
        "savol": "Velosiped pedali aylanadi, lekin tizza qanday harakat qiladi?",
        "asosiy": [
            "Aylanma harakat — doira bo'ylab to'xtovsiz aylanish.",
            "Tebranma harakat — oldinga-orqaga yoki yuqoriga-pastga qaytariluvchi harakat.",
            "Mexanizm aylanma harakatni tebranmaga aylantira oladi.",
        ],
        "chuqur": "Aylanma harakat cheksiz davom etadi, tebranma harakat esa chegaralangan — u har safar qaytadi.",
        "tajriba": "Motorni (yoki dastakni) aylantirib, modelning qaysi qismi aylanishini va qaysi qismi tebranishini aniqlash.",
        "uyga": "Uyda aylanma va tebranma harakat qiladigan bittadan narsa toping va yozing.",
    },
    {
        "fokus": "Mexanizm qismlari: krivoship va shatun",
        "savol": "Aylanuvchi qismni tebranuvchi qismga nima bog'laydi?",
        "asosiy": [
            "Krivoship — aylanadigan qism (motor unga ulanadi).",
            "Shatun — krivoshipni tebranuvchi qismga bog'lovchi tayoqcha.",
            "Shatun aylanma harakatni \"tortib-itarib\" tebranishga aylantiradi.",
        ],
        "chuqur": "Shatunning ikkala uchi ham erkin aylanadigan bo'g'in bilan biriktiriladi — shuning uchun mexanizm tiqilib qolmaydi.",
        "tajriba": "Modeldagi krivoship va shatunni aniqlab, shatunni barmoq bilan kuzatib borish.",
        "uyga": "Krivoship va shatunni chizib, har birini nomlab belgilang.",
    },
    {
        "fokus": "Krivoship radiusi va tebranish kengligi",
        "savol": "Tebranish kengligini qanday qilib kattalashtirish mumkin?",
        "asosiy": [
            "Krivoship radiusi — aylanish markazidan shatun ulangan nuqtagacha bo'lgan masofa.",
            "Radius katta bo'lsa, tebranish ham keng bo'ladi.",
            "Radius kichik bo'lsa, harakat mayda va tez-tez bo'ladi.",
        ],
        "chuqur": "Tebranish amplitudasi krivoship radiusining taxminan ikki barobariga teng bo'ladi.",
        "tajriba": "Iloji bo'lsa shatunni krivoshipning boshqa teshigiga ko'chirib, tebranish kengligi qanday o'zgarishini kuzatish.",
        "uyga": "Kichik va katta radiusli krivoshipni chizib, qaysi biri kengroq harakat berishini belgilang.",
    },
    {
        "fokus": "Shatun uzunligining ta'siri",
        "savol": "Shatunni uzunroq qilsak, harakat o'zgaradimi?",
        "asosiy": [
            "Shatun uzunligi tebranish kengligini deyarli o'zgartirmaydi.",
            "Lekin uzun shatun harakatni silliqroq va tekisroq qiladi.",
            "Kalta shatunda harakat keskinroq va notekis bo'ladi.",
        ],
        "chuqur": "Kalta shatunda tebranishning borish va qaytish tezligi teng bo'lmaydi — bu real dvigatellarda hisobga olinadi.",
        "tajriba": "Mexanizmni sekin aylantirib, harakatning borish va qaytish tezligi bir xilmi yoki yo'qmi kuzatish.",
        "uyga": "Uzun va kalta shatunli mexanizmni chizib, qaysi biri silliqroq ishlashini belgilang.",
    },
    {
        "fokus": "Yuqoriga-pastga tebranish (vertikal)",
        "savol": "Bolg'a uradigan mexanizm qanday ishlaydi?",
        "asosiy": [
            "Krivoship gorizontal aylansa ham, mexanizm harakatni vertikalga burishi mumkin.",
            "Bunday harakat urish, bosish, tuyish ishlarida ishlatiladi.",
            "Har aylanishda qism bir marta yuqoriga chiqib, bir marta pastga tushadi.",
        ],
        "chuqur": "Vertikal tebranishda og'irlik kuchi ham ta'sir qiladi — pastga tushish yuqoriga chiqishdan osonroq bo'ladi.",
        "tajriba": "Mexanizmni aylantirib, yuqoriga-pastga harakatlanadigan qismni kuzatish va bir aylanishda necha marta urishini sanash.",
        "uyga": "Yuqoriga-pastga harakat qiladigan mexanizmga (bolg'a, tuyish) 1 ta misol toping va chizing.",
    },
    {
        "fokus": "Oldinga-orqaga tebranish (gorizontal)",
        "savol": "Arra yoki supurgi qanday harakat qiladi?",
        "asosiy": [
            "Krivoship harakatni gorizontal (yon tomonlarga) tebranishga ham aylantira oladi.",
            "Bunday harakat arralash, supurish, silash ishlarida ishlatiladi.",
            "Yo'nalish mexanizmning joylashuviga bog'liq.",
        ],
        "chuqur": "Bir xil krivoshipdan vertikal yoki gorizontal harakat olish — mexanizmni qanday o'rnatishga bog'liq.",
        "tajriba": "Modeldagi gorizontal tebranuvchi qismning bir tomondan ikkinchi tomonga qancha masofa bosishini kuzatish.",
        "uyga": "Oldinga-orqaga harakat qiladigan mexanizmga (arra, supurgi) 1 ta misol toping va chizing.",
    },
    {
        "fokus": "Sakrash harakati qanday hosil bo'ladi",
        "savol": "Robot qanday qilib sakraydi?",
        "asosiy": [
            "Sakrash — qismning tez yuqoriga itarilishi va keyin tushishi.",
            "Krivoship qismni tez ko'tarib, keyin birdan qo'yib yuboradi.",
            "Tez harakat sakrash effektini beradi.",
        ],
        "chuqur": "Sakrash uchun harakat tez bo'lishi kerak — sekin ko'tarilsa jism shunchaki ko'tariladi, sakramaydi.",
        "tajriba": "Mexanizmni avval sekin, keyin tez aylantirib, sakrash qachon yaqqol ko'rinishini kuzatish.",
        "uyga": "Sakraydigan hayvonni (quyon, chumchuq) kuzatib, u sakrashdan oldin nima qilishini yozing.",
    },
    {
        "fokus": "Chayqalish (tebranib turish) harakati",
        "savol": "Beshik yoki chayqaluvchi kursi qanday harakat qiladi?",
        "asosiy": [
            "Chayqalish — jismning bir tomondan ikkinchi tomonga sekin og'ishi.",
            "Bu harakat yumshoq va bir maromda bo'ladi.",
            "Krivoship radiusi kichik bo'lsa, chayqalish nozik chiqadi.",
        ],
        "chuqur": "Chayqalish harakatida jismning og'irlik markazi ham u yoqdan-bu yoqqa siljiydi.",
        "tajriba": "Mexanizmni bir maromda aylantirib, chayqalish qanchalik tekis chiqayotganini kuzatish.",
        "uyga": "Chayqaluvchi narsani (beshik, arg'imchoq) kuzatib, u bir daqiqada necha marta chayqalishini sanang.",
    },
    {
        "fokus": "Harakat sikli — bir to'liq aylanish",
        "savol": "Krivoship bir marta aylanganda tebranuvchi qism nima qiladi?",
        "asosiy": [
            "Sikl — harakatning bir marta to'liq takrorlanishi.",
            "Krivoship bir marta aylansa, tebranuvchi qism bir marta borib-qaytadi.",
            "Shuning uchun mexanizm harakati muntazam va bashoratli bo'ladi.",
        ],
        "chuqur": "Bir sikl davomida qism ikki marta eng chekka nuqtaga yetadi — boshida va o'rtasida.",
        "tajriba": "Krivoshipga belgi qo'yib, uni aynan bir marta aylantirish va tebranuvchi qism nechta harakat qilishini sanash.",
        "uyga": "Bir siklda nima sodir bo'lishini bosqichma-bosqich (1, 2, 3) chizib ko'rsating.",
    },
    {
        "fokus": "Motor tezligi va tebranish tezligi",
        "savol": "Motorni tezroq aylantirsak, harakat qanday o'zgaradi?",
        "asosiy": [
            "Motor tez aylansa, tebranish ham tez-tez bo'ladi.",
            "Lekin tebranish KENGLIGI o'zgarmaydi — u faqat krivoship radiusiga bog'liq.",
            "Demak tezlik va kenglik alohida boshqariladi.",
        ],
        "chuqur": "Tezlik (chastota) va kenglik (amplituda) — tebranishning ikki mustaqil xususiyati.",
        "tajriba": "Motor tezligini o'zgartirib, tebranish tez-tezligi o'zgarsa ham kengligi o'zgarmasligini tekshirish.",
        "uyga": "Tez va sekin tebranadigan narsalarni (soat mayatnigi, ventilyator) taqqoslab yozing.",
    },
    {
        "fokus": "Ikki mexanizm birga — navbatma-navbat harakat",
        "savol": "Robotning ikki oyog'i qanday qilib navbat bilan qadam tashlaydi?",
        "asosiy": [
            "Ikki krivoship bir-biriga nisbatan burilib o'rnatilsa, ular navbat bilan harakat qiladi.",
            "Biri yuqorida bo'lganda ikkinchisi pastda bo'ladi.",
            "Shu tufayli yurish harakati tabiiy ko'rinadi.",
        ],
        "chuqur": "Bu \"faza farqi\" deb ataladi — ikki mexanizm bir xil ishlaydi, lekin vaqt bo'yicha siljigan holda.",
        "tajriba": "Modeldagi ikki tomon harakatini kuzatib, ular bir vaqtda emas, navbat bilan ishlashini tekshirish.",
        "uyga": "O'z yurishingizni kuzatib, oyoqlaringiz bir vaqtda harakat qiladimi yoki navbat bilanmi — yozing.",
    },
    {
        "fokus": "Harakat trayektoriyasi — nuqta qanday yo'l chizadi",
        "savol": "Mexanizmning uchidagi nuqta havoda qanday shakl chizadi?",
        "asosiy": [
            "Mexanizmning har bir nuqtasi o'ziga xos yo'l (trayektoriya) chizadi.",
            "Krivoshipdagi nuqta doira chizadi, tebranuvchi uchidagi nuqta esa yoy yoki chiziq chizadi.",
            "Muhandislar kerakli yo'lni olish uchun mexanizmni maxsus loyihalaydi.",
        ],
        "chuqur": "Murakkab bo'g'inlar yordamida deyarli to'g'ri chiziq yoki maxsus shakldagi trayektoriya olish mumkin.",
        "tajriba": "Mexanizmni sekin aylantirib, tanlangan nuqta qanday shakl chizishini havoda barmoq bilan kuzatib borish.",
        "uyga": "Mexanizmning bir nuqtasi chizadigan yo'lni qog'ozga taxminan chizib ko'ring.",
    },
    {
        "fokus": "O'lik nuqta — mexanizm nega tiqilib qoladi",
        "savol": "Nega ba'zan mexanizm boshlanmay turib qoladi?",
        "asosiy": [
            "O'lik nuqta — krivoship va shatun bir chiziqda bo'lgan holat.",
            "Bu holatda itaruvchi kuch aylantira olmaydi, mexanizm tiqilib qoladi.",
            "Uni qo'l bilan biroz surib qo'yish yetarli.",
        ],
        "chuqur": "Real dvigatellarda o'lik nuqtani o'tish uchun og'ir g'ildirak (mayovik) ishlatiladi — u inersiya bilan o'tkazib yuboradi.",
        "tajriba": "Mexanizmni o'lik nuqtaga qo'yib, uni aylantirishga harakat qilish va nega qiyin ekanini kuzatish.",
        "uyga": "Nega poyezd g'ildiraklarida shatunlar turli burchakda o'rnatilganini o'ylab, taxminingizni yozing.",
    },
    {
        "fokus": "Kulachok (cam) — muqobil mexanizm",
        "savol": "Aylanma harakatni tebranishga aylantirishning boshqa yo'li bormi?",
        "asosiy": [
            "Kulachok — notekis shakldagi aylanuvchi detal.",
            "Uning ustidan yurgan qism ko'tarilib-tushadi.",
            "Kulachok shaklini o'zgartirib, istalgan harakat naqshini olish mumkin.",
        ],
        "chuqur": "Krivoship har doim silliq tebranish beradi, kulachok esa keskin, sakrashli harakat ham bera oladi.",
        "tajriba": "Agar modelda kulachokka o'xshash notekis detal bo'lsa, uni aylantirib harakat naqshini kuzatish.",
        "uyga": "Notekis shaklli kulachok chizib, u ustidan yurgan qism qanday harakat qilishini strelka bilan ko'rsating.",
    },
    {
        "fokus": "To'rt bo'g'inli mexanizm",
        "savol": "Bir necha tayoqcha birlashsa qanday harakat chiqadi?",
        "asosiy": [
            "To'rt bo'g'inli mexanizm — to'rtta qattiq qism bo'g'inlar bilan bog'langan tizim.",
            "Bir qismni harakatlantirsak, qolganlari ma'lum yo'l bo'ylab harakat qiladi.",
            "Bu mexanizm ko'plab mashinalarda uchraydi.",
        ],
        "chuqur": "Bo'g'inlar uzunligini o'zgartirib, mexanizmni to'liq aylanuvchi yoki faqat tebranuvchi qilish mumkin.",
        "tajriba": "Modeldagi bo'g'inlarni sanab, ular qanday bog'langanini kuzatish.",
        "uyga": "To'rt tayoqchali mexanizm chizib, qaysi biri harakatlantiruvchi ekanini belgilang.",
    },
    {
        "fokus": "Muvozanatlash — tebranish silliq bo'lishi uchun",
        "savol": "Nega ba'zi mexanizmlar ishlaganda qattiq titraydi?",
        "asosiy": [
            "Tez tebranuvchi qism mexanizmni silkitadi.",
            "Qarama-qarshi tomonga og'irlik qo'yilsa, titrash kamayadi.",
            "Bu muvozanatlash (balanslash) deb ataladi.",
        ],
        "chuqur": "Real dvigatellarda maxsus qarshi og'irliklar (kontr-vaznlar) shu maqsadda o'rnatiladi.",
        "tajriba": "Mexanizmni tez ishlatib, model titrayaptimi yoki yo'qmi kuzatish; iloji bo'lsa mahkamroq ushlab sinash.",
        "uyga": "Kir yuvish mashinasi tez aylanganda nega silkinishini o'ylab, taxminingizni yozing.",
    },
    {
        "fokus": "Harakatni kuchaytirish (richag bilan birga)",
        "savol": "Kichik tebranishni kattaroq qilish mumkinmi?",
        "asosiy": [
            "Tebranuvchi qismga richag qo'shilsa, harakat kattalashadi.",
            "Richagning uzun tomoni ko'proq masofa bosadi.",
            "Lekin kuch shunga yarasha kamayadi.",
        ],
        "chuqur": "Krivoship + richag kombinatsiyasi mexanizmga ikki bosqichli sozlash imkonini beradi.",
        "tajriba": "Mexanizmning tayanchga yaqin va uzoq nuqtalari qancha masofa bosishini taqqoslash.",
        "uyga": "Kichik harakatni kattalashtiradigan mexanizm chizib, qaysi qism ko'proq harakat qilishini belgilang.",
    },
    {
        "fokus": "Real dvigatel bilan solishtirish",
        "savol": "Mashina dvigateli ichida nima aylanadi?",
        "asosiy": [
            "Dvigatelda porshen yuqoriga-pastga harakat qiladi.",
            "Krivoship-shatun mexanizmi buni g'ildirak aylanishiga aylantiradi.",
            "Ya'ni mexanizm teskari tomonga ham ishlay oladi.",
        ],
        "chuqur": "Bizning modelda aylanish tebranishga aylanadi, dvigatelda esa tebranish aylanishga — bir xil mexanizm, teskari yo'nalishda.",
        "tajriba": "Tebranuvchi qismni qo'l bilan itarib, krivoshipning aylanishini kuzatish (teskari yo'nalish).",
        "uyga": "Dvigatel porsheni va krivoship qanday bog'langanini rasm orqali o'rganib, chizib keling.",
    },
    {
        "fokus": "Harakatni to'xtatish va boshlash",
        "savol": "Mexanizmni istalgan joyda to'xtatish mumkinmi?",
        "asosiy": [
            "Motor to'xtaganda mexanizm istalgan holatda qolishi mumkin.",
            "Ba'zi holatlarda qayta boshlash qiyinroq bo'ladi.",
            "Shuning uchun boshlanish holatini o'ylab tanlash kerak.",
        ],
        "chuqur": "Dasturda mexanizmni har doim bir xil holatdan boshlash uni bashoratli qiladi.",
        "tajriba": "Mexanizmni turli holatlarda to'xtatib, qaysi holatdan qayta boshlash oson ekanini aniqlash.",
        "uyga": "Mexanizm qaysi holatda to'xtasa yaxshi bo'lishini chizib ko'rsating.",
    },
    {
        "fokus": "Bir motordan bir necha harakat",
        "savol": "Bitta motor bilan bir nechta qismni harakatlantirish mumkinmi?",
        "asosiy": [
            "Bitta motorga bir nechta mexanizm ulanishi mumkin.",
            "Ular bir vaqtda, lekin turlicha harakat qiladi.",
            "Bu detal va energiyani tejaydi.",
        ],
        "chuqur": "Bir manbadan bir necha harakat olish — muhandislikda \"mexanizmni taqsimlash\" deb ataladi.",
        "tajriba": "Modelda bitta motordan nechta qism harakat olayotganini sanash.",
        "uyga": "Bitta motor bilan 2 ta turli harakat beradigan g'oyani chizib ko'rsating.",
    },
    {
        "fokus": "Harakat kuchi va qarshilik",
        "savol": "Mexanizmga to'siq bo'lsa nima bo'ladi?",
        "asosiy": [
            "Tebranuvchi qismga qarshilik bo'lsa, mexanizm sekinlashadi.",
            "Kuchli qarshilik motorni to'xtatishi mumkin.",
            "Shuning uchun mexanizm erkin harakatlanishi kerak.",
        ],
        "chuqur": "Qarshilik ortganda motor ko'proq tok tortadi va tez qiziydi.",
        "tajriba": "Tebranuvchi qismni barmoq bilan yengil ushlab, mexanizm sekinlashganini kuzatish.",
        "uyga": "Mexanizm erkin harakatlanishi uchun nimaga e'tibor berish kerakligini yozing.",
    },
    {
        "fokus": "Mexanizm bo'g'inlaridagi bo'shliq",
        "savol": "Nega ba'zi mexanizmlar \"qaltiraydi\"?",
        "asosiy": [
            "Bo'g'inlarda ortiqcha bo'shliq bo'lsa, harakat aniq bo'lmaydi.",
            "Qismlar bir-biriga urilib, shovqin chiqadi.",
            "Mahkam va aniq yig'ish buni oldini oladi.",
        ],
        "chuqur": "Bo'shliq (lyuft) mexanizm aniqligini kamaytiradi — bu robototexnikada muhim muammo.",
        "tajriba": "Mexanizm bo'g'inlarini qo'l bilan qimirlatib, bo'shliq bor-yo'qligini tekshirish.",
        "uyga": "Bo'shliq nima uchun zararli ekanini o'z so'zingiz bilan tushuntiring.",
    },
    {
        "fokus": "Tebranishning tekisligi",
        "savol": "Harakat bir maromda bo'lishi uchun nima kerak?",
        "asosiy": [
            "Mexanizm silliq ishlashi uchun qismlar erkin aylanishi kerak.",
            "Motor tezligi ham bir xil bo'lishi kerak.",
            "Aks holda harakat sakrab-sakrab chiqadi.",
        ],
        "chuqur": "Og'ir aylanuvchi qism (mayovik) tezlik o'zgarishini tekislaydi.",
        "tajriba": "Mexanizmni ishlatib, harakat tekismi yoki sakrab chiqayotganini kuzatish.",
        "uyga": "Tekis va notekis harakatga bittadan misol yozing.",
    },
    {
        "fokus": "Mexanizm o'lchamini o'zgartirish",
        "savol": "Mexanizmni kattalashtirsak, u xuddi shunday ishlaydimi?",
        "asosiy": [
            "Mexanizmning barcha qismlari mutanosib kattalashsa, harakat o'xshash bo'ladi.",
            "Lekin og'irlik ancha ortadi.",
            "Katta mexanizm ko'proq kuch talab qiladi.",
        ],
        "chuqur": "O'lcham ikki barobar oshsa, og'irlik sakkiz barobar ortadi — shuning uchun katta mexanizmlar boshqacha loyihalanadi.",
        "tajriba": "Mexanizmning kichik va katta qismlarini taqqoslab, qaysi biri oson harakatlanishini kuzatish.",
        "uyga": "Kichik va katta mexanizmga bittadan misol yozing.",
    },
    {
        "fokus": "Harakatni sanash",
        "savol": "Mexanizm bir daqiqada necha marta harakat qiladi?",
        "asosiy": [
            "Harakat sonini sanash mumkin.",
            "Bir daqiqadagi harakat soni mexanizm tezligini bildiradi.",
            "Motor tezligi o'zgarsa, bu son ham o'zgaradi.",
        ],
        "chuqur": "Bir daqiqadagi takrorlanish soni \"chastota\" deb ataladi.",
        "tajriba": "Mexanizm 30 soniyada necha marta harakat qilishini sanab, bir daqiqaga hisoblash.",
        "uyga": "Mexanizmingiz bir daqiqada necha marta harakat qilishini sanab yozing.",
    },
    {
        "fokus": "Mexanizmni mustahkamlash",
        "savol": "Tez ishlaganda mexanizm nega buziladi?",
        "asosiy": [
            "Tez harakatda qismlarga katta kuch tushadi.",
            "Zaif joylar birinchi bo'lib ajraladi.",
            "Ularni qo'shimcha detal bilan mustahkamlash kerak.",
        ],
        "chuqur": "Takroriy yuklanish materialni asta-sekin charchatadi — bu \"charchoq buzilishi\" deb ataladi.",
        "tajriba": "Mexanizmni bir necha daqiqa ishlatib, qaysi qism bo'shashganini aniqlash.",
        "uyga": "Mexanizmingizning eng zaif joyini topib, uni qanday mustahkamlash mumkinligini yozing.",
    },
    {
        "fokus": "Ikki tomonlama harakat",
        "savol": "Mexanizm ikkala yo'nalishda ham ishlay oladimi?",
        "asosiy": [
            "Ko'p mexanizmlar ikkala yo'nalishda ishlay oladi.",
            "Motor teskari aylansa, harakat ham teskari bo'ladi.",
            "Lekin ba'zi mexanizmlar faqat bir tomonga mo'ljallangan.",
        ],
        "chuqur": "Faqat bir tomonga ishlaydigan mexanizmlarda maxsus tishcha (храповик) bo'ladi.",
        "tajriba": "Motorni teskari aylantirib, mexanizm harakati qanday o'zgarishini kuzatish.",
        "uyga": "Faqat bir tomonga aylanadigan mexanizmga misol toping (masalan, velosiped pedali).",
    },
    {
        "fokus": "Mexanizm shovqini",
        "savol": "Nega ba'zi mexanizmlar shovqin qiladi?",
        "asosiy": [
            "Qismlar bir-biriga urilganda shovqin chiqadi.",
            "Bo'shliq va notekis harakat shovqinni oshiradi.",
            "Silliq harakat kam shovqinli bo'ladi.",
        ],
        "chuqur": "Shovqin — energiya yo'qotilishining belgisi; jim ishlaydigan mexanizm odatda samaraliroq.",
        "tajriba": "Mexanizmni ishlatib, shovqin qaysi qismdan kelayotganini aniqlash.",
        "uyga": "Shovqinli va jim ishlaydigan bittadan qurilma yozing.",
    },
    {
        "fokus": "Harakatni ko'zdan kechirish (sekin rejim)",
        "savol": "Tez harakatni qanday o'rganish mumkin?",
        "asosiy": [
            "Tez harakatni ko'z ilg'ay olmaydi.",
            "Mexanizmni qo'lda sekin aylantirsak, hammasi ko'rinadi.",
            "Muhandislar ham shunday tekshiradi.",
        ],
        "chuqur": "Zamonaviy muhandislikda tez harakatni o'rganish uchun yuqori tezlikdagi kamera ishlatiladi.",
        "tajriba": "Mexanizmni juda sekin aylantirib, har bir bosqichni alohida kuzatish.",
        "uyga": "Sekin va tez harakatni kuzatishda qanday farq borligini yozing.",
    },
    {
        "fokus": "Mexanizmni loyihalash tartibi",
        "savol": "Yangi mexanizm yaratishni qayerdan boshlash kerak?",
        "asosiy": [
            "Avval qanday harakat kerakligini aniqlash kerak.",
            "Keyin shunga mos mexanizm tanlanadi.",
            "Oxirida sinab, kerak bo'lsa tuzatiladi.",
        ],
        "chuqur": "Muhandislik dizayni jarayoni: talab -> g'oya -> qurish -> sinov -> takomillashtirish.",
        "tajriba": "Modelning qanday harakat berishi kerakligini aytib, uning mexanizmi shunga mosligini tekshirish.",
        "uyga": "O'zingiz istagan harakatni tanlab, unga qanday mexanizm kerakligini yozing.",
    },
    {
        "fokus": "Mexanizmlarni birlashtirish",
        "savol": "Ikki xil mexanizmni birga ishlatish mumkinmi?",
        "asosiy": [
            "Krivoship va tishli g'ildirakni birga ishlatish mumkin.",
            "Har biri o'z vazifasini bajaradi.",
            "Natijada murakkabroq harakat hosil bo'ladi.",
        ],
        "chuqur": "Murakkab mashinalar oddiy mexanizmlarning ketma-ket ulangan zanjiridan iborat.",
        "tajriba": "Modeldagi barcha mexanizm turlarini sanab, ular qanday bog'langanini aniqlash.",
        "uyga": "Ikki xil mexanizm birga ishlaydigan qurilma chizing.",
    },
    {
        "fokus": "Harakat va vaqt bog'liqligi",
        "savol": "Mexanizm bir sikl uchun qancha vaqt sarflaydi?",
        "asosiy": [
            "Har bir sikl ma'lum vaqt oladi.",
            "Motor tez bo'lsa, sikl vaqti qisqaradi.",
            "Sikl vaqtini bilsak, harakatni rejalashtira olamiz.",
        ],
        "chuqur": "Sikl vaqti chastotaga teskari: chastota ikki barobar oshsa, sikl vaqti ikki barobar qisqaradi.",
        "tajriba": "Sekundomer bilan bir sikl qancha vaqt olishini o'lchash.",
        "uyga": "Mexanizmingizning bir sikli qancha vaqt olishini o'lchab yozing.",
    },
    {
        "fokus": "Mexanizm harakatini oldindan aytish",
        "savol": "Mexanizmni ishlatmasdan turib, u qanday harakat qilishini bilish mumkinmi?",
        "asosiy": [
            "Mexanizm tuzilishiga qarab harakatini oldindan taxmin qilish mumkin.",
            "Krivoship radiusi va bo'g'inlar joylashuvi natijani belgilaydi.",
            "Muhandis qurishdan oldin natijani bashorat qiladi.",
        ],
        "chuqur": "Bashorat qilish qobiliyati muhandislikning asosi — u vaqt va materialni tejaydi.",
        "tajriba": "Mexanizmni ishlatishdan oldin natijani taxmin qilib, keyin sinab tekshirish.",
        "uyga": "Mexanizmingiz qanday harakat qilishini oldindan yozib, keyin tekshirib ko'ring.",
    },
    {
        "fokus": "Mexanizmni takomillashtirish",
        "savol": "Ishlab turgan mexanizmni yanada yaxshilash mumkinmi?",
        "asosiy": [
            "Har qanday mexanizmni yaxshilash mumkin.",
            "Silliqroq, tezroq yoki jimroq qilish yo'llari bor.",
            "Muhandis doim yaxshilash yo'lini izlaydi.",
        ],
        "chuqur": "Takomillashtirish — bir marta emas, doimiy jarayon; har sinov yangi g'oya beradi.",
        "tajriba": "Mexanizmda bitta narsani o'zgartirib, natija yaxshilanganini tekshirish.",
        "uyga": "Mexanizmingizni yaxshilash uchun 2 ta g'oya yozing.",
    },
]

# ---------------------------------------------------------------------------
# MUVOZANAT (4 ta)
# ---------------------------------------------------------------------------
SUBTOPICS["muvozanat"] = [
    {
        "fokus": "Og'irlik markazi nima",
        "savol": "Nega ba'zi narsalar turg'un turadi, ba'zilari yiqiladi?",
        "asosiy": [
            "Og'irlik markazi — jismning \"eng og'ir\" nuqtasi kabi tasavvur qilinadigan joy.",
            "U tayanch ustida bo'lsa, jism turadi.",
            "U tayanchdan chiqib ketsa, jism yiqiladi.",
        ],
        "chuqur": "Og'irlik markazi jismning ichida bo'lishi shart emas — masalan, halqada u markazdagi bo'shliqda joylashadi.",
        "tajriba": "Modelni barmoq ustida muvozanatlashga harakat qilib, og'irlik markazi qayerdaligini topish.",
        "uyga": "Chizg'ichni barmog'ingiz ustida muvozanatlab, u qaysi nuqtada turishini belgilang.",
    },
    {
        "fokus": "Tayanch maydoni kengligi",
        "savol": "Nega keng oyoqli stol mustahkamroq turadi?",
        "asosiy": [
            "Tayanch maydoni — jism yerga tegib turgan hudud.",
            "Maydon keng bo'lsa, jism barqarorroq bo'ladi.",
            "Tor tayanchli jism oson ag'dariladi.",
        ],
        "chuqur": "Og'irlik markazi tayanch maydonidan chiqqan zahoti ag'darilish boshlanadi.",
        "tajriba": "Modelni asta qiyshaytirib, u qaysi burchakda yiqila boshlashini kuzatish.",
        "uyga": "Keng va tor tayanchli 2 ta narsani taqqoslab, qaysi biri barqarorroq ekanini yozing.",
    },
    {
        "fokus": "Balandlik va barqarorlik",
        "savol": "Baland minora nega osonroq yiqiladi?",
        "asosiy": [
            "Jism baland bo'lsa, og'irlik markazi ham baland bo'ladi.",
            "Baland og'irlik markazi jismni beqaror qiladi.",
            "Pastroq va og'irroq asos barqarorlikni oshiradi.",
        ],
        "chuqur": "Shuning uchun poyga mashinalari past qilib yasaladi — burilishda ag'darilmasligi uchun.",
        "tajriba": "Modelning tepasiga qo'shimcha detal qo'yib, u barqarorlikni qanday o'zgartirishini sinash.",
        "uyga": "Baland va past narsalarni turtib ko'rib (ehtiyotkorlik bilan), qaysi biri oson yiqilishini yozing.",
    },
    {
        "fokus": "Tebranuvchi muvozanat",
        "savol": "Arg'imchoq nega o'z-o'zidan to'xtaydi?",
        "asosiy": [
            "Ba'zi jismlar muvozanat holati atrofida tebranadi.",
            "Ular har safar muvozanat nuqtasidan o'tib ketadi, keyin qaytadi.",
            "Asta-sekin tebranish susayib, jism muvozanatda to'xtaydi.",
        ],
        "chuqur": "Tebranish ishqalanish va havo qarshiligi tufayli susayadi — energiya asta-sekin yo'qoladi.",
        "tajriba": "Modelni turtib yuborib, u necha marta tebranib to'xtashini sanash.",
        "uyga": "Arg'imchoqni turtib yuborib, u necha marta tebranib to'xtashini sanang va yozing.",
    },
]

# ---------------------------------------------------------------------------
# GEOMETRIYA (10 ta)
# ---------------------------------------------------------------------------
SUBTOPICS["geometriya"] = [
    {
        "fokus": "Uchburchak va to'rtburchak — qaysi mustahkam",
        "savol": "Qaysi shakl bosganda o'z shaklini saqlaydi?",
        "asosiy": [
            "Uchburchak bosganda ham shaklini o'zgartirmaydi — u mustahkam.",
            "To'rtburchak oson egilib, romb shaklga o'tib ketadi.",
            "Shuning uchun qurilishda uchburchak ko'p ishlatiladi.",
        ],
        "chuqur": "Uchburchakning burchaklari tomonlar uzunligi bilan to'liq belgilanadi — boshqa ko'pburchaklarda bunday emas.",
        "tajriba": "Uchburchak va to'rtburchak shaklni qo'lda bosib, qaysi biri egilishini his qilish.",
        "uyga": "Uyda yoki ko'chada uchburchak shakl ishlatilgan 2 ta joyni toping.",
    },
    {
        "fokus": "Diagonal qo'shish",
        "savol": "Egiluvchan to'rtburchakni qanday mustahkamlash mumkin?",
        "asosiy": [
            "To'rtburchakning burchaklarini qiyshiq detal (diagonal) bilan bog'lash mumkin.",
            "Diagonal to'rtburchakni ikkita uchburchakka bo'ladi.",
            "Shundan keyin konstruksiya mustahkam bo'ladi.",
        ],
        "chuqur": "Bitta diagonal yetarli — u shaklning erkin o'zgarishini butunlay to'xtatadi.",
        "tajriba": "To'rtburchak konstruksiyaga diagonal qo'shib, egiluvchanlik yo'qolganini tekshirish.",
        "uyga": "Darvoza yoki panjarada diagonal detal borligini kuzatib, nima uchun kerakligini yozing.",
    },
    {
        "fokus": "Burchaklar va tomonlar bog'liqligi",
        "savol": "Uchburchak tomonlarini o'zgartirsak, burchaklar o'zgaradimi?",
        "asosiy": [
            "Uchburchakda tomonlar uzunligi burchaklarni belgilaydi.",
            "Tomonlarni o'zgartirmasak, burchaklar ham o'zgarmaydi.",
            "Aynan shu xususiyat uchburchakni mustahkam qiladi.",
        ],
        "chuqur": "To'rtburchakda tomonlar bir xil qolsa ham burchaklar erkin o'zgarishi mumkin — shuning uchun u beqaror.",
        "tajriba": "Uchburchak tomonlarini o'zgartirmasdan uning shaklini o'zgartirishga harakat qilish (imkonsizligini ko'rish).",
        "uyga": "Uch xil uzunlikdagi tayoqchalar bilan nechta turli uchburchak yasash mumkinligini o'ylab yozing.",
    },
    {
        "fokus": "Ko'p uchburchakdan konstruksiya (ferma)",
        "savol": "Ko'prik osti nega uchburchaklarga to'la?",
        "asosiy": [
            "Ferma — ko'plab uchburchakdan tuzilgan konstruksiya.",
            "Har bir uchburchak yukning bir qismini ko'taradi.",
            "Shu tufayli ferma juda mustahkam va yengil bo'ladi.",
        ],
        "chuqur": "Fermada ba'zi elementlar cho'ziladi, ba'zilari siqiladi — yuk butun tuzilma bo'ylab taqsimlanadi.",
        "tajriba": "Modeldagi uchburchaklarni sanab, ular konstruksiyaning qaysi qismini mustahkamlayotganini aniqlash.",
        "uyga": "Ko'prik yoki minora rasmini topib, undagi uchburchaklarni sanang.",
    },
    {
        "fokus": "Balandlik va mustahkamlik",
        "savol": "Baland konstruksiyani qanday mustahkam qilish mumkin?",
        "asosiy": [
            "Baland konstruksiya yon tomondan bosganda oson egiladi.",
            "Uni qiyshiq detallar bilan bog'lash kerak.",
            "Asosini kengaytirish ham yordam beradi.",
        ],
        "chuqur": "Baland tuzilmalarda shamol yon tomondan katta kuch beradi — shuning uchun minoralar pastdan keng qilinadi.",
        "tajriba": "Baland qismni yon tomondan asta bosib, u qanchalik egilishini kuzatish.",
        "uyga": "Baland minorani chizib, uni mustahkamlash uchun qayerga qo'shimcha detal qo'yish kerakligini belgilang.",
    },
    {
        "fokus": "Asos kengligi",
        "savol": "Konstruksiya asosini kengaytirsak nima o'zgaradi?",
        "asosiy": [
            "Keng asos konstruksiyani barqaror qiladi.",
            "Tor asosda konstruksiya oson ag'dariladi.",
            "Shuning uchun minoralar pastdan keng bo'ladi.",
        ],
        "chuqur": "Keng asos og'irlik markazining tayanch maydonidan chiqib ketishini qiyinlashtiradi.",
        "tajriba": "Konstruksiyani asta turtib, u qaysi tomonga osonroq ag'darilishini aniqlash.",
        "uyga": "Keng va tor asosli 2 ta bino/minora rasmini solishtiring va farqini yozing.",
    },
    {
        "fokus": "Yopiq va ochiq konstruksiya",
        "savol": "Konstruksiya berk bo'lsa, mustahkamroq bo'ladimi?",
        "asosiy": [
            "Yopiq (berk) konstruksiya har tomondan bog'langan bo'ladi.",
            "Ochiq konstruksiyaning erkin uchlari qimirlaydi.",
            "Yopiq shakl odatda mustahkamroq bo'ladi.",
        ],
        "chuqur": "Yopiq konturda kuch aylanma bo'ylab tarqaladi va bir joyga to'planmaydi.",
        "tajriba": "Konstruksiyaning erkin (bog'lanmagan) uchlarini topib, ularni bog'lash mustahkamlikni oshirishini sinash.",
        "uyga": "Yopiq va ochiq shaklni chizib, qaysi biri mustahkamroq ekanini belgilang.",
    },
    {
        "fokus": "Simmetriya",
        "savol": "Nega ko'p konstruksiyalar ikki tomoni bir xil qilib yasaladi?",
        "asosiy": [
            "Simmetriya — chap va o'ng tomonning bir xil bo'lishi.",
            "Simmetrik konstruksiyada yuk teng taqsimlanadi.",
            "Bu uni barqaror va chiroyli qiladi.",
        ],
        "chuqur": "Nosimmetrik konstruksiyada og'irlik markazi bir tomonga siljiydi va ag'darilish xavfi oshadi.",
        "tajriba": "Modelning chap va o'ng tomonini taqqoslab, ular bir xilmi yoki yo'qmi tekshirish.",
        "uyga": "Simmetrik va nosimmetrik 2 ta narsani toping va chizing.",
    },
    {
        "fokus": "Yuk qayerga tushadi — kuch taqsimoti",
        "savol": "Konstruksiyaga yuk qo'ysak, u qayerga bosim beradi?",
        "asosiy": [
            "Yuk konstruksiya bo'ylab pastga qarab tarqaladi.",
            "Eng ko'p bosim pastki qismlarga tushadi.",
            "Shuning uchun pastki qism mustahkamroq bo'lishi kerak.",
        ],
        "chuqur": "Yuk yo'li (load path) — kuchning yukdan tayanchgacha bo'lgan yo'li; muhandis uni qisqa va to'g'ri qilishga harakat qiladi.",
        "tajriba": "Konstruksiyaning turli joyiga yuk qo'yib, qaysi holatda u mustahkamroq turishini sinash.",
        "uyga": "Konstruksiya chizib, yuk qanday yo'l bilan pastga tushishini strelkalar bilan ko'rsating.",
    },
    {
        "fokus": "Kam detal bilan ko'p mustahkamlik",
        "savol": "Mustahkamlikni yo'qotmasdan detallarni kamaytirish mumkinmi?",
        "asosiy": [
            "Har bir detal og'irlik va xarajat qo'shadi.",
            "Uchburchaklarni to'g'ri joylashtirsak, kam detal bilan ham mustahkam bo'ladi.",
            "Muhandislar doim shu muvozanatni izlaydi.",
        ],
        "chuqur": "Optimallashtirish — kerakli mustahkamlikni eng kam material bilan ta'minlash; bu zamonaviy muhandislikning asosiy vazifasi.",
        "tajriba": "Konstruksiyadan bittalab detal olib, u qachon zaiflashishini aniqlash (eng zarur detalni topish).",
        "uyga": "Konstruksiyangizdan qaysi detalni olib tashlash mumkinligi haqida taxminingizni yozing.",
    },
]

# ---------------------------------------------------------------------------
# VINT (2 ta)
# ---------------------------------------------------------------------------
SUBTOPICS["vint"] = [
    {
        "fokus": "Vint aylanma harakatni chiziqli qiladi",
        "savol": "Shishani ochganda qopqoq qanday harakat qiladi?",
        "asosiy": [
            "Vint — spiral shaklidagi tishcha bo'lgan detal.",
            "Uni aylantirsak, u oldinga yoki orqaga siljiydi.",
            "Ya'ni aylanma harakat chiziqli harakatga aylanadi.",
        ],
        "chuqur": "Vint aslida silindr atrofiga o'ralgan qiyalik — shuning uchun u oz kuch bilan katta bosim bera oladi.",
        "tajriba": "Vintni aylantirib, uning qaysi tomonga siljishini kuzatish va yo'nalishni teskari qilib sinash.",
        "uyga": "Uyda vint ishlatiladigan 2 ta narsani toping (shurup, qopqoq) va chizing.",
    },
    {
        "fokus": "Vint qadami — bir aylanishda qancha siljiydi",
        "savol": "Vintni bir marta aylantirsak, u qancha yuradi?",
        "asosiy": [
            "Qadam — vintning bir to'liq aylanishida bosib o'tgan masofasi.",
            "Qadam kichik bo'lsa, harakat sekin, lekin kuch katta bo'ladi.",
            "Qadam katta bo'lsa, tez harakatlanadi, lekin kuch kamayadi.",
        ],
        "chuqur": "Domkrat kichik qadamli vintdan foydalanadi — shuning uchun bir odam mashinani ko'tara oladi.",
        "tajriba": "Vintni bir marta to'liq aylantirib, qancha siljiganini o'lchash yoki taxmin qilish.",
        "uyga": "Kichik va katta qadamli vintni chizib, qaysi biri kuchliroq ekanini belgilang.",
    },
]

# ---------------------------------------------------------------------------
# KO'TARGICH (11 ta)
# ---------------------------------------------------------------------------
SUBTOPICS["kotargich"] = [
    {
        "fokus": "Nega og'ir yukni ko'tarish qiyin",
        "savol": "Og'ir qutini ko'targanda nima bizga qarshilik qiladi?",
        "asosiy": [
            "Har bir jismga Yerning tortish kuchi ta'sir qiladi.",
            "Yuk qanchalik og'ir bo'lsa, tortish kuchi shunchalik katta.",
            "Ko'tarish uchun shu kuchdan kattaroq kuch kerak bo'ladi.",
        ],
        "chuqur": "Ko'tarish uchun bajarilgan ish = og'irlik x balandlik; mexanizm ishni kamaytirmaydi, faqat kuchni taqsimlaydi.",
        "tajriba": "Yukni avval qo'lda, keyin mexanizm yordamida ko'tarib, farqni his qilish.",
        "uyga": "Og'ir narsani ko'tarishda odamlar qanday vositalardan foydalanishini 2 ta misol bilan yozing.",
    },
    {
        "fokus": "Richag bilan ko'tarish",
        "savol": "Uzun tayoq og'ir yukni ko'tarishga qanday yordam beradi?",
        "asosiy": [
            "Richagning uzun tomoniga bosilsa, kam kuch bilan yuk ko'tariladi.",
            "Tayanch nuqtasi yukga yaqin bo'lsa yanada osonlashadi.",
            "Kran strelasi ham aslida katta richag.",
        ],
        "chuqur": "Richag mexanik yutuq beradi, lekin qo'lni yuk ko'tarilgan balandlikdan ko'proq masofaga harakatlantirish kerak bo'ladi.",
        "tajriba": "Strelaning turli joyiga yuk osib, qaysi holatda ko'tarish osonroq ekanini taqqoslash.",
        "uyga": "Richag yordamida yuk ko'tarilayotgan holatni chizib, tayanch nuqtasini belgilang.",
    },
    {
        "fokus": "Shkiv bilan ko'tarish",
        "savol": "Quduqdan suvni qanday osonroq tortish mumkin?",
        "asosiy": [
            "Shkiv trosning yo'nalishini o'zgartiradi — pastga tortib, yukni yuqoriga chiqaramiz.",
            "Bir necha shkiv ishlatilsa, kerakli kuch kamayadi.",
            "Kranlarda shu tamoyil ishlatiladi.",
        ],
        "chuqur": "Har bir qo'shimcha qo'zg'aluvchi shkiv kerakli kuchni taxminan ikki barobar kamaytiradi.",
        "tajriba": "Trosni shkiv orqali va to'g'ridan-to'g'ri tortib, kuch farqini his qilish.",
        "uyga": "Shkiv ishlatiladigan 2 ta joyni toping (lift, quduq, kran) va yozing.",
    },
    {
        "fokus": "Vint bilan ko'tarish",
        "savol": "Domkrat qanday qilib mashinani ko'taradi?",
        "asosiy": [
            "Vint aylanganda asta-sekin yuqoriga siljiydi va yukni ko'taradi.",
            "Vint harakati sekin, lekin juda kuchli.",
            "Bundan tashqari, vint yukni o'z holatida ushlab tura oladi.",
        ],
        "chuqur": "Vint mexanizmi \"o'z-o'zini tormozlaydi\" — kuch olib tashlansa ham yuk pastga tushib ketmaydi.",
        "tajriba": "Vintli mexanizmni aylantirib yukni ko'tarish va keyin qo'yib yuborib, yuk tushmasligini tekshirish.",
        "uyga": "Domkrat rasmini topib, undagi vintni belgilang.",
    },
    {
        "fokus": "Strela uzunligi va ko'tarish kuchi",
        "savol": "Kran strelasi uzunroq bo'lsa, ko'proq yuk ko'tara oladimi?",
        "asosiy": [
            "Strela uzun bo'lsa, yuk uzoqroqqa yetkaziladi.",
            "Lekin uzun strelada bir xil yuk kranni kuchliroq ag'darishga intiladi.",
            "Shuning uchun uzoq masofada kamroq yuk ko'tariladi.",
        ],
        "chuqur": "Ag'darish momenti = yuk x strela uzunligi; shuning uchun kranlarda yuk diagrammasi bo'ladi.",
        "tajriba": "Yukni strelaning yaqin va uzoq nuqtasiga osib, konstruksiya barqarorligini taqqoslash.",
        "uyga": "Kran uzoqqa yuk uzatganda nega kamroq yuk ko'tarishini o'z so'zingiz bilan tushuntiring.",
    },
    {
        "fokus": "Kontr-vazn (qarshi og'irlik)",
        "savol": "Nega kranning orqa tomonida katta og'irlik bor?",
        "asosiy": [
            "Kontr-vazn — kranning orqasidagi og'ir blok.",
            "U yuk ag'darishga intilganda qarshi tomonga tortadi.",
            "Shu tufayli kran muvozanatda qoladi.",
        ],
        "chuqur": "Kontr-vazn momenti yuk momentini kompensatsiya qiladi — ikkalasi teng bo'lsa kran barqaror turadi.",
        "tajriba": "Modelning orqa tomoniga qo'shimcha og'irlik qo'yib, uning ag'darilishga qarshiligini sinash.",
        "uyga": "Qurilish krani rasmini topib, kontr-vazn qayerdaligini belgilang.",
    },
    {
        "fokus": "Ko'tarish balandligi va barqarorlik",
        "savol": "Yukni baland ko'tarsak, kran barqarorroq bo'ladimi?",
        "asosiy": [
            "Yuk baland ko'tarilsa, umumiy og'irlik markazi ham balandlashadi.",
            "Baland og'irlik markazi barqarorlikni kamaytiradi.",
            "Shuning uchun yuk imkon qadar pastroq tashiladi.",
        ],
        "chuqur": "Shuning uchun forkliftlar yukni yurish paytida yerga yaqin ushlab boradi.",
        "tajriba": "Yukni past va baland holatda ushlab, modelni asta qiyshaytirib barqarorlikni taqqoslash.",
        "uyga": "Forklift yukni nega past ushlab yurishini tushuntirib yozing.",
    },
    {
        "fokus": "Yukni ushlab turish",
        "savol": "Ko'tarilgan yuk nega o'z-o'zidan tushib ketmaydi?",
        "asosiy": [
            "Mexanizmda yukni ushlab turuvchi qism (tormoz yoki tutqich) bo'ladi.",
            "Vintli va tishli mexanizmlar o'z-o'zidan ushlab turadi.",
            "Shkivli mexanizmda esa maxsus tormoz kerak bo'ladi.",
        ],
        "chuqur": "Xavfsizlik uchun real kranlarda bir nechta mustaqil tormoz tizimi bo'ladi.",
        "tajriba": "Yukni ko'tarib, mexanizmni qo'yib yuborish va u ushlab turadimi yoki tushadimi kuzatish.",
        "uyga": "Liftda yuk qanday ushlab turilishi haqida taxminingizni yozing.",
    },
    {
        "fokus": "Ko'tarish tezligi va kuch murosasi",
        "savol": "Yukni tezroq ko'tarish uchun nima qilish kerak?",
        "asosiy": [
            "Tez ko'tarish uchun ko'proq kuch kerak bo'ladi.",
            "Sekin ko'tarilsa, kam kuch bilan ham bo'ladi.",
            "Muhandis bu ikkisi orasidan tanlaydi.",
        ],
        "chuqur": "Quvvat = ish / vaqt; bir xil ishni tezroq bajarish ko'proq quvvat talab qiladi.",
        "tajriba": "Uzatmani o'zgartirib (yoki tezlikni sozlab), ko'tarish tezligi va qiyinligi qanday bog'liqligini sinash.",
        "uyga": "Tez va sekin ishlaydigan ko'targichga bittadan misol yozing.",
    },
    {
        "fokus": "Yuk sig'imi chegarasi",
        "savol": "Kran cheksiz og'ir yukni ko'tara oladimi?",
        "asosiy": [
            "Har bir mexanizmning ko'tara oladigan chegarasi bor.",
            "Chegaradan oshsa, konstruksiya buziladi yoki ag'dariladi.",
            "Shuning uchun har bir kranda ruxsat etilgan yuk yozib qo'yiladi.",
        ],
        "chuqur": "Muhandislar xavfsizlik zaxirasi qo'shadi — kran rasmiy chegaradan ancha ko'pini ko'tara olishi kerak.",
        "tajriba": "Yukni asta-sekin oshirib, model qachon qiynala boshlashini kuzatish (buzilmasdan to'xtash).",
        "uyga": "Liftda \"maksimal 8 kishi\" kabi yozuv nega borligini tushuntirib yozing.",
    },
    {
        "fokus": "Bir necha mexanizm birga",
        "savol": "Kranda bir vaqtda nechta mexanizm ishlaydi?",
        "asosiy": [
            "Kran bir vaqtda richag, shkiv va aylanish mexanizmidan foydalanadi.",
            "Har biri o'z vazifasini bajaradi.",
            "Birga ishlaganda murakkab vazifani hal qiladi.",
        ],
        "chuqur": "Murakkab mashinalar oddiy mexanizmlarning kombinatsiyasidan iborat — bu muhandislikning asosiy tamoyili.",
        "tajriba": "Modeldagi barcha mexanizmlarni (richag, shkiv, tishli) sanab, har birining vazifasini aytish.",
        "uyga": "Modelingizda nechta turli mexanizm borligini sanab, ro'yxat qilib yozing.",
    },
]
