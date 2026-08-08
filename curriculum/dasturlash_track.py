# -*- coding: utf-8 -*-
"""
2-yil, 3-4-chorak — YANGI qo'shimcha dasturlash kursi (haftaning 3-soati, Scratch-uslub, Makerzoid ilovasi).
Har bir sinf: 19 dars (Q3: 7 mavzu+1 nazorat+1 loyiha=9; Q4: 8 mavzu+1 nazorat+1 loyiha=10).
1-yilda yasalgan modellarga dastur yozish orqali o'rganiladi — motor/detal xarid qilinmaydi, faqat dastur qo'shiladi.
"""

DASTURLASH_TRACK = {
    "0-sinf": {
        "Q3": {
            "lessons": [
                "Ilovada Scratch-uslub interfeys bilan tanishuv",
                "Birinchi blok: \"Bosilganda ishga tush\"",
                "Motorni blok bilan yurgizish",
                "Motorni to'xtatish blogi",
                "Ikki blokni ketma-ket qo'yish",
                "O'zim yig'gan modelimni dastur bilan yurgizish",
                "Kichik o'yin: kim tez dastur tuzadi",
            ],
            "nazorat": "Amaliy: 2 blokli oddiy dasturni tuzib ko'rsatish",
            "loyiha": "Modelimni ilk marta dastur bilan boshqarish",
        },
        "Q4": {
            "lessons": [
                "Takrorlash blogi (necha marta?) bilan tanishuv",
                "Takrorlash bilan oddiy o'yin",
                "Sensor blogi bilan tanishuv",
                "Sensor+harakat blogini birlashtirish",
                "Kutish (timer) blogi",
                "Tovush blogi qo'shish",
                "O'z modelim uchun to'liq dastur (4-5 blok)",
                "Dasturni sinash va tuzatish",
            ],
            "nazorat": "Amaliy: 4-5 blokli dasturni tuzib, sinab ko'rsatish",
            "loyiha": "Yakuniy dastur: 1-yilda yasagan sevimli modelimni \"jonlantirish\"",
        },
    },
    "1-sinf": {
        "Q3": {
            "lessons": [
                "Scratch-uslub interfeys, blok turlari",
                "Ketma-ketlik: 3-4 blokli dastur",
                "Motor blogi bilan mashg'ulot",
                "Takrorlash (sikl) blogi",
                "Sikl bilan naqshli harakat",
                "Sensor blogi bilan tanishuv",
                "Sensor+harakat: oddiy reaksiya",
            ],
            "nazorat": "Amaliy: sikl+sensor ishlatilgan dasturni ko'rsatish",
            "loyiha": "1-yilda yasagan modelimga dastur yozish",
        },
        "Q4": {
            "lessons": [
                "Shart (agar) blogi bilan tanishuv",
                "Shart bilan o'yin",
                "Ikki shartni solishtirish",
                "Tovush/animatsiya bloklari",
                "Bir nechta blokni guruhlash (funksiya boshlang'ichi)",
                "O'z loyiham uchun dastur rejasi",
                "Dasturni yozish",
                "Sinov va tuzatish",
            ],
            "nazorat": "Amaliy: shart ishlatilgan to'liq dasturni ko'rsatish",
            "loyiha": "Yakuniy dastur: sevimli modelimga \"aql\" qo'shish",
        },
    },
    "2-sinf": {
        "Q3": {
            "lessons": [
                "Scratch-uslub muhitni chuqurroq o'rganish",
                "Ketma-ketlik+sikl mustahkamlash",
                "O'zgaruvchi (hisoblagich) bilan tanishuv",
                "Hisoblagich bilan o'yin",
                "Ikki sensorni birlashtirish",
                "Shart ichida shart (murakkabroq)",
                "Debugging: xatoni topish mashqi",
            ],
            "nazorat": "Amaliy: o'zgaruvchi+shart ishlatilgan dasturni ko'rsatish",
            "loyiha": "1-yil modelimga \"xotira\" (hisoblagich) qo'shish",
        },
        "Q4": {
            "lessons": [
                "Funksiya (blok guruhi) tushunchasi",
                "O'z funksiyamni yaratish",
                "Funksiyadan qayta foydalanish",
                "Parallel harakatlar (motor+tovush bir vaqtda)",
                "Vaqt boshqaruvi (timer bilan)",
                "Murakkab loyiha rejasi",
                "Dasturni yozish",
                "Sinov, tuzatish, yakunlash",
            ],
            "nazorat": "Amaliy: funksiyalardan foydalangan dasturni ko'rsatish",
            "loyiha": "Yakuniy dastur: 1-yil eng sevimli modelimni to'liq avtomatlashtirish",
        },
    },
    "3-sinf": {
        "Q3": {
            "lessons": [
                "Scratch-uslub muhitni chuqur takrorlash",
                "Murakkab shartlar: VA, YOKI",
                "Mantiqiy o'yin",
                "Ichma-ich sikllar",
                "Naqshli harakat dasturi",
                "Ikki sensorli qaror qabul qilish",
                "Ko'p qadamli dastur rejasi",
            ],
            "nazorat": "Amaliy: VA/YOKI va ichma-ich sikl ishlatilgan dasturni ko'rsatish",
            "loyiha": "1-yil modelimga murakkab mantiq qo'shish",
        },
        "Q4": {
            "lessons": [
                "Holat (state) tushunchasi — sodda",
                "Holatlar bilan o'yin",
                "Xato-bardosh dastur (agar sensor ishlamasa?)",
                "Debugging usullari",
                "Dasturni optimallashtirish",
                "Yakuniy loyiha rejasi",
                "Dasturni yozish",
                "Sinov, tuzatish, taqdimot",
            ],
            "nazorat": "Amaliy: to'liq avtonom dasturni ko'rsatish",
            "loyiha": "Yakuniy dastur: 1-yil eng murakkab modelimni to'liq \"aqlli\" qilish (SPIKE'ga tayyorgarlik)",
        },
    },
}
