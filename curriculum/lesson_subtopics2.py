# -*- coding: utf-8 -*-
"""
Sub-mavzular — 2-qism: elastik, ishqalanish, motor, aerodinamika, suv, transport,
darvoza, biomimikriya, sensor, kosmik temalar.
Format lesson_subtopics.py bilan bir xil.
"""

SUBTOPICS2 = {}

# ---------------------------------------------------------------------------
# ELASTIK ENERGIYA (8 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["elastik"] = [
    {
        "fokus": "Elastik jism nima",
        "savol": "Rezinani cho'zib qo'yib yuborsak, u nima qiladi?",
        "asosiy": [
            "Elastik jism cho'zilgandan keyin yana avvalgi shakliga qaytadi.",
            "Rezina, prujina — elastik jismlarga misol.",
            "Loy yoki qog'oz esa elastik emas — ular qaytmaydi.",
        ],
        "chuqur": "Elastiklik chegarasi bor: haddan tashqari cho'zilsa, jism qaytmaydi yoki uziladi.",
        "tajriba": "Modeldagi elastik elementni asta cho'zib, qo'yib yuborilganda qaytishini kuzatish.",
        "uyga": "Uyda elastik va elastik bo'lmagan 2 tadan narsa toping va ro'yxat qiling.",
    },
    {
        "fokus": "Cho'zilgan rezinada energiya to'planadi",
        "savol": "Cho'zilgan rezina qayerdan kuch oladi?",
        "asosiy": [
            "Rezinani cho'zganda unda energiya to'planadi.",
            "Bu energiya \"zaxirada\" turadi va ko'rinmaydi.",
            "Qo'yib yuborilganda u harakatga aylanadi.",
        ],
        "chuqur": "Bu potensial energiya deb ataladi — jismning holati tufayli ega bo'lgan energiya.",
        "tajriba": "Rezinani turlicha cho'zib, model qanchalik uzoq/tez harakat qilishini kuzatish.",
        "uyga": "Cho'zilgan rezina va cho'zilmagan rezinani solishtirib, farqni yozing.",
    },
    {
        "fokus": "Energiya harakatga aylanadi",
        "savol": "To'plangan energiya qayoqqa ketadi?",
        "asosiy": [
            "Qo'yib yuborilganda to'plangan energiya harakat energiyasiga aylanadi.",
            "Model oldinga otiladi yoki tez harakatlanadi.",
            "Energiya yo'qolmaydi — u faqat bir turdan boshqasiga o'tadi.",
        ],
        "chuqur": "Bu energiya saqlanishi qonuni: energiya yaralmaydi va yo'qolmaydi, faqat shaklini o'zgartiradi.",
        "tajriba": "Modelni qo'yib yuborib, qanchalik uzoq borishini o'lchash yoki qadamlar bilan sanash.",
        "uyga": "Cho'zilgan rezina qanday qilib harakat berishini o'z so'zingiz bilan tushuntiring.",
    },
    {
        "fokus": "Cho'zish kuchi va bosib o'tilgan masofa",
        "savol": "Ko'proq cho'zsak, model uzoqroq boradimi?",
        "asosiy": [
            "Rezina qanchalik ko'p cho'zilsa, shunchalik ko'p energiya to'planadi.",
            "Ko'p energiya — uzoqroq masofa.",
            "Lekin haddan ortiq cho'zish rezinani buzishi mumkin.",
        ],
        "chuqur": "Bog'liqlik chiziqli emas — ikki barobar cho'zish to'rt barobar energiya berishi mumkin.",
        "tajriba": "Modelni 3 xil darajada cho'zib qo'yib yuborish va bosib o'tgan masofani taqqoslash.",
        "uyga": "3 xil cho'zishda model qancha yurganini jadval qilib yozing.",
    },
    {
        "fokus": "Inersiya — harakat davom etadi",
        "savol": "Rezina to'xtaganidan keyin ham model nega yuraveradi?",
        "asosiy": [
            "Harakatga tushgan jism o'z-o'zidan to'xtamaydi.",
            "Uni to'xtatish uchun boshqa kuch (ishqalanish) kerak.",
            "Bu Nyutonning 1-qonuni — inersiya qonuni.",
        ],
        "chuqur": "Ideal sharoitda (ishqalanishsiz) jism cheksiz harakatda davom etardi.",
        "tajriba": "Modelni qo'yib yuborib, rezina bo'shaganidan keyin ham u qancha masofa yurishini kuzatish.",
        "uyga": "Avtobus birdan to'xtaganda nega oldinga intilamiz — inersiya bilan tushuntiring.",
    },
    {
        "fokus": "Pull-back mexanizmi",
        "savol": "O'yinchoq mashinani orqaga tortsak nega oldinga yuguradi?",
        "asosiy": [
            "Orqaga tortganda ichidagi prujina buraladi va energiya to'playdi.",
            "Qo'yib yuborilganda prujina bo'shalib, g'ildirakni aylantiradi.",
            "Shuning uchun mashina oldinga yuguradi.",
        ],
        "chuqur": "Pull-back mexanizmida energiya g'ildirak orqali kiritiladi va yana g'ildirak orqali chiqariladi.",
        "tajriba": "Modelni turli masofaga orqaga tortib qo'yib yuborish va natijani taqqoslash.",
        "uyga": "Pull-back o'yinchoq bo'lsa, uni turli masofaga tortib sinang va natijani yozing.",
    },
    {
        "fokus": "Sirt turi natijaga qanday ta'sir qiladi",
        "savol": "Bir xil model gilamda va stolda bir xil yuradimi?",
        "asosiy": [
            "Silliq sirtda model uzoqroq yuradi.",
            "G'adir-budur sirtda tezroq to'xtaydi.",
            "Chunki notekis sirt ko'proq ishqalanish beradi.",
        ],
        "chuqur": "Ishqalanish harakat energiyasini issiqlikka aylantirib \"yo'q qiladi\" — shuning uchun model to'xtaydi.",
        "tajriba": "Modelni 2 xil sirtda (stol va gilam) sinab, bosib o'tgan masofani taqqoslash.",
        "uyga": "Modelni uyda 2 xil sirtda sinab, qaysi birida uzoqroq yurganini yozing.",
    },
    {
        "fokus": "Energiya qayerga yo'qoladi",
        "savol": "Model nega oxir-oqibat to'xtaydi?",
        "asosiy": [
            "Harakat energiyasi ishqalanish tufayli asta-sekin kamayadi.",
            "U issiqlikka aylanadi (juda oz miqdorda).",
            "Shuning uchun hech qanday model cheksiz yura olmaydi.",
        ],
        "chuqur": "Energiya yo'qolmaydi — u foydasiz shaklga (issiqlik, tovush) o'tadi; buni \"energiya tarqalishi\" deyiladi.",
        "tajriba": "Modelni bir necha marta ishlatib, g'ildirak o'qi qiziganini (yoki qarshilik ortganini) sezishga harakat qilish.",
        "uyga": "Qo'lingizni bir-biriga tez ishqalab, nima sezishingizni va nega ekanini yozing.",
    },
]

