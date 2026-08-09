# -*- coding: utf-8 -*-
"""
Har bir STEAM tema uchun 3 ta sinf darajasi (tier) bo'yicha to'liq dars-reja kontenti.
Tier A = 0-1-sinf (sodda til, ko'p yordam), Tier B = 2-3-sinf (o'rta), Tier C = 4-sinf (chuqur, mustaqil).

Har bir tema uchun:
  concept    - maqsad-1 jumlasiga qo'yiladigan qisqa ibora
  lugat      - 5 ta atama (Atama (inglizcha) - ta'rif)
  nazariya   - 3 ta kichik bo'lim: (sarlavha, daqiqa, [bandlar]) - jami 15 daqiqa (5+7+3)
  softskills - 2-3 ta (nom, matn) - dars raqamiga qarab navbat bilan tanlanadi
"""

THEME_CONTENT = {

"richag": {
    "concept": "richag qonuni va tayanch nuqtasi atrofida aylanish tamoyilini",
    "A": {
        "lugat": [
            "Richag (Lever) – tayanch nuqtasi atrofida aylanadigan qattiq tayoq yoki qism",
            "Tayanch nuqtasi (Fulcrum) – richag tiralib turadigan, aylanadigan nuqta",
            "Kuch (Force) – biror narsani harakatga keltiradigan yoki ko'taradigan ta'sir",
            "Yuk (Load) – richag yordamida ko'tariladigan yoki harakatlantiriladigan narsa",
            "Qo'l (Arm/Handle) – richagning kuch qo'llaydigan uzun qismi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "O'quvchilarga richag nima ekanligi kundalik misollar bilan tushuntiriladi: qaychi, eshik dastagi, teeter-totter.",
                "Savol: nega uzun tayoq bilan og'ir narsani ko'chirish osonroq?",
            ]),
            ("Richag qanday ishlaydi", 7, [
                "Tayanch nuqtasi, kuch va yuk tushunchalari oddiy chizma yoki jonli namoyish bilan ko'rsatiladi.",
                "O'qituvchi qo'lda kichik richag namunasini aylantirib, kuchning qayerga qo'yilishini ko'rsatadi.",
                "O'quvchilar navbat bilan richagni sinab, yukni ko'tarishga harakat qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Richag atrofimizda qayerlarda uchrashini birga sanab chiqamiz.",
                "Bugungi modelda richag qaysi qismda ishlatilishini eslatib o'tamiz.",
            ]),
        ],
        "softskills": [
            ("Diqqat va aniqlik", "Kichik detallarni to'g'ri joylashtirish orqali sinchkovlik ko'nikmasini rivojlantirish. O'quvchilarga har bir qadamni instruksiya bilan solishtirib tekshirishni o'rgating."),
            ("Sabr-toqat", "Model darrov ishlamasa ham, qayta urinib ko'rish kerakligini tushuntiring — bu muhandislikning tabiiy qismi."),
        ],
    },
    "B": {
        "lugat": [
            "Richag (Lever) – tayanch nuqtasi atrofida aylanadigan qattiq jism",
            "Tayanch nuqtasi (Fulcrum) – richag aylanadigan nuqta",
            "Kuch yelkasi (Force arm) – tayanch nuqtasidan kuch qo'yilgan joygacha bo'lgan masofa",
            "Yuk yelkasi (Load arm) – tayanch nuqtasidan yukgacha bo'lgan masofa",
            "Moment kuchi (Torque) – aylantiruvchi kuch, kuch yelkasi uzunligiga bog'liq",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Richag kundalik hayotda qayerda ishlatilishi muhokama qilinadi (qaychi, mixchiqargich, eshik dastagi).",
                "Nima uchun uzun richag bilan ishlash osonroq — kichik savol-javob.",
            ]),
            ("Kuch yelkasi va moment", 7, [
                "Kuch yelkasi uzunroq bo'lsa, kichik kuch bilan katta yukni ko'tarish mumkinligi tushuntiriladi.",
                "Amaliy misol: uzun tayoq bilan og'ir toshni qo'zg'atish nima uchun osonroq.",
                "Ikki xil uzunlikdagi richag qo'lda taqqoslanadi (agar mumkin bo'lsa).",
            ]),
            ("Yakunlash", 3, [
                "Richagning real hayotdagi qo'llanilishi (kran, tarozi, asboblar) umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Diqqat va aniqlik", "Bitta noto'g'ri joylashtirilgan detal butun mexanizmning ishlamay qolishiga sabab bo'lishini tushuntiring — har bir bosqichni tekshirib borish muhim."),
            ("Muammoni tahlil qilish", "Model kutilganidek ishlamasa, sababini richag uzunligi yoki tayanch nuqtasi joylashuvidan qidirishni o'rgating."),
        ],
    },
    "C": {
        "lugat": [
            "Richag (Lever) – tayanch nuqtasi atrofida aylanadigan qattiq jism",
            "Moment kuchi (Torque) – F x d formulasi bilan hisoblanadigan aylantiruvchi ta'sir",
            "Mexanik yutuq (Mechanical advantage) – richag necha marta kuchni kuchaytirishi",
            "1/2/3-toifa richag (Class 1/2/3 lever) – tayanch, kuch va yukning joylashuv tartibiga qarab richag turlari",
            "Muvozanat sharti (Equilibrium) – ikki tomondagi moment kuchlari teng bo'lganda richag muvozanatda turadi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Richagning muhandislikdagi ahamiyati va tarixiy misollar (Arximed: \"Menga tayanch nuqta bering, Yerni qo'zg'ataman\").",
            ]),
            ("Moment kuchi va richag toifalari", 7, [
                "Moment kuchi = kuch x kuch yelkasi tushunchasi sodda misolda ko'rsatiladi.",
                "1, 2 va 3-toifa richaglar orasidagi farq (tayanch/kuch/yukning joylashuvi) muhokama qilinadi.",
                "O'quvchilar bugungi modeldagi richag qaysi toifaga yaqinligini aniqlashga harakat qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Richag zamonaviy texnikada (kran, ekskavator, protez) qanday ishlatilishi qisqacha muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Har bir konstruktiv qarorni (nega bu uzunlikda, nega bu joyda) asoslashga undang — bu haqiqiy muhandislarning ish uslubi."),
            ("Jamoada ishlash", "Murakkabroq mexanizmlarda ish bo'linishi (bir o'quvchi yig'adi, ikkinchisi tekshiradi) samaradorlikni oshirishini ko'rsating."),
        ],
    },
},

"tishli": {
    "concept": "tishli g'ildiraklar orqali tezlik va kuchning bir-biriga almashinishini",
    "A": {
        "lugat": [
            "Tishli g'ildirak (Gear) – tishchalari bo'lgan, aylanadigan dumaloq detal",
            "Aylanish (Rotation) – g'ildirakning o'z o'qi atrofida harakati",
            "Katta g'ildirak (Big gear) – ko'p tishli, sekinroq aylanadigan g'ildirak",
            "Kichik g'ildirak (Small gear) – kam tishli, tezroq aylanadigan g'ildirak",
            "Ulanish (Mesh) – ikki tishli g'ildirakning tishlari bir-biriga kirib ishlashi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Tishli g'ildirak nima — velosiped yoki soat ichidagi tishli g'ildiraklar misol qilinadi.",
            ]),
            ("Katta va kichik g'ildirak", 7, [
                "Ikki xil o'lchamdagi tishli g'ildirak qo'lda aylantirib ko'rsatiladi: biri tez, biri sekin aylanadi.",
                "O'quvchilar o'zlari qo'lda ikkita tishlini ulab, aylantirib sinab ko'radilar.",
            ]),
            ("Yakunlash", 3, [
                "Tishli g'ildiraklar qayerlarda ishlatilishini (soat, velosiped) birga sanab chiqamiz.",
            ]),
        ],
        "softskills": [
            ("Kuzatuvchanlik", "Ikki tishli g'ildirak ulanganda nima o'zgarishini diqqat bilan kuzatishni so'rang."),
            ("Jamoada ishlash", "Juftlikda ishlashda navbat bilan detal ulash va tekshirishni tavsiya qiling."),
        ],
    },
    "B": {
        "lugat": [
            "Tishli g'ildirak (Gear) – tishlari bir-biriga ulanib aylanadigan detal",
            "Uzatma nisbati (Gear ratio) – ikki tishli g'ildirak tishlari sonining nisbati",
            "Tezlik (Speed) – g'ildirakning bir daqiqada necha marta aylanishi",
            "Moment (Torque) – tishli g'ildirak orqali uzatiladigan aylantiruvchi kuch",
            "Uzatma tizimi (Gear train) – bir nechta tishli g'ildirakning birgalikda ishlashi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Tishli g'ildiraklar tezlik va kuchni qanday almashtirishi haqida savol-javob.",
            ]),
            ("Uzatma nisbati", 7, [
                "Kichik g'ildirak tezroq aylanadi, katta g'ildirak esa ko'proq kuch (moment) berishi tushuntiriladi.",
                "Velosiped uzatmasi bilan solishtiriladi: past uzatma — kuch, baland uzatma — tezlik.",
                "O'quvchilar ikki xil o'lchamdagi tishlini ulab, tezlik farqini o'lchashga harakat qiladilar (necha marta aylanadi).",
            ]),
            ("Yakunlash", 3, [
                "Uzatma nisbati nima uchun texnikada muhimligi umumlashtiriladi (mashina uzatmalari misolida).",
            ]),
        ],
        "softskills": [
            ("Mantiqiy fikrlash", "Nega kichik g'ildirak tezroq aylanishini o'z so'zlari bilan tushuntirishni so'rang."),
            ("Aniqlik", "Tishli g'ildiraklar to'g'ri ulanmasa mexanizm g'ijirlab qolishini, shu sababli aniq yig'ish zarurligini ta'kidlang."),
        ],
    },
    "C": {
        "lugat": [
            "Uzatma nisbati (Gear ratio) – ikki g'ildirak tishlari sonining nisbati (masalan 3:1)",
            "Moment-tezlik almashinuvi (Torque-speed tradeoff) – uzatma tezlikni oshirsa, moment kamayadi va aksincha",
            "Ideal g'ildirak (Idler gear) – aylanish yo'nalishini o'zgartiruvchi, nisbatga ta'sir qilmaydigan g'ildirak",
            "Kompound uzatma (Compound gear train) – bir necha uzatma juftligi ketma-ket ulangan tizim",
            "Samaradorlik (Efficiency) – uzatmada ishqalanish tufayli yo'qotiladigan kuch ulushi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Uzatma tizimlarining zamonaviy texnikadagi (avtomobil, robot qo'llari) ahamiyati muhokama qilinadi.",
            ]),
            ("Uzatma nisbatini hisoblash", 7, [
                "Uzatma nisbati = tishlar soni nisbati sifatida sodda misolda hisoblanadi (masalan 24:8 = 3:1).",
                "Moment va tezlik o'rtasidagi \"almashinuv\" tushunchasi — birini oshirish ikkinchisini kamaytiradi.",
                "Kompound (ketma-ket) uzatma qanday katta nisbatlarga erishishga yordam berishi ko'rsatiladi.",
            ]),
            ("Yakunlash", 3, [
                "Real texnikada (mashina uzatma qutisi, soat mexanizmi) uzatma nisbatining qo'llanilishi muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Uzatma nisbatini o'zgartirish natijani qanday o'zgartirishini bashorat qilib, keyin sinab ko'rishni so'rang — gipoteza-sinov usuli."),
            ("Aniq hisob-kitob", "Tishlar sonini sanab, uzatma nisbatini hisoblashda aniqlikka e'tibor bering."),
        ],
    },
},

