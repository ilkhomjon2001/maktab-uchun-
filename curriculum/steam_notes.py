# -*- coding: utf-8 -*-
"""
Har bir dars mavzusi/model uchun qisqa STEAM (fizika/muhandislik) tushuntirishi.
Kalit so'z bo'yicha moslashtiriladi — eng mos birinchi qoida ishlatiladi.
"""

STEAM_RULES = [
    # (keywords tuple, tushuntirish)
    (("ko'prik", "bridge"),
     "STEAM: Ko'prik konstruksiyasi uchburchak shakllar orqali mustahkam bo'ladi — uchburchak "
     "burchaklari kuch ta'sirida o'zgarmaydi, shu sababli yuk konstruksiya bo'ylab teng taqsimlanadi."),
    ("kran",
     "STEAM: Kran richag va shkiv tamoyilini birlashtiradi — uzun qo'l aylanish momentini oshiradi, "
     "shkiv esa kerakli ko'tarish kuchini kamaytiradi."),
    ("ekskavator",
     "STEAM: Ekskavator qo'li ketma-ket richaglar zanjiridan iborat — har bir bo'g'im alohida "
     "kuch momentini hosil qilib, uzoq masofaga yetib borish va katta kuch berishni ta'minlaydi."),
    (("forklift", "ko'targich", "lifting"),
     "STEAM: Ko'targich mexanizmi richag yoki vint tamoyili orqali tik yo'nalishda kam kuch bilan "
     "og'ir yukni ko'taradi."),
    (("richag", "pilers", "jackknife", "wheelbarrow", "hayfork", "rake"),
     "STEAM: Richag — tayanch nuqtasi (os') atrofida aylanadigan qattiq jism; kuch yelkasi uzunroq "
     "bo'lsa, kichik kuch bilan katta yukni ko'tarish mumkin."),
    (("tishli g'ildirak", "gear", "buhr mill", "grinding"),
     "STEAM: Tishli g'ildiraklar tezlik va kuchni bir-biriga almashtiradi — kichik g'ildirak tezroq "
     "aylanadi, katta g'ildirak esa ko'proq kuch (moment) beradi."),
    (("shkiv", "pulley", "conveyor", "konveyer"),
     "STEAM: Shkiv-tasma tizimi kuch yo'nalishini o'zgartiradi va uzatadi, bir necha shkiv birgalikda "
     "ishlatilsa, kerakli tortish kuchi kamayadi."),
    (("krivoship", "joint motion", "jumping", "rocking", "roating", "rotating"),
     "STEAM: Krivoship-shatun mexanizmi aylanma harakatni tebranma (oldinga-orqaga yoki yuqori-past) "
     "harakatga aylantiradi — dvigatelning klassik tamoyili."),
    (("differensial",),
     "STEAM: Differensial mexanizm burilishda ikki g'ildirakka turli tezlikda aylanish imkonini "
     "beradi — tashqi g'ildirak ichkisiga qaraganda uzunroq yo'l bosadi."),
    (("muvozanat", "balance", "barqarorlik", "teeterboard", "tumbler", "balance car"),
     "STEAM: Jism muvozanatda turishi uchun uning og'irlik markazi tayanch nuqtasi tepasida bo'lishi "
     "kerak — past va keng tayanch barqarorlikni oshiradi."),
    (("vint", "drill", "extrusion", "stirrer"),
     "STEAM: Vint (spiral) mexanizmi aylanma harakatni chiziqli harakatga aylantiradi yoki moddani "
     "bir joydan ikkinchisiga siljitadi."),
    (("g'ildirak", "wheel", "arava", "trailer", "scooter", "skateboard"),
     "STEAM: G'ildirak va o'q ishqalanish kuchini kamaytirib, harakatni ancha osonlashtiradi "
     "(sirpanish ishqalanishi aylanish ishqalanishidan katta)."),
    (("motor",),
     "STEAM: Elektr motor elektr energiyasini aylanma mexanik harakatga aylantiradi — bu ichida "
     "magnit maydon va tok o'zaro ta'sirlashuvi (elektromagnit induksiya) orqali sodir bo'ladi."),
    (("gyroskop", "gyro"),
     "STEAM: Gyroskopik sensor burchak tezligini o'lchaydi — robot qancha va qaysi tomonga "
     "burilganini aniq biladi, bu esa to'g'ri yo'nalishda yurishga yordam beradi."),
    (("rang sensor", "color"),
     "STEAM: Rang sensori sirtdan qaytgan yorug'lik to'lqin uzunligini o'lchab, uni rangga aylantiradi."),
    (("chiziq", "line patrol"),
     "STEAM: Chiziq kuzatuvchi robot yorug'likning sirtdan aks etish farqidan foydalanadi — oq sirt "
     "ko'proq, qora chiziq kamroq yorug'lik qaytaradi, sensor shu farqni o'qiydi."),
    (("to'siqdan qochish", "obstacle", "masofa sensor", "ultratovush", "distance"),
     "STEAM: Masofa sensori tovush yoki infraqizil signal yuborib, uning to'siqdan qaytib kelish "
     "vaqtini o'lchaydi — shu vaqtdan masofa hisoblanadi (tovush tezligi asosida)."),
    (("bosim", "kuch sensor", "force", "touch"),
     "STEAM: Bosim (kuch) sensori unga qo'llanilgan mexanik bosimni elektr signaliga aylantiradi."),
    (("sensor",),
     "STEAM: Sensor — atrof-muhitdagi fizik o'zgarishni (yorug'lik, masofa, bosim, harakat) "
     "elektr signaliga aylantiruvchi qurilma; robot shu signal orqali \"his qiladi\"."),
    (("algoritm", "ketma-ketlik", "buyruq"),
     "STEAM: Algoritm — masalani hal qilish uchun aniq va tartibli qadamlar ketma-ketligi; "
     "har qanday dastur asosida shu tamoyil yotadi."),
    (("shart", "agar", "if"),
     "STEAM: Shartli operator (\"agar...bo'lsa\") dasturga vaziyatga qarab turlicha qaror qabul "
     "qilish imkonini beradi — bu robotni \"aqlli\" qiladigan asosiy mantiq."),
    (("sikl", "takrorlash", "loop"),
     "STEAM: Sikl (takrorlash) bir xil harakatni qayta-qayta yozmasdan bir necha marta bajarish "
     "imkonini beradi — dasturlashda samaradorlik tamoyili."),
    (("o'zgaruvchi", "hisoblagich", "variable"),
     "STEAM: O'zgaruvchi — dastur ishlash jarayonida qiymati o'zgarishi mumkin bo'lgan \"xotira "
     "katakchasi\"; hisoblash va holatni kuzatish uchun ishlatiladi."),
    (("funksiya",),
     "STEAM: Funksiya — qayta-qayta ishlatiladigan buyruqlar to'plami; dasturni qisqa, tushunarli "
     "va xatosiz qiladi (muhandislikdagi \"modullilik\" tamoyili)."),
    (("holat mashinasi", "state machine"),
     "STEAM: Holat mashinasi — robot bir vaqtning o'zida faqat bitta \"holat\"da bo'lib, voqealarga "
     "qarab boshqa holatga o'tishi mumkin (masalan: to'xtagan -> yuruvchi -> to'siq oldida)."),
    (("crane", "tower crane", "bridge crane"),
     "STEAM: Kran richag va shkiv tamoyilini birlashtiradi — uzun qo'l aylanish momentini oshiradi, "
     "shkiv esa kerakli ko'tarish kuchini kamaytiradi."),
    (("fan", "propeller", "helicopter", "aircraft", "plane", "jet", "fighter"),
     "STEAM: Aylanuvchi parrak havo massasini itarib, reaktiv kuch hosil qiladi (Nyutonning uchinchi "
     "qonuni: har bir ta'sirga teng va qarama-qarshi aks ta'sir mavjud)."),
    (("boat", "ship"),
     "STEAM: Suzuvchi vositalar suv siqib chiqargan bosim kuchi (Arximed qonuni) tufayli suv "
     "yuzasida qalqib turadi."),
    (("rover", "satellite", "lunar", "moon", "interstellar", "interplanetary", "space", "cosmic"),
     "STEAM: Kosmik texnika og'ir yuklarni kam ishqalanishli maxsus g'ildirak tizimlari orqali "
     "notekis yuzalarda harakatlantiradi."),
    (("tyrannosaurus", "stegosaurus", "triceratops", "crocodile", "dolphin", "brachiosaurus",
      "hadrosaur", "euoplocephalus", "buffalo", "mouse", "cat", "bear", "deer", "rabbit", "bull",
      "tortoise"),
     "STEAM: Hayvon-robotlar oyoq yoki dum harakatini krivoship-shatun mexanizmi orqali taqlid "
     "qiladi — bu \"biomimikriya\" (tabiatdan ilhomlanib muhandislik yechimi yaratish) deb ataladi."),
    (("car", "truck", "motorcycle", "tractor", "vehicle", "patrol", "combat", "battle", "trailer"),
     "STEAM: Transport vositasi g'ildirak va o'q yordamida ishqalanishni kamaytirib, motor kuchini "
     "tekis harakatga aylantiradi."),
    (("gate", "darvoza"),
     "STEAM: Avtomatik darvoza richag yoki vint mexanizmi orqali ochiladi-yopiladi."),
    (("scooter", "wings", "copter"),
     "STEAM: Muvozanat va aerodinamika tamoyillari — jismning shakli havo/harakat qarshiligiga "
     "ta'sir qiladi."),
]

DEFAULT_STEAM = ("Amaliy dars: qisqa tushuntirishdan so'ng asosiy vaqt qurish/dasturlash/sinovga "
                  "ajratiladi (nazariy ma'ruza sifatida o'tilmaydi).")

NAZORAT_STEAM = ("Amaliy nazorat: o'quvchi robotni yig'ib/dasturlab, ishlashini ko'rsatish orqali "
                  "baholanadi (yozma test emas).")


def get_steam_note(topic_text, model_name=None, is_nazorat=False):
    if is_nazorat:
        return NAZORAT_STEAM
    text = (topic_text + " " + (model_name or "")).lower()
    for keys, note in STEAM_RULES:
        if isinstance(keys, str):
            keys = (keys,)
        for k in keys:
            if k.lower() in text:
                return note
    return DEFAULT_STEAM