# ---------------------------------------------------------------------------
# ISHQALANISH (8 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["ishqalanish"] = [
    {
        "fokus": "Ishqalanish nima",
        "savol": "Nega yerda surilayotgan quti o'z-o'zidan to'xtaydi?",
        "asosiy": [
            "Ishqalanish — ikki sirt tegib harakatlanganda paydo bo'ladigan qarshilik.",
            "U harakatga qarshi yo'nalgan bo'ladi.",
            "Shuning uchun harakatdagi jism sekinlashadi.",
        ],
        "chuqur": "Ishqalanish sirtlarning mikroskopik notekisliklari bir-biriga ilashib qolishidan kelib chiqadi.",
        "tajriba": "Modelni qo'l bilan surib, qarshilikni his qilish va uni g'ildirakli holat bilan taqqoslash.",
        "uyga": "Ishqalanish sezilib turadigan 2 ta holatni yozing (masalan, muzda yurish).",
    },
    {
        "fokus": "G'ildirak ishqalanishni kamaytiradi",
        "savol": "Nega og'ir yukni g'ildirakli aravada tashish osonroq?",
        "asosiy": [
            "Sirg'anib harakatlanish ko'p ishqalanish beradi.",
            "G'ildirak aylanib harakatlanadi — bu ancha kam qarshilik.",
            "Shuning uchun deyarli barcha transport g'ildirakli.",
        ],
        "chuqur": "Aylanish ishqalanishi sirpanish ishqalanishidan bir necha marta kichik bo'ladi.",
        "tajriba": "Bir xil narsani avval sirg'antirib, keyin g'ildirak ustida itarib, kuch farqini his qilish.",
        "uyga": "G'ildiraksiz va g'ildirakli yuk tashishni taqqoslab, farqini yozing.",
    },
    {
        "fokus": "Silliq va notekis sirt",
        "savol": "Muzda va asfaltda yurish nega har xil?",
        "asosiy": [
            "Silliq sirtda ishqalanish kam — sirg'anib ketish oson.",
            "Notekis sirtda ishqalanish ko'p — tutib turadi.",
            "Sirt turi harakatga kuchli ta'sir qiladi.",
        ],
        "chuqur": "Har bir sirt juftligi uchun ishqalanish koeffitsienti degan son mavjud — u qanchalik \"sirpanchiq\" ekanini bildiradi.",
        "tajriba": "Modelni 2-3 xil sirtda yurgizib, qaysi birida yaxshi harakatlanishini aniqlash.",
        "uyga": "Sirpanchiq va tutib turadigan 2 tadan sirtni ro'yxat qiling.",
    },
    {
        "fokus": "Og'irlik ishqalanishga ta'siri",
        "savol": "Og'irroq narsani surish nega qiyinroq?",
        "asosiy": [
            "Jism og'irroq bo'lsa, sirtga kuchliroq bosadi.",
            "Kuchli bosim ko'proq ishqalanish beradi.",
            "Shuning uchun og'ir yukni surish qiyin.",
        ],
        "chuqur": "Ishqalanish kuchi normal (sirtga perpendikulyar) kuchga to'g'ri proporsional.",
        "tajriba": "Modelga qo'shimcha yuk qo'yib, harakatlanish qiyinlashganini sezish.",
        "uyga": "Bo'sh va to'la sumkani surib ko'rib, farqni yozing.",
    },
    {
        "fokus": "Ishqalanish foydali bo'lgan holatlar",
        "savol": "Ishqalanish bo'lmasa nima bo'lardi?",
        "asosiy": [
            "Ishqalanish har doim ham zararli emas.",
            "Usiz yura olmasdik — oyoq sirg'anib ketardi.",
            "Tormoz ham aynan ishqalanish tufayli ishlaydi.",
        ],
        "chuqur": "Muhandis ishqalanishni ba'zi joyda kamaytiradi (podshipnik), ba'zi joyda oshiradi (tormoz, shina).",
        "tajriba": "Modelning g'ildiragini qo'l bilan ushlab to'xtatish — bu tormoz tamoyili ekanini ko'rsatish.",
        "uyga": "Ishqalanish FOYDALI bo'lgan 2 ta holatni yozing.",
    },
    {
        "fokus": "Ishqalanishni kamaytirish yo'llari",
        "savol": "Mexanizm silliqroq ishlashi uchun nima qilish mumkin?",
        "asosiy": [
            "Sirtlarni silliqlash ishqalanishni kamaytiradi.",
            "Moy yoki grafit surtish ham yordam beradi.",
            "G'ildirak va podshipnik eng samarali yechim.",
        ],
        "chuqur": "Podshipnik sirpanish ishqalanishini aylanish ishqalanishiga almashtiradi — shuning uchun juda samarali.",
        "tajriba": "Model o'qini bo'shatib yoki tekislab, harakat silliqlashganini kuzatish.",
        "uyga": "Velosiped zanjiriga nega moy surtilishini tushuntirib yozing.",
    },
    {
        "fokus": "Ishqalanish va tezlik",
        "savol": "Tez yurganda ishqalanish ko'payadimi?",
        "asosiy": [
            "Sirtlar orasidagi ishqalanish tezlikka kam bog'liq.",
            "Lekin havo qarshiligi tezlik bilan keskin ortadi.",
            "Shuning uchun tez mashinalar oqimli shaklda yasaladi.",
        ],
        "chuqur": "Havo qarshiligi tezlik kvadratiga proporsional — tezlik 2 marta oshsa, qarshilik 4 marta ortadi.",
        "tajriba": "Modelni sekin va tez harakatlantirib, qarshilik farqini kuzatish.",
        "uyga": "Poyga mashinalari nega past va oqimli shaklda ekanini yozing.",
    },
    {
        "fokus": "Statik va harakatdagi ishqalanish",
        "savol": "Nega og'ir qutini QO'ZG'ATISH surishdan qiyinroq?",
        "asosiy": [
            "Turgan jismni qo'zg'atish uchun ko'proq kuch kerak.",
            "Harakatga tushgandan keyin surish osonlashadi.",
            "Chunki turgan holatdagi ishqalanish kattaroq.",
        ],
        "chuqur": "Statik ishqalanish kinetik (harakatdagi) ishqalanishdan katta bo'ladi.",
        "tajriba": "Modelni asta itarib, qo'zg'alish momentida kuch keskin kamayishini sezish.",
        "uyga": "Og'ir narsani surganda qo'zg'atish qiyinroqmi yoki davom ettirishmi — sinab yozing.",
    },
]

# ---------------------------------------------------------------------------
# MOTOR (8 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["motorAylanma"] = [
    {
        "fokus": "Motor nima va nima qiladi",
        "savol": "Motorga elektr bersak nima bo'ladi?",
        "asosiy": [
            "Motor — elektr energiyasini harakatga aylantiruvchi qurilma.",
            "Elektr berilganda uning ichidagi qism aylanadi.",
            "Bu aylanish mexanizmga uzatiladi.",
        ],
        "chuqur": "Motor ichida magnit va tok o'zaro ta'sirlashib aylanish hosil qiladi.",
        "tajriba": "Motorni yoqib-o'chirib, aylanish boshlanishi va to'xtashini kuzatish.",
        "uyga": "Uyda motorli 3 ta qurilmani toping va ro'yxat qiling.",
    },
    {
        "fokus": "Motorsiz va motorli model farqi",
        "savol": "Motor modelga nima qo'shadi?",
        "asosiy": [
            "Motorsiz model faqat qo'l bilan harakatlanadi.",
            "Motorli model o'z-o'zidan, uzoq vaqt ishlaydi.",
            "Motor bir maromda va charchamasdan ishlaydi.",
        ],
        "chuqur": "Motor bir xil tezlikni uzoq vaqt ushlab tura oladi — qo'l bunga qodir emas.",
        "tajriba": "Modelni avval qo'lda, keyin motor bilan ishlatib, farqni taqqoslash.",
        "uyga": "Qo'l bilan va motor bilan ishlaydigan bittadan qurilma yozing.",
    },
    {
        "fokus": "Aylanish yo'nalishini o'zgartirish",
        "savol": "Motorni teskari aylantirish mumkinmi?",
        "asosiy": [
            "Motorning aylanish yo'nalishini o'zgartirish mumkin.",
            "Buning uchun ulanish yo'nalishi almashtiriladi.",
            "Shunda model orqaga harakat qiladi.",
        ],
        "chuqur": "Yo'nalishni o'zgartirish uchun motordagi tok yo'nalishi teskari qilinadi.",
        "tajriba": "Motor yo'nalishini o'zgartirib, modelning teskari harakat qilishini kuzatish.",
        "uyga": "Oldinga va orqaga yura oladigan 2 ta qurilma yozing.",
    },
    {
        "fokus": "Motor tezligini boshqarish",
        "savol": "Motorni sekinroq aylantirish mumkinmi?",
        "asosiy": [
            "Motor tezligini controller orqali sozlash mumkin.",
            "Sekin tezlikda model aniqroq harakat qiladi.",
            "Tez tezlikda model tezroq, lekin kamroq aniq ishlaydi.",
        ],
        "chuqur": "Tezlik motorga beriladigan quvvat miqdorini o'zgartirish orqali boshqariladi.",
        "tajriba": "Motor tezligini 2-3 darajaga sozlab, model harakati qanday o'zgarishini kuzatish.",
        "uyga": "Ventilyatorda nechta tezlik darajasi borligini kuzatib yozing.",
    },
    {
        "fokus": "Motor kuchi (moment)",
        "savol": "Motor og'ir yukni ko'tara oladimi?",
        "asosiy": [
            "Motorning aylantirish kuchi \"moment\" deb ataladi.",
            "Yuk og'ir bo'lsa, motor sekinlashadi yoki to'xtaydi.",
            "Tishli uzatma orqali momentni oshirish mumkin.",
        ],
        "chuqur": "Tishli uzatma tezlikni kamaytirib momentni oshiradi — motorning \"kuchini\" ko'paytiradi.",
        "tajriba": "Modelga yuk qo'yib, motor sekinlashganini yoki to'xtaganini kuzatish.",
        "uyga": "Motor og'ir yukni ko'tara olmasa nima qilish kerakligi haqida taxminingizni yozing.",
    },
    {
        "fokus": "Motor va energiya manbai",
        "savol": "Motor energiyani qayerdan oladi?",
        "asosiy": [
            "Motor batareyadan (yoki quvvat manbaidan) energiya oladi.",
            "Batareya bo'shalsa, motor sekinlashadi.",
            "Shuning uchun batareya holatini tekshirib turish kerak.",
        ],
        "chuqur": "Batareya kuchsizlansa motor tezligi tushadi — bu vaqtga asoslangan dasturlarni buzishi mumkin.",
        "tajriba": "Model tezligini kuzatib, batareya holatiga bog'liqligini muhokama qilish.",
        "uyga": "Batareya bilan ishlaydigan 3 ta qurilmani yozing.",
    },
    {
        "fokus": "Motordan mexanizmga kuch uzatish",
        "savol": "Motor aylanishi modelning boshqa qismiga qanday yetadi?",
        "asosiy": [
            "Motor aylanishi tishli, shkiv yoki o'q orqali uzatiladi.",
            "Har bir uzatma turi o'z afzalligiga ega.",
            "To'g'ri uzatma tanlansa, model samarali ishlaydi.",
        ],
        "chuqur": "Uzatmada bir qism energiya ishqalanishga sarflanadi — hech bir uzatma 100% samarali emas.",
        "tajriba": "Modeldagi motordan oxirgi harakatlanuvchi qismgacha bo'lgan yo'lni barmoq bilan kuzatib borish.",
        "uyga": "Motordan g'ildirakkacha bo'lgan yo'lni chizib, har bir qismni nomlang.",
    },
    {
        "fokus": "Motor issiqligi va chegarasi",
        "savol": "Motor uzoq ishlasa nima bo'ladi?",
        "asosiy": [
            "Uzoq ishlagan motor qiziydi.",
            "Haddan ortiq yuk motorni tez qizdiradi.",
            "Shuning uchun motorga dam berish kerak.",
        ],
        "chuqur": "Motor energiyaning bir qismini issiqlikka aylantiradi — bu foydasiz yo'qotish (samaradorlik kamayishi).",
        "tajriba": "Motorni bir necha daqiqa ishlatgandan keyin uning issiqlanishini ehtiyotkorlik bilan sezish.",
        "uyga": "Uzoq ishlagan qurilmalar (kompyuter, telefon) nega qizishini yozing.",
    },
]

