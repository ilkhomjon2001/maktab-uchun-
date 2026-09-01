/*
 * CHORAK LOYIHALARI — har sinf uchun alohida
 * ==========================================
 * MUAMMO: bazada loyiha darsi 20 ta joyda (4 chorak x 5 sinf) AYNAN bir xil
 * matn edi: "shu chorak modellaridan birini tanlab, o'zgartirib/kengaytirib
 * qurish (erkin ijod)". Bola 5 yil davomida 20 marta bir xil topshiriq oladi.
 *
 * YECHIM: loyiha talabi sinfdan sinfga O'SADI —
 *   0-sinf : bitta modelni o'zgartirish
 *   1-sinf : ikki mexanizmni birlashtirish
 *   2-sinf : berilgan talabga javob beradigan qurilma loyihalash
 *   3-sinf : hayotdagi muammoni tanlab, yechim qurish va o'lchash
 *   4-sinf : to'liq muhandislik tsikli (talab -> eskiz -> qurish -> sinov -> takomil)
 * Chorak ichida ham talab murakkablashadi.
 *
 * Baholash uch mezon bo'yicha: model ishlashi / talabga muvofiqlik / taqdimot.
 */

const LOYIHA = {
  "0-sinf": [
    { nom: "Eng uzoq yuradigan model",
      vazifa: "chorakdagi elastik yoki inersiyali modellardan birini tanlab, uni imkon qadar uzoq yuradigan qilib o'zgartirish",
      talab: ["Modelga kamida 1 ta o'zgartirish kiritilsin",
              "O'zgartirishdan oldingi va keyingi masofa o'lchab yozilsin"],
      savol: "Nima o'zgartirdingiz va masofa qanchaga o'zgardi?" },
    { nom: "O'zimning richagli qurilmam",
      vazifa: "richag qonunidan foydalanib, biror narsani ko'taradigan yoki qisadigan o'z qurilmangizni qurish",
      talab: ["Qurilmada tayanch nuqtasi aniq ko'rinsin",
              "Qurilma kamida 1 ta detalni ko'tara olsin"],
      savol: "Tayanch nuqtasini qayerga qo'ydingiz va nega aynan u yerga?" },
    { nom: "Mustahkam minora",
      vazifa: "iloji boricha baland, lekin turg'un konstruksiya qurish",
      talab: ["Minora o'z-o'zidan tik tursin (ushlab turilmasin)",
              "Konstruksiyada uchburchak ishlatilsin", "Balandligi o'lchab yozilsin"],
      savol: "Minorangiz qayeri eng kuchsiz edi?" },
    { nom: "Tezlashtirgich",
      vazifa: "tishli g'ildirak yoki shkiv uzatmasi qurib, chiqish qismini kirishdan tezroq aylantirish",
      talab: ["Kamida 2 ta tishli g'ildirak yoki shkiv ishlatilsin",
              "Kirish va chiqish aylanishlari sanab, nisbati yozilsin"],
      savol: "Tezlik oshganda kuch nima bo'ldi?" }
  ],

  "1-sinf": [
    { nom: "Harakatlanuvchi o'yinchoq",
      vazifa: "krivoship mexanizmiga o'z figurangizni qo'shib, harakatlanuvchi o'yinchoq yasash",
      talab: ["Qo'l aylantirilganda figura harakatlansin",
              "Mexanizm tiqilib qolmasin"],
      savol: "Figurangiz qanday harakat qiladi — tebranmami, aylanmami?" },
    { nom: "Ikki harakat bitta mexanizmda",
      vazifa: "bitta krivoshipdan ikki xil harakat chiqaradigan mexanizm qurish",
      talab: ["Ikkala harakat ham bir vaqtda ishlasin",
              "Harakatlar bir-biridan farq qilsin (masalan: biri yuqoriga-pastga, ikkinchisi oldinga-orqaga)"],
      savol: "Bitta aylanishdan ikki xil harakat qanday chiqdi?" },
    { nom: "Sozlanadigan mexanizm",
      vazifa: "tebranish kengligini foydalanuvchi o'zgartira oladigan mexanizm qurish",
      talab: ["Kamida 2 ta sozlash holati bo'lsin",
              "Har holatda tebranish kengligi o'lchab yozilsin"],
      savol: "Sozlashni qanday qildingiz — nimani surdingiz yoki almashtirdingiz?" },
    { nom: "Mexanizm teatri",
      vazifa: "yil davomida o'rgangan mexanizmlardan 2-3 tasini birlashtirib, kichik sahna yasash",
      talab: ["Kamida 2 ta turli mexanizm ishlatilsin", "Sahnada bir kichik voqea ko'rsatilsin",
              "Mexanizmlar bir vaqtda ishlasin"],
      savol: "Qaysi mexanizmni birlashtirish eng qiyin bo'ldi?" }
  ],

  "2-sinf": [
    { nom: "Ogohlantiruvchi qurilma",
      vazifa: "biror narsani sezib, ogohlantirish beradigan qurilma loyihalash",
      talab: ["Qurilma sensor bilan ishlasin", "Ogohlantirish aniq ko'rinsin yoki eshitilsin",
              "5 sinovdan kamida 4 tasida to'g'ri ishlasin"],
      savol: "Qurilmangiz qayerda kerak bo'lardi?" },
    { nom: "Ikki sensorli model",
      vazifa: "ikki xil signalga ikki xil javob beradigan model qurish",
      talab: ["Ikki sensor mustaqil ishlasin",
              "Javoblar bir-biridan farq qilsin", "Har javob sinab ko'rsatilsin"],
      savol: "Ikkala sensor bir vaqtda ishga tushsa nima bo'ladi?" },
    { nom: "Avtomatik ombor",
      vazifa: "yukni sezib, ko'tarib, boshqa joyga qo'yadigan tizim loyihalash",
      talab: ["Sezish va ko'tarish bosqichlari birga ishlasin",
              "Yuk tushib ketmasin", "Tizim 3 marta ketma-ket ishlasin"],
      savol: "Tizimingiz qaysi bosqichda eng ko'p xato qildi?" },
    { nom: "Maktabga robot",
      vazifa: "maktabdagi biror ishni yengillashtiradigan yuk ko'targich robot loyihalash",
      talab: ["Muammo bir gapda yozilsin", "Robot o'sha muammoni hal qilsin",
              "Ish vaqti o'lchab yozilsin"],
      savol: "Robotingiz odamga qancha vaqt tejaydi?" }
  ],

  "3-sinf": [
    { nom: "Motorli yordamchi",
      vazifa: "motor kuchidan foydalanadigan foydali qurilma loyihalash",
      talab: ["Qurilma motor bilan ishlasin", "Bajaradigan ishi aniq bo'lsin",
              "Uzatma tanlovi tushuntirilsin"],
      savol: "Motorni to'g'ridan-to'g'ri ulaganingizda va uzatma orqali ulaganingizda farq bormi?" },
    { nom: "Har yerda yuradigan mashina",
      vazifa: "uch xil sirtda ham yura oladigan transport loyihalash",
      talab: ["Uch sirtda sinalsin va natija jadvalga yozilsin",
              "Eng yomon natija bergan sirt uchun yaxshilanish kiritilsin"],
      savol: "Qaysi sirt eng qiyin bo'ldi va uni qanday yengdingiz?" },
    { nom: "Maxsus transport",
      vazifa: "aniq bir vazifa uchun mo'ljallangan transport loyihalash (tez yordam, yuk tashish, qutqaruv)",
      talab: ["Vazifa aniq yozilsin", "Transportda o'sha vazifaga xos kamida 1 ta qism bo'lsin",
              "2 metrlik trassada sinalsin"],
      savol: "Transportingizni oddiy mashinadan nima ajratib turadi?" },
    { nom: "Havo mashinasi",
      vazifa: "havo oqimi yoki reaktiv kuch bilan harakatlanadigan model loyihalash",
      talab: ["Model havo kuchi bilan siljisin", "Masofa o'lchab yozilsin",
              "Havo qarshiligini kamaytirish uchun kamida 1 ta o'zgartirish kiritilsin"],
      savol: "Shaklni o'zgartirganingiz masofaga qanday ta'sir qildi?" }
  ],

  "4-sinf": [
    { nom: "Mening bionik ixtirom",
      vazifa: "tabiatdagi biror moslashuvni texnikaga ko'chirib, o'z ixtirongizni qurish",
      talab: ["Qaysi jonzotdan nima olingani yozilsin",
              "Model harakatlansin", "Tabiiy yechim nega samarali ekani tushuntirilsin"],
      savol: "Tabiatdagi yechim texnikada ham shunday yaxshi ishladimi?" },
    { nom: "Yuradigan mexanizm",
      vazifa: "g'ildiraksiz, oyoq bilan yuradigan model loyihalash",
      talab: ["G'ildirak ishlatilmasin", "Model kamida 1 metr yursin",
              "Qadam tsikli tushuntirilsin"],
      savol: "Oyoq bilan yurish g'ildirakdan nimasi bilan yaxshi, nimasi bilan yomon?" },
    { nom: "Tadqiqot roboti",
      vazifa: "notekis yuzada harakatlanib, ma'lumot yoki namuna yig'adigan robot loyihalash",
      talab: ["Robot to'siqlardan o'tsin", "Namunani ola bilsin",
              "Missiya bosqichlari oldindan yozilsin"],
      savol: "Missiyangizda eng zaif bosqich qaysi edi?" },
    { nom: "Bitiruv loyihasi",
      vazifa: "o'zingiz tanlagan muammoni to'liq muhandislik tsikli bo'yicha hal qilish",
      talab: ["Talab yozilsin (robot nima qilishi kerak)", "Eskiz chizilsin",
              "Model qurilsin va sinalsin", "Sinov natijasiga ko'ra kamida 1 ta takomil kiritilsin",
              "Natija sinfga taqdim etilsin"],
      savol: "Birinchi variantingiz bilan oxirgi variantingiz orasida nima farq bor?" }
  ]
};

