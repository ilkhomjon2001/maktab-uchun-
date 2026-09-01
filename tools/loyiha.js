/*
 * OYLIK NAZORAT — AMALIY LOYIHA-IMTIHON (har chorakning 18-darsi)
 * ===============================================================
 * 2026-09-01 dan tuzilma o'zgardi (foydalanuvchi so'rovi):
 *   - har chorakda 2 ta baholanadigan nuqta bor:
 *       9-dars  = NAZARIY TEST (nazorat.js)          -> 1-oy bahosi
 *       18-dars = AMALIY LOYIHA-IMTIHON (shu fayl)   -> 2-oy bahosi
 *   - loyiha endi "erkin ijod" emas, balki CHECK-LIST bo'yicha
 *     baholanadigan amaliy imtihon: 10 band, har band 1 ball.
 *     9-10 ball = 5;  7-8 = 4;  5-6 = 3;  3-4 = 2;  0-2 = FAILED.
 *   - eski chorak-oxiri musobaqalarining o'lchanadigan sinovlari
 *     check-listning "sinov" bandlariga kiritilgan.
 *
 * Loyiha talabi sinfdan sinfga O'SADI:
 *   0-sinf : bitta modelni o'zgartirish
 *   1-sinf : ikki mexanizmni birlashtirish
 *   2-sinf : berilgan talabga javob beradigan qurilma loyihalash
 *   3-sinf : hayotdagi muammoni tanlab, yechim qurish va o'lchash
 *   4-sinf : to'liq muhandislik tsikli (talab -> eskiz -> qurish -> sinov -> takomil)
 *
 * Har yozuv:
 *   nom     — loyiha mavzusi
 *   vazifa  — nima qurilishi kerakligi (bitta gap)
 *   talab   — bajarilishi SHART bo'lgan shartlar
 *   etibor  — nimalarga e'tibor berish kerak (o'quvchiga yo'l-yo'riq)
 *   tekshir — check-listning loyihaga XOS 6 bandi (har biri 1 ball);
 *             qolgan 4 umumiy band quruvchi tomonidan qo'shiladi
 *   savol   — taqdimotdagi asosiy savol
 */

/* =====================================================================
 * 1-YIL — maktabning birinchi yili
 * ===================================================================== */
