# -*- coding: utf-8 -*-
"""
1-yil (barcha sinflar) uchun har chorak nazorat ishi — musobaqa formatida.
1-chorak (RoboRace) — foydalanuvchi tomonidan aniq berilgan. 2-4-chorak — shu uslubda
taklif etilgan namuna (aniq vaqt me'yorlari maktabda sinov orqali moslashtirilishi mumkin).
"""

QUARTER_NAZORAT = {
    1: (
        "1-chorak nazorat ishi — \"RoboRace\" musobaqasi: robot 2 metr masofani bosib o'tish "
        "vaqti bo'yicha baholanadi. Baholash mezoni: 10 soniyagacha = 5 (a'lo); 11-25 soniya = 4 "
        "(yaxshi); 26-45 soniya = 3 (qoniqarli); 46-60 soniya = 2 (qoniqarsiz); 1 daqiqadan ortiq "
        "(60 soniyadan ko'p) yoki finishga yetib bormasa = FAILED (topshiriq bajarilmagan)."
    ),
    2: (
        "2-chorak nazorat ishi — \"RoboLift\" musobaqasi: robot belgilangan yukni (1 ta standart "
        "kubik/detal) ko'tarib, 1 metr masofaga tashish vaqti bo'yicha baholanadi. Baholash mezoni: "
        "15 soniyagacha = 5 (a'lo); 16-30 soniya = 4 (yaxshi); 31-50 soniya = 3 (qoniqarli); "
        "51-60 soniya = 2 (qoniqarsiz); 1 daqiqadan ortiq yoki yukni tushirib yuborsa = FAILED. "
        "(Aniq vaqt me'yorlari maktabda sinov orqali moslashtirilishi mumkin.)"
    ),
    3: (
        "3-chorak nazorat ishi — \"RoboSense\" musobaqasi: sensorli robot 1.5 metr masofada "
        "to'siqni to'g'ri aniqlab, to'xtashi yoki aylanib o'tishi kerak — vaqt VA to'g'ri aniqlash "
        "birga baholanadi. Baholash mezoni: 15 soniyagacha va to'siqni to'g'ri aniqlagan = 5 (a'lo); "
        "16-30 soniya = 4 (yaxshi); 31-50 soniya = 3 (qoniqarli); 51-60 soniya = 2 (qoniqarsiz); "
        "1 daqiqadan ortiq YOKI to'siqni sezmay to'qnashsa = FAILED."
    ),
    4: (
        "4-chorak (yakuniy) nazorat ishi — \"RoboChampionship\" (yil yakuni musobaqasi): robot "
        "kamida 1 burilish va 1 to'siqli, 2.5-3 metrlik murakkab yo'lakni bosib o'tish vaqti bo'yicha "
        "baholanadi. Baholash mezoni: 20 soniyagacha = 5 (a'lo); 21-40 soniya = 4 (yaxshi); "
        "41-55 soniya = 3 (qoniqarli); 56-70 soniya = 2 (qoniqarsiz); 70 soniyadan ortiq yoki "
        "yo'lakni tugatolmasa = FAILED. G'oliblarga sertifikat/kichik sovrin tavsiya etiladi."
    ),
}
