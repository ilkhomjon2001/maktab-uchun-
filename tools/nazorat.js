/*
 * CHORAK NAZORAT ISHLARI — har sinf uchun alohida
 * ===============================================
 * MUAMMO: bazada nazorat ishi matni beshala sinfda BIR XIL edi —
 *   1-chorak "RoboRace", 2-chorak "RoboLift", 3-chorak "RoboSense",
 *   4-chorak "RoboChampionship" (20 ta darsda 4 ta matn).
 * Model taqsimotidan keyin ular chorak mazmuniga ham to'g'ri kelmay qoldi:
 *   0-sinf 3-choragi geometrik shakllar haqida, nazorat esa sensorli
 *   robot talab qilardi — sinfda sensor umuman yo'q.
 *
 * YECHIM: har sinfning har choragi uchun O'SHA chorak mavzusidan kelib
 * chiqadigan alohida musobaqa. Bola 0-sinfda "Rezina-Yurish" da qatnashsa,
 * 1-sinfda "Krivoship-Usta" da qatnashadi — bir xil topshiriq qaytmaydi.
 *
 * Baholash 5 pog'onali: 5 / 4 / 3 / 2 / FAILED (asosiy bazadagi kabi).
 */

// Har chorakda takrorlanadigan soft skill (chorak bo'yicha, sinf bo'yicha emas)
const SOFT = [
  "Sportchan munosabat — g'alaba va mag'lubiyatga sog'lom qarash, boshqalarning natijasini olqishlash. Yutqazish ham o'rganishning bir qismi.",
  "Vaqtni boshqarish — Musobaqagacha tayyorgarlikni ulgurish, oxirgi daqiqaga qoldirmaslik.",
  "Bosim ostida ishlash — Hamma qarab turganda ham xotirjam ishlash, xato bo'lsa vahima qilmaslik.",
  "Mas'uliyat va o'zini baholash — Yil yakunida o'z natijasini haqqoniy baholay olish, kuchli va kuchsiz tomonini aytish."
];

const UMUMIY_LUGAT = [
  "Musobaqa (Competition) – g'olibni aniqlash uchun o'tkaziladigan raqobat",
  "Baholash mezoni (Grading criteria) – natijani baholash uchun oldindan belgilangan qoidalar"
];

/*
 * Har yozuv:
 *   nom     — musobaqa nomi
 *   vazifa  — bola nima qilishi kerakligi (bitta gap)
 *   olchov  — nima o'lchanadi
 *   mezon   — 5 pog'ona (5 / 4 / 3 / 2 / FAILED)
 *   jihoz   — chorakka xos qo'shimcha jihoz
 *   lugat   — chorakka xos 3 ta atama
 *   savol   — tahlil bosqichidagi asosiy savol
 */