const LOYIHA = {
  "0-sinf": [
    { nom: "Eng uzoq yuradigan model",
      vazifa: "chorakdagi elastik yoki inersiyali modellardan birini tanlab, uni imkon qadar uzoq yuradigan qilib o'zgartirish",
      talab: ["Modelga kamida 1 ta o'zgartirish kiritilsin",
              "O'zgartirishdan oldingi va keyingi masofa o'lchab yozilsin"],
      etibor: ["Masofani nima to'xtatadi — ishqalanishmi, energiya tugashimi, shuni o'ylab o'zgartirish tanlang",
               "G'ildiraklar erkin aylanishini har o'zgartirishdan keyin tekshiring",
               "O'lchovni har safar bir xil joydan (start chizig'idan) boshlang"],
      tekshir: ["Model o'zi yuradi — itarilmaydi, elastik/inersiya kuchi bilan harakatlanadi",
                "Modelga kamida 1 ta aniq o'zgartirish kiritilgan va bola uni ko'rsata oladi",
                "O'zgartirishdan OLDINGI masofa o'lchab, daftarga yozilgan",
                "O'zgartirishdan KEYINGI masofa o'lchab, daftarga yozilgan",
                "Sinov: model start chizig'idan kamida 1 metr yuradi",
                "Masofa avvalgidan oshgan yoki bola nega oshmaganini tushuntira olgan"],
      savol: "Nima o'zgartirdingiz va masofa qanchaga o'zgardi?" },
    { nom: "O'zimning richagli qurilmam",
      vazifa: "richag qonunidan foydalanib, biror narsani ko'taradigan yoki qisadigan o'z qurilmangizni qurish",
      talab: ["Qurilmada tayanch nuqtasi aniq ko'rinsin",
              "Qurilma kamida 1 ta detalni ko'tara olsin"],
      etibor: ["Tayanch nuqtasining joyi kuchni belgilaydi — uni surib eng qulay joyni toping",
               "Richag egilmasligi uchun mustahkam uzun detal tanlang",
               "Yuk qo'yiladigan joyni oldindan belgilab oling"],
      tekshir: ["Qurilmada richag va tayanch nuqtasi bor, bola ularni ko'rsatib bera oladi",
                "Tayanch nuqtasi mahkam — ishlaganda joyidan siljimaydi",
                "Sinov: qurilma kamida 1 ta detal-yukni ko'taradi yoki qisadi",
                "Sinov: yuk 2 barobar oshirilganda qurilma sinmaydi (ko'tara olmasa ham)",
                "Bola tayanch nuqtasini surganda nima o'zgarishini ko'rsatib berdi",
                "Kuch yelkasi yuk yelkasidan uzun qilib tanlangan (yengil ko'tarish uchun)"],
      savol: "Tayanch nuqtasini qayerga qo'ydingiz va nega aynan u yerga?" },
    { nom: "Mustahkam minora",
      vazifa: "iloji boricha baland, lekin turg'un konstruksiya qurish",
      talab: ["Minora o'z-o'zidan tik tursin (ushlab turilmasin)",
              "Konstruksiyada uchburchak ishlatilsin", "Balandligi o'lchab yozilsin"],
      etibor: ["Pastki qavat keng va og'ir, yuqori qavat yengil bo'lsin",
               "Har qavatni qo'shishdan oldin oldingi qavat qimirlamasligini tekshiring",
               "Uchburchaklar burchaklarga qo'yilsa ko'proq foyda beradi"],
      tekshir: ["Minora o'z-o'zidan tik turadi, hech kim ushlab turmaydi",
                "Konstruksiyada kamida 2 ta uchburchak ishlatilgan va bola ularni ko'rsatadi",
                "Balandlik o'lchab, daftarga yozilgan",
                "Sinov: minora kamida 40 sm baland",
                "Sinov: stol sekin turtilganda (tebranish sinovi) minora yiqilmaydi",
                "Pastki qismi yuqorisidan keng — og'irlik markazi pastda"],
      savol: "Minorangiz qayeri eng kuchsiz edi?" },
    { nom: "Tezlashtirgich",
      vazifa: "tishli g'ildirak yoki shkiv uzatmasi qurib, chiqish qismini kirishdan tezroq aylantirish",
      talab: ["Kamida 2 ta tishli g'ildirak yoki shkiv ishlatilsin",
              "Kirish va chiqish aylanishlari sanab, nisbati yozilsin"],
      etibor: ["Tezlik uchun KATTA g'ildirak kichigini aylantirishi kerak",
               "G'ildiraklar tishlari to'liq tishlashsin — oraliq qolsa sirpanadi",
               "O'qlar egilmasligi uchun ikki tomondan tayanch bering"],
      tekshir: ["Uzatmada kamida 2 ta tishli g'ildirak yoki shkiv bor",
                "Kirish aylantirilganda chiqish ham aylanadi — uzatma sirpanmaydi",
                "Chiqish kirishdan TEZROQ aylanadi (kuzatishda aniq ko'rinadi)",
                "Kirish 1 marta aylanganda chiqish necha marta aylangani sanab yozilgan",
                "Uzatma nisbati to'g'ri aytilgan (masalan: 3 ga 1)",
                "Sinov: uzatma 10 marta ketma-ket aylantirilganda buzilmaydi"],
      savol: "Tezlik oshganda kuch nima bo'ldi?" }
  ],

  "1-sinf": [
    { nom: "Harakatlanuvchi o'yinchoq",
      vazifa: "krivoship mexanizmiga o'z figurangizni qo'shib, harakatlanuvchi o'yinchoq yasash",
      talab: ["Qo'l aylantirilganda figura harakatlansin",
              "Mexanizm tiqilib qolmasin"],
      etibor: ["Avval mexanizmni ishlating, figurani KEYIN qo'shing",
               "Figura yengil bo'lsin — og'ir figura mexanizmni to'xtatadi",
               "Krivoship radiusi figuraning harakat kengligini belgilashini eslang"],
      tekshir: ["Krivoship mexanizmi to'g'ri yig'ilgan va aylanadi",
                "O'z figurasi qo'shilgan (instruksiyadagi modeldan farq qiladi)",
                "Qo'l aylantirilganda figura aniq ko'rinadigan harakat qiladi",
                "Sinov: mexanizm 20 marta aylantirilganda birer marta ham tiqilmaydi",
                "Figura mexanizmdan chiqib ketmaydi, mahkam o'rnatilgan",
                "Bola figuraning harakat turini (tebranma/aylanma) to'g'ri aytadi"],
      savol: "Figurangiz qanday harakat qiladi — tebranmami, aylanmami?" },
    { nom: "Ikki harakat bitta mexanizmda",
      vazifa: "bitta krivoshipdan ikki xil harakat chiqaradigan mexanizm qurish",
      talab: ["Ikkala harakat ham bir vaqtda ishlasin",
              "Harakatlar bir-biridan farq qilsin (masalan: biri yuqoriga-pastga, ikkinchisi oldinga-orqaga)"],
      etibor: ["Ikkinchi harakatni krivoshipning boshqa nuqtasidan yoki uzatma orqali oling",
               "Ikkala mexanizm bir-biriga urilmasligini oldindan tekshiring",
               "Bitta harakat ishlagach ikkinchisini qo'shing — birdan ikkalasini emas"],
      tekshir: ["Mexanizmda bitta krivoship va undan chiqadigan IKKITA harakat bor",
                "Ikkala harakat bir vaqtda ishlaydi",
                "Harakatlar turi bir-biridan aniq farq qiladi",
                "Sinov: 15 marta aylantirilganda ikkala harakat ham uzluksiz ishlaydi",
                "Bola qaysi qism qaysi harakatni berayotganini ko'rsatib beradi",
                "Bo'g'inlarda ortiqcha bo'shliq yo'q — harakat taqillamaydi"],
      savol: "Bitta aylanishdan ikki xil harakat qanday chiqdi?" },
    { nom: "Sozlanadigan mexanizm",
      vazifa: "tebranish kengligini foydalanuvchi o'zgartira oladigan mexanizm qurish",
      talab: ["Kamida 2 ta sozlash holati bo'lsin",
              "Har holatda tebranish kengligi o'lchab yozilsin"],
      etibor: ["Kenglikni krivoship radiusini o'zgartirish orqali sozlash eng ishonchli yo'l",
               "Sozlash oson bo'lsin — butun mexanizmni qayta yig'ish talab qilinmasin",
               "O'lchashda tebranishning ikki chekka nuqtasini belgilang"],
      tekshir: ["Mexanizm kamida 2 ta sozlash holatiga ega",
                "Holatni almashtirish 1 daqiqadan kam vaqt oladi",
                "1-holatda tebranish kengligi o'lchab yozilgan",
                "2-holatda tebranish kengligi o'lchab yozilgan",
                "Ikki holat orasidagi farq aniq ko'rinadi (kamida 2 sm)",
                "Bola kenglik nimaga bog'liqligini to'g'ri tushuntiradi"],
      savol: "Sozlashni qanday qildingiz — nimani surdingiz yoki almashtirdingiz?" },
    { nom: "Mexanizm teatri",
      vazifa: "yil davomida o'rgangan mexanizmlardan 2-3 tasini birlashtirib, kichik sahna yasash",
      talab: ["Kamida 2 ta turli mexanizm ishlatilsin", "Sahnada bir kichik voqea ko'rsatilsin",
              "Mexanizmlar bir vaqtda ishlasin"],
      etibor: ["Avval har mexanizmni alohida ishlating, keyin birlashtiring",
               "Voqeani oldindan o'ylab oling — mexanizm voqeaga xizmat qilsin",
               "Umumiy yuritma (bitta dasta yoki motor) rejalashtiring"],
      tekshir: ["Sahnada kamida 2 ta TURLI mexanizm ishlatilgan (bola turlarini aytadi)",
                "Mexanizmlar bir vaqtda, bir yuritmadan ishlaydi",
                "Sahna aniq bir voqeani ko'rsatadi va bola uni aytib beradi",
                "Sinov: sahna 30 soniya uzluksiz ishlaydi",
                "Mexanizmlar bir-biriga xalaqit bermaydi",
                "Konstruksiya sahna asosiga mahkam o'rnatilgan"],
      savol: "Qaysi mexanizmni birlashtirish eng qiyin bo'ldi?" }
  ],

  "2-sinf": [
    { nom: "Ogohlantiruvchi qurilma",
      vazifa: "biror narsani sezib, ogohlantirish beradigan qurilma loyihalash",
      talab: ["Qurilma sensor bilan ishlasin", "Ogohlantirish aniq ko'rinsin yoki eshitilsin",
              "5 sinovdan kamida 4 tasida to'g'ri ishlasin"],
      etibor: ["Avval NIMANI sezish kerakligini aniq yozib oling",
               "Sensorni seziladigan narsa albatta o'tadigan joyga o'rnating",
               "Chegara qiymatini sinab-sinab toping — birinchi qiymat kamdan-kam to'g'ri chiqadi"],
      tekshir: ["Qurilma nimani sezishi bir gapda yozilgan",
                "Sensor to'g'ri joyga o'rnatilgan va mahkam turibdi",
                "Ogohlantirish aniq ko'rinadi yoki eshitiladi",
                "Sinov: 5 sinovdan kamida 4 tasida qurilma to'g'ri ishladi (natija yozilgan)",
                "Yolg'on ishga tushish tekshirilgan: sezilmasligi kerak narsada jim turadi",
                "Bola sezish-qaror-harakat zanjirini o'z qurilmasida ko'rsatib beradi"],
      savol: "Qurilmangiz qayerda kerak bo'lardi?" },
    { nom: "Ikki sensorli model",
      vazifa: "ikki xil signalga ikki xil javob beradigan model qurish",
      talab: ["Ikki sensor mustaqil ishlasin",
              "Javoblar bir-biridan farq qilsin", "Har javob sinab ko'rsatilsin"],
      etibor: ["Har sensorga alohida vazifa bering — bitta narsani ikki sensor kuzatmasin",
               "Avval bitta sensorni to'liq ishlating, keyin ikkinchisini qo'shing",
               "Ikkala signal birdan kelganda nima bo'lishini oldindan o'ylang"],
      tekshir: ["Modelda 2 ta sensor bor va har birining vazifasi aytilgan",
                "1-sensor signaliga model to'g'ri javob beradi (sinab ko'rsatildi)",
                "2-sensor signaliga model BOSHQA javob beradi (sinab ko'rsatildi)",
                "Sensorlar bir-biriga xalaqit bermaydi",
                "Sinov: har sensor 3 martadan tekshirilib, natija jadvalga yozilgan",
                "Bola ikkala signal birdan kelganda nima bo'lishini tushuntiradi"],
      savol: "Ikkala sensor bir vaqtda ishga tushsa nima bo'ladi?" },
    { nom: "Avtomatik ombor",
      vazifa: "yukni sezib, ko'tarib, boshqa joyga qo'yadigan tizim loyihalash",
      talab: ["Sezish va ko'tarish bosqichlari birga ishlasin",
              "Yuk tushib ketmasin", "Tizim 3 marta ketma-ket ishlasin"],
      etibor: ["Tizimni bosqichlarga bo'ling: sezish - ushlash - ko'tarish - qo'yish",
               "Yukni ushlaydigan qism yuk shakliga mos bo'lsin",
               "Har bosqichni alohida sinang, keyin ulang"],
      tekshir: ["Tizim yukni sensor bilan sezadi",
                "Yuk ishonchli ushlanadi va ko'tarilganda tushib ketmaydi",
                "Yuk belgilangan boshqa joyga qo'yiladi",
                "Sinov: tizim 3 marta KETMA-KET to'liq tsiklni bajaradi",
                "Bosqichlar orasida qo'l aralashuvi minimal (faqat yukni berish mumkin)",
                "Bola qaysi bosqich eng ko'p xato berganini va sababini aytadi"],
      savol: "Tizimingiz qaysi bosqichda eng ko'p xato qildi?" },
    { nom: "Maktabga robot",
      vazifa: "maktabdagi biror ishni yengillashtiradigan yuk ko'targich robot loyihalash",
      talab: ["Muammo bir gapda yozilsin", "Robot o'sha muammoni hal qilsin",
              "Ish vaqti o'lchab yozilsin"],
      etibor: ["Haqiqiy muammo tanlang: kitob tashish, bo'r yetkazish, doska artish...",
               "Robot ko'taradigan yukning og'irligi va o'lchamini oldindan aniqlang",
               "Barqarorlikni tekshiring — yuk ko'tarilganda ag'anamasin"],
      tekshir: ["Muammo bir gapda aniq yozilgan",
                "Robot aynan shu muammoga mos qurilgan (bola bog'liqlikni tushuntiradi)",
                "Sinov: robot belgilangan yukni ko'tarib, joyiga yetkazadi",
                "Sinov: yuk ko'tarilganda robot ag'anamaydi",
                "Ish vaqti sekundomer bilan o'lchab yozilgan",
                "Ko'tarish mexanizmi turi (richag/shkiv/vint) to'g'ri aytilgan"],
      savol: "Robotingiz odamga qancha vaqt tejaydi?" }
  ],

  "3-sinf": [
    { nom: "Motorli yordamchi",
      vazifa: "motor kuchidan foydalanadigan foydali qurilma loyihalash",
      talab: ["Qurilma motor bilan ishlasin", "Bajaradigan ishi aniq bo'lsin",
              "Uzatma tanlovi tushuntirilsin"],
      etibor: ["Qurilmaning ishi kuch talab qilsa uzatmani kuchga, tezlik talab qilsa tezlikka sozlang",
               "Motor o'qiga to'g'ridan-to'g'ri og'ir yuk ulamang — uzatma orqali ulang",
               "O'chirib-yoqish qulay joyda bo'lsin"],
      tekshir: ["Qurilma motor bilan ishlaydi va aniq bir ishni bajaradi",
                "Bajariladigan ish bir gapda yozilgan",
                "Motor va ish qismi orasida uzatma bor",
                "Uzatma tanlovi (kuchga yoki tezlikka) to'g'ri asoslangan",
                "Sinov: qurilma o'z ishini 3 marta ketma-ket muvaffaqiyatli bajaradi",
                "Motor zo'riqmaydi: ishlaganda to'xtab-to'xtab qolmaydi"],
      savol: "Motorni to'g'ridan-to'g'ri ulaganingizda va uzatma orqali ulaganingizda farq bormi?" },
    { nom: "Har yerda yuradigan mashina",
      vazifa: "uch xil sirtda ham yura oladigan transport loyihalash",
      talab: ["Uch sirtda sinalsin va natija jadvalga yozilsin",
              "Eng yomon natija bergan sirt uchun yaxshilanish kiritilsin"],
      etibor: ["Sirtlar har xil bo'lsin: silliq pol, gilam, qiyalik yoki qum",
               "Katta va protektorli g'ildirak notekis sirtda yaxshi ishlaydi",
               "Har sinovda bir xil masofa va bir xil start ishlatilsin"],
      tekshir: ["Transport 3 xil sirtda sinalgan",
                "Har sirtdagi natija (masofa yoki vaqt) jadvalga yozilgan",
                "Eng yomon natija bergan sirt aniqlangan",
                "O'sha sirt uchun kamida 1 ta yaxshilanish kiritilgan",
                "Sinov: yaxshilanishdan keyin natija qayta o'lchab, taqqoslangan",
                "Bola qaysi sirtda nima xalaqit berganini (ishqalanish/tishlashish) tushuntiradi"],
      savol: "Qaysi sirt eng qiyin bo'ldi va uni qanday yengdingiz?" },
    { nom: "Maxsus transport",
      vazifa: "aniq bir vazifa uchun mo'ljallangan transport loyihalash (tez yordam, yuk tashish, qutqaruv)",
      talab: ["Vazifa aniq yozilsin", "Transportda o'sha vazifaga xos kamida 1 ta qism bo'lsin",
              "2 metrlik trassada sinalsin"],
      etibor: ["Vazifadan kelib chiqib tanlang: tezlik kerakmi, kuchmi, barqarorlikmi",
               "Maxsus qism shunchaki bezak emas, ishlaydigan bo'lsin",
               "Og'irlik taqsimotini tekshiring — maxsus qism muvozanatni buzmasin"],
      tekshir: ["Transport vazifasi bir gapda yozilgan",
                "Vazifaga xos kamida 1 ta ISHLAYDIGAN maxsus qism bor",
                "Sinov: transport 2 metrlik trassani to'xtamasdan bosib o'tadi",
                "Sinov: maxsus qism ish holatida ko'rsatildi",
                "Trassa vaqti o'lchab yozilgan",
                "Bola transportining oddiy mashinadan farqini asoslab beradi"],
      savol: "Transportingizni oddiy mashinadan nima ajratib turadi?" },
    { nom: "Havo mashinasi",
      vazifa: "havo oqimi yoki reaktiv kuch bilan harakatlanadigan model loyihalash",
      talab: ["Model havo kuchi bilan siljisin", "Masofa o'lchab yozilsin",
              "Havo qarshiligini kamaytirish uchun kamida 1 ta o'zgartirish kiritilsin"],
      etibor: ["Model yengil bo'lsin — havo kuchi katta emas",
               "Parrak yo'nalishini tekshiring: havo ORQAGA itarilishi kerak",
               "G'ildiraklar erkin aylansin, ishqalanish yutib qo'ymasin"],
      tekshir: ["Model faqat havo kuchi bilan siljiydi (itarilmaydi)",
                "Boshlang'ich masofa o'lchab yozilgan",
                "Havo qarshiligini kamaytiruvchi kamida 1 ta o'zgartirish kiritilgan",
                "O'zgartirishdan keyingi masofa o'lchab, taqqoslangan",
                "Sinov: model kamida 1 metr masofani bosib o'tadi",
                "Bola qaysi kuch modelni siljitayotganini to'g'ri tushuntiradi"],
      savol: "Shaklni o'zgartirganingiz masofaga qanday ta'sir qildi?" }
  ],

  "4-sinf": [
    { nom: "Mening bionik ixtirom",
      vazifa: "tabiatdagi biror moslashuvni texnikaga ko'chirib, o'z ixtirongizni qurish",
      talab: ["Qaysi jonzotdan nima olingani yozilsin",
              "Model harakatlansin", "Tabiiy yechim nega samarali ekani tushuntirilsin"],
      etibor: ["Jonzotning BITTA aniq moslashuvini tanlang — hammasini emas",
               "Avval moslashuv qanday ishlashini tushunib oling, keyin qurishni boshlang",
               "Model tashqi ko'rinishni emas, ISHLASH PRINSIPINI takrorlasin"],
      tekshir: ["Qaysi jonzot va qaysi moslashuv — daftarga yozilgan",
                "Model o'sha moslashuv PRINSIPINI takrorlaydi (shunchaki o'xshamaydi)",
                "Model harakatlanadi yoki ishlaydi",
                "Sinov: asosiy funksiya 3 marta ketma-ket ko'rsatildi",
                "Tabiiy yechimning samarasi (nega tabiat shunday qilgan) tushuntirilgan",
                "Bola tabiiy va texnik yechim farqini aytib beradi"],
      savol: "Tabiatdagi yechim texnikada ham shunday yaxshi ishladimi?" },
    { nom: "Yuradigan mexanizm",
      vazifa: "g'ildiraksiz, oyoq bilan yuradigan model loyihalash",
      talab: ["G'ildirak ishlatilmasin", "Model kamida 1 metr yursin",
              "Qadam tsikli tushuntirilsin"],
      etibor: ["Har qadamda kamida uchta tayanch nuqta yerda qolsin — model yiqilmaydi",
               "Oyoqlar juft bo'lib, navbat bilan harakatlansin",
               "Og'irlik markazini past tuting"],
      tekshir: ["Modelda yurish uchun g'ildirak ishlatilmagan",
                "Model oyoqlar harakati bilan oldinga siljiydi",
                "Sinov: model to'xtamasdan kamida 1 metr yuradi",
                "Sinov: yurish davomida model yiqilmaydi",
                "Qadam tsikli (oyoqlar qaysi tartibda harakatlanishi) tushuntirilgan",
                "Yurish tezligi o'lchab yozilgan (1 metrga necha soniya)"],
      savol: "Oyoq bilan yurish g'ildirakdan nimasi bilan yaxshi, nimasi bilan yomon?" },
    { nom: "Tadqiqot roboti",
      vazifa: "notekis yuzada harakatlanib, ma'lumot yoki namuna yig'adigan robot loyihalash",
      talab: ["Robot to'siqlardan o'tsin", "Namunani ola bilsin",
              "Missiya bosqichlari oldindan yozilsin"],
      etibor: ["Missiyani bosqichlarga bo'ling va har bosqichni alohida sinang",
               "Notekis yuzada katta g'ildirak va yaxshi tishlashish kerak",
               "Namuna olish qismi harakat qismiga xalaqit bermasin"],
      tekshir: ["Missiya bosqichlari OLDINDAN daftarga yozilgan",
                "Sinov: robot notekis yuzadan (to'siqli trassadan) o'ta oladi",
                "Sinov: robot namunani (belgilangan buyumni) oladi",
                "Namuna qaytishda tushib qolmaydi",
                "Butun missiya boshdan-oxir 1 marta to'liq bajarildi",
                "Bola eng zaif bosqichni va uni qanday kuchaytirganini aytadi"],
      savol: "Missiyangizda eng zaif bosqich qaysi edi?" },
    { nom: "Bitiruv loyihasi",
      vazifa: "o'zingiz tanlagan muammoni to'liq muhandislik tsikli bo'yicha hal qilish",
      talab: ["Talab yozilsin (robot nima qilishi kerak)", "Eskiz chizilsin",
              "Model qurilsin va sinalsin", "Sinov natijasiga ko'ra kamida 1 ta takomil kiritilsin",
              "Natija sinfga taqdim etilsin"],
      etibor: ["Muammoni kichik va aniq tanlang — katta muammoning bir qismi ham loyiha",
               "Sinov natijalarini raqam bilan yozing, \"yaxshi ishladi\" yetarli emas",
               "Takomil = sinovda topilgan kamchilikka javob"],
      tekshir: ["Talab (robot nima qilishi kerakligi) oldindan yozilgan",
                "Model talabga mos qurilgan",
                "Sinov o'tkazilib, natijasi raqam bilan yozilgan",
                "Sinov asosida kamida 1 ta takomil kiritilgan",
                "Takomildan keyin natija qayta o'lchangan va farq ko'rsatilgan",
                "To'liq tsikl (talab-eskiz-qurish-sinov-takomil) bosqichlari aytib berildi"],
      savol: "Birinchi variantingiz bilan oxirgi variantingiz orasida nima farq bor?" }
  ]
};

