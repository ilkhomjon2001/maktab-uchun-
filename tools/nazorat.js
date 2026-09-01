/*
 * OYLIK NAZORAT — NAZARIY TEST (har chorakning 9-darsi)
 * =====================================================
 * 2026-09-01 dan tuzilma o'zgardi (foydalanuvchi so'rovi):
 *   - ustozlarning oylik maoshi o'quvchilarning nazorat bahosidan kelib
 *     chiqadi, shuning uchun baho chorak oxirida emas, HAR OYda chiqadi;
 *   - har chorakda 2 ta baholanadigan nusqta bor:
 *       9-dars  = NAZARIY TEST (shu fayl)          -> 1-oy bahosi
 *       18-dars = AMALIY LOYIHA-IMTIHON (loyiha.js) -> 2-oy bahosi
 *   - eski "chorak oxiridagi musobaqa" bekor qilindi; uning o'lchovlari
 *     loyiha check-listining "sinov" bandiga ko'chdi.
 *
 * Har test: 10 savol, 3 variant (A/B/C), 20 daqiqa.
 * Baholash: 9-10 to'g'ri = 5;  7-8 = 4;  5-6 = 3;  3-4 = 2;  0-2 = FAILED.
 *
 * Savollar QAYSI darslarni qamraydi: testgacha o'tilgan 7 ta qurish darsi
 * (chorakning birinchi yarmi mavzulari). Har sinf-yil-chorak uchun savollar
 * alohida yozilgan — bola hech qaysi oqimda bir xil testga ikki marta
 * duch kelmaydi (2-yil 3-4-sinf SPIKE bundan mustasno: dastur bir xil).
 *
 * Yozuv formati:
 *   mavzu    — test sarlavhasi (chorak yo'nalishi)
 *   savollar — [{s: savol, v: [A, B, C], t: to'g'ri javob indeksi}]
 */

/* =====================================================================
 * 1-YIL — maktabning birinchi yili (yoyilgan, osonroq variant)
 * ===================================================================== */