# ---------------------------------------------------------------------------
# AERODINAMIKA (8 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["aero"] = [
    {
        "fokus": "Parrak havoni itaradi",
        "savol": "Vertolyot qanday qilib havoga ko'tariladi?",
        "asosiy": [
            "Aylanuvchi parrak havoni bir tomonga itaradi.",
            "Havo itarilganda, parrak qarama-qarshi tomonga itariladi.",
            "Shu tufayli vertolyot yuqoriga ko'tariladi.",
        ],
        "chuqur": "Bu Nyutonning 3-qonuni: har bir ta'sirga teng va qarama-qarshi aks ta'sir mavjud.",
        "tajriba": "Parrakni aylantirib, havo oqimini qo'l bilan sezish va yo'nalishini aniqlash.",
        "uyga": "Parrak ishlatiladigan 3 ta qurilmani yozing.",
    },
    {
        "fokus": "Parrak qanotining burchagi",
        "savol": "Nega parrak qanotlari qiyshiq?",
        "asosiy": [
            "Parrak qanotlari burchak ostida joylashgan.",
            "Aylanganda ular havoni qiyshiq \"kesib\" itaradi.",
            "Burchak katta bo'lsa, ko'proq havo itariladi.",
        ],
        "chuqur": "Hujum burchagi juda katta bo'lsa, havo oqimi uzilib, ko'tarish kuchi keskin kamayadi.",
        "tajriba": "Parrak qanotlarining burchagini kuzatib, ular bir tomonga qiyshayganini aniqlash.",
        "uyga": "Ventilyator parragini kuzatib, qanotlar qiyshiqligini chizib ko'rsating.",
    },
    {
        "fokus": "Tortish kuchi va tezlik",
        "savol": "Parrak tez aylansa nima o'zgaradi?",
        "asosiy": [
            "Parrak tez aylansa, ko'proq havo itariladi.",
            "Demak tortish kuchi ham ortadi.",
            "Sekin aylanishda kuch kam bo'ladi.",
        ],
        "chuqur": "Tortish kuchi aylanish tezligining kvadratiga taxminan proporsional bo'ladi.",
        "tajriba": "Parrak tezligini o'zgartirib, hosil bo'lgan havo oqimi kuchini qo'l bilan taqqoslash.",
        "uyga": "Ventilyator turli tezlikda ishlaganda farqni sezib, yozing.",
    },
    {
        "fokus": "Samolyot qanoti vertolyot parragidan farqi",
        "savol": "Samolyot parraksiz ham ucha oladimi?",
        "asosiy": [
            "Vertolyotda parrak aylanib ko'tarish kuchini hosil qiladi.",
            "Samolyotda esa qanot qo'zg'almas — ko'tarish tezlikdan hosil bo'ladi.",
            "Shuning uchun samolyot uchish uchun tez yugurishi kerak.",
        ],
        "chuqur": "Qanot ustidagi havo pastdagidan tezroq oqadi va bosim farqi ko'tarish kuchini hosil qiladi.",
        "tajriba": "Modelni tez harakatlantirib, qanot/parrak ta'sirini kuzatish.",
        "uyga": "Samolyot va vertolyot farqini 2-3 gapda yozing.",
    },
    {
        "fokus": "Havo qarshiligi",
        "savol": "Nega tez yurgan mashinada shamol kuchli seziladi?",
        "asosiy": [
            "Havo harakatlanayotgan jismga qarshilik ko'rsatadi.",
            "Tez harakatda qarshilik keskin ortadi.",
            "Qarshilik jismni sekinlashtiradi.",
        ],
        "chuqur": "Havo qarshiligi tezlik kvadratiga proporsional — shuning uchun tez transportda u asosiy to'siq bo'ladi.",
        "tajriba": "Modelni tez va sekin harakatlantirib, havo qarshiligi ta'sirini kuzatish.",
        "uyga": "Qo'lingizni harakatlanayotgan mashina oynasidan (xavfsiz holatda) yoki ventilyator oldida tutib, qarshilikni sezib yozing.",
    },
    {
        "fokus": "Oqimli shakl (aerodinamik shakl)",
        "savol": "Nega samolyot va tez poyezdlar uchli shaklda?",
        "asosiy": [
            "Oqimli shakl havoni yumshoq yorib o'tadi.",
            "Bunday shaklda qarshilik kam bo'ladi.",
            "Shuning uchun tez transport uchli va silliq yasaladi.",
        ],
        "chuqur": "Oqimli shakl havo oqimini uzilishsiz o'tkazadi va orqada hosil bo'ladigan \"tortuvchi\" bo'shliqni kamaytiradi.",
        "tajriba": "Modelning old qismi shaklini kuzatib, u oqimli yoki tekismi aniqlash.",
        "uyga": "Oqimli shakldagi 2 ta transport vositasini toping va chizing.",
    },
    {
        "fokus": "Parvozdagi kuchlar muvozanati",
        "savol": "Uchayotgan samolyotga nechta kuch ta'sir qiladi?",
        "asosiy": [
            "Ko'tarish kuchi — yuqoriga.",
            "Og'irlik — pastga; tortish kuchi — oldinga; qarshilik — orqaga.",
            "Bu kuchlar muvozanatda bo'lsa, samolyot tekis uchadi.",
        ],
        "chuqur": "Ko'tarish og'irlikdan katta bo'lsa samolyot ko'tariladi, kichik bo'lsa pastga tushadi.",
        "tajriba": "Modelga ta'sir qiluvchi kuchlarni aniqlab, ularni strelkalar bilan ko'rsatib berish.",
        "uyga": "Samolyotni chizib, unga ta'sir qiluvchi 4 ta kuchni strelka bilan belgilang.",
    },
    {
        "fokus": "Reaktiv harakat tamoyili",
        "savol": "Raketa kosmosda havosiz joyda qanday uchadi?",
        "asosiy": [
            "Raketa orqaga gaz otib, oldinga itariladi.",
            "Buning uchun havo kerak emas.",
            "Shuning uchun raketa kosmosda ham ucha oladi.",
        ],
        "chuqur": "Reaktiv harakat impulsning saqlanishi qonuniga asoslanadi — otilgan massa va raketa impulslari teng bo'ladi.",
        "tajriba": "Modelning itaruvchi qismini kuzatib, u qaysi tomonga havo/kuch berayotganini aniqlash.",
        "uyga": "Shishirilgan sharni qo'yib yuborsangiz nega uchishini reaktiv harakat bilan tushuntiring.",
    },
]

# ---------------------------------------------------------------------------
# SUZISH (2 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["suv"] = [
    {
        "fokus": "Nega og'ir kema cho'kmaydi",
        "savol": "Metall tosh cho'kadi, metall kema esa suzadi — nega?",
        "asosiy": [
            "Suv jismni yuqoriga itaradi — bu suzuvchanlik kuchi.",
            "Kema keng va ichi bo'sh bo'lgani uchun ko'p suv siqib chiqaradi.",
            "Shuning uchun u og'ir bo'lsa ham suzadi.",
        ],
        "chuqur": "Arximed qonuni: jism siqib chiqargan suv og'irligiga teng kuch bilan yuqoriga itariladi.",
        "tajriba": "Modelning suvda qanday turishini kuzatish yoki shaklini o'zgartirib sinash (imkon bo'lsa).",
        "uyga": "Suvda suzadigan va cho'kadigan 2 tadan narsani sinab, ro'yxat qiling.",
    },
    {
        "fokus": "Shakl suzishga qanday ta'sir qiladi",
        "savol": "Bir xil massadagi narsa shakliga qarab suzadimi yoki cho'kadimi?",
        "asosiy": [
            "Keng va yassi shakl ko'proq suv siqib chiqaradi.",
            "Shuning uchun u yaxshiroq suzadi.",
            "Ixcham va og'ir shakl esa cho'kadi.",
        ],
        "chuqur": "Muhim narsa massa emas, o'rtacha zichlik — shakl orqali o'rtacha zichlikni suvnikidan kichik qilish mumkin.",
        "tajriba": "Modelga qo'shimcha yuk qo'yib, u qachon cho'ka boshlashini kuzatish.",
        "uyga": "Folgadan qayiq va shar yasab, qaysi biri suzishini sinang va yozing.",
    },
]