const NAZORAT = {
  "0-sinf": [
    {
      nom: "Rezina-Yurish",
      vazifa: "elastik yoki pull-back mexanizmli model start chizig'idan turtkisiz jo'natiladi va bosib o'tgan masofasi o'lchanadi",
      olchov: "bosib o'tilgan masofa",
      mezon: ["3 metrdan uzoq = 5 (a'lo)", "2–3 metr = 4 (yaxshi)", "1–2 metr = 3 (qoniqarli)",
              "0,5–1 metr = 2 (qoniqarsiz)", "0,5 metrdan kam yoki model yo'lda tarqalib ketsa = FAILED"],
      jihoz: ["3 metrlik o'lchov lentasi bilan belgilangan tekis yo'lak", "Start chizig'i uchun rangli lenta"],
      lugat: ["Elastik energiya (Elastic energy) – cho'zilgan yoki siqilgan jismda to'planadigan energiya",
              "Inersiya (Inertia) – harakatdagi jismning harakatini davom ettirishga intilishi",
              "Start (Start line) – harakat boshlanadigan chiziq"],
      savol: "Modelingiz nega aynan shu masofani bosib o'tdi — nima ko'proq ta'sir qildi?"
    },
    {
      nom: "Richag-Kuch",
      vazifa: "richagli model yordamida stol ustidagi yukni ko'taradi; tayanch nuqtasini surib, eng kam kuch bilan ko'tarish holati topiladi",
      olchov: "ko'tarilgan yuk og'irligi va tayanch nuqtasi to'g'ri tanlanganligi",
      mezon: ["3 va undan ko'p detal-yukni ko'tarsa va tayanch nuqtasini to'g'ri tushuntirsa = 5 (a'lo)",
              "2 detal-yukni ko'tarsa = 4 (yaxshi)", "1 detal-yukni ko'tarsa = 3 (qoniqarli)",
              "Richag ishlaydi, lekin yuk ko'tarilmasa = 2 (qoniqarsiz)",
              "Richag mexanizmi yig'ilmagan bo'lsa = FAILED"],
      jihoz: ["Yuk sifatida bir xil og'irlikdagi detallar to'plami", "Tayanch nuqtasini surish uchun qo'shimcha bloklar"],
      lugat: ["Richag (Lever) – tayanch nuqtasi atrofida aylanadigan qattiq sterjen",
              "Tayanch nuqtasi (Fulcrum) – richag aylanadigan nuqta",
              "Kuch yelkasi (Effort arm) – kuch qo'yiladigan nuqtadan tayanchgacha masofa"],
      savol: "Tayanch nuqtasini surganingizda ko'tarish osonlashdimi yoki qiyinlashdimi — nega?"
    },
    {
      nom: "Mustahkam Ko'prik",
      vazifa: "o'quvchi 20 sm oraliqni bosib o'tadigan konstruksiya quradi va uning ustiga bosqichma-bosqich yuk qo'yiladi",
      olchov: "konstruksiya buzilgunga qadar ko'targan yuk miqdori",
      mezon: ["5 va undan ko'p detal-yukni ko'tarsa va uchburchak ishlatgan bo'lsa = 5 (a'lo)",
              "3–4 detal-yukni ko'tarsa = 4 (yaxshi)", "1–2 detal-yukni ko'tarsa = 3 (qoniqarli)",
              "Konstruksiya turadi, lekin yuk ko'tarmasa = 2 (qoniqarsiz)",
              "Konstruksiya 20 sm oraliqni bosib o'tmasa = FAILED"],
      jihoz: ["20 sm oraliq hosil qilish uchun ikkita bir xil balandlikdagi tayanch", "Bir xil og'irlikdagi yuk detallari"],
      lugat: ["Mustahkamlik (Rigidity) – konstruksiyaning shaklini saqlash qobiliyati",
              "Uchburchak (Triangle) – shaklini o'zgartirmaydigan yagona ko'pburchak",
              "Deformatsiya (Deformation) – yuk ostida shaklning o'zgarishi"],
      savol: "Ko'prigingiz qayeridan buzildi — o'sha joyni qanday mustahkamlash mumkin edi?"
    },
    {
      nom: "Tezlik va Kuch",
      vazifa: "tishli g'ildirak yoki shkiv uzatmasi qurib, bir xil qo'l aylanishida chiqish g'ildiragi necha marta aylanishini ko'rsatadi va tushuntiradi",
      olchov: "uzatma nisbati to'g'ri qurilgani va tushuntirilgani",
      mezon: ["Uzatmani quradi, nisbatni o'lchaydi va nega tezlik/kuch o'zgarganini tushuntiradi = 5 (a'lo)",
              "Uzatmani quradi va nisbatni o'lchaydi = 4 (yaxshi)",
              "Uzatmani quradi, u aylanadi = 3 (qoniqarli)",
              "Tishli g'ildiraklar ulangan, lekin aylanmasa = 2 (qoniqarsiz)",
              "Uzatma yig'ilmagan bo'lsa = FAILED"],
      jihoz: ["Turli o'lchamdagi tishli g'ildiraklar va shkivlar", "Aylanishlarni sanash uchun rangli belgi (stiker)"],
      lugat: ["Uzatma nisbati (Gear ratio) – kirish va chiqish aylanishlari soni nisbati",
              "Shkiv (Pulley) – tasma orqali kuch uzatuvchi g'ildirak",
              "Moment (Torque) – aylantiruvchi kuch"],
      savol: "Katta g'ildirak kichigini aylantirganda tezlik oshdimi yoki kuch oshdimi?"
    }
  ],

  "1-sinf": [
    {
      nom: "Mexanizm-Detektiv",
      vazifa: "o'quvchi qo'l bilan aylantiriladigan mexanizm quradi va uning qaysi qismi aylanma, qaysi qismi tebranma harakat qilishini ko'rsatib beradi",
      olchov: "mexanizm ishlashi va qismlarning to'g'ri nomlanishi",
      mezon: ["Mexanizm silliq ishlaydi va 3 ta qismni to'g'ri nomlaydi = 5 (a'lo)",
              "Mexanizm ishlaydi va 2 ta qismni nomlaydi = 4 (yaxshi)",
              "Mexanizm ishlaydi = 3 (qoniqarli)",
              "Mexanizm yig'ilgan, lekin tiqilib qoladi = 2 (qoniqarsiz)",
              "Mexanizm yig'ilmagan bo'lsa = FAILED"],
      jihoz: ["Mexanizm qismlari nomi yozilgan kartochkalar", "Namoyish uchun stol maydoni"],
      lugat: ["Aylanma harakat (Rotary motion) – o'q atrofida aylanish",
              "Tebranma harakat (Oscillating motion) – oldinga-orqaga takrorlanuvchi harakat",
              "Mexanizm (Mechanism) – harakatni uzatuvchi va o'zgartiruvchi qismlar tizimi"],
      savol: "Aylanma harakat qaysi qismda tebranma harakatga aylandi?"
    },
    {
      nom: "Krivoship-Usta",
      vazifa: "krivoship-shatun mexanizmi qurib, 30 soniya davomida uzluksiz aylantiradi; mexanizm necha marta to'liq tebranish berishi sanaladi",
      olchov: "30 soniyadagi to'liq tebranishlar soni va mexanizmning uzilmasligi",
      mezon: ["25 va undan ko'p tebranish, uzilishsiz = 5 (a'lo)", "15–24 tebranish = 4 (yaxshi)",
              "8–14 tebranish = 3 (qoniqarli)", "1–7 tebranish yoki mexanizm ikki marta uzilsa = 2 (qoniqarsiz)",
              "Mexanizm umuman tebranmasa = FAILED"],
      jihoz: ["Sekundomer", "Tebranishlarni sanash uchun juftlik (bir bola aylantiradi, ikkinchisi sanaydi)"],
      lugat: ["Krivoship (Crank) – aylanma harakatni beruvchi bukilgan o'q",
              "Shatun (Connecting rod) – krivoshipni ishchi qismga ulovchi sterjen",
              "Tebranish (Oscillation) – bir marta oldinga va orqaga qaytish"],
      savol: "Mexanizmingiz qayerda tiqilib qoldi — sabab shatunning uzunligimi yoki biriktirishmi?"
    },
    {
      nom: "Amplituda-Aniqlik",
      vazifa: "o'quvchi krivoship radiusini o'zgartirib, mexanizmning tebranish kengligini belgilangan nishonga (10 sm) moslashtiradi",
      olchov: "tebranish kengligining nishondan farqi",
      mezon: ["Farq 1 sm dan kam = 5 (a'lo)", "Farq 1–2 sm = 4 (yaxshi)", "Farq 2–4 sm = 3 (qoniqarli)",
              "Farq 4–7 sm = 2 (qoniqarsiz)", "Farq 7 sm dan ko'p yoki sozlash umuman qilinmasa = FAILED"],
      jihoz: ["O'lchov lentasi yoki chizg'ich", "10 sm nishon belgisi qo'yilgan taxta yoki qog'oz"],
      lugat: ["Amplituda (Amplitude) – tebranishning eng katta kengligi",
              "Radius (Radius) – markazdan chetgacha masofa",
              "Sozlash (Adjustment) – natijani nishonga yaqinlashtirish uchun o'zgartirish kiritish"],
      savol: "Radiusni kattalashtirsangiz amplituda qanday o'zgardi — qaysi tomonga?"
    },
    {
      nom: "Mexanizm-Chempionati",
      vazifa: "yil davomida o'rgangan mexanizmlardan birini tanlab qurib, uning harakatini sinfga tushuntiradi va bitta yaxshilanish kiritganini ko'rsatadi",
      olchov: "mexanizmning ishlashi, tushuntirish sifati va kiritilgan yaxshilanish",
      mezon: ["Mexanizm ishlaydi, tushuntiradi va yaxshilanishni asoslaydi = 5 (a'lo)",
              "Mexanizm ishlaydi va tushuntiradi = 4 (yaxshi)",
              "Mexanizm ishlaydi = 3 (qoniqarli)",
              "Mexanizm qisman ishlaydi = 2 (qoniqarsiz)",
              "Mexanizm yig'ilmagan bo'lsa = FAILED"],
      jihoz: ["Taqdimot uchun stol", "Yil davomidagi barcha instruksiyalar (tanlash uchun)"],
      lugat: ["Taqdimot (Presentation) – o'z ishini boshqalarga ko'rsatib tushuntirish",
              "Takomillashtirish (Improvement) – mavjud yechimni yaxshilash",
              "Asoslash (Justification) – nima uchun shunday qilganini dalil bilan aytish"],
      savol: "Kiritgan yaxshilanishingiz natijani o'zgartirdimi — buni qanday tekshirdingiz?"
    }
  ],

  "2-sinf": [
    {
      nom: "Sensor-Test",
      vazifa: "sensorli model qurib, sensorga 5 marta signal beriladi; model har safar to'g'ri javob berishi kerak",
      olchov: "5 sinovdan nechtasida model to'g'ri ishlagani",
      mezon: ["5/5 to'g'ri = 5 (a'lo)", "4/5 to'g'ri = 4 (yaxshi)", "3/5 to'g'ri = 3 (qoniqarli)",
              "1–2/5 to'g'ri = 2 (qoniqarsiz)", "Sensor umuman javob bermasa = FAILED"],
      jihoz: ["Sensorni ishga tushirish uchun signal manbai (qo'l, karta, chiroq)", "Natija jadvali"],
      lugat: ["Sensor (Sensor) – atrof-muhitdagi o'zgarishni sezuvchi qism",
              "Signal (Signal) – sensorga tushadigan ta'sir",
              "Javob (Response) – model signalga qanday harakat bilan javob berishi"],
      savol: "Sensor qaysi holatda xato qildi — sabab masofami, yorug'likmi?"
    },
    {
      nom: "Aqlli Model",
      vazifa: "model uch xil turli signalga uch xil javob berishi kerak (masalan: to'xtash, orqaga qaytish, ovoz/chiroq)",
      olchov: "to'g'ri ishlagan javoblar soni",
      mezon: ["3 xil javob ham to'g'ri = 5 (a'lo)", "2 xil javob to'g'ri = 4 (yaxshi)",
              "1 xil javob to'g'ri = 3 (qoniqarli)", "Javoblar chalkash ishlasa = 2 (qoniqarsiz)",
              "Model signalga umuman javob bermasa = FAILED"],
      jihoz: ["Uch xil signal berish uchun jihoz (to'siq, rangli karta, chiroq)", "Sinov maydoni"],
      lugat: ["Shart (Condition) – qaysi holatda qaysi javob berilishi",
              "Ketma-ketlik (Sequence) – harakatlarning tartibi",
              "Sozlash (Calibration) – sensorni to'g'ri ishlashi uchun moslash"],
      savol: "Ikki signal bir vaqtda kelsa, model nima qiladi?"
    },
    {
      nom: "Sensor va Yuk",
      vazifa: "model to'siqni sensor bilan aniqlab to'xtaydi, so'ng yukni ko'tarib 50 sm masofaga tashiydi",
      olchov: "to'siqni aniqlash va yukni tashish bosqichlari bajarilgani",
      mezon: ["Ikkala bosqich ham to'g'ri, yuk tushmasa = 5 (a'lo)",
              "Ikkala bosqich bajarildi, yuk bir marta tushdi = 4 (yaxshi)",
              "Faqat bitta bosqich bajarildi = 3 (qoniqarli)",
              "Bosqichlar boshlandi, lekin tugamadi = 2 (qoniqarsiz)",
              "Model harakatlanmasa = FAILED"],
      jihoz: ["To'siq (quti yoki devor)", "Ko'tarish uchun yuk", "50 sm belgilangan yo'lak"],
      lugat: ["To'siq (Obstacle) – yo'ldagi to'sqinlik",
              "Yuk (Load) – ko'tarilishi kerak bo'lgan og'irlik",
              "Bosqich (Stage) – topshiriqning bir qismi"],
      savol: "Model to'siqni juda kech aniqladimi — sensorni qayerga ko'chirish kerak edi?"
    },
    {
      nom: "RoboLift",
      vazifa: "yuk ko'targich robot bir xil yukni belgilangan balandlikka ko'taradi va 1 metr masofaga tashiydi; vaqt o'lchanadi",
      olchov: "topshiriqni bajarish vaqti",
      mezon: ["30 soniyagacha = 5 (a'lo)", "31–60 soniya = 4 (yaxshi)", "61–90 soniya = 3 (qoniqarli)",
              "91–120 soniya = 2 (qoniqarsiz)", "2 daqiqadan ortiq yoki yuk tashilmasa = FAILED"],
      jihoz: ["Sekundomer", "Standart yuk (kubik yoki detal to'plami)", "1 metrlik belgilangan trassa"],
      lugat: ["Manipulyator (Manipulator) – yukni ushlaydigan va ko'taradigan qism",
              "Barqarorlik (Stability) – yuk bilan yiqilmay harakatlanish",
              "Samaradorlik (Efficiency) – natijani kam vaqt va kuch bilan olish"],
      savol: "Yuk og'irlashsa, robotingiz qayeridan nosozlik beradi?"
    }
  ],

  "3-sinf": [
    {
      nom: "Motor-Start",
      vazifa: "motorli model o'z kuchi bilan 2 metr masofani bosib o'tadi; vaqt o'lchanadi",
      olchov: "2 metrni bosib o'tish vaqti",
      mezon: ["10 soniyagacha = 5 (a'lo)", "11–25 soniya = 4 (yaxshi)", "26–45 soniya = 3 (qoniqarli)",
              "46–60 soniya = 2 (qoniqarsiz)", "60 soniyadan ortiq yoki finishga yetmasa = FAILED"],
      jihoz: ["2 metrlik to'g'ri trassa", "Sekundomer", "Zaxira batareyalar"],
      lugat: ["Motor (Motor) – elektr energiyasini aylanma harakatga aylantiruvchi qism",
              "Moment (Torque) – motorning aylantiruvchi kuchi",
              "Uzatma (Transmission) – motor harakatini g'ildirakka yetkazuvchi tizim"],
      savol: "Modelingiz sekin yurdimi yoki tez — buni motor uzatmasi bilan qanday bog'laysiz?"
    },
    {
      nom: "Ishqalanish-Sinovi",
      vazifa: "bitta model uch xil sirtda (silliq stol, gilam, qog'oz) sinaladi va har birida bosib o'tgan masofasi yoziladi",
      olchov: "uch sinov o'tkazilgani va farq to'g'ri tushuntirilgani",
      mezon: ["Uch sinov ham o'tkazilib, jadval to'ldiriladi va farq tushuntiriladi = 5 (a'lo)",
              "Uch sinov o'tkazilib, jadval to'ldiriladi = 4 (yaxshi)",
              "Ikki sinov o'tkaziladi = 3 (qoniqarli)",
              "Bitta sinov o'tkaziladi = 2 (qoniqarsiz)",
              "Model harakatlanmasa = FAILED"],
      jihoz: ["Uch xil sirt (stol, gilam parchasi, qog'oz varaq)", "O'lchov lentasi", "Natija jadvali"],
      lugat: ["Ishqalanish (Friction) – sirtlar orasidagi harakatga qarshilik",
              "Sirt (Surface) – model harakatlanadigan yuza",
              "Taqqoslash (Comparison) – natijalarni yonma-yon qo'yib xulosa chiqarish"],
      savol: "Qaysi sirtda model eng uzoq yurdi va nega aynan o'sha sirtda?"
    },
    {
      nom: "RoboRace",
      vazifa: "model 2,5 metrlik trassani bosib o'tadi; trassada kamida bitta burilish va bitta to'siq bor",
      olchov: "trassani bosib o'tish vaqti va to'siqqa tegmaganligi",
      mezon: ["20 soniyagacha, to'siqqa tegmasdan = 5 (a'lo)", "21–40 soniya = 4 (yaxshi)",
              "41–70 soniya = 3 (qoniqarli)", "71–100 soniya yoki to'siqqa 2 marta tegsa = 2 (qoniqarsiz)",
              "Finishga yetib bormasa = FAILED"],
      jihoz: ["2,5 metrlik burilishli trassa", "To'siq", "Sekundomer"],
      lugat: ["Trassa (Track) – belgilangan harakat yo'li",
              "Burilish radiusi (Turning radius) – robot burila oladigan eng kichik aylana",
              "Boshqaruv (Control) – robot yo'nalishini boshqarish"],
      savol: "Burilishda modelingiz nega sekinlashdi — g'ildiraklar joylashuvi qanday ta'sir qildi?"
    },
    {
      nom: "Havo-Chempionati",
      vazifa: "havo oqimi yoki reaktiv kuch bilan harakatlanadigan model quriladi va uning uchish/siljish masofasi o'lchanadi",
      olchov: "bosib o'tilgan masofa va modelning barqarorligi",
      mezon: ["4 metrdan uzoq va to'g'ri yo'nalishda = 5 (a'lo)", "2,5–4 metr = 4 (yaxshi)",
              "1,5–2,5 metr = 3 (qoniqarli)", "0,5–1,5 metr = 2 (qoniqarsiz)",
              "0,5 metrdan kam yoki model boshqarib bo'lmaydigan holda aylansa = FAILED"],
      jihoz: ["5 metrlik ochiq maydon", "O'lchov lentasi", "Havo oqimi manbai (propeller yoki puflagich)"],
      lugat: ["Aerodinamika (Aerodynamics) – havo oqimining jismga ta'siri",
              "Reaktiv kuch (Thrust) – havo yoki gaz otilishidan hosil bo'ladigan itaruvchi kuch",
              "Qarshilik (Drag) – havoning harakatga qarshiligi"],
      savol: "Modelingizning qaysi qismi havo qarshiligini eng ko'p oshirdi?"
    }
  ],

  "4-sinf": [
    {
      nom: "Bionika-Taqdimot",
      vazifa: "tabiatdagi biror jonzotdan ilhomlangan model qurib, qaysi hayvondan nimani olganini va nega shunday qilganini sinfga tushuntiradi",
      olchov: "modelning ishlashi va biologik o'xshatishning asoslanishi",
      mezon: ["Model harakatlanadi va 2 ta aniq o'xshatish asoslanadi = 5 (a'lo)",
              "Model harakatlanadi va 1 ta o'xshatish asoslanadi = 4 (yaxshi)",
              "Model harakatlanadi = 3 (qoniqarli)",
              "Model yig'ilgan, lekin harakatlanmasa = 2 (qoniqarsiz)",
              "Model yig'ilmagan bo'lsa = FAILED"],
      jihoz: ["Taqdimot uchun stol", "Hayvonlar rasmlari yoki qisqa video (taqqoslash uchun)"],
      lugat: ["Biomimikriya (Biomimicry) – tabiatdagi yechimlarni texnikaga ko'chirish",
              "Moslashuv (Adaptation) – jonzotning muhitga moslashgan xususiyati",
              "Analogiya (Analogy) – ikki narsa orasidagi o'xshashlik"],
      savol: "Tabiatdagi yechim nega aynan shunday — u qanday muammoni hal qiladi?"
    },
    {
      nom: "Yurish-Musobaqasi",
      vazifa: "g'ildiraksiz, oyoqli model 1,5 metr masofani bosib o'tadi; yiqilsa qaytadan qo'yiladi va urinish sanaladi",
      olchov: "masofani bosib o'tish vaqti va yiqilishlar soni",
      mezon: ["Yiqilmasdan bosib o'tsa = 5 (a'lo)", "1 marta yiqilsa = 4 (yaxshi)",
              "2–3 marta yiqilsa = 3 (qoniqarli)", "4–6 marta yiqilsa = 2 (qoniqarsiz)",
              "Model yura olmasa yoki g'ildirak ishlatilsa = FAILED"],
      jihoz: ["1,5 metrlik tekis yo'lak", "Sekundomer", "Yiqilishlarni sanash varaqasi"],
      lugat: ["Qadam tsikli (Gait cycle) – oyoqlarning takrorlanuvchi harakat tartibi",
              "Tayanch nuqtalari (Points of contact) – yerga tegib turgan oyoqlar",
              "Statik barqarorlik (Static stability) – to'xtaganda ham yiqilmaslik"],
      savol: "Modelingiz nechta oyoq bilan yerga tayanib turdi — bu barqarorlikka qanday ta'sir qildi?"
    },
    {
      nom: "Notekis Yo'l",
      vazifa: "model notekis yuzadan (to'siqlar, qiyalik, g'adir-budir sirt) 1,5 metr masofani bosib o'tadi",
      olchov: "bosib o'tilgan masofa va to'siqlardan o'ta olgani",
      mezon: ["Barcha to'siqlardan o'tib, finishga yetsa = 5 (a'lo)",
              "1 ta to'siqda qoqilib, keyin o'tsa = 4 (yaxshi)",
              "Masofaning yarmidan ko'pini bosib o'tsa = 3 (qoniqarli)",
              "Masofaning yarmidan kamini bosib o'tsa = 2 (qoniqarsiz)",
              "Birinchi to'siqdan o'ta olmasa = FAILED"],
      jihoz: ["Notekis maydon: kitoblar, qiyalik taxta, g'adir-budir mato", "O'lchov lentasi"],
      lugat: ["Klirens (Ground clearance) – model tagi bilan yer orasidagi masofa",
              "Ilashish (Traction) – g'ildirak yoki oyoqning yuzaga yopishishi",
              "Osma tizim (Suspension) – zarbani yumshatuvchi qism"],
      savol: "Model qayerda qoqildi — klirens yetmadimi yoki ilashish kam edimi?"
    },
    {
      nom: "Mars-Missiya",
      vazifa: "rover notekis maydondan o'tib, belgilangan nuqtadagi namunani (detal) olib, start nuqtasiga qaytadi",
      olchov: "missiya bosqichlarining bajarilishi va umumiy vaqt",
      mezon: ["Namunani olib qaytsa, 2 daqiqadan kam vaqtda = 5 (a'lo)",
              "Namunani olib qaytsa, 2–4 daqiqada = 4 (yaxshi)",
              "Namunani olsa, lekin qaytmasa = 3 (qoniqarli)",
              "Nuqtaga yetsa, lekin namunani ololmasa = 2 (qoniqarsiz)",
              "Nuqtaga yetib bormasa = FAILED"],
      jihoz: ["Notekis \"Mars\" maydoni", "Namuna sifatida rangli detal", "Sekundomer"],
      lugat: ["Missiya (Mission) – aniq maqsadli topshiriqlar ketma-ketligi",
              "Rover (Rover) – sayyora yuzasida harakatlanuvchi tadqiqot roboti",
              "Manipulyator (Manipulator) – namunani olish uchun ishlatiladigan qism"],
      savol: "Missiyaning qaysi bosqichi eng ko'p vaqt oldi — uni qanday tezlashtirish mumkin?"
    }
  ]
};