const TESTLAR = {

  "0-sinf": [
    { mavzu: "Muvozanat va barqarorlik",
      savollar: [
        { s: "Qaysi model qiyinroq ag'anaydi?",
          v: ["Tayanchi keng model", "Tayanchi tor model", "Eng chiroyli model"], t: 0 },
        { s: "Minora juda baland qurilsa nima bo'ladi?",
          v: ["Mustahkamroq bo'ladi", "Tezroq ag'anadigan bo'ladi", "Hech narsa o'zgarmaydi"], t: 1 },
        { s: "Og'irlik markazi nima?",
          v: ["Modelning eng chiroyli joyi", "Modelning nomi", "Modelning og'irligi to'plangan nuqtasi"], t: 2 },
        { s: "Tarozi qachon tebranmay tinch turadi?",
          v: ["Ikki tomoni teng og'irlikda bo'lsa", "Bir tomoni og'ir bo'lsa", "Tarozi hech qachon tinch turmaydi"], t: 0 },
        { s: "Model stol chetidan nega tushib ketadi?",
          v: ["Rangi och bo'lgani uchun", "Og'irligi tayanchdan tashqariga chiqib ketgani uchun", "Stol sovuq bo'lgani uchun"], t: 1 },
        { s: "Barqaror turishi uchun og'ir detallarni qayerga qo'yish kerak?",
          v: ["Eng tepaga", "O'rtaga osiltirib", "Pastga, tayanchga yaqin"], t: 2 },
        { s: "Tebranuvchi o'yinchoq (pastki qismi og'ir yumaloq o'yinchoq) nega yiqilmaydi?",
          v: ["Og'irligi eng pastida bo'lgani uchun", "Juda yengil bo'lgani uchun", "Yumaloq boshli bo'lgani uchun"], t: 0 },
        { s: "Ikki oyoqda turgan robot va to'rt oyoqda turgan robotdan qaysi biri barqarorroq?",
          v: ["Ikki oyoqlisi", "To'rt oyoqlisi", "Ikkalasi bir xil"], t: 1 },
        { s: "Shamol essa qaysi minora yiqilmaydi?",
          v: ["Baland va tor minora", "Bir oyoqli minora", "Past va keng minora"], t: 2 },
        { s: "Muvozanatni tekshirish uchun modelni nima qilamiz?",
          v: ["Sekin turtib ko'ramiz", "Otib yuboramiz", "Suvga solamiz"], t: 0 }
      ] },
    { mavzu: "Richag qonuni",
      savollar: [
        { s: "Richag nima?",
          v: ["Yumaloq g'ildirak", "Tayanch nuqtasi atrofida aylanadigan uzun qattiq bo'lak", "Kichkina kubik"], t: 1 },
        { s: "Richag qaysi nuqta atrofida aylanadi?",
          v: ["O'zining uchida", "Havoda", "Tayanch nuqtasi atrofida"], t: 2 },
        { s: "Tarozi richagning qaysi turiga o'xshaydi?",
          v: ["Tayanch o'rtada bo'lgan richagga", "Tayanch chetda bo'lgan richagga", "Tarozida richag yo'q"], t: 0 },
        { s: "Og'ir yukni yengil ko'tarish uchun kuchni qayerga qo'yamiz?",
          v: ["Tayanchga juda yaqin joyga", "Tayanchdan uzoqroq joyga", "Yukning ustiga"], t: 1 },
        { s: "Zambilg'altak (tachka)da yuk qayerda joylashadi?",
          v: ["Kuch bilan tayanch orasida", "G'ildirakning ostida", "Dastaning uchida"], t: 0 },
        { s: "Qaysiqchi (qisqich) ikki richagning birga ishlashiga misolmi?",
          v: ["Yo'q, u richag emas", "Ha — ikkala dastasi ham richag", "U faqat bitta richag"], t: 1 },
        { s: "Kuch yelkasi uzaysa, ko'tarish qanday bo'ladi?",
          v: ["Qiyinlashadi", "O'zgarmaydi", "Osonlashadi"], t: 2 },
        { s: "Eshik tutqichi nega eshikning chetiga o'rnatiladi?",
          v: ["Chiroyli ko'rinishi uchun", "Chetdan itarish osonroq bo'lgani uchun", "Boshqa joy qolmagani uchun"], t: 1 },
        { s: "1-toifa richagda nima o'rtada turadi?",
          v: ["Tayanch nuqtasi", "Yuk", "Kuch"], t: 0 },
        { s: "Richag bilan toshni ko'tarayotganda tayanchni toshga yaqinlashtirsak nima bo'ladi?",
          v: ["Ko'tarish qiyinlashadi", "Hech narsa o'zgarmaydi", "Ko'tarish osonlashadi"], t: 2 }
      ] },
    { mavzu: "Geometrik shakllar va mustahkamlik",
      savollar: [
        { s: "Qaysi shakl yuk ostida ham shaklini o'zgartirmaydi?",
          v: ["To'rtburchak", "Uchburchak", "Doira"], t: 1 },
        { s: "To'rtburchak ramkani mustahkam qilish uchun nima qo'shamiz?",
          v: ["Diagonal bo'lak", "Yana bitta to'rtburchak", "Rangli detal"], t: 0 },
        { s: "Diagonal qo'shilgan to'rtburchak nimaga aylanadi?",
          v: ["Doiraga", "Kattaroq to'rtburchakka", "Ikkita uchburchakka"], t: 2 },
        { s: "Ko'priklarda nega uchburchaklar ko'p ishlatiladi?",
          v: ["Uchburchak mustahkam bo'lgani uchun", "Chizish oson bo'lgani uchun", "Uchburchak yengil bo'lgani uchun"], t: 0 },
        { s: "Yopiq konstruksiya qanday bo'ladi?",
          v: ["Bir tomoni ochiq qolgan", "Barcha tomonlari tutashgan", "Faqat bitta bo'lakdan iborat"], t: 1 },
        { s: "Ko'p uchburchakdan yasalgan konstruksiya nima deb ataladi?",
          v: ["G'ildirak", "Zanjir", "Ferma"], t: 2 },
        { s: "Konstruksiya ustiga yuk qo'ysak, kuch qayerga tushadi?",
          v: ["Faqat yuqoriga", "Tayanchlar orqali pastga tarqaladi", "Hech qayerga"], t: 1 },
        { s: "Baland konstruksiyani mustahkam qilish uchun pastini qanday quramiz?",
          v: ["Kengroq qilib", "Torroq qilib", "Bo'sh qoldirib"], t: 0 },
        { s: "Ramka yon tomonga qiyshayib ketsa, bu nima?",
          v: ["Mustahkamlik", "Deformatsiya (shakl o'zgarishi)", "Muvozanat"], t: 1 },
        { s: "Ikki tayanch orasidagi ko'prik qayeridan sinishi ehtimoli katta?",
          v: ["Tayanchning tagidan", "Chetidan", "O'rtasidan"], t: 2 }
      ] },
    { mavzu: "Tishli g'ildirak va shkiv",
      savollar: [
        { s: "Tishli g'ildiraklar bir-biriga qanday ulanadi?",
          v: ["Tishlari bilan tishlashib", "Ip bilan bog'lanib", "Yelim bilan yopishib"], t: 0 },
        { s: "Katta tishli g'ildirak kichigini aylantirsa, kichigi qanday aylanadi?",
          v: ["Sekinroq", "Tezroq", "Bir xil tezlikda"], t: 1 },
        { s: "Ikkita tishlashgan g'ildirak qaysi tomonga aylanadi?",
          v: ["Ikkalasi bir tomonga", "Ikkalasi ham to'xtab qoladi", "Bir-biriga qarama-qarshi tomonga"], t: 2 },
        { s: "Uzatma nisbatini bilish uchun nimani sanaymiz?",
          v: ["G'ildiraklarning tishlarini", "G'ildiraklarning rangini", "Detallar narxini"], t: 0 },
        { s: "Shkiv tishli g'ildirakdan nimasi bilan farq qiladi?",
          v: ["Shkiv kattaroq bo'ladi", "Shkivda tish yo'q — tasma yoki ip bilan ishlaydi", "Farqi yo'q"], t: 1 },
        { s: "Shkiv orqali yuk ko'targanda ipni qaysi tomonga tortamiz?",
          v: ["Yon tomonga", "Yuk tomonga", "Pastga — yuk esa yuqoriga ko'tariladi"], t: 2 },
        { s: "8 tishli g'ildirak 24 tishli g'ildirakni aylantirsa, katta g'ildirak qanday aylanadi?",
          v: ["3 barobar sekin", "3 barobar tez", "Bir xil"], t: 0 },
        { s: "Velosipedning pedali va orqa g'ildiragi nima orqali ulangan?",
          v: ["Yelim bilan", "Zanjir bilan", "Magnit bilan"], t: 1 },
        { s: "Aylanish yo'nalishini o'zgartirmay uzatish uchun ikki g'ildirak orasiga nima qo'yamiz?",
          v: ["Hech narsa", "Suv", "Uchinchi (oraliq) g'ildirak"], t: 2 },
        { s: "Tez aylanish kerak bo'lsa, motorni qaysi g'ildirakka ulaymiz?",
          v: ["Katta g'ildirakka — u kichigini tez aylantiradi", "Kichik g'ildirakka", "Ikkalasiga birdan"], t: 0 }
      ] }
  ],

  "1-sinf": [
    { mavzu: "Vint mexanizmi va avtomatik harakat",
      savollar: [
        { s: "Vint mexanizmi aylanma harakatni qanday harakatga aylantiradi?",
          v: ["To'g'ri chiziqli (oldinga-orqaga) harakatga", "Sakrash harakatiga", "Hech qanday harakatga"], t: 0 },
        { s: "Vintni burasak, gayka nima qiladi?",
          v: ["Joyida turadi", "Vint bo'ylab siljiydi", "Uchib ketadi"], t: 1 },
        { s: "Avtomatik darvoza qo'lda ochiladimi?",
          v: ["Ha, faqat qo'lda", "U hech qachon ochilmaydi", "Yo'q — mexanizm o'zi ochadi"], t: 2 },
        { s: "Aylanma harakat qanday harakat?",
          v: ["Bir nuqta atrofida aylanish", "Faqat oldinga yurish", "Joyida turish"], t: 0 },
        { s: "Tebranma harakat qanday harakat?",
          v: ["Doim bir tomonga aylanish", "U yoqdan-bu yoqqa qaytib turadigan harakat", "Juda tez uchish"], t: 1 },
        { s: "Mexanizm bo'g'inlari orasida katta bo'shliq qolsa nima bo'ladi?",
          v: ["Mexanizm tezlashadi", "Hech narsa bo'lmaydi", "Harakat noaniq, taqillab ishlaydi"], t: 2 },
        { s: "Vintli ko'targich (domkrat) nima uchun ishlatiladi?",
          v: ["Og'ir narsani sekin va kuchli ko'tarish uchun", "Musiqa chalish uchun", "Tez yugurish uchun"], t: 0 },
        { s: "Mexanizmni harakatga nima keltiradi?",
          v: ["Bo'yoq", "Kuch (qo'l yoki motor)", "Sovuq havo"], t: 1 },
        { s: "Vint mexanizmida harakat qaysi yo'nalishda uzatiladi?",
          v: ["Faqat yon tomonga", "Hech qayerga", "Aylanishdan — vint o'qi bo'ylab"], t: 2 },
        { s: "Avtomatik mexanizmning qo'lda ishlaydigan mexanizmdan afzalligi nima?",
          v: ["Odam kuchini tejaydi va o'zi ishlaydi", "Chiroyliroq", "Har doim kichkina bo'ladi"], t: 0 }
      ] },
    { mavzu: "Mexanizmni takomillashtirish va harakat turlari",
      savollar: [
        { s: "Mexanizmni takomillashtirish nima degani?",
          v: ["Uni ishlashini yaxshilash", "Uni buzib tashlash", "Uni bo'yash"], t: 0 },
        { s: "Chayqalish harakati qanday harakat?",
          v: ["Doim bir tomonga aylanish", "Beshik kabi u yoqqa-bu yoqqa tebranish", "To'g'ri chiziq bo'ylab uchish"], t: 1 },
        { s: "Harakatni kuchaytirish uchun mexanizmga nima qo'shamiz?",
          v: ["Ko'proq bo'yoq", "Og'ir tosh", "Richag"], t: 2 },
        { s: "Aylanma va tebranma harakatning farqi nimada?",
          v: ["Aylanma to'liq doira bo'ylab, tebranma qaytib turadi", "Farqi yo'q", "Tebranma tezroq"], t: 0 },
        { s: "Mexanizm o'lchamini kattalashtirsak, harakati qanday o'zgaradi?",
          v: ["Hech qanday", "Harakat kengroq (kattaroq) bo'ladi", "Mexanizm yo'qolib qoladi"], t: 1 },
        { s: "Mexanizm qiyshayib ishlasa, avvalo nimani tekshiramiz?",
          v: ["Rangini", "Narxini", "Bo'g'inlar mahkam ulanganini"], t: 2 },
        { s: "Ikki tomonlama harakat nima?",
          v: ["Mexanizm ham oldinga, ham orqaga ishlay olishi", "Ikki xil rangda bo'lishi", "Ikkita odam boshqarishi"], t: 0 },
        { s: "Beshik qaysi harakat turiga misol?",
          v: ["Aylanma", "Chayqalish (tebranma)", "Sakrash"], t: 1 },
        { s: "Mexanizmni mustahkamlash uchun nima qilamiz?",
          v: ["Detallarni olib tashlaymiz", "Uni silkitamiz", "Bo'sh bo'g'inlarni mahkamlaymiz, tayanch qo'shamiz"], t: 2 },
        { s: "Takomillashtirilgan mexanizm qanday ishlashi kerak?",
          v: ["Avvalgidan yaxshiroq va tekisroq", "Avvalgidan yomonroq", "Umuman ishlamasligi kerak"], t: 0 }
      ] },
    { mavzu: "O'lik nuqta, motor va murakkab harakatlar",
      savollar: [
        { s: "Mexanizmning \"o'lik nuqtasi\" nima?",
          v: ["Mexanizm tiqilib qoladigan holat", "Mexanizmning eng chiroyli joyi", "Motorning tugmasi"], t: 0 },
        { s: "O'lik nuqtadan chiqish uchun mexanizmga nima yordam beradi?",
          v: ["Suv quyish", "Aylanib turgan og'irlik (maxovik) yoki turtki", "Sovutish"], t: 1 },
        { s: "Sakrash harakati qanday hosil bo'ladi?",
          v: ["Model doim yerda sudraladi", "Model faqat aylanadi", "Mexanizm modelni yuqoriga itarib yuboradi"], t: 2 },
        { s: "Motor tezroq aylansa, tebranish qanday o'zgaradi?",
          v: ["Tebranish ham tezlashadi", "Tebranish sekinlashadi", "Tebranish to'xtaydi"], t: 0 },
        { s: "Bitta motordan nechta harakat olish mumkin?",
          v: ["Faqat bitta", "Uzatmalar orqali bir nechta", "Hech qancha"], t: 1 },
        { s: "Ikki mexanizm navbatma-navbat ishlashi uchun nima kerak?",
          v: ["Ikkita alohida stol", "Ikki xil rang", "Harakatni navbat bilan uzatadigan uzatma"], t: 2 },
        { s: "Motor nima qiladi?",
          v: ["Elektr energiyasini aylanma harakatga aylantiradi", "Faqat chiroq yoqadi", "Detallarni yopishtiradi"], t: 0 },
        { s: "Mexanizm bir joyda tiqilib qolsa, birinchi nima qilamiz?",
          v: ["Kuchliroq bosamiz", "To'xtatib, tiqilgan joyini topamiz", "Modelni otib yuboramiz"], t: 1 },
        { s: "Sakrovchi model qattiq yerga tushganda nimasi muhim?",
          v: ["Rangi o'chmasligi", "Ovoz chiqarishi", "Konstruksiyasi tarqalib ketmasligi"], t: 2 },
        { s: "Motorli mexanizmda harakat zanjiri qanday boshlanadi?",
          v: ["Motor - uzatma - mexanizm - harakat", "Harakat - motor", "Mexanizm - motor - uzatma"], t: 0 }
      ] },
    { mavzu: "Krivoship-shatun mexanizmi",
      savollar: [
        { s: "Krivoship-shatun mexanizmi nimani nimaga aylantiradi?",
          v: ["Aylanma harakatni tebranma (borib-kelib) harakatga", "Suvni muzga", "Tovushni yorug'likka"], t: 0 },
        { s: "Krivoship qaysi qism?",
          v: ["Tebranib turadigan uzun tayoq", "Aylanadigon o'qqa o'rnatilgan bandli (tirsakli) qism", "Yerda yotgan plastina"], t: 1 },
        { s: "Shatun nima vazifani bajaradi?",
          v: ["Motorni sovutadi", "Modelga rang beradi", "Krivoship bilan tebranuvchi qismni bog'laydi"], t: 2 },
        { s: "Krivoship radiusi kattalashsa, tebranish qanday o'zgaradi?",
          v: ["Tebranish kengayadi (amplituda oshadi)", "Tebranish torayadi", "O'zgarmaydi"], t: 0 },
        { s: "Harakat trayektoriyasi nima?",
          v: ["Modelning og'irligi", "Harakatlanayotgan nuqta chizadigan yo'l", "Motorning ovozi"], t: 1 },
        { s: "Yuqoriga-pastga (vertikal) tebranish uchun mexanizmni qanday joylashtiramiz?",
          v: ["Istalgancha — farqi yo'q", "Faqat yonboshlatib", "Shatun yuqoriga-pastga yuradigan qilib"], t: 2 },
        { s: "Paravoz g'ildiragidagi harakatlanuvchi tayoq nimaga misol?",
          v: ["Krivoship-shatun mexanizmiga", "Shkivga", "Tishli g'ildirakka"], t: 0 },
        { s: "Krivoship bir marta to'liq aylansa, shatun necha marta borib-keladi?",
          v: ["Ikki marta", "Bir marta", "O'n marta"], t: 1 },
        { s: "Amplituda so'zi nimani bildiradi?",
          v: ["Motor turini", "Detal rangini", "Tebranish kengligini"], t: 2 },
        { s: "Krivoship radiusini KICHRAYTIRSAK nima bo'ladi?",
          v: ["Tebranish torayadi", "Tebranish kengayadi", "Model uchib ketadi"], t: 0 }
      ] }
  ],

  "2-sinf": [
    { mavzu: "Sensor nima va qanday ishlaydi",
      savollar: [
        { s: "Sensor nima qiladi?",
          v: ["Atrofdagi o'zgarishni sezadi va signal beradi", "Faqat chiroq yoqadi", "Modelni harakatga keltiradi"], t: 0 },
        { s: "Sensor inson tanasidagi nimaga o'xshaydi?",
          v: ["Sochga", "Sezgi organlariga (ko'z, quloq, teri)", "Tirnoqqa"], t: 1 },
        { s: "Insonning ko'zi robotdagi qaysi narsaga to'g'ri keladi?",
          v: ["Motorga", "G'ildirakka", "Yorug'lik/rang sensoriga"], t: 2 },
        { s: "Chiziq kuzatuvchi robot nimani sezadi?",
          v: ["Yerdagi qora chiziqni", "Havoning haroratini", "Odamning ovozini"], t: 0 },
        { s: "Sensor signalni qayerga yuboradi?",
          v: ["Osmonga", "Boshqaruv qismiga (miyaga)", "Boshqa robotga"], t: 1 },
        { s: "Sensorsiz robot qanday bo'ladi?",
          v: ["Aqlliroq", "Tezroq", "Atrofni sezmaydigan — \"ko'r\""], t: 2 },
        { s: "\"Sezish - o'ylash - harakat\" zanjirida sensor qaysi bosqichda?",
          v: ["Sezish", "O'ylash", "Harakat"], t: 0 },
        { s: "Sensor xato ko'rsatishi mumkinmi?",
          v: ["Hech qachon", "Ha — masalan iflos yoki xira muhitda", "Faqat kechasi"], t: 1 },
        { s: "Insondagi \"sezish - o'ylash - harakat\" zanjiriga misol qaysi?",
          v: ["Uxlash - tush ko'rish - uyg'onish", "Yeyish - yurish - yugurish", "Issiqni sezish - qo'lni tortib olishga qaror qilish - tortib olish"], t: 2 },
        { s: "Robot to'siqni sezib to'xtadi. Birinchi nima ishladi?",
          v: ["Sensor", "G'ildirak", "Batareya"], t: 0 }
      ] },
    { mavzu: "Masofa, yorug'lik va chegara qiymati",
      savollar: [
        { s: "Masofa sensori nimani o'lchaydi?",
          v: ["To'siqqacha bo'lgan masofani", "Havoning rangini", "Vaqtni"], t: 0 },
        { s: "Masofa sensori ko'pincha qanday ishlaydi?",
          v: ["Suv purkab", "To'lqin yuborib, qaytishini kutib", "Qo'l cho'zib"], t: 1 },
        { s: "To'siqdan qochuvchi robot to'siqni ko'rsa nima qiladi?",
          v: ["To'siqqa uriladi", "To'xtab qoladi va yig'laydi", "To'xtaydi yoki aylanib o'tadi"], t: 2 },
        { s: "Chegara qiymati nima?",
          v: ["Sensor ishga tushadigan belgilangan qiymat", "Robotning eng katta tezligi", "Maydonning chegarasi"], t: 0 },
        { s: "Chegara qiymati 10 sm bo'lsa, robot qachon to'xtaydi?",
          v: ["100 sm qolganda", "To'siqqa 10 sm qolganda", "Hech qachon"], t: 1 },
        { s: "Yorug'lik sensori nimani farqlaydi?",
          v: ["Ovozni", "Hidni", "Yorug' va qorong'ini"], t: 2 },
        { s: "Oq qog'oz va qora qog'ozdan qaysi biri yorug'likni ko'proq qaytaradi?",
          v: ["Oq qog'oz", "Qora qog'oz", "Ikkalasi bir xil"], t: 0 },
        { s: "Sensor iflos bo'lib qolsa nima bo'ladi?",
          v: ["Yaxshiroq ishlaydi", "Xato o'lchashi mumkin", "Tezroq ishlaydi"], t: 1 },
        { s: "Ko'chadagi chiroqlar qorong'ida o'zi yonsa, bunda nima ishlagan?",
          v: ["Taymer", "Odam tugma bosgan", "Yorug'lik sensori"], t: 2 },
        { s: "Chegara qiymatini juda kichik qilib qo'ysak (masalan 1 sm), robot qanday to'xtaydi?",
          v: ["To'siqqa juda yaqin kelib, urilib ketishi mumkin", "Juda erta to'xtaydi", "Umuman yurmaydi"], t: 0 }
      ] },
    { mavzu: "Bosim sensori va avtomatik tizimlar",
      savollar: [
        { s: "Bosim (teginish) sensori qachon signal beradi?",
          v: ["Unga tegilganda yoki bosilganda", "Yorug'lik tushganda", "Ovoz eshitilganda"], t: 0 },
        { s: "Lift eshigi odamni qisib qolmasligi uchun qaysi sensor kerak?",
          v: ["Rang sensori", "Teginish/to'siq sensori", "Harorat sensori"], t: 1 },
        { s: "Avtomatik tizim nima?",
          v: ["Odam doim boshqarib turadigan tizim", "Faqat o'yinchoq", "Sensor signali bilan o'zi ishlaydigan tizim"], t: 2 },
        { s: "Ikki sensor birga ishlashiga misol qaysi?",
          v: ["Robot ham chiziqni, ham to'siqni birdan kuzatadi", "Robot faqat turadi", "Ikkita robot yonma-yon"], t: 0 },
        { s: "Muzlatgich eshigi ochilganda chiroq yonadi. Buni nima sezadi?",
          v: ["Motor", "Eshikdagi tugma-sensor", "Muz"], t: 1 },
        { s: "Sensor \"yolg'on signal\" bersa, robot nima qiladi?",
          v: ["To'g'ri ishlashda davom etadi", "Doim to'xtab qoladi", "Kerak bo'lmagan joyda harakat qiladi"], t: 2 },
        { s: "Avtomatik darvoza mashina kelganda ochiladi. Zanjir qanday?",
          v: ["Sensor sezadi - tizim qaror qiladi - motor ochadi", "Motor ochadi - sensor sezadi", "Darvoza o'zi biladi"], t: 0 },
        { s: "Bosim sensorini qayerga o'rnatgan ma'qul?",
          v: ["Robotning ichiga, berkitib", "To'siq tegishi mumkin bo'lgan old qismga", "G'ildirakning ostiga"], t: 1 },
        { s: "Sensorli tizimning odam boshqaruvidan afzalligi nima?",
          v: ["Har doim qimmatroq", "Chiroyliroq", "Charchamaydi va tez javob beradi"], t: 2 },
        { s: "Robot qo'li narsani sezib ushlashi uchun qayerida sensor bo'lishi kerak?",
          v: ["Ushlagich (panja) qismida", "Orqa g'ildiragida", "Simida"], t: 0 }
      ] },
    { mavzu: "Ko'tarish mexanizmlari",
      savollar: [
        { s: "Yuk baland ko'tarilganda model nega ag'anashi mumkin?",
          v: ["Og'irlik markazi ko'tarilib, barqarorlik kamayadi", "Yuk chiroyli emas", "Motor charchaydi"], t: 0 },
        { s: "Kran ag'anab ketmasligi uchun orqa tomoniga nima qo'yiladi?",
          v: ["Bayroq", "Kontr-vazn (qarshi og'irlik)", "Yana bitta kran"], t: 1 },
        { s: "Richag bilan ko'tarishda kuchni tejash uchun nima qilamiz?",
          v: ["Yukni tayanchdan uzoqlashtiramiz", "Richagni qisqartiramiz", "Kuch yelkasini uzaytiramiz"], t: 2 },
        { s: "Shkiv bilan ko'tarishning qulayligi nimada?",
          v: ["Pastga tortib, yukni yuqoriga ko'tarish mumkin", "Shkiv yukni yengillashtiradi", "Ip kerak emas"], t: 0 },
        { s: "Vint bilan ko'tarish qanday bo'ladi?",
          v: ["Juda tez va kuchsiz", "Sekin, lekin kuchli va ishonchli", "Umuman ishlamaydi"], t: 1 },
        { s: "Nega og'ir yukni birdan (tez) ko'tarish xavfli?",
          v: ["Yuk rangi o'chadi", "Vaqt tejaladi", "Model muvozanatini yo'qotishi yoki sinishi mumkin"], t: 2 },
        { s: "Kontr-vazn qayerga qo'yiladi?",
          v: ["Yukka qarama-qarshi tomonga", "Yukning ustiga", "Yerga, modeldan uzoqqa"], t: 0 },
        { s: "Ko'tarish balandligi oshgani sari nimaga ko'proq e'tibor beramiz?",
          v: ["Rangga", "Barqarorlikka", "Tezlikka"], t: 1 },
        { s: "Qaysi mexanizm yukni ko'tarib TURIB QOLA oladi (qo'yib yubormaydi)?",
          v: ["Silliq shkiv", "Erkin richag", "Vintli mexanizm"], t: 2 },
        { s: "Haqiqiy ko'tarish kranida quyidagilardan qaysi biri ishlatiladi?",
          v: ["Shkiv, tros va kontr-vazn birga", "Faqat richag", "Faqat rezina"], t: 0 }
      ] }
  ],

  "3-sinf": [
    { mavzu: "Elektr motor",
      savollar: [
        { s: "Motorli modelning motorsiz modeldan asosiy farqi nima?",
          v: ["O'zi harakatlanadi, itarish shart emas", "Og'irroq turadi", "Chiroyliroq"], t: 0 },
        { s: "Motor qaysi energiyani harakatga aylantiradi?",
          v: ["Quyosh issig'ini to'g'ridan-to'g'ri", "Elektr energiyasini", "Shamolni"], t: 1 },
        { s: "Motorning aylanish yo'nalishini qanday o'zgartiramiz?",
          v: ["Motorni qizdirib", "Kuchliroq bosib", "Tok qutblarini (simlarni) almashtirib"], t: 2 },
        { s: "Motor kuchi (moment) nima?",
          v: ["Motorning aylantirish kuchi", "Motorning rangi", "Motorning narxi"], t: 0 },
        { s: "Motor kuchini qayerda sezamiz?",
          v: ["Motor hidida", "Og'ir yukni aylantira olishida", "Motor ovozining balandligida"], t: 1 },
        { s: "Motordan g'ildirakka kuch qanday yetib boradi?",
          v: ["Havo orqali", "O'z-o'zidan", "Uzatma (tishli g'ildirak, val) orqali"], t: 2 },
        { s: "Motorga juda og'ir yuk ulansa nima bo'ladi?",
          v: ["Sekinlashadi yoki to'xtab qoladi", "Tezlashadi", "Yengillashadi"], t: 0 },
        { s: "Batareya motorga nima beradi?",
          v: ["Suv", "Elektr toki", "Havo"], t: 1 },
        { s: "Motorni to'xtatish uchun nima qilamiz?",
          v: ["Qo'l bilan g'ildiragini ushlaymiz", "Kutamiz", "Tok zanjirini uzamiz (o'chirgich)"], t: 2 },
        { s: "Bitta motor ikkita g'ildirakni aylantira oladimi?",
          v: ["Ha — uzatma orqali ikkalasiga ham kuch beriladi", "Yo'q, har g'ildirakka alohida motor shart", "Motor g'ildirak aylantirmaydi"], t: 0 }
      ] },
    { mavzu: "Ishqalanish kuchi",
      savollar: [
        { s: "Ishqalanish kuchi qachon paydo bo'ladi?",
          v: ["Ikki sirt bir-biriga tegib harakatlanganda", "Model havoda uchganda", "Model turganda faqat"], t: 0 },
        { s: "Statik ishqalanish nima?",
          v: ["Harakatdagi ishqalanish", "Turgan jismni qo'zg'atishga qarshilik", "Suvdagi ishqalanish"], t: 1 },
        { s: "Qaysi sirtda model uzoqroq siljiydi?",
          v: ["Gilamda", "Qumda", "Silliq polda"], t: 2 },
        { s: "G'ildirak ishqalanishni qanday kamaytiradi?",
          v: ["Sirpanish o'rniga dumalaydi", "Sirtni ho'llaydi", "Umuman kamaytirmaydi"], t: 0 },
        { s: "Model og'irlashsa, ishqalanish qanday o'zgaradi?",
          v: ["Kamayadi", "Ortadi", "O'zgarmaydi"], t: 1 },
        { s: "Ishqalanishni kamaytirish uchun mashinalarga nima quyiladi?",
          v: ["Suv", "Qum", "Moy"], t: 2 },
        { s: "Ishqalanish har doim zararlimi?",
          v: ["Yo'q — yurish, tormozlash uchun kerak", "Ha, doim zararli", "Ishqalanish umuman yo'q narsa"], t: 0 },
        { s: "Qishda yo'lga nega qum sepiladi?",
          v: ["Chiroyli bo'lishi uchun", "Ishqalanishni oshirib, sirpanishni kamaytirish uchun", "Yo'lni isitish uchun"], t: 1 },
        { s: "Harakatdagi ishqalanish statik ishqalanishdan odatda qanday?",
          v: ["Ancha katta", "Teng", "Kichikroq"], t: 2 },
        { s: "Tezlik oshsa, sirt bilan ishqalanishdan tashqari yana nima qarshilik qiladi?",
          v: ["Havo qarshiligi", "Tovush", "Yorug'lik"], t: 0 }
      ] },
    { mavzu: "Transport: shassi, g'ildirak, tormoz",
      savollar: [
        { s: "Shassi nima?",
          v: ["Transportning asosiy ko'taruvchi asosi (skeleti)", "Mashinaning bo'yog'i", "Faraning nomi"], t: 0 },
        { s: "G'ildirak nimaga o'rnatiladi?",
          v: ["To'g'ridan-to'g'ri motorning ichiga", "O'qqa (valga)", "Oynaga"], t: 1 },
        { s: "Tezlik va kuch o'rtasidagi muros nima degani?",
          v: ["Ikkalasi doim birga oshadi", "Ikkalasi ham muhim emas", "Biri oshsa, ikkinchisi kamayadi"], t: 2 },
        { s: "Og'ir yuk tashiydigan transportga qanday uzatma kerak?",
          v: ["Kuchni oshiradigan (sekin, lekin kuchli)", "Tezlikni oshiradigan", "Uzatmasiz"], t: 0 },
        { s: "G'ildiraklar soni ko'paysa nima yaxshilanadi?",
          v: ["Tezlik keskin oshadi", "Og'irlik ko'proq nuqtaga taqsimlanadi", "Hech narsa"], t: 1 },
        { s: "Tormoz qanday ishlaydi?",
          v: ["Motorga tok qo'shadi", "G'ildirakni tezlashtiradi", "Ishqalanish bilan g'ildirakni sekinlatadi"], t: 2 },
        { s: "Poyga mashinasida qaysi xususiyat muhimroq?",
          v: ["Tezlik", "Yuk ko'tarish", "Balandlik"], t: 0 },
        { s: "Traktor katta kuchga ega, lekin sekin. Nega?",
          v: ["Motori yomon", "Uzatmasi kuchga sozlangan", "G'ildiragi rangli"], t: 1 },
        { s: "Shassi bo'sh (mo'rt) bo'lsa nima bo'ladi?",
          v: ["Model tezlashadi", "Hech narsa", "Yuk ostida egilib, model buziladi"], t: 2 },
        { s: "Transport turi nimaga qarab tanlanadi?",
          v: ["Bajaradigan vazifasiga qarab", "Faqat rangiga qarab", "Nomiga qarab"], t: 0 }
      ] },
    { mavzu: "Osma tizim va og'irlik taqsimoti",
      savollar: [
        { s: "Osma tizim (amortizator) nima uchun kerak?",
          v: ["Zarbani yumshatish uchun", "Tezlikni oshirish uchun", "Chiroy uchun"], t: 0 },
        { s: "Notekis yo'ldan o'tayotganda osma tizimsiz model qanday yuradi?",
          v: ["Yumshoq va tekis", "Qattiq silkinib, detallar bo'shashadi", "Tezroq"], t: 1 },
        { s: "Osma tizimda nima ishlatiladi?",
          v: ["Shisha bo'lak", "Qattiq tosh", "Prujina yoki elastik element"], t: 2 },
        { s: "Og'irlik taqsimoti nima degani?",
          v: ["Og'irlikning model bo'ylab qanday joylashgani", "Modelning umumiy narxi", "Motorning kuchi"], t: 0 },
        { s: "Og'irlik faqat orqa g'ildiraklarda bo'lsa nima bo'ladi?",
          v: ["Model tekis yuradi", "Old g'ildiraklar yerdan ko'tarilib ketishi mumkin", "Model tezlashadi"], t: 1 },
        { s: "Zarba kuchini kamaytirishning yo'li qaysi?",
          v: ["Qattiqroq urilish", "Tezroq yurish", "Zarbani yumshoq element orqali qabul qilish"], t: 2 },
        { s: "Mashina g'ildiragidagi rezina shina nima vazifani ham bajaradi?",
          v: ["Mayda zarbalarni yumshatadi", "Mashinani og'irlashtiradi", "Faqat rang beradi"], t: 0 },
        { s: "Yuk mashinasiga yukni qanday joylash to'g'ri?",
          v: ["Hammasi bir chetga", "Teng taqsimlab", "Faqat tepaga"], t: 1 },
        { s: "Osma tizim juda qattiq bo'lsa nima bo'ladi?",
          v: ["Zarba juda yaxshi yumshaydi", "Model yumshoq yuradi", "Zarba deyarli yumshamaydi"], t: 2 },
        { s: "Tez yuradigan model uchun og'irlik markazi qanday bo'lgani ma'qul?",
          v: ["Past va o'rtada", "Baland va chetda", "Ahamiyati yo'q"], t: 0 }
      ] }
  ],

  "4-sinf": [
    { mavzu: "Biomimikriya: hayvonlardan o'rganamiz",
      savollar: [
        { s: "Biomimikriya nima?",
          v: ["Tabiatdagi yechimlarni texnikaga ko'chirish", "Hayvonlarni o'rgatish", "Rasm chizish usuli"], t: 0 },
        { s: "Hayvon oyog'i qanday harakat qiladi?",
          v: ["Faqat aylanadi", "Bo'g'inlar orqali bukiladi va yoziladi", "Umuman harakatlanmaydi"], t: 1 },
        { s: "Hayvon skeleti modeldagi nimaga o'xshaydi?",
          v: ["Bo'yoqqa", "Motorga", "Konstruksiya karkasiga"], t: 2 },
        { s: "Qushlar qanotidan qaysi texnika uchun g'oya olingan?",
          v: ["Samolyot qanoti", "Avtomobil g'ildiragi", "Televizor"], t: 0 },
        { s: "Tikanli o'simlik urug'idan qaysi ixtiro kelib chiqqan?",
          v: ["Sement", "Yopishqoq lenta-taqish (liposhka)", "Kompyuter"], t: 1 },
        { s: "Uchuvchi hayvonlar qanday umumiy xususiyatga ega?",
          v: ["Og'ir suyaklar", "Kichkina qanotlar", "Yengil tana va katta qanot yuzasi"], t: 2 },
        { s: "Gepard tez yugurishi uchun tanasi qanday tuzilgan?",
          v: ["Egiluvchan umurtqa va uzun oyoqlar", "Og'ir va katta", "Kalta oyoqlar"], t: 0 },
        { s: "Robot-oyoq qurayotganda hayvondan nimani ko'chiramiz?",
          v: ["Yungi va rangini", "Bo'g'inlar joylashuvi va harakat tartibini", "Ovozini"], t: 1 },
        { s: "Ov qiluvchi hayvonga tezlik nima uchun kerak?",
          v: ["Chiroyli ko'rinish uchun", "Isinish uchun", "O'ljaga yetib olish uchun"], t: 2 },
        { s: "Baliqning suzgichlari qaysi texnikada takrorlangan?",
          v: ["Suv osti kemasi rullarida", "Velosiped pedalida", "Eshik tutqichida"], t: 0 }
      ] },
    { mavzu: "Hayvon harakatini mexanizmda takrorlash",
      savollar: [
        { s: "Hayvon yurishini modelda takrorlash uchun qaysi mexanizm ko'p ishlatiladi?",
          v: ["Krivoship-richag (oyoq mexanizmi)", "Faqat g'ildirak", "Shkiv"], t: 0 },
        { s: "Ilon qanday harakatlanadi?",
          v: ["Sakrab", "Tanasini to'lqinsimon egib", "G'ildirakda"], t: 1 },
        { s: "Hayvon dumi nima vazifani bajaradi?",
          v: ["Faqat chiroy", "Ovqat topish", "Muvozanatni saqlash va yo'nalish"], t: 2 },
        { s: "Suzuvchi hayvonlar suvni qanday itaradi?",
          v: ["Suzgich va dum harakati bilan", "Tishlari bilan", "Ko'zlari bilan"], t: 0 },
        { s: "To'rt oyoqli hayvon yurganda oyoqlari qanday tartibda harakatlanadi?",
          v: ["To'rttasi bir vaqtda", "Navbat bilan, muvozanat saqlangan holda", "Faqat old oyoqlari"], t: 1 },
        { s: "Sudralib yuruvchining modelida asosiy harakat qanday?",
          v: ["Yuqoriga sakrash", "Tez aylanish", "Tanani egib-to'g'rilab siljish"], t: 2 },
        { s: "Qushning qanot qoqishini modelda nima bilan takrorlaymiz?",
          v: ["Tebranma mexanizm bilan", "G'ildirak bilan", "Tormoz bilan"], t: 0 },
        { s: "Model-hayvon yurganda ag'anab ketmasligi uchun nima muhim?",
          v: ["Tez yurishi", "Har qadamda muvozanat saqlanishi", "Ko'p ovoz chiqarishi"], t: 1 },
        { s: "Kenguru harakatidan qanday mexanizm g'oyasi olingan?",
          v: ["Suzish mexanizmi", "Aylanish mexanizmi", "Prujinali sakrash mexanizmi"], t: 2 },
        { s: "Hayvon harakatini takrorlashda avval nimani kuzatamiz?",
          v: ["Harakatning qaysi bo'g'inlardan chiqishini", "Hayvonning rangini", "Hayvonning ovqatini"], t: 0 }
      ] },
    { mavzu: "Kuch, o'lcham va harakat strategiyasi",
      savollar: [
        { s: "Katta hayvonlar nega sekin harakatlanadi?",
          v: ["Og'ir tanani ko'tarish ko'p kuch talab qiladi", "Dangasa bo'lgani uchun", "Ko'zlari yomon ko'rgani uchun"], t: 0 },
        { s: "Chumoli o'zidan og'ir yukni ko'tara oladi. Bu nimani ko'rsatadi?",
          v: ["Chumoli sehrli", "Kichik o'lchamda kuch-og'irlik nisbati katta", "Yuk aslida yengil"], t: 1 },
        { s: "Ko'p oyoqli (masalan, olti oyoqli) robotning afzalligi nima?",
          v: ["Tezroq uchadi", "Kamroq detal ketadi", "Bir nechta oyoq yerda qolib, barqaror yuradi"], t: 2 },
        { s: "Fil va sichqon: qaysi birining yuragi tezroq uradi?",
          v: ["Sichqonning", "Filning", "Bir xil"], t: 0 },
        { s: "Ov paytida gepard uzoq yugura olmaydi. Nega?",
          v: ["Yo'lni bilmaydi", "Katta tezlik ko'p energiya sarflaydi", "Oyog'i qisqa"], t: 1 },
        { s: "Modelning oyoqlarini uzunlashtirsak nima o'zgaradi?",
          v: ["Hech narsa", "Model kichrayadi", "Qadam kengayadi, lekin muvozanat qiyinlashadi"], t: 2 },
        { s: "Og'ir model uchun oyoq mexanizmini qanday quramiz?",
          v: ["Kuchli va keng tayanchli", "Ingichka va uzun", "Bitta oyoqli"], t: 0 },
        { s: "Harakat strategiyasi nima degani?",
          v: ["Modelning nomi", "Qachon tez, qachon kuchli harakat qilishni tanlash", "Bo'yoq turi"], t: 1 },
        { s: "Toshbaqa sekin, lekin qanday afzalligi bor?",
          v: ["Uzun oyoqlari", "Katta tezligi", "Mustahkam himoyasi va kam energiya sarfi"], t: 2 },
        { s: "Model uchun oyoq soni qanday tanlanadi?",
          v: ["Vazifa va barqarorlik talabiga qarab", "Qancha ko'p bo'lsa shuncha yaxshi", "Doim ikkita"], t: 0 }
      ] },
    { mavzu: "Kosmik texnika",
      savollar: [
        { s: "Kosmosda Yer bilan qanday bog'lanadi?",
          v: ["Radio to'lqinlar (aloqa antennalari) orqali", "Sim tortib", "Baqirib"], t: 0 },
        { s: "Oyda gravitatsiya Yerdagidan qanday?",
          v: ["Kuchliroq", "Ancha kuchsiz", "Bir xil"], t: 1 },
        { s: "Past gravitatsiyada yurgan rover qanday harakat qiladi?",
          v: ["Og'irlashadi", "Yura olmaydi", "Yengil — sakrab ketmasligi uchun sekin yurishi kerak"], t: 2 },
        { s: "Kosmik texnika nega juda ishonchli bo'lishi kerak?",
          v: ["Kosmosda ta'mirlash deyarli imkonsiz", "Qimmat ko'rinishi uchun", "Tez uchishi uchun"], t: 0 },
        { s: "Marsoxodlarda nega 6 ta g'ildirak bo'ladi?",
          v: ["Chiroyli bo'lishi uchun", "Notekis yuzada barqarorlik va o'tuvchanlik uchun", "Tezroq yurish uchun"], t: 1 },
        { s: "Namuna olish mexanizmi nima qiladi?",
          v: ["Suratga oladi", "Signal yuboradi", "Tuproq yoki tosh bo'lagini olib saqlaydi"], t: 2 },
        { s: "Kosmosda harorat qanday o'zgaradi?",
          v: ["Juda katta farq: quyoshda issiq, soyada qattiq sovuq", "Doim iliq", "Doim +20"], t: 0 },
        { s: "Kosmik apparatga himoya qatlami nima uchun kerak?",
          v: ["Og'irroq bo'lishi uchun", "Harorat va zarralardan saqlash uchun", "Rang berish uchun"], t: 1 },
        { s: "Quyosh panellari kosmik apparatga nima beradi?",
          v: ["Suv", "Havo", "Elektr energiyasi"], t: 2 },
        { s: "Kelajak kosmik missiyalarida robotlar nima uchun muhim?",
          v: ["Odam bora olmaydigan joylarda ishlay oladi", "Odamdan chiroyliroq", "Ovqat yemaydi, shuning uchun arzon"], t: 0 }
      ] }
  ]
};