# ---------------------------------------------------------------------------
# TRANSPORT (11 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["transport"] = [
    {
        "fokus": "G'ildirak va o'q",
        "savol": "G'ildirak nimaning atrofida aylanadi?",
        "asosiy": [
            "O'q — g'ildirak aylanadigan markaziy tayoqcha.",
            "G'ildirak o'q atrofida erkin aylanishi kerak.",
            "Agar u qisilib qolsa, harakat qiyinlashadi.",
        ],
        "chuqur": "O'q va g'ildirak orasidagi ishqalanishni kamaytirish uchun podshipnik ishlatiladi.",
        "tajriba": "G'ildirakni qo'l bilan aylantirib, u erkin aylanadimi yoki qisiladimi tekshirish.",
        "uyga": "G'ildirak va o'qni chizib, ikkalasini nomlang.",
    },
    {
        "fokus": "Shassi — transportning asosi",
        "savol": "Mashinaning \"skeleti\" qayerda?",
        "asosiy": [
            "Shassi — barcha qismlar biriktiriladigan asosiy ramka.",
            "U mustahkam bo'lishi kerak.",
            "Shassi egilsa, g'ildiraklar noto'g'ri turadi.",
        ],
        "chuqur": "Shassi butun konstruksiya yukini ko'taradi va uni g'ildiraklarga taqsimlaydi.",
        "tajriba": "Modelning shassisini asta egishga harakat qilib, mustahkamligini tekshirish.",
        "uyga": "Mashina shassisini chizib, unga nimalar biriktirilishini ko'rsating.",
    },
    {
        "fokus": "G'ildiraklar soni va joylashuvi",
        "savol": "Nega yuk mashinasida ko'p g'ildirak bor?",
        "asosiy": [
            "Ko'p g'ildirak og'irlikni ko'proq nuqtaga taqsimlaydi.",
            "Shu tufayli har bir g'ildirakka kamroq bosim tushadi.",
            "Bu yo'lni ham, g'ildirakni ham asraydi.",
        ],
        "chuqur": "Yer bosimi = og'irlik / tegib turgan yuza; ko'p g'ildirak bosimni kamaytiradi.",
        "tajriba": "Modeldagi g'ildiraklarni sanab, ular og'irlikni qanday taqsimlashini muhokama qilish.",
        "uyga": "Yengil va yuk mashinasidagi g'ildiraklar sonini taqqoslab yozing.",
    },
    {
        "fokus": "Og'irlik taqsimoti",
        "savol": "Yukni mashinaning qayeriga qo'ygan ma'qul?",
        "asosiy": [
            "Yuk bir tomonga to'plansa, mashina qiyshayadi.",
            "Teng taqsimlangan yuk barqarorroq.",
            "Og'ir yuk pastroqqa qo'yilsa yaxshiroq.",
        ],
        "chuqur": "Og'irlik taqsimoti boshqaruvchanlikka ham ta'sir qiladi — orqasi og'ir mashina burilishda beqaror bo'ladi.",
        "tajriba": "Yukni modelning turli joylariga qo'yib, harakat barqarorligini taqqoslash.",
        "uyga": "Yukni sumkaning qayeriga solsangiz ko'tarish oson bo'lishini sinab yozing.",
    },
    {
        "fokus": "Burilish qanday sodir bo'ladi",
        "savol": "Mashina qanday qilib buriladi?",
        "asosiy": [
            "Burilishda old g'ildiraklar burchak ostida turadi.",
            "Yoki bir tomondagi g'ildirak sekinroq aylanadi.",
            "Shunda mashina yoy chizib buriladi.",
        ],
        "chuqur": "Burilishda tashqi g'ildirak ichkisidan uzunroq yo'l bosadi — shuning uchun differensial kerak bo'ladi.",
        "tajriba": "Modelni burilishga majbur qilib, g'ildiraklar qanday harakat qilishini kuzatish.",
        "uyga": "Mashina burilayotganda ichki va tashqi g'ildirak yo'lini chizib solishtiring.",
    },
    {
        "fokus": "Motordan g'ildirakkacha kuch uzatish",
        "savol": "Motor kuchi g'ildirakka qanday yetadi?",
        "asosiy": [
            "Kuch tishli, tasma yoki o'q orqali uzatiladi.",
            "Bu yo'l \"yurish tizimi\" deb ataladi.",
            "Har bir bo'g'in ishonchli bo'lishi kerak.",
        ],
        "chuqur": "Uzatma nisbatini o'zgartirib, transportni tezroq yoki kuchliroq qilish mumkin.",
        "tajriba": "Motordan g'ildirakkacha bo'lgan barcha qismlarni ketma-ket aniqlab chiqish.",
        "uyga": "Motordan g'ildirakkacha bo'lgan zanjirni chizib, qismlarni nomlang.",
    },
    {
        "fokus": "Tezlik va kuch murosasi",
        "savol": "Tez mashina og'ir yuk tashiy oladimi?",
        "asosiy": [
            "Tezlikka moslangan transport kam yuk tashiydi.",
            "Kuchga moslangan transport sekin, lekin ko'p yuk tashiydi.",
            "Ikkalasini bir vaqtda olish qiyin.",
        ],
        "chuqur": "Uzatma nisbati bu murosani belgilaydi — poyga mashinasi va traktor buning ikki cheti.",
        "tajriba": "Modelni bo'sh va yuk bilan yurgizib, tezlik farqini kuzatish.",
        "uyga": "Tezlikka va kuchga moslangan bittadan transport yozing.",
    },
    {
        "fokus": "Zarbani yumshatish (osma tizim)",
        "savol": "Nega notekis yo'lda mashina ichida unchalik silkinmaymiz?",
        "asosiy": [
            "Osma tizim g'ildirak bilan kuzov orasida joylashadi.",
            "U yo'ldagi zarbalarni yutadi.",
            "Shu tufayli yurish qulay bo'ladi.",
        ],
        "chuqur": "Osma tizim yo'l bilan aloqani ham yaxshilaydi — g'ildirak yerdan uzilib qolmaydi.",
        "tajriba": "Modelni notekis sirtda yurgizib, silkinishni kuzatish.",
        "uyga": "Velosiped va mashina zarbani qanday yumshatishini taqqoslab yozing.",
    },
    {
        "fokus": "Tormozlash",
        "savol": "Mashina qanday to'xtaydi?",
        "asosiy": [
            "Tormoz g'ildirak aylanishiga qarshilik beradi.",
            "Bu qarshilik ishqalanish orqali hosil bo'ladi.",
            "Tez yurgan transport uzoqroq masofada to'xtaydi.",
        ],
        "chuqur": "Tormozlash masofasi tezlik kvadratiga proporsional — tezlik 2 marta oshsa, masofa 4 marta ortadi.",
        "tajriba": "Modelni turli tezlikda yurgizib, qo'l bilan to'xtatish qanchalik qiyinligini taqqoslash.",
        "uyga": "Nega tez yurgan mashina uzoqroq masofada to'xtashini tushuntirib yozing.",
    },
    {
        "fokus": "Yuk tashish uchun maxsus qismlar",
        "savol": "Trailer nima uchun kerak?",
        "asosiy": [
            "Trailer — ortga ulanadigan qo'shimcha yuk qismi.",
            "U asosiy mashinani og'irlashtirmasdan yuk sig'imini oshiradi.",
            "Kerak bo'lmasa uni ajratib qo'yish mumkin.",
        ],
        "chuqur": "Trailer ulanish nuqtasi (dishlo) burilishda erkin bo'lishi kerak, aks holda tizim buriladi olmaydi.",
        "tajriba": "Modelga trailer ulab (yoki tasavvur qilib), burilish qanday o'zgarishini muhokama qilish.",
        "uyga": "Trailerli transportni ko'rsangiz kuzatib, u qanday ulanganini chizing.",
    },
    {
        "fokus": "Transport turi vazifaga bog'liq",
        "savol": "Nima uchun barcha transport bir xil emas?",
        "asosiy": [
            "Har bir transport o'z vazifasiga moslab yasaladi.",
            "Yuk mashinasi — ko'p yuk uchun; poyga mashinasi — tezlik uchun.",
            "Dizayn har doim vazifadan kelib chiqadi.",
        ],
        "chuqur": "Muhandislikda \"shakl vazifadan kelib chiqadi\" tamoyili — bu barcha loyihalash ishining asosi.",
        "tajriba": "Model qanday vazifaga mo'ljallanganini aniqlab, dizayni shunga mos yoki yo'qligini muhokama qilish.",
        "uyga": "3 xil transportni vazifasi bilan birga jadval qilib yozing.",
    },
]

# ---------------------------------------------------------------------------
# DARVOZA / AVTOMATIK MEXANIZM (2 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["darvoza"] = [
    {
        "fokus": "Avtomatik darvoza qanday ochiladi",
        "savol": "Do'kon eshigi qanday qilib o'zi ochiladi?",
        "asosiy": [
            "Avtomatik darvoza motor yordamida harakatlanadi.",
            "Motor richag yoki vint orqali darvozani suradi.",
            "Odam kuchi kerak emas.",
        ],
        "chuqur": "Darvoza mexanizmi ochiq va yopiq holatlarni aniqlash uchun chegara sezgichlaridan foydalanadi.",
        "tajriba": "Darvoza modelini ochib-yopib, mexanizmning qaysi qismi harakatlanishini kuzatish.",
        "uyga": "Avtomatik ochiladigan 2 ta eshik/darvozani eslang va yozing.",
    },
    {
        "fokus": "Darvoza xavfsizligi va chegaralar",
        "savol": "Darvoza yopilayotganda kimdir o'tsa nima bo'ladi?",
        "asosiy": [
            "Xavfsiz darvozada to'siqni sezuvchi tizim bo'ladi.",
            "To'siq sezilsa, darvoza to'xtaydi yoki ochiladi.",
            "Bu jarohatning oldini oladi.",
        ],
        "chuqur": "Avtomatik tizimlarda xavfsizlik birinchi o'rinda turadi — mexanizm shubha bo'lsa doim xavfsiz holatga o'tishi kerak.",
        "tajriba": "Darvoza yopilayotganda yo'liga to'siq qo'yib, mexanizm nima qilishini kuzatish.",
        "uyga": "Lift eshigi yopilayotganda qo'l qo'yilsa nima bo'lishini kuzatib yozing.",
    },
]

