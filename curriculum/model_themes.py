# -*- coding: utf-8 -*-
"""
Har bir model uchun: (1) Dars mavzusi = ILMIY/STEAM tushuncha (masalan "Ishqalanish kuchi"),
(2) O'qituvchi uchun qo'llanma = darsda NIMALARNI tushuntirish kerakligi bo'yicha yo'riqnoma.
Model nomi (masalan "Little Lantern 1") alohida "Amaliy ish" ustunida ko'rsatiladi.
"""

THEMES = {
    "richag": (
        "Richag qonuni",
        "O'quvchilarga richag nima ekanligini tushuntiring: tayanch nuqtasi (os') atrofida "
        "aylanadigan qattiq jism. Kuch yelkasi uzunroq bo'lsa, kichik kuch bilan katta yukni "
        "ko'tarish mumkinligini amaliy misolda ko'rsating (masalan, uzun tayoq bilan og'ir "
        "toshni qo'zg'atish). Kundalik hayotdan misollar so'rang: qaychi, eshik dastagi, teeter-totter."
    ),
    "tishli": (
        "Tishli g'ildirak uzatmasi",
        "Tishli g'ildiraklar tezlik va kuchni bir-biriga qanday almashtirishini tushuntiring: "
        "kichik g'ildirak tezroq aylanadi, katta g'ildirak esa ko'proq kuch (moment) beradi. "
        "Ikki xil o'lchamdagi tishlini qo'lda aylantirib, tezlik farqini ko'rsating. Velosiped "
        "uzatmasi bilan solishtiring."
    ),
    "shkiv": (
        "Shkiv va tortish kuchi",
        "Shkiv-tasma tizimining kuch yo'nalishini o'zgartirishini va bir necha shkiv birga "
        "ishlatilsa kerakli tortish kuchi kamayishini tushuntiring. Qudiq chig'iri yoki lift "
        "tros tizimi bilan solishtiring."
    ),
    "krivoship": (
        "Aylanma harakatni tebranishga aylantirish",
        "Krivoship-shatun mexanizmini tushuntiring: motor/qo'l aylanma harakat beradi, mexanizm "
        "buni oldinga-orqaga yoki yuqori-past tebranma harakatga aylantiradi. Bu dvigatelning "
        "klassik ishlash tamoyili — velosiped pedali va tizza harakatini misol qiling."
    ),
    "muvozanat": (
        "Muvozanat markazi",
        "Jismning muvozanatda turishi uchun og'irlik markazi tayanch nuqtasi tepasida bo'lishi "
        "kerakligini tushuntiring. Past va keng tayanch barqarorlikni oshirishini amaliy sinab "
        "ko'ring (modelni turli holatlarda qiyshaytirib, qachon yiqilishini kuzating)."
    ),
    "geometriya": (
        "Geometrik shakl mustahkamligi",
        "Nima uchun uchburchak shakl o'zgarmasligini (mustahkam), to'rtburchak esa oson egilib "
        "ketishini (beqaror) qo'lda sinab ko'rsating. Ko'prik va minoralarda nega uchburchak "
        "ko'p ishlatilishini muhokama qiling."
    ),
    "elastik": (
        "Elastik energiya va inersiya kuchi",
        "Elastik element (rezina/prujina) cho'zilganda potensial energiya to'planishini va "
        "qo'yib yuborilganda bu energiya harakat energiyasiga aylanishini tushuntiring. "
        "Pull-back (orqaga tortib qo'yib yuborish) mexanizmida inersiya qonunini (Nyutonning "
        "1-qonuni) ko'rsating: jism harakatga tushgach, kuch to'xtatmasa harakatda davom etadi."
    ),
    "vint": (
        "Vint mexanizmi",
        "Vint (spiral) aylanma harakatni chiziqli harakatga qanday aylantirishini tushuntiring. "
        "Konservka qopqog'i yoki shurup misolida ko'rsating."
    ),
    "ishqalanish": (
        "Ishqalanish kuchi",
        "Ishqalanish kuchi nima ekanligini tushuntiring: ikki sirt tegib harakatlanganda paydo "
        "bo'ladigan qarshilik kuchi. G'ildirakli va g'ildiraksiz harakatni solishtiring — nega "
        "g'ildirak harakatni osonlashtiradi? Silliq va notekis sirtlarda ishqalanish farqini "
        "muhokama qiling (masalan, muzda va asfaltda yurish)."
    ),
    "kotargich": (
        "Ko'tarish mexanizmi (richag+vint+shkiv)",
        "Og'ir yukni kam kuch bilan ko'tarish uchun richag, vint yoki shkivning birgalikda "
        "qanday ishlashini tushuntiring. Haqiqiy kran yoki lift misolida muhokama qiling."
    ),
    "motorAylanma": (
        "Elektr motor va aylanma harakat",
        "Elektr motor elektr energiyasini aylanma mexanik harakatga qanday aylantirishini "
        "(elektromagnit induksiya) sodda tilda tushuntiring. Motorsiz va motorli modelni "
        "solishtirib, farqni his qildiring."
    ),
    "aero": (
        "Aerodinamika va reaktiv kuch",
        "Aylanuvchi parrak havo massasini itarib, reaktiv kuch hosil qilishini tushuntiring "
        "(Nyutonning 3-qonuni: har bir ta'sirga teng va qarama-qarshi aks ta'sir). Vertolyot "
        "parragi va samolyot qanoti farqini muhokama qiling."
    ),
    "suv": (
        "Suzish kuchi (Arximed qonuni)",
        "Suzuvchi vositalar suv siqib chiqargan bosim kuchi tufayli suv yuzasida qalqib "
        "turishini tushuntiring. Og'ir metall kema nega cho'kmasligini muhokama qiling."
    ),
    "biomimikriya": (
        "Biomimikriya (tabiatdan ilhomlanish)",
        "Hayvon-robotlar oyoq yoki dum harakatini qanday mexanizm (odatda krivoship-shatun) "
        "orqali taqlid qilishini tushuntiring. Muhandislar tabiatdan qanday g'oya olishini "
        "(biomimikriya atamasi) misollar bilan tushuntiring — masalan, qush qanotidan samolyot."
    ),
    "sensor": (
        "Sensor va signal",
        "Sensor atrof-muhitdagi fizik o'zgarishni (yorug'lik, masofa, bosim, harakat) elektr "
        "signaliga qanday aylantirishini tushuntiring. Inson sezgi organlari bilan solishtiring "
        "(ko'z=yorug'lik sensori, teri=bosim sensori)."
    ),
    "kosmik": (
        "Notekis yuzada harakat (kosmik texnika)",
        "Kosmik texnika (rover) nega maxsus g'ildirak/oyoq tizimidan foydalanishini tushuntiring "
        "— notekis, tosh-qumli yuzada oddiy g'ildirak siqilib qolishi mumkin. Oy/Mars yuzasi "
        "bilan Yer yuzasini solishtiring."
    ),
    "transport": (
        "Transport va ishqalanish",
        "Transport vositasi g'ildirak-o'q yordamida ishqalanishni kamaytirib, motor kuchini "
        "tekis harakatga aylantirishini tushuntiring. Yuk mashinasi nega ko'p g'ildirakli "
        "bo'lishini muhokama qiling (og'irlik taqsimoti)."
    ),
    "darvoza": (
        "Avtomatik mexanizm (richag/vint)",
        "Avtomatik darvoza yoki eshik richag yoki vint mexanizmi orqali qanday ochilib-yopilishini "
        "tushuntiring. Uy eshigi bilan avtomatik darvozani solishtiring."
    ),
    "holat": (
        "Holat mashinasi (mantiq)",
        "Robot bir vaqtning o'zida faqat bitta \"holat\"da bo'lib, voqealarga qarab boshqa "
        "holatga o'tishini tushuntiring (masalan: to'xtagan -> yuruvchi -> to'siq oldida). "
        "Svetofor holatlari bilan solishtiring."
    ),
}