/* ---------------------------------------------------------------------
 * 2-YIL — doimiy, qiyinroq variant
 * ---------------------------------------------------------------------
 * Korpus uch sinfga siqilgani uchun (tools/taqsimot.js) chorak mavzulari
 * boshqacha. Talablar ham qattiqroq: 2-yilda deyarli har loyihada o'lchov
 * va taqqoslash talab qilinadi, "erkin ijod" bosqichi tugagan.
 */
const LOYIHA_2 = {
  "0-sinf": [
    { nom: "Aniq otuvchi mexanizm",
      vazifa: "elastik energiya bilan ishlaydigan, nishonga aniq tushadigan mexanizm loyihalash",
      talab: ["Mexanizm bir xil kuch bilan otsin (qo'l kuchi emas)",
              "3 marta otilib, uchala natija yozilsin", "Natijalar tarqoqligi 20 sm dan kam bo'lsin"],
      savol: "Natijalar nega har safar bir xil chiqmadi?" },
    { nom: "Ikki bosqichli uzatma",
      vazifa: "kirish aylanishini kamida 4 barobar tezlashtiradigan yoki sekinlashtiradigan uzatma qurish",
      talab: ["Kamida 2 bosqich bo'lsin", "Nisbat hisoblab yozilsin",
              "Konstruksiya yuk ostida egilmasin"],
      savol: "Nisbatni oshirganingizda nimani yo'qotdingiz?" },
    { nom: "Blokli yuk ko'targich",
      vazifa: "shkiv bloklari yordamida yukni yengil ko'taradigan qurilma loyihalash",
      talab: ["Kamida 2 shkiv ishlatilsin", "Bitta shkiv bilan va ikkita shkiv bilan tortish taqqoslansin",
              "Farq daftarga yozilsin"],
      savol: "Shkiv qo'shganingizda tortish yengillashdi, lekin nima uzaydi?" },
    { nom: "Ritmli mexanizm",
      vazifa: "belgilangan ritmda (masalan 1 soniyada 1 marta) tebranadigan mexanizm loyihalash",
      talab: ["Ritm sekundomer bilan tekshirilsin", "Mexanizm 30 soniya uzluksiz ishlasin",
              "Ritmni o'zgartirish usuli ko'rsatilsin"],
      savol: "Ritmni nima belgilaydi — uzatmami, krivoship radiusimi?" }
  ],

  "1-sinf": [
    { nom: "Ritm mashinasi",
      vazifa: "ikki xil ritmda ishlaydigan, foydalanuvchi ritmni almashtira oladigan mexanizm loyihalash",
      talab: ["Ikki ritm aniq farq qilsin", "Almashtirish 5 soniyada bajarilsin",
              "Har ritm o'lchab yozilsin"],
      savol: "Ritmni almashtirganda amplituda ham o'zgardimi?" },
    { nom: "Sensorli yordamchi",
      vazifa: "aniq bir vazifani sensor yordamida avtomatik bajaradigan qurilma loyihalash",
      talab: ["Vazifa bir gapda yozilsin", "10 sinovdan kamida 8 tasi to'g'ri chiqsin",
              "Sensor xato qilgan holat tahlil qilinsin"],
      savol: "Sensor qaysi sharoitda ishonchsiz bo'lib qoladi?" },
    { nom: "Kran loyihasi",
      vazifa: "yukni ko'tarib, aylantirib, boshqa joyga qo'yadigan kran loyihalash",
      talab: ["Kran kamida 15 sm balandlikka ko'tarsin", "Strela aylansin yoki uzaysin",
              "Kontr-vazn hisobga olinsin", "Yuk 3 marta ketma-ket tashilsin"],
      savol: "Kraningiz qanday og'irlikda ag'darila boshlaydi?" },
    { nom: "Maxsus yurar transport",
      vazifa: "aniq bir sharoit uchun mo'ljallangan motorli transport loyihalash (qiyalik, notekis sirt, og'ir yuk)",
      talab: ["Sharoit oldindan tanlansin va yozilsin", "Transport o'sha sharoitda sinalsin",
              "Oddiy transport bilan taqqoslansin"],
      savol: "Maxsus qismingiz haqiqatan yordam berdimi — raqam bilan isbotlang" }
  ],

  "2-sinf": [
    { nom: "Vazifaga mo'ljallangan transport",
      vazifa: "tanlangan vazifa uchun to'liq transport tizimi loyihalash (qutqaruv, yuk tashish, patrul)",
      talab: ["Vazifa va talablar ro'yxati yozilsin", "Transportda kamida 2 ta maxsus qism bo'lsin",
              "3 metrlik trassada sinalsin", "Natija talablarga solishtirilsin"],
      savol: "Qaysi talab bajarilmay qoldi va nega?" },
    { nom: "Uchar model",
      vazifa: "havo kuchi bilan harakatlanadigan model loyihalash va uning tortish kuchini oshirish",
      talab: ["Boshlang'ich tortish kuchi o'lchansin", "Bitta o'zgartirish kiritilsin",
              "Yangi natija o'lchansin va taqqoslansin"],
      savol: "O'zgartirishingiz tortish kuchini necha foizga oshirdi?" },
    { nom: "Bionik robot",
      vazifa: "tabiatdagi harakat usulini takrorlaydigan robot loyihalash",
      talab: ["Qaysi jonzot va qaysi harakat — yozilsin", "Robot o'sha harakatni bajarsin",
              "Tabiiy yechim bilan robot yechimi taqqoslansin", "Kamida 1,5 metr harakatlansin"],
      savol: "Tabiat bu masalani sizdan qanday farqli hal qilgan?" },
    { nom: "Kosmik missiya (bitiruv)",
      vazifa: "o'zingiz tuzgan kosmik missiyani to'liq muhandislik tsikli bo'yicha hal qilish",
      talab: ["Missiya bosqichlari yozilsin", "Eskiz chizilsin", "Rover qurilsin va sinalsin",
              "Sinov natijasiga ko'ra kamida 2 ta takomil kiritilsin",
              "Natija va o'lchovlar bilan sinfga taqdim etilsin"],
      savol: "Qaysi takomil eng katta farq berdi — buni qanday o'lchadingiz?" }
  ]
};

