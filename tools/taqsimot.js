/*
 * 0-4 MAKERZOID MODEL TAQSIMOTI - sinflararo takrorlanishni yo'q qilish
 * =====================================================================
 * MUAMMO (2026-09-01 gacha bo'lgan holat):
 *   Bir xil model bir necha sinfda takrorlanardi. Bola 0-sinfda qurgan
 *   robotini 1-sinfda yana qurardi:
 *       0-sinf x 1-sinf : 40 ta umumiy model (72 dan!)
 *       1-sinf x 2-sinf : 25 ta
 *       3-sinf x 4-sinf : 35 ta
 *
 * QAROR (foydalanuvchi, 2026-09-01):
 *   "asosiy qaytarilmasligi kerak bo'lgan narsa, 2-sinf o'quvchisi
 *    3-sinfda ham shu narsani o'tmasligi kerak"
 *
 * YECHIM - MAVZU BO'YICHA TAQSIMLASH:
 *   Bazadagi har bir model AYNAN BITTA mavzuga tegishli (241/241 tekshirilgan).
 *   Shuning uchun mavzuni sinfga biriktirsak, modellar avtomatik ajraladi.
 *   18 ta mavzu 5 ta sinfga aynan 72 tadan dars tushadigan qilib bo'lindi
 *   (jami 360 = 5 x 72), murakkablik (instruksiya qadamlari soni) bo'yicha
 *   o'suvchi tartibda.
 *
 * NATIJA: hech qanday model va hech qanday kichik mavzu ikki sinfda
 *         takrorlanmaydi. tools/verify.js buni har safar tekshiradi.
 *
 * SARLAVHA: daraxtdagi eski sarlavha juda qo'pol edi (atigi 18 ta unikal,
 *   "Aylanma harakatni tebranishga aylantirish" 67 darsda). Aslida aniq
 *   mavzu dars kontentining ichida yozilgan:
 *       maqsad[0] = O'quvchilar "<KICHIK MAVZU>" mavzusini "<MODEL>" ...
 *   Shu kichik mavzu sarlavha qilib olinadi -> 172 ta unikal sarlavha.
 *
 * Bu fayl `data/` ni qo'lda tahrirlashning o'rnini bosadi. extract.js
 * har ishga tushganda data/ ni boshidan yozadi.
 */

const SINFLAR = ["0-sinf", "1-sinf", "2-sinf", "3-sinf", "4-sinf"];