# ---------------------------------------------------------------------------
# BIOMIMIKRIYA (14 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["biomimikriya"] = [
    {
        "fokus": "Biomimikriya nima",
        "savol": "Muhandislar g'oyalarni qayerdan oladi?",
        "asosiy": [
            "Biomimikriya — tabiatdan ilhomlanib qurilma yaratish.",
            "Qush qanotidan samolyot g'oyasi olingan.",
            "Tabiat millionlab yil davomida eng yaxshi yechimlarni topgan.",
        ],
        "chuqur": "Biomimikriya faqat shaklni emas, ishlash tamoyilini ham nusxalaydi.",
        "tajriba": "Model qaysi hayvonga o'xshashini va uning qaysi harakatini taqlid qilishini aniqlash.",
        "uyga": "Tabiatdan ilhomlangan 2 ta ixtironi toping (masalan, samolyot, velcro).",
    },
    {
        "fokus": "Hayvon oyog'i qanday harakat qiladi",
        "savol": "Hayvon yurganda oyog'i qanday harakatlanadi?",
        "asosiy": [
            "Oyoq oldinga chiqib, yerga tegib, orqaga itaradi.",
            "Keyin yerdan ko'tarilib yana oldinga chiqadi.",
            "Bu takrorlanuvchi sikl.",
        ],
        "chuqur": "Oyoq harakati ikki bosqichga bo'linadi: tayanch bosqichi (yerda) va o'tish bosqichi (havoda).",
        "tajriba": "Model oyog'ini sekin harakatlantirib, sikl bosqichlarini kuzatish.",
        "uyga": "Uy hayvoni yoki qushning yurishini kuzatib, oyoq harakatini tasvirlab yozing.",
    },
    {
        "fokus": "Ko'p oyoqli harakat tartibi",
        "savol": "To'rt oyoqli hayvon oyoqlarini qanday tartibda qo'yadi?",
        "asosiy": [
            "Hamma oyoq bir vaqtda harakatlanmaydi.",
            "Ular navbat bilan qo'yiladi.",
            "Shu tufayli hayvon muvozanatini yo'qotmaydi.",
        ],
        "chuqur": "Har qanday paytda kamida ikki-uch oyoq yerda bo'lishi barqarorlikni ta'minlaydi.",
        "tajriba": "Modelning oyoqlari navbat bilan harakatlanishini kuzatib, tartibni aniqlash.",
        "uyga": "Mushuk yoki it yurishini kuzatib, oyoqlar tartibini yozing.",
    },
    {
        "fokus": "Dum va muvozanat",
        "savol": "Hayvonga dum nima uchun kerak?",
        "asosiy": [
            "Dum muvozanat saqlashga yordam beradi.",
            "Ba'zi hayvonlar dumi bilan yo'nalishni ham boshqaradi.",
            "Dinozavrlarda dum og'ir tanani muvozanatlagan.",
        ],
        "chuqur": "Dum og'irlik markazini siljitib, tananing oldinga egilishini kompensatsiya qiladi.",
        "tajriba": "Modelning dumi bor bo'lsa, uni ushlab turib va qo'yib yuborib, barqarorlik farqini kuzatish.",
        "uyga": "Dumi uzun 2 ta hayvonni toping va dum ularga nima uchun kerakligini yozing.",
    },
    {
        "fokus": "Suzuvchi hayvonlar harakati",
        "savol": "Baliq suvda qanday oldinga siljiydi?",
        "asosiy": [
            "Baliq tanasi va dumi bilan suvni orqaga itaradi.",
            "Shunda u oldinga siljiydi.",
            "Suzgichlar yo'nalishni boshqaradi.",
        ],
        "chuqur": "Suvda harakat ham reaktiv tamoyilga asoslanadi — suv orqaga, jism oldinga.",
        "tajriba": "Modelning dum/suzgich harakatini kuzatib, u qaysi tomonga itarayotganini aniqlash.",
        "uyga": "Baliq suzishini kuzatib (yoki videodan), dum harakatini chizing.",
    },
    {
        "fokus": "Uchuvchi hayvonlar",
        "savol": "Qush qanoti bilan nima qiladi?",
        "asosiy": [
            "Qush qanotini pastga urib, havoni itaradi.",
            "Shunda tanasi yuqoriga ko'tariladi.",
            "Qanot shakli ham ko'tarishga yordam beradi.",
        ],
        "chuqur": "Qush qanoti bir vaqtning o'zida ham ko'tarish, ham oldinga siljish kuchini hosil qiladi.",
        "tajriba": "Model qanoti harakatini kuzatib, u havoni qaysi tomonga itarayotganini aniqlash.",
        "uyga": "Qush uchishini kuzatib, qanot harakatini tasvirlab yozing.",
    },
    {
        "fokus": "Sudralib yuruvchilar harakati",
        "savol": "Ilon oyoqsiz qanday harakatlanadi?",
        "asosiy": [
            "Ilon tanasini to'lqinsimon egib harakatlanadi.",
            "Tana yer bilan ishqalanib, oldinga suriladi.",
            "Timsoh esa kalta oyoqlari bilan sudraladi.",
        ],
        "chuqur": "To'lqinsimon harakatda tananing har bir qismi navbat bilan yerdan itariladi.",
        "tajriba": "Modelning tana harakatini kuzatib, u to'lqinsimon yoki oyoqli ekanini aniqlash.",
        "uyga": "Oyoqsiz harakatlanadigan 2 ta jonzotni yozing.",
    },
    {
        "fokus": "Hayvon skeleti va konstruksiya",
        "savol": "Hayvonni nima tik ushlab turadi?",
        "asosiy": [
            "Skelet — hayvonning ichki tayanch tuzilmasi.",
            "U tanani ushlab turadi va shakl beradi.",
            "Robotda ham xuddi shunday ramka bo'ladi.",
        ],
        "chuqur": "Ba'zi jonzotlarda skelet tashqarida bo'ladi (qisqichbaqa, hasharotlar) — bu ekzoskelet deb ataladi.",
        "tajriba": "Modelning \"skeleti\" — asosiy ko'taruvchi qismini aniqlash.",
        "uyga": "Skeleti ichkarida va tashqarida bo'lgan bittadan jonzot yozing.",
    },
    {
        "fokus": "Hayvonlarning himoya usullari",
        "savol": "Toshbaqa xavfdan qanday himoyalanadi?",
        "asosiy": [
            "Ba'zi hayvonlar qattiq qobiq bilan himoyalanadi.",
            "Boshqalari tez qochadi yoki yashirinadi.",
            "Himoya usuli hayvon tuzilishiga ta'sir qiladi.",
        ],
        "chuqur": "Qobiq mustahkam, lekin og'ir — bu tezlik bilan himoya orasidagi murosaga misol.",
        "tajriba": "Model himoya qismiga (qobiq, tikan) ega bo'lsa, uni aniqlab muhokama qilish.",
        "uyga": "Turli usulda himoyalanadigan 2 ta hayvonni yozing.",
    },
    {
        "fokus": "Ov qilish va harakat tezligi",
        "savol": "Yirtqich hayvon nega tez yuguradi?",
        "asosiy": [
            "Ovchi hayvonlar ovni tutish uchun tez bo'lishi kerak.",
            "Ularning oyoqlari uzun va yengil bo'ladi.",
            "Ov ham qochish uchun tez bo'lishga intiladi.",
        ],
        "chuqur": "Uzun oyoq bir qadamda ko'proq masofa bosadi — bu 3-toifa richag tamoyiliga o'xshaydi.",
        "tajriba": "Model harakat tezligini kuzatib, uning oyoq/mexanizm uzunligi bilan bog'liqligini muhokama qilish.",
        "uyga": "Eng tez yuguradigan 2 ta hayvonni toping va tezligini yozing.",
    },
    {
        "fokus": "Katta hayvonlar qanday harakat qiladi",
        "savol": "Fil yoki dinozavr og'ir tanasini qanday ko'taradi?",
        "asosiy": [
            "Katta hayvonlarning oyog'i yo'g'on va ustunga o'xshash.",
            "Ular sekin, lekin ishonchli harakat qiladi.",
            "Og'irlik to'g'ridan-to'g'ri pastga tushadi.",
        ],
        "chuqur": "Jism kattalashganda og'irlik hajmga (kub) proporsional, suyak kuchi esa kesim yuzasiga (kvadrat) — shuning uchun katta hayvonlar yo'g'on oyoqli bo'ladi.",
        "tajriba": "Modelning oyoqlari tanaga nisbatan qanchalik yo'g'on ekanini kuzatish.",
        "uyga": "Katta va kichik hayvon oyoqlarini taqqoslab, farqini yozing.",
    },
    {
        "fokus": "Hayvon harakatini mexanizm bilan takrorlash",
        "savol": "Robot hayvon harakatini qanday nusxalaydi?",
        "asosiy": [
            "Mexanizm hayvon harakatiga o'xshash yo'l chizadi.",
            "Odatda krivoship-shatun mexanizmi ishlatiladi.",
            "Aniq nusxa emas, lekin o'xshash natija beradi.",
        ],
        "chuqur": "Robot mexanizmi soddalashtirilgan model — u tabiiy harakatning eng muhim qismini takrorlaydi.",
        "tajriba": "Model harakatini haqiqiy hayvon harakati bilan solishtirib, o'xshash va farqli tomonlarni aytish.",
        "uyga": "Model harakati haqiqiy hayvondan nimasi bilan farq qilishini yozing.",
    },
    {
        "fokus": "Muhitga moslashish",
        "savol": "Nega cho'l va qutb hayvonlari bir-biriga o'xshamaydi?",
        "asosiy": [
            "Har bir hayvon o'z muhitiga moslashgan.",
            "Sovuq joyda qalin junli, issiqda esa yengil bo'ladi.",
            "Muhandis ham qurilmani ishlash sharoitiga moslaydi.",
        ],
        "chuqur": "Moslashuv millionlab yillik tanlanish natijasi — muhandislik esa shu jarayonni tezlashtirilgan holda takrorlaydi.",
        "tajriba": "Model qanday muhitda ishlashga mo'ljallanganini muhokama qilish.",
        "uyga": "Sovuq va issiq joyda yashaydigan bittadan hayvonni taqqoslab yozing.",
    },
    {
        "fokus": "Tabiatdan olingan zamonaviy ixtirolar",
        "savol": "Bugungi texnikada tabiatdan olingan nimalar bor?",
        "asosiy": [
            "Velcro (yopishqoch lenta) — o'simlik urug'idan olingan.",
            "Tez poyezd burni — qushning tumshug'idan.",
            "Robot-itlar — haqiqiy hayvon harakatidan.",
        ],
        "chuqur": "Biomimikriya bugun materiallar, arxitektura va tibbiyotda ham keng qo'llaniladi.",
        "tajriba": "Model qaysi zamonaviy texnikaga o'xshashini muhokama qilish.",
        "uyga": "Tabiatdan ilhomlangan zamonaviy ixtironi internetdan 1 ta toping va yozing.",
    },
    {
        "fokus": "Hayvonlarning sezgi organlari",
        "savol": "Hayvonlar atrofni qanday sezadi?",
        "asosiy": [
            "Hayvonlarda ko'z, quloq, hid sezgisi bor.",
            "Ba'zilari inson sezmaydigan narsalarni ham sezadi.",
            "Robotdagi sensorlar ham xuddi shu vazifani bajaradi.",
        ],
        "chuqur": "Ko'rshapalak tovush aks-sadosi bilan \"ko'radi\" — bu ultratovush sensori bilan bir xil tamoyil.",
        "tajriba": "Modelda sensor bo'lsa, u qaysi hayvon sezgisiga o'xshashini aniqlash.",
        "uyga": "Insonda yo'q sezgiga ega 2 ta hayvonni toping va yozing.",
    },
    {
        "fokus": "Guruh bo'lib harakatlanish",
        "savol": "Nega baliqlar va qushlar to'da bo'lib yuradi?",
        "asosiy": [
            "To'da bo'lib yurish xavfsizroq.",
            "Har bir jonzot qo'shnisiga qarab harakat qiladi.",
            "Natijada butun to'da bir tan bo'lib harakatlanadi.",
        ],
        "chuqur": "Bu tamoyil robotlar guruhida (swarm robotics) ham qo'llaniladi — sodda qoidalar murakkab xatti-harakat beradi.",
        "tajriba": "Bir nechta modelni birga qo'yib, ular guruh bo'lib qanday harakatlanishi mumkinligini muhokama qilish.",
        "uyga": "To'da bo'lib yuradigan 2 ta jonzotni yozing va nima uchun shunday qilishini tushuntiring.",
    },
    {
        "fokus": "Rang va naqsh nima uchun kerak",
        "savol": "Nega ba'zi hayvonlar rang-barang, ba'zilari esa bir xil rangda?",
        "asosiy": [
            "Ba'zi hayvonlar atrof-muhitga qo'shilib ketish uchun rang oladi.",
            "Boshqalari yorqin rang bilan ogohlantiradi.",
            "Rang — himoya yoki muloqot vositasi.",
        ],
        "chuqur": "Kamuflyaj tamoyili harbiy texnika va kiyimlarda ham qo'llaniladi.",
        "tajriba": "Model rangi uning \"vazifasi\"ga mos kelishi mumkinmi — muhokama qilish.",
        "uyga": "Atrof-muhitga qo'shilib ketadigan 2 ta hayvonni toping va yozing.",
    },
    {
        "fokus": "Kuch va o'lcham nisbati",
        "savol": "Chumoli nega o'zidan og'ir yukni ko'tara oladi?",
        "asosiy": [
            "Kichik jonzotlar o'z og'irligiga nisbatan juda kuchli.",
            "Chumoli o'zidan bir necha marta og'ir yukni ko'taradi.",
            "Katta hayvonlarda bunday nisbat bo'lmaydi.",
        ],
        "chuqur": "Jism kichrayganda hajm (og'irlik) kuchdan tezroq kamayadi — shuning uchun kichik jonzotlar nisbatan kuchli bo'ladi.",
        "tajriba": "Modelning o'z og'irligiga nisbatan qancha yuk ko'tara olishini sinash.",
        "uyga": "Chumoli o'zidan necha marta og'ir yuk ko'tarishini topib yozing.",
    },
]