"shkiv": {
    "concept": "shkiv-tasma tizimi orqali kuch yo'nalishi va miqdorining o'zgarishini",
    "A": {
        "lugat": [
            "Shkiv (Pulley) – tros yoki tasma o'tadigan, aylanuvchi g'ildirak",
            "Tros/Tasma (Rope/Belt) – shkiv ustidan o'tib, kuchni uzatuvchi ip yoki lenta",
            "Tortish (Pull) – tros yordamida narsani harakatga keltirish",
            "Ko'tarish (Lift) – narsani yuqoriga olib chiqish",
            "Chig'ir (Winch/Well pulley) – quduqdan suv tortishda ishlatiladigan shkiv turi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Shkiv nima — quduq chig'iri yoki bayroq ustuni misolida tushuntiriladi.",
            ]),
            ("Shkiv qanday yordam beradi", 7, [
                "Tros shkiv ustidan o'tganda, kuch yo'nalishi o'zgarishi (pastga tortsak, narsa yuqoriga chiqadi) ko'rsatiladi.",
                "O'quvchilar qo'lda kichik ip va halqa bilan shkiv tamoyilini sinab ko'radilar.",
            ]),
            ("Yakunlash", 3, [
                "Shkiv qayerlarda ishlatilishini (bayroq ustuni, parda) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Ehtiyotkorlik", "Tros/ip bilan ishlashda chalkashtirmaslik va ehtiyotkorlikni o'rgating."),
            ("Hamkorlik", "Shkiv sinovida bir o'quvchi trosni tortsa, ikkinchisi natijani kuzatishi mumkin — juftlikda ishlash."),
        ],
    },
    "B": {
        "lugat": [
            "Shkiv (Pulley) – tros/tasma yordamida kuchni uzatuvchi aylanuvchi g'ildirak",
            "Qo'zg'almas shkiv (Fixed pulley) – joyi o'zgarmaydigan, faqat kuch yo'nalishini o'zgartiruvchi shkiv",
            "Qo'zg'aluvchi shkiv (Movable pulley) – yuk bilan birga harakatlanadigan, kuchni kamaytiruvchi shkiv",
            "Shkiv tizimi (Block and tackle) – bir nechta shkivning birgalikda ishlashi",
            "Tortish kuchi (Tension) – tros bo'ylab uzatiluvchi kuch",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Shkiv-tasma tizimining kundalik hayotdagi (lift, kran, parda) misollari muhokama qilinadi.",
            ]),
            ("Kuchni kamaytirish", 7, [
                "Bitta shkiv faqat yo'nalishni o'zgartirishi, bir nechta shkiv birga ishlatilsa esa kerakli tortish kuchi kamayishi tushuntiriladi.",
                "Buning evaziga tros uzunroq tortilishi kerakligi (energiya saqlanishi tamoyili sodda tarzda) aytib o'tiladi.",
                "Qudiq chig'iri yoki lift tros tizimi bilan solishtiriladi.",
            ]),
            ("Yakunlash", 3, [
                "Shkiv tizimining real qurilmalarda (kran, lift) qo'llanilishi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Diqqat va aniqlik", "Tros/tasma to'g'ri tarangligi mexanizmning silliq ishlashiga ta'sir qilishini tushuntiring."),
            ("Muammoni hal qilish", "Agar tros sirg'alib chiqib ketsa, sababini (taranglik, shkiv joylashuvi) birga qidirishni o'rgating."),
        ],
    },
    "C": {
        "lugat": [
            "Shkiv tizimi (Block and tackle) – bir nechta qo'zg'almas va qo'zg'aluvchan shkivlar kombinatsiyasi",
            "Mexanik yutuq (Mechanical advantage) – shkiv tizimi kuchni necha marta kamaytirishi",
            "Tortish kuchi taqsimoti (Tension distribution) – trosdagi kuchning har bir shkiv segmentida taqsimlanishi",
            "Ishqalanish yo'qotishi (Friction loss) – shkivda ishqalanish tufayli yo'qoladigan kuch ulushi",
            "Statik va dinamik yuk (Static/dynamic load) – harakatsiz va harakatdagi yukning shkivga ta'siri",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Shkiv tizimlarining zamonaviy inshootlarda (qurilish kranlari, liftlar) muhim roli muhokama qilinadi.",
            ]),
            ("Mexanik yutuqni hisoblash", 7, [
                "Bir nechta shkiv ishlatilganda, kerakli kuch necha marta kamayishi (mexanik yutuq) sodda misolda ko'rsatiladi.",
                "Kuchning kamayishi evaziga tros uzunroq tortilishi kerakligi (energiya saqlanishi qonuni) tushuntiriladi.",
                "O'quvchilar bugungi modeldagi shkivlar sonini sanab, taxminiy yutuqni baholaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Zamonaviy kranlar va liftlarda shkiv tizimlarining qo'llanilishi qisqacha muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Tizimli fikrlash", "Murakkab shkiv tizimini kichik qismlarga bo'lib tahlil qilishni o'rgating — har bir shkiv alohida vazifa bajaradi."),
            ("Aniqlik va sinov", "Nazariy hisob bilan amaliy natijani solishtirib, farq bo'lsa sababini muhokama qiling."),
        ],
    },
},

"krivoship": {
    "concept": "krivoship-shatun mexanizmi orqali aylanma harakatning tebranma harakatga aylanishini",
    "A": {
        "lugat": [
            "Aylanma harakat (Rotation) – doira bo'ylab aylanish",
            "Tebranma harakat (Back-and-forth) – oldinga-orqaga yoki yuqori-past qaytariluvchi harakat",
            "Motor (Motor) – elektr yordamida aylanadigan qurilma",
            "Bog'lovchi qism (Link) – aylanma harakatni tebranishga o'zgartiruvchi detal",
            "Mexanizm (Mechanism) – harakatni uzatuvchi yoki o'zgartiruvchi qurilmalar tizimi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Velosiped pedali va tizzaning harakati misolida aylanma va tebranma harakat farqi ko'rsatiladi.",
            ]),
            ("Aylanma harakat tebranishga aylanadi", 7, [
                "Motor/qo'l aylanma harakat berishi, mexanizm esa buni oldinga-orqaga tebranishga aylantirishi tushuntiriladi.",
                "O'quvchilar qo'lda kichik krivoship qismini aylantirib, uchidagi qismning tebranishini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Bugungi modelda qaysi qism aylanadi, qaysi qism tebranishini birga aniqlaymiz.",
            ]),
        ],
        "softskills": [
            ("Kuzatuvchanlik", "Aylanma harakat qanday qilib tebranishga aylanishini diqqat bilan kuzatishni so'rang."),
            ("Sabr-toqat", "Mexanizm birinchi urinishda silliq ishlamasligi mumkinligini, qayta sozlash normal ekanini tushuntiring."),
        ],
    },
    "B": {
        "lugat": [
            "Krivoship-shatun mexanizmi (Crank-slider mechanism) – aylanma harakatni tebranmaga aylantiruvchi tizim",
            "Krivoship (Crank) – aylanadigan qism",
            "Shatun (Connecting rod) – krivoship va tebranuvchi qismni bog'lovchi tayoqcha",
            "Amplituda (Amplitude) – tebranish qanchalik katta yoki kichik ekanligi",
            "Sikl (Cycle) – harakatning bir marta to'liq takrorlanishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Dvigatelning klassik ishlash tamoyili sifatida krivoship-shatun mexanizmi tanishtiriladi.",
            ]),
            ("Mexanizmning ishlashi", 7, [
                "Motor aylanma harakat berishi, krivoship-shatun mexanizmi buni tebranma harakatga aylantirishi ko'rsatiladi.",
                "Velosiped pedali va tizza harakati bilan solishtiriladi — aylanma kuch tebranma yurishga aylanadi.",
                "O'quvchilar mexanizmning tezligini o'zgartirib, tebranish tezligiga ta'sirini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Bu mexanizm hayvon-robotlar va mashinalarda qanday ishlatilishi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Mantiqiy fikrlash", "Nega aylanma harakat tebranishga aylanishini o'z so'zi bilan tushuntirishni so'rang."),
            ("Diqqat va aniqlik", "Shatun va krivoship noto'g'ri ulansa mexanizm tiqilib qolishini, shu sababli aniqlik zarurligini ta'kidlang."),
        ],
    },
    "C": {
        "lugat": [
            "Krivoship-shatun mexanizmi (Crank-slider/four-bar linkage) – aylanma harakatni chiziqli/tebranma harakatga aylantiruvchi tizim",
            "Amplituda (Amplitude) – tebranish kengligi, krivoship radiusiga bog'liq",
            "Faza (Phase) – mexanizmning aylanish siklidagi joriy holati",
            "To'rt bo'g'inli mexanizm (Four-bar linkage) – to'rtta qattiq bo'g'indan iborat harakat mexanizmi",
            "Davriylik (Periodicity) – harakatning muntazam ravishda takrorlanishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Ichki yonuv dvigateli va bug' mashinasida krivoship-shatun mexanizmining tarixiy ahamiyati muhokama qilinadi.",
            ]),
            ("Amplituda va mexanizm geometriyasi", 7, [
                "Krivoship radiusi o'zgarsa, tebranish amplitudasi (kengligi) qanday o'zgarishi tushuntiriladi.",
                "Mexanizmning geometrik nisbatlari harakat trayektoriyasiga qanday ta'sir qilishi muhokama qilinadi.",
                "O'quvchilar bugungi modeldagi krivoship uzunligini o'zgartirsa, natija qanday bo'lishini bashorat qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Bu mexanizmning zamonaviy robototexnikada (yurish roboti, biomimetika) qo'llanilishi qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Mexanizm geometriyasini o'zgartirish natijaga qanday ta'sir qilishini bashorat qilib, keyin sinab ko'rishni tavsiya qiling."),
            ("Ijodiy yondashuv", "O'z krivoship mexanizmini biroz o'zgartirib, boshqacha harakat olish mumkinligini taklif qiling."),
        ],
    },
},