/* =====================================================================
 * 2-YIL — doimiy, qiyinroq variant (0-2-sinf Makerzoid)
 * 1-yilni o'qigan bola keyingi yil boshqa sinf-mavzuga o'tadi, shuning
 * uchun bu testlar 1-yildagilar bilan TAKRORLANMAYDI.
 * ===================================================================== */
const TESTLAR_2 = {

  "0-sinf": [
    { mavzu: "Muvozanat va elastik energiya",
      savollar: [
        { s: "Og'irlik markazi pastroq bo'lgan model qanday bo'ladi?",
          v: ["Barqarorroq", "Tezroq ag'anaydi", "Yengilroq"], t: 0 },
        { s: "Elastik jism nima?",
          v: ["Singandan keyin tiklanmaydigan jism", "Cho'zilgach yoki siqilgach o'z shakliga qaytadigan jism", "Faqat metall jism"], t: 1 },
        { s: "Cho'zilgan rezinada qanday energiya to'planadi?",
          v: ["Issiqlik energiyasi", "Yorug'lik energiyasi", "Elastik energiya"], t: 2 },
        { s: "Rezina qo'yib yuborilganda energiya nimaga aylanadi?",
          v: ["Harakatga", "Suvga", "Rangga"], t: 0 },
        { s: "Model to'xtaguncha energiya qayerga \"yo'qoladi\"?",
          v: ["Hech qayerga — model buzilgan", "Ishqalanish orqali issiqlikka aylanadi", "Batareyaga qaytadi"], t: 1 },
        { s: "Tebranuvchi muvozanatdagi model turtilsa nima qiladi?",
          v: ["Darhol yiqiladi", "Joyidan qimirlamaydi", "Tebranib, yana muvozanatga qaytadi"], t: 2 },
        { s: "Rezinani ikki barobar ko'proq cho'zsak, model qanday yuradi?",
          v: ["Sezilarli uzoqroq", "Xuddi shunday", "Umuman yurmaydi"], t: 0 },
        { s: "Tayanch maydoni deganda nima tushuniladi?",
          v: ["Modelning balandligi", "Model yerga tayanadigan nuqtalar orasidagi maydon", "Modelning og'irligi"], t: 1 },
        { s: "Qaysi holatda model ag'anaydi?",
          v: ["Og'irlik markazi tayanch ustida bo'lsa", "Model past bo'lsa", "Og'irlik markazi tayanch maydonidan chiqib ketsa"], t: 2 },
        { s: "Pull-back (orqaga tortib qo'yib yuboriladigan) mashina qanday ishlaydi?",
          v: ["Orqaga tortilganda prujina energiya yig'adi, qo'yib yuborilganda harakatga aylantiradi", "Batareya bilan yuradi", "Shamol bilan yuradi"], t: 0 }
      ] },
    { mavzu: "Richag va mustahkam konstruksiya",
      savollar: [
        { s: "Kuch yelkasi nima?",
          v: ["Kuch qo'yilgan nuqtadan tayanchgacha bo'lgan masofa", "Yukning og'irligi", "Richagning rangi"], t: 0 },
        { s: "Yuk yelkasi qisqarsa, yukni ko'tarish qanday bo'ladi?",
          v: ["Qiyinlashadi", "Osonlashadi", "O'zgarmaydi"], t: 1 },
        { s: "Richag muvozanatda: kuch yelkasi 4 birlik, yuk yelkasi 2 birlik. Kuch yukdan qanday?",
          v: ["2 barobar katta", "Teng", "2 barobar kichik"], t: 2 },
        { s: "Ferma konstruksiyasi nimadan tuziladi?",
          v: ["Ko'p uchburchakdan", "Faqat doiralardan", "Bitta katta plastinadan"], t: 0 },
        { s: "Yuk ostidagi ko'prikda kuch qayerga tarqaladi?",
          v: ["Faqat yuk turgan nuqtaga", "Bo'g'inlar orqali tayanchlarga", "Havoga"], t: 1 },
        { s: "Yopiq konstruksiya ochiq konstruksiyadan qanday farq qiladi?",
          v: ["Yengilroq", "Chiroyliroq", "Mustahkamroq — kuch aylana bo'ylab tarqaladi"], t: 2 },
        { s: "To'rtburchak ramka qiyshaymasligi uchun eng kam nechta diagonal kerak?",
          v: ["Bitta", "To'rtta", "Umuman kerak emas"], t: 0 },
        { s: "Burchak kichraysa, konstruksiya tomonlari bir-biriga qanday bo'ladi?",
          v: ["Uzoqlashadi", "Yaqinlashadi", "O'zgarmaydi"], t: 1 },
        { s: "1-toifa richagga misol qaysi?",
          v: ["Zambilg'altak", "Pinset", "Qaychi"], t: 2 },
        { s: "Konstruksiyaning eng zaif joyini qanday topamiz?",
          v: ["Asta yuklab, qayeri egilishini kuzatamiz", "Rangiga qaraymiz", "Otib yuborib sinaymiz"], t: 0 }
      ] },
    { mavzu: "Uzatmalar zanjiri: g'ildirak, shkiv, vint",
      savollar: [
        { s: "Uzatma zanjiri nima?",
          v: ["Bir necha uzatmaning ketma-ket ulanishi", "Velosiped qulfi", "Bitta katta g'ildirak"], t: 0 },
        { s: "Ketma-ket ulangan 3 tishli g'ildirakdan oxirgisi qaysi tomonga aylanadi?",
          v: ["Har doim chapga", "Birinchisi bilan bir xil tomonga", "Aylana olmaydi"], t: 1 },
        { s: "Bir nechta shkivni birga ishlatishdan maqsad nima?",
          v: ["Chiroy", "Ipni uzaytirish", "Ko'tarish kuchini kamaytirish (yengillashtirish)"], t: 2 },
        { s: "Shkiv kuchning YO'NALISHINI o'zgartira oladimi?",
          v: ["Ha — pastga tortib yukni yuqoriga ko'taramiz", "Yo'q, hech qachon", "Faqat katta shkivlar"], t: 0 },
        { s: "Vint mexanizmining afzalligi nima?",
          v: ["Juda tez ishlaydi", "Katta kuch beradi va o'z-o'zidan orqaga qaytmaydi", "Detali kam"], t: 1 },
        { s: "Mexanizm bo'g'inidagi ortiqcha bo'shliq (lyuft) nimaga olib keladi?",
          v: ["Tezlikka", "Tejamkorlikka", "Harakat noaniq bo'lishiga"], t: 2 },
        { s: "Avtomatik ochiladigan darvozada qanday uzatma ishlatilishi mumkin?",
          v: ["Vint yoki tishli uzatma", "Faqat rezina", "Hech qanday"], t: 0 },
        { s: "Uzatma zanjirida har bosqich nimani o'zgartirishi mumkin?",
          v: ["Faqat rangni", "Tezlik, kuch yoki yo'nalishni", "Detal sonini"], t: 1 },
        { s: "Kichik g'ildirak katta g'ildirakni aylantirganda nima YUTAMIZ?",
          v: ["Tezlik", "Hech narsa", "Kuch"], t: 2 },
        { s: "Uzatma nisbati 3:1 degani nima?",
          v: ["Kirish 3 marta aylanganda chiqish 1 marta aylanadi", "3 ta g'ildirak bor", "Model 3 metrga yuradi"], t: 0 }
      ] },
    { mavzu: "Krivoship, trayektoriya va ikki tomonlama harakat",
      savollar: [
        { s: "Krivoship-shatun mexanizmida krivoship nima qiladi?",
          v: ["Aylanadi va shatunni yuritadi", "Faqat turadi", "Modelni bo'yaydi"], t: 0 },
        { s: "Harakat trayektoriyasini qanday ko'rish mumkin?",
          v: ["Trayektoriyani ko'rib bo'lmaydi", "Nuqtaga qalam bog'lab, chizgan yo'lini kuzatib", "Modelni to'xtatib"], t: 1 },
        { s: "Mexanizmni sekin rejimda kuzatishdan maqsad nima?",
          v: ["Vaqtni cho'zish", "Modelni charchatmaslik", "Har bir bo'g'in qanday harakatlanishini aniq ko'rish"], t: 2 },
        { s: "Ikki tomonlama harakat mexanizmi nimani bajara oladi?",
          v: ["Ham oldinga, ham orqaga ish bajarish", "Faqat bir tomonga ishlash", "Hech narsa"], t: 0 },
        { s: "Krivoship radiusi 2 sm dan 4 sm ga oshirilsa, tebranish kengligi qanday o'zgaradi?",
          v: ["2 barobar kamayadi", "Taxminan 2 barobar oshadi", "O'zgarmaydi"], t: 1 },
        { s: "Shatunni uzaytirsak nima o'zgaradi?",
          v: ["Amplituda 10 barobar oshadi", "Mexanizm to'xtaydi", "Harakat xarakteri (siljish egri chizig'i) o'zgaradi"], t: 2 },
        { s: "Tikuv mashinasining ignasi qaysi mexanizm bilan yuqoriga-pastga yuradi?",
          v: ["Krivoship-shatun", "Shkiv", "Faqat prujina"], t: 0 },
        { s: "Bir tekis aylanishdan NOTEKIS (to'xtab-to'xtab) harakat olish mumkinmi?",
          v: ["Yo'q, hech qachon", "Ha — maxsus mexanizmlar bilan", "Faqat suvda"], t: 1 },
        { s: "Trayektoriya doira shaklida bo'lsa, nuqta qanday harakatlangan?",
          v: ["To'g'ri chiziq bo'ylab", "Tebranib", "Aylana bo'ylab"], t: 2 },
        { s: "Mexanizm loyihalashda trayektoriyani oldindan bilish nega muhim?",
          v: ["Qism qayerga borishini bilib, to'qnashuvni oldini olamiz", "Chiroyli bo'lishi uchun", "Muhim emas"], t: 0 }
      ] }
  ],

  "1-sinf": [
    { mavzu: "Krivoship va motor tebranishi",
      savollar: [
        { s: "Motor tezligi oshsa, mexanizm tebranishi qanday o'zgaradi?",
          v: ["Tezlashadi", "Sekinlashadi", "O'zgarmaydi"], t: 0 },
        { s: "Tebranish KENGLIGI (amplituda) nimaga bog'liq?",
          v: ["Motor rangiga", "Krivoship radiusiga", "Xona haroratiga"], t: 1 },
        { s: "Ikki mexanizm navbatma-navbat ishlashi uchun harakat qanday taqsimlanadi?",
          v: ["Ikkalasiga bir vaqtda", "Hech qaysiga", "Bir aylanishning turli qismlarida turli mexanizmga"], t: 2 },
        { s: "Haqiqiy avtomobil dvigatelida krivoship-shatun nima qiladi?",
          v: ["Porshen harakatini aylanishga aylantiradi", "Benzin quyadi", "Chiroq yoqadi"], t: 0 },
        { s: "Motor sekin aylansa, amplituda o'zgaradimi?",
          v: ["Ha, kichrayadi", "Yo'q — faqat tezlik o'zgaradi, kenglik radiusga bog'liq", "Ha, kattalashadi"], t: 1 },
        { s: "Tebranish chastotasi nima?",
          v: ["Tebranishning kengligi", "Tebranishning rangi", "Bir soniyadagi tebranishlar soni"], t: 2 },
        { s: "Krivoshipni motorga qaysi qism orqali ulaymiz?",
          v: ["Val (o'q) orqali", "Ip orqali", "Yelim bilan"], t: 0 },
        { s: "Mexanizm juda tez ishlaganda nima xavfi bor?",
          v: ["Rangi o'chadi", "Bo'g'inlar bo'shashib, detallar chiqib ketishi mumkin", "Hech qanday xavf yo'q"], t: 1 },
        { s: "Bitta motordan ikki xil TEZLIKDAGI harakat olish uchun nima kerak?",
          v: ["Ikkita batareya", "Ikki xil rang", "Turli uzatma nisbatlari"], t: 2 },
        { s: "Real dvigatel bilan model mexanizmning o'xshashligi nimada?",
          v: ["Ikkalasida ham aylanish va tebranish o'zaro aylantiriladi", "Ikkalasi ham benzin ishlatadi", "O'xshashligi yo'q"], t: 0 }
      ] },
    { mavzu: "Kulachok, suzish va masofa sensori",
      savollar: [
        { s: "Kulachok (cam) mexanizmi qanday ishlaydi?",
          v: ["Notekis shaklli disk aylanib, tayanchni ko'tarib-tushiradi", "Ikki g'ildirak tishlashadi", "Ip tortiladi"], t: 0 },
        { s: "Kulachokning krivoshipdan farqi nimada?",
          v: ["Farqi yo'q", "Kulachok shakli bilan harakat qonunini belgilaydi", "Kulachok faqat katta bo'ladi"], t: 1 },
        { s: "Og'ir kema nega cho'kmaydi?",
          v: ["Temir suvdan yengil", "Kema uchadi", "Kengligi katta — itarib chiqaruvchi kuch yetarli"], t: 2 },
        { s: "Suvning itarib chiqaruvchi kuchi nimaga bog'liq?",
          v: ["Jismning suvga botgan hajmiga", "Jismning rangiga", "Suvning chuqurligiga faqat"], t: 0 },
        { s: "Chayqalish harakatida model qanday tebranadi?",
          v: ["Doim bir tomonga aylanadi", "Beshik kabi ikki tomonga", "Faqat yuqoriga"], t: 1 },
        { s: "Masofa sensori qanday to'lqin yuboradi (ko'p hollarda)?",
          v: ["Suv to'lqini", "Radio to'lqin faqat", "Ultratovush to'lqini"], t: 2 },
        { s: "Masofa sensori to'siqni qanday aniqlaydi?",
          v: ["Yuborilgan to'lqin qaytib kelgan vaqtidan", "To'siqni ushlab ko'rib", "Rangidan"], t: 0 },
        { s: "Chegara qiymati (threshold) nima uchun kerak?",
          v: ["Sensor narxini bilish uchun", "Sensor qachon \"ishga tushishini\" belgilash uchun", "To'lqin tezligini oshirish uchun"], t: 1 },
        { s: "Suzuvchi modelni og'irlashtirsak nima bo'ladi?",
          v: ["Balandroq suzadi", "Tezlashadi", "Chuqurroq botadi, oxiri cho'kishi mumkin"], t: 2 },
        { s: "Kulachok shaklini o'zgartirsak, harakat qanday o'zgaradi?",
          v: ["Ko'tarilish-tushish tartibi (ritmi) o'zgaradi", "Hech qanday", "Faqat rang o'zgaradi"], t: 0 }
      ] },
    { mavzu: "Sensor aniqligi va ko'tarish mexanizmlari",
      savollar: [
        { s: "Sensor xatosi nima?",
          v: ["Sensorning haqiqiy qiymatdan chetga chiqishi", "Sensorning narxi", "Sensorning rangi"], t: 0 },
        { s: "Sensor xatosini kamaytirish uchun nima qilamiz?",
          v: ["Sensorni olib tashlaymiz", "Bir necha marta o'lchab, o'rtachasini olamiz", "Tezroq o'lchaymiz"], t: 1 },
        { s: "Vint bilan ko'tarishning boshqa usullardan farqi nima?",
          v: ["Eng tez usul", "Eng rangli usul", "Sekin, lekin yuk o'z-o'zidan tushib ketmaydi"], t: 2 },
        { s: "Kran strelasi uzaysa, ko'tarish qanday o'zgaradi?",
          v: ["Ag'anash xavfi ortadi — kontr-vazn kuchaytiriladi", "Osonlashadi", "Hech narsa o'zgarmaydi"], t: 0 },
        { s: "Kontr-vazn qanday tanlanadi?",
          v: ["Istalgan og'irlikda", "Yuk va strela uzunligiga mos ravishda", "Doim eng og'iri"], t: 1 },
        { s: "Yukni ushlab turish mexanizmi nima uchun kerak?",
          v: ["Chiroy uchun", "Tezlik uchun", "Motor o'chganda yuk tushib ketmasligi uchun"], t: 2 },
        { s: "Bir necha mexanizm birga ishlaganda nimaga e'tibor beramiz?",
          v: ["Ular bir-biriga xalaqit bermasligiga", "Faqat rangiga", "Faqat narxiga"], t: 0 },
        { s: "Strela uzunligi va ko'tarish kuchi qanday bog'langan?",
          v: ["Bog'lanmagan", "Strela uzaysa, xuddi shu motor kamroq yuk ko'taradi", "Strela uzaysa kuch oshadi"], t: 1 },
        { s: "Sensor ikki marta ketma-ket boshqa-boshqa qiymat ko'rsatdi. Bu nima?",
          v: ["Normal — sensor buzilgan emas, aniqlik chegarasi bor", "Sensor sehrlangan", "Model harakatlandi degani faqat"], t: 0 },
        { s: "Ko'tarish mexanizmini sinashda yukni qanday oshiramiz?",
          v: ["Birdan eng og'irini qo'yamiz", "Yuk qo'ymaymiz", "Bosqichma-bosqich, har safar kuzatib"], t: 2 }
      ] },
    { mavzu: "Motor chegaralari va ishqalanish",
      savollar: [
        { s: "Motor uzoq ishlasa nega qiziydi?",
          v: ["Energiyaning bir qismi issiqlikka aylanadi", "Quyosh isitadi", "Motor kasal bo'ladi"], t: 0 },
        { s: "Motor tezligini qanday boshqarish mumkin?",
          v: ["Faqat qo'l bilan ushlab", "Berilayotgan quvvatni o'zgartirib", "Iloji yo'q"], t: 1 },
        { s: "Motorning energiya manbai nima?",
          v: ["Suv", "Havo", "Batareya (elektr)"], t: 2 },
        { s: "Batareya kuchsizlanganda model qanday yuradi?",
          v: ["Sekinroq", "Tezroq", "Xuddi shunday"], t: 0 },
        { s: "Statik ishqalanish qachon ishlaydi?",
          v: ["Jism harakatda bo'lganda", "Jism qo'zg'almay turganda", "Faqat suvda"], t: 1 },
        { s: "G'ildirakli model sudraluvchi modeldan nega kam energiya sarflaydi?",
          v: ["G'ildirak chiroyliroq", "Motor kichikroq", "Dumalash ishqalanishi sirpanishnikidan kichik"], t: 2 },
        { s: "Motor \"zo'riqib\" to'xtab qolsa, birinchi nima qilamiz?",
          v: ["Quvvatni uzamiz — motor kuyishi mumkin", "Kuchliroq bosamiz", "Kutib turamiz"], t: 0 },
        { s: "Ishqalanishni QAYERDA ataylab oshiramiz?",
          v: ["Uzatma o'qlarida", "Tormozda va g'ildirak protektorida", "Hamma joyda"], t: 1 },
        { s: "Motor issiqligi juda oshib ketsa nima xavfi bor?",
          v: ["Rang o'zgaradi", "Hech qanday", "Motor ishdan chiqishi mumkin"], t: 2 },
        { s: "Bir xil motor bilan tezroq yurish uchun nima qilamiz?",
          v: ["Uzatmani tezlikka sozlaymiz va modelni yengillashtiramiz", "Modelni og'irlashtiramiz", "G'ildirakni olib tashlaymiz"], t: 0 }
      ] }
  ],

  "2-sinf": [
    { mavzu: "Transport mexanikasi",
      savollar: [
        { s: "Burilish qanday sodir bo'ladi?",
          v: ["Bir tomon g'ildiraklari boshqa tomondan farqli harakatlanadi", "Model sakraydi", "Motor to'xtaydi"], t: 0 },
        { s: "Motordan g'ildirakkacha kuch nima orqali uzatiladi?",
          v: ["Havo orqali", "Uzatma (tishli g'ildirak, val) orqali", "Magnit orqali"], t: 1 },
        { s: "4 g'ildirakli va 6 g'ildirakli yuk mashinasi: qaysi biri og'ir yukni yaxshi ko'taradi?",
          v: ["4 g'ildirakli", "Farqi yo'q", "6 g'ildirakli — yuk ko'proq nuqtaga taqsimlanadi"], t: 2 },
        { s: "Tezlikka sozlangan uzatmada nimani yo'qotamiz?",
          v: ["Kuchni", "Rangni", "G'ildirakni"], t: 0 },
        { s: "G'ildirak bilan o'q (val) qanday ulanishi kerak?",
          v: ["Bo'sh — aylanib turadigan", "Vazifasiga qarab: yetaklovchi mahkam, erkin g'ildirak bo'sh", "Doim yelimlangan"], t: 1 },
        { s: "Old va orqa g'ildiraklar orasidagi masofa (baza) uzaysa nima o'zgaradi?",
          v: ["Model chiroyli bo'ladi", "Motor kuchayadi", "Yurish barqarorlashadi, burilish kengayadi"], t: 2 },
        { s: "Yetaklovchi g'ildirak qaysi?",
          v: ["Motordan kuch oladigan g'ildirak", "Eng katta g'ildirak", "Old g'ildirak doim"], t: 0 },
        { s: "Transportga yuk ortilganda uzatmani nega kuchga sozlaymiz?",
          v: ["Tezlik muhimroq bo'lgani uchun", "Og'ir yukni qo'zg'atishga katta kuch kerak", "Shunchaki odat"], t: 1 },
        { s: "Model to'g'ri yurmay, bir tomonga og'ib ketsa, sababi nima bo'lishi mumkin?",
          v: ["Rangi noto'g'ri", "Motor charchagan", "G'ildiraklar o'lchami/ishqalanishi farq qiladi"], t: 2 },
        { s: "Tormozsiz model qanday to'xtaydi?",
          v: ["Ishqalanish hisobiga sekin-asta", "Darhol", "Hech qachon to'xtamaydi"], t: 0 }
      ] },
    { mavzu: "Aerodinamika",
      savollar: [
        { s: "Oqimli (aerodinamik) shakl nima beradi?",
          v: ["Havo qarshiligini kamaytiradi", "Og'irlikni oshiradi", "Rangni yaxshilaydi"], t: 0 },
        { s: "Parrak qanotining burchagi kattalashsa nima bo'ladi?",
          v: ["Hech narsa", "Havoni kuchliroq itaradi, lekin aylantirish og'irlashadi", "Parrak to'xtaydi"], t: 1 },
        { s: "Parvozda qanday kuchlar qatnashadi?",
          v: ["Faqat og'irlik", "Faqat tortish", "Ko'tarish, og'irlik, tortish va qarshilik"], t: 2 },
        { s: "Parrak havoni orqaga itarsa, model qayoqqa harakatlanadi?",
          v: ["Oldinga", "Orqaga", "Pastga"], t: 0 },
        { s: "Reaktiv harakat tamoyili qanday?",
          v: ["G'ildirak yerni itaradi", "Oqim bir tomonga — jism qarama-qarshi tomonga", "Magnit tortadi"], t: 1 },
        { s: "Shar ichidan havo chiqib ketayotganda shar qayoqqa uchadi?",
          v: ["Havo chiqayotgan tomonga", "Pastga", "Havo oqimiga qarama-qarshi tomonga"], t: 2 },
        { s: "Tortish kuchi oshsa (qarshilik o'zgarmasa), tezlik qanday o'zgaradi?",
          v: ["Oshadi", "Kamayadi", "O'zgarmaydi"], t: 0 },
        { s: "Nega poyga mashinalarining shakli past va cho'ziq?",
          v: ["Chiroyli ko'rinish uchun", "Havo qarshiligini kamaytirish uchun", "Arzon bo'lishi uchun"], t: 1 },
        { s: "Parashyut qaysi kuchdan foydalanadi?",
          v: ["Ko'tarish kuchidan", "Magnit kuchidan", "Havo qarshiligidan"], t: 2 },
        { s: "Ikki xil parrak sinovida nimani bir xil qoldiramiz?",
          v: ["Motor tezligi va sinov sharoitini", "Hech narsani", "Faqat rangni"], t: 0 }
      ] },
    { mavzu: "Biomimikriya va tabiiy dizayn",
      savollar: [
        { s: "Biomimikriyaning maqsadi nima?",
          v: ["Tabiat yechimlarini texnikada qo'llash", "Hayvonlarni qafasda saqlash", "Rasm chizish"], t: 0 },
        { s: "Qushlarning suyaklari qanday tuzilgan?",
          v: ["Juda og'ir va qattiq", "Ichi g'ovak — yengil, lekin mustahkam", "Rezinadan"], t: 1 },
        { s: "Hayvon dumini modelda nima bilan takrorlash mumkin?",
          v: ["Motor bilan faqat", "G'ildirak bilan", "Harakatlanuvchi bo'g'inli uzun qism bilan"], t: 2 },
        { s: "Rang va naqsh hayvonlarga nima uchun kerak?",
          v: ["Yashirinish yoki ogohlantirish uchun", "Chiroy uchun faqat", "Tezlik uchun"], t: 0 },
        { s: "Askari kiyimidagi kamuflyaj qaysi tabiiy yechimdan olingan?",
          v: ["Qush sayrashidan", "Hayvonlarning yashirinish rangidan", "Daraxt ildizidan"], t: 1 },
        { s: "Uchuvchi hayvonning qanot YUZASI katta bo'lishi nima beradi?",
          v: ["Og'irlikni oshiradi", "Hech narsa", "Ko'proq havoga tayanib, ko'tarilish oson bo'ladi"], t: 2 },
        { s: "Skelet konstruksiyada nimaga mos keladi?",
          v: ["Karkas (ramka)", "Bo'yoq", "G'ildirak"], t: 0 },
        { s: "Delfin shaklidan qaysi transportda foydalanilgan?",
          v: ["Traktorda", "Suv osti kemasida", "Velosipedda"], t: 1 },
        { s: "Hayvon oyog'idagi bo'g'in modeldagi nimaga o'xshaydi?",
          v: ["Yelimga", "Bo'yoqqa", "Sharnir (aylanadigan birikma)ga"], t: 2 },
        { s: "Tabiatdan g'oya olishdan oldin nima qilamiz?",
          v: ["Hayvon harakatini diqqat bilan kuzatamiz", "Darhol quramiz", "Rasm sotib olamiz"], t: 0 }
      ] },
    { mavzu: "Notekis yuza va kosmik texnika",
      savollar: [
        { s: "Notekis yuzada qaysi g'ildirak yaxshi yuradi?",
          v: ["Katta va protektorli (naqshli)", "Kichkina va silliq", "Yassi"], t: 0 },
        { s: "Marsoxod g'ildiraklari nega mustaqil harakatlana oladi?",
          v: ["Chiroyli bo'lishi uchun", "Har g'ildirak notekislikka moslashishi uchun", "Tezlik uchun"], t: 1 },
        { s: "Past gravitatsiyada sakrab ketmaslik uchun rover qanday yurishi kerak?",
          v: ["Juda tez", "Sakrab-sakrab", "Sekin va tekis"], t: 2 },
        { s: "Kosmik aloqa qanday amalga oshadi?",
          v: ["Antenna va radio to'lqinlar orqali", "Sim orqali", "Ovoz bilan"], t: 0 },
        { s: "Nega kosmik texnikada har qism ikki-uch marta tekshiriladi?",
          v: ["Vaqt ko'p bo'lgani uchun", "Kosmosda ta'mirlab bo'lmaydi", "Qoida shunaqa"], t: 1 },
        { s: "Namuna olish mexanizmi qanday qismlardan iborat bo'lishi mumkin?",
          v: ["Faqat g'ildirakdan", "Faqat antennadan", "Qazish qismi va saqlash idishidan"], t: 2 },
        { s: "Kosmosdagi katta harorat farqiga qanday chidaladi?",
          v: ["Maxsus himoya qatlamlari bilan", "Hech qanday himoya kerak emas", "Suv sepib"], t: 0 },
        { s: "6 g'ildirakli roverning bir g'ildiragi toshga chiqsa nima bo'ladi?",
          v: ["Rover ag'anaydi", "Qolgan g'ildiraklar yerda qoladi — rover barqaror", "Rover to'xtaydi"], t: 1 },
        { s: "G'ildirak protektorining (naqshining) vazifasi nima?",
          v: ["Chiroy", "Og'irlik qo'shish", "Sirt bilan tishlashishni oshirish"], t: 2 },
        { s: "Ishonchli kosmik model qurishda eng muhim tamoyil qaysi?",
          v: ["Oddiy va puxta konstruksiya", "Iloji boricha murakkab qilish", "Faqat tez qurish"], t: 0 }
      ] }
  ]
};