/* ---------------------------------------------------------------------
 * 2-YIL — doimiy, qiyinroq variant
 * ---------------------------------------------------------------------
 * 2-yilda korpus uch sinfga siqilgan (tools/taqsimot.js), shuning uchun
 * chorak mavzulari boshqacha va nazorat ishlari ham alohida. Bundan
 * tashqari ular 1-yil musobaqalaridan FARQ QILISHI shart: 1-yil 0-sinfni
 * o'qigan bola keyingi yil 2-yil 1-sinfga o'tadi.
 *
 * 2-yil musobaqalari qiyinroq mezon bo'yicha: eng uzoq/eng tez emas,
 * balki ANIQLIK, takroriylik va bir necha bosqichni birga bajarish.
 */
const NAZORAT_2 = {
  "0-sinf": [
    {
      nom: "Aniq-Masofa",
      vazifa: "elastik yoki pull-back model start chizig'idan jo'natiladi va 2 metrda belgilangan 30 sm kenglikdagi nishon zonasida to'xtashi kerak",
      olchov: "nishon zonasi markazidan chetlanish",
      mezon: ["Chetlanish 10 sm dan kam = 5 (a'lo)", "10–20 sm = 4 (yaxshi)", "20–40 sm = 3 (qoniqarli)",
              "40–70 sm = 2 (qoniqarsiz)", "70 sm dan ko'p yoki model qo'zg'almasa = FAILED"],
      jihoz: ["2 metrlik yo'lak va 30 sm kenglikdagi nishon zonasi (lenta bilan)", "O'lchov lentasi"],
      lugat: ["Aniqlik (Accuracy) – natijaning nishonga qanchalik yaqinligi",
              "Sozlash (Adjustment) – natijani nishonga yaqinlashtirish uchun o'zgartirish",
              "Elastik energiya (Elastic energy) – cho'zilgan jismda to'planadigan energiya"],
      savol: "Nishondan o'tib ketdingizmi yoki yetib bormadingizmi — nimani o'zgartirish kerak edi?"
    },
    {
      nom: "Uzatma-Nisbati",
      vazifa: "ikki bosqichli tishli uzatma qurib, kirish va chiqish aylanishlari nisbatini o'lchaydi va konstruksiya yuk ostida buzilmasligini ko'rsatadi",
      olchov: "uzatma nisbati to'g'ri hisoblangani va konstruksiyaning yuk ko'targani",
      mezon: ["Nisbat to'g'ri hisoblanadi va konstruksiya 3 detal-yukni ko'taradi = 5 (a'lo)",
              "Nisbat to'g'ri hisoblanadi va 1–2 yuk ko'tariladi = 4 (yaxshi)",
              "Uzatma ishlaydi, nisbat taxminan aytiladi = 3 (qoniqarli)",
              "Uzatma ishlaydi, lekin nisbat aytilmaydi = 2 (qoniqarsiz)",
              "Ikki bosqichli uzatma yig'ilmasa = FAILED"],
      jihoz: ["Turli o'lchamdagi tishli g'ildiraklar", "Aylanishlarni sanash uchun rangli belgi", "Yuk detallari"],
      lugat: ["Ikki bosqichli uzatma (Two-stage gearing) – ketma-ket ulangan ikki juft tishli g'ildirak",
              "Uzatma nisbati (Gear ratio) – kirish va chiqish aylanishlari nisbati",
              "Yuklama (Load) – mexanizmga tushadigan og'irlik"],
      savol: "Ikki bosqich bir bosqichdan nimasi bilan kuchli?"
    },
    {
      nom: "Shkiv-Kuchi",
      vazifa: "shkiv tizimi qurib yukni ko'taradi va shkivlar sonini oshirganda tortish qanchalik yengillashishini ko'rsatadi",
      olchov: "ko'tarilgan yuk va shkiv sonining ta'siri tushuntirilgani",
      mezon: ["2 va undan ko'p shkivli tizim ishlaydi, farq tushuntiriladi = 5 (a'lo)",
              "2 shkivli tizim ishlaydi = 4 (yaxshi)", "1 shkivli tizim ishlaydi = 3 (qoniqarli)",
              "Shkiv o'rnatilgan, lekin yuk ko'tarilmaydi = 2 (qoniqarsiz)",
              "Shkiv tizimi yig'ilmasa = FAILED"],
      jihoz: ["Shkivlar va tasma/ip", "Bir xil og'irlikdagi yuk detallari", "Ko'tarish uchun ramka"],
      lugat: ["Shkiv bloki (Pulley block) – bir necha shkivdan tuzilgan tizim",
              "Mexanik yutuq (Mechanical advantage) – mexanizm kuchni necha marta yengillashtirishi",
              "Tortish kuchi (Pulling force) – ipni tortishga sarflanadigan kuch"],
      savol: "Shkiv sonini ikki barobar oshirsangiz, tortish qanchaga yengillashadi?"
    },
    {
      nom: "Tebranish-Nishoni",
      vazifa: "krivoship mexanizmini sozlab, 30 soniyada AYNAN 20 marta tebranishga erishish kerak (ko'p ham, kam ham emas)",
      olchov: "20 dan chetlanish",
      mezon: ["Chetlanish 0–1 tebranish = 5 (a'lo)", "2–3 tebranish = 4 (yaxshi)",
              "4–6 tebranish = 3 (qoniqarli)", "7–10 tebranish = 2 (qoniqarsiz)",
              "10 dan ko'p yoki mexanizm uzilib qolsa = FAILED"],
      jihoz: ["Sekundomer", "Sanash uchun juftlik", "Sozlash uchun turli o'lchamdagi g'ildiraklar"],
      lugat: ["Chastota (Frequency) – vaqt birligidagi tebranishlar soni",
              "Sozlash (Tuning) – kerakli natijaga moslash",
              "Barqarorlik (Consistency) – mexanizmning bir tekis ishlashi"],
      savol: "Tezlikni nima orqali sozladingiz — uzatma bilanmi yoki qo'l tezligi bilanmi?"
    }
  ],

  "1-sinf": [
    {
      nom: "Ritm-Sozlash",
      vazifa: "mexanizmning tebranish kengligini uchta turli nishonga (5 sm, 10 sm, 15 sm) ketma-ket sozlash kerak",
      olchov: "uch nishondan nechtasiga 1,5 sm aniqlikda erishilgani",
      mezon: ["3/3 nishon = 5 (a'lo)", "2/3 nishon = 4 (yaxshi)", "1/3 nishon = 3 (qoniqarli)",
              "Sozlash qilinadi, lekin nishonga tushmaydi = 2 (qoniqarsiz)",
              "Mexanizm sozlanmasa = FAILED"],
      jihoz: ["Chizg'ich va uch nishon belgisi", "Sozlash uchun qo'shimcha detallar"],
      lugat: ["Amplituda (Amplitude) – tebranishning eng katta kengligi",
              "Nishon qiymati (Target value) – erishilishi kerak bo'lgan natija",
              "Chetlanish (Deviation) – natijaning nishondan farqi"],
      savol: "Qaysi nishon eng qiyin bo'ldi va nega?"
    },
    {
      nom: "Sensor-Aniqligi",
      vazifa: "sensorli model 10 marta sinaladi; sensor har safar bir xil masofada (±5 sm) ishga tushishi kerak",
      olchov: "10 sinovdan nechtasi ±5 sm oralig'ida chiqqani",
      mezon: ["9–10/10 = 5 (a'lo)", "7–8/10 = 4 (yaxshi)", "5–6/10 = 3 (qoniqarli)",
              "3–4/10 = 2 (qoniqarsiz)", "3 dan kam yoki sensor ishlamasa = FAILED"],
      jihoz: ["O'lchov lentasi", "Sinov to'sig'i", "10 qatorli natija jadvali"],
      lugat: ["Takroriylik (Repeatability) – bir xil sinovda bir xil natija chiqishi",
              "Kalibrlash (Calibration) – sensorni to'g'ri ishlashga sozlash",
              "Chegara qiymati (Threshold) – sensor ishga tushadigan qiymat"],
      savol: "Natijalar nega har safar bir xil chiqmadi — sabab yorug'likmi, sirtmi?"
    },
    {
      nom: "Kran-Operatori",
      vazifa: "kran yoki strela mexanizmi yukni 20 sm balandlikka ko'tarib, 40 sm yon tomondagi belgilangan joyga qo'yishi kerak",
      olchov: "topshiriq bajarilgani va yuk tushib ketmagani",
      mezon: ["Yuk to'g'ri joyga qo'yiladi, tushmaydi, 60 soniyagacha = 5 (a'lo)",
              "Yuk to'g'ri joyga qo'yiladi, 61–120 soniya = 4 (yaxshi)",
              "Yuk ko'tariladi, lekin joyiga aniq qo'yilmaydi = 3 (qoniqarli)",
              "Yuk ko'tariladi, lekin tushib ketadi = 2 (qoniqarsiz)",
              "Yuk ko'tarilmasa = FAILED"],
      jihoz: ["Standart yuk", "20 sm balandlikdagi tayanch va nishon belgisi", "Sekundomer"],
      lugat: ["Strela (Boom) – kranning uzun ko'taruvchi qismi",
              "Kontr-vazn (Counterweight) – kranni ag'darilishdan saqlovchi qarshi og'irlik",
              "Ish zonasi (Working area) – kran yeta oladigan maydon"],
      savol: "Strela uzunlashganda kran nega beqaror bo'lib qoladi?"
    },
    {
      nom: "Transport-Sinovi",
      vazifa: "motorli transport uch xil sirtda 1 metr masofani bosib o'tadi va yo'lda bitta burilish bajaradi",
      olchov: "uch sirtda ham finishga yetgani va umumiy vaqt",
      mezon: ["3/3 sirtda finish, jami 60 soniyagacha = 5 (a'lo)",
              "3/3 sirtda finish, jami 61–120 soniya = 4 (yaxshi)",
              "2/3 sirtda finish = 3 (qoniqarli)", "1/3 sirtda finish = 2 (qoniqarsiz)",
              "Hech bir sirtda finishga yetmasa = FAILED"],
      jihoz: ["Uch xil sirt (stol, gilam, qog'oz)", "Burilishli 1 metrlik trassa", "Sekundomer"],
      lugat: ["Ilashish (Traction) – g'ildirakning sirtga yopishishi",
              "Burilish radiusi (Turning radius) – eng kichik burilish aylanasi",
              "Uzatma (Transmission) – motordan g'ildirakka kuch yetkazuvchi tizim"],
      savol: "Qaysi sirt eng qiyin bo'ldi va uni yengish uchun nima o'zgartirdingiz?"
    }
  ],

  "2-sinf": [
    {
      nom: "Yo'l-Chempionati",
      vazifa: "transport 3 metrlik trassani bosib o'tadi; trassada ikki burilish, bitta to'siq va bitta qiyalik bor",
      olchov: "trassani tugatish vaqti va to'siqqa tegmaganligi",
      mezon: ["30 soniyagacha, tegmasdan = 5 (a'lo)", "31–60 soniya = 4 (yaxshi)",
              "61–100 soniya yoki 1 marta tegsa = 3 (qoniqarli)",
              "100 soniyadan ko'p yoki 2 marta tegsa = 2 (qoniqarsiz)",
              "Qiyalikdan o'ta olmasa yoki finishga yetmasa = FAILED"],
      jihoz: ["3 metrlik trassa: 2 burilish, 1 to'siq, 1 qiyalik", "Sekundomer"],
      lugat: ["Osma tizim (Suspension) – zarbani yumshatuvchi qism",
              "Qiyalik (Incline) – ko'tarilish burchagi",
              "Klirens (Ground clearance) – model tagi bilan yer orasidagi masofa"],
      savol: "Qiyalikda modelingiz nega sekinlashdi — og'irlikmi, uzatmami?"
    },
    {
      nom: "Havo-Kuchi",
      vazifa: "parrakli yoki reaktiv model yasab, uning tortish kuchini o'lchash: model ip bilan bog'lanadi va necha detal-yukni tortib siljita olishi sanaladi",
      olchov: "tortib siljitilgan yuk miqdori",
      mezon: ["4 va undan ko'p detal-yuk = 5 (a'lo)", "3 detal-yuk = 4 (yaxshi)",
              "2 detal-yuk = 3 (qoniqarli)", "1 detal-yuk = 2 (qoniqarsiz)",
              "Model yukni umuman siljitolmasa = FAILED"],
      jihoz: ["Parrak va motor", "Ip va yuk detallari", "Silliq sirt"],
      lugat: ["Tortish kuchi (Thrust) – parrak hosil qiladigan itaruvchi kuch",
              "Qanot burchagi (Blade pitch) – parrak qanotining qiyaligi",
              "Havo oqimi (Airflow) – parrak haydaydigan havo"],
      savol: "Qanot burchagini o'zgartirsangiz tortish kuchi qanday o'zgaradi?"
    },
    {
      nom: "Bionik-Yurish",
      vazifa: "hayvondan ilhomlangan, g'ildiraksiz oyoqli model 2 metr masofani bosib o'tadi va yo'lda 3 sm balandlikdagi to'siqdan oshib o'tadi",
      olchov: "masofani bosib o'tgani va to'siqdan oshgani",
      mezon: ["To'siqdan oshib, 2 metrni yiqilmasdan bosib o'tsa = 5 (a'lo)",
              "To'siqdan oshadi, 1 marta yiqiladi = 4 (yaxshi)",
              "2 metrni bosadi, lekin to'siqdan o'tolmaydi = 3 (qoniqarli)",
              "1 metrdan ko'proq yuradi = 2 (qoniqarsiz)",
              "Yura olmasa yoki g'ildirak ishlatilsa = FAILED"],
      jihoz: ["2 metrlik yo'lak", "3 sm balandlikdagi to'siq", "Yiqilishlarni sanash varaqasi"],
      lugat: ["Qadam tsikli (Gait cycle) – oyoqlarning takrorlanuvchi harakat tartibi",
              "Klirens (Ground clearance) – model tagining balandligi",
              "Biomimikriya (Biomimicry) – tabiatdagi yechimni texnikaga ko'chirish"],
      savol: "Qaysi hayvon oyog'idan nusxa oldingiz va u to'siqda yordam berdimi?"
    },
    {
      nom: "Rover-Missiyasi",
      vazifa: "rover notekis maydondan o'tib, ikkita namunani (turli joydan) yig'ib, start nuqtasiga qaytadi",
      olchov: "yig'ilgan namunalar soni va umumiy vaqt",
      mezon: ["2 namuna olib qaytsa, 3 daqiqadan kam = 5 (a'lo)",
              "2 namuna olib qaytsa, 3–5 daqiqa = 4 (yaxshi)",
              "1 namuna olib qaytsa = 3 (qoniqarli)",
              "Namuna olinadi, lekin qaytmaydi = 2 (qoniqarsiz)",
              "Notekis maydondan o'ta olmasa = FAILED"],
      jihoz: ["Notekis \"Mars\" maydoni", "Ikkita rangli namuna detali", "Sekundomer"],
      lugat: ["Missiya (Mission) – aniq maqsadli topshiriqlar ketma-ketligi",
              "Navigatsiya (Navigation) – yo'lni topib borish",
              "Manipulyator (Manipulator) – namunani olish qismi"],
      savol: "Ikkinchi namunani olish birinchisidan nimasi bilan qiyin bo'ldi?"
    }
  ]
};

