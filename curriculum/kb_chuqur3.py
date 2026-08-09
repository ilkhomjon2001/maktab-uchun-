# -*- coding: utf-8 -*-
"""
NAZARIYANI CHUQURLASHTIRISH — 3-qism: muhandislik bosqichlari va
chorak kirish darslari.

CHUQUR3    — mavzu bo'yicha qo'shimcha bloklar (kb_chuqur.py bilan bir xil tuzilish).
KIRISH_YO  — chorak kirish darslari uchun YO'NALISH bo'yicha umumiy bloklar.
             Kirish darslari 32 ta va ularning mazmuni yo'nalishga bog'liq,
             shuning uchun har biriga alohida yozish o'rniga yo'nalish
             bo'yicha beriladi.
"""


def D(*bloklar):
    return [(sarlavha, list(bandlar)) for sarlavha, bandlar in bloklar]


CHUQUR3 = {

# ============================================================ ALGORITM
"Algoritmni chizish": D(
 ("Blok-sxemaning shartli belgilari", [
  "Oval — boshlanish va tugash. Har bir sxemada bittadan bo'ladi.",
  "To'g'ri to'rtburchak — amal: 'LEDni yoq', 'sensorni o'qi'.",
  "Romb — shart: undan IKKI strelka chiqadi, biri 'ha', ikkinchisi 'yo'q'.",
  "Parallelogramm — kirish yoki chiqish: 'qiymatni o'qi', 'ekranga chiqar'.",
  "Strelkalar bajarilish tartibini ko'rsatadi va faqat bir yo'nalishda bo'ladi.",
 ]),
 ("Algoritmni to'g'ri tuzish", [
  "Har bir qadam BITTA aniq amal bo'lishi kerak. 'Qurilmani ishlat' — bu qadam emas, bu butun loyiha.",
  "Shart romblarida savol 'ha/yo'q' bilan javob beriladigan qilib yoziladi.",
  "Takrorlanish strelkaning orqaga qaytishi bilan ko'rsatiladi.",
  "Tuzilgan sxema boshqa o'quvchiga berib tekshiriladi: u tushunib bajara olsa — sxema to'g'ri.",
 ]),
 ("Nima uchun avval chizish kerak", [
  "Kodni yozib bo'lgandan keyin mantiqiy xatoni topish qiyin, sxemada esa u darhol ko'rinadi.",
  "Sxema kodga o'girilishi oson: har bir romb — if, har bir orqaga qaytish — sikl.",
  "Sxema loyiha hujjatining bir qismi bo'ladi va himoyada tushuntirishni osonlashtiradi.",
  "Amaliyotda muhandislar ham xuddi shunday ishlaydi: avval sxema, keyin kod.",
 ]),
),

"Qurilmaning ish algoritmini chizish": D(
 ("Qurilma algoritmining uch qismi", [
  "SEZISH — sensordan qiymat o'qish. Bu algoritmning kirishi.",
  "QAROR — o'qilgan qiymatni chegara bilan solishtirish, mantiqiy shart tekshirish.",
  "HARAKAT — LED, motor, zummer yoki ekranga ta'sir qilish. Bu chiqish.",
  "Deyarli har qanday qurilma shu uch bosqichni takrorlab turadi — bu loop() ning mazmuni.",
 ]),
 ("Holatlar (state) bilan ishlash", [
  "Ba'zi qurilmalar bir necha HOLATDA bo'ladi: kutish, ishlash, ogohlantirish.",
  "Har bir holat uchun alohida qoida yoziladi: shu holatda nima qiladi va qaysi shartda boshqa holatga o'tadi.",
  "Holat diagrammasi chiziladi: doiralar — holatlar, strelkalar — o'tish shartlari.",
  "Bu usul murakkab qurilmani (masalan svetofor yoki signalizatsiya) tushunarli qiladi.",
 ]),
),

"Algoritmni blokli dasturga aylantirish": D(
 ("Sxemadan blokka o'tish qoidalari", [
  "Oval (boshlanish) — 'boshlanganda' blogi.",
  "To'rtburchak (amal) — mos amal blogi: 'yoq', 'kut', 'chiqar'.",
  "Romb (shart) — 'agar ... bo'lsa' blogi. Ikki chiqishli romb esa 'agar ... aks holda'.",
  "Orqaga qaytuvchi strelka — 'doim' yoki 'takrorla' blogi.",
  "Ya'ni sxemadagi har bir shakl uchun aniq bitta blok bor — bu tarjima mexanik ish.",
 ]),
 ("Tekshirish tartibi", [
  "Dastur yig'ilgach, uni sxema bilan yonma-yon qo'yib solishtirish kerak.",
  "Har bir sxema qadami dasturda o'z blogini topganini belgilab chiqiladi.",
  "Qolib ketgan qadam bo'lsa — dastur to'liq emas.",
  "Dasturda sxemada yo'q blok bo'lsa — u yerdan ortiqcha ish bajarilyapti va uni tekshirish kerak.",
 ]),
),

# ============================================================ LOYIHA BOSQICHLARI
"Loyihani rejalashtirish": D(
 ("Rejaning tarkibi", [
  "Muammo bayoni: qanday muammo hal qilinadi va u kimga kerak.",
  "Talablar ro'yxati: qurilma nima qila olishi kerak. Har bir talab TEKSHIRILADIGAN qilib yoziladi.",
  "Komponentlar ro'yxati: nima kerak va nechta.",
  "Bosqichlar va vaqt: har bir bosqichga necha dars ajratiladi.",
  "Xavflar: nima noto'g'ri ketishi mumkin va u holda nima qilinadi.",
 ]),
 ("Yaxshi va yomon talab", [
  "Yomon talab: 'qurilma yaxshi ishlasin'. Buni tekshirib bo'lmaydi.",
  "Yaxshi talab: 'harorat 30 darajadan oshganda 2 sekund ichida signal bersin'.",
  "Yaxshi talabda son bor va uni o'lchash mumkin.",
  "Talablar loyiha oxirida bandma-band tekshiriladi — shuning uchun ular aniq bo'lishi shart.",
 ]),
 ("Vaqtni taqsimlash", [
  "Amaliyotda yig'ish va dasturlash rejalashtirilganidan ikki barobar ko'p vaqt oladi.",
  "Shuning uchun rejaga zaxira vaqt qo'yish kerak: har uch darsga bitta zaxira dars.",
  "Eng katta xavfli qismni BIRINCHI qilish kerak: u ishlamasa, rejani o'zgartirishga vaqt qoladi.",
  "Oxirgi dars taqdimot uchun qoldiriladi va unga yangi funksiya qo'shilmaydi.",
 ]),
),

"Loyihani rejalashtirish va bosqichlarga bo'lish": D(
 ("Katta vazifani bo'lish", [
  "Butun loyihani birdan yig'ishga urinish — eng ko'p uchraydigan xato.",
  "To'g'ri usul: qurilmani mustaqil ishlaydigan bo'laklarga bo'lish.",
  "Masalan meteostansiya: 1) sensorni o'qish, 2) ekranga chiqarish, 3) tarmoqqa yuborish, 4) korpusga joylash.",
  "Har bir bo'lak ALOHIDA yig'iladi va sinaladi. Faqat ishlagach keyingisiga o'tiladi.",
 ]),
 ("Bosqichlarni birlashtirish", [
  "Ikki ishlaydigan bo'lak birlashtirilganda ishlamay qolishi mumkin — bu normal holat.",
  "Sabablari odatda: pin to'qnashuvi, quvvat yetishmasligi, kutubxonalar bir-biriga xalaqit berishi.",
  "Shuning uchun birlashtirish alohida bosqich sifatida rejalashtiriladi va unga vaqt ajratiladi.",
  "Har birlashtirishdan keyin oldingi funksiyalar hali ham ishlayotgani tekshiriladi.",
 ]),
),

"Prototipni yig'ish": D(
 ("Prototip nima va nima uchun kerak", [
  "Prototip — g'oyani sinab ko'rish uchun yig'ilgan dastlabki namuna. U chiroyli bo'lishi shart emas.",
  "Maqsad — g'oya UMUMAN ishlashini tekshirish, tayyor mahsulot yasash emas.",
  "Shuning uchun breadboard ishlatiladi: kavsharlash kerak emas, o'zgartirish oson.",
  "Prototipda topilgan har bir muammo — keyingi bosqichda tejalgan vaqt.",
 ]),
 ("Yig'ish tartibi", [
  "1) Quvvat liniyalarini birinchi ulash: breadboardning ikki chetiga 5V va GND.",
  "2) Bitta komponentni ulab, uni ALOHIDA sinash.",
  "3) Ishlagach keyingisini qo'shish va yana sinash.",
  "4) Har qo'shimchadan keyin oldingilari ishlayotganini tekshirish.",
  "Hammasini birdan ulab, keyin sinash — xato qayerdaligini topishni juda qiyinlashtiradi.",
 ]),
 ("Simlarni tartibga solish", [
  "Rang bilan belgilash: qizil — quvvat, qora yoki ko'k — GND, qolgan ranglar — signal.",
  "Simlar qisqa va yassi bo'lsin: uzun va osilgan sim uzilib ketadi va xatoni ko'rsatmaydi.",
  "Bir xil ranglar chalkashmasligi uchun sxema daftarga chiziladi va simlar shunga qarab ulanadi.",
  "Tartibli sxemada xatoni topish bir necha barobar tez bo'ladi.",
 ]),
),

"Prototipni yig'ish va sinash": D(
 ("Sinov rejasi tuzish", [
  "Sinov rejasi talablar ro'yxatidan kelib chiqadi: har bir talab uchun bitta sinov.",
  "Sinovda uch narsa yoziladi: nima qilinadi, nima kutiladi, nima chiqdi.",
  "Chegaraviy holatlarni ham sinash kerak: eng past va eng baland qiymat, sensor uzilgan holat.",
  "Sinov natijalari jadvalga yoziladi — bu loyiha hujjatining asosiy qismi bo'ladi.",
 ]),
 ("Nosozlikni topish tartibi", [
  "Avval QUVVAT: manba ulanganmi, kuchlanish yetarlimi, GND umumiymi.",
  "Keyin ULANISH: har bir sim to'g'ri pinda turibdimi, kontakt yaxshimi.",
  "Keyin KOMPONENT: uni alohida sinab ko'rish, ishlayotgan boshqasi bilan almashtirish.",
  "Oxirida KOD: Serial monitorga log qo'yib, dastur qayerga yetayotganini kuzatish.",
  "Bu tartibni buzmaslik kerak: ko'pchilik koddan boshlaydi va aslida sim tushib qolgan bo'lib chiqadi.",
 ]),
),

"Prototipni yig'ish (1-bosqich)": D(
 ("Birinchi bosqichning maqsadi", [
  "1-bosqichda butun qurilma emas, uning ENG MUHIM qismi yig'iladi.",
  "Eng muhim qism — loyihaning butun g'oyasi bog'liq bo'lgan qism.",
  "Masalan AI loyihasida bu — sensor ma'lumotini to'g'ri yig'a olish.",
  "Agar shu qism ishlamasa, qolgan hamma ish ma'nosiz — shuning uchun u birinchi qilinadi.",
 ]),
 ("Bosqich yakunida tekshiriladigan narsalar", [
  "Asosiy qism o'z vazifasini bajaryaptimi.",
  "O'lchangan qiymatlar mantiqiy oraliqdami.",
  "Qurilma barqaror ishlaydimi yoki bir necha daqiqadan keyin to'xtab qoladimi.",
  "Natija ish daftariga yoziladi va keyingi bosqich rejasi shunga qarab aniqlashtiriladi.",
 ]),
),

"Dasturni yozish (1-bosqich)": D(
 ("Dasturni bosqichma-bosqich yozish", [
  "Butun dasturni birdan yozib, keyin yuklash — xatoni topishni juda qiyinlashtiradi.",
  "To'g'ri usul: eng kichik ishlaydigan qismni yozib yuklash, keyin ustiga qo'shib borish.",
  "Masalan: 1) sensorni o'qib Serial ga chiqarish, 2) chegara qo'shish, 3) LEDni boshqarish, 4) ekran qo'shish.",
  "Har qadamdan keyin yuklab sinash — shunda xato faqat oxirgi qo'shilgan qismda bo'ladi.",
 ]),
 ("Boshlang'ich tuzilma", [
  "Avval pin doimiylari e'lon qilinadi va ularga ma'noli nom beriladi.",
  "setup() da pinMode va Serial.begin yoziladi.",
  "loop() da esa uch qism bo'ladi: o'qish, qaror, bajarish.",
  "Har bir qismga izoh yoziladi — bu keyin qaytib kelganda vaqtni tejaydi.",
 ]),
),

"Yakuniy sinov va tuzatish": D(
 ("Yakuniy sinovning farqi", [
  "Oraliq sinovda alohida qismlar tekshiriladi, yakuniy sinovda esa BUTUN tizim birga.",
  "Sinov haqiqiy ish sharoitida o'tkaziladi: qurilma qayerda ishlasa, o'sha yerda.",
  "Uzoq muddat sinov shart: 10-30 daqiqa uzluksiz ishlatib, to'xtab qolmasligini tekshirish.",
  "Ko'p xatolar faqat uzoq ishlaganda chiqadi: xotira tugashi, sensor qizishi, aloqa uzilishi.",
 ]),
 ("Tuzatishlarni boshqarish", [
  "Har bir tuzatishdan keyin BUTUN sinov qaytariladi: tuzatish boshqa joyni buzgan bo'lishi mumkin.",
  "Ishlaydigan variant har safar nusxalab saqlanadi — qaytish nuqtasi bo'ladi.",
  "Taqdimotga bir dars qolganda yangi funksiya QO'SHILMAYDI, faqat mavjudi barqarorlashtiriladi.",
  "Tuzatilmagan kamchiliklar ro'yxati tuziladi va himoyada ochiq aytiladi — bu kuchsizlik emas, halollik.",
 ]),
),

"Qurilmani bosqichma-bosqich sinash": D(
 ("Sinov bosqichlari", [
  "1) Komponent sinovi: har bir element alohida ishlayaptimi.",
  "2) Modul sinovi: bir necha element birga (masalan sensor + ekran).",
  "3) Tizim sinovi: hammasi birga, haqiqiy ish sharoitida.",
  "4) Chidamlilik sinovi: uzoq vaqt va noqulay sharoitda.",
  "Har bosqich o'tmaguncha keyingisiga o'tilmaydi.",
 ]),
 ("Nimani o'lchash kerak", [
  "Javob vaqti: sensor o'zgargandan qurilma javob berguncha necha sekund o'tadi.",
  "Aniqlik: o'lchov etalon bilan qanchalik mos.",
  "Barqarorlik: 30 daqiqada necha marta noto'g'ri ishladi.",
  "Quvvat sarfi: batareya bilan necha soat ishlaydi.",
  "Bu to'rt son loyiha hujjatida bo'lishi kerak — ular ishning sifatini raqam bilan ko'rsatadi.",
 ]),
),

"Birinchi sinov va o'lchov": D(
 ("Birinchi sinovda nimaga qarash kerak", [
  "Qurilma umuman ishga tushdimi: quvvat bormi, indikator yonyaptimi.",
  "Sensor mantiqiy qiymat qaytaryaptimi yoki 0 va maksimumda qotib turibdimi.",
  "Ijro qurilmasi (LED, motor, zummer) buyruqqa javob beryaptimi.",
  "Serial monitorda kutilgan yozuvlar chiqyaptimi.",
 ]),
 ("Boshlang'ich o'lchovlarni yozib olish", [
  "Sensorning tinch holatdagi qiymati — bu keyin kalibrlash uchun etalon bo'ladi.",
  "Eng past va eng baland qiymat — chegara tanlashda kerak.",
  "Ta'minot kuchlanishi va iste'mol toki — quvvat manbai yetarliligini baholash uchun.",
  "Bu sonlarsiz keyingi bosqichlarda har safar noldan boshlashga to'g'ri keladi.",
 ]),
),

"Yaxshilash va qayta sinash": D(
 ("Nimani yaxshilash kerakligini aniqlash", [
  "Yaxshilash tasodifiy emas, sinov natijalariga asoslangan bo'lishi kerak.",
  "Sinov jadvalidan eng ko'p muammo chiqqan joy topiladi va birinchi o'sha tuzatiladi.",
  "Har bir yaxshilash uchun o'lchanadigan maqsad qo'yiladi: 'javob vaqtini 3 sekunddan 1 sekundga tushirish'.",
  "Maqsadsiz o'zgartirish natijani yomonlashtirib qo'yishi ham mumkin.",
 ]),
 ("Qayta sinash qoidasi", [
  "Har o'zgarishdan keyin FAQAT o'sha joy emas, butun sinov rejasi qaytariladi.",
  "Natijalar oldingi jadval bilan yonma-yon yoziladi — yaxshilanish shunda ko'rinadi.",
  "Yomonlashgan joy bo'lsa, o'zgarish qaytarib olinadi.",
  "Bir vaqtda faqat bitta narsani o'zgartirish kerak, aks holda qaysi biri ta'sir qilganini bilib bo'lmaydi.",
 ]),
),

"Kamchiliklarni aniqlash": D(
 ("Kamchiliklarni tizimli izlash", [
  "Kamchilik uch joydan kelib chiqadi: sxema, kod yoki g'oyaning o'zi.",
  "Sxema kamchiligi: kontakt yomon, quvvat yetmaydi, sensor noto'g'ri joyda.",
  "Kod kamchiligi: chegara noto'g'ri, filtr yo'q, xato holat tekshirilmagan.",
  "G'oya kamchiligi: tanlangan sensor bu vazifa uchun umuman mos emas.",
  "Uchinchi turi eng og'ir va uni erta aniqlash kerak — shuning uchun prototip bosqichi bor.",
 ]),
 ("Kamchiliklarni yozib borish", [
  "Har bir kamchilik yoziladi: nima bo'ldi, qachon bo'ldi, qanday takrorlanadi.",
  "Takrorlanish shartini yozish eng muhimi: takrorlab bo'lmaydigan xatoni tuzatib ham bo'lmaydi.",
  "Kamchiliklar muhimlik bo'yicha tartiblanadi: qurilmani ishlatib bo'lmaydigan holat birinchi.",
  "Tuzatilmagani ham ro'yxatda qoldiriladi va himoyada aytiladi.",
 ]),
),

# ============================================================ HUJJAT VA TAQDIMOT
"Hujjatlashtirish: sxema va kod": D(
 ("Hujjatning tarkibi", [
  "Muammo va yechim bayoni — bir sahifada, sodda tilda.",
  "Printsipial sxema — hamma ulanishlar ko'rsatilgan chizma.",
  "Komponentlar ro'yxati — nom, miqdor, taxminiy narx.",
  "Kod — izohlar bilan, asosiy qismlari tushuntirilgan.",
  "Sinov natijalari jadvali va topilgan kamchiliklar ro'yxati.",
 ]),
 ("Sxemani to'g'ri chizish", [
  "Har bir komponent shartli belgi bilan chiziladi, rasm bilan emas.",
  "Pin raqamlari albatta yoziladi — usiz sxema qayta yig'ish uchun yaroqsiz.",
  "Quvvat liniyalari alohida ajratiladi: yuqorida plyus, pastda GND.",
  "Sxema shunday bo'lishi kerakki, uni ko'rgan boshqa odam qurilmani qaytadan yig'a olsin. Bu — hujjatning asosiy sinovi.",
 ]),
),

"Sxema va kodni hujjatlashtirish": D(
 ("Kodni hujjatlashtirish", [
  "Fayl boshida izoh bloki: loyiha nomi, muallif, sana, qurilma nima qiladi.",
  "Pin ro'yxati doimiylar sifatida boshida beriladi va har biriga izoh yoziladi.",
  "Har bir funksiya oldida bir qatorlik izoh: u nima qiladi.",
  "Murakkab formula yoki koeffitsient oldida u qayerdan olingani yoziladi.",
  "Kalibrlash qiymatlari alohida belgilanadi — ular boshqa nusxada o'zgartirilishi kerak bo'ladi.",
 ]),
 ("Izoh yozishning qoidasi", [
  "Izoh kod NIMA qilishini emas, NIMA UCHUN qilinganini tushuntirishi kerak.",
  "Yomon izoh: 'i ni bittaga oshiradi' — buni koddan ham ko'rish mumkin.",
  "Yaxshi izoh: 'sensor sekundiga bir marta o'qiladi, tezroq so'ralsa nan qaytaradi'.",
  "Ma'noli o'zgaruvchi nomi ko'p izohni keraksiz qiladi — bu eng yaxshi hujjatlashtirish usuli.",
 ]),
),

"Kodni izoh bilan yozish": D(
 ("Izohning turlari", [
  "Fayl sarlavhasi: loyiha haqida umumiy ma'lumot.",
  "Bo'lim izohi: kodning katta qismlarini ajratadi (sozlash, o'lchash, qaror).",
  "Qator izohi: aniq bir qatorning noaniq joyini tushuntiradi.",
  "Ogohlantirish izohi: 'bu qatorni o'zgartirmang' yoki 'bir marta yuklab, keyin izohga oling'.",
 ]),
 ("Qancha izoh yozish kerak", [
  "Har qatorga izoh yozish ham xato: kod izohlar orasida ko'rinmay qoladi.",
  "Izoh kerak bo'ladigan joylar: sehrli sonlar, formulalar, kutilmagan yechimlar, apparat cheklovlari.",
  "Agar kodni tushuntirish uchun uzun izoh kerak bo'lsa — ko'pincha kodning o'zini soddalashtirish to'g'riroq.",
  "Bir haftadan keyin o'z kodingizni o'qib ko'rish — izohlar yetarli ekanini tekshirishning eng yaxshi usuli.",
 ]),
),

"Texnik hujjat tayyorlash": D(
 ("Texnik topshiriq (TZ)", [
  "TZ — loyiha boshlanishida yoziladigan hujjat: qurilma NIMA qilishi kerak.",
  "Unda funksional talablar bo'ladi: qurilma qanday vazifalarni bajaradi.",
  "Va texnik cheklovlar: quvvat manbai, o'lchamlar, narx, ishlash muddati.",
  "TZ loyiha oxirida tekshirish ro'yxati bo'lib xizmat qiladi: har bir band bajarildimi.",
 ]),
 ("Yakuniy texnik hujjat", [
  "Tuzilish sxemasi: qurilma qanday bloklardan iborat va ular qanday bog'langan.",
  "Printsipial sxema: aniq ulanishlar va pin raqamlari.",
  "Kod va uning tuzilishi tavsifi.",
  "Sinov protokoli: nima sinaldi, qanday natija chiqdi.",
  "Foydalanish qo'llanmasi: qurilmani qanday yoqish, sozlash va ishlatish.",
  "Bu to'plam bilan boshqa jamoa loyihani davom ettira olishi kerak — hujjatning asosiy mezoni shu.",
 ]),
),

"Qurilma uchun qo'llanma yozish": D(
 ("Qo'llanmaning tarkibi", [
  "Qurilma nima qiladi — bir-ikki gapda, texnik atamalarsiz.",
  "Nima kerak: quvvat manbai, kabel, qo'shimcha jihoz.",
  "Ishga tushirish: qadamma-qadam, rasm bilan.",
  "Boshqarish: qaysi tugma nima qiladi, indikatorlar nimani bildiradi.",
  "Muammolar va yechimlar: eng ko'p uchraydigan 3-5 holat.",
 ]),
 ("Qo'llanma kim uchun yoziladi", [
  "Qo'llanma qurilmani BIRINCHI MARTA ko'rayotgan odam uchun yoziladi.",
  "Shuning uchun 'ma'lumki', 'oddiy' kabi so'zlar ishlatilmaydi.",
  "Har bir qadam bajarilganini tekshirish belgisi bo'lishi kerak: 'yashil chiroq yonadi'.",
  "Sinov: qo'llanmani boshqa sinf o'quvchisiga berib, u qurilmani ishlata olishini tekshirish.",
 ]),
),

"Foydalanuvchi qo'llanmasi yozish": D(
 ("Tilni soddalashtirish", [
  "Texnik atama ishlatilsa, u birinchi marta izohlanadi.",
  "Uzun gap o'rniga qisqa gaplar: bir gapda bir fikr.",
  "Buyruq shaklida yozish: 'USB kabelni ulang' — 'USB kabel ulanishi kerak' emas.",
  "Raqamlangan qadamlar matn bo'lagidan ancha oson tushuniladi.",
 ]),
 ("Rasm va sxemalar", [
  "Har bir muhim qadamga rasm qo'yish tushunishni bir necha barobar osonlashtiradi.",
  "Rasmda tugma yoki razyom strelka bilan belgilanadi.",
  "Indikator holatlari jadval qilinadi: yashil doimiy — ishlayapti, qizil miltillayapti — xato.",
  "Xavfsizlik ogohlantirishlari alohida ajratib ko'rsatiladi.",
 ]),
),

"Taqdimot va himoya": D(
 ("Taqdimot tuzilishi (5 daqiqa)", [
  "1) Muammo (30 sekund): qanday muammo hal qilinmoqda va u kimga kerak.",
  "2) Yechim (1 daqiqa): qurilma nima qiladi va qanday ishlaydi.",
  "3) Tuzilish (1 daqiqa): qanday komponentlardan iborat, sxemani ko'rsatish.",
  "4) NAMOYISH (1,5 daqiqa): qurilma jonli ishlatib ko'rsatiladi. Bu eng muhim qism.",
  "5) Natija va cheklovlar (1 daqiqa): nima ishladi, nima ishlamadi, keyin nima qilish kerak.",
 ]),
 ("Namoyishga tayyorgarlik", [
  "Namoyish oldindan kamida uch marta mashq qilinadi.",
  "Zaxira reja bo'lishi kerak: qurilma ishlamay qolsa, avval yozib olingan video ko'rsatiladi.",
  "Quvvat manbai, kabel va zaxira komponentlar oldindan tayyorlab qo'yiladi.",
  "Namoyish paytida qurilmani sozlash yoki tuzatish bilan shug'ullanish mumkin emas — hammasi oldindan tayyor bo'lishi kerak.",
 ]),
 ("Savollarga javob berish", [
  "Bilmagan narsani 'bilmayman, lekin shunday tekshirish mumkin' deb aytish — to'g'ri javob.",
  "Kamchilikni yashirish emas, ochiq aytish kerak: baholovchi uni baribir topadi.",
  "Har bir tanlovni asoslashga tayyor bo'lish: nima uchun aynan shu sensor, nima uchun shu chegara.",
  "Raqam bilan javob berish eng ishonchli: 'sinovda 20 martadan 18 tasi to'g'ri chiqdi'.",
 ]),
),

"Taqdimotga tayyorgarlik": D(
 ("Tayyorgarlik ro'yxati", [
  "Qurilma to'liq ishlaydigan holatda va zaryadlangan.",
  "Zaxira: qo'shimcha batareya, kabel, eng ko'p buziladigan komponentdan bittadan.",
  "Namoyish videosi oldindan yozib olingan.",
  "Slaydlar yoki plakat: sxema, komponentlar ro'yxati, sinov natijalari.",
  "Gapiriladigan matn qisqa tezislar shaklida yozilgan (to'liq matn o'qilmaydi).",
 ]),
 ("Vaqtni boshqarish", [
  "Taqdimot vaqti oldindan aytiladi va unga rioya qilinadi.",
  "Mashq paytida sekundomer bilan o'lchash kerak — birinchi urinishda odatda ikki barobar uzun chiqadi.",
  "Uzun bo'lsa texnik tafsilotlar qisqartiriladi, namoyish esa QISQARTIRILMAYDI.",
  "Jamoada har kimga o'z qismi belgilanadi va o'tish joylari mashq qilinadi.",
 ]),
),

"Boshqalarning loyihasini baholash": D(
 ("Baholash mezonlari", [
  "Ishlaydimi: qurilma e'lon qilingan vazifani bajaradimi.",
  "Talablarga mos keladimi: boshda qo'yilgan bandlarning nechtasi bajarilgan.",
  "Yechim asoslanganmi: komponent va chegaralar tanlovi tushuntirilganmi.",
  "Hujjat to'liqmi: sxema bilan qurilmani qayta yig'ish mumkinmi.",
  "Taqdimot tushunarlimi: begona odam nima qilinganini tushundimi.",
 ]),
 ("Foydali fikr bildirish", [
  "Avval ishlagan narsani aytish kerak — bu adolat va u muallifga nimani saqlash kerakligini bildiradi.",
  "Keyin ANIQ taklif: 'yaxshi emas' emas, 'sensorni 5 sm pastroq qo'ysangiz aniqlik ortadi'.",
  "Shaxsga emas, ishga baho beriladi.",
  "O'z loyihangizga qo'llash mumkin bo'lgan g'oyani yozib olish — baholashning eng katta foydasi.",
 ]),
),

"Komponentlarni tanlash va asoslash": D(
 ("Tanlov mezonlari", [
  "Vazifaga moslik: sensor o'lchaydigan oraliq kerakli oraliqni qamrab oladimi.",
  "Aniqlik: talab qilingan aniqlik yetarlimi (DHT22 uchun 0,5 daraja, DHT11 uchun 2 daraja).",
  "Ta'minot: 3,3 V yoki 5 V, platangizga mos keladimi.",
  "Interfeys: analog, raqamli, I2C yoki SPI — bo'sh pinlaringiz yetadimi.",
  "Narx va mavjudlik: bozorda bormi, qancha turadi.",
 ]),
 ("Tanlovni asoslash", [
  "Har bir komponent uchun kamida ikki variant solishtiriladi.",
  "Solishtirish jadval shaklida: parametr, 1-variant, 2-variant, tanlov sababi.",
  "Misol: DHT11 arzon lekin aniqligi 2 daraja; DHT22 qimmatroq lekin 0,5 daraja. Issiqxona uchun DHT22 tanlandi, chunki 1 daraja farq muhim.",
  "Bu jadval loyiha himoyasida eng ko'p savol tug'diradigan joyni oldindan yopib qo'yadi.",
 ]),
),

"Yechim variantlarini solishtirish": D(
 ("Variantlarni tuzish", [
  "Bitta muammoning kamida uch yechimi o'ylab topiladi.",
  "Birinchi kelgan g'oya deyarli hech qachon eng yaxshisi bo'lmaydi.",
  "Variantlar bir-biridan jiddiy farq qilishi kerak, kichik o'zgarish bilan emas.",
  "Masalan masofani o'lchash: ultratovush, infraqizil, lazer, kamera — to'rt xil yondashuv.",
 ]),
 ("Solishtirish jadvali", [
  "Ustunlar: variantlar. Qatorlar: mezonlar (aniqlik, narx, murakkablik, quvvat sarfi, mavjudlik).",
  "Har bir katakka baho qo'yiladi yoki aniq son yoziladi.",
  "Mezonlarning muhimligi teng emas — eng muhimlariga ko'proq og'irlik beriladi.",
  "Yakunda tanlov va uning sababi bir gapda yoziladi.",
  "Bu jadval muhandislik qarorining asosiy hujjati bo'ladi.",
 ]),
),

"Korpus yasash va montaj": D(
 ("Korpusning vazifalari", [
  "Himoya: chang, namlik va mexanik zarbadan saqlash.",
  "Mustahkamlash: simlar tortilib uzilmasligi uchun elementlarni qotirish.",
  "Xavfsizlik: ochiq kontaktlarni yopish.",
  "Ko'rinish: qurilma tayyor mahsulotga o'xshab qoladi — bu taqdimotda sezilarli ta'sir qiladi.",
 ]),
 ("Loyihalash qoidalari", [
  "Razyomlar uchun teshiklar oldindan o'lchab belgilanadi: USB, quvvat, sensor.",
  "Sensorlar tashqariga chiqarilishi kerak: harorat sensori korpus ichida bo'lsa, u korpus haroratini o'lchaydi.",
  "Havo almashinuvi: isiydigan elementlar uchun teshik qoldiriladi.",
  "Xizmat ko'rsatish: korpus ochilib, batareya almashtirilishi va kod qayta yuklanishi mumkin bo'lsin.",
  "Material: karton (tez prototip), plastik quti (arzon), 3D bosma (aniq, lekin vaqt oladi).",
 ]),
),

"Korpus va yakuniy montaj": D(
 ("Montaj tartibi", [
  "1) Korpusdagi hamma teshik oldindan tayyorlanadi.",
  "2) Razyomlar va tugmalar o'rnatiladi.",
  "3) Plata mahkamlanadi — u qimirlamasligi kerak.",
  "4) Simlar ulanadi va bog'lab tartibga solinadi.",
  "5) Korpus yopilishidan OLDIN to'liq sinov o'tkaziladi.",
  "Yopilgandan keyin xato topilsa, hammasini qayta ochishga to'g'ri keladi.",
 ]),
 ("Simlarni mahkamlash", [
  "Har bir sim shunday bog'lanishi kerakki, tortilganda kontakt emas, bog'lam kuchni ko'tarsin.",
  "Breadboard simlari korpusda ishonchsiz — yakuniy montajda kavsharlash yoki razyom ishlatiladi.",
  "Isituvchi naycha yoki izolyatsiya lentasi bilan ochiq joylar yopiladi.",
  "Simlar ranglari saqlanadi: keyin ochib qaraganda qaysi sim qayerga ketishi darhol ko'rinadi.",
 ]),
),

"Tizim arxitekturasini chizish": D(
 ("Arxitektura sxemasi nima", [
  "Bu printsipial sxema emas — bu qurilmaning KATTA bloklari va ular orasidagi aloqa.",
  "Bloklar: sensorlar, protsessor, ijro qurilmalari, aloqa moduli, quvvat manbai.",
  "Strelkalar ma'lumot yo'nalishini ko'rsatadi: sensordan protsessorga, protsessordan motorga.",
  "Bu sxema butun tizimni bir sahifada ko'rsatadi va uni tushuntirishni osonlashtiradi.",
 ]),
 ("Chizish tartibi", [
  "Markazga protsessor (plata) qo'yiladi.",
  "Chap tomonga kirishlar: sensorlar, tugmalar.",
  "O'ng tomonga chiqishlar: LED, motor, ekran.",
  "Yuqoriga aloqa: WiFi, Bluetooth, bulut.",
  "Pastga quvvat: manba, stabilizator, batareya.",
  "Har bir bog'lanishga interfeys nomi yoziladi: analog, I2C, SPI, PWM.",
 ]),
),

"Tizim arxitekturasini loyihalash": D(
 ("Loyihalashda hal qilinadigan savollar", [
  "Qaysi ish qurilmada, qaysi ish bulutda bajariladi.",
  "Ma'lumot qayerda saqlanadi: qurilmada, SD kartda yoki serverda.",
  "Aloqa uzilsa nima bo'ladi: qurilma ishlashda davom etadimi yoki to'xtaydimi.",
  "Quvvat o'chsa sozlamalar saqlanadimi.",
  "Bu savollarga oldindan javob berilmasa, keyin butun tuzilmani qayta qurishga to'g'ri keladi.",
 ]),
 ("Yaxshi arxitektura belgilari", [
  "Bloklar mustaqil: bittasini almashtirsa qolganlariga tegmaydi.",
  "Nosozlikka chidamli: bir qism ishlamay qolsa, tizim xavfsiz holatga o'tadi.",
  "Kengaytiriladigan: yangi sensor qo'shish uchun hammasini qayta yozish kerak emas.",
  "Tushunarli: sxemani ko'rgan odam tizim qanday ishlashini tushunadi.",
 ]),
),

"Tizimni sinash va o'lchash": D(
 ("O'lchanadigan ko'rsatkichlar", [
  "Javob vaqti (latency): hodisa bo'lgandan javob kelguncha o'tgan vaqt.",
  "Aniqlik: o'lchov etalonga qanchalik yaqin, foizda yoki mutlaq xatoda.",
  "Ishonchlilik: 100 sinovdan nechtasi to'g'ri ishladi.",
  "Quvvat sarfi: o'rtacha tok va batareya bilan ishlash muddati.",
  "Barqarorlik: uzoq ishlaganda ko'rsatkichlar o'zgaradimi.",
 ]),
 ("O'lchash usullari", [
  "Javob vaqti: millis() bilan hodisa va javob orasidagi farqni kodda o'lchash.",
  "Aniqlik: etalon asbob bilan yonma-yon o'lchab, farqni jadvalga yozish.",
  "Ishonchlilik: sinovni ko'p marta takrorlab, muvaffaqiyatlarni sanash.",
  "Quvvat: INA219 moduli yoki multimetr bilan tokni o'lchash.",
  "Har bir o'lchov kamida uch marta takrorlanadi va o'rtachasi olinadi.",
 ]),
),

"Sxema va kodni birga tekshirish": D(
 ("Nima uchun birga tekshiriladi", [
  "Xatolarning katta qismi sxema va kod O'RTASIDA bo'ladi: kodda D9 yozilgan, sim esa D10 da.",
  "Alohida tekshirilganda ikkalasi ham to'g'ri ko'rinadi, birga esa ishlamaydi.",
  "Shuning uchun tekshiruv jadvali tuziladi: kodda qaysi pin, sxemada qaysi pin, mos keladimi.",
 ]),
 ("Tekshirish tartibi", [
  "1) Koddagi hamma pin doimiylarini ro'yxat qilib yozish.",
  "2) Har biri uchun sxemadagi haqiqiy ulanishni tekshirish.",
  "3) Kirish va chiqish turlarini solishtirish: pinMode to'g'ri qo'yilganmi.",
  "4) Mantiqni tekshirish: INPUT_PULLUP bo'lsa kodda LOW ni kutish kerak.",
  "5) Quvvat va GND: tashqi manba bo'lsa umumiy GND ulanganmi.",
  "Bu besh qadam ko'p uchraydigan xatolarning deyarli hammasini topadi.",
 ]),
),

}