/* =====================================================================
 * SPIKE (2-yil 3- va 4-sinf) — dastur bir xil, testlar ham umumiy
 * ===================================================================== */
const TEST_SPIKE = [
  { mavzu: "SPIKE Prime: qismlar va yig'ish",
    savollar: [
      { s: "SPIKE Prime to'plamining \"miyasi\" qaysi qism?",
        v: ["Hub (dasturlanadigan blok)", "Katta motor", "G'ildirak"], t: 0 },
      { s: "Motor va sensorlar Hub'ga qanday ulanadi?",
        v: ["Yelim bilan", "Portlarga kabel orqali", "Simsiz faqat"], t: 1 },
      { s: "Driving Base nima?",
        v: ["O'yin maydoni", "Dastur nomi", "Ikki motorli harakatlanuvchi robot asosi"], t: 2 },
      { s: "Robot to'g'ri yurishi uchun ikkala motor qanday ishlashi kerak?",
        v: ["Bir xil tezlikda", "Har xil tezlikda", "Faqat bittasi"], t: 0 },
      { s: "Attachment nima?",
        v: ["Dastur xatosi", "Robotga taqiladigan almashtiriladigan qo'shimcha mexanizm", "Batareya turi"], t: 1 },
      { s: "Yig'ishda rasmli instruksiyaga rioya qilish nega muhim?",
        v: ["Tezroq tugatish uchun faqat", "O'qituvchi xafa bo'lmasligi uchun", "Bitta xato keyingi bosqichlarni buzadi"], t: 2 },
      { s: "Robot Arm (robot-qo'l) qanday vazifani bajaradi?",
        v: ["Narsalarni ushlab ko'taradi", "Faqat yuradi", "Musiqa chaladi"], t: 0 },
      { s: "Line Follower attachment'da sensor qayerga qaraydi?",
        v: ["Osmonga", "Pastga — chiziqni ko'rish uchun", "Orqaga"], t: 1 },
      { s: "Ultrasonik sensor qanday o'lchaydi?",
        v: ["Rangni solishtiradi", "Og'irlikni tortadi", "Tovush to'lqini yuborib, qaytish vaqtini o'lchaydi"], t: 2 },
      { s: "Yig'ilgan modelni sinashdan oldin nimani tekshiramiz?",
        v: ["Barcha birikmalar mahkamligini va kabellar ulanganini", "Faqat rangini", "Hech narsani"], t: 0 }
    ] },
  { mavzu: "SPIKE sensorlari va dasturlash",
    savollar: [
      { s: "Rang sensori nimani aniqlaydi?",
        v: ["Sirt rangini va yorug'likni", "Masofani", "Og'irlikni"], t: 0 },
      { s: "Chiziq kuzatishda robot qora chiziqdan chiqib ketsa nima qilishi kerak?",
        v: ["To'xtab qolishi", "Chiziq tomonga burilishi", "Tezlashishi"], t: 1 },
      { s: "\"Agar ... aks holda\" (if/else) bloki nima qiladi?",
        v: ["Dasturni o'chiradi", "Robotni tezlashtiradi", "Shartga qarab ikki yo'ldan birini tanlaydi"], t: 2 },
      { s: "Ultrasonik sensor bilan robot to'siq oldida to'xtashi uchun dasturda nima bo'lishi kerak?",
        v: ["Masofa shartdan kichik bo'lsa - to'xtash buyrug'i", "Faqat oldinga yurish", "Rang tekshirish"], t: 0 },
      { s: "Gyroskopik sensor nimani o'lchaydi?",
        v: ["Rangni", "Burilish burchagini", "Masofani"], t: 1 },
      { s: "90 gradusga ANIQ burilish uchun qaysi sensor eng qulay?",
        v: ["Rang sensori", "Bosim sensori", "Gyroskopik sensor"], t: 2 },
      { s: "Kuch (bosim) sensori qachon signal beradi?",
        v: ["Bosilganda", "Yorug'lik tushganda", "Ovoz chiqqanda"], t: 0 },
      { s: "Bir nechta sensorni birlashtirish nima beradi?",
        v: ["Dastur qisqaradi", "Robot bir vaqtda bir necha narsani kuzata oladi", "Batareya tejaladi"], t: 1 },
      { s: "Dastur kutilgandek ishlamasa nima qilamiz?",
        v: ["Robotni almashtiramiz", "Boshqa dastur yozamiz darhol", "Qadamma-qadam tekshirib, xatoni topamiz"], t: 2 },
      { s: "Aqlli parking robot qanday ishlaydi?",
        v: ["Sensor bo'sh joyni aniqlab, robot o'zi to'xtaydi", "Odam pult bilan boshqaradi", "Tasodifiy to'xtaydi"], t: 0 }
    ] },
  { mavzu: "FLL missiyalari: strategiya va ball",
    savollar: [
      { s: "FLL musobaqasida missiya nima?",
        v: ["Maydonchadagi ball beriladigan aniq vazifa", "Robot nomi", "Jamoa qo'shig'i"], t: 0 },
      { s: "Missiya bajarishdan oldin nima tuziladi?",
        v: ["Yangi robot", "Reja (strategiya)", "Yangi maydon"], t: 1 },
      { s: "Yuk tashish missiyasida attachment qanday bo'lishi kerak?",
        v: ["Og'ir va katta", "Chiroyli", "Yukni ishonchli ushlab, kerakli joyda qo'yib yuboradigan"], t: 2 },
      { s: "Robot chiziq bo'ylab yetkazishda qaysi sensordan foydalanadi?",
        v: ["Rang sensori", "Bosim sensori", "Harorat sensori"], t: 0 },
      { s: "Sinovda robot vazifani bajara olmadi. To'g'ri xulosa qaysi?",
        v: ["Robot yaroqsiz", "Xato sababini topib, dastur yoki mexanizmni tuzatamiz", "Missiyani tashlab ketamiz"], t: 1 },
      { s: "Ball tizimi nimani belgilaydi?",
        v: ["Robot narxini", "Jamoa yoshini", "Har missiya uchun beriladigan ochkolarni"], t: 2 },
      { s: "Ikki missiyani ketma-ket bajarish uchun dastur qanday tuziladi?",
        v: ["Bosqichlar ketma-ketligi sifatida", "Ikkita alohida robotga", "Dastur kerak emas"], t: 0 },
      { s: "Attachmentni tez almashtirish nega muhim?",
        v: ["Chiroyli ko'rinadi", "Musobaqada vaqt cheklangan", "Ustoz talab qiladi"], t: 1 },
      { s: "Yakuniy sinov (ballga qo'yiladigan) oldidan nima qilamiz?",
        v: ["Dam olamiz", "Yangi robot quramiz", "Mashq sinovlarini o'tkazib, barqaror natijaga erishamiz"], t: 2 },
      { s: "Missiya natijasini tahlil qilishda nimani yozib boramiz?",
        v: ["Urinish, natija va xato sabablarini", "Faqat g'alabalarni", "Hech narsani"], t: 0 }
    ] },
  { mavzu: "To'liq missiya turi va jamoaviy ish",
    savollar: [
      { s: "To'liq missiya turida vaqt chegarasi qancha (FLL formatida)?",
        v: ["2,5 daqiqa", "1 soat", "10 soniya"], t: 0 },
      { s: "4 missiyani qaysi tartibda bajargan ma'qul?",
        v: ["Istalgan tartibda, o'ylamasdan", "Eng ko'p ball va eng qulay yo'l hisobiga tuzilgan tartibda", "Faqat oson missiyalarni"], t: 1 },
      { s: "Muhandislik daftari (Inventor Notebook) nima uchun yuritiladi?",
        v: ["Rasm chizish uchun", "Baho olish uchun faqat", "G'oyalar, sinovlar va xulosalarni hujjatlash uchun"], t: 2 },
      { s: "Jamoada vazifalar qanday taqsimlanadi?",
        v: ["Har kim kuchli tomoniga qarab mas'ul bo'ladi", "Hamma hamma narsani qiladi", "Faqat sardor ishlaydi"], t: 0 },
      { s: "Robot start zonasidan chiqqanda unga qo'l tegizish mumkinmi?",
        v: ["Ha, doim", "Yo'q — jarima bo'lishi mumkin, qoidaga qarab", "Faqat sardorga mumkin"], t: 1 },
      { s: "Missiya turi paytida dastur ishlamay qolsa nima qilamiz?",
        v: ["Musobaqani tashlab ketamiz", "Yig'laymiz", "Robotni bazaga qaytarib, keyingi dasturni ishga tushiramiz"], t: 2 },
      { s: "Taqdimotda nimani ko'rsatamiz?",
        v: ["Yechimimiz qanday ishlashi va qanday qarorlar qabul qilganimizni", "Faqat robotning rasmini", "Boshqa jamoaning ishini"], t: 0 },
      { s: "Vaqtni tejash uchun attachmentlar qanday loyihalanadi?",
        v: ["Katta va og'ir", "Tez taqiladigan-yechiladigan", "Yelimlangan"], t: 1 },
      { s: "Repetitsiya (mashq turi) nima beradi?",
        v: ["Vaqtni behuda sarflaydi", "Faqat charchatadi", "Xatolarni musobaqadan OLDIN topib tuzatish imkonini"], t: 2 },
      { s: "Yakuniy turnirda eng muhim natija nima?",
        v: ["O'rganilgan ko'nikma va jamoaviy tajriba", "Faqat oltin medal", "Boshqalardan ustun kelish"], t: 0 }
    ] }
];