/* =====================================================================
 * 2-YIL — doimiy, qiyinroq variant (0-2-sinf Makerzoid)
 * Talablar qattiqroq: deyarli har bandda o'lchov va taqqoslash bor.
 * ===================================================================== */
const LOYIHA_2 = {
  "0-sinf": [
    { nom: "Aniq otuvchi mexanizm",
      vazifa: "elastik energiya bilan ishlaydigan, nishonga aniq tushadigan mexanizm loyihalash",
      talab: ["Mexanizm bir xil kuch bilan otsin (qo'l kuchi emas)",
              "3 marta otilib, uchala natija yozilsin", "Natijalar tarqoqligi 20 sm dan kam bo'lsin"],
      etibor: ["Aniqlik uchun har otishda rezina BIR XIL masofaga tortilsin — chegara (upor) qo'ying",
               "Mexanizm har otishdan keyin joyidan siljimasin",
               "Snaryad yengil va bir xil bo'lsin"],
      tekshir: ["Otish kuchini mexanizm beradi, qo'l emas (tortish chegarasi bor)",
                "Mexanizm otishdan keyin joyidan siljimaydi",
                "Sinov: 3 marta otilib, har natija (tushgan joy) belgilangan",
                "Uchala natija orasidagi eng katta farq o'lchab yozilgan",
                "Tarqoqlik 20 sm dan kam chiqqan (yoki bola sababini tahlil qilgan)",
                "Bola aniqlikka nima ta'sir qilishini (tortish, og'irlik, turtki) aytadi"],
      savol: "Natijalar nega har safar bir xil chiqmadi?" },
    { nom: "Ikki bosqichli uzatma",
      vazifa: "kirish aylanishini kamida 4 barobar tezlashtiradigan yoki sekinlashtiradigan uzatma qurish",
      talab: ["Kamida 2 bosqich bo'lsin", "Nisbat hisoblab yozilsin",
              "Konstruksiya yuk ostida egilmasin"],
      etibor: ["Umumiy nisbat = bosqichlar nisbatlarining ko'paytmasi",
               "Har bosqichni alohida tekshiring, keyin ulang",
               "O'qlarni ikki nuqtadan mahkamlang — bitta nuqta yetmaydi"],
      tekshir: ["Uzatmada kamida 2 ta bosqich bor",
                "Har bosqich nisbati (tishlar soni bo'yicha) yozilgan",
                "Umumiy nisbat hisoblab yozilgan va kamida 4:1 (yoki 1:4) chiqqan",
                "Sinov: kirish 4 marta aylantirilganda chiqish kutilganidek aylanadi",
                "Konstruksiya ishlaganda egilmaydi va g'ildiraklar chiqib ketmaydi",
                "Bola nisbat oshganda nima yo'qotilishini (kuch yoki tezlik) aytadi"],
      savol: "Nisbatni oshirganingizda nimani yo'qotdingiz?" },
    { nom: "Blokli yuk ko'targich",
      vazifa: "shkiv bloklari yordamida yukni yengil ko'taradigan qurilma loyihalash",
      talab: ["Kamida 2 shkiv ishlatilsin", "Bitta shkiv bilan va ikkita shkiv bilan tortish taqqoslansin",
              "Farq daftarga yozilsin"],
      etibor: ["Harakatlanuvchi shkiv kuchni kamaytiradi, qo'zg'almas shkiv yo'nalishni o'zgartiradi",
               "Ip shkivdan chiqib ketmasligi uchun yo'naltiruvchi qo'ying",
               "Taqqoslashda bir xil yuk ishlatilsin"],
      tekshir: ["Qurilmada kamida 2 ta shkiv ishlaydi",
                "Yuk bitta shkiv bilan ko'tarilib, sezgi (og'ir/yengil) yozilgan",
                "Xuddi shu yuk ikki shkiv bilan ko'tarilib, taqqoslangan",
                "Farq daftarga yozilgan",
                "Sinov: yuk 20 sm balandlikka silliq, tushib ketmasdan ko'tariladi",
                "Ip shkivlardan chiqib ketmaydi"],
      savol: "Shkiv qo'shganingizda tortish yengillashdi, lekin nima uzaydi?" },
    { nom: "Ritmli mexanizm",
      vazifa: "belgilangan ritmda (masalan 1 soniyada 1 marta) tebranadigan mexanizm loyihalash",
      talab: ["Ritm sekundomer bilan tekshirilsin", "Mexanizm 30 soniya uzluksiz ishlasin",
              "Ritmni o'zgartirish usuli ko'rsatilsin"],
      etibor: ["Ritmni uzatma nisbati bilan sozlash mumkin",
               "10 soniyada nechta tebranish — shundan ritmni hisoblang",
               "Uzluksiz ishlash uchun bo'g'inlarni ortiqcha qismasin ham, bo'sh ham qoldirmasin"],
      tekshir: ["Mexanizm belgilangan ritmga sozlangan",
                "Ritm sekundomer bilan o'lchangan (10 soniyadagi tebranishlar soni yozilgan)",
                "Sinov: mexanizm 30 soniya to'xtamasdan ishlaydi",
                "Ritmni o'zgartirish usuli amalda ko'rsatildi",
                "O'zgartirilgan ritm ham o'lchab yozilgan",
                "Bola ritm nimaga bog'liqligini to'g'ri aytadi"],
      savol: "Ritmni nima belgilaydi — uzatmami, krivoship radiusimi?" }
  ],

  "1-sinf": [
    { nom: "Ritm mashinasi",
      vazifa: "ikki xil ritmda ishlaydigan, foydalanuvchi ritmni almashtira oladigan mexanizm loyihalash",
      talab: ["Ikki ritm aniq farq qilsin", "Almashtirish 5 soniyada bajarilsin",
              "Har ritm o'lchab yozilsin"],
      etibor: ["Ritm farqini uzatma nisbati bilan bering — radius amplitudani o'zgartiradi, ritmni emas",
               "Almashtirish mexanizmini oddiy qiling: bitta g'ildirakni surish yetarli",
               "Har ritmni alohida sozlab oling"],
      tekshir: ["Mexanizm ikki xil ritmda ishlay oladi",
                "1-ritm o'lchab yozilgan (10 soniyadagi tebranishlar)",
                "2-ritm o'lchab yozilgan va 1-ritmdan aniq farq qiladi",
                "Sinov: ritmni almashtirish 5 soniyadan kam vaqt oldi",
                "Har ikki ritmda mexanizm 20 soniya barqaror ishlaydi",
                "Bola ritm va amplituda farqini to'g'ri tushuntiradi"],
      savol: "Ritmni almashtirganda amplituda ham o'zgardimi?" },
    { nom: "Sensorli yordamchi",
      vazifa: "aniq bir vazifani sensor yordamida avtomatik bajaradigan qurilma loyihalash",
      talab: ["Vazifa bir gapda yozilsin", "10 sinovdan kamida 8 tasi to'g'ri chiqsin",
              "Sensor xato qilgan holat tahlil qilinsin"],
      etibor: ["Chegara qiymatini turli sharoitda (yorug'/qorong'i, yaqin/uzoq) sinab toping",
               "Sinov jadvalini oldindan chizib qo'ying: № / natija / izoh",
               "Xato chiqqanda sharoitda nima boshqacha bo'lganini yozing"],
      tekshir: ["Vazifa bir gapda yozilgan",
                "Qurilma vazifani sensor orqali AVTOMATIK bajaradi",
                "Sinov: 10 sinov o'tkazilib, jadvalga yozilgan",
                "Kamida 8 sinov muvaffaqiyatli chiqqan",
                "Xato holat(lar) sababi tahlil qilinib yozilgan",
                "Bola sensor qaysi sharoitda ishonchsizligini aytadi"],
      savol: "Sensor qaysi sharoitda ishonchsiz bo'lib qoladi?" },
    { nom: "Kran loyihasi",
      vazifa: "yukni ko'tarib, aylantirib, boshqa joyga qo'yadigan kran loyihalash",
      talab: ["Kran kamida 15 sm balandlikka ko'tarsin", "Strela aylansin yoki uzaysin",
              "Kontr-vazn hisobga olinsin", "Yuk 3 marta ketma-ket tashilsin"],
      etibor: ["Avval strela va kontr-vaznni muvozanatlang, keyin ko'tarish mexanizmini qo'shing",
               "Yuk ilgagi yukni o'zi qo'yib yubormasin",
               "Aylanish tekis bo'lsin — keskin burilishda yuk tebranadi"],
      tekshir: ["Kran yukni kamida 15 sm balandlikka ko'taradi (o'lchab ko'rsatildi)",
                "Strela aylanadi yoki uzayadi",
                "Kontr-vazn bor va bola uning vazifasini tushuntiradi",
                "Sinov: yuk 3 marta ketma-ket ko'tarilib, boshqa joyga qo'yildi",
                "Sinov davomida kran ag'anamadi va yuk tushib ketmadi",
                "Bola kran qancha yukda ag'darila boshlashini sinab aytadi"],
      savol: "Kraningiz qanday og'irlikda ag'darila boshlaydi?" },
    { nom: "Maxsus yurar transport",
      vazifa: "aniq bir sharoit uchun mo'ljallangan motorli transport loyihalash (qiyalik, notekis sirt, og'ir yuk)",
      talab: ["Sharoit oldindan tanlansin va yozilsin", "Transport o'sha sharoitda sinalsin",
              "Oddiy transport bilan taqqoslansin"],
      etibor: ["Sharoitga mos yechim tanlang: qiyalikka kuchli uzatma, notekislikka katta g'ildirak",
               "Taqqoslash uchun oddiy (maxsus qismsiz) variant ham sinalsin",
               "Natijani raqam bilan yozing: masofa, vaqt yoki ko'tarilgan yuk"],
      tekshir: ["Sharoit oldindan tanlanib, daftarga yozilgan",
                "Transportda sharoitga mos kamida 1 ta maxsus yechim bor",
                "Sinov: transport tanlangan sharoitda vazifani bajaradi",
                "Oddiy variant ham xuddi shu sharoitda sinalgan",
                "Ikkala natija raqam bilan yozilib, taqqoslangan",
                "Maxsus yechim foydasi raqam bilan isbotlangan"],
      savol: "Maxsus qismingiz haqiqatan yordam berdimi — raqam bilan isbotlang" }
  ],

  "2-sinf": [
    { nom: "Vazifaga mo'ljallangan transport",
      vazifa: "tanlangan vazifa uchun to'liq transport tizimi loyihalash (qutqaruv, yuk tashish, patrul)",
      talab: ["Vazifa va talablar ro'yxati yozilsin", "Transportda kamida 2 ta maxsus qism bo'lsin",
              "3 metrlik trassada sinalsin", "Natija talablarga solishtirilsin"],
      etibor: ["Talablar ro'yxatini qurishdan OLDIN yozing — u sizning check-listingiz bo'ladi",
               "Ikki maxsus qism bir-biriga xalaqit bermasin",
               "Trassada burilish ham bo'lsin — faqat to'g'ri yo'l emas"],
      tekshir: ["Vazifa va kamida 3 bandli talablar ro'yxati oldindan yozilgan",
                "Transportda 2 ta ISHLAYDIGAN maxsus qism bor",
                "Sinov: transport 3 metrlik trassani (burilish bilan) bosib o'tdi",
                "Trassa vaqti o'lchab yozilgan",
                "Har talab bo'yicha bajarildi/bajarilmadi belgilangan",
                "Bajarilmagan talab sababi tahlil qilingan"],
      savol: "Qaysi talab bajarilmay qoldi va nega?" },
    { nom: "Uchar model",
      vazifa: "havo kuchi bilan harakatlanadigan model loyihalash va uning tortish kuchini oshirish",
      talab: ["Boshlang'ich tortish kuchi o'lchansin", "Bitta o'zgartirish kiritilsin",
              "Yangi natija o'lchansin va taqqoslansin"],
      etibor: ["Tortish kuchini masofa yoki tortilgan yuk orqali o'lchang",
               "Bir vaqtda FAQAT BITTA narsani o'zgartiring — aks holda nima ta'sir qilgani noma'lum qoladi",
               "Parrak burchagi va o'lchami — asosiy ta'sir omillari"],
      tekshir: ["Model havo kuchi bilan harakatlanadi",
                "Boshlang'ich natija (masofa/yuk) o'lchab yozilgan",
                "Aniq BITTA o'zgartirish kiritilgan va u yozilgan",
                "Yangi natija o'lchab yozilgan",
                "Farq foizda yoki raqamda hisoblangan",
                "Bola o'zgartirish nega ta'sir qilganini fizika bilan tushuntiradi"],
      savol: "O'zgartirishingiz tortish kuchini necha foizga oshirdi?" },
    { nom: "Bionik robot",
      vazifa: "tabiatdagi harakat usulini takrorlaydigan robot loyihalash",
      talab: ["Qaysi jonzot va qaysi harakat — yozilsin", "Robot o'sha harakatni bajarsin",
              "Tabiiy yechim bilan robot yechimi taqqoslansin", "Kamida 1,5 metr harakatlansin"],
      etibor: ["Harakat mexanikasini avval qog'ozda chizing: qaysi bo'g'in qayerga buriladi",
               "Muvozanatni har qadam bosqichida tekshiring",
               "Tabiiy harakatning qaysi qismini soddalashtirdingiz — buni yozib qo'ying"],
      tekshir: ["Jonzot va harakat turi daftarga yozilgan",
                "Robot o'sha harakat PRINSIPINI bajaradi",
                "Sinov: robot to'xtamasdan kamida 1,5 metr harakatlandi",
                "Harakat davomida robot yiqilmadi",
                "Tabiiy va robot yechimi taqqoslab yozilgan",
                "Bola qaysi soddalashtirish kiritilganini aytadi"],
      savol: "Tabiat bu masalani sizdan qanday farqli hal qilgan?" },
    { nom: "Kosmik missiya (bitiruv)",
      vazifa: "o'zingiz tuzgan kosmik missiyani to'liq muhandislik tsikli bo'yicha hal qilish",
      talab: ["Missiya bosqichlari yozilsin", "Eskiz chizilsin", "Rover qurilsin va sinalsin",
              "Sinov natijasiga ko'ra kamida 2 ta takomil kiritilsin",
              "Natija va o'lchovlar bilan sinfga taqdim etilsin"],
      etibor: ["Missiyada kamida 3 bosqich bo'lsin: yetib borish, vazifa, qaytish",
               "Har sinovni raqam bilan yozing — takomil o'sha raqamga tayanadi",
               "Notekis 'sirt' (kitoblar, to'siqlar) tayyorlab oling"],
      tekshir: ["Missiya bosqichlari (kamida 3 ta) oldindan yozilgan",
                "Rover eskiz asosida qurilgan",
                "Sinov natijalari raqam bilan yozilgan",
                "Kamida 2 ta takomil kiritilgan va har biri sinovga asoslangan",
                "Sinov: to'liq missiya boshdan-oxir 1 marta bajarildi",
                "Taqdimotda o'lchovlar va takomillar ko'rsatildi"],
      savol: "Qaysi takomil eng katta farq berdi — buni qanday o'lchadingiz?" }
  ]
};