"muvozanat": {
    "concept": "og'irlik markazi va muvozanat sharti tushunchalarini",
    "A": {
        "lugat": [
            "Muvozanat (Balance) – jismning yiqilmasdan turishi",
            "Og'irlik markazi (Center of gravity) – jismning \"eng og'ir\" nuqtasi kabi tasavvur qilinadigan joy",
            "Tayanch (Support) – jism tiralib turadigan asos",
            "Yiqilish (Fall/Tip over) – muvozanat buzilganda yuz beradigan holat",
            "Barqarorlik (Stability) – jismning yiqilmay turish qobiliyati",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Bir oyoqda turib muvozanatni saqlashga harakat qilish o'yini bilan mavzuga kirish qilinadi.",
            ]),
            ("Nega ba'zi narsalar yiqilmaydi", 7, [
                "Keng tayanchli narsalar (uchburchak, piramida) yiqilmasligi, tor tayanchlilar osongina yiqilishi ko'rsatiladi.",
                "O'quvchilar qo'lda turli shakldagi bloklarni tik qo'yib, qaysi biri barqarorroq ekanini sinaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Muvozanatli narsalar atrofimizda qayerda uchrashini (stol, minora) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Sinov va xato orqali o'rganish", "Model yiqilib tushsa, bu normal ekanini va qayta sozlab ko'rish kerakligini tushuntiring."),
            ("Diqqat", "Modelni tik qo'yishda asta va ehtiyotkorlik bilan ishlashni o'rgating."),
        ],
    },
    "B": {
        "lugat": [
            "Muvozanat markazi (Center of gravity) – jismning og'irligi \"yig'ilgan\" deb tasavvur qilinadigan nuqta",
            "Tayanch maydoni (Base of support) – jism yer bilan tegib turgan hudud",
            "Barqarorlik (Stability) – jismning tebranib ham yiqilmay turish qobiliyati",
            "Og'dirish momenti (Tipping moment) – jismni yiqitishga harakat qiluvchi kuch ta'siri",
            "Muvozanat holati (Equilibrium) – jismga ta'sir etuvchi kuchlar teng bo'lgan holat",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Nima uchun ba'zi robotlar yurganda yiqilib ketmasligi haqida savol-javob.",
            ]),
            ("Og'irlik markazi va tayanch", 7, [
                "Jismning muvozanatda turishi uchun og'irlik markazi tayanch nuqtasi/maydoni tepasida bo'lishi kerakligi tushuntiriladi.",
                "Past va keng tayanch barqarorlikni oshirishi amaliy sinovda ko'rsatiladi (modelni turli holatlarda qiyshaytirib, qachon yiqilishini kuzatish).",
                "Balandroq va torroq tayanchli jismlar bilan solishtirish.",
            ]),
            ("Yakunlash", 3, [
                "Muvozanat tamoyili real hayotda (velosiped, minora, robot) qanday qo'llanilishi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Tahliliy fikrlash", "Model yiqilib ketsa, sababini (tayanch torligi, og'irlik markazi balandligi) tahlil qilishni o'rgating."),
            ("Sabr-toqat", "Muvozanatni topish uchun bir necha marta sozlash kerak bo'lishi mumkinligini tushuntiring."),
        ],
    },
    "C": {
        "lugat": [
            "Og'irlik markazi (Center of gravity) – jism og'irligining nazariy jamlangan nuqtasi",
            "Statik barqarorlik (Static stability) – harakatsiz holatdagi muvozanat qobiliyati",
            "Dinamik barqarorlik (Dynamic stability) – harakatdagi (yurish, burilish) muvozanat qobiliyati",
            "Ag'darilish burchagi (Tipping angle) – jism yiqila boshlaydigan qiyalik burchagi",
            "Tayanch poligoni (Support polygon) – tayanch nuqtalari orasidagi shartli maydon",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Robototexnikada muvozanat nega muhandislik muammosi ekanligi (yuruvchi robotlar, kranlar misolida) muhokama qilinadi.",
            ]),
            ("Statik va dinamik barqarorlik", 7, [
                "Og'irlik markazi tayanch poligoni ichida bo'lsa jism muvozanatda turishi tushuntiriladi.",
                "Harakatdagi barqarorlik (dinamik) statikdan farqi — tezlik va inersiya ta'siri muhokama qilinadi.",
                "O'quvchilar modelning og'irlik markazini o'zgartirib (yuk qo'shib), barqarorlikka ta'sirini sinaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Zamonaviy robototexnikada (ikki oyoqli robotlar, kranlar) barqarorlik masalasi qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Gipoteza va sinov", "Barqarorlikka ta'sir qiladigan omilni o'zgartirishdan oldin natijani bashorat qilishni so'rang."),
            ("Muhandislik fikrlashi", "Barqarorlik va harakatchanlik o'rtasidagi murosani (tradeoff) muhokama qiling."),
        ],
    },
},

"geometriya": {
    "concept": "geometrik shakllarning mustahkamlik xususiyatlarini",
    "A": {
        "lugat": [
            "Uchburchak (Triangle) – uchta tomonli shakl",
            "To'rtburchak (Quadrilateral) – to'rtta tomonli shakl",
            "Mustahkam (Strong/Rigid) – shakli oson o'zgarmaydigan",
            "Egiluvchan (Flexible) – shakli oson o'zgaradigan",
            "Burchak (Angle/Corner) – ikki tomon kesishgan joy",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Bolalarga uchburchak va to'rtburchak shakllar ko'rsatiladi, ular haqida gaplashiladi.",
            ]),
            ("Qaysi shakl mustahkamroq", 7, [
                "O'qituvchi qo'lda to'rtburchak shaklni bosib, oson egilib ketishini ko'rsatadi.",
                "Keyin uchburchak shaklni bosib, u o'zgarmasligini ko'rsatadi.",
                "O'quvchilar o'zlari ikkala shaklni qo'lda sinab, farqni his qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Ko'prik va minoralarda uchburchak shakl qayerda ko'rinishini birga qidiramiz (rasmda yoki tashqarida).",
            ]),
        ],
        "softskills": [
            ("Kuzatuvchanlik", "Ikki shaklni solishtirib, farqni o'z so'zi bilan aytishni so'rang."),
            ("Ijodkorlik", "O'z shaklini yasab, uni mustahkam qilish uchun nima qo'shish mumkinligini so'rang."),
        ],
    },
    "B": {
        "lugat": [
            "Geometrik mustahkamlik (Structural rigidity) – shaklning tashqi kuchga qarshi shaklini saqlash qobiliyati",
            "Uchburchaklash (Triangulation) – konstruksiyani uchburchaklar bilan mustahkamlash usuli",
            "Diagonal (Diagonal) – to'rtburchak burchaklarini bog'lovchi qiyshiq chiziq",
            "Deformatsiya (Deformation) – shaklning tashqi kuch ta'sirida o'zgarishi",
            "Konstruksiya (Structure) – detallardan tuzilgan qurilma",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Nima uchun ko'prik va minoralarda uchburchak shakl ko'p ishlatilishi haqida savol-javob.",
            ]),
            ("Uchburchaklash tamoyili", 7, [
                "Nima uchun uchburchak shakl o'zgarmasligi (burchaklari qattiq belgilangan), to'rtburchak esa oson egilib ketishi (burchaklari erkin) tushuntiriladi.",
                "Diagonal qo'shish orqali to'rtburchakni qanday mustahkamlash mumkinligi ko'rsatiladi.",
                "O'quvchilar to'rtburchak konstruksiyaga diagonal qo'shib, mustahkamlik farqini sinaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Ko'prik va minoralarda nega uchburchak ko'p ishlatilishi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Muammoni hal qilish", "Konstruksiya beqaror bo'lsa, qayerga diagonal/qo'shimcha detal qo'shish kerakligini birga topishni o'rgating."),
            ("Ijodiy dizayn", "O'z konstruksiyasini mustahkamlashning bir necha yo'lini taklif qilishni so'rang."),
        ],
    },
    "C": {
        "lugat": [
            "Struktura mustahkamligi (Structural integrity) – konstruksiyaning yuk ostida shaklini saqlash qobiliyati",
            "Uchburchaklash (Triangulation) – statik jihatdan barqaror shakllar yaratish usuli",
            "Kuchlanish va siqilish (Tension and compression) – konstruksiya elementlariga ta'sir qiluvchi ikki asosiy kuch turi",
            "Fermalar (Truss) – uchburchaklardan tashkil topgan mustahkam konstruksiya tizimi",
            "Yuk taqsimoti (Load distribution) – tashqi kuchning konstruksiya bo'ylab tarqalishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Zamonaviy inshootlarda (ko'prik, minoralar, kran) ferma konstruksiyalarining ahamiyati muhokama qilinadi.",
            ]),
            ("Kuchlanish, siqilish va uchburchaklash", 7, [
                "Uchburchak nega geometrik jihatdan yagona \"qattiq\" ko'pburchak ekanligi (burchaklari tomonlar uzunligi bilan to'liq belgilanadi) tushuntiriladi.",
                "Ferma konstruksiyalarida ba'zi elementlar cho'zilishi (kuchlanish), ba'zilari siqilishi tushuntiriladi.",
                "O'quvchilar bugungi modelning qaysi qismlari yuk ostida qanday ishlashini (cho'ziladimi, siqiladimi) muhokama qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Haqiqiy ko'priklar va minoralarning ferma konstruksiyasi qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Konstruksiyani optimallashtirish — minimal detal bilan maksimal mustahkamlikka erishish g'oyasini muhokama qiling."),
            ("Tanqidiy tahlil", "O'z konstruksiyasining eng zaif nuqtasini topib, uni qanday mustahkamlash mumkinligini so'rang."),
        ],
    },
},