// Har sinf uchun: mavzular (jami aynan 72 dars) va chorak modullari nomi.
// Mavzular murakkablik bo'yicha avtomatik tartiblanadi (tartibla() ga qarang).
const TAQSIMOT = {
  "0-sinf": {
    yonalish: "Oddiy mexanizmlar, muvozanat va mustahkam konstruksiya",
    mavzular: [
      "Muvozanat markazi",                    //  8 dars /  4 model
      "Elastik energiya va inersiya kuchi",   //  8 dars /  8 model
      "Richag qonuni",                        // 19 dars / 11 model
      "Geometrik shakl mustahkamligi",        // 15 dars / 10 model
      "Tishli g'ildirak uzatmasi",            // 16 dars /  9 model
      "Shkiv va tortish kuchi"                //  6 dars /  3 model
    ],
    kirishlar: [
      "muvozanat, tayanch va elastik energiya bilan tanishuv",
      "richag, tayanch nuqtasi va kuch yelkasi",
      "geometrik shakllar va konstruksiya mustahkamligi",
      "tishli g'ildirak, shkiv va harakat uzatish"
    ],
    modullar: [
      "M1. Muvozanat va elastik energiya",
      "M2. Richag qonuni",
      "M3. Mustahkam konstruksiya",
      "M4. Tishli g'ildirak va shkiv"
    ]
  },

  "1-sinf": {
    yonalish: "Aylanma harakatni tebranma harakatga aylantirish",
    mavzular: [
      "Vint mexanizmi",                            //  1 dars
      "Avtomatik mexanizm (richag/vint)",          //  3 dars
      "Aylanma harakatni tebranishga aylantirish", // 67 dars / 56 model
      "Suzish kuchi (Arximed qonuni)"              //  1 dars
    ],
    kirishlar: [
      "mexanizm nima — aylanma va tebranma harakat",
      "krivoship va shatun mexanizmi",
      "tebranish kengligi va yo'nalishini sozlash",
      "murakkab tebranma mexanizmlar va ularni birlashtirish"
    ],
    modullar: [
      "M1. Mexanizm bilan tanishuv",
      "M2. Krivoship va shatun",
      "M3. Tebranish kengligi va yo'nalishi",
      "M4. Murakkab tebranma mexanizmlar"
    ]
  },

  "2-sinf": {
    yonalish: "Sensorlar, signal va yuk ko'tarish mexanizmlari",
    mavzular: [
      "Sensor va signal",                        // 44 dars / 19 model
      "Ko'tarish mexanizmi (richag+vint+shkiv)"  // 28 dars / 16 model
    ],
    kirishlar: [
      "sensor nima, qanday ishlaydi va nimani sezadi",
      "sensorli aqlli modellar va shartli javoblar",
      "sensordan yuk ko'tarish mexanizmiga o'tish",
      "yuk ko'tarish mexanizmlari: kran, forklift, manipulyator"
    ],
    modullar: [
      "M1. Sensor bilan tanishuv",
      "M2. Sensorli aqlli modellar",
      "M3. Sensordan ko'tarish mexanizmiga",
      "M4. Yuk ko'tarish mexanizmlari"
    ]
  },

  "3-sinf": {
    yonalish: "Elektr motor, ishqalanish, transport va aerodinamika",
    mavzular: [
      "Elektr motor va aylanma harakat",  // 13 dars /  9 model
      "Ishqalanish kuchi",                // 14 dars / 10 model
      "Transport va ishqalanish",         // 34 dars / 22 model
      "Aerodinamika va reaktiv kuch"      // 11 dars / 11 model
    ],
    kirishlar: [
      "elektr motor, moment va uzatma",
      "ishqalanish kuchi va transport g'ildiraklari",
      "murakkab transport: shassi, burilish, osma tizim",
      "aerodinamika, havo qarshiligi va reaktiv kuch"
    ],
    modullar: [
      "M1. Elektr motor va harakat",
      "M2. Ishqalanish va transport",
      "M3. Murakkab transport",
      "M4. Aerodinamika va reaktiv kuch"
    ]
  },

  "4-sinf": {
    yonalish: "Biomimikriya va notekis yuzada harakatlanuvchi texnika",
    mavzular: [
      "Biomimikriya (tabiatdan ilhomlanish)",   // 50 dars / 30 model
      "Notekis yuzada harakat (kosmik texnika)" // 22 dars / 20 model
    ],
    kirishlar: [
      "biomimikriya — tabiatdagi yechimlarni texnikaga ko'chirish",
      "hayvon harakati mexanikasi: oyoq, qadam tsikli, muvozanat",
      "biomimikriyadan kosmik texnikaga o'tish",
      "notekis yuzada harakat: klirens, ilashish, osma tizim"
    ],
    modullar: [
      "M1. Tabiatdan ilhomlanish",
      "M2. Hayvon harakati mexanikasi",
      "M3. Biomimikriyadan kosmik texnikaga",
      "M4. Notekis yuzada harakat"
    ]
  }
};

const CHORAK_DARS = 21;   // 1 kirish + 18 modelli + 1 nazorat + 1 loyiha
const MODELLI     = 18;