# ---------------------------------------------------------------------------
# SENSOR (13 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["sensor"] = [
    {
        "fokus": "Sensor nima va nima qiladi",
        "savol": "Robot atrofini qanday \"sezadi\"?",
        "asosiy": [
            "Sensor — atrof-muhitdagi o'zgarishni sezuvchi qurilma.",
            "U sezgan narsasini signalga aylantiradi.",
            "Robot shu signal orqali \"biladi\".",
        ],
        "chuqur": "Sensor fizik kattalikni (yorug'lik, masofa) elektr signaliga aylantiradi.",
        "tajriba": "Sensorga qo'l yaqinlashtirib, robot reaksiyasini kuzatish.",
        "uyga": "Sensor ishlatiladigan 3 ta qurilmani toping va yozing.",
    },
    {
        "fokus": "Sensor va inson sezgi organlari",
        "savol": "Sensor bizning qaysi a'zomizga o'xshaydi?",
        "asosiy": [
            "Ko'z — yorug'lik sensoriga o'xshaydi.",
            "Teri — bosim sensoriga o'xshaydi.",
            "Quloq — tovush sensoriga o'xshaydi.",
        ],
        "chuqur": "Inson sezgi organlari ham signalni miyaga uzatadi — robot sensori esa controllerga.",
        "tajriba": "Sensorni sinab, u qaysi sezgi organiga o'xshashini aniqlash.",
        "uyga": "Har bir sezgi organiga mos sensor turini jadval qilib yozing.",
    },
    {
        "fokus": "Masofa sensori",
        "savol": "Robot to'siq qanchalik uzoqligini qanday biladi?",
        "asosiy": [
            "Masofa sensori signal yuborib, uning qaytishini kutadi.",
            "Qaytish vaqtidan masofa hisoblanadi.",
            "Yaqin to'siq — tez qaytadi, uzoq to'siq — sekin.",
        ],
        "chuqur": "Ultratovush sensori tovush tezligidan (taxminan 340 m/s) foydalanib masofani hisoblaydi.",
        "tajriba": "To'siqni turli masofaga qo'yib, sensor reaksiyasi qanday o'zgarishini kuzatish.",
        "uyga": "Mashinadagi parktronik qanday ishlashini tushuntirib yozing.",
    },
    {
        "fokus": "Yorug'lik va rang sensori",
        "savol": "Robot rangni qanday ajratadi?",
        "asosiy": [
            "Rang sensori sirtdan qaytgan yorug'likni o'lchaydi.",
            "Oq sirt ko'p, qora sirt kam yorug'lik qaytaradi.",
            "Shu farqdan rang aniqlanadi.",
        ],
        "chuqur": "Sensor turli to'lqin uzunligidagi yorug'likni alohida o'lchab, rangni aniqlaydi.",
        "tajriba": "Sensorni oq va qora sirt ustida sinab, ko'rsatkich farqini kuzatish.",
        "uyga": "Oq va qora kiyim quyoshda nega har xil qizishini yozing.",
    },
    {
        "fokus": "Bosim va teginish sensori",
        "savol": "Robot biror narsaga tekkanini qanday biladi?",
        "asosiy": [
            "Bosim sensori unga qo'yilgan kuchni o'lchaydi.",
            "Teginish sensori bosilganda signal beradi.",
            "Bu eng oddiy sensor turlaridan biri.",
        ],
        "chuqur": "Bosim sensori kuch miqdorini ham o'lchay oladi — faqat \"bor/yo'q\" emas.",
        "tajriba": "Sensorga turli kuch bilan bosib, reaksiya o'zgarishini kuzatish.",
        "uyga": "Bosish orqali ishlaydigan 3 ta qurilmani yozing.",
    },
    {
        "fokus": "Sensordan reaksiyagacha",
        "savol": "Sensor sezgandan keyin nima bo'ladi?",
        "asosiy": [
            "Sensor signalni controllerga yuboradi.",
            "Controller signalga qarab qaror qabul qiladi.",
            "Keyin motorga buyruq beriladi.",
        ],
        "chuqur": "Bu zanjir: sezish -> qaror -> harakat; barcha avtomatik tizimlar shu tamoyilda ishlaydi.",
        "tajriba": "Sensorni ishga tushirib, signal-qaror-harakat zanjirini kuzatib borish.",
        "uyga": "Sezish-qaror-harakat zanjirini chizib, har bir bosqichni nomlang.",
    },
    {
        "fokus": "Chegara qiymati (sensor qachon ishlaydi)",
        "savol": "Sensor qanchalik yaqinlashganda ishlashi kerak?",
        "asosiy": [
            "Chegara qiymat — sensor reaksiya beradigan nuqta.",
            "Chegara kichik bo'lsa, sensor kech ishlaydi.",
            "Katta bo'lsa, juda erta ishlaydi.",
        ],
        "chuqur": "Chegarani to'g'ri tanlash muhim — noto'g'ri chegara robotni ishonchsiz qiladi.",
        "tajriba": "Chegara qiymatini o'zgartirib, robot qachon reaksiya berishini sozlash.",
        "uyga": "Avtomatik chiroq qachon yonishi kerakligi haqida fikringizni yozing.",
    },
    {
        "fokus": "Sensor xatolari",
        "savol": "Sensor har doim to'g'ri ishlaydimi?",
        "asosiy": [
            "Sensor ba'zan noto'g'ri qiymat berishi mumkin.",
            "Chang, yorug'lik yoki notekis sirt xalaqit beradi.",
            "Shuning uchun tekshirib turish kerak.",
        ],
        "chuqur": "Ishonchli tizimda bir necha o'lchov o'rtachasi olinadi yoki bir necha sensor solishtiriladi.",
        "tajriba": "Sensorni noqulay sharoitda (yon burchakda, uzoqdan) sinab, xato paydo bo'lishini kuzatish.",
        "uyga": "Sensor xato qilishi mumkin bo'lgan holatni 1 ta yozing.",
    },
    {
        "fokus": "Sensorni sozlash (kalibrlash)",
        "savol": "Sensorni aniqroq ishlashga qanday majbur qilamiz?",
        "asosiy": [
            "Kalibrlash — sensorni aniq ishlashi uchun sozlash.",
            "Avval ma'lum holatda o'lchov olinadi.",
            "Keyin shunga qarab chegara belgilanadi.",
        ],
        "chuqur": "Yorug'lik sharoiti o'zgarsa, rang sensorini qayta kalibrlash kerak bo'ladi.",
        "tajriba": "Sensorni oq va qora sirtda o'lchab, o'rtacha chegarani hisoblab qo'yish.",
        "uyga": "Nega bir xil sensor turli xonada turlicha ishlashi mumkinligini yozing.",
    },
    {
        "fokus": "Ikki sensor birga",
        "savol": "Ikkita sensor bittadan yaxshiroqmi?",
        "asosiy": [
            "Ikki sensor ko'proq ma'lumot beradi.",
            "Robot aniqroq qaror qabul qila oladi.",
            "Masalan, ham masofani, ham rangni bilishi mumkin.",
        ],
        "chuqur": "Bir nechta sensordan olingan ma'lumotni birlashtirish \"sensor fusion\" deb ataladi.",
        "tajriba": "Ikki sensorli modelda ikkalasini ham sinab, birgalikda qanday ishlashini kuzatish.",
        "uyga": "Ikki sensordan foydalanadigan qurilma g'oyasini yozing.",
    },
    {
        "fokus": "Chiziq kuzatish tamoyili",
        "savol": "Robot chiziqdan chiqib ketmasdan qanday yuradi?",
        "asosiy": [
            "Sensor chiziq ustidami yoki chetdami — shuni tekshiradi.",
            "Chetga chiqsa, robot qarama-qarshi tomonga buriladi.",
            "Shu tarzda u doim chiziqqa qaytadi.",
        ],
        "chuqur": "Bu doimiy tuzatish jarayoni — robot aslida chiziq atrofida biroz chayqalib yuradi.",
        "tajriba": "Robotni chiziq ustida yurgizib, u qanday tuzatish qilayotganini kuzatish.",
        "uyga": "Robot chiziqdan chetga chiqsa nima qilishi kerakligini chizib ko'rsating.",
    },
    {
        "fokus": "To'siqdan qochish tamoyili",
        "savol": "Robot to'siqni ko'rgach nima qiladi?",
        "asosiy": [
            "Robot avval to'xtaydi.",
            "Keyin biroz orqaga qaytib, boshqa tomonga buriladi.",
            "So'ng yana oldinga yuradi.",
        ],
        "chuqur": "Yaxshi algoritm to'siqning qaysi tomonda ekanini ham aniqlab, mos tomonga buriladi.",
        "tajriba": "Robot yo'liga to'siq qo'yib, uning qochish harakatini kuzatish.",
        "uyga": "Robot to'siqni sezganda bajaradigan qadamlarni tartib bilan yozing.",
    },
    {
        "fokus": "Sensorlar avtomatik tizimlarda",
        "savol": "Sensorlar hayotimizda qayerda ishlatiladi?",
        "asosiy": [
            "Avtomatik eshik, chiroq, lift — hammasi sensorli.",
            "Telefon ham ko'plab sensordan foydalanadi.",
            "Sensor zamonaviy texnikaning asosi.",
        ],
        "chuqur": "Avtomatik mashinalarda o'nlab sensor bir vaqtda ishlaydi va ma'lumotlari birlashtiriladi.",
        "tajriba": "Model sensorlarini sanab, ular real hayotda qayerda ishlatilishini muhokama qilish.",
        "uyga": "Uyingizdagi sensorli qurilmalarni sanab, ro'yxat qiling.",
    },
]