/* =====================================================================
 * SPIKE (2-yil 3- va 4-sinf) — dastur bir xil, loyihalar ham umumiy
 * ===================================================================== */
const LOYIHA_SPIKE = [
  { nom: "Mening Driving Base kombinatsiyam",
    vazifa: "o'z Driving Base + 2 ta tanlangan attachment kombinatsiyasini yig'ib, har birining ishlashini ko'rsatish",
    talab: ["Driving Base mustaqil yig'ilsin", "2 ta attachment tanlanib, taqilsin",
            "Har attachment ish holatida ko'rsatilsin"],
    etibor: ["Attachmentlarni vazifasiga qarab juftlang — ular bir-biriga xalaqit bermasin",
             "Kabellarni harakatlanuvchi qismlardan uzoqroq o'tkazing",
             "Yig'ishda instruksiya bosqichlarini o'tkazib yubormang"],
    tekshir: ["Driving Base instruksiya bo'yicha to'g'ri va mahkam yig'ilgan",
              "Robot to'g'ri chiziq bo'ylab og'masdan yuradi",
              "1-attachment taqilgan va ish holatida ko'rsatildi",
              "2-attachment taqilgan va ish holatida ko'rsatildi",
              "Attachment almashtirish 2 daqiqadan kam vaqt oldi",
              "Kabellar to'g'ri portlarga ulangan va harakatga xalaqit bermaydi"],
    savol: "Qaysi attachment juftligi eng foydali kombinatsiya bo'ldi va nega?" },
  { nom: "Aqlli parking robot",
    vazifa: "sensorlar yordamida bo'sh joyni topib, o'zi to'xtaydigan parking robotini qurish va dasturlash",
    talab: ["Robot bo'sh joyni sensor bilan aniqlasin", "To'xtash aniq belgilangan zonada bo'lsin",
            "5 urinishdan kamida 4 tasi muvaffaqiyatli chiqsin"],
    etibor: ["Masofa sensorining chegara qiymatini maydonchada sinab toping",
             "Tezlikni kamaytiring — tez robot to'xtash zonasidan o'tib ketadi",
             "Dasturni bosqichlab sinang: avval yurish, keyin sezish, keyin to'xtash"],
    tekshir: ["Robot bo'sh joyni sensor orqali o'zi aniqlaydi",
              "Robot belgilangan zonada to'xtaydi (chiziqdan chiqmaydi)",
              "Dasturda shart (agar/aks holda) bloki ishlatilgan va bola uni tushuntiradi",
              "Sinov: 5 urinishdan kamida 4 tasi muvaffaqiyatli (jadvalga yozilgan)",
              "Muvaffaqiyatsiz urinish sababi tahlil qilingan",
              "To'xtash aniqligi o'lchab yozilgan (zona chetigacha necha sm qoldi)"],
    savol: "Robot qaysi holatda parkovkani xato qildi va dasturda nimani tuzatdingiz?" },
  { nom: "Missiya-yechim: 1-2-missiya uchun mukammal robot",
    vazifa: "yuk tashish va chiziq bo'ylab yetkazish missiyalari uchun robot+attachment yechimini takomillashtirib, ball sinovidan o'tkazish",
    talab: ["Ikkala missiya ketma-ket bajarilsin", "Har missiya balli hisoblansin",
            "Kamida 1 ta takomil kiritilib, ball farqi ko'rsatilsin"],
    etibor: ["Avval har missiyani alohida barqaror bajarishga erishing, keyin ketma-ket ulang",
             "Ballni yo'qotadigan eng zaif nuqtani toping — takomilni o'sha yerga kiriting",
             "Har urinishdan keyin natijani jadvalga yozing"],
    tekshir: ["1-missiya (yuk tashish) bajarildi va balli yozilgan",
              "2-missiya (chiziq bo'ylab yetkazish) bajarildi va balli yozilgan",
              "Ikkala missiya KETMA-KET, bitta dastur turida bajarildi",
              "Kamida 1 ta takomil kiritilgan (mexanik yoki dasturiy)",
              "Takomildan oldingi va keyingi ball taqqoslab ko'rsatilgan",
              "Urinishlar jadvali yuritilgan (kamida 3 urinish)"],
    savol: "Eng ko'p ballni qaysi o'zgartirish qo'shdi?" },
  { nom: "Bitiruv missiya turi",
    vazifa: "to'liq 4-missiyali turni jamoa bo'lib o'tkazish: strategiya, dastur, taqdimot",
    talab: ["4 missiya uchun strategiya (tartib) yozilsin", "Tur 2,5 daqiqaga sig'sin",
            "Muhandislik daftari to'ldirilsin", "Jamoa taqdimot qilsin"],
    etibor: ["Strategiyada oson va ko'p ball beradigan missiyalarni birinchi qo'ying",
             "Attachment almashtirishlar sonini kamaytiring — har almashtirish vaqt yeydi",
             "Taqdimotda har a'zo o'z hissasini aytsin"],
    tekshir: ["4 missiya tartibi (strategiya) oldindan yozilgan va asoslangan",
              "Sinov: to'liq tur o'tkazildi va 2,5 daqiqaga sig'di",
              "Umumiy ball hisoblanib yozilgan",
              "Muhandislik daftarida sinovlar va xulosalar bor",
              "Jamoaning har a'zosi taqdimotda o'z qismini aytdi",
              "Tur davomida qoidalar buzilmadi (robotga ruxsatsiz tegilmadi)"],
    savol: "Strategiyangizda nimani o'zgartirsangiz, ball yana oshardi?" }
];

