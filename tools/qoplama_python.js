/*
 * 4-SINF QOPLAMASI — MATNLI DASTURLASH (Python, SPIKE App 3)
 * =========================================================
 * 3-sinf va 4-sinf BIR XIL robotlarni quradi. Farq — dasturlash uslubida:
 *   3-sinf : bloklar (SPIKE ilovasidagi so'z-bloklar) — manba kontenti
 *   4-sinf : Python matnli kod — SHU QOPLAMA
 *
 * Qoplama faqat ko'rsatilgan darslarni va faqat ko'rsatilgan maydonlarni
 * almashtiradi. Ko'rsatilmagan hamma narsa (qurish darslari, missiya tahlili,
 * ball jadvallari, maydonchalar) manbadan o'zgarishsiz keladi.
 *
 * Kalit: "<chorak>|<indeks>"  (indeks 0 dan boshlanadi)
 *
 * ── API ESLATMASI ────────────────────────────────────────────────────────
 * Kod SPIKE App 3 (2023+) Python API'sida yozilgan. Asosiy modullar:
 *
 *   from hub import port, light_matrix, motion_sensor
 *   import motor, motor_pair, color_sensor, distance_sensor,
 *          force_sensor, runloop, color
 *
 *   motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)   juftlikni e'lon qilish
 *   motor_pair.move(PAIR_1, steering, velocity=...)      to'xtovsiz yurish
 *   await motor_pair.move_for_time(PAIR_1, ms, steering, velocity=...)
 *   motor_pair.stop(PAIR_1)
 *   await motor.run_for_degrees(port.C, gradus, tezlik)  bitta motor
 *   color_sensor.reflection(port.E)      qaytgan yorug'lik 0..100
 *   color_sensor.color(port.E)           rang (color.RED, color.BLUE ...)
 *   distance_sensor.distance(port.F)     millimetr, hech narsa yo'q bo'lsa -1
 *   force_sensor.pressed(port.D)         True / False
 *   motion_sensor.tilt_angles()[0]       yaw, DECIGRADUS (90° = 900)
 *   await runloop.sleep_ms(500)
 *   runloop.run(main())                  dasturni ishga tushirish
 *
 * `await` faqat `async def` ichida ishlaydi — shuning uchun deyarli har bir
 * dastur `async def main():` ichiga yoziladi va oxirida `runloop.run(main())`
 * turadi. Bu 4-sinf uchun O'ZGARMAS SHABLON: bolalar uni yodlab oladi.
 *
 * Portlar butun kurs bo'yicha bir xil (chalkashmaslik uchun):
 *   A, B — yurish motorlari      C — attachment motori
 *   E — rang sensori             F — masofa sensori      D — kuch sensori
 * ─────────────────────────────────────────────────────────────────────────
 */

// Har bir Python darsida takrorlanadigan atamalar — lug'atga qo'shiladi
const SHABLON = "Shablon (Template) – har bir dastur boshlanadigan o'zgarmas qism: " +
                "import, async def main(), runloop.run(main())";