function loyihaDarsi(yil, sinf, chorakNo) {
  const jadval = (yil === "2-yil" && LOYIHA_2[sinf]) ? LOYIHA_2 : LOYIHA;
  const p = (jadval[sinf] || [])[chorakNo - 1];
  if (!p) return null;

  const yakuniy = chorakNo === 4;
  const sarlavha = chorakNo + '-chorak loyihasi' + (yakuniy ? ' (yil yakuni)' : '') +
    ': "' + p.nom + '" — ' + p.vazifa;

  return {
    nom: sarlavha,
    kontent: {
      maqsad: [
        'O\'quvchilar "' + p.nom + '" loyihasi doirasida ' + p.vazifa + '.',
        'O\'quvchilar oldindan berilgan talablarga javob beradigan yechim qurish tajribasini oladilar.',
        'O\'quvchilar o\'z loyihasini sinfga taqdim etib, qabul qilgan qarorlarini asoslaydilar.'
      ],
      lugat: [
        'Loyiha (Project) – aniq maqsadga qaratilgan mustaqil ish',
        'Talab (Requirement) – loyiha albatta bajarishi kerak bo\'lgan shart',
        'Eskiz (Sketch) – qurishdan oldin chiziladigan qo\'lda chizma',
        'Taqdimot (Presentation) – o\'z ishini boshqalarga ko\'rsatib tushuntirish',
        'Asoslash (Justification) – nima uchun shunday qilganini dalil bilan aytish'
      ],
      softSkill: 'Mustaqillik va tashabbus — O\'qituvchidan tayyor javob kutmasdan, o\'z yechimingizni sinab ko\'rish. Ishlamasa — boshqasini sinash.',
      resurslar: [
        'Makerzoid Robot Master Standard to\'plami',
        'Chorak davomida o\'rganilgan modellarning instruksiyalari (g\'oya olish uchun)',
        'Eskiz chizish uchun daftar va qalam',
        'O\'lchov lentasi va sekundomer (sinov uchun)'
      ],
      nazariya: [
        {
          title: '5.1. Loyiha talabi (5 daqiqa)',
          points: ['Topshiriq e\'lon qilinadi: ' + p.vazifa + '.']
            .concat(p.talab.map(t => 'Talab: ' + t + '.'))
        },
        {
          title: '5.2. Eskiz (5 daqiqa)',
          points: [
            'Har bir o\'quvchi qurishdan OLDIN g\'oyasini daftarga chizadi.',
            'Eskizda qaysi qism nima qilishi belgilanadi.',
            'O\'qituvchi eskizlarni ko\'rib chiqib, talablarga mos kelishini tekshiradi.'
          ]
        }
      ],
      amaliy: [
        {
          title: '6.1. Qurish (22 daqiqa)',
          points: [
            'O\'quvchilar eskiz bo\'yicha o\'z loyihasini quradilar.',
            'Ishlamagan yechim o\'zgartiriladi — bu normal, eskizga tuzatish kiritish mumkin.'
          ]
        },
        {
          title: '6.2. Sinov (8 daqiqa)',
          points: [
            'Loyiha talablar bo\'yicha sinaladi va natija daftarga yoziladi.',
            'Talab bajarilmasa, bitta tuzatish kiritib qayta sinaladi.'
          ]
        },
        {
          title: '6.3. Taqdimot (10 daqiqa)',
          points: [
            'Har bir o\'quvchi loyihasini ko\'rsatib, talablarni qanday bajarganini aytadi.',
            'Asosiy savol: ' + p.savol
          ]
        }
      ],
      uyga: [
        'Loyihangizning rasmini chizib yoki fotosini olib, unga yana qanday funksiya qo\'shish mumkinligini yozing.',
        'Sinfdagi boshqa bitta loyihani tanlab, undan nimani o\'rganganingizni bir gapda yozing.'
      ]
    }
  };
}

module.exports = { faol: true, LOYIHA, LOYIHA_2, loyihaDarsi };