/* ================================================================ dars quruvchi */

const SOFT = [
  "Mustaqillik va tashabbus — o'qituvchidan tayyor javob kutmasdan, o'z yechimingizni sinab ko'rish. Ishlamasa — boshqasini sinash.",
  "Rejali ishlash — vaqtni bosqichlarga bo'lib, eskiz va sinovga ham vaqt qoldirish.",
  "Natijaga halol munosabat — o'lchovni bo'rttirmasdan, qanday chiqqan bo'lsa shunday yozish.",
  "O'z ishini himoya qilish — qarorlarini dalil va o'lchov bilan asoslab berish."
];

const UMUMIY_TEKSHIR = [
  "Eskiz qurishdan OLDIN chizilgan va unda asosiy qismlar belgilangan",
  "Konstruksiya mustahkam: model qo'lga olinganda tarqalmaydi",
  "O'quvchi loyihani O'ZI tushuntira oldi: nima qildi va nega shunday qildi",
  "Ish vaqtida yakunlangan va ish o'rni tartibli qoldirilgan"
];

const SHKALA = [
  "9-10 ball = 5 (a'lo)",
  "7-8 ball = 4 (yaxshi)",
  "5-6 ball = 3 (qoniqarli)",
  "3-4 ball = 2 (qoniqarsiz)",
  "0-2 ball = FAILED"
];