# ---------------------------------------------------------------------------
# KOSMIK (12 ta)
# ---------------------------------------------------------------------------
SUBTOPICS2["kosmik"] = [
    {
        "fokus": "Kosmik texnika nima uchun maxsus",
        "savol": "Oddiy mashina Oyda yura oladimi?",
        "asosiy": [
            "Oy va Marsda yo'l yo'q — faqat tosh va chang.",
            "Havo ham yo'q, harorat keskin o'zgaradi.",
            "Shuning uchun maxsus texnika kerak.",
        ],
        "chuqur": "Kosmik texnikani ta'mirlash imkoni yo'q — u birinchi urinishdayoq ishonchli ishlashi kerak.",
        "tajriba": "Modelni notekis sirtda yurgizib, oddiy sirt bilan farqni taqqoslash.",
        "uyga": "Oy yuzasi Yerdan nimasi bilan farq qilishini 3 ta band bilan yozing.",
    },
    {
        "fokus": "Notekis yuzada harakat",
        "savol": "Tosh-qumli yerda qanday yurish mumkin?",
        "asosiy": [
            "Oddiy g'ildirak qumga botib qolishi mumkin.",
            "Keng g'ildirak bosimni kamaytiradi.",
            "Shuning uchun roverlar keng g'ildirakli.",
        ],
        "chuqur": "Yer bosimi = og'irlik / tegib turgan yuza; keng g'ildirak bosimni kamaytirib botishning oldini oladi.",
        "tajriba": "Modelni yumshoq sirtda (mato, qum) yurgizib, g'ildirak botishini kuzatish.",
        "uyga": "Qumda yurish uchun qanday g'ildirak kerakligini chizib ko'rsating.",
    },
    {
        "fokus": "Ko'p g'ildirakli tizim",
        "savol": "Nega roverlarda 6 ta g'ildirak bor?",
        "asosiy": [
            "Ko'p g'ildirak yaxshiroq tayanch beradi.",
            "Bittasi to'siqqa tushsa, qolganlari harakatni davom ettiradi.",
            "Bu ishonchlilikni oshiradi.",
        ],
        "chuqur": "Ko'p g'ildirakli tizimda bir g'ildirak ishdan chiqsa ham rover harakatda qola oladi.",
        "tajriba": "Modelning g'ildiraklarini sanab, bittasi to'siqda bo'lganda nima bo'lishini kuzatish.",
        "uyga": "Mars roverlaridan birining g'ildiraklari sonini toping va yozing.",
    },
    {
        "fokus": "To'siqdan oshib o'tish",
        "savol": "Rover katta toshga duch kelsa nima qiladi?",
        "asosiy": [
            "Rover to'siqni aylanib o'tishi mumkin.",
            "Yoki maxsus osma tizim bilan ustidan oshadi.",
            "G'ildirak diametri katta bo'lsa, oshish osonroq.",
        ],
        "chuqur": "Rover odatda g'ildirak radiusidan kichik to'siqlardan bemalol oshib o'ta oladi.",
        "tajriba": "Model yo'liga kichik to'siq qo'yib, u oshib o'ta oladimi sinash.",
        "uyga": "Rover qanchalik baland to'siqdan osha olishini taxmin qilib yozing.",
    },
    {
        "fokus": "Past gravitatsiya ta'siri",
        "savol": "Oyda narsalar nega yengil bo'ladi?",
        "asosiy": [
            "Oyning tortish kuchi Yernikidan ancha kam.",
            "Shuning uchun u yerda hamma narsa yengilroq.",
            "Lekin massa o'zgarmaydi — faqat og'irlik o'zgaradi.",
        ],
        "chuqur": "Oyda tortish kuchi Yerdagining taxminan oltidan biriga teng.",
        "tajriba": "Model og'irligi o'zgarsa harakat qanday o'zgarishini muhokama qilish.",
        "uyga": "Yerda 60 kg keladigan odam Oyda taxminan qancha bo'lishini hisoblang.",
    },
    {
        "fokus": "Rover energiyani qayerdan oladi",
        "savol": "Oyda benzin quyish mumkin emas — rover qanday ishlaydi?",
        "asosiy": [
            "Roverlar quyosh panelidan energiya oladi.",
            "Energiya batareyada saqlanadi.",
            "Tunda yoki changda energiya kamayadi.",
        ],
        "chuqur": "Ba'zi uzoq missiyalarda quyosh yetarli bo'lmagani uchun radioizotop generatorlari ishlatiladi.",
        "tajriba": "Modelning energiya manbaini aniqlab, u qancha vaqt ishlashini muhokama qilish.",
        "uyga": "Quyosh paneli ishlatiladigan 2 ta qurilmani yozing.",
    },
    {
        "fokus": "Rover qanday boshqariladi",
        "savol": "Marsdagi roverni kim boshqaradi?",
        "asosiy": [
            "Rover Yerdan buyruq oladi.",
            "Lekin signal borishi uchun bir necha daqiqa kerak.",
            "Shuning uchun rover ba'zi qarorlarni o'zi qabul qiladi.",
        ],
        "chuqur": "Marsdan signal Yerga 3-22 daqiqada yetadi — shuning uchun real vaqtda boshqarish imkonsiz.",
        "tajriba": "Modelni avtomatik (dasturli) va qo'lda boshqarish farqini muhokama qilish.",
        "uyga": "Nega Mars roveri o'zi qaror qabul qilishi kerakligini tushuntirib yozing.",
    },
    {
        "fokus": "Rover nima ish bajaradi",
        "savol": "Rover kosmosda nima qiladi?",
        "asosiy": [
            "Rover tuproq va tosh namunalarini oladi.",
            "Rasmga oladi va o'lchovlar o'tkazadi.",
            "Ma'lumotlarni Yerga yuboradi.",
        ],
        "chuqur": "Roverlar suv izlari va hayot belgilarini qidirish uchun maxsus asboblar bilan jihozlanadi.",
        "tajriba": "Modelda namuna olish yoki ushlash qismi bor-yo'qligini aniqlash.",
        "uyga": "Rover qanday vazifalarni bajarishi mumkinligini 3 ta band bilan yozing.",
    },
    {
        "fokus": "Harorat va himoya",
        "savol": "Kosmosda juda sovuq va juda issiq — texnika qanday chidaydi?",
        "asosiy": [
            "Kosmik texnika maxsus qatlam bilan o'raladi.",
            "U ham sovuqdan, ham issiqdan himoya qiladi.",
            "Ichki qismlar doim ma'lum haroratda saqlanadi.",
        ],
        "chuqur": "Havo yo'qligi sababli issiqlik faqat nurlanish orqali tarqaladi — bu maxsus yechim talab qiladi.",
        "tajriba": "Model himoya qoplamasi bor-yo'qligini kuzatish va nega kerakligini muhokama qilish.",
        "uyga": "Kosmik kostyum nima uchun qalin ekanini yozing.",
    },
    {
        "fokus": "Yurish (oyoqli) kosmik texnika",
        "savol": "G'ildirak o'rniga oyoq ishlatish mumkinmi?",
        "asosiy": [
            "Oyoqli robotlar juda notekis yerda yaxshiroq harakatlanadi.",
            "Ular to'siq ustidan qadam tashlab o'tadi.",
            "Lekin ular murakkab va sekinroq.",
        ],
        "chuqur": "Oyoqli tizim ko'proq energiya talab qiladi va boshqarish murakkabroq — shuning uchun hozircha g'ildirak ustunlik qiladi.",
        "tajriba": "Model oyoqli bo'lsa, uni to'siq ustidan o'tkazib sinash.",
        "uyga": "G'ildirakli va oyoqli robot afzalliklarini taqqoslab yozing.",
    },
    {
        "fokus": "Kosmik yuk tashish",
        "savol": "Kosmosga yuk qanday olib boriladi?",
        "asosiy": [
            "Har bir kilogramm juda qimmat turadi.",
            "Shuning uchun texnika yengil qilib yasaladi.",
            "Ba'zi qismlar joyida yig'iladi.",
        ],
        "chuqur": "Kosmosga 1 kg yuk chiqarish minglab dollar turadi — shuning uchun har gramm hisobga olinadi.",
        "tajriba": "Modelni yengillashtirish mumkin bo'lgan joylarni aniqlash.",
        "uyga": "Kosmik texnika nega yengil bo'lishi kerakligini tushuntirib yozing.",
    },
    {
        "fokus": "Kelajakdagi kosmik missiyalar",
        "savol": "Kelajakda kosmosda qanday robotlar ishlaydi?",
        "asosiy": [
            "Kelajakda robotlar Oyda baza qurishi mumkin.",
            "Ular o'zi qaror qabul qiladigan darajada aqlli bo'ladi.",
            "Bir necha robot birga ishlashi rejalashtirilmoqda.",
        ],
        "chuqur": "Robotlar guruhi (swarm) birgalikda ishlab, bitta katta robotdan ko'ra ishonchliroq bo'lishi mumkin.",
        "tajriba": "O'z modelini kelajak missiyasi uchun qanday takomillashtirish mumkinligini muhokama qilish.",
        "uyga": "Kelajakdagi kosmik missiya haqida o'z g'oyangizni yozing.",
    },
    {
        "fokus": "Kosmik texnikaning ishonchliligi",
        "savol": "Kosmosda buzilgan robotni kim tuzatadi?",
        "asosiy": [
            "Kosmosda ta'mirlash deyarli imkonsiz.",
            "Shuning uchun texnika juda ishonchli bo'lishi kerak.",
            "Har bir qism ko'p marta sinovdan o'tkaziladi.",
        ],
        "chuqur": "Muhim tizimlar ikki nusxada quriladi — biri ishdan chiqsa, ikkinchisi ishlaydi (zaxiralash).",
        "tajriba": "Modelning eng zaif qismini topib, uni qanday ishonchliroq qilish mumkinligini muhokama qilish.",
        "uyga": "Nima uchun kosmik texnika ko'p marta sinovdan o'tkazilishini yozing.",
    },
    {
        "fokus": "Chang va kir muammosi",
        "savol": "Oydagi chang texnikaga zarar bera oladimi?",
        "asosiy": [
            "Oy changi juda mayda va o'tkir.",
            "U mexanizm ichiga kirib, ishlashiga xalaqit beradi.",
            "Quyosh panelini ham qoplab qo'yadi.",
        ],
        "chuqur": "Oy changi statik elektrlanganligi sababli yuzalarga yopishib qoladi — bu jiddiy muhandislik muammosi.",
        "tajriba": "Modelning harakatlanuvchi qismlari ochiq yoki himoyalanganligini kuzatish.",
        "uyga": "Changdan himoyalanish uchun qanday yechim taklif qilasiz — yozing.",
    },
    {
        "fokus": "Namuna olish mexanizmi",
        "savol": "Rover tuproqni qanday oladi?",
        "asosiy": [
            "Roverda maxsus qo'l yoki cho'mich bo'ladi.",
            "U tuproqni olib, maxsus idishga soladi.",
            "Keyin ichki asboblar uni tekshiradi.",
        ],
        "chuqur": "Ba'zi roverlarda burg'ulash moslamasi bo'lib, u yer ostidan ham namuna ola oladi.",
        "tajriba": "Modelda ushlash yoki olish qismi bo'lsa, uni sinab ko'rish.",
        "uyga": "Namuna olish uchun qanday mexanizm kerakligini chizib ko'rsating.",
    },
    {
        "fokus": "Kosmik aloqa",
        "savol": "Rover ma'lumotni Yerga qanday yuboradi?",
        "asosiy": [
            "Rover radio to'lqinlar orqali ma'lumot yuboradi.",
            "Katta antenna signalni uzoqqa uzatadi.",
            "Ba'zan sun'iy yo'ldosh orqali uzatiladi.",
        ],
        "chuqur": "Uzoq masofada signal juda kuchsizlanadi — shuning uchun Yerda ulkan antennalar ishlatiladi.",
        "tajriba": "Modelda antenna yoki aloqa qismi bor-yo'qligini aniqlash.",
        "uyga": "Radio to'lqin ishlatiladigan 3 ta qurilmani yozing.",
    },
    {
        "fokus": "Kosmik texnikani sinash",
        "savol": "Roverni Yerda qanday sinab ko'rish mumkin?",
        "asosiy": [
            "Yerda maxsus maydonchalar quriladi.",
            "Ular Oy yoki Mars yuzasiga o'xshatiladi.",
            "Rover u yerda uzoq vaqt sinaladi.",
        ],
        "chuqur": "Bunday sinov maydonchalari \"Mars yard\" deb ataladi va haqiqiy missiyadan oldin barcha vaziyat sinab ko'riladi.",
        "tajriba": "Sinf ichida \"kosmik yuza\" yasab (matolar, kitoblar bilan), modelni sinab ko'rish.",
        "uyga": "Uyda \"Mars yuzasi\" yasab, modelingizni sinab ko'ring va natijani yozing.",
    },
    {
        "fokus": "Kosmik texnika og'irligi va o'lchami",
        "savol": "Rover katta bo'lgani yaxshimi yoki kichik?",
        "asosiy": [
            "Katta rover ko'proq asbob olib yura oladi.",
            "Lekin uni kosmosga chiqarish qimmat va qiyin.",
            "Kichik rover arzon, lekin kam ish bajaradi.",
        ],
        "chuqur": "Missiya rejalashtirishda har doim imkoniyat va og'irlik orasida muroza qilinadi.",
        "tajriba": "Modelga qo'shimcha \"asbob\" (detal) qo'shib, harakatlanish qiyinlashganini kuzatish.",
        "uyga": "Katta va kichik rover afzalliklarini taqqoslab yozing.",
    },
    {
        "fokus": "Kosmik texnikada avtomatik xavfsizlik",
        "savol": "Rover xato qilsa, o'zini qanday saqlaydi?",
        "asosiy": [
            "Roverda xavfli holatni sezuvchi tizim bo'ladi.",
            "Muammo sezilsa, u to'xtaydi va Yerdan buyruq kutadi.",
            "Bu \"xavfsiz rejim\" deb ataladi.",
        ],
        "chuqur": "Xavfsiz rejim (safe mode) — noaniq vaziyatda hech narsa qilmay turish; bu missiyani saqlab qoladi.",
        "tajriba": "Model to'siqqa duch kelganda to'xtashi kerakmi yoki davom etishi — muhokama qilish.",
        "uyga": "Robot qanday holatlarda o'zini to'xtatishi kerakligini 2 ta misol bilan yozing.",
    },
    {
        "fokus": "Boshqa sayyoralarni o'rganish",
        "savol": "Nega odamlar boshqa sayyoralarni o'rganadi?",
        "asosiy": [
            "Boshqa sayyoralarda suv yoki hayot izlari bo'lishi mumkin.",
            "Ular Yer tarixini tushunishga yordam beradi.",
            "Kelajakda u yerda yashash imkoni ham o'rganilmoqda.",
        ],
        "chuqur": "Mars tadqiqotlarining asosiy maqsadlaridan biri — o'tmishda suyuq suv bo'lganini isbotlash.",
        "tajriba": "Model qanday tadqiqot vazifasini bajara olishini muhokama qilish.",
        "uyga": "Boshqa sayyorada nimani o'rganishni istagan bo'lardingiz — yozing.",
    },
]