/* =====================================================================
 * 2-YIL — DOIMIY VARIANT (siqilgan)
 * =====================================================================
 * NEGA IKKI XIL YIL BOR (foydalanuvchi, 2026-09-01):
 *   Maktab birinchi marta ochilganda 2-3-4-sinf bolalari ham konstruktorni
 *   ko'rmagan bo'ladi — shuning uchun 1-yil hamma uchun OSONROQ va sekinroq
 *   variant. Ikkinchi yildan boshlab asl, doimiy va qiyinroq variant ishlaydi.
 *
 * ARIFMETIKA: doimiy rejimda bola 0-sinfda kirib, faqat UCH yil Makerzoid
 * ko'radi (0-1-2), 3-4-sinfda SPIKE ga o'tadi. Ya'ni 1-yilda BESH sinfga
 * yoyilgan butun korpus 2-yilda UCH sinfga sig'ishi kerak:
 *       1-yil : 5 x 72 = 360 dars  (241 model, ba'zisi 2-3 darsda)
 *       2-yil : 3 x 72 = 216 dars  (216 model, HAR MODEL BIR MARTA)
 *
 * QANDAY SIQILADI:
 *   1) Har model faqat BITTA darsda beriladi — 1-yildagi "muhandislik
 *      sinovi" va "takomillashtirish" takrorlari olib tashlanadi. Tajribali
 *      bola modelni tezroq quradi, takroriy mashq kerak emas.
 *   2) 241 model -> 216 ga tushiriladi: har manba sinfdan proporsional
 *      ravishda, AYNI kichik mavzuni beradigan modellardan qadami kamrog'i
 *      (soddaroq qurilishi) tashlab yuboriladi. Mavzu yo'qolmaydi.
 *   3) Qolgan 216 model 1-yil o'quv tartibida (oson -> qiyin) uchga bo'linadi.
 *
 * BOLA OQIMI (shuning uchun bloklar aynan shunday kesilgan):
 *   1-yil 0-sinf bolasi -> 2-yil 1-sinf -> 2-yil 2-sinf
 *   1-yil 1-sinf bolasi -> 2-yil 2-sinf -> (SPIKE)
 *   yangi kelgan bola   -> 2-yil 0-sinf -> 1-sinf -> 2-sinf -> (SPIKE)
 *   Bloklar 1-yil sinflari chegarasidan o'tib kesilgani uchun bu yo'llarning
 *   HECH BIRIDA model takrorlanmaydi. verify.js buni tekshiradi.
 */
const IKKINCHI = {
  faol: true,
  // 1-yilning qaysi sinfidan nechta model olinadi (jami 216)
  nishon: { "0-sinf": 40, "1-sinf": 53, "2-sinf": 31, "3-sinf": 47, "4-sinf": 45 },

  sinflar: {
    "0-sinf": {
      yonalish: "Oddiy mexanizmlardan krivoshipgacha",
      kirishlar: [
        "muvozanat, elastik energiya va richag qonuni",
        "tishli g'ildirak uzatmasi va mustahkam konstruksiya",
        "shkiv, vint va mexanizmni loyihalash",
        "krivoship-shatun mexanizmi va tebranma harakat"
      ],
      modullar: [
        "M1. Muvozanat, elastik energiya va richag",
        "M2. Tishli g'ildirak va mustahkam konstruksiya",
        "M3. Shkiv, vint va mexanizm loyihasi",
        "M4. Krivoship va tebranma harakat"
      ]
    },
    "1-sinf": {
      yonalish: "Tebranish sozlashdan sensor, kran va transportgacha",
      kirishlar: [
        "krivoship radiusi, amplituda va mexanizmni sozlash",
        "sensor va signal — masofa, rang, teginish",
        "yuk ko'tarish: richag, vint, shkiv, strela",
        "elektr motor, ishqalanish va transport asoslari"
      ],
      modullar: [
        "M1. Tebranish kengligi va sozlash",
        "M2. Sensor va signal",
        "M3. Yuk ko'tarish mexanizmlari",
        "M4. Elektr motor, ishqalanish va transport"
      ]
    },
    "2-sinf": {
      yonalish: "Transport, aerodinamika, biomimikriya va kosmik texnika",
      kirishlar: [
        "murakkab transport: shassi, burilish, osma tizim",
        "aerodinamika, parrak va reaktiv kuch",
        "biomimikriya — hayvon harakati va skeleti",
        "kosmik texnika, roverlar va missiyalar"
      ],
      modullar: [
        "M1. Murakkab transport",
        "M2. Aerodinamika va reaktiv kuch",
        "M3. Biomimikriya",
        "M4. Kosmik texnika va roverlar"
      ]
    }
  }
};

// ------------------------------------------------------- kichik mavzuni olish