"elastik": {
    "concept": "elastik energiya va inersiya kuchining harakatga aylanishini",
    "A": {
        "lugat": [
            "Elastik (Elastic) – cho'zilgach yana avvalgi holatiga qaytadigan (masalan rezina)",
            "Cho'zish (Stretch) – elastik narsani uzunroq qilib tortish",
            "Energiya (Energy) – harakat yoki ish bajarish uchun kerakli kuch zaxirasi",
            "Qo'yib yuborish (Release) – tortilgan narsani bo'shatib yuborish",
            "Tezlanish (Speed up) – harakatning tezlashishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Rezina lentani cho'zib-qo'yib yuborish o'yini bilan mavzuga kirish qilinadi.",
            ]),
            ("Rezina qanday energiya to'playdi", 7, [
                "Rezina/prujina cho'zilganda \"energiya\" to'planishi, qo'yib yuborilganda bu energiya harakatga aylanishi tushuntiriladi.",
                "O'quvchilar qo'lda rezina bilan kichik narsani \"otib\" ko'radilar (xavfsiz tarzda, o'qituvchi nazoratida).",
            ]),
            ("Yakunlash", 3, [
                "Rezina qayerlarda ishlatilishini (sirg'aluvchi arava, o'q-yoy o'yinchoq) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Xavfsizlik qoidalariga rioya", "Elastik/rezina bilan ishlashda boshqalarga qaratib otmaslik kerakligini alohida ta'kidlang."),
            ("Qiziqish va kashfiyot", "Rezinani turlicha cho'zib, natija qanday o'zgarishini kuzatishga undang."),
        ],
    },
    "B": {
        "lugat": [
            "Elastik energiya (Elastic energy) – cho'zilgan/siqilgan elastik jismda to'plangan energiya",
            "Potensial energiya (Potential energy) – jismning holati tufayli ega bo'lgan \"zaxiradagi\" energiyasi",
            "Kinetik energiya (Kinetic energy) – harakatdagi jismning energiyasi",
            "Inersiya (Inertia) – jismning harakat holatini saqlashga intilishi",
            "Pull-back mexanizmi (Pull-back mechanism) – orqaga tortib qo'yib yuborilganda oldinga yuruvchi mexanizm",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Pull-back (orqaga tortib qo'yib yuborish) o'yinchoq mashinalar qanday ishlashi haqida savol-javob.",
            ]),
            ("Energiya almashinuvi va inersiya", 7, [
                "Elastik element cho'zilganda potensial energiya to'planishi, qo'yib yuborilganda bu energiya harakat (kinetik) energiyasiga aylanishi tushuntiriladi.",
                "Nyutonning 1-qonuni sodda tilda: jism harakatga tushgach, kuch to'xtatmasa harakatda davom etadi (inersiya).",
                "O'quvchilar pull-back mexanizmini turlicha tortib, masofa farqini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Elastik energiya va inersiya birgalikda qanday ishlashi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Ilmiy kuzatish", "Tortish kuchi va bosib o'tilgan masofa orasidagi bog'liqlikni kuzatib, xulosa chiqarishni so'rang."),
            ("Xavfsizlik madaniyati", "Elastik kuch bilan ishlashda atrofdagilarni hisobga olish zarurligini ta'kidlang."),
        ],
    },
    "C": {
        "lugat": [
            "Elastik potensial energiya (Elastic potential energy) – deformatsiyalangan jismda saqlanadigan energiya",
            "Energiya saqlanishi qonuni (Conservation of energy) – energiya yo'q bo'lib ketmaydi, bir turdan ikkinchisiga aylanadi",
            "Inersiya (Inertia) – Nyutonning 1-qonuniga ko'ra jismning harakat holatini saqlashga intilishi",
            "Ishqalanish yo'qotishi (Friction loss) – energiyaning ishqalanish tufayli issiqlikka aylanib yo'qolishi",
            "Impuls (Momentum) – jismning massasi va tezligi ko'paytmasi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Energiya turlari (potensial, kinetik) va ularning bir-biriga aylanishi haqida kirish suhbati.",
            ]),
            ("Energiya saqlanishi va inersiya", 7, [
                "Elastik potensial energiya qo'yib yuborilganda deyarli to'liq kinetik energiyaga aylanishi, lekin ishqalanish tufayli bir qismi yo'qolishi tushuntiriladi.",
                "Nyutonning 1-qonuni (inersiya qonuni) aniq ta'rif bilan berilib, pull-back mexanizmi misolida ko'rsatiladi.",
                "O'quvchilar bosib o'tilgan masofa va sirt turi (silliq/notekis) o'rtasidagi bog'liqlikni sinaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Energiya saqlanishi qonunining texnika va tabiatdagi boshqa misollari qisqacha muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Ilmiy metod", "Gipoteza qo'yish (\"ko'proq tortsam, uzoqroq boradi\") va uni sinov orqali tekshirishni o'rgating."),
            ("Ma'lumotlarni tahlil qilish", "Bir nechta sinov natijasini solishtirib, xulosa chiqarishga undang."),
        ],
    },
},

"vint": {
    "concept": "vint (spiral) mexanizmining aylanma harakatni chiziqli harakatga aylantirishini",
    "A": {
        "lugat": [
            "Vint (Screw) – spiral shaklidagi, buralib ishlaydigan detal",
            "Burash (Twist/Turn) – vintni aylantirib harakatlantirish",
            "Yuqoriga-pastga (Up-down) – vint yordamida hosil bo'ladigan harakat yo'nalishi",
            "Spiral (Spiral) – aylana shaklida cho'ziluvchi chiziq",
            "Mahkamlash (Fasten) – vint yordamida ikki qismni birlashtirish",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Konservka qopqog'ini yoki shishani ochish-yopish harakati misol qilinadi.",
            ]),
            ("Vint qanday ishlaydi", 7, [
                "Vintni burasak, u yuqoriga yoki pastga siljishini o'qituvchi ko'rsatib beradi.",
                "O'quvchilar qo'lda kichik vint/shurup namunasini burab, harakatni his qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Vint qayerlarda ishlatilishini (shisha qopqog'i, shurup) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Qo'l motorikasi", "Vintni burashda qo'l harakatini nazorat qilishni mashq qildiring."),
            ("Sabr-toqat", "Vintni burash biroz vaqt talab qilishini, shoshilmaslik kerakligini tushuntiring."),
        ],
    },
    "B": {
        "lugat": [
            "Vint mexanizmi (Screw mechanism) – aylanma harakatni chiziqli harakatga aylantiruvchi spiral detal",
            "Qadam (Pitch) – vintning bir aylanishda qancha siljishi",
            "Buralish yo'nalishi (Thread direction) – vintning o'ng yoki chap tomonga buralishi",
            "Siljish (Displacement) – vint aylanishi natijasida hosil bo'lgan chiziqli harakat",
            "Ekstruziya (Extrusion) – vint yordamida moddani bir joydan boshqasiga siljitish",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Vint mexanizmi qayerlarda ishlatilishi (shurup, domkrat) haqida savol-javob.",
            ]),
            ("Aylanmadan chiziqli harakatga", 7, [
                "Vint (spiral) aylanma harakatni chiziqli harakatga qanday aylantirishi tushuntiriladi.",
                "Shurup yog'ochga kirib borishi yoki domkrat mashinani ko'tarishi misolida ko'rsatiladi.",
                "O'quvchilar vint mexanizmini aylantirib, siljishni kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Vint mexanizmining og'ir yukni kam kuch bilan ko'tarishdagi ahamiyati umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Aniqlik", "Vint mexanizmini yig'ishda bosqichlarni ketma-ket, chalkashtirmasdan bajarishni o'rgating."),
            ("Kuzatuvchanlik", "Vintning bir aylanishida qancha siljishini kuzatib, taxminiy hisoblashni so'rang."),
        ],
    },
    "C": {
        "lugat": [
            "Vint qadam (Screw pitch) – vintning bir to'liq aylanishida siljigan masofasi",
            "Mexanik yutuq (Mechanical advantage) – vint mexanizmi kuchni necha marta kuchaytirishi",
            "O'z-o'zini tormozlash (Self-locking) – vint mexanizmining tashqi kuchsiz o'z holatini saqlashi",
            "Arximed vinti (Archimedes' screw) – suyuqlik yoki moddani ko'tarish uchun qadimiy vint mexanizmi",
            "Ekstruziya bosimi (Extrusion pressure) – vint moddani siqib chiqarishda hosil qiladigan bosim",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Vint mexanizmining qadimdan (Arximed vinti) hozirgi kungacha qo'llanilishi haqida qisqacha tarixiy kirish.",
            ]),
            ("Mexanik yutuq va o'z-o'zini tormozlash", 7, [
                "Vint qadami kichik bo'lsa, mexanik yutuq (kuch kuchayishi) katta bo'lishi, lekin harakat sekinlashishi tushuntiriladi.",
                "Vint mexanizmining \"o'z-o'zini tormozlash\" xususiyati (masalan domkrat o'z-o'zidan pastga tushib ketmasligi) muhokama qilinadi.",
                "O'quvchilar bugungi modeldagi vint qadamini kuzatib, u qanchalik \"kuchli\" yoki \"tez\" ekanini baholaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Vint mexanizmining zamonaviy texnikada (domkrat, ekstruder, dron pervanesi) qo'llanilishi qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Vint qadami va tezlik/kuch o'rtasidagi murosani (tradeoff) muhokama qiling."),
            ("Tarixiy-ilmiy qiziqish", "Arximed vinti kabi qadimiy ixtirolarning zamonaviy texnikaga ta'sirini muhokama qiling."),
        ],
    },
},

"ishqalanish": {
    "concept": "ishqalanish kuchi va g'ildirakning harakatni osonlashtirishini",
    "A": {
        "lugat": [
            "Ishqalanish (Friction) – ikki sirt tegib harakatlanganda paydo bo'ladigan qarshilik",
            "G'ildirak (Wheel) – aylanib harakatni osonlashtiradigan dumaloq detal",
            "Silliq sirt (Smooth surface) – tekis, kam qarshilik beradigan yuza",
            "Notekis sirt (Rough surface) – g'adir-budur, ko'p qarshilik beradigan yuza",
            "Sirpanish (Slide) – g'ildiraksiz, sirt bo'ylab sudralib harakatlanish",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Muzda va asfaltda yurish qanday farq qilishi haqida suhbat.",
            ]),
            ("G'ildirak nega yordam beradi", 7, [
                "O'quvchilarga bir xil narsani avval g'ildiraksiz, keyin g'ildirak bilan itarib ko'rish taklif qilinadi.",
                "G'ildirak harakatni qanday osonlashtirishi qo'lda his qildiriladi.",
            ]),
            ("Yakunlash", 3, [
                "G'ildirak qayerlarda ishlatilishini (velosiped, arava) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Solishtirish ko'nikmasi", "Ikki holatni (g'ildirakli/g'ildiraksiz) solishtirib, farqni tushuntirishni so'rang."),
            ("Qiziqish", "Nega muzda yurish qiyinligi haqida savol berib, fikr yuritishga undang."),
        ],
    },
    "B": {
        "lugat": [
            "Ishqalanish kuchi (Friction force) – ikki sirt orasidagi harakatga qarshilik ko'rsatuvchi kuch",
            "Sirpanish ishqalanishi (Sliding friction) – sirt bo'ylab sudralganda yuzaga keladigan ishqalanish",
            "Aylanish ishqalanishi (Rolling friction) – g'ildirak aylanganda yuzaga keladigan, ancha kichik ishqalanish",
            "O'q (Axle) – g'ildirak aylanadigan markaziy tayoqcha",
            "Sirt g'adir-budurligi (Surface texture) – sirtning silliq yoki notekisligi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Nega mashinalar g'ildirakda yuradi, sirg'anib yurmaydi — savol-javob.",
            ]),
            ("Ishqalanish turlari", 7, [
                "Sirpanish ishqalanishi aylanish ishqalanishidan kattaligi, shu sababli g'ildirak harakatni osonlashtirishi tushuntiriladi.",
                "Silliq va notekis sirtlarda ishqalanish farqi muhokama qilinadi (masalan, muzda va asfaltda yurish).",
                "O'quvchilar bir xil modelni g'ildiraksiz va g'ildirak bilan itarib, kerakli kuchni taqqoslaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Ishqalanishning foydali (tormoz) va zararli (energiya yo'qotish) tomonlari umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Tahliliy fikrlash", "Ishqalanishning har doim ham yomon emasligini (tormoz uchun kerakligini) muhokama qiling."),
            ("Sinov o'tkazish", "Turli sirtlarda modelni sinab, natijalarni solishtirishni o'rgating."),
        ],
    },
    "C": {
        "lugat": [
            "Ishqalanish koeffitsienti (Coefficient of friction) – ikki sirt orasidagi ishqalanish darajasini bildiruvchi son",
            "Statik va kinetik ishqalanish (Static vs kinetic friction) – harakat boshlanishidagi va davomidagi ishqalanish turlari",
            "Aylanish ishqalanishi (Rolling resistance) – g'ildirakning deformatsiyasi tufayli yuzaga keladigan qarshilik",
            "Normal kuch (Normal force) – sirtning jismga perpendikulyar ta'sir qiluvchi kuchi",
            "Energiya yo'qotish (Energy dissipation) – ishqalanish tufayli mexanik energiyaning issiqlikka aylanishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Transport vositalarida ishqalanishni kamaytirish (moylash, podshipnik) muhandislik masalasi ekanligi muhokama qilinadi.",
            ]),
            ("Ishqalanish turlari va omillar", 7, [
                "Statik ishqalanish kinetik ishqalanishdan odatda kattaroq ekanligi (jism qo'zg'almasdan turgan holatda ko'proq qarshilik) tushuntiriladi.",
                "Ishqalanish sirt materiali va normal kuchga (og'irlikka) bog'liqligi muhokama qilinadi.",
                "O'quvchilar bugungi modelning g'ildiragiga qo'shimcha yuk qo'shib, ishqalanish/harakat qulayligiga ta'sirini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Ishqalanishni kamaytirish (moylash, podshipnik) va oshirish (tormoz, shina protektori) misollari qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Ishqalanishni kamaytirish kerak bo'lgan holatlar (harakat) va oshirish kerak bo'lgan holatlarni (tormoz) solishtiring."),
            ("Ilmiy sinov", "O'zgaruvchini (sirt turi, yuk) birma-bir o'zgartirib sinash usulini (bitta o'zgaruvchi qoidasi) o'rgating."),
        ],
    },
},

