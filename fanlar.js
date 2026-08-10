/* Tarbion xususiy maktabi — FANLAR RO'YXATI
 *
 * Sayt endi faqat robototexnika emas, maktabning BARCHA fanlari uchun dars
 * rejalari bazasi. Har bir fan shu ro'yxatda bitta yozuv:
 *
 *   id       — havolada ishlatiladi (#/matematika), lotin harflari va chiziqcha
 *   nom      — kartochkada va sarlavhada ko'rinadigan nom
 *   qisqa    — juda tor joyda (sarlavha ostida) ishlatiladi
 *   belgi    — kartochkadagi belgi (emoji)
 *   rang     — kartochka urg'u rangi
 *   sinflar  — qaysi sinflarda o'qitiladi
 *   guruh    — bosh sahifada qaysi bo'limda turadi
 *   tavsif   — kartochkadagi bir qatorli izoh
 *   holat    — "tayyor"  : kontent bazasi bor, darslar ochiladi
 *              "reja"    : fan ro'yxatda bor, kontent hali tayyorlanmagan
 *   manba    — "tree" bo'lsa darslar window.TREE_DATA dan olinadi.
 *              Kelajakda har fanning o'z daraxti bo'lsa, shu maydon o'zgaradi
 *              (masalan manba:"tree_matematika") va app.js shu nomdagi
 *              global o'zgaruvchidan o'qiydi.
 *
 * YANGI FAN QO'SHISH: shu ro'yxatga yozuv qo'shish yetarli — app.js va
 * index.html ga tegilmaydi. Kontent tayyor bo'lganda holat "tayyor" qilinadi
 * va manba ko'rsatiladi.
 */