function loyihaTop(yil, sinf, chorakNo) {
  if (yil === "2-yil" && (sinf === "3-sinf" || sinf === "4-sinf")) {
    return LOYIHA_SPIKE[chorakNo - 1] || null;
  }
  const jadval = (yil === "2-yil" && LOYIHA_2[sinf]) ? LOYIHA_2 : LOYIHA;
  return (jadval[sinf] || [])[chorakNo - 1] || null;
}

function loyihaDarsi(yil, sinf, chorakNo) {
  const p = loyihaTop(yil, sinf, chorakNo);
  if (!p) return null;

  const oy = (chorakNo - 1) * 2 + 2;                    // yil bo'yicha oy raqami
  const tekshirlar = p.tekshir.concat(UMUMIY_TEKSHIR);   // 6 xos + 4 umumiy = 10 ball

  const sarlavha = oy + "-oylik nazorat (AMALIY LOYIHA-IMTIHON) — \"" + p.nom +
    "\": " + p.vazifa + ". Baholash: 10 bandli check-list, har band 1 ball; " +
    "9-10 = 5; 7-8 = 4; 5-6 = 3; 3-4 = 2; 0-2 = FAILED.";

  return {
    nom: sarlavha,
    kontent: {
      maqsad: [
        "O'quvchilar \"" + p.nom + "\" loyihasi doirasida " + p.vazifa + ".",
        "Har bir o'quvchi ishini oldindan e'lon qilingan 10 bandli check-list " +
          "bo'yicha himoya qiladi va " + oy + "-oy uchun jurnal bahosini oladi.",
        "O'quvchilar o'z qarorlarini o'lchov va dalil bilan asoslash tajribasini oladilar."
      ],
      lugat: [
        "Loyiha-imtihon (Project exam) – natijasi baholanadigan mustaqil amaliy ish",
        "Check-list (Checklist) – har bandi alohida tekshiriladigan baholash ro'yxati",
        "Talab (Requirement) – loyiha albatta bajarishi kerak bo'lgan shart",
        "Eskiz (Sketch) – qurishdan oldin chiziladigan qo'lda chizma",
        "Sinov (Trial) – natijani o'lchab tekshirish"
      ],
      softSkill: SOFT[chorakNo - 1],
      resurslar: [
        "Konstruktor to'plami va chorak davomida o'rganilgan modellar instruksiyalari (g'oya olish uchun)",
        "Har o'quvchi (juftlik) uchun chop etilgan check-list varag'i — 10 band, har bandda belgilash katagi",
        "Eskiz chizish uchun daftar va qalam",
        "O'lchov lentasi va sekundomer (sinov bandlari uchun)"
      ],
      nazariya: [
        {
          title: "5.1. Loyiha mavzusi va talablar (5 daqiqa)",
          points: ["Topshiriq e'lon qilinadi: " + p.vazifa + "."]
            .concat(p.talab.map(function (t) { return "Talab: " + t + "."; }))
        },
        {
          title: "5.2. Nimalarga e'tibor berish kerak",
          points: p.etibor
        },
        {
          title: "5.3. Baholash check-listi (ish boshlanishidan OLDIN e'lon qilinadi)",
          points: tekshirlar.map(function (t, i) {
            return (i + 1) + "-band (1 ball): " + t + ".";
          }).concat(SHKALA).concat([
            "Baho jurnalga " + oy + "-OYLIK NAZORAT bahosi sifatida qo'yiladi — " +
              "o'qituvchining oylik hisobotiga aynan shu baho kiradi."
          ])
        }
      ],
      amaliy: [
        {
          title: "6.1. Eskiz (5 daqiqa)",
          points: [
            "Har bir o'quvchi qurishdan OLDIN g'oyasini daftarga chizadi.",
            "Eskizda qaysi qism nima qilishi belgilanadi — bu check-listning alohida bandi."
          ]
        },
        {
          title: "6.2. Qurish (18 daqiqa)",
          points: [
            "O'quvchilar eskiz bo'yicha loyihani quradilar.",
            "Ishlamagan yechim o'zgartiriladi — eskizga tuzatish kiritish mumkin.",
            "O'qituvchi aralashmaydi, faqat xavfsizlik va vaqtni nazorat qiladi — bu imtihon."
          ]
        },
        {
          title: "6.3. Sinov va o'lchov (7 daqiqa)",
          points: [
            "Check-listdagi sinov bandlari bajariladi, natijalar daftarga yoziladi.",
            "O'lchov talab qilingan bandlarda natija raqam bilan qayd etiladi."
          ]
        },
        {
          title: "6.4. Himoya va baholash (10 daqiqa)",
          points: [
            "Har o'quvchi (juftlik) loyihasini ko'rsatib, check-list bandlari bo'yicha himoya qiladi.",
            "O'qituvchi har bandni varaqda belgilaydi: bajarildi = 1 ball, bajarilmadi = 0.",
            "Asosiy savol: " + p.savol,
            "Ballar yig'indisi shkala bo'yicha bahoga aylantiriladi va e'lon qilinadi."
          ]
        }
      ],
      uyga: [
        "Check-listda ball ololmagan bandingizni yozib, uni qanday bajarish mumkinligini bir gapda tushuntiring.",
        "Loyihangizning rasmini chizib yoki fotosini olib, unga yana qanday yaxshilanish kiritish mumkinligini yozing."
      ]
    }
  };
}

module.exports = { faol: true, LOYIHA, LOYIHA_2, LOYIHA_SPIKE, loyihaTop, loyihaDarsi };