"kotargich": {
    "concept": "richag, vint va shkiv mexanizmlarining birgalikda og'ir yukni ko'tarishini",
    "A": {
        "lugat": [
            "Ko'tarish (Lift) – narsani pastdan yuqoriga olib chiqish",
            "Kran (Crane) – og'ir narsalarni ko'taradigan qurilma",
            "Qo'l/Strela (Arm/Boom) – kranning uzun, cho'zilgan qismi",
            "Yuk (Load) – ko'tariladigan og'ir narsa",
            "Tros (Cable) – yukni osib ko'tarishda ishlatiladigan mustahkam ip",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Qurilishda kranlarni qayerda ko'rganimiz haqida suhbat.",
            ]),
            ("Kran qanday yordam beradi", 7, [
                "Og'ir narsani odam kuchi bilan ko'tarib bo'lmasligi, mashina yordam berishi tushuntiriladi.",
                "O'quvchilar o'zlarining kichik kran namunasida yukni ko'tarishga harakat qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Kranlar qayerlarda ishlatilishini (qurilish, port) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Diqqat va aniqlik", "Kichik detallarni to'g'ri joylashtirish orqali sinchkovlikni rivojlantiring."),
            ("Jamoada ishlash", "Juftlikda ishlab, birga yukni ko'tarishga harakat qilishni tavsiya qiling."),
        ],
    },
    "B": {
        "lugat": [
            "Ko'tarish mexanizmi (Lifting mechanism) – og'ir yukni kam kuch bilan ko'taruvchi tizim",
            "Moment kuchi (Torque) – strelaning aylantiruvchi ta'siri",
            "Shkiv (Pulley) – tortish kuchini kamaytiruvchi aylanuvchi g'ildirak",
            "Konstruksiya barqarorligi (Structural stability) – kranning ag'darilmay turish qobiliyati",
            "Yuk sig'imi (Load capacity) – mexanizm ko'tara oladigan maksimal og'irlik",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Kran nima uchun kerak — og'ir yukni odam kuchi bilan ko'tarib bo'lmasligi muhokama qilinadi.",
            ]),
            ("Richag, shkiv va moment kuchi birgalikda", 7, [
                "Kran strelasi (uzun qo'l) nima uchun kerakligi — kuch yelkasi uzunroq bo'lsa moment kuchi oshishi tushuntiriladi.",
                "Shkiv yordamida kerakli ko'tarish kuchining kamayishi (lekin tros uzunroq tortilishi) tushuntiriladi.",
                "O'quvchilar strela uzunligini o'zgartirib, bu ko'tarish kuchiga qanday ta'sir qilishini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Kranning ishlash tamoyili (richag+shkiv) umumlashtiriladi, real hayotda qo'llanilishi (qurilish, port) muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Diqqat va aniqlik", "Bitta noto'g'ri detal butun mexanizmning ishlamay qolishiga sabab bo'lishi mumkinligini tushuntiring."),
            ("Muammoni tahlil qilish", "Yuk ko'tarilmasa, sababini (tros taranglik, richag uzunligi) birga qidirishni o'rgating."),
        ],
    },
    "C": {
        "lugat": [
            "Mexanik yutuq (Mechanical advantage) – mexanizm kuchni necha marta kuchaytirishi",
            "Yuk momenti (Load moment) – yukning strela uzunligiga ko'paytirilgan ta'siri",
            "Muvozanat kontr-vazni (Counterweight) – kranning ag'darilishining oldini oluvchi qarshi og'irlik",
            "Yuk diagrammasi (Load chart) – kranning strela uzunligiga qarab ko'tara oladigan yuk chegarasi",
            "Statik moment muvozanati (Static moment balance) – kranning ag'darilmasligi uchun momentlar tengligi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Zamonaviy qurilish kranlari va ularning yuk chegaralari haqida muhokama qilinadi.",
            ]),
            ("Yuk momenti va barqarorlik", 7, [
                "Strela uzunligi oshsa, bir xil yuk uchun moment (va ag'darilish xavfi) oshishi tushuntiriladi — shuning uchun uzoqroq strelada kamroq yuk ko'tariladi.",
                "Kontr-vazn (qarshi og'irlik) kranning ag'darilishining oldini qanday olishi muhokama qilinadi.",
                "O'quvchilar bugungi modelda strela uzunligi va ko'tarilayotgan yuk orasidagi bog'liqlikni sinaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Real qurilish kranlarining yuk diagrammasi tushunchasi qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Xavfsizlik chegaralari (maksimal yuk) nega muhim ekanini muhokama qiling."),
            ("Miqdoriy baholash", "Strela uzunligi va yuk orasidagi murosani taxminiy baholashga undang."),
        ],
    },
},

"motorAylanma": {
    "concept": "elektr motorning elektr energiyasini aylanma harakatga aylantirishini",
    "A": {
        "lugat": [
            "Motor (Motor) – elektr yordamida aylanadigan qurilma",
            "Elektr (Electricity) – qurilmalarni ishga tushiradigan energiya turi",
            "Aylanish (Spin) – motorning tez-tez o'z o'qi atrofida harakati",
            "Yoqish/O'chirish (On/Off) – motorni ishga tushirish yoki to'xtatish",
            "Tezlik (Speed) – motor qanchalik tez aylanishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Uyimizda motor bilan ishlaydigan narsalar (ventilyator, o'yinchoq) haqida suhbat.",
            ]),
            ("Motor qanday ishlaydi", 7, [
                "Motorga elektr berilganda u aylana boshlashi ko'rsatiladi (namoyish).",
                "Motorsiz va motorli modelni solishtirib, farqni his qildiramiz.",
            ]),
            ("Yakunlash", 3, [
                "Motor qayerlarda ishlatilishini (ventilyator, o'yinchoq mashina) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Xavfsizlik", "Motor ishlab turganda barmoqlarni aylanuvchi qismdan uzoq tutish kerakligini ta'kidlang."),
            ("Qiziqish", "Motor tezligini o'zgartirib, natijani kuzatishga undang."),
        ],
    },
    "B": {
        "lugat": [
            "Elektr motor (Electric motor) – elektr energiyasini aylanma harakatga aylantiruvchi qurilma",
            "Magnit maydon (Magnetic field) – motor ichida aylanishni hosil qiluvchi kuch maydoni",
            "Tok (Current) – motorni ishga tushiruvchi elektr oqimi",
            "Aylanish tezligi (RPM – revolutions per minute) – motorning bir daqiqadagi aylanishlar soni",
            "Yo'nalish (Direction) – motorning soat mili bo'yicha yoki teskarisiga aylanishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Motorli va motorsiz mexanizmlar orasidagi farq haqida savol-javob.",
            ]),
            ("Motorning ishlash tamoyili", 7, [
                "Elektr motor elektr energiyasini aylanma mexanik harakatga aylantirishi (magnit maydon va tok o'zaro ta'siri) sodda tilda tushuntiriladi.",
                "Motor tezligini o'zgartirish (agar controller imkon bersa) va yo'nalishni o'zgartirish ko'rsatiladi.",
                "O'quvchilar motorli modelni ishga tushirib, tezlikni turlicha sozlab sinaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Motorning kundalik hayotdagi (ventilyator, aylanuvchi o'yinchoq) qo'llanilishi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Ilmiy qiziqish", "Motorning ichida nima borligi haqida taxmin qilishga undang (elektromagnit haqida sodda tasavvur)."),
            ("Ehtiyotkorlik", "Motor va simlar bilan ishlashda ehtiyotkorlikni o'rgating."),
        ],
    },
    "C": {
        "lugat": [
            "Elektromagnit induksiya (Electromagnetic induction) – tok va magnit maydon o'zaro ta'sirida harakat hosil bo'lish hodisasi",
            "Moment (Torque) – motorning aylantiruvchi kuchi",
            "PWM (Pulse Width Modulation) – motor tezligini boshqarishning keng tarqalgan usuli",
            "Aylanish tezligi (RPM) – motorning bir daqiqadagi aylanishlar soni",
            "Samaradorlik (Efficiency) – motorga berilgan energiyaning foydali ishga aylanish nisbati",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Elektr motorlarining zamonaviy texnikadagi (robotlar, elektromobillar) keng qo'llanilishi muhokama qilinadi.",
            ]),
            ("Elektromagnit induksiya va boshqaruv", 7, [
                "Motor ichidagi magnit maydon va tok o'zaro ta'siri (elektromagnit induksiya) orqali aylanish hosil bo'lishi tushuntiriladi.",
                "Motor tezligini dasturiy boshqarish (controller orqali) tushunchasi kiritiladi.",
                "O'quvchilar controllerda tezlikni turli darajaga sozlab, moment va tezlik orasidagi bog'liqlikni kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Elektr motorlarining kelajakdagi texnika (elektromobillar, dronlar) uchun ahamiyati qisqacha muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Texnik qiziqish", "Motor xususiyatlarini (tezlik, moment) real hayotdagi qurilmalar bilan bog'lashga undang."),
            ("Aniq sozlash", "Controller sozlamalarini aniq va tizimli o'zgartirishni o'rgating."),
        ],
    },
},