window.FANLAR = [
  /* ---------------- Aniq va tabiiy fanlar ---------------- */
  {
    id: "robototexnika", nom: "Robototexnika va IT", qisqa: "Robototexnika",
    belgi: "🤖", rang: "#17602D", sinflar: "0–8-sinf",
    guruh: "Aniq va tabiiy fanlar", holat: "tayyor", manba: "tree",
    tavsif: "Konstruksiya, mexanizmlar, elektronika, Arduino, ESP32 va sun'iy intellekt"
  },
  {
    id: "matematika", nom: "Matematika", belgi: "📐", rang: "#0b6b8f",
    sinflar: "1–11-sinf", guruh: "Aniq va tabiiy fanlar", holat: "reja",
    tavsif: "Arifmetika, algebra, geometriya, ehtimollar va statistika"
  },
  {
    id: "fizika", nom: "Fizika", belgi: "🧲", rang: "#6b3fa0",
    sinflar: "6–11-sinf", guruh: "Aniq va tabiiy fanlar", holat: "reja",
    tavsif: "Mexanika, issiqlik, elektr, optika, atom fizikasi va laboratoriya ishlari"
  },
  {
    id: "kimyo", nom: "Kimyo", belgi: "⚗️", rang: "#b04a20",
    sinflar: "7–11-sinf", guruh: "Aniq va tabiiy fanlar", holat: "reja",
    tavsif: "Modda tuzilishi, reaksiyalar, organik kimyo va xavfsiz tajribalar"
  },
  {
    id: "biologiya", nom: "Biologiya", belgi: "🌿", rang: "#4a7d1c",
    sinflar: "5–11-sinf", guruh: "Aniq va tabiiy fanlar", holat: "reja",
    tavsif: "Botanika, zoologiya, odam anatomiyasi, genetika va ekologiya"
  },
  {
    id: "informatika", nom: "Informatika", belgi: "💻", rang: "#0f7a72",
    sinflar: "5–11-sinf", guruh: "Aniq va tabiiy fanlar", holat: "reja",
    tavsif: "Kompyuter savodxonligi, algoritmlar, dasturlash va raqamli xavfsizlik"
  },
  {
    id: "astronomiya", nom: "Astronomiya", belgi: "🔭", rang: "#3a4fa0",
    sinflar: "10–11-sinf", guruh: "Aniq va tabiiy fanlar", holat: "reja",
    tavsif: "Osmon jismlari, Quyosh sistemasi, teleskop bilan kuzatish"
  },

  /* ---------------- Til va adabiyot ---------------- */
  {
    id: "ona-tili", nom: "Ona tili", belgi: "✍️", rang: "#a03a6b",
    sinflar: "1–11-sinf", guruh: "Til va adabiyot", holat: "reja",
    tavsif: "Savod o'rgatish, fonetika, morfologiya, sintaksis va nutq madaniyati"
  },
  {
    id: "adabiyot", nom: "Adabiyot", belgi: "📚", rang: "#8a2f52",
    sinflar: "5–11-sinf", guruh: "Til va adabiyot", holat: "reja",
    tavsif: "Xalq og'zaki ijodi, mumtoz va zamonaviy adabiyot, matn tahlili"
  },
  {
    id: "ingliz-tili", nom: "Ingliz tili", belgi: "🌍", rang: "#1f5fa0",
    sinflar: "1–11-sinf", guruh: "Til va adabiyot", holat: "reja",
    tavsif: "Tinglash, gapirish, o'qish, yozish — CEFR darajalari bo'yicha"
  },
  {
    id: "rus-tili", nom: "Rus tili", belgi: "🗣️", rang: "#2f6f8a",
    sinflar: "2–11-sinf", guruh: "Til va adabiyot", holat: "reja",
    tavsif: "Alifbo, grammatika, o'qish va og'zaki nutq"
  },

  /* ---------------- Ijtimoiy fanlar ---------------- */
  {
    id: "tarix", nom: "Tarix", belgi: "🏛️", rang: "#8a6a1f",
    sinflar: "5–11-sinf", guruh: "Ijtimoiy fanlar", holat: "reja",
    tavsif: "O'zbekiston tarixi va jahon tarixi, manbalar bilan ishlash"
  },
  {
    id: "geografiya", nom: "Geografiya", belgi: "🗺️", rang: "#1f7a5c",
    sinflar: "5–11-sinf", guruh: "Ijtimoiy fanlar", holat: "reja",
    tavsif: "Xarita, tabiiy geografiya, iqtisodiy geografiya va o'lkashunoslik"
  },
  {
    id: "tarbiya", nom: "Tarbiya", belgi: "🤝", rang: "#7a4a1f",
    sinflar: "1–11-sinf", guruh: "Ijtimoiy fanlar", holat: "reja",
    tavsif: "Odob-axloq, milliy qadriyatlar, huquqiy savodxonlik va kasb tanlash"
  },

  /* ---------------- Ijod, mehnat va salomatlik ---------------- */
  {
    id: "chizmachilik", nom: "Chizmachilik", belgi: "📏", rang: "#4a5568",
    sinflar: "8–9-sinf", guruh: "Ijod, mehnat va salomatlik", holat: "reja",
    tavsif: "Proyeksiya, chizma o'qish, o'lchamlar va texnik grafika"
  },
  {
    id: "tasviriy-sanat", nom: "Tasviriy san'at", belgi: "🎨", rang: "#a0522d",
    sinflar: "1–7-sinf", guruh: "Ijod, mehnat va salomatlik", holat: "reja",
    tavsif: "Rang, kompozitsiya, naqsh va amaliy bezak san'ati"
  },
  {
    id: "musiqa", nom: "Musiqa madaniyati", belgi: "🎵", rang: "#7b3fa0",
    sinflar: "1–7-sinf", guruh: "Ijod, mehnat va salomatlik", holat: "reja",
    tavsif: "Nota savodi, ashula, milliy cholg'ular va tinglash madaniyati"
  },
  {
    id: "texnologiya", nom: "Texnologiya", belgi: "🔧", rang: "#6a6a2f",
    sinflar: "1–9-sinf", guruh: "Ijod, mehnat va salomatlik", holat: "reja",
    tavsif: "Qo'l mehnati, materiallar, asboblar bilan xavfsiz ishlash"
  },
  {
    id: "jismoniy-tarbiya", nom: "Jismoniy tarbiya", belgi: "⚽", rang: "#b0402a",
    sinflar: "1–11-sinf", guruh: "Ijod, mehnat va salomatlik", holat: "reja",
    tavsif: "Umumiy jismoniy tayyorgarlik, sport turlari va sog'lom turmush"
  }
];

/* Bosh sahifadagi bo'limlar tartibi. Ro'yxatdagi "guruh" shu nomlardan biri
   bo'lishi kerak — bo'lmasa fan eng oxirida "Boshqa fanlar" ostida chiqadi. */
window.FAN_GURUHLARI = [
  "Aniq va tabiiy fanlar",
  "Til va adabiyot",
  "Ijtimoiy fanlar",
  "Ijod, mehnat va salomatlik"
];