// maqsad[0] namunasi:
//   O'quvchilar "Og'irlik markazi nima" mavzusini "Balance" modeli misolida ...
const QISM_RE = /["“]([^"”]{4,90})["”]\s*mavzusini/;

function kichikMavzu(kontent, zaxira) {
  const m = kontent && kontent.maqsad && kontent.maqsad[0] &&
            kontent.maqsad[0].match(QISM_RE);
  return m ? m[1] : zaxira;
}

// ------------------------------------------------------------------ tartiblash

/*
 * Sinfning 72 ta darsini pedagogik tartibga soladi:
 *   1) mavzular o'rtacha instruksiya qadami bo'yicha (sodda -> murakkab)
 *   2) mavzu ichida modellar qadam soni bo'yicha
 *   3) bitta modelning barcha darslari ketma-ket turadi (qur -> chuqurlashtir)
 */
function tartibla(hovuz, mavzular) {
  const tanlangan = hovuz.filter(x => mavzular.indexOf(x.mavzu) !== -1);

  const ortacha = {};
  mavzular.forEach(mv => {
    const t = tanlangan.filter(x => x.mavzu === mv);
    ortacha[mv] = t.length ? t.reduce((a, x) => a + x.qadam, 0) / t.length : 0;
  });

  const natija = [];
  mavzular.slice().sort((a, b) => ortacha[a] - ortacha[b]).forEach(mv => {
    const t = tanlangan.filter(x => x.mavzu === mv);
    const modelQadam = {};
    t.forEach(x => { modelQadam[x.model] = x.qadam; });
    Object.keys(modelQadam)
      .sort((a, b) => modelQadam[a] - modelQadam[b] || a.localeCompare(b, "en"))
      .forEach(mo => t.filter(x => x.model === mo).forEach(x => natija.push(x)));
  });
  return natija;
}

// ------------------------------------------------------- 2-yil siqilgan qatori

/*
 * birYilKetma — 1-yilning 360 ta modelli darsi O'QUV TARTIBIDA
 *               (0-sinf 1..4-chorak, keyin 1-sinf, ... 4-sinf).
 * Qaytaradi: { "0-sinf": [72 dars], "1-sinf": [72], "2-sinf": [72] }
 */
function ikkinchiYil(birYilKetma, qadamOl) {
  // 1) har model uchun faqat birinchi dars
  const modelDars = new Map();          // model -> birinchi dars
  const modelSinf = {};                 // model -> manba sinf
  const qismlar = {};                   // manba sinf -> qism -> [model]
  birYilKetma.forEach(x => {
    if (!modelDars.has(x.model)) {
      modelDars.set(x.model, x);
      modelSinf[x.model] = x.yangiSinf;
    }
    const s = modelSinf[x.model];
    const q = (qismlar[s] = qismlar[s] || {});
    (q[x.qism] = q[x.qism] || []).push(x.model);
  });

  const tartib = [...modelDars.keys()];

  // 2) proporsional qisqartirish: ayni kichik mavzuni beradigan modellardan
  //    qadami kamrog'i (soddaroq qurilishi) tashlanadi
  const tashlangan = new Set();
  for (const sinf of Object.keys(IKKINCHI.nishon)) {
    const sinfModel = tartib.filter(m => modelSinf[m] === sinf);
    const kerak = sinfModel.length - IKKINCHI.nishon[sinf];
    if (kerak <= 0) continue;

    const nomzod = [];
    for (const lst of Object.values(qismlar[sinf] || {})) {
      const uniq = [...new Set(lst)];
      if (uniq.length < 2) continue;
      uniq.sort((a, b) => qadamOl(b) - qadamOl(a) || a.localeCompare(b, "en"))
          .slice(1).forEach(m => { if (nomzod.indexOf(m) === -1) nomzod.push(m); });
    }
    nomzod.sort((a, b) => qadamOl(a) - qadamOl(b) || a.localeCompare(b, "en"));

    if (nomzod.length < kerak) {
      throw new Error("taqsimot: " + sinf + " dan " + kerak + " model tashlash kerak, " +
                      "lekin faqat " + nomzod.length + " nomzod bor");
    }
    nomzod.slice(0, kerak).forEach(m => tashlangan.add(m));
  }

  const qolgan = tartib.filter(m => !tashlangan.has(m));
  const kerakJami = MODELLI * 4 * 3;
  if (qolgan.length !== kerakJami) {
    throw new Error("taqsimot: 2-yil uchun " + qolgan.length + " model qoldi, " +
                    "kerak " + kerakJami + " (nishon yig'indisini tekshiring)");
  }

  /* 3) uchga bo'lish — 1-yil tartibida (oson -> qiyin), LEKIN bitta kichik
   *    mavzu ikki sinfga bo'linib ketmasligi kerak: aks holda bola bir xil
   *    sarlavhali darsni ikki yil ko'radi (modeli boshqa bo'lsa ham).
   *    Shuning uchun avval bir xil qismli modellar guruhga yig'iladi, keyin
   *    bloklar BUTUN guruhlar bilan aynan 72 taga to'ldiriladi.            */
  const guruhTartib = [];
  const guruh = new Map();                 // qism -> [model]
  qolgan.forEach(m => {
    const q = modelDars.get(m).qism;
    if (!guruh.has(q)) { guruh.set(q, []); guruhTartib.push(q); }
    guruh.get(q).push(m);
  });

  const qolganGuruh = guruhTartib.slice();
  const bloklar = [];
  for (let b = 0; b < 3; b++) {
    const blok = [];
    while (blok.length < 72) {
      const bosh = 72 - blok.length;
      // tartibda sig'adigan birinchi guruh
      let idx = qolganGuruh.findIndex(q => guruh.get(q).length <= bosh);
      if (idx === -1) {
        throw new Error("taqsimot: 2-yil bloklarini butun mavzu guruhlari bilan " +
                        "to'ldirib bo'lmadi (qolgan joy " + bosh + ")");
      }
      const q = qolganGuruh.splice(idx, 1)[0];
      guruh.get(q).forEach(m => blok.push(m));
    }
    bloklar.push(blok);
  }

  const natija = {};
  ["0-sinf", "1-sinf", "2-sinf"].forEach((s, i) => {
    natija[s] = bloklar[i].map(m => modelDars.get(m));
  });
  return natija;
}

// -------------------------------------------------- chuqurlashtirish darslari

/*
 * Bitta (model + kichik mavzu) juftligi sinf ichida bir necha marta uchrasa,
 * birinchisi qurish darsi bo'lib qoladi, keyingilari ALMASHTIRILADI.
 * Sababi: bazada bu darslar bir-birining nusxasi (ilgari turli sinflarda
 * turgani uchun sezilmasdi). Sinfga yig'ilganda ular ochiq takror bo'lib qoladi.
 *
 * O'rniga bola uchun mazmunan boshqa ish beriladi:
 *   2-uchrashuv -> MUHANDISLIK SINOVI  (xotiradan yig'ish, o'lchash, jadval)
 *   3-uchrashuv -> TAKOMILLASHTIRISH   (bitta qismni o'zgartirib, taqqoslash)
 * Model bir xil, instruksiya bir xil - lekin dars butunlay boshqa.
 */

function sinovDarsi(asos, model, qism) {
  return {
    nom: qism + " - muhandislik sinovi",
    kontent: {
      maqsad: [
        "O'quvchilar \"" + model + "\" modelini instruksiyaga kamroq qarab qayta yig'adilar va yig'ish vaqtini o'lchaydilar.",
        "O'quvchilar \"" + qism + "\" mavzusi bo'yicha modelning ishlashini aniq mezon (vaqt, masofa yoki takrorlar soni) bilan o'lchab, natijani jadvalga yozadilar.",
        "O'quvchilar uch marta o'lchov o'tkazib, natijalar nega bir xil chiqmasligini tushuntiradilar."
      ],
      lugat: (asos.lugat || []).slice(0, 3).concat([
        "O'lchov (Measurement) - natijani raqam bilan ifodalash",
        "Mezon (Criteria) - nimani o'lchayotganimizni aniq belgilash",
        "Takroriylik (Repeatability) - bir xil sinov qayta o'tkazilganda natija qanchalik yaqin chiqishi"
      ]),
      softSkill: "Aniqlik va halollik - O'lchagan natijani qanday chiqqan bo'lsa, shundayligicha yozish kerak. Yomon natija ham natija: u nimanidir o'rgatadi.",
      resurslar: [
        "Makerzoid Robot Master Standard to'plami (har 1-2 o'quvchiga bitta)",
        "\"" + model + "\" modeli uchun bosqichma-bosqich rasmli instruksiya",
        "Sekundomer yoki telefon soati (har guruhga bitta)",
        "O'lchov lentasi yoki chizg'ich",
        "Natija jadvali uchun daftar varag'i (3 ta sinov ustuni bilan)"
      ],
      nazariya: [
        {
          title: "5.1. Kirish (4 daqiqa)",
          points: [
            "O'tgan darsda \"" + model + "\" modelini qurgan edik va \"" + qism + "\" mavzusini ko'rgan edik.",
            "Bugun uni qaytadan quramiz - lekin bu safar tezlikka va aniqlikka e'tibor beramiz."
          ]
        },
        {
          title: "5.2. Muhandis nimani o'lchaydi (8 daqiqa)",
          points: [
            "Muhandis \"yaxshi ishladi\" demaydi - u raqam aytadi: necha soniya, necha santimetr, necha marta.",
            "Shuning uchun avval MEZON tanlanadi: biz aynan nimani o'lchaymiz?",
            "Bir marta o'lchash yetarli emas. Uch marta o'lchab, o'rtachasini olamiz."
          ]
        },
        {
          title: "5.3. Bugungi mezon (3 daqiqa)",
          points: [
            "Sinf birgalikda ikkita mezon tanlaydi: (1) modelni yig'ish vaqti, (2) modelning ishlash ko'rsatkichi.",
            "Mezonlar doskaga yoziladi - hamma bir xil narsani o'lchaydi."
          ]
        }
      ],
      amaliy: [
        {
          title: "6.1. Xotiradan yig'ish (15 daqiqa)",
          points: [
            "O'quvchilar \"" + model + "\" modelini yig'ishni boshlaydilar va sekundomerni ishga tushiradilar.",
            "Instruksiyaga qarash mumkin, lekin har qaraganda daftarga bitta belgi qo'yiladi.",
            "Model tayyor bo'lganda vaqt to'xtatiladi va daftarga yoziladi: vaqt + necha marta qaralgani."
          ]
        },
        {
          title: "6.2. O'lchash va jadval (12 daqiqa)",
          points: [
            "Tanlangan mezon bo'yicha model UCH MARTA sinaladi, har safar natija jadvalga yoziladi.",
            "Uch natijaning o'rtachasi hisoblanadi.",
            "O'qituvchi savol beradi: natijalar bir xil chiqdimi? Agar yo'q bo'lsa, nima o'zgardi?"
          ]
        },
        {
          title: "6.3. Xulosa (3 daqiqa)",
          points: [
            "Har bir juftlik o'z jadvalini ko'rsatib, eng yaxshi va eng yomon natijani aytadi.",
            "Sinf birgalikda aniqlaydi: modelning qaysi qismi natijaga eng ko'p ta'sir qildi?"
          ]
        }
      ],
      uyga: [
        "Uyda biror ishni (masalan, portfel yig'ish) uch marta bajarib, har safar vaqtini yozing. Natijalar bir xil chiqdimi?",
        "Ijodiy topshiriq: \"" + model + "\" modelining natijasini yaxshilash uchun bitta g'oyangizni bir gapda yozib keling."
      ]
    }
  };
}

function takomilDarsi(asos, model, qism) {
  return {
    nom: qism + " - takomillashtirish",
    kontent: {
      maqsad: [
        "O'quvchilar \"" + model + "\" modelining bitta qismini ataylab o'zgartirib, natija qanday o'zgarishini bashorat qiladilar.",
        "O'quvchilar o'zgartirishdan oldingi va keyingi natijani o'lchab taqqoslaydilar.",
        "O'quvchilar \"" + qism + "\" mavzusi bo'yicha o'z xulosasini dalil (o'lchov natijasi) bilan asoslaydilar."
      ],
      lugat: (asos.lugat || []).slice(0, 3).concat([
        "Bashorat (Prediction) - sinovdan oldin natijani taxmin qilish",
        "O'zgaruvchi (Variable) - biz ataylab o'zgartirayotgan qism",
        "Taqqoslash (Comparison) - oldingi va keyingi natijani yonma-yon qo'yish"
      ]),
      softSkill: "Tanqidiy fikrlash - Bashoratingiz noto'g'ri chiqsa, bu xato emas. Muhimi: nega shunday bo'lganini tushuntira olish.",
      resurslar: [
        "Makerzoid Robot Master Standard to'plami (har 1-2 o'quvchiga bitta)",
        "\"" + model + "\" modeli uchun bosqichma-bosqich rasmli instruksiya",
        "Sekundomer va o'lchov lentasi",
        "Taqqoslash jadvali uchun daftar varag'i (\"oldin\" va \"keyin\" ustunlari bilan)",
        "Qo'shimcha detallar (turli o'lchamdagi g'ildirak, tishli g'ildirak, og'irlik)"
      ],
      nazariya: [
        {
          title: "5.1. Kirish (4 daqiqa)",
          points: [
            "\"" + model + "\" modelini biz allaqachon qurganmiz va sinaganmiz.",
            "Bugun muhandis kabi ish qilamiz: modelni YAXSHILASHGA harakat qilamiz."
          ]
        },
        {
          title: "5.2. Faqat bitta narsani o'zgartiring (8 daqiqa)",
          points: [
            "Agar bir vaqtda ikki narsani o'zgartirsak, natija nima uchun o'zgarganini bilib bo'lmaydi.",
            "Shuning uchun qoida: bir sinovda FAQAT BITTA o'zgaruvchi.",
            "\"" + qism + "\" mavzusiga qaytamiz: bu modelda natijaga eng ko'p nima ta'sir qiladi?"
          ]
        },
        {
          title: "5.3. Bashorat (3 daqiqa)",
          points: [
            "Har bir juftlik o'zgartirishni tanlaydi va natijani BASHORAT qilib daftarga yozadi.",
            "Bashorat sinovdan oldin yozilishi shart - keyin yozilsa, u bashorat emas."
          ]
        }
      ],
      amaliy: [
        {
          title: "6.1. Boshlang'ich natijani olish (8 daqiqa)",
          points: [
            "Model asl holicha yig'iladi va tanlangan mezon bo'yicha sinaladi.",
            "Natija jadvalning \"oldin\" ustuniga yoziladi."
          ]
        },
        {
          title: "6.2. O'zgartirish va qayta sinov (17 daqiqa)",
          points: [
            "Juftlik o'zi tanlagan bitta qismni o'zgartiradi (g'ildirak o'lchami, richag uzunligi, og'irlik joyi va h.k.).",
            "Model qayta sinaladi va natija \"keyin\" ustuniga yoziladi.",
            "Bashorat to'g'ri chiqdimi - daftarga belgilanadi."
          ]
        },
        {
          title: "6.3. Taqqoslash va himoya (5 daqiqa)",
          points: [
            "Har bir juftlik sinfga chiqib, \"oldin\" va \"keyin\" natijasini aytadi.",
            "Savol: nima uchun aynan shunday o'zgardi? Javob \"" + qism + "\" mavzusi asosida tushuntiriladi."
          ]
        }
      ],
      uyga: [
        "Velosiped yoki o'yinchoqda bitta narsani o'zgartirsangiz (masalan, shina bosimi), nima o'zgarishini yozing.",
        "Ijodiy topshiriq: \"" + model + "\" modeliga qo'shimcha bitta funksiya qo'shish g'oyasini chizib keling."
      ]
    }
  };
}

// Nechanchi marta uchrayotganiga qarab almashtirish darsini qaytaradi.
// nechanchi = 1 bo'lsa null (asl qurish darsi qoladi).
function almashtir(asos, model, qism, nechanchi) {
  if (nechanchi <= 1) return null;
  if (nechanchi === 2) return sinovDarsi(asos, model, qism);
  return takomilDarsi(asos, model, qism);
}

// ------------------------------------------------------- chorak kirish darsi

/*
 * Model taqsimotidan keyin chorak mazmuni o'zgardi, shuning uchun bazadagi
 * kirish darsi endi to'g'ri kelmaydi (masalan 0-sinf 3-choragi geometrik
 * shakllar haqida, bazadagi kirish esa motorni va'da qilardi).
 * Kirish darsi chorak moduliga qarab qayta yoziladi.
 */
function belgi(yil, sinf) {
  if (yil === "2-yil" && IKKINCHI.faol && IKKINCHI.sinflar[sinf]) {
    return IKKINCHI.sinflar[sinf];
  }
  return TAQSIMOT[sinf];
}

function kirishDarsi(yil, sinf, chorakNo) {
  const b = belgi(yil, sinf);
  if (!b || !b.kirishlar) return null;
  const tavsif = b.kirishlar[chorakNo - 1];
  const modul = b.modullar[chorakNo - 1];
  if (!tavsif) return null;

  const birinchi = chorakNo === 1;

  return {
    nom: "Chorak kirish: " + tavsif,
    kontent: {
      maqsad: [
        "O'quvchilar " + chorakNo + "-chorakda nimani o'rganishlarini biladilar: " + tavsif + ".",
        "O'quvchilar chorak oxirida qanday nazorat ishi va loyiha bo'lishini oldindan biladilar.",
        "O'quvchilar to'plam bilan ishlash va xavfsizlik qoidalarini takrorlaydilar."
      ],
      lugat: [
        "Chorak (Quarter) - o'quv yilining to'rtdan bir qismi",
        "Modul (Module) - bir mavzuga bag'ishlangan darslar guruhi",
        "Instruksiya (Instruction) - modelni bosqichma-bosqich yig'ish qo'llanmasi",
        "Detal (Part) - to'plamdagi alohida bo'lak",
        "Xavfsizlik (Safety) - ishlashda shikastlanmaslik qoidalari"
      ],
      softSkill: birinchi
        ? "Tartib va mas'uliyat - Ish joyini toza saqlash, detallarni joyiga qaytarish. To'plam guruhniki, undan hamma foydalanadi."
        : "Rejalashtirish - Chorak boshida oxirgi maqsadni bilish, ishni shunga qarab yo'lga qo'yish.",
      resurslar: [
        "Makerzoid Robot Master Standard to'plami (har 1-2 o'quvchiga bitta)",
        "Taqdimot uchun kompyuter va proyektor",
        "Chorak rejasi chop etilgan varaq (doskaga osish uchun)",
        "Detallarni saralash uchun qutilar yoki laganlar"
      ],
      nazariya: [
        {
          title: "5.1. Bu chorakda nima o'rganamiz (10 daqiqa)",
          points: [
            "Chorak mavzusi e'lon qilinadi: " + tavsif + ".",
            "Modul nomi: \"" + modul + "\".",
            "Chorakda 18 ta model quriladi, so'ng nazorat ishi va loyiha bo'ladi."
          ]
        },
        {
          title: "5.2. Xavfsizlik va tartib (7 daqiqa)",
          points: [
            "Detallarni og'izga solmaslik, boshqa o'quvchiga qarab otmaslik.",
            "Har dars oxirida detallar sanab, joyiga qaytariladi.",
            "Model yig'ilmasa - qo'l ko'tarib so'raladi, kuch bilan bosilmaydi."
          ]
        }
      ],
      amaliy: [
        {
          title: "6.1. To'plamni ko'rib chiqish (12 daqiqa)",
          points: [
            "O'quvchilar to'plamni ochib, detallar turlarini ko'rib chiqadilar.",
            birinchi
              ? "Har bir detal turi nima uchun kerakligi birga muhokama qilinadi."
              : "Shu chorakda ko'p ishlatiladigan detallar alohida ajratib ko'rsatiladi."
          ]
        },
        {
          title: "6.2. Sinov yig'ilishi (13 daqiqa)",
          points: [
            "Juftliklar kichik sinov konstruksiyasini yig'ib ko'radilar (instruksiyasiz, erkin).",
            "Maqsad - detallarni ulash usullarini qo'l bilan his qilish."
          ]
        },
        {
          title: "6.3. Chorak rejasi (5 daqiqa)",
          points: [
            "Chorak rejasi doskaga osiladi: qaysi haftada nima bo'lishi ko'rsatiladi.",
            "Nazorat ishi va loyiha talablari oldindan aytiladi."
          ]
        }
      ],
      uyga: [
        "Uyingizdan \"" + tavsif.split(/[-:,]/)[0].trim() + "\" mavzusiga aloqador bitta narsani toping va daftaringizga yozing.",
        "To'plam bilan ishlash qoidalaridan ikkitasini eslab qoling."
      ]
    }
  };
}

// --------------------------------------------------------------------- meta

// "1-chorak, 5-hafta" - chorakda 21 dars, haftasiga 2 dars
function haftaMatni(chorakNo, idx) {
  return chorakNo + "-chorak, " + (Math.floor(idx / 2) + 1) + "-hafta";
}

function darsRaqami(chorakNo, idx) {
  return ((chorakNo - 1) * CHORAK_DARS + idx + 1) + " / " + (CHORAK_DARS * 4);
}

module.exports = {
  faol: true,
  manbaYil: "1-yil",          // Makerzoid hovuzi shu yildan yig'iladi
  SINFLAR, TAQSIMOT, IKKINCHI, CHORAK_DARS, MODELLI,
  kichikMavzu, tartibla, ikkinchiYil, almashtir, belgi, kirishDarsi,
  haftaMatni, darsRaqami
};