"aero": {
    "concept": "aylanuvchi parrak havo massasini itarib reaktiv kuch hosil qilishini",
    "A": {
        "lugat": [
            "Parrak (Propeller) – aylanib havo yoki suvni itaruvchi detal",
            "Havo (Air) – atrofimizni o'rab turgan, ko'rinmas gaz",
            "Uchish (Fly) – havoda harakatlanish",
            "Itarish (Push) – narsani oldinga yoki yuqoriga siljitish",
            "Samolyot (Airplane) – havoda uchadigan transport vositasi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Samolyot va vertolyotlarni ko'rganmizmi, ular qanday uchadi degan savol-javob.",
            ]),
            ("Parrak qanday ishlaydi", 7, [
                "Parrak aylanganda havoni orqaga itarishi, bu esa modelni oldinga siljitishi ko'rsatiladi.",
                "O'quvchilar qo'lda kichik parrak/shamolchani aylantirib, havo harakatini his qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Parrak qayerlarda ishlatilishini (vertolyot, ventilyator) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Xavfsizlik", "Aylanuvchi parrakdan barmoqlarni uzoq tutish kerakligini ta'kidlang."),
            ("Kuzatuvchanlik", "Parrak tezligi oshsa nima o'zgarishini kuzatishga undang."),
        ],
    },
    "B": {
        "lugat": [
            "Aerodinamika (Aerodynamics) – havo harakati va uning jismlarga ta'sirini o'rganuvchi soha",
            "Reaktiv kuch (Reaction force) – bir tomonga itarilgan havoga javoban hosil bo'ladigan qarama-qarshi kuch",
            "Parrak qanoti (Propeller blade) – parrakning havoni itaruvchi qiya qismi",
            "Ko'tarish kuchi (Lift) – havo oqimi tufayli hosil bo'ladigan yuqoriga yo'naltirilgan kuch",
            "Tortish kuchi (Thrust) – parrak hosil qiladigan oldinga/yuqoriga itaruvchi kuch",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Vertolyot parragi va samolyot qanoti qanday farq qilishi haqida savol-javob.",
            ]),
            ("Reaktiv kuch tamoyili", 7, [
                "Aylanuvchi parrak havo massasini itarib, reaktiv kuch hosil qilishi (Nyutonning 3-qonuni: har bir ta'sirga teng va qarama-qarshi aks ta'sir) tushuntiriladi.",
                "Vertolyot parragi (ko'tarish) va samolyot qanoti (ko'tarish kuchi boshqacha hosil bo'ladi) farqi muhokama qilinadi.",
                "O'quvchilar parrak tezligini o'zgartirib, hosil bo'lgan kuchning o'zgarishini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Parrak asosidagi transport (dron, vertolyot) haqida qisqacha muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Ilmiy tushuntirish", "Nyutonning 3-qonunini o'z so'zi va misoli bilan tushuntirishni so'rang."),
            ("Xavfsizlik madaniyati", "Aylanuvchi qismlar bilan ishlashda xavfsizlik qoidalarini eslatib turing."),
        ],
    },
    "C": {
        "lugat": [
            "Nyutonning 3-qonuni (Newton's third law) – har bir ta'sirga teng va qarama-qarshi aks ta'sir mavjudligi",
            "Ko'tarish kuchi (Lift) – qanot/parrak shakli tufayli hosil bo'ladigan yuqoriga yo'naltirilgan aerodinamik kuch",
            "Tortish kuchi (Thrust) – dvigatel/parrak hosil qiladigan harakatlantiruvchi kuch",
            "Qarshilik kuchi (Drag) – havoning jism harakatiga qarshilik ko'rsatishi",
            "Hujum burchagi (Angle of attack) – qanot/parrakning havo oqimiga nisbatan burchagi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Havo transportining (samolyot, dron, vertolyot) zamonaviy ahamiyati muhokama qilinadi.",
            ]),
            ("Kuchlar muvozanati (parvoz)", 7, [
                "Nyutonning 3-qonuni parrak/qanot ishlashiga qanday tatbiq etilishi aniq tushuntiriladi.",
                "Ko'tarish, tortish, og'irlik va qarshilik kuchlari orasidagi muvozanat sodda tarzda ko'rsatiladi.",
                "O'quvchilar parrak burchagi yoki tezligini o'zgartirib, hosil bo'lgan kuchga ta'sirini muhokama qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Zamonaviy aviatsiya va dronlarda aerodinamika tamoyillarining qo'llanilishi qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Fizik tushuntirish", "Kuchlar muvozanatini diagramma kabi tasavvur qilib tushuntirishni so'rang."),
            ("Muhandislik qiziqishi", "Zamonaviy dron dizaynida aerodinamika qanday hisobga olinishini muhokama qiling."),
        ],
    },
},

"suv": {
    "concept": "suzuvchi vositalarning suv siqib chiqargan bosim kuchi tufayli suzishini",
    "A": {
        "lugat": [
            "Suzish (Float) – suv yuzasida cho'kmasdan turish",
            "Cho'kish (Sink) – suv tagiga tushib ketish",
            "Qayiq (Boat) – suvda suzadigan transport vositasi",
            "Suv (Water) – qayiq suzadigan suyuqlik",
            "Yengil/Og'ir (Light/Heavy) – narsaning og'irlik darajasi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Qayiqlar va kemalar suvda qanday yurishi haqida suhbat.",
            ]),
            ("Nima suzadi, nima cho'kadi", 7, [
                "Metall qayiq suzishi, lekin metall tosh cho'kishi haqida qiziqarli savol beriladi.",
                "O'quvchilarga (agar imkon bo'lsa) kichik suv idishida turli shakldagi narsalarni sinash taklif qilinadi.",
            ]),
            ("Yakunlash", 3, [
                "Qayiqlar qayerlarda ishlatilishini (dengiz, ko'l) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Kuzatuvchanlik", "Turli shakldagi narsalarning suzish-cho'kishini kuzatib, taxmin qilishni so'rang."),
            ("Ehtiyotkorlik", "Suv bilan ishlashda toza va tartibli bo'lishni o'rgating."),
        ],
    },
    "B": {
        "lugat": [
            "Suzuvchanlik kuchi (Buoyancy) – suv jismni yuqoriga itaruvchi kuch",
            "Arximed qonuni (Archimedes' principle) – jism suvda siqib chiqargan suv og'irligiga teng kuch bilan yuqoriga itarilishi",
            "Suv ostiga botish (Displacement) – jismning suv ichida egallagan hajmi",
            "Zichlik (Density) – jismning hajm birligidagi og'irligi",
            "Muvozanat (Balance) – og'irlik va suzuvchanlik kuchi teng bo'lgan holat",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Nega og'ir metall kema cho'kmasligi haqida qiziqarli savol beriladi.",
            ]),
            ("Arximed qonuni", 7, [
                "Suzuvchi vositalar suv siqib chiqargan bosim kuchi tufayli suv yuzasida qalqib turishi tushuntiriladi.",
                "Shakl (keng va yassi) suzishga qanday yordam berishi muhokama qilinadi.",
                "O'quvchilar model shaklini o'zgartirib (agar mumkin bo'lsa), suzish qobiliyatiga ta'sirini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Kemalar va qayiqlarning dizayni nega keng va yassi qilib yasalishi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Ilmiy tushuntirish", "Nega og'ir kema cho'kmasligini o'z so'zi bilan tushuntirishni so'rang."),
            ("Sinov o'tkazish", "Turli shakldagi modellarni sinab, natijalarni solishtirishni o'rgating."),
        ],
    },
    "C": {
        "lugat": [
            "Arximed qonuni (Archimedes' principle) – suyuqlikka botirilgan jism, siqib chiqargan suyuqlik og'irligiga teng kuch bilan yuqoriga itariladi",
            "Suzuvchanlik kuchi (Buoyant force) – suyuqlik jismga ta'sir qiluvchi yuqoriga yo'naltirilgan kuch",
            "Zichlik (Density) – massaning hajmga nisbati, suzish-cho'kishni belgilovchi asosiy omil",
            "Siqib chiqarilgan hajm (Displaced volume) – jism suv ichiga botirilganda egallaydigan hajm",
            "Barqarorlik markazi (Metacenter) – suzuvchi vositaning muvozanatini belgilovchi nazariy nuqta",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Katta okean kemalarining og'irligiga qaramay suzishi muhandislik hodisasi sifatida muhokama qilinadi.",
            ]),
            ("Zichlik va suzuvchanlik kuchi", 7, [
                "Arximed qonuni aniq shaklda tushuntiriladi: siqib chiqarilgan suyuqlik og'irligi = suzuvchanlik kuchi.",
                "Jismning o'rtacha zichligi suvdan kichik bo'lsa suzishi, kattaroq bo'lsa cho'kishi tushuntiriladi (shakl orqali zichlikni \"kamaytirish\" mumkinligi bilan).",
                "O'quvchilar model shaklini o'zgartirib, ko'proq yuk ko'tarish (suzib turgan holda) sinovini o'tkazadilar.",
            ]),
            ("Yakunlash", 3, [
                "Zamonaviy kemasozlikda barqarorlik va yuk sig'imi masalalari qisqacha muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Shaklni optimallashtirib ko'proq yuk ko'tarishga erishish g'oyasini muhokama qiling."),
            ("Miqdoriy tahlil", "Zichlik tushunchasini sonli misollar bilan mustahkamlang."),
        ],
    },
},