# Model nomi -> tema kaliti
MODEL_THEME_MAP = {}

def _reg(theme_key, models):
    for m in models:
        MODEL_THEME_MAP[m] = theme_key

_reg("richag", [
    "Pilers", "Jackknife", "Wheelbarrow", "Wheel Barrow", "Hayfork", "Rake", "Expansion Clamp",
    "Insert With Clips", "Jack", "Counter Scale", "Ladder",
])
_reg("tishli", [
    "Grinding Machine", "Manual Buhr Mill", "Electric Buhr Mill", "Eggbeater", "Hand Drill",
    "Manual Drill Car", "Manual Gatling Gun", "Electric Gatling Gun", "Weirdo Clock",
])
_reg("vint", ["Vigorous Extrusion Machine"])
_reg("krivoship", ["Sewing Machine", "Barbecue Grill"])
_reg("kotargich", ["Crawler Excavator"])
_reg("aero", ["Star War Aircraft"])
_reg("biomimikriya", [
    "Tyannosaurus Rex (Adv)", "Stegosaurus (Adv)", "Electric Crocodile 2.0", "Tyrannosaurus (AI)",
])
_reg("sensor", ["Scooter (Prog)", "Programmable Car (AI)", "Flytrap (Prog)"])
_reg("transport", ["Car with YL Man 3", "Car with YL Man 4"])
_reg("shkiv", [
    "Pulley Crane", "Conveyor", "Line Car",
])
_reg("krivoship", [
    "Joint Motion 1", "Joint Motion 2", "Joint Motion 3", "Joint Motion 4",
    "Manual Joint Motion 1", "Manual Joint Motion 2", "Manual Joint Motion 3", "Manual Joint Motion 4",
    "Jumping YL Man 1", "Jumping YL Man 2", "Jumping YL Man 3", "Jumping YL Man 4",
    "Manual Jumping YL Man 1", "Manual Jumping YL Man 2", "Manual Jumping YL Man 3",
    "Manual Jumping YL Man 4", "Manual Jumping YL Man 5",
    "Rocking YL Man 1", "Rocking YL Man 2", "Rocking YL Man 3", "Rocking YL Man 4", "Rocking YL Man 5",
    "Manual Rocking YL Man 1", "Manual Rocking YL Man 2", "Manual Rocking YL Man 3",
    "Manual Rocking YL Man 6", "Manual Rocking YL Man 7", "Manual Rocking YL Man 8",
    "Roating YL Man 1", "Roating YL Man 2",
    "Manual Rotating YL Man 1", "Manual Rotating YL Man 2", "Manual Rotating YL Man 3",
    "Manual Rotating YL Man 4", "Manual Rotating YL Man 5", "Manual Rotating YL Man 6", "Manual Rotating YL Man 7",
    "Dancing Man", "Hoeing Man", "Weighting Man", "Step Man", "Car Puller", "Skiing Man",
    "Inchworm", "Sweeper", "Scarecrow", "Hammer Machine", "Dotting Machine", "Circling Machine",
    "Drawing Machine", "Electric Sewing Machine", "Woodpecker", "Rocking Trojan", "Pastry Chef",
])
_reg("muvozanat", ["Balance", "Teeterboard", "Tumbler", "Swing"])
_reg("geometriya", [
    "Triangle", "Quadrilateral", "Parallelogram", "Lantern",
    "Little Lantern 1", "Little Lantern 2", "Little Lantern 3", "Little Lantern 4",
    "Cellphone Mount", "Christmas Tree",
])
_reg("elastik", [
    "Elastic Band Gun", "Top Launcher (with wheels)", "Elasti-Pumper", "Elasti-Car",
    "Inertia Car 1", "Inertia Car 2", "Inertia Pull-Back Car", "Flytrap",
])
_reg("ishqalanish", [
    "Wheel Car", "Skateboard", "Scooter", "Trailer", "Formula Car", "Speeding Car", "Telecar",
    "Hooded Motorcycle", "Ploughing Tractor", "RWD Car", "Harley", "Turnable F1",
])
_reg("kotargich", [
    "Crane", "Tower Crane", "Bridge Crane", "Fork Lift Truck", "Forklift", "Intelligent Forklift",
    "Combat Forklift", "Excavator (Gear-driven)", "Excavator (Belt-driven)", "Elevator",
    "Lifting Platform", "Oil Extractor", "Ferris Wheel", "Storage Robot", "Intersteller Radar Forklift",
])
_reg("motorAylanma", [
    "Electric Fan", "Rotating Plane", "Gear Shifting Fan", "Pivoting Fan", "Big Hand Fan",
    "Hand Fan", "Spinning Top 3", "Spinning Top 4", "Electric Helicopter",
])
_reg("aero", [
    "Osprey Aircraft", "Transport Helicopter", "Propeller-driven Vehicle", "Twin Propeller Aircraft",
    "Star Fighting", "X Fighter", "Interplanetary Jet", "Alien Reconnaissance Aircraft",
    "Space Shuttle", "Space Transport Aircraft",
])
_reg("suv", ["Dragon Boat"])
_reg("darvoza", ["Rail Gate"])
_reg("biomimikriya", [
    "Buffalo (electric)", "Electric Tyrannosaurus", "Electric Stegosaurus", "Electric Crocodile",
    "Triceratops (electric)", "Dolphin (electric)", "Brachiosaurus (electric)", "Hadrosaur (electric)",
    "Euoplocephalus (electric)", "Electric Mouse", "Electric Cat and Mouse", "Electric Tortoise",
    "Crab (electric)", "Bull", "Little Bear", "Little Deer", "Rabbit (AI)", "Mouse (AI)",
    "Cat And Mouse (AI)", "Crocodile (AI)", "Stegosaurus (AI)", "Crab (AI)", "Crab Premium",
    "Shark", "Koi", "Pterosaur",
])
_reg("sensor", [
    "Score Indicator", "Sorting Box", "Color Sorting", "Score Maker (AI)", "Bus",
    "Automatic Gate", "Automatic Gate (Prog)", "Intelligent Gate", "Mine Clearance",
    "Obstacle Avoiding Car", "Obstacle Avoiding (2)", "Obstacle Avoiding (3)",
    "Line Patrol Tank", "Line Patrol Dog", "Line Patrol Dragon", "Animal Trap",
])
_reg("kosmik", [
    "Moon Rover", "Off-road Rover", "Exploration Robot", "Satellite Car", "Transport Walker",
    "Reconnaissance Walker", "Moon Exploration Vehicle", "Batmobile", "Interstellar Cannon",
    "Satellite Rover", "Intersteller Pathfinder Robot", "Probe Robot", "Plantary System",
    "Collection Robot", "Moon Collection Rover", "Armoured Vehicle (Space)", "Interstellar Train",
    "Lunar Transporter", "Interplanetary Repair Station", "Dual Motor Lunar Rover",
])
_reg("transport", [
    "Armoured Vehicle", "Infantry Fighting Vehicle", "Transformers", "Cheetch", "Kowtow Machine",
    "Infinite Loop", "Upside Down", "Steam Train", "Santa Claus Car", "Santa Claus Car 2",
    "Santa's Sleigh", "Big Truck", "Patrol Car", "Inspection Robot", "Battle Robot",
    "Combat Robot", "War Robot", "Car with YL Man 1", "Car with YL Man 2", "Wings Car",
])


def get_theme_and_guide(model_name):
    key = MODEL_THEME_MAP.get(model_name)
    if key:
        return THEMES[key]
    return ("Muhandislik konstruksiyasi",
            "Modelning asosiy qismlari va ular birgalikda qanday ishlashini o'quvchilarga "
            "tushuntiring, keyin qurishga o'ting.")