# ================================================================ KIRISH DARSLARI
# Chorak kirish darslari 32 ta. Ularning mazmuni mavzuga emas, YO'NALISHGA
# bog'liq: har bir yo'nalishda chorak boshida bir xil narsalar aytiladi.
KIRISH_YO = {

"elektronika": D(
 ("Chorak davomida qanday ishlaymiz", [
  "Har bir dars bir xil tartibda o'tadi: takrorlash, yangi mavzu, sxema yig'ish, o'lchash, natijani yozish.",
  "Ish juftlikda bajariladi: bittasi yig'adi, ikkinchisi sxema bo'yicha tekshiradi, keyin almashadilar.",
  "Har dars oxirida ish daftariga yoziladi: nima yig'ildi, qanday qiymat o'lchandi, qanday xato bo'ldi.",
  "Chorak oxirida nazorat musobaqasi va loyiha bo'ladi — ularning mezonlari oldindan e'lon qilinadi.",
 ]),
 ("Elektr xavfsizligi — asosiy qoidalar", [
  "Darsda ishlatiladigan kuchlanish 3,3-9 V — bu inson uchun xavfsiz oraliq.",
  "220 V bilan ishlash faqat o'qituvchi nazoratida va faqat namoyish tarzida bo'ladi.",
  "Zanjirni o'zgartirishdan oldin quvvat UZILADI. Ulangan holatda sim ulash — eng ko'p uchraydigan xato.",
  "Batareyaning ikki qutbini bevosita ulash mumkin emas: bu qisqa tutashuv, batareya qiziydi.",
  "Qizigan komponentni ushlamaslik: rezistor va stabilizator 80 darajagacha qizishi mumkin.",
  "Ishdan keyin quvvat uziladi va komponentlar joyiga qaytariladi.",
 ]),
 ("Ish o'rni va jihoz", [
  "Stol toza va quruq bo'lishi kerak — suv va elektronika birga bo'lmaydi.",
  "Komponentlar qutichada saralab saqlanadi: rezistorlar alohida, LEDlar alohida.",
  "Breadboard, multimetr va simlar to'plami har juftlikda alohida bo'ladi.",
  "Jihoz buzilsa yashirilmaydi — darhol aytiladi. Buzilgan jihoz bilan ishlash xavfli.",
  "To'plam to'liqligi dars boshida va oxirida ro'yxat bo'yicha tekshiriladi.",
 ]),
),

"arduino": D(
 ("Chorak davomida qanday ishlaymiz", [
  "Har bir dars uch qismdan iborat: yangi tushuncha, sxema yig'ish, dastur yozish va sinash.",
  "Kod har safar noldan yozilmaydi — oldingi darsdagi dastur ustiga qo'shib boriladi.",
  "Ishlaydigan har bir dastur alohida faylga saqlanadi, keyin qaytib kerak bo'ladi.",
  "Juftlikda ishlanadi: bittasi kod yozadi, ikkinchisi sxemani tekshiradi, keyin almashadilar.",
 ]),
 ("Dasturiy muhit va uni sozlash", [
  "Arduino IDE bepul dastur, u kodni yozadi, tekshiradi va plataga yuklaydi.",
  "Birinchi ulanishda drayver o'rnatilishi kerak, aks holda port ro'yxatda ko'rinmaydi.",
  "Har yuklashdan oldin ikki narsa tekshiriladi: Tools > Board (plata turi) va Tools > Port.",
  "Serial monitor tezligi koddagi Serial.begin qiymatiga MOS bo'lishi kerak, aks holda ma'nosiz belgilar chiqadi.",
  "Kod saqlanmagan bo'lsa IDE uni vaqtinchalik papkaga qo'yadi — shuning uchun har ishni o'z papkangizga saqlash kerak.",
 ]),
 ("Xavfsizlik va jihozni asrash", [
  "Plataga sim ulashdan oldin USB kabel UZILADI.",
  "Bir pindan maksimum 20 mA olish mumkin, butun platadan 200 mA. Motor va servo alohida quvvatlanadi.",
  "5V va GND ni bevosita ulash — qisqa tutashuv va plataning kuyishi.",
  "Platani metall sirtga qo'ymaslik: pastki tomonidagi kontaktlar tutashib ketadi.",
  "Modullarning qutbini tekshirish odat bo'lishi kerak: teskari ulangan modul bir zumda ishdan chiqadi.",
 ]),
),

"esp32": D(
 ("Chorak davomida qanday ishlaymiz", [
  "Darslar tarmoq va IoT ustiga quriladi: har bir dars natijasi telefon yoki brauzerda ko'rinadi.",
  "Sinf WiFi tarmog'i oldindan sozlanadi, nom va parol hammaga beriladi.",
  "Har bir juftlikning qurilmasi tarmoqda o'z IP manzilini oladi va u yozib olinadi.",
  "Kod bo'laklari qayta ishlatiladi: WiFi ga ulanish qismi deyarli har darsda bir xil bo'ladi.",
 ]),
 ("ESP32 ning Arduino'dan farqlari", [
  "Mantiq darajasi 3,3 V — 5 V signal pinni SHIKASTLAYDI. Bu eng muhim farq.",
  "ADC 12 bitli: qiymat 0 dan 4095 gacha (Uno'da 0-1023).",
  "Serial tezligi odatda 115200 (Uno'da 9600).",
  "Pin nomlari GPIO bilan beriladi va ularning bir qismi band: GPIO6-11 flesh xotiraga tegishli, ishlatilmaydi.",
  "GPIO34-39 faqat KIRISH uchun, ular chiqish bo'la olmaydi va ichki tortuvchi rezistori yo'q.",
  "Ba'zi platalarda yuklash paytida BOOT tugmasini bosib turish kerak bo'ladi.",
 ]),
 ("Tarmoq bilan ishlash madaniyati", [
  "WiFi paroli kodga ochiq yoziladi — shuning uchun kodni ulashishdan oldin uni olib tashlash kerak.",
  "Ochiq MQTT brokerlardan foydalanganda mavzu nomi noyob bo'lishi kerak, aks holda boshqalar ham ko'radi.",
  "Boshqaruv sahifasi parolsiz bo'lsa, tarmoqdagi har kim qurilmani boshqara oladi.",
  "Bulut xizmatlarining bepul chegarasi bor: ThingSpeak 15 sekundda bir marta yozishga ruxsat beradi.",
 ]),
),

"ai": D(
 ("Chorak davomida qanday ishlaymiz", [
  "Chorak AI loyihasining to'liq siklidan iborat: ma'lumot yig'ish, belgilash, o'rgatish, yuklash, sinash.",
  "Eng ko'p vaqt ma'lumot yig'ish va belgilashga ketadi — bu haqiqiy AI ishining asosiy qismi.",
  "Model brauzerda (Edge Impulse) o'rgatiladi, shuning uchun internet aloqasi kerak.",
  "Har bir bosqich natijasi ish daftariga raqam bilan yoziladi: nechta misol, qancha aniqlik, qancha kechikish.",
 ]),
 ("Jihoz va platforma", [
  "XIAO ESP32S3 Sense — kamera va mikrofoni platada o'rnatilgan, qo'shimcha sim kerak emas.",
  "Arduino IDE da PSRAM sozlamasi YOQILGAN bo'lishi shart, aks holda kamera ishlamaydi.",
  "Edge Impulse — bepul platforma, brauzerda ishlaydi, ro'yxatdan o'tish kerak.",
  "Model ZIP kutubxona sifatida yuklab olinadi va IDE ga Add .ZIP Library orqali qo'shiladi.",
  "Model qurilmaning O'ZIDA ishlaydi: internetsiz ham javob beradi va ma'lumot hech qayerga yuborilmaydi.",
 ]),
 ("Ma'lumot bilan ishlash qoidalari", [
  "Ovoz yoki tasvir yozib olishdan oldin odamdan rozilik so'raladi.",
  "Ma'lumot faqat shu loyiha uchun ishlatiladi va chorak oxirida keraksizi o'chiriladi.",
  "Yig'ishda xilma-xillik shart: turli odamlar, turli sharoit. Bir kishining ovozi bilan o'rgatilgan model boshqalarni tanimaydi.",
  "Har bir sinf uchun kamida 50-100 misol kerak va ular soni taxminan TENG bo'lishi lozim.",
  "'Fon' yoki 'hech narsa' sinfi ham albatta yig'iladi, aks holda model har qanday shovqinni buyruq deb qabul qiladi.",
 ]),
),

}
