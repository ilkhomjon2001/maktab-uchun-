/*
 * QURISH INSTRUKSIYALARI — resurs bazasi
 * ======================================
 *
 * Har bir dars uchun qurish instruksiyasi havolasi (yoki lokal fayl yo'li).
 * Kalit — model nomi (tree_data.js dagi "model" maydoni yoki SPIKE darsi sarlavhasidagi nom).
 *
 * Yozuv formati:
 *   "Model nomi": [
 *     { nom: "Ko'rinadigan nom", url: "https://...", manba: "LEGO Education", tur: "pdf" },
 *     ...  // bir modelga bir nechta fayl bo'lishi mumkin (masalan 5 qismli instruksiya)
 *   ]
 *
 * tur:  "pdf" | "web" | "video" | "lokal"
 * manba: havola qayerdan olingani (LEGO Education, Pybricks, Makerzoid va h.k.)
 *
 * LOKAL FAYL ishlatish uchun:  url: "instructions/makerzoid/crane.pdf"
 * (fayllarni site/instructions/ papkasiga joylashtiring)
 *
 * BARCHA SPIKE HAVOLALARI 2026-08-08 da tekshirilgan — HTTP 200 qaytargan.
 */

window.LESSON_RESOURCES = {

// =====================================================================
// SPIKE PRIME — LEGO Education rasmiy instruksiyalari
// =====================================================================

"Driving Base 1": [
  { nom: "Driving Base — rasmiy qurish instruksiyasi (PDF)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blte58422fa7d508a60/5f8802b882eaa522ca601c9f/driving-base-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Interaktiv qurish (SPIKE App onlayn)",
    url: "https://spike.legoeducation.com/prime/models/",
    manba: "LEGO Education", tur: "web" }
],

"Driving Base 2": [
  { nom: "Driving Base — rasmiy qurish instruksiyasi (PDF)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blte58422fa7d508a60/5f8802b882eaa522ca601c9f/driving-base-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Driving Base + Tools & Accessories (PDF)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt4bbe3f59ee1a3097/5f88024bde194e1bde3f0844/driving-base-tools-accessories-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Driving Base 3 (Advanced Driving Base)": [
  { nom: "Advanced Driving Base — 1/5: Old qism (Front Part)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt9d23fa8f579e63ea/5f8802346c54ba0f72c2081e/advanced-driving-base-bi-pdf-book1of5.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Advanced Driving Base — 2/5: O'ng yon (Right Side)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt0ee7fdaec9e58ae1/5f88021925f8972408a02fde/advanced-driving-base-bi-pdf-book2of5.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Advanced Driving Base — 3/5: Chap yon (Left Side)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt493de8c0e8747730/5f88021dce1f390e99419eca/advanced-driving-base-bi-pdf-book3of5.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Advanced Driving Base — 4/5: Orqa qism (Rear Part)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt31204a16915d90ff/5f88023d0fa6ca0be8c8d3bd/advanced-driving-base-bi-pdf-book4of5.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Advanced Driving Base — 5/5: Yakuniy yig'ish (Assembly)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt12341bbb85ea4318/5f8802c42792080f77214054/advanced-driving-base-bi-pdf-book5of5.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Dars rejasi: Assembling an Advanced Driving Base",
    url: "https://education.lego.com/en-us/lessons/prime-competition-ready/assembling-an-advanced-driving-base/",
    manba: "LEGO Education", tur: "web" }
],

"StarterBot": [
  { nom: "SPIKE Prime StarterBot — qadam-baqadam qurish",
    url: "https://pybricks.com/learn/building-a-robot/spike-prime/",
    manba: "Pybricks", tur: "web" }
],

"Robot Arm (robot-qo'l)": [
  { nom: "Arm Holder (robot-qo'l tayanchi) — 1/2",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt1aaa26c441e04c6a/5f880449887a311d8fa19846/design-for-someone-bi-pdf-book1of2.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Connection Interface (ulanish qismi) — 2/2",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt78418d3d7505c864/5f8802404eb7997a5159387e/design-for-someone-bi-pdf-book2of2.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Line Follower attachment": [
  { nom: "Line Module (chiziq kuzatish moduli) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blte06e23b5b07790a9/5f88029344cd830f46b07278/line-module-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Dars rejasi: Training Camp 3 — Reacting to Lines",
    url: "https://education.lego.com/en-us/lessons/prime-competition-ready/training-camp-3-react-to-lines/",
    manba: "LEGO Education", tur: "web" }
],

"Color sensor mount": [
  { nom: "Driving Base + Color Sensor Module — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/bltc7abeab0450c5a27/5f880246e787ed1c02270883/driving-base-with-color-sensor-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Gripper (ushlagich) attachment": [
  { nom: "Grabber 1 (ushlagich) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/bltb5e585f94cb4e72b/5f8802e5a302dc0d859a734d/supercleaup-bi-pdf-book2of3.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Grabber 2 (ushlagich, ikkinchi variant) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/bltb8840f08a6d0362b/5f8802dc2792080f7721405c/supercleaup-bi-pdf-book3of3.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Plow attachment (belkurak)": [
  { nom: "Dozer Blade (belkurak) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt8ce27485ca75b9a0/5f88026bc32d3d15cedf7c26/dozer-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Fork-lift attachment": [
  { nom: "Lift Arm (ko'tarish qo'li) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt61c6a675caa6e159/5f880275bf5ab07ee90076db/lift-arm-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Crates (yuk qutilari — sinov uchun) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/bltcd184ccf008fdd05/5f88023282eaa522ca601c95/crates-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Ultrasonic sensor mount": [
  { nom: "Driving Base + Tools & Accessories (sensor o'rnatish qismlari)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt4bbe3f59ee1a3097/5f88024bde194e1bde3f0844/driving-base-tools-accessories-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Bumper attachment (to'siq sezuvchi)": [
  { nom: "StarterBot — Hub tugmalari bumper sifatida (bo'lim: bumpers)",
    url: "https://pybricks.com/learn/building-a-robot/spike-prime/",
    manba: "Pybricks", tur: "web" },
  { nom: "Dars rejasi: Training Camp 2 — Playing with Objects",
    url: "https://education.lego.com/en-us/lessons/prime-competition-ready/training-camp-2-playing-with-objects/",
    manba: "LEGO Education", tur: "web" }
],

"Ball Shooter attachment": [
  { nom: "Player (to'p tepuvchi mexanizm) — 1/2",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/bltaf274cbd7c262aea/5f88025330c48e7ee7c062e3/goal-bi-pdf-book1of2.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Goal and Accessories (darvoza va aksessuarlar) — 2/2",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt1bbf8d1125cbeceb/5f88024d44cd830f46b07270/goal-bi-pdf-book2of2.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Catapult attachment": [
  { nom: "Hopper (sakrash/otish mexanizmi) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt94f5015eec2dae38/5f88025b722f2a15c7ba2521/hopper-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Scoop attachment (cho'mich)": [
  { nom: "Brick Sorter Base (saralash/olish moslamasi) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blte262c4974fee83b0/5f8802a3ed5ccb12e4342dac/automate-it-bi-pdf-book2of3.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Tractor": [
  { nom: "Driving Base + Dozer Blade (traktor-uslub konfiguratsiya)",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt8ce27485ca75b9a0/5f88026bc32d3d15cedf7c26/dozer-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Kriket (box robot)": [
  { nom: "Game Module (ixcham quti-robot moduli) — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/bltfe6f04e1aad7e4a1/5f880295ad20281d51fbc1d8/game-module-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
],

"Sensor arm attachment": [
  { nom: "Markers / sensor qo'l moslamasi — PDF",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt74887606455c5c18/5f880280ed5ccb12e4342da4/markers-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" },
  { nom: "Driving Base + Tools & Accessories",
    url: "https://assets.education.lego.com/v3/assets/blt293eea581807678a/blt4bbe3f59ee1a3097/5f88024bde194e1bde3f0844/driving-base-tools-accessories-bi-pdf-book1of1.pdf?locale=en-us",
    manba: "LEGO Education", tur: "pdf" }
]

// =====================================================================
// MAKERZOID — bu yerga o'z resurslaringizni qo'shing
// =====================================================================
//
// Ikrom, Makerzoid instruksiyalarini shu yerga qo'shasiz. Format:
//
// ,"Crane": [
//   { nom: "Crane — qurish instruksiyasi",
//     url: "instructions/makerzoid/crane.pdf",
//     manba: "Makerzoid", tur: "lokal" }
// ]
//
// ,"Little Lantern 1": [
//   { nom: "Little Lantern 1 — instruksiya",
//     url: "https://drive.google.com/file/d/XXXX/view",
//     manba: "Makerzoid (Google Drive)", tur: "web" }
// ]
//
// MUHIM: model nomi tree_data.js dagi nom bilan AYNAN bir xil bo'lishi kerak
// (masalan "Little Lantern 1", "Manual Rocking YL Man 3").
// Barcha 241 ta model nomini ko'rish uchun:  curriculum/list_models.py ni ishga tushiring.
//
// Lokal fayllarni site/instructions/makerzoid/ papkasiga joylashtiring.

};