"biomimikriya": {
    "concept": "hayvon-robotlarning tabiiy harakatlarni mexanizm orqali taqlid qilishini (biomimikriya)",
    "A": {
        "lugat": [
            "Hayvon (Animal) – tabiatda yashovchi jonzot",
            "Taqlid qilish (Imitate/Copy) – boshqa narsaga o'xshab harakat qilish",
            "Oyoq (Leg) – hayvon yoki robot yuradigan qism",
            "Harakat (Movement) – joydan-joyga siljish",
            "Robot-hayvon (Animal robot) – hayvonga o'xshab yasalgan robot",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Sevimli hayvonlar qanday harakat qilishi (yurish, sakrash) haqida suhbat.",
            ]),
            ("Robot hayvonga qanday o'xshaydi", 7, [
                "Robot-hayvonning oyoq yoki dumi qanday harakat qilishi ko'rsatiladi (motor aylanishi orqali).",
                "O'quvchilar qo'lda mexanizmni aylantirib, \"hayvon harakati\"ga o'xshashligini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Qaysi hayvonlarga o'xshash robotlar bor ekanini birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Ijodiy tasavvur", "Robotning qaysi hayvonga o'xshashini o'z so'zi bilan tasvirlashni so'rang."),
            ("Kuzatuvchanlik", "Haqiqiy hayvon harakati bilan robot harakatini solishtirishga undang."),
        ],
    },
    "B": {
        "lugat": [
            "Biomimikriya (Biomimicry) – tabiatdan ilhomlanib muhandislik yechimi yaratish",
            "Krivoship-shatun mexanizmi (Crank mechanism) – hayvon oyoq/dum harakatini taqlid qiluvchi tizim",
            "Harakat naqshi (Gait pattern) – hayvonning yurish yoki yugurish tartibi",
            "Moslashuv (Adaptation) – tabiatdagi jonzotlarning muhitga moslashishi",
            "Prototip (Prototype) – g'oyani sinab ko'rish uchun yasalgan dastlabki model",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Muhandislar tabiatdan qanday g'oya olishi (masalan, qush qanotidan samolyot) haqida savol-javob.",
            ]),
            ("Biomimikriya tamoyili", 7, [
                "Hayvon-robotlar oyoq yoki dum harakatini qanday mexanizm (odatda krivoship-shatun) orqali taqlid qilishi tushuntiriladi.",
                "Muhandislik va tabiat orasidagi bog'liqlik (biomimikriya atamasi) misollar bilan tushuntiriladi.",
                "O'quvchilar modelning harakatini haqiqiy hayvon harakati bilan solishtiradilar.",
            ]),
            ("Yakunlash", 3, [
                "Boshqa biomimikriya misollari (Velcro, suzuvchi kiyim) qisqacha aytib o'tiladi.",
            ]),
        ],
        "softskills": [
            ("Ijodiy tafakkur", "O'z modelini boshqa hayvon harakatiga o'xshatib o'zgartirish g'oyasini so'rang."),
            ("Tabiatga qiziqish", "Tabiatdagi boshqa hayvonlarning qiziqarli harakatlarini eslashga undang."),
        ],
    },
    "C": {
        "lugat": [
            "Biomimikriya (Biomimicry) – tabiiy tizimlardan ilhomlanib muhandislik yechimlari yaratish sohasi",
            "Kinematik zanjir (Kinematic chain) – bo'g'inlar orqali bog'langan harakatlanuvchi qismlar tizimi",
            "Harakat naqshi (Gait) – ko'p oyoqli jonzot/robotning oyoqlarni ketma-ket qo'yish tartibi",
            "Moslashuvchan dizayn (Adaptive design) – muhitga qarab o'zgaruvchan muhandislik yechimi",
            "Biomexanika (Biomechanics) – tirik organizmlarning mexanik harakatini o'rganuvchi soha",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Zamonaviy robototexnikada biomimikriyaning ahamiyati (masalan, Boston Dynamics robotlari) muhokama qilinadi.",
            ]),
            ("Biomexanika va mexanizm", 7, [
                "Hayvonlarning oyoq/dum harakati krivoship-shatun kabi mexanik zanjirlar orqali qanday taqlid qilinishi chuqurroq tushuntiriladi.",
                "Turli hayvonlarning harakat naqshlari (masalan, to'rt oyoqli yurish tartibi) qisqacha muhokama qilinadi.",
                "O'quvchilar o'z modelining harakat mexanizmini tahlil qilib, uni yaxshilash g'oyalarini taklif qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Biomimikriyaning boshqa sohalardagi (materiallar, arxitektura) qo'llanilishi qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Tanqidiy va ijodiy fikrlash", "Tabiiy tizimni tahlil qilib, undan texnik yechim chiqarish jarayonini muhokama qiling."),
            ("Tadqiqotchilik", "Boshqa biomimikriya misollarini mustaqil qidirib topishga undang (uyga vazifa sifatida ham)."),
        ],
    },
},

"sensor": {
    "concept": "sensorning atrof-muhitdagi o'zgarishni elektr signaliga aylantirishini",
    "A": {
        "lugat": [
            "Sensor (Sensor) – atrofdagi o'zgarishni \"sezadigan\" qurilma",
            "Sezish (Sense/Feel) – biror narsani aniqlash",
            "Signal (Signal) – sensordan kelayotgan xabar",
            "Yaqin/Uzoq (Near/Far) – masofa sensori aniqlaydigan holat",
            "Reaksiya (Reaction) – sensor signaliga javob sifatida sodir bo'ladigan harakat",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Ko'zimiz va qo'limiz qanday \"sezishi\" (ko'rish, ushlab bilish) haqida suhbat.",
            ]),
            ("Sensor qanday ishlaydi", 7, [
                "Sensor atrof-muhitdagi o'zgarishni (yorug'lik, masofa) \"sezishi\" tushuntiriladi.",
                "O'quvchilar qo'lini sensorga yaqinlashtirib, robot reaksiyasini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Sensorlar qayerlarda ishlatilishini (avtomatik eshik, telefon) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Kuzatuvchanlik", "Sensor signalga qanday reaksiya berishini diqqat bilan kuzatishni so'rang."),
            ("Qiziqish", "Sensorni turli masofada sinab, natijani solishtirishga undang."),
        ],
    },
    "B": {
        "lugat": [
            "Sensor (Sensor) – fizik o'zgarishni elektr signaliga aylantiruvchi qurilma",
            "Signal (Signal) – sensordan controllerga uzatiladigan ma'lumot",
            "Masofa sensori (Distance sensor) – to'siqgacha bo'lgan masofani aniqlovchi sensor",
            "Harakat sensori (Motion sensor) – harakatni aniqlovchi sensor",
            "Chegara qiymati (Threshold) – sensor reaksiya boshlaydigan chegara",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Inson sezgi organlari (ko'z, teri) bilan sensorlar orasidagi o'xshashlik muhokama qilinadi.",
            ]),
            ("Sensordan reaksiyagacha", 7, [
                "Sensor atrof-muhitdagi fizik o'zgarishni (yorug'lik, masofa, bosim, harakat) elektr signaliga qanday aylantirishi tushuntiriladi.",
                "Signal controllerga uzatilib, unga qarab robot harakat qilishi (reaksiya) ko'rsatiladi.",
                "O'quvchilar sensor chegara qiymatini (masalan, qay masofada reaksiya berishi) sinab ko'radilar.",
            ]),
            ("Yakunlash", 3, [
                "Sensorlarning kundalik hayotda (avtomatik eshik, yorug'lik o'chirgich) qo'llanilishi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Mantiqiy fikrlash", "Sensor signalidan robot reaksiyasigacha bo'lgan zanjirni tushuntirishni so'rang."),
            ("Sinov va sozlash", "Sensor chegara qiymatini sozlab, optimal natijani topishni o'rgating."),
        ],
    },
    "C": {
        "lugat": [
            "Sensor (Sensor) – fizik kattalikni o'lchab, elektr signaliga aylantiruvchi qurilma",
            "Analog va raqamli signal (Analog vs digital signal) – sensor signalining ikki asosiy turi",
            "Kalibrlash (Calibration) – sensorni aniq ishlashi uchun sozlash jarayoni",
            "Sezgirlik (Sensitivity) – sensorning kichik o'zgarishlarni aniqlay olish darajasi",
            "Fikr-aylanish (Feedback loop) – sensor-qaror-harakat-qayta sensor tsikli",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Zamonaviy \"aqlli\" qurilmalarda (telefon, avtomobil) sensorlarning roli muhokama qilinadi.",
            ]),
            ("Fikr-aylanish tizimi", 7, [
                "Sensor-qaror-harakat-qayta sensor (feedback loop) tsikli tushuntiriladi — bu robotni \"aqlli\" qiladigan asosiy mexanizm.",
                "Analog va raqamli signal farqi sodda misolda ko'rsatiladi.",
                "O'quvchilar sensorni kalibrlab (chegara qiymatini sozlab), aniqroq ishlashiga erishadilar.",
            ]),
            ("Yakunlash", 3, [
                "Sensorlarning avtonom robototexnika va sun'iy intellekt tizimlaridagi ahamiyati qisqacha muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Tizimli fikrlash", "Sensor-qaror-harakat zanjirini bosqichma-bosqich tahlil qilishni o'rgating."),
            ("Aniq sozlash (kalibrlash)", "Sensorni turli sharoitda sinab, eng barqaror sozlamani topishga undang."),
        ],
    },
},

"kosmik": {
    "concept": "kosmik texnika notekis yuzada harakatlanish uchun maxsus g'ildirak/oyoq tizimlaridan foydalanishini",
    "A": {
        "lugat": [
            "Kosmos (Space) – Yerdan tashqaridagi katta bo'shliq",
            "Oy (Moon) – Yer atrofida aylanadigan osmon jismi",
            "Rover (Rover) – kosmosda yuruvchi maxsus mashina",
            "Notekis yuza (Rough surface) – tosh-qumli, tekis bo'lmagan yer",
            "G'ildirak (Wheel) – roverning harakatlanishiga yordam beruvchi dumaloq qism",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Oy va boshqa sayyoralar haqida qiziqarli suhbat, rasm yoki video.",
            ]),
            ("Rover qanday harakatlanadi", 7, [
                "Oy yuzasi tekis emasligi, shuning uchun maxsus g'ildirak kerakligi tushuntiriladi.",
                "O'quvchilar rover modelini notekis (masalan gilam ustida) sirtda sinab ko'radilar.",
            ]),
            ("Yakunlash", 3, [
                "Kosmosga uchgan roverlar haqida qiziqarli faktlar aytib o'tiladi.",
            ]),
        ],
        "softskills": [
            ("Qiziqish va tadqiqotchilik", "Kosmos haqida savol berishga va o'z fikrini bildirishga undang."),
            ("Sinov o'tkazish", "Roverni turli yuzada sinab, farqni kuzatishni o'rgating."),
        ],
    },
    "B": {
        "lugat": [
            "Rover (Rover) – boshqa sayyora/oy yuzasida harakatlanadigan avtomatik/masofadan boshqariladigan mashina",
            "Notekis yuza (Rough terrain) – tosh-qumli, tekis bo'lmagan yuza",
            "Ko'p g'ildirakli tizim (Multi-wheel drive) – barqarorlik uchun ko'p g'ildirakdan foydalanish",
            "Bo'shliq (Vacuum) – havo bo'lmagan kosmik muhit",
            "Gravitatsiya (Gravity) – jismlarni tortib turuvchi kuch, sayyoralarda har xil bo'ladi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Nega kosmik roverlar oddiy mashinaga o'xshamasligi haqida savol-javob.",
            ]),
            ("Notekis yuzada harakat", 7, [
                "Kosmik texnika (rover) nega maxsus g'ildirak/oyoq tizimidan foydalanishi tushuntiriladi — notekis, tosh-qumli yuzada oddiy g'ildirak siqilib qolishi mumkin.",
                "Oy/Mars yuzasi bilan Yer yuzasi solishtiriladi (gravitatsiya, tuproq turi).",
                "O'quvchilar rover modelini notekis sirtda sinab, harakatlanish qulayligini baholaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Haqiqiy kosmik roverlar (Mars roverlari) haqida qisqacha aytib o'tiladi.",
            ]),
        ],
        "softskills": [
            ("Tadqiqotchilik", "Kosmik missiyalar haqida qiziqarli faktlarni izlashga undang."),
            ("Muammoni hal qilish", "Rover to'siqqa duch kelsa, qanday yechim topish mumkinligini muhokama qiling."),
        ],
    },
    "C": {
        "lugat": [
            "Planetar rover (Planetary rover) – boshqa sayyora yuzasida ilmiy tadqiqot olib boruvchi avtomatik mashina",
            "Yer bosimi (Ground pressure) – g'ildirak yuzaga tushiradigan bosim, botib ketishga ta'sir qiladi",
            "Regolit (Regolith) – Oy/Mars yuzasini qoplagan mayda tosh-chang qatlami",
            "Avtonom navigatsiya (Autonomous navigation) – roverning odam yordamisiz yo'l topishi",
            "Radiatsiya himoyasi (Radiation shielding) – kosmik nurlanishdan himoyalanish tizimi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Zamonaviy Mars/Oy missiyalari (rover loyihalari) haqida muhokama qilinadi.",
            ]),
            ("Muhandislik yechimlari", 7, [
                "Yer bosimini kamaytirish uchun keng g'ildirak yoki ko'p g'ildirakli tizim ishlatilishi tushuntiriladi.",
                "Regolit (chang-tosh) qatlamida oddiy g'ildirak botib qolishi, shuning uchun maxsus dizayn kerakligi muhokama qilinadi.",
                "O'quvchilar bugungi rover modelining g'ildirak/oyoq dizaynini tahlil qilib, yaxshilash g'oyalarini taklif qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Kelajakdagi kosmik missiyalar uchun robototexnika qanday rivojlanayotgani qisqacha muhokama qilinadi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik ijodkorligi", "Cheklangan resurslar (kosmosda ta'mirlash imkoni yo'q) sharoitida ishonchli dizayn yaratish muhimligini muhokama qiling."),
            ("Ilmiy qiziqish", "Kosmik tadqiqotlarning kelajagi haqida fikr almashishga undang."),
        ],
    },
},