// ------------------------------------------------------------------ generator

function nazoratDarsi(yil, sinf, chorakNo) {
  const jadval = (yil === "2-yil" && NAZORAT_2[sinf]) ? NAZORAT_2 : NAZORAT;
  const n = (jadval[sinf] || [])[chorakNo - 1];
  if (!n) return null;

  const yakuniy = chorakNo === 4;
  const sarlavha = chorakNo + '-chorak' + (yakuniy ? ' (yakuniy)' : '') +
    ' nazorat ishi — "' + n.nom + '" musobaqasi: ' + n.vazifa +
    '. Baholash mezoni: ' + n.mezon.join('; ') + '.';

  return {
    nom: sarlavha,
    kontent: {
      maqsad: [
        'O\'quvchilar chorak davomida o\'rgangan bilim va ko\'nikmalarini "' + n.nom +
          '" musobaqasida amaliy tarzda namoyish etadilar.',
        'O\'quvchilar oldindan e\'lon qilingan aniq mezon (' + n.olchov +
          ') asosida baholanish tajribasini oladilar.',
        'O\'quvchilar o\'z natijasini tahlil qilib, nima uchun shunday chiqqanini tushuntiradilar.'
      ],
      lugat: n.lugat.concat(UMUMIY_LUGAT),
      softSkill: SOFT[chorakNo - 1],
      resurslar: [
        'Chorak davomida o\'quvchilar yig\'gan modellar',
        'Natijalarni yozish uchun jadval (doskada yoki qog\'ozda)'
      ].concat(n.jihoz),
      nazariya: [
        {
          title: '5.1. Musobaqa qoidalari (5 daqiqa)',
          points: [
            'Topshiriq e\'lon qilinadi: ' + n.vazifa + '.',
            'Navbat tartibi belgilanadi va xavfsizlik qoidalari eslatiladi.'
          ]
        },
        {
          title: '5.2. Baholash mezoni (10 daqiqa)',
          points: n.mezon.concat([
            'Mezon doskaga yoziladi — musobaqa davomida o\'zgartirilmaydi.'
          ])
        }
      ],
      amaliy: [
        {
          title: '6.1. Tayyorgarlik (5 daqiqa)',
          points: [
            'O\'quvchilar modelini oxirgi marta tekshiradilar va kerak bo\'lsa batareyani almashtiradilar.',
            'Har bir juftlik bitta sinov urinishi qilib ko\'radi.'
          ]
        },
        {
          title: '6.2. Musobaqa (20 daqiqa)',
          points: [
            'Har bir o\'quvchi yoki juftlik navbat bilan chiqib topshiriqni bajaradi.',
            'O\'qituvchi natijani (' + n.olchov + ') o\'lchab jadvalga yozadi.',
            'Har bir natija darhol mezon bo\'yicha baholanadi va e\'lon qilinadi.'
          ]
        },
        {
          title: '6.3. Natija tahlili (5 daqiqa)',
          points: [
            'Sinf jadvalga birga qaraydi: eng yaxshi natija nima bilan ajralib turdi?',
            'Asosiy savol muhokama qilinadi: ' + n.savol
          ]
        }
      ],
      uyga: [
        'Bugungi natijangizni yaxshilash uchun modelga qanday bitta o\'zgartirish kiritgan bo\'lardingiz — daftaringizga yozib keling.',
        'Sinfdagi eng yaxshi natijani ko\'rsatgan model nimasi bilan farq qilganini bir gapda yozing.'
      ]
    }
  };
}

module.exports = { faol: true, NAZORAT, NAZORAT_2, nazoratDarsi };