/* ================================================================ dars quruvchi */

const SOFT = [
  "Halollik — testni mustaqil yechish, ko'chirmaslik. Natija qanday bo'lsa ham, u O'ZINGIZNIKI bo'lsin.",
  "Diqqatni jamlash — 20 daqiqa davomida chalg'imasdan ishlash, savolni oxirigacha o'qish.",
  "Xatodan o'rganish — noto'g'ri javob \"yomon\" degani emas; qaysi mavzuni takrorlash kerakligini ko'rsatadigan belgi.",
  "O'zini baholash — testdan oldin qaysi savollarga ishonchingiz komil ekanini his qilish va yakunda solishtirish."
];

const TEST_LUGAT = [
  "Test (Test) – bilimni tekshiradigan savollar to'plami",
  "Variant (Option) – savolga taklif qilingan javoblardan biri",
  "Javoblar kaliti (Answer key) – to'g'ri javoblar ro'yxati, faqat o'qituvchida bo'ladi",
  "Baholash shkalasi (Grading scale) – nechta to'g'ri javob qaysi bahoga tengligi"
];

const SHKALA = [
  "9-10 ta to'g'ri javob = 5 (a'lo)",
  "7-8 ta to'g'ri javob = 4 (yaxshi)",
  "5-6 ta to'g'ri javob = 3 (qoniqarli)",
  "3-4 ta to'g'ri javob = 2 (qoniqarsiz)",
  "0-2 ta to'g'ri javob = FAILED"
];