"transport": {
    "concept": "transport vositasi g'ildirak va o'q yordamida harakatni tekis va samarali qilishini",
    "A": {
        "lugat": [
            "Transport (Transport) – odam yoki narsani bir joydan boshqasiga olib boruvchi vosita",
            "Mashina (Car) – g'ildirakli transport vositasi",
            "G'ildirak (Wheel) – mashinaning aylanib yuradigan dumaloq qismi",
            "O'q (Axle) – g'ildirak aylanadigan tayoqcha",
            "Yurish (Drive/Move) – transportning joydan-joyga siljishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Ko'chada ko'rgan turli transport vositalari haqida suhbat.",
            ]),
            ("Mashina qanday yuradi", 7, [
                "G'ildirak va o'q mashinaga harakat qilishga qanday yordam berishi ko'rsatiladi.",
                "O'quvchilar o'z mashina modellarini itarib, harakatini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Turli transport vositalarini (mashina, yuk mashinasi, poyezd) birga sanaymiz.",
            ]),
        ],
        "softskills": [
            ("Jamoada ishlash", "Yo'l qoidalari va navbat kutish kabi kundalik ko'nikmalarni transport mavzusi orqali eslatib o'ting."),
            ("Ijodkorlik", "O'z mashinasini bezashga yoki nomlashga undang."),
        ],
    },
    "B": {
        "lugat": [
            "Shassi (Chassis) – transport vositasining asosiy tayanch qismi",
            "O'q (Axle) – g'ildirak aylanadigan tayoqcha",
            "Ishqalanish (Friction) – g'ildirak va yo'l orasidagi qarshilik",
            "Yurish tizimi (Drivetrain) – motordan g'ildirakkacha kuchni uzatuvchi tizim",
            "Barqarorlik (Stability) – transportning harakatda yiqilmay/ag'darilmay yurishi",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Turli transport vositalarining (yengil mashina, yuk mashinasi) tuzilishidagi farqlar haqida savol-javob.",
            ]),
            ("G'ildirak-o'q tizimi", 7, [
                "Transport vositasi g'ildirak-o'q yordamida ishqalanishni kamaytirib, motor kuchini tekis harakatga aylantirishi tushuntiriladi.",
                "Yuk mashinasi nega ko'p g'ildirakli bo'lishi (og'irlik taqsimoti) muhokama qilinadi.",
                "O'quvchilar modelning g'ildiraklari soni/joylashuvini tahlil qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Transport dizaynining maqsadga (tezlik, yuk ko'tarish) qarab farqlanishi umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Tahliliy fikrlash", "Transport dizayni uning vazifasiga (tezyurar yoki yukyurar) qanday bog'liqligini muhokama qiling."),
            ("Diqqat va aniqlik", "G'ildiraklarning to'g'ri va bir tekis o'rnatilishi harakat sifatiga ta'sir qilishini ta'kidlang."),
        ],
    },
    "C": {
        "lugat": [
            "Yurish tizimi (Drivetrain) – motordan g'ildirakkacha kuch va harakatni uzatuvchi to'liq tizim",
            "Og'irlik taqsimoti (Weight distribution) – transportning og'irligi g'ildiraklar bo'ylab qanday taqsimlanishi",
            "Burilish radiusi (Turning radius) – transportning minimal burilish doirasi",
            "Muallaq osma tizim (Suspension) – g'ildirak va shassi orasidagi zarbani yutuvchi tizim",
            "Differensial (Differential) – burilishda g'ildiraklarga turli tezlik beruvchi mexanizm",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Zamonaviy transport muhandisligi (avtomobil, poyezd) qanday murakkab tizimlardan tashkil topgani muhokama qilinadi.",
            ]),
            ("Kuch uzatish va barqarorlik", 7, [
                "Og'irlik taqsimoti transportning barqarorligi va boshqaruvchanligiga qanday ta'sir qilishi tushuntiriladi.",
                "Differensial mexanizm burilishda g'ildiraklarga nima uchun turli tezlik berishi (tushuncha darajasida) muhokama qilinadi.",
                "O'quvchilar bugungi modelning yurish tizimini tahlil qilib, yaxshilash imkoniyatlarini taklif qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Zamonaviy transport texnologiyalari (elektromobil, avtonom mashinalar) qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Muhandislik fikrlashi", "Transport dizaynidagi murosalarni (tezlik vs barqarorlik vs yuk sig'imi) muhokama qiling."),
            ("Tizimli tahlil", "Yurish tizimini bosqichma-bosqich (motor->uzatma->g'ildirak) tahlil qilishni o'rgating."),
        ],
    },
},

"darvoza": {
    "concept": "avtomatik mexanizmning richag yoki vint orqali ochilib-yopilishini",
    "A": {
        "lugat": [
            "Darvoza (Gate) – kirish-chiqish uchun ochiladigan-yopiladigan to'siq",
            "Ochish (Open) – darvozani yo'l bo'shatib qo'yish",
            "Yopish (Close) – darvozani to'siq qilib qo'yish",
            "Avtomatik (Automatic) – o'z-o'zidan, odam kuchisiz ishlaydigan",
            "Mexanizm (Mechanism) – harakatni bajaruvchi qurilma qismlari",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Avtomatik eshik yoki darvozalarni ko'rganmizmi (do'kon, avtoturargoh) haqida suhbat.",
            ]),
            ("Darvoza qanday ochiladi-yopiladi", 7, [
                "Darvoza richag yoki vint yordamida ochilib-yopilishi ko'rsatiladi.",
                "O'quvchilar o'z darvoza modelini qo'lda yoki motor bilan ochib-yopib sinaydilar.",
            ]),
            ("Yakunlash", 3, [
                "Uy eshigi bilan avtomatik darvozani solishtiramiz.",
            ]),
        ],
        "softskills": [
            ("Diqqat", "Mexanizm harakatini kuzatib, qaysi qism harakatlanishini aytishni so'rang."),
            ("Jamoada ishlash", "Juftlikda ishlab, birga sinashni tavsiya qiling."),
        ],
    },
    "B": {
        "lugat": [
            "Avtomatik mexanizm (Automatic mechanism) – odam kuchisiz, motor/sensor yordamida ishlovchi tizim",
            "Richag (Lever) – darvozani ko'taruvchi/suruvchi qattiq qism",
            "Vint mexanizmi (Screw mechanism) – aylanma harakatni chiziqli harakatga aylantiruvchi tizim",
            "Ochiq/Yopiq holat (Open/Closed state) – darvozaning ikki asosiy holati",
            "Chegaralovchi (Limit) – darvozaning qanchagacha ochilishi/yopilishini belgilovchi qism",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Avtomatik darvozalar qayerlarda ishlatilishi (avtoturargoh, sanoat) haqida savol-javob.",
            ]),
            ("Richag va vint mexanizmi birgalikda", 7, [
                "Avtomatik darvoza yoki eshik richag yoki vint mexanizmi orqali qanday ochilib-yopilishi tushuntiriladi.",
                "Uy eshigi (qo'lda) bilan avtomatik darvoza (motor bilan) solishtiriladi.",
                "O'quvchilar darvoza mexanizmini motor bilan ishga tushirib, ochilish-yopilish vaqtini kuzatadilar.",
            ]),
            ("Yakunlash", 3, [
                "Avtomatik darvozalarning xavfsizlik va qulaylik jihatlari umumlashtiriladi.",
            ]),
        ],
        "softskills": [
            ("Muammoni tahlil qilish", "Darvoza to'liq ochilmasa/yopilmasa, sababini (mexanizm cheklovi) birga qidirishni o'rgating."),
            ("Aniqlik", "Mexanizmning aniq va bir tekis ishlashi uchun detallarni tekshirishni o'rgating."),
        ],
    },
    "C": {
        "lugat": [
            "Aktuator (Actuator) – boshqaruv signalini mexanik harakatga aylantiruvchi qurilma (bu yerda motor)",
            "Chegara kalitlari (Limit switches) – mexanizmning chegara holatini aniqlovchi elementlar",
            "Kuch uzatish zanjiri (Force transmission chain) – motordan darvozagacha kuch uzatiladigan yo'l",
            "Xavfsizlik to'xtatish (Safety stop) – to'siq bo'lsa mexanizmni to'xtatuvchi tizim",
            "Sikl vaqti (Cycle time) – darvozaning to'liq ochilib-yopilishiga ketadigan vaqt",
        ],
        "nazariya": [
            ("Kirish", 5, [
                "Sanoat va aqlli uy tizimlaridagi avtomatik darvoza/eshik yechimlari muhokama qilinadi.",
            ]),
            ("Avtomatlashtirilgan mexanizm dizayni", 7, [
                "Richag va vint mexanizmlarining kombinatsiyasi qanday ishonchli avtomatik harakat berishi tushuntiriladi.",
                "Xavfsizlik uchun to'siqni sezib to'xtash tizimlari (sensor bilan birgalikda) muhokama qilinadi.",
                "O'quvchilar mexanizm sikl vaqtini o'lchab, uni tezlashtirish yo'llarini muhokama qiladilar.",
            ]),
            ("Yakunlash", 3, [
                "Aqlli uy va sanoat avtomatlashtirish tizimlaridagi shunga o'xshash mexanizmlar qisqacha ko'rib chiqiladi.",
            ]),
        ],
        "softskills": [
            ("Xavfsizlikka yo'naltirilgan dizayn", "Avtomatik mexanizmlarda xavfsizlik nega birinchi o'rinda turishi kerakligini muhokama qiling."),
            ("Optimallashtirish fikri", "Mexanizmni tezroq va ishonchliroq qilish g'oyalarini muhokama qiling."),
        ],
    },
},

}