module.exports = {
  nom: "Matnli dasturlash (Python · SPIKE App 3)",

  darslar: {

  /* ══════════════════════ 2-CHORAK — SENSORLAR VA PYTHON ══════════════════════ */

  '2-chorak|0': {
    maqsad: [
      "O'quvchilar rang sensorining qiymatini Python kodi orqali o'qiydilar.",
      "O'quvchilar `print()` yordamida qiymatni konsolda ko'rishni o'rganadilar.",
      "O'quvchilar oq va qora yuzada qiymat qanday o'zgarishini yozib oladilar."
    ],
    lugat: [
      "Kutubxona (Library) – tayyor buyruqlar to'plami, `import` bilan chaqiriladi",
      "Funksiya (Function) – qavs bilan chaqiriladigan buyruq: `color_sensor.reflection()`",
      "Port (Port) – sensor ulangan uya; kodda `port.E` deb yoziladi",
      "Qiymat (Value) – sensor qaytargan son, 0 dan 100 gacha",
      SHABLON
    ],
    nazariya: [
      { title: "5.1. Blokdan matnga (7 daqiqa)", points: [
        "3-sinfda dastur bloklardan yig'ilgan edi; endi xuddi shu narsa matn bilan yoziladi.",
        "Blok — bu aslida yozilgan buyruqning rasmi. Biz endi buyruqni o'zimiz yozamiz.",
        "Afzalligi: kod tez yoziladi, nusxa olinadi, uzun dasturda adashilmaydi."
      ]},
      { title: "5.2. Birinchi shablon (10 daqiqa)", points: [
        "Har bir dastur uchta qismdan iborat: `import` (kutubxonalar), `async def main()` (asosiy qism), `runloop.run(main())` (ishga tushirish).",
        "Sensordan o'qish: `color_sensor.reflection(port.E)` — bu 0 dan 100 gacha son qaytaradi.",
        "Sonni ko'rish uchun `print()` ishlatiladi, natija SPIKE ilovasidagi konsolda chiqadi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Qora yuzada qiymat kichik (0 ga yaqin), oq yuzada katta (100 ga yaqin) bo'ladi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Shablonni terish (10 daqiqa)", points: [
        "O'quvchilar SPIKE ilovasida Python loyihasi ochib, quyidagi kodni o'zlari teradilar (nusxa olmaydilar).",
        "O'qituvchi harf xatolarini ko'rsatadi: katta-kichik harf, qavs, ikki nuqta."
      ]},
      { title: "6.2. Qiymatlarni o'lchash (15 daqiqa)", points: [
        "Sensor oq qog'ozga, keyin qora chiziqqa tutiladi; ekrandagi son daftarga yoziladi.",
        "Guruh bo'yicha jadval to'ldiriladi: oq = ?, qora = ?, o'rtacha (chegara) = ?"
      ]}
    ],
    kod: {
      nom: "Rang sensori qiymatini o'qish",
      izoh: "Eng birinchi Python dasturi. Har yarim soniyada sensor qiymatini chiqaradi.",
      matn: [
        "from hub import port",
        "import color_sensor, runloop",
        "",
        "async def main():",
        "    while True:",
        "        qiymat = color_sensor.reflection(port.E)",
        "        print(qiymat)",
        "        await runloop.sleep_ms(500)",
        "",
        "runloop.run(main())"
      ].join("\n")
    },
    uyga: [
      "Shablonning uch qismini (import / async def main / runloop.run) daftarga yodlab yozing.",
      "Uyda uchta turli rangdagi yuzani sensor bilan o'lchab, qiymatlarini yozib keling."
    ]
  },

  '2-chorak|1': {
    maqsad: [
      "O'quvchilar `if ... else` shartini Python sintaksisida yozadilar.",
      "O'quvchilar rang qiymatiga qarab robotga turli harakat berishni o'rganadilar.",
      "O'quvchilar dasturni turli ranglarda sinaydilar."
    ],
    lugat: [
      "Shart (if) – `if qiymat < 40:` — agar shart bajarilsa, ichidagi qatorlar ishlaydi",
      "Aks holda (else) – shart bajarilmaganda ishlaydigan qism",
      "Taqqoslash (Comparison) – `<` kichik, `>` katta, `==` teng",
      "Ichkariga surish (Indentation) – shart ichidagi qatorlar 4 bo'sh joy bilan suriladi",
      "O'zgaruvchi (Variable) – qiymat saqlanadigan nom: `qiymat = ...`"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "O'tgan darsdagi o'lchangan qiymatlar eslanadi: oq ~80, qora ~15, chegara ~40."
      ]},
      { title: "5.2. if / else sintaksisi (10 daqiqa)", points: [
        "Blokdagi \"agar\" endi shunday yoziladi: `if qiymat < 40:` — oxirida ikki nuqta SHART.",
        "Shartga tegishli qatorlar 4 ta bo'sh joy bilan ichkariga suriladi — Python buni shu bilan tushunadi.",
        "`else:` qismi shart bajarilmaganda ishlaydi. `==` (ikkita teng) tenglikni tekshiradi, `=` esa qiymat beradi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Ichkariga surish xatosi (IndentationError) — eng ko'p uchraydigan xato; uni birga ko'rib chiqiladi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Dastur yozish (15 daqiqa)", points: [
        "O'quvchilar kamida 2 xil rangga turlicha reaksiya beruvchi dastur yozadilar.",
        "Rang bo'yicha ishlash uchun `color` kutubxonasi va `color_sensor.color(port.E)` ishlatiladi."
      ]},
      { title: "6.2. Sinov (10 daqiqa)", points: [
        "Dastur turli rangdagi kartonchalarda sinaladi; ekranda to'g'ri belgi chiqishi tekshiriladi."
      ]}
    ],
    kod: {
      nom: "Rangga qarab qaror qabul qilish",
      izoh: "Qizil ko'rsa to'xtaydi, aks holda oldinga yuradi.",
      matn: [
        "from hub import port, light_matrix",
        "import color, color_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def main():",
        "    while True:",
        "        rang = color_sensor.color(port.E)",
        "        if rang == color.RED:",
        "            motor_pair.stop(motor_pair.PAIR_1)",
        "            light_matrix.write('X')",
        "        else:",
        "            motor_pair.move(motor_pair.PAIR_1, 0, velocity=300)",
        "        await runloop.sleep_ms(50)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|2': {
    maqsad: [
      "O'quvchilar chiziq kuzatish algoritmini Python qatorlari ketma-ketligi sifatida rejalashtiradilar.",
      "O'quvchilar `while True:` takrorlash halqasining ma'nosini tushunadilar.",
      "O'quvchilar rejani qog'ozda kod ko'rinishida yozadilar."
    ],
    lugat: [
      "Halqa (while) – `while True:` — ichidagi qatorlar to'xtovsiz takrorlanadi",
      "Algoritm (Algorithm) – aniq ketma-ketlikdagi qadamlar",
      "Burilish (steering) – `motor_pair.move()` ning ikkinchi soni: -100 chapga, +100 o'ngga",
      "Chegara (Threshold) – oq va qora orasidagi o'rtacha son",
      "Psevdokod (Pseudocode) – kodga o'xshash, lekin oddiy til bilan yozilgan reja"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Chiziq kuzatish g'oyasi eslanadi: sensor chiziqning CHETIDA turadi, robot chapga-o'ngga tebranib yuradi."
      ]},
      { title: "5.2. Algoritmni kodga aylantirish (10 daqiqa)", points: [
        "Reja: takrorla { qiymatni o'qi; agar qora bo'lsa bir tomonga bur; aks holda ikkinchi tomonga bur }.",
        "`while True:` — bu \"to'xtovsiz takrorla\" bloki. Ichidagi hamma narsa 4 bo'sh joy bilan suriladi.",
        "Burilish soni: `motor_pair.move(PAIR_1, -30)` chapga egiladi, `+30` o'ngga egiladi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Keyingi darsda shu reja haqiqiy kodga aylanadi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Rejani yozish (20 daqiqa)", points: [
        "Har bir guruh chiziq kuzatish algoritmini psevdokod ko'rinishida daftarga yozadi.",
        "Chegara soni o'tgan darsdagi o'lchovlardan olinadi va rejaga yoziladi."
      ]},
      { title: "6.2. Rejani tekshirish (5 daqiqa)", points: [
        "Guruhlar rejalarini almashtirib, bir-birining ketma-ketligini tekshiradilar."
      ]}
    ],
    kod: {
      nom: "Reja — psevdokod (hali to'liq dastur emas)",
      izoh: "Bu qog'ozdagi reja. Keyingi darsda haqiqiy kodga aylantiriladi.",
      matn: [
        "# REJA (psevdokod)",
        "# 1. Motorlarni juftlikka bog'la (A va B)",
        "# 2. To'xtovsiz takrorla:",
        "#      qiymat = rang sensoridan o'qi",
        "#      agar qiymat < CHEGARA:      # qora ko'rdi",
        "#          chapga egilib yur",
        "#      aks holda:                  # oq ko'rdi",
        "#          o'ngga egilib yur",
        "",
        "CHEGARA = 40   # o'z o'lchovingizga qarab o'zgartiring"
      ].join("\n")
    }
  },

  '2-chorak|3': {
    maqsad: [
      "O'quvchilar o'tgan darsdagi rejani haqiqiy Python kodiga aylantiradilar.",
      "O'quvchilar `motor_pair` bilan ikkala motorni bitta buyruq orqali boshqaradilar.",
      "O'quvchilar dasturning dastlabki qismini sinaydilar."
    ],
    lugat: [
      "motor_pair – ikkita yurish motorini bitta juftlik sifatida boshqarish",
      "pair() – juftlikni e'lon qilish: `motor_pair.pair(PAIR_1, port.A, port.B)`",
      "move() – to'xtovsiz yurish buyrug'i (steering va velocity bilan)",
      "velocity – tezlik, gradus/soniyada (masalan 300)",
      "Konstanta (Constant) – dastur boshida bir marta yoziladigan o'zgarmas son (CHEGARA)"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "O'tgan darsdagi psevdokod doskaga chiqariladi va qator-baqator kodga o'giriladi."
      ]},
      { title: "5.2. Motorlarni kod bilan boshqarish (10 daqiqa)", points: [
        "Ikkala motor bitta juftlikka bog'lanadi — shunda ular birga boshqariladi: `motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)`.",
        "`motor_pair.move(PAIR_1, steering, velocity=300)` — steering -100 dan +100 gacha; 0 bo'lsa to'g'ri yuradi.",
        "CHEGARA sonini dastur boshida bir marta yozib qo'yish — keyin uni bitta joyda o'zgartirish yetarli."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Bugungi maqsad — dasturning asosiy halqasini ishga tushirish."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "O'quvchilar rejaga asosan chiziq kuzatish dasturining asosiy qismini teradilar.",
        "O'qituvchi ichkariga surish va qavslarni alohida tekshiradi."
      ]},
      { title: "6.2. Qisman sinov (5 daqiqa)", points: [
        "Dastur trassada qisman sinab ko'riladi; robot chiziqni umuman sezayotganini tekshirish yetarli."
      ]}
    ],
    kod: {
      nom: "Chiziq kuzatish — asosiy halqa",
      izoh: "Eng sodda (ikki holatli) chiziq kuzatish. Keyingi darsda yaxshilanadi.",
      matn: [
        "from hub import port",
        "import color_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "CHEGARA = 40",
        "TEZLIK = 300",
        "",
        "async def main():",
        "    while True:",
        "        qiymat = color_sensor.reflection(port.E)",
        "        if qiymat < CHEGARA:",
        "            motor_pair.move(motor_pair.PAIR_1, -35, velocity=TEZLIK)",
        "        else:",
        "            motor_pair.move(motor_pair.PAIR_1, 35, velocity=TEZLIK)",
        "        await runloop.sleep_ms(10)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|4': {
    maqsad: [
      "O'quvchilar chiziq kuzatish dasturini sinab, sonlarni o'zgartirib yaxshilaydilar.",
      "O'quvchilar tezlik va burilish sonlari natijaga qanday ta'sir qilishini tushunadilar.",
      "O'quvchilar dasturni to'liq trassada sinovdan o'tkazadilar."
    ],
    lugat: [
      "Sozlash (Tuning) – sonlarni o'zgartirib eng yaxshi natijani topish",
      "Tebranish (Oscillation) – robotning chapga-o'ngga haddan tashqari chayqalishi",
      "Xatolarni tuzatish (Debugging) – dasturdagi kamchilikni topib to'g'rilash",
      "print() – qiymatni konsolga chiqarib, nima bo'layotganini ko'rish",
      "Sinov qaydnomasi (Test log) – har sinovda o'zgartirilgan son va natija yozuvi"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "O'tgan darsdagi dastur ishga tushiriladi va kuzatiladi: robot chiziqdan chiqib ketyaptimi yoki qattiq tebranyaptimi?"
      ]},
      { title: "5.2. Qaysi sonni o'zgartirish kerak (10 daqiqa)", points: [
        "Robot chiziqdan chiqib ketsa — burilish soni (35) kichik; uni oshirish kerak.",
        "Robot qattiq chayqalsa — burilish soni katta yoki TEZLIK yuqori; birini kamaytirish kerak.",
        "HAR SAFAR FAQAT BITTA sonni o'zgartirish kerak — aks holda qaysi biri ta'sir qilganini bilib bo'lmaydi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Har bir sinov natijasi daftarga yoziladi: qaysi son, qanday qiymat, qanday natija."
      ]}
    ],
    amaliy: [
      { title: "6.1. Sozlash sinovlari (20 daqiqa)", points: [
        "Guruhlar kamida 4 marta sinaydi, har safar bitta sonni o'zgartirib, natijani yozadilar.",
        "Eng yaxshi natija bergan sonlar dasturda qoldiriladi."
      ]},
      { title: "6.2. To'liq trassa sinovi (5 daqiqa)", points: [
        "Robot butun trassani boshdan oxir bosib o'tishga uriniladi; vaqti o'lchanadi."
      ]}
    ],
    kod: {
      nom: "Chiziq kuzatish + sinov uchun print()",
      izoh: "print() qatori qiymatni konsolda ko'rsatadi — sozlashda juda yordam beradi. Musobaqada uni o'chirib qo'yiladi (sekinlashtiradi).",
      matn: [
        "from hub import port",
        "import color_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "CHEGARA = 40      # <- 1-sinovda shuni o'zgartiring",
        "BURILISH = 35     # <- 2-sinovda shuni",
        "TEZLIK = 300      # <- 3-sinovda shuni",
        "",
        "async def main():",
        "    while True:",
        "        qiymat = color_sensor.reflection(port.E)",
        "        print(qiymat)          # sozlash tugagach shu qatorni o'chiring",
        "        if qiymat < CHEGARA:",
        "            motor_pair.move(motor_pair.PAIR_1, -BURILISH, velocity=TEZLIK)",
        "        else:",
        "            motor_pair.move(motor_pair.PAIR_1, BURILISH, velocity=TEZLIK)",
        "        await runloop.sleep_ms(10)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|5': {
    maqsad: [
      "O'quvchilar masofa sensorini Python orqali o'qiydilar.",
      "O'quvchilar millimetrdagi masofani shartda ishlatishni o'rganadilar.",
      "O'quvchilar to'siqqa yaqinlashganda to'xtaydigan dastur yozadilar."
    ],
    lugat: [
      "distance_sensor – masofa (ultratovush) sensori kutubxonasi",
      "distance() – masofani MILLIMETRDA qaytaradi (200 mm = 20 sm)",
      "-1 qiymati – oldinda hech narsa yo'q degani, buni alohida tekshirish kerak",
      "and / or – ikkita shartni birlashtirish: `if a > 0 and a < 200:`",
      "break – halqadan chiqib ketish buyrug'i"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Ultratovush sensori tovush to'lqini yuborib, qaytishini kutadi — shundan masofa hisoblanadi."
      ]},
      { title: "5.2. Masofani kodda ishlatish (10 daqiqa)", points: [
        "`distance_sensor.distance(port.F)` millimetr qaytaradi: 200 = 20 santimetr.",
        "MUHIM: oldinda hech narsa bo'lmasa sensor **-1** qaytaradi. -1 har qanday sondan kichik, shuning uchun uni alohida tekshirmasa robot yo'q joyda to'xtaydi.",
        "To'g'ri shart: `if masofa > 0 and masofa < 200:` — ya'ni \"o'lchov bor VA 20 sm dan yaqin\"."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Bu -1 tuzog'i musobaqada eng ko'p uchraydigan xatolardan biri."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "O'quvchilar to'siqqa 20 sm qolganda to'xtaydigan dastur yozadilar.",
        "Sensor ko'rsatgan sonni `print()` bilan tekshirib, haqiqiy masofa bilan solishtiradilar."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Robot devorga yurgiziladi; qaysi masofada to'xtagani chizg'ich bilan o'lchanadi."
      ]}
    ],
    kod: {
      nom: "To'siqni sezib to'xtash",
      izoh: "-1 tekshiruviga e'tibor bering — usiz robot bo'sh joyda ham to'xtaydi.",
      matn: [
        "from hub import port",
        "import distance_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "TOXTASH_MM = 200   # 20 santimetr",
        "",
        "async def main():",
        "    motor_pair.move(motor_pair.PAIR_1, 0, velocity=300)",
        "    while True:",
        "        masofa = distance_sensor.distance(port.F)",
        "        if masofa > 0 and masofa < TOXTASH_MM:",
        "            motor_pair.stop(motor_pair.PAIR_1)",
        "            break",
        "        await runloop.sleep_ms(10)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|6': {
    maqsad: [
      "O'quvchilar to'siqni sezib to'xtash dasturini orqaga qaytish bilan to'ldiradilar.",
      "O'quvchilar `move_for_time` bilan aniq vaqtga harakat berishni o'rganadilar.",
      "O'quvchilar `await` nima uchun kerakligini tushunadilar."
    ],
    lugat: [
      "await – \"kutib tur\": buyruq tugagunicha keyingi qatorga o'tilmaydi",
      "move_for_time() – berilgan MILLISEKUND davomida yurish",
      "Manfiy tezlik – orqaga yurish (velocity=-300)",
      "Ketma-ketlik (Sequence) – buyruqlar yuqoridan pastga birin-ketin bajariladi",
      "async def – ichida `await` ishlatiladigan funksiya"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "O'tgan darsdagi to'xtash dasturi eslanadi; endi robot to'xtabgina qolmay, orqaga qaytishi kerak."
      ]},
      { title: "5.2. await va vaqtli harakat (10 daqiqa)", points: [
        "`motor_pair.move()` buyruq berib darrov keyingi qatorga o'tadi; `move_for_time()` esa belgilangan vaqt yuradi.",
        "`await` — \"tugagunicha kut\" degani. `await motor_pair.move_for_time(PAIR_1, 1000, 0, velocity=-300)` bir soniya orqaga yuradi.",
        "`await` yozilmasa robot buyruqni boshlaydi-yu, darrov keyingisiga o'tib ketadi — harakat yarim qoladi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "`await` faqat `async def` ichida ishlaydi — shuning uchun shablonda `async` so'zi turadi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "O'quvchilar bumper to'siqqa tegib to'xtagach, 1 soniya orqaga yurib, 90 daraja buriladigan dastur yozadilar.",
        "Har bir `await` qatori ustida to'xtalib, nima uchun kerakligi aytiladi."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Robot to'siqqa yurgiziladi; orqaga qaytish va burilish ketma-ketligi kuzatiladi."
      ]}
    ],
    kod: {
      nom: "To'siqni sezib — to'xta, orqaga qayt, burl",
      izoh: "Uchta harakat ketma-ket. Har birida `await` bor, shuning uchun ular birin-ketin bajariladi.",
      matn: [
        "from hub import port",
        "import distance_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def main():",
        "    motor_pair.move(motor_pair.PAIR_1, 0, velocity=300)",
        "    while True:",
        "        masofa = distance_sensor.distance(port.F)",
        "        if masofa > 0 and masofa < 150:",
        "            motor_pair.stop(motor_pair.PAIR_1)",
        "            await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0, velocity=-300)",
        "            await motor_pair.move_for_time(motor_pair.PAIR_1, 700, 100, velocity=300)",
        "            motor_pair.move(motor_pair.PAIR_1, 0, velocity=300)",
        "        await runloop.sleep_ms(10)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|7': {
    maqsad: [
      "O'quvchilar attachment motorini alohida boshqarishni o'rganadilar.",
      "O'quvchilar `motor.run_for_degrees()` bilan aniq burchakka aylantiradilar.",
      "O'quvchilar ushlab olish va qo'yib yuborish ketma-ketligini yozadilar."
    ],
    lugat: [
      "motor – bitta motorni boshqarish kutubxonasi (motor_pair emas)",
      "run_for_degrees() – motorni aniq gradusga aylantirish",
      "Gradus (Degrees) – 360 = bir to'liq aylanish",
      "Manfiy gradus – teskari tomonga aylantirish",
      "Funksiya yaratish (def) – takrorlanadigan qadamlarga nom berish"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Gripper (qisqich) attachmenti C portidagi alohida motor bilan ochilib-yopiladi."
      ]},
      { title: "5.2. Bitta motorni boshqarish (10 daqiqa)", points: [
        "Yurish motorlari juftlikda, attachment motori esa ALOHIDA: `motor.run_for_degrees(port.C, 180, 500)`.",
        "Uch son: qaysi port, necha gradus, qanday tezlik. Manfiy gradus teskari tomonga aylantiradi.",
        "Takrorlanadigan qadamlarga nom berish mumkin: `async def ushla():` — keyin `await ushla()` deb chaqiriladi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Gradusni sinov bilan topish kerak: 90 kam bo'lsa qisqich yopilmaydi, 270 ko'p bo'lsa motor tiqiladi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "O'quvchilar `ushla()` va `qoyib_yubor()` funksiyalarini yozib, ularni ketma-ket chaqiradilar.",
        "Kerakli gradus sinov yo'li bilan topiladi va daftarga yoziladi."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Robot buyumni ushlab, 30 sm yurib, qo'yib yuboradi."
      ]}
    ],
    kod: {
      nom: "Gripper — ushlash va qo'yib yuborish",
      izoh: "`def` bilan qadamlarga nom berilgan — kod ancha o'qishli bo'ladi.",
      matn: [
        "from hub import port",
        "import motor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "GRADUS = 180   # sinov bilan toping",
        "",
        "async def ushla():",
        "    await motor.run_for_degrees(port.C, GRADUS, 500)",
        "",
        "async def qoyib_yubor():",
        "    await motor.run_for_degrees(port.C, -GRADUS, 500)",
        "",
        "async def main():",
        "    await ushla()",
        "    await motor_pair.move_for_time(motor_pair.PAIR_1, 1500, 0, velocity=300)",
        "    await qoyib_yubor()",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|8': {
    maqsad: [
      "O'quvchilar kuch (bosim) sensorini Python orqali o'qiydilar.",
      "O'quvchilar `pressed()` mantiqiy qiymatini shartda ishlatadilar.",
      "O'quvchilar sensorni dasturni ishga tushirish tugmasi sifatida qo'llaydilar."
    ],
    lugat: [
      "force_sensor – kuch (bosim) sensori kutubxonasi",
      "pressed() – bosilganmi? `True` yoki `False` qaytaradi",
      "Mantiqiy qiymat (Boolean) – faqat True yoki False bo'ladigan qiymat",
      "force() – bosim kuchi, 0 dan 100 gacha son",
      "not – teskarisi: `if not force_sensor.pressed(port.D):`"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Kuch sensori ikki xil ma'lumot beradi: bosilganmi (ha/yo'q) va qanchalik qattiq bosilgan (son)."
      ]},
      { title: "5.2. True / False bilan ishlash (10 daqiqa)", points: [
        "`force_sensor.pressed(port.D)` faqat True yoki False qaytaradi — bunday qiymat mantiqiy deyiladi.",
        "Mantiqiy qiymatni taqqoslash shart emas: `if force_sensor.pressed(port.D):` yozish yetarli.",
        "Kutish uchun: `while not force_sensor.pressed(port.D): await runloop.sleep_ms(10)` — bosilmaguncha kutadi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Musobaqada dastur tugmani bosgandan keyin boshlanishi kerak — bu shuning uchun kerak."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "O'quvchilar sensor bosilishini kutib turadigan, so'ng yurishni boshlaydigan dastur yozadilar.",
        "`force()` qiymati `print()` bilan chiqarilib, qattiq va yumshoq bosish farqi kuzatiladi."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Robot faqat tugma bosilganda ishga tushishi tekshiriladi."
      ]}
    ],
    kod: {
      nom: "Kuch sensori — start tugmasi",
      izoh: "Musobaqada juda foydali: robot tayyor turadi, tugma bosilganda yo'lga chiqadi.",
      matn: [
        "from hub import port, light_matrix",
        "import force_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def main():",
        "    light_matrix.write('?')",
        "    while not force_sensor.pressed(port.D):",
        "        await runloop.sleep_ms(10)",
        "",
        "    light_matrix.write('GO')",
        "    await motor_pair.move_for_time(motor_pair.PAIR_1, 2000, 0, velocity=400)",
        "    motor_pair.stop(motor_pair.PAIR_1)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|9': {
    maqsad: [
      "O'quvchilar gyroskopik sensor yordamida aniq burchakka buriladilar.",
      "O'quvchilar decigradus (90° = 900) o'lchovini tushunadilar.",
      "O'quvchilar burilish aniqligini vaqt bo'yicha burilish bilan solishtiradilar."
    ],
    lugat: [
      "motion_sensor – hubning ichidagi gyroskop",
      "yaw – gorizontal burilish burchagi",
      "Decigradus – gyroskop o'lchovi: 90 daraja = 900",
      "reset_yaw() – burchakni nolga qaytarish",
      "abs() – sonning musbat qiymati (ishorasiz)"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Vaqt bo'yicha burilish (`move_for_time`) har safar boshqacha chiqadi — batareya, gilam, og'irlik ta'sir qiladi."
      ]},
      { title: "5.2. Gyroskop bilan aniq burilish (10 daqiqa)", points: [
        "`motion_sensor.reset_yaw(0)` — hozirgi yo'nalishni nol deb belgilaydi.",
        "`motion_sensor.tilt_angles()[0]` — burchakni DECIGRADUSDA qaytaradi: 90 daraja = **900**.",
        "Usul: robotni burishni boshlab, burchak kerakli songa yetguncha halqada kutib turiladi, so'ng to'xtatiladi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Gyroskop bilan burilish missiyalarda vaqt bo'yicha burilishdan ancha ishonchli."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "O'quvchilar 90 daraja aniq buriladigan dastur yozadilar.",
        "Burilish 5 marta takrorlanib, har safar chetlanish daftarga yoziladi."
      ]},
      { title: "6.2. Solishtirish (5 daqiqa)", points: [
        "Vaqt bo'yicha burilish va gyroskop bo'yicha burilish aniqligi taqqoslanadi."
      ]}
    ],
    kod: {
      nom: "Gyroskop bilan 90 daraja burilish",
      izoh: "900 = 90 daraja (decigradus). abs() ishorani hisobga olmaydi — ikki tomonga ham ishlaydi.",
      matn: [
        "from hub import port, motion_sensor",
        "import motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def bur(burchak_gradus):",
        "    motion_sensor.reset_yaw(0)",
        "    nishon = burchak_gradus * 10        # 90 -> 900 decigradus",
        "    motor_pair.move(motor_pair.PAIR_1, 100, velocity=200)",
        "    while abs(motion_sensor.tilt_angles()[0]) < nishon:",
        "        await runloop.sleep_ms(5)",
        "    motor_pair.stop(motor_pair.PAIR_1)",
        "",
        "async def main():",
        "    await bur(90)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|10': {
    maqsad: [
      "O'quvchilar bir nechta sensordan kelgan ma'lumotni bitta dasturda birlashtiradilar.",
      "O'quvchilar `and` va `or` mantiqiy amallarini qo'llaydilar.",
      "O'quvchilar sensorlar ustuvorligini rejalashtiradilar."
    ],
    lugat: [
      "and – ikkala shart ham bajarilishi kerak",
      "or – kamida bittasi bajarilsa yetarli",
      "elif – \"aks holda agar\", uchinchi va undan keyingi holatlar uchun",
      "Ustuvorlik (Priority) – qaysi shart avval tekshiriladi",
      "Ichma-ich shart (Nested if) – shart ichidagi shart"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Haqiqiy robot bir vaqtda ham chiziqni kuzatadi, ham to'siqni sezadi."
      ]},
      { title: "5.2. Shartlarni birlashtirish (10 daqiqa)", points: [
        "`if a and b:` — ikkalasi ham to'g'ri bo'lsa ishlaydi. `if a or b:` — bittasi yetarli.",
        "Uchdan ortiq holat bo'lsa `elif` ishlatiladi: `if ... elif ... else`.",
        "TARTIB MUHIM: eng xavfli holat (to'siq) birinchi tekshiriladi, chiziq kuzatish keyin."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Shartlar tartibi noto'g'ri bo'lsa robot to'siqqa urilib qoladi — bu tez-tez uchraydigan xato."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "O'quvchilar chiziqni kuzatadigan, lekin to'siq ko'rsa to'xtaydigan dastur yozadilar.",
        "Shartlar tartibi almashtirilib, natija farqi kuzatiladi."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Trassaga to'siq qo'yiladi; robot chiziqda yurib, to'siq oldida to'xtashi tekshiriladi."
      ]}
    ],
    kod: {
      nom: "Chiziq kuzatish + to'siqni sezish",
      izoh: "Diqqat: to'siq sharti BIRINCHI tekshiriladi. Agar tartibni almashtirsangiz robot to'siqqa uriladi.",
      matn: [
        "from hub import port",
        "import color_sensor, distance_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "CHEGARA = 40",
        "",
        "async def main():",
        "    while True:",
        "        masofa = distance_sensor.distance(port.F)",
        "        qiymat = color_sensor.reflection(port.E)",
        "",
        "        if masofa > 0 and masofa < 150:      # 1-ustuvorlik: to'siq",
        "            motor_pair.stop(motor_pair.PAIR_1)",
        "        elif qiymat < CHEGARA:               # 2-ustuvorlik: qora",
        "            motor_pair.move(motor_pair.PAIR_1, -35, velocity=300)",
        "        else:                                # 3: oq",
        "            motor_pair.move(motor_pair.PAIR_1, 35, velocity=300)",
        "",
        "        await runloop.sleep_ms(10)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|11': {
    maqsad: [
      "O'quvchilar ko'p tarmoqli qaror qabul qilish dasturini yozadilar.",
      "O'quvchilar `elif` zanjirini to'g'ri tartibda tuzadilar.",
      "O'quvchilar qaror daraxtini avval qog'ozda chizadilar."
    ],
    lugat: [
      "Qaror daraxti (Decision tree) – shartlarning tarmoqlangan chizmasi",
      "elif zanjiri – bir nechta holatni ketma-ket tekshirish",
      "Standart holat (else) – hech qaysi shart bajarilmaganda",
      "Rang doimiylari (color.RED, color.BLUE) – `color` kutubxonasidagi nomlar",
      "Ustuvorlik – shartlarning tekshirilish tartibi"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Saralash robotida rangga qarab uch xil harakat qilish kerak — bitta if yetmaydi."
      ]},
      { title: "5.2. if / elif / else zanjiri (10 daqiqa)", points: [
        "Zanjir yuqoridan pastga tekshiriladi va BIRINCHI to'g'ri kelgan tarmoq bajariladi, qolganlari o'tkazib yuboriladi.",
        "Shuning uchun eng aniq shart tepada, eng umumiysi (`else`) pastda turadi.",
        "Rangni tekshirish: `if rang == color.RED:` — `color` kutubxonasini import qilish esdan chiqmasin."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Kod yozishdan oldin qaror daraxtini qog'ozda chizish xatoni ancha kamaytiradi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Qaror daraxti va kod (20 daqiqa)", points: [
        "O'quvchilar avval qog'ozda qaror daraxtini chizadilar, so'ng uni elif zanjiriga o'giradilar.",
        "Har bir tarmoq uchun alohida harakat yoziladi."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Uch xil rangli buyum ko'rsatilib, har birida to'g'ri tarmoq ishlashi tekshiriladi."
      ]}
    ],
    kod: {
      nom: "Rang bo'yicha saralash — elif zanjiri",
      izoh: "Zanjir yuqoridan pastga tekshiriladi; birinchi mos kelgani ishlaydi.",
      matn: [
        "from hub import port, light_matrix",
        "import color, color_sensor, motor, runloop",
        "",
        "async def main():",
        "    while True:",
        "        rang = color_sensor.color(port.E)",
        "",
        "        if rang == color.RED:",
        "            light_matrix.write('R')",
        "            await motor.run_for_degrees(port.C, 90, 400)",
        "        elif rang == color.BLUE:",
        "            light_matrix.write('B')",
        "            await motor.run_for_degrees(port.C, -90, 400)",
        "        elif rang == color.YELLOW:",
        "            light_matrix.write('Y')",
        "        else:",
        "            light_matrix.write('-')",
        "",
        "        await runloop.sleep_ms(200)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|12': {
    maqsad: [
      "O'quvchilar o'rgangan Python buyruqlarini mustaqil masalada qo'llaydilar.",
      "O'quvchilar dasturni bo'laklarga bo'lib yozishni mashq qiladilar.",
      "O'quvchilar bir-birining kodini o'qib, xatosini topadilar."
    ],
    lugat: [
      "Masala sharti (Task) – nima qilinishi kerakligi aniq yozilgan matn",
      "Bo'laklash (Decomposition) – katta masalani kichik qadamlarga bo'lish",
      "Kodni o'qish (Code reading) – birovning kodini tushunish",
      "Sintaksis xatosi (SyntaxError) – yozuv qoidasi buzilgani",
      "Mantiq xatosi (Logic error) – kod ishlaydi, lekin noto'g'ri natija beradi"
    ],
    nazariya: [
      { title: "5.1. Masalalar sharti (7 daqiqa)", points: [
        "Uchta masala beriladi: (1) 3 marta kvadrat chizib yurish, (2) chiziqni topib to'xtash, (3) buyumni ushlab olib kelish."
      ]},
      { title: "5.2. Bo'laklash usuli (10 daqiqa)", points: [
        "Har bir masala avval 3-5 ta qadamga bo'linadi va qog'ozga yoziladi.",
        "Har qadam uchun qaysi buyruq kerakligi belgilanadi (move_for_time, run_for_degrees, if ...).",
        "Faqat shundan keyin kod teriladi — bu vaqtni tejaydi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Ikki xil xato farqi: SyntaxError'ni ilova o'zi ko'rsatadi, mantiq xatosini faqat sinov ko'rsatadi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Mustaqil ishlash (20 daqiqa)", points: [
        "Guruhlar tanlagan masalasini bo'laklab, kodini yozadilar va sinaydilar."
      ]},
      { title: "6.2. Kod almashish (5 daqiqa)", points: [
        "Guruhlar kodini almashtirib, bir-birining dasturidagi kamchilikni topadilar."
      ]}
    ],
    kod: {
      nom: "1-masala yechimi: kvadrat bo'ylab yurish",
      izoh: "for halqasi bir xil qadamni takrorlaydi — to'rt marta yozib o'tirmaydi.",
      matn: [
        "from hub import port, motion_sensor",
        "import motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def bur(gradus):",
        "    motion_sensor.reset_yaw(0)",
        "    motor_pair.move(motor_pair.PAIR_1, 100, velocity=200)",
        "    while abs(motion_sensor.tilt_angles()[0]) < gradus * 10:",
        "        await runloop.sleep_ms(5)",
        "    motor_pair.stop(motor_pair.PAIR_1)",
        "",
        "async def main():",
        "    for i in range(4):",
        "        await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0, velocity=350)",
        "        await bur(90)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|13': {
    maqsad: [
      "O'quvchilar `for` halqasi bilan takrorlanuvchi harakatni qisqartiradilar.",
      "O'quvchilar o'z kodini qisqartirish va tozalashni o'rganadilar.",
      "O'quvchilar funksiyalarga bo'lingan dastur tuzadilar."
    ],
    lugat: [
      "for halqasi – ma'lum sondagi takrorlash: `for i in range(4):`",
      "range() – sonlar ketma-ketligini hosil qiladi",
      "Takrorlanuvchi kod (Duplication) – bir xil qatorlarning qayta-qayta yozilishi",
      "Funksiya (def) – qadamlar to'plamiga berilgan nom",
      "Tozalash (Refactoring) – ishlayotgan kodni o'zgartirmasdan chiroyliroq qilish"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "O'tgan darsda ba'zi guruhlar bir xil qatorlarni 4 marta yozgan edi — buni qisqartirish mumkin."
      ]},
      { title: "5.2. for va def (10 daqiqa)", points: [
        "`for i in range(4):` — ichidagi qatorlar aynan 4 marta bajariladi.",
        "`while True:` cheksiz takrorlaydi, `for` esa sanab takrorlaydi — farqni ajratish kerak.",
        "Takrorlanuvchi qadamlar to'plamiga `async def` bilan nom berilsa, kod qisqaradi va tuzatish osonlashadi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Yaxshi kod — qisqa emas, O'QILADIGAN kod. Nomlar ma'noli bo'lishi kerak."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kodni qisqartirish (20 daqiqa)", points: [
        "O'quvchilar o'tgan darsdagi kodini `for` va `def` yordamida qayta yozadilar.",
        "Qator soni oldin va keyin sanab, daftarga yoziladi."
      ]},
      { title: "6.2. Tekshirish (5 daqiqa)", points: [
        "Qisqartirilgan dastur avvalgidek ishlashi sinab ko'riladi."
      ]}
    ],
    kod: {
      nom: "Takrorlanuvchi kodni for bilan qisqartirish",
      izoh: "Yuqoridagi va pastdagi kod bir xil ishlaydi, lekin ikkinchisi ancha qisqa.",
      matn: [
        "# ESKI USUL — bir xil qatorlar 3 marta",
        "# await motor.run_for_degrees(port.C, 90, 400)",
        "# await runloop.sleep_ms(300)",
        "# await motor.run_for_degrees(port.C, 90, 400)",
        "# await runloop.sleep_ms(300)",
        "# await motor.run_for_degrees(port.C, 90, 400)",
        "",
        "# YANGI USUL",
        "from hub import port",
        "import motor, runloop",
        "",
        "async def main():",
        "    for i in range(3):",
        "        await motor.run_for_degrees(port.C, 90, 400)",
        "        await runloop.sleep_ms(300)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|15': {
    maqsad: [
      "O'quvchilar parking robot loyihasini Python kodida amalga oshiradilar.",
      "O'quvchilar bir nechta sensorni bitta dasturda birlashtiradilar.",
      "O'quvchilar dasturni bosqichma-bosqich sinab, tuzatadilar."
    ],
    lugat: [
      "Loyiha kodi (Project code) – bir nechta qismdan yig'ilgan to'liq dastur",
      "Holat (State) – robot hozir qaysi bosqichda ekani",
      "Bosqichma-bosqich sinov – har bir qismni alohida tekshirish",
      "Konstanta – dastur boshidagi sozlanadigan sonlar",
      "Izoh (#) – kodda tushuntirish uchun yoziladigan, bajarilmaydigan qator"
    ],
    nazariya: [
      { title: "5.1. Loyiha talabi (7 daqiqa)", points: [
        "Robot bo'sh joyni topib, unga kirib, to'g'ri to'xtashi kerak."
      ]},
      { title: "5.2. Dasturni bosqichlarga bo'lish (10 daqiqa)", points: [
        "Bosqichlar: (1) devor bo'ylab yurish, (2) bo'sh joyni sezish, (3) burilib kirish, (4) to'xtash.",
        "Har bosqich alohida funksiya qilib yoziladi — shunda birini tuzatganda boshqasi buzilmaydi.",
        "Sozlanadigan sonlar (masofa, vaqt, tezlik) dastur boshiga chiqariladi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Har bosqich alohida sinaladi, keyin birlashtiriladi — hammasini birdan yozib sinash eng ko'p vaqt yo'qotadi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Loyihani dasturlash (20 daqiqa)", points: [
        "Guruhlar loyiha kodini bosqichma-bosqich yozadilar va har bosqichni alohida sinaydilar."
      ]},
      { title: "6.2. To'liq sinov (5 daqiqa)", points: [
        "Butun ketma-ketlik boshdan oxir sinab ko'riladi."
      ]}
    ],
    kod: {
      nom: "Aqlli parking robot — to'liq dastur",
      izoh: "Har bosqich alohida funksiya. Sozlanadigan sonlar tepada.",
      matn: [
        "from hub import port, light_matrix",
        "import distance_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "BOSH_JOY_MM = 300     # shundan uzoq bo'lsa - joy bo'sh",
        "TEZLIK = 250",
        "",
        "async def devor_boylab_yur():",
        "    motor_pair.move(motor_pair.PAIR_1, 0, velocity=TEZLIK)",
        "    while True:",
        "        m = distance_sensor.distance(port.F)",
        "        if m < 0 or m > BOSH_JOY_MM:      # joy bo'sh",
        "            motor_pair.stop(motor_pair.PAIR_1)",
        "            return",
        "        await runloop.sleep_ms(10)",
        "",
        "async def joyga_kir():",
        "    await motor_pair.move_for_time(motor_pair.PAIR_1, 600, 100, velocity=200)",
        "    await motor_pair.move_for_time(motor_pair.PAIR_1, 900, 0, velocity=200)",
        "",
        "async def main():",
        "    await devor_boylab_yur()",
        "    await joyga_kir()",
        "    light_matrix.write('P')",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '2-chorak|16': {
    maqsad: [
      "O'quvchilar chorak davomida o'rgangan Python buyruqlarini tizimlashtiradilar.",
      "O'quvchilar o'zlarining shpargalka (qo'llanma) varag'ini tuzadilar.",
      "O'quvchilar tipik xatolarni va ularning yechimini eslab qoladilar."
    ],
    lugat: [
      "Sintaksis (Syntax) – yozuv qoidasi: qavs, ikki nuqta, ichkariga surish",
      "IndentationError – ichkariga surish xatosi",
      "NameError – yozilmagan yoki xato yozilgan nom",
      "Shpargalka (Cheat sheet) – asosiy buyruqlar yozilgan bitta varaq",
      "Kutubxona importi – dastur boshidagi `import` qatorlari"
    ],
    nazariya: [
      { title: "5.1. Chorak xulosasi (7 daqiqa)", points: [
        "O'rganilgan sensorlar: rang, masofa, kuch, gyroskop. Har biri uchun bitta buyruq eslanadi."
      ]},
      { title: "5.2. Tipik xatolar (10 daqiqa)", points: [
        "IndentationError — shart ichidagi qator surilmagan yoki bo'sh joy soni har xil.",
        "NameError — kutubxona import qilinmagan yoki nom xato yozilgan (`Port` emas, `port`).",
        "Robot qimirlamaydi — `await` yozilmagan yoki `runloop.run(main())` qatori tushib qolgan."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Shpargalka keyingi chorakda missiya dasturlashda ishlatiladi — saqlab qo'yish kerak."
      ]}
    ],
    amaliy: [
      { title: "6.1. Shpargalka tuzish (20 daqiqa)", points: [
        "Har bir o'quvchi bitta A4 varaqqa asosiy buyruqlarni namuna bilan ko'chirib yozadi.",
        "Varaqda kamida: shablon, sensorlarni o'qish, motor buyruqlari, if/elif/else, for/while bo'lishi kerak."
      ]},
      { title: "6.2. Xatoni top (5 daqiqa)", points: [
        "O'qituvchi ataylab xato yozilgan 3 ta kod ko'rsatadi, o'quvchilar xatoni topadilar."
      ]}
    ],
    kod: {
      nom: "Shpargalka — chorakda o'rganilgan hamma narsa",
      izoh: "Bitta varaqqa ko'chiriladigan asosiy buyruqlar.",
      matn: [
        "# ── SHABLON ──────────────────────────────",
        "from hub import port, light_matrix, motion_sensor",
        "import motor, motor_pair, color_sensor, distance_sensor",
        "import force_sensor, color, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def main():",
        "    pass          # kod shu yerga yoziladi",
        "",
        "runloop.run(main())",
        "",
        "# ── SENSORLAR ────────────────────────────",
        "# color_sensor.reflection(port.E)     0..100",
        "# color_sensor.color(port.E)          color.RED, color.BLUE ...",
        "# distance_sensor.distance(port.F)    mm, yo'q bo'lsa -1",
        "# force_sensor.pressed(port.D)        True / False",
        "# motion_sensor.tilt_angles()[0]      yaw, 90 grad = 900",
        "",
        "# ── HARAKAT ──────────────────────────────",
        "# motor_pair.move(PAIR_1, steering, velocity=300)",
        "# await motor_pair.move_for_time(PAIR_1, 1000, 0, velocity=300)",
        "# motor_pair.stop(PAIR_1)",
        "# await motor.run_for_degrees(port.C, 180, 500)",
        "# await runloop.sleep_ms(500)"
      ].join("\n")
    }
  },

  '2-chorak|17': {
    maqsad: [
      "O'quvchilar hubning tugmalarini dasturda ishlatadilar.",
      "O'quvchilar bir dasturda bir nechta rejimni tanlashni o'rganadilar.",
      "O'quvchilar menyuli dastur tuzadilar."
    ],
    lugat: [
      "button – hubning tugmalari kutubxonasi",
      "Rejim (Mode) – dasturning tanlanadigan variantlari",
      "Menyu (Menu) – rejimni tanlash ekrani",
      "Global o'zgaruvchi – butun dastur davomida saqlanadigan qiymat",
      "light_matrix.write() – hub ekraniga harf/son chiqarish"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Musobaqada bitta robotga bir nechta dastur kerak bo'ladi — hammasini alohida yuklash vaqt oladi."
      ]},
      { title: "5.2. Menyu tuzish (10 daqiqa)", points: [
        "Hub tugmalari: `button.pressed(button.LEFT)` va `button.pressed(button.RIGHT)` — bosilgan bo'lsa True qaytaradi.",
        "Chap tugma raqamni kamaytiradi, o'ng tugma oshiradi; tanlangan raqam ekranda ko'rinadi.",
        "Tanlangan raqamga qarab kerakli funksiya chaqiriladi — bu `if/elif` zanjiri bilan qilinadi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Bu usul 3-4-chorakda barcha missiyalarni bitta dasturga yig'ishda ishlatiladi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Menyu kodini yozish (20 daqiqa)", points: [
        "O'quvchilar 3 ta rejimli menyu yozadilar; har rejim boshqacha harakat qiladi.",
        "Tanlangan rejim raqami ekranda ko'rinishi ta'minlanadi."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Har uch rejim tugma orqali tanlanib, ishlashi tekshiriladi."
      ]}
    ],
    kod: {
      nom: "Tugmali menyu — bitta dasturda 3 rejim",
      izoh: "Chap/o'ng tugma bilan raqam tanlanadi, kuch sensori bosilganda tanlangan rejim ishga tushadi.",
      matn: [
        "from hub import port, button, light_matrix",
        "import force_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def rejim_1():",
        "    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0, velocity=300)",
        "",
        "async def rejim_2():",
        "    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 100, velocity=300)",
        "",
        "async def rejim_3():",
        "    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0, velocity=-300)",
        "",
        "async def main():",
        "    tanlov = 1",
        "    light_matrix.write(str(tanlov))",
        "",
        "    while not force_sensor.pressed(port.D):",
        "        if button.pressed(button.LEFT) and tanlov > 1:",
        "            tanlov = tanlov - 1",
        "            light_matrix.write(str(tanlov))",
        "            await runloop.sleep_ms(300)",
        "        if button.pressed(button.RIGHT) and tanlov < 3:",
        "            tanlov = tanlov + 1",
        "            light_matrix.write(str(tanlov))",
        "            await runloop.sleep_ms(300)",
        "        await runloop.sleep_ms(10)",
        "",
        "    if tanlov == 1:",
        "        await rejim_1()",
        "    elif tanlov == 2:",
        "        await rejim_2()",
        "    else:",
        "        await rejim_3()",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  /* ══════════════════ 3-CHORAK — MISSIYA DASTURLASH ══════════════════ */

  '3-chorak|5': {
    maqsad: [
      "O'quvchilar 1-missiya harakatini Python funksiyalari ketma-ketligi sifatida yozadilar.",
      "O'quvchilar masofani vaqt emas, gradus bilan o'lchashni qo'llaydilar.",
      "O'quvchilar missiya kodini alohida funksiyaga joylashtiradilar."
    ],
    lugat: [
      "move_for_degrees() – g'ildirak aylanishi bo'yicha aniq masofa",
      "Missiya funksiyasi – bitta missiyaning butun kodi solingan `async def`",
      "Takrorlanuvchanlik (Repeatability) – har safar bir xil natija berishi",
      "Kalibrlash (Calibration) – bir gradus necha santimetrga to'g'ri kelishini o'lchash",
      "Bazaga qaytish (Return to base) – missiya oxirida start joyiga qaytish"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "O'tgan darslardagi reja va attachment tayyor; endi harakat kodga aylantiriladi."
      ]},
      { title: "5.2. Vaqt emas, gradus (10 daqiqa)", points: [
        "`move_for_time` batareya quvvatiga qarab har safar boshqa masofa beradi — musobaqada ishonchsiz.",
        "`await motor_pair.move_for_degrees(PAIR_1, 720, 0, velocity=400)` — g'ildirak aylanishi bo'yicha yuradi, bu ancha barqaror.",
        "Kalibrlash: robot 360 gradusda necha santimetr yurishini o'lchab, keyingi hisoblarda shundan foydalaniladi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Butun missiya bitta `async def missiya_1():` ichiga yoziladi — keyin uni menyudan chaqirish oson bo'ladi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kalibrlash (10 daqiqa)", points: [
        "Robot 360 gradus yurgiziladi, bosib o'tgan masofa o'lchanadi va daftarga yoziladi."
      ]},
      { title: "6.2. Missiya kodini yozish (15 daqiqa)", points: [
        "Guruhlar 1-missiya harakatini `missiya_1()` funksiyasi ichida yozadilar.",
        "Har bir qadam ustiga izoh (#) yozib qo'yiladi."
      ]}
    ],
    kod: {
      nom: "1-missiya — yuk tashish",
      izoh: "Butun missiya bitta funksiyada. Gradus bilan yurish vaqt bilan yurishdan ishonchliroq.",
      matn: [
        "from hub import port",
        "import motor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "# Kalibrlash natijasi: 360 gradus = 17.5 sm (o'zingiznikini yozing)",
        "",
        "async def missiya_1():",
        "    # 1. Bazadan yuk oldiga yurish",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0, velocity=400)",
        "    # 2. Yukni ushlash",
        "    await motor.run_for_degrees(port.C, 180, 500)",
        "    # 3. Yukni belgilangan joyga olib borish",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 400, 0, velocity=400)",
        "    # 4. Qo'yib yuborish",
        "    await motor.run_for_degrees(port.C, -180, 500)",
        "    # 5. Bazaga qaytish",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1120, 0, velocity=-400)",
        "",
        "runloop.run(missiya_1())"
      ].join("\n")
    }
  },

  '3-chorak|6': {
    maqsad: [
      "O'quvchilar missiya dasturidagi xatolarni tizimli topib tuzatadilar.",
      "O'quvchilar `print()` yordamida dastur qayerda turganini kuzatadilar.",
      "O'quvchilar har sinov natijasini qaydnomaga yozadilar."
    ],
    lugat: [
      "Debugging – xatoni topib tuzatish jarayoni",
      "print() nazorat nuqtasi – dastur qaysi qadamga yetganini ko'rsatuvchi qator",
      "Chetlanish (Deviation) – rejadagi va haqiqiy natija farqi",
      "Bir o'zgarishli sinov – har safar faqat bitta sonni o'zgartirish",
      "Qaydnoma (Log) – sinov natijalari jadvali"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "O'tgan darsdagi kod ishga tushiriladi; qaysi qadamda xato ketayotgani belgilanadi."
      ]},
      { title: "5.2. Xatoni qanday topish kerak (10 daqiqa)", points: [
        "Har qadam boshiga `print('1-qadam')` qo'yiladi — konsolda qaysi qadamgacha yetgani ko'rinadi.",
        "Robot noto'g'ri joyda to'xtasa — gradus soni; noto'g'ri tomonga bursa — steering ishorasi tekshiriladi.",
        "HAR SAFAR FAQAT BITTA sonni o'zgartirib, natijani yozib borish kerak."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Sinov tugagach nazorat `print()` qatorlari o'chiriladi — ular dasturni sekinlashtiradi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Nazorat nuqtalari bilan sinov (15 daqiqa)", points: [
        "O'quvchilar kodga print qatorlarini qo'yib, 3 marta sinaydilar va qaydnoma to'ldiradilar."
      ]},
      { title: "6.2. Tuzatish (10 daqiqa)", points: [
        "Topilgan kamchilikka qarab sonlar tuzatiladi va qayta sinaladi."
      ]}
    ],
    kod: {
      nom: "Nazorat nuqtalari bilan missiya kodi",
      izoh: "print() qatorlari qaysi qadamgacha yetganini ko'rsatadi. Musobaqadan oldin ularni o'chiring.",
      matn: [
        "from hub import port",
        "import motor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def missiya_1():",
        "    print('1-qadam: yukka yurish')",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0, velocity=400)",
        "",
        "    print('2-qadam: ushlash')",
        "    await motor.run_for_degrees(port.C, 180, 500)",
        "",
        "    print('3-qadam: tashish')",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 400, 0, velocity=400)",
        "",
        "    print('4-qadam: qoyib yuborish')",
        "    await motor.run_for_degrees(port.C, -180, 500)",
        "",
        "    print('TUGADI')",
        "",
        "runloop.run(missiya_1())"
      ].join("\n")
    }
  },

  '3-chorak|11': {
    maqsad: [
      "O'quvchilar chiziq kuzatishni missiya kodiga qo'shadilar.",
      "O'quvchilar halqadan chiqish shartini to'g'ri yozadilar.",
      "O'quvchilar chiziq tugagach keyingi qadamga o'tadigan dastur tuzadilar."
    ],
    lugat: [
      "Chiqish sharti (Exit condition) – halqani to'xtatadigan shart",
      "break – halqadan darhol chiqish",
      "Kesishma chiziq (Cross line) – yo'lning tugaganini bildiruvchi belgi",
      "Hisoblagich (Counter) – necha marta bajarilganini sanovchi o'zgaruvchi",
      "Cheksiz halqa (Infinite loop) – chiqish sharti yozilmagan `while True`"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "2-missiyada robot chiziq bo'ylab yurib, belgilangan joyda to'xtashi kerak."
      ]},
      { title: "5.2. Halqadan qanday chiqiladi (10 daqiqa)", points: [
        "`while True:` cheksiz takrorlaydi — undan chiqish uchun ichida `break` bo'lishi SHART.",
        "Chiqish sharti: masofa sensori devorni ko'rdi, yoki rang sensori qora kesishmani ko'rdi.",
        "Chiqish sharti yozilmasa robot to'xtamaydi — missiya vaqti behuda ketadi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Chiqishdan keyin motorlarni `stop()` qilish esdan chiqmasin."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "Guruhlar chiziq kuzatib borib, to'siqni sezganda to'xtaydigan missiya kodini yozadilar."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Robot chiziq bo'ylab yurib, kerakli joyda to'xtashi tekshiriladi."
      ]}
    ],
    kod: {
      nom: "2-missiya — chiziq bo'ylab yetkazish",
      izoh: "while True ichida break bor — usiz robot to'xtamaydi.",
      matn: [
        "from hub import port",
        "import color_sensor, distance_sensor, motor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "CHEGARA = 40",
        "",
        "async def chiziq_boylab_yur():",
        "    while True:",
        "        masofa = distance_sensor.distance(port.F)",
        "        if masofa > 0 and masofa < 100:      # yetib keldi",
        "            motor_pair.stop(motor_pair.PAIR_1)",
        "            break",
        "",
        "        if color_sensor.reflection(port.E) < CHEGARA:",
        "            motor_pair.move(motor_pair.PAIR_1, -35, velocity=250)",
        "        else:",
        "            motor_pair.move(motor_pair.PAIR_1, 35, velocity=250)",
        "        await runloop.sleep_ms(10)",
        "",
        "async def missiya_2():",
        "    await chiziq_boylab_yur()",
        "    await motor.run_for_degrees(port.C, -180, 500)   # yukni qo'yish",
        "",
        "runloop.run(missiya_2())"
      ].join("\n")
    }
  },

  '3-chorak|12': {
    maqsad: [
      "O'quvchilar 2-missiya dasturini sinab, sonlarni sozlaydilar.",
      "O'quvchilar chiziq kuzatish tezligi va aniqligi orasidagi muvozanatni topadilar.",
      "O'quvchilar natijalarni qaydnomaga yozadilar."
    ],
    lugat: [
      "Muvozanat (Trade-off) – tezlik oshsa aniqlik tushadi",
      "Barqarorlik (Stability) – har safar bir xil natija",
      "Sozlanadigan son (Parameter) – dastur boshidagi o'zgartiriladigan qiymat",
      "Chetlanish – rejadagi va haqiqiy to'xtash joyi farqi",
      "Qayta sinov (Re-test) – o'zgartirishdan keyingi tekshiruv"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Kecha yozilgan dastur ishga tushiriladi va muammoli joy aniqlanadi."
      ]},
      { title: "5.2. Tezlik va aniqlik (10 daqiqa)", points: [
        "Tezlikni oshirsak vaqt yutamiz, lekin robot chiziqdan chiqib ketishi mumkin.",
        "Yechim: to'g'ri qismda tez, burilishda sekin yurish — buni ikki xil TEZLIK soni bilan qilish mumkin.",
        "Har o'zgarishdan keyin kamida 3 marta sinash kerak — bir marta omad bo'lishi mumkin."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Eng yaxshi sonlar dastur boshiga yozib qo'yiladi va daftarga ko'chiriladi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Sozlash sinovlari (20 daqiqa)", points: [
        "Guruhlar CHEGARA, BURILISH va TEZLIK sonlarini navbat bilan o'zgartirib sinaydilar.",
        "Har variant 3 martadan sinalib, o'rtacha vaqt yoziladi."
      ]},
      { title: "6.2. Eng yaxshi variantni qayd etish (5 daqiqa)", points: [
        "Tanlangan sonlar va natija qaydnomaga yoziladi."
      ]}
    ],
    kod: {
      nom: "Sozlanadigan sonlar bitta joyda",
      izoh: "Hamma o'zgartiriladigan son tepada — kod ichini titkilash shart emas.",
      matn: [
        "# ── SOZLAMALAR (faqat shu sonlarni o'zgartiring) ──",
        "CHEGARA   = 40     # oq/qora chegarasi",
        "BURILISH  = 35     # qanchalik keskin buriladi",
        "TEZLIK    = 250    # asosiy tezlik",
        "TOXTASH   = 100    # necha mm qolganda to'xtaydi",
        "",
        "# Sinov qaydnomasi:",
        "# | CHEGARA | BURILISH | TEZLIK | vaqt | natija      |",
        "# |    40   |    35    |  250   | 12s  | yaxshi      |",
        "# |    40   |    35    |  350   |  9s  | chiqib ketdi|",
        "# |    40   |    50    |  350   | 10s  | yaxshi      |"
      ].join("\n")
    }
  },

  '3-chorak|14': {
    maqsad: [
      "O'quvchilar ikki missiyani bitta dasturda ketma-ket bajaradilar.",
      "O'quvchilar funksiyalarni chaqirish tartibini boshqaradilar.",
      "O'quvchilar bazaga qaytish qadamini qo'shadilar."
    ],
    lugat: [
      "Funksiyani chaqirish – `await missiya_1()`",
      "Ketma-ketlik – funksiyalarning bajarilish tartibi",
      "Bazaga qaytish – keyingi missiyaga tayyor holatga kelish",
      "Umumiy vaqt (Total time) – ikkala missiya uchun ketgan vaqt",
      "Modullilik (Modularity) – dasturni mustaqil bo'laklarga bo'lish"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Ikkala missiya alohida ishlaydi; endi ular bitta dasturga birlashtiriladi."
      ]},
      { title: "5.2. Funksiyalarni ketma-ket chaqirish (10 daqiqa)", points: [
        "Har missiya alohida `async def` bo'lgani uchun ularni shunchaki ketma-ket chaqirish yetarli.",
        "MUHIM: har missiya oxirida robot BAZAGA qaytishi kerak — aks holda keyingisi noto'g'ri joydan boshlanadi.",
        "Gyroskopni har missiya boshida `reset_yaw(0)` bilan nolga qaytarish xatoni kamaytiradi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Umumiy vaqt o'lchanadi va 3-chorak nazorat me'yori bilan solishtiriladi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Birlashtirish (20 daqiqa)", points: [
        "Guruhlar ikkala missiya funksiyasini bitta faylga ko'chirib, ketma-ket chaqiradilar.",
        "Bazaga qaytish qadamlari qo'shiladi."
      ]},
      { title: "6.2. To'liq sinov (5 daqiqa)", points: [
        "Ikkala missiya boshdan oxir bajariladi, umumiy vaqt yoziladi."
      ]}
    ],
    kod: {
      nom: "Ikki missiyani ketma-ket bajarish",
      izoh: "Har missiya oxirida bazaga qaytish shart — keyingisi shu joydan boshlanadi.",
      matn: [
        "from hub import port, motion_sensor",
        "import motor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def bazaga_qayt(gradus):",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, gradus, 0, velocity=-400)",
        "",
        "async def missiya_1():",
        "    motion_sensor.reset_yaw(0)",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0, velocity=400)",
        "    await motor.run_for_degrees(port.C, 180, 500)",
        "    await bazaga_qayt(720)",
        "",
        "async def missiya_2():",
        "    motion_sensor.reset_yaw(0)",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 500, 0, velocity=400)",
        "    await motor.run_for_degrees(port.C, -180, 500)",
        "    await bazaga_qayt(500)",
        "",
        "async def main():",
        "    await missiya_1()",
        "    await missiya_2()",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  /* ══════════════════ 4-CHORAK — MISSIYA DASTURLASH ══════════════════ */

  '4-chorak|3': {
    maqsad: [
      "O'quvchilar 3-missiya harakatini Python kodida yozadilar.",
      "O'quvchilar attachment motorini yurish bilan birga boshqaradilar.",
      "O'quvchilar richagni ko'tarish qadamini kodga qo'shadilar."
    ],
    lugat: [
      "Richag mexanizmi – attachment motori bilan ko'tariladigan qism",
      "Bir vaqtda harakat – yurish davom etayotganda attachment ishlashi",
      "await'siz chaqirish – buyruq berib, kutmasdan davom etish",
      "Ketma-ketlik tartibi – qaysi harakat oldin bajariladi",
      "Xavfsiz to'xtash – missiya oxirida barcha motorlarni to'xtatish"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "3-missiyada robot to'siqli yo'ldan o'tib, richagni ko'tarishi kerak."
      ]},
      { title: "5.2. Yurish va attachment (10 daqiqa)", points: [
        "`await` bilan chaqirilsa buyruq tugagunicha kutiladi — harakatlar birin-ketin bo'ladi.",
        "`await` yozilmasa buyruq boshlanadi-yu, dastur keyingi qatorga o'tadi — ikkala harakat BIR VAQTDA ketadi.",
        "Bu ba'zan foydali (yurayotganda qo'lni ko'tarish), lekin ehtiyot bo'lish kerak — attachment to'siqqa tegib qolishi mumkin."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Missiya oxirida `motor_pair.stop()` va `motor.stop(port.C)` yozib qo'yish odat bo'lishi kerak."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "Guruhlar 3-missiya kodini yozadilar; kamida bitta joyda harakatlarni bir vaqtda bajarishni sinaydilar."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Robot to'siqdan o'tib, richagni ko'tarishi tekshiriladi."
      ]}
    ],
    kod: {
      nom: "3-missiya — to'siqli yo'l va richag",
      izoh: "5-qatorda `await` yo'q — shuning uchun qo'l ko'tarilayotganda robot yurishda davom etadi.",
      matn: [
        "from hub import port",
        "import motor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def missiya_3():",
        "    # 1. To'siqqacha yurish",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 600, 0, velocity=400)",
        "",
        "    # 2. Qo'lni ko'tarishni BOSHLAB, yurishda davom etish (await yo'q!)",
        "    motor.run_for_degrees(port.C, 120, 400)",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 0, velocity=250)",
        "",
        "    # 3. Richagni bosish",
        "    await motor.run_for_degrees(port.C, 90, 600)",
        "",
        "    # 4. Xavfsiz to'xtash",
        "    motor_pair.stop(motor_pair.PAIR_1)",
        "    motor.stop(port.C)",
        "",
        "runloop.run(missiya_3())"
      ].join("\n")
    }
  },

  '4-chorak|4': {
    maqsad: [
      "O'quvchilar 3-missiya dasturini sinab tuzatadilar.",
      "O'quvchilar bir vaqtda ketayotgan harakatlar to'qnashuvini aniqlaydilar.",
      "O'quvchilar sonlarni qaydnoma asosida sozlaydilar."
    ],
    lugat: [
      "To'qnashuv (Collision) – attachment to'siqqa tegib qolishi",
      "Vaqtlash (Timing) – qaysi harakat qachon boshlanishi",
      "Qaydnoma – sinov natijalari jadvali",
      "Bir o'zgarishli sinov – har safar bitta sonni o'zgartirish",
      "Ishonchlilik (Reliability) – 5 sinovdan nechtasi muvaffaqiyatli"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Kecha yozilgan kod ishga tushiriladi; qo'l juda erta yoki juda kech ko'tarilayotgani kuzatiladi."
      ]},
      { title: "5.2. Vaqtlashni to'g'rilash (10 daqiqa)", points: [
        "Qo'l erta ko'tarilsa — `motor.run_for_degrees` qatorini pastroqqa ko'chirish yoki tezlikni kamaytirish kerak.",
        "Kech ko'tarilsa — aksincha, uni yuqoriroqqa ko'chirish yoki tezlikni oshirish kerak.",
        "Ishonchlilik 5 sinovdan kamida 4 tasi muvaffaqiyatli bo'lishi bilan o'lchanadi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Musobaqada bir marta ishlagan dastur emas, HAR SAFAR ishlaydigan dastur kerak."
      ]}
    ],
    amaliy: [
      { title: "6.1. Sinov va sozlash (20 daqiqa)", points: [
        "Guruhlar 5 martadan sinab, muvaffaqiyat sonini qaydnomaga yozadilar.",
        "Har o'zgarishdan keyin yana 5 marta sinaladi."
      ]},
      { title: "6.2. Yakuniy variant (5 daqiqa)", points: [
        "Eng ishonchli variant tanlanib, sonlari daftarga ko'chiriladi."
      ]}
    ],
    kod: {
      nom: "Sinov qaydnomasi shabloni",
      izoh: "Kod emas — daftarga chiziladigan jadval. Har o'zgarishdan keyin to'ldiriladi.",
      matn: [
        "# 3-MISSIYA SINOV QAYDNOMASI",
        "#",
        "# | Sinov | Qo'l tezligi | Yurish tezligi | 5 dan nechta OK | Izoh          |",
        "# |-------|--------------|----------------|-----------------|---------------|",
        "# |   1   |     400      |      250       |      2 / 5      | qo'l erta     |",
        "# |   2   |     250      |      250       |      4 / 5      | yaxshi        |",
        "# |   3   |     250      |      200       |      5 / 5      | TANLANDI      |",
        "",
        "# QOIDA: har safar FAQAT BITTA sonni o'zgartiring."
      ].join("\n")
    }
  },

  '4-chorak|9': {
    maqsad: [
      "O'quvchilar 4-missiyada rang saralash va ko'tarishni birlashtiradilar.",
      "O'quvchilar sensor qiymatiga qarab turli harakat qiladigan kod yozadilar.",
      "O'quvchilar funksiyaga parametr berishni o'rganadilar."
    ],
    lugat: [
      "Parametr (Parameter) – funksiyaga uzatiladigan qiymat: `async def bur(gradus):`",
      "Argument – funksiyani chaqirganda beriladigan aniq son: `await bur(90)`",
      "Qayta ishlatish (Reuse) – bitta funksiyani turli sonlar bilan chaqirish",
      "Saralash (Sorting) – rangga qarab turli joyga qo'yish",
      "Ichma-ich funksiya chaqiruvi – funksiya ichida boshqa funksiyani chaqirish"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "4-missiyada robot buyumning rangini aniqlab, ikki xil joyga saralashi kerak."
      ]},
      { title: "5.2. Parametrli funksiya (10 daqiqa)", points: [
        "`async def yur(gradus):` — funksiya ichida `gradus` o'zgaruvchi kabi ishlatiladi.",
        "Chaqirish: `await yur(720)` yoki `await yur(300)` — bitta funksiya turli masofalarga xizmat qiladi.",
        "Bu takrorlanuvchi kodni yo'qotadi: 5 xil masofa uchun 5 ta funksiya yozish shart emas."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Parametr — 4-sinf Python kursining eng muhim tushunchalaridan biri."
      ]}
    ],
    amaliy: [
      { title: "6.1. Kod yozish (20 daqiqa)", points: [
        "Guruhlar parametrli `yur()` va `bur()` funksiyalarini yozib, 4-missiyani shular bilan tuzadilar.",
        "Rang bo'yicha ikki tarmoqli saralash qo'shiladi."
      ]},
      { title: "6.2. Sinov (5 daqiqa)", points: [
        "Ikki xil rangli buyum bilan sinab ko'riladi."
      ]}
    ],
    kod: {
      nom: "4-missiya — parametrli funksiyalar bilan saralash",
      izoh: "yur() va bur() funksiyalari parametr oladi — shuning uchun ular butun missiya davomida qayta ishlatiladi.",
      matn: [
        "from hub import port, motion_sensor",
        "import color, color_sensor, motor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "async def yur(gradus, tezlik=400):",
        "    await motor_pair.move_for_degrees(motor_pair.PAIR_1, gradus, 0, velocity=tezlik)",
        "",
        "async def bur(burchak):",
        "    motion_sensor.reset_yaw(0)",
        "    motor_pair.move(motor_pair.PAIR_1, 100, velocity=200)",
        "    while abs(motion_sensor.tilt_angles()[0]) < burchak * 10:",
        "        await runloop.sleep_ms(5)",
        "    motor_pair.stop(motor_pair.PAIR_1)",
        "",
        "async def missiya_4():",
        "    await yur(500)",
        "    rang = color_sensor.color(port.E)",
        "",
        "    if rang == color.RED:",
        "        await bur(90)",
        "        await yur(200, 300)",
        "    else:",
        "        await bur(-90)",
        "        await yur(300, 300)",
        "",
        "    await motor.run_for_degrees(port.C, 200, 500)   # ko'tarish",
        "",
        "runloop.run(missiya_4())"
      ].join("\n")
    }
  },

  '4-chorak|10': {
    maqsad: [
      "O'quvchilar 4-missiya dasturini ishonchlilik bo'yicha sinaydilar.",
      "O'quvchilar rang aniqlashdagi xatolar sababini topadilar.",
      "O'quvchilar yorug'lik ta'sirini hisobga oladilar."
    ],
    lugat: [
      "Ishonchlilik – 5 sinovdan nechtasi to'g'ri bajarilgani",
      "Yorug'lik ta'siri – xona yorug'ligining sensorga ta'siri",
      "Sensor balandligi – sensorning yuzadan masofasi",
      "Takroriy o'lchov – bir necha marta o'qib, o'rtachasini olish",
      "Barqaror shart – turli sharoitda ham to'g'ri ishlaydigan shart"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "Rang sensori ba'zan qizilni to'q sariq deb o'qiydi — sabablari muhokama qilinadi."
      ]},
      { title: "5.2. Rang aniqlashni barqarorlashtirish (10 daqiqa)", points: [
        "Sensor yuzadan 5-10 mm balandlikda turishi kerak — uzoq bo'lsa xona yorug'ligi aralashadi.",
        "Bir marta emas, 3 marta o'qib, ko'p chiqqan qiymatni olish ishonchliroq.",
        "Musobaqa maydonchasida sinash shart — sinfdagi yorug'lik boshqacha bo'lishi mumkin."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "Sensorni pastroq tushirish ko'pincha kod o'zgartirishdan ko'ra ko'proq foyda beradi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Ishonchlilik sinovi (20 daqiqa)", points: [
        "Har guruh 5 martadan sinaydi; noto'g'ri aniqlangan holatlar yozib boriladi.",
        "Sensor balandligi o'zgartirilib, sinov takrorlanadi."
      ]},
      { title: "6.2. Xulosa (5 daqiqa)", points: [
        "Eng barqaror sozlama tanlanadi va daftarga yoziladi."
      ]}
    ],
    kod: {
      nom: "Rangni 3 marta o'qib, ishonchli aniqlash",
      izoh: "Bir marta o'qish xato berishi mumkin. Uch o'qishdan ko'p chiqqani olinadi.",
      matn: [
        "from hub import port",
        "import color, color_sensor, runloop",
        "",
        "async def ishonchli_rang():",
        "    natijalar = []",
        "    for i in range(3):",
        "        natijalar.append(color_sensor.color(port.E))",
        "        await runloop.sleep_ms(50)",
        "",
        "    # uchtadan kamida ikkitasi bir xil bo'lsa - shu rang",
        "    if natijalar[0] == natijalar[1]:",
        "        return natijalar[0]",
        "    if natijalar[1] == natijalar[2]:",
        "        return natijalar[1]",
        "    return natijalar[0]",
        "",
        "async def main():",
        "    rang = await ishonchli_rang()",
        "    print(rang)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  },

  '4-chorak|12': {
    maqsad: [
      "O'quvchilar barcha 4 missiyani bitta dasturga birlashtiradilar.",
      "O'quvchilar tugmali menyu orqali missiya tanlashni qo'llaydilar.",
      "O'quvchilar to'liq turni vaqt bilan sinaydilar."
    ],
    lugat: [
      "Bosh dastur (Main program) – barcha missiyalarni boshqaruvchi qism",
      "Menyu – tugma bilan missiya tanlash",
      "To'liq tur (Full round) – 2.5 daqiqada barcha missiyalar",
      "Modul – mustaqil ishlaydigan dastur bo'lagi",
      "Zaxira reja (Fallback) – bir missiya ishlamasa keyingisiga o'tish"
    ],
    nazariya: [
      { title: "5.1. Kirish (7 daqiqa)", points: [
        "To'rt missiya alohida ishlaydi; endi ular bitta dasturga yig'iladi."
      ]},
      { title: "5.2. Bosh dastur tuzilishi (10 daqiqa)", points: [
        "Har missiya alohida `async def` bo'lib qoladi — ular o'zgartirilmaydi.",
        "Bosh qismda tugmali menyu turadi: chap/o'ng tugma bilan missiya raqami tanlanadi, kuch sensori ishga tushiradi.",
        "Bir missiya ishlamay qolsa, menyu orqali keyingisiga o'tish mumkin — bu musobaqada vaqt tejaydi."
      ]},
      { title: "5.3. Yakunlash (3 daqiqa)", points: [
        "To'liq tur vaqti o'lchanadi va 2.5 daqiqa me'yori bilan solishtiriladi."
      ]}
    ],
    amaliy: [
      { title: "6.1. Birlashtirish (20 daqiqa)", points: [
        "Guruhlar to'rt missiya funksiyasini bitta faylga yig'ib, menyu qo'shadilar.",
        "Har missiya menyudan tanlanib sinaladi."
      ]},
      { title: "6.2. To'liq tur (5 daqiqa)", points: [
        "Barcha missiyalar ketma-ket bajarilib, umumiy vaqt yoziladi."
      ]}
    ],
    kod: {
      nom: "Bosh dastur — 4 missiya + menyu",
      izoh: "Musobaqaga tayyor tuzilma. Missiya funksiyalari o'zgarmaydi, faqat menyudan chaqiriladi.",
      matn: [
        "from hub import port, button, light_matrix",
        "import force_sensor, motor_pair, runloop",
        "",
        "motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)",
        "",
        "# missiya_1 ... missiya_4 funksiyalari shu yerga ko'chiriladi",
        "",
        "async def menyu():",
        "    tanlov = 1",
        "    light_matrix.write(str(tanlov))",
        "    while not force_sensor.pressed(port.D):",
        "        if button.pressed(button.RIGHT) and tanlov < 4:",
        "            tanlov += 1",
        "            light_matrix.write(str(tanlov))",
        "            await runloop.sleep_ms(300)",
        "        if button.pressed(button.LEFT) and tanlov > 1:",
        "            tanlov -= 1",
        "            light_matrix.write(str(tanlov))",
        "            await runloop.sleep_ms(300)",
        "        await runloop.sleep_ms(10)",
        "    return tanlov",
        "",
        "async def main():",
        "    while True:",
        "        n = await menyu()",
        "        if n == 1:",
        "            await missiya_1()",
        "        elif n == 2:",
        "            await missiya_2()",
        "        elif n == 3:",
        "            await missiya_3()",
        "        else:",
        "            await missiya_4()",
        "        await runloop.sleep_ms(500)",
        "",
        "runloop.run(main())"
      ].join("\n")
    }
  }

  }
};