function testTop(yil, sinf, chorakNo) {
  if (yil === "2-yil" && (sinf === "3-sinf" || sinf === "4-sinf")) {
    return TEST_SPIKE[chorakNo - 1] || null;
  }
  const jadval = (yil === "2-yil" && TESTLAR_2[sinf]) ? TESTLAR_2 : TESTLAR;
  return (jadval[sinf] || [])[chorakNo - 1] || null;
}

function nazoratDarsi(yil, sinf, chorakNo) {
  const test = testTop(yil, sinf, chorakNo);
  if (!test) return null;

  const oy = (chorakNo - 1) * 2 + 1;                    // yil bo'yicha oy raqami
  const harf = ["A", "B", "C"];
  // 0-1-sinfda bolalar hali ravon o'qimaydi — savollar ovoz chiqarib o'qiladi
  const ogzaki = (sinf === "0-sinf" || sinf === "1-sinf");

  const sarlavha = oy + "-oylik nazorat (NAZARIY TEST) — \"" + test.mavzu +
    "\": 10 ta savol, 3 variantli, 20 daqiqa. Baholash: 9-10 = 5; 7-8 = 4; " +
    "5-6 = 3; 3-4 = 2; 0-2 = FAILED.";

  return {
    nom: sarlavha,
    kontent: {
      maqsad: [
        "O'quvchilar \"" + test.mavzu + "\" bo'yicha chorakning shu kungacha o'tilgan " +
          "darslarida olgan nazariy bilimlarini test orqali namoyish etadilar.",
        "Har bir o'quvchi " + oy + "-oy uchun jurnal bahosini oladi — bu oylik " +
          "nazorat bahosi hisoblanadi.",
        "O'quvchilar test natijasi orqali qaysi mavzuni takrorlash kerakligini aniqlaydilar."
      ],
      lugat: TEST_LUGAT,
      softSkill: SOFT[chorakNo - 1],
      resurslar: [
        "Har bir o'quvchi uchun test varag'i (chop etilgan) yoki savollar doskaga/ekranga chiqariladi",
        "Javob varag'i: 1 dan 10 gacha raqam va A/B/C katakchalari",
        "Qalam va o'chirg'ich",
        "O'qituvchi uchun javoblar kaliti (6.2-bo'lim) — o'quvchilarga ko'rsatilmaydi"
      ],
      nazariya: [
        {
          title: "5.1. O'tkazish instruksiyasi (o'qituvchi uchun)",
          points: [
            "Test darsning birinchi yarmida o'tkaziladi — savollarga 20 daqiqa ajratiladi.",
            ogzaki
              ? "Savollar o'qituvchi tomonidan baland ovozda, har biri 2 martadan o'qib beriladi; o'quvchilar javob varag'ida mos katakchani (A/B/C) belgilaydilar."
              : "Har bir o'quvchi mustaqil ishlaydi: varaqlar tarqatilgach savollar izohlanmaydi, faqat texnik savolga (varaq, qalam) javob beriladi.",
            "Partalar oralig'i ochiladi, kitob-daftarlar yig'ishtiriladi; testda kitobdan foydalanilmaydi.",
            "Har savolda FAQAT BITTA to'g'ri javob bor — o'quvchilarga bu boshida aytiladi.",
            "Vaqt tugagach varaqlar yig'ib olinadi va shu darsning o'zida javoblar kaliti bo'yicha tekshiriladi."
          ]
        },
        {
          title: "5.2. Baholash shkalasi",
          points: SHKALA.concat([
            "Baho jurnalga " + oy + "-OYLIK NAZORAT bahosi sifatida qo'yiladi — " +
              "o'qituvchining oylik hisobotiga aynan shu baho kiradi.",
            "Shkala testdan OLDIN doskaga yoziladi va o'zgartirilmaydi."
          ])
        }
      ],
      amaliy: [
        {
          title: "6.1. Test savollari (20 daqiqa)",
          points: test.savollar.map(function (q, i) {
            return (i + 1) + "-savol. " + q.s + "  A) " + q.v[0] +
              ".  B) " + q.v[1] + ".  C) " + q.v[2] + ".";
          })
        },
        {
          title: "6.2. Javoblar kaliti (FAQAT o'qituvchi uchun)",
          points: [
            test.savollar.map(function (q, i) {
              return (i + 1) + "-" + harf[q.t];
            }).join(",  "),
            "Tekshirishda har to'g'ri javob 1 ball; yarim ball yo'q."
          ]
        },
        {
          title: "6.3. Xatolar tahlili (15 daqiqa)",
          points: [
            "Varaqlar tekshirilgach eng ko'p xato qilingan 3 ta savol doskada birgalikda yechiladi.",
            "Har bir o'quvchi o'zi xato qilgan savol mavzusini daftariga yozib qo'yadi.",
            "Baholar e'lon qilinadi va jurnal hamda oylik hisobotga kiritiladi."
          ]
        }
      ],
      uyga: [
        "Testda xato qilgan savollaringiz mavzusini darslikdagi (daftardagi) yozuvlardan topib takrorlang.",
        "Shu mavzu bo'yicha o'zingiz 1 ta yangi test savoli tuzib keling — 3 varianti va to'g'ri javobi bilan."
      ]
    }
  };
}

module.exports = { faol: true, TESTLAR, TESTLAR_2, TEST_SPIKE, testTop, nazoratDarsi };
