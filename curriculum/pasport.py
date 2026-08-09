# -*- coding: utf-8 -*-
"""
KOMPONENT PASPORTI — har bir modul/komponentning to'liq texnik ma'lumotnomasi.

ulanish.py da faqat PIN XARITASI va kutubxona nomi bor. Bu yerda esa
o'qituvchi darsda aytishi kerak bo'lgan qolgan hamma narsa:

    tasnif  — texnik xususiyatlar (ta'minot, o'lchov oralig'i, aniqlik, tok, ...)
    ishlash — qurilma ichida FIZIK jihatdan nima sodir bo'ladi
    oqish   — qiymatni qanday o'qish, qanday formulaga solish
    kod     — to'liq, ko'chirib yuklasa ISHLAYDIGAN sketch
    qollash — hayotda qayerda uchraydi

Kalit — ulanish.py dagi ULANISH lug'atining kaliti bilan AYNAN bir xil.
Mos kelmasa __main__ tekshiruvi shuni aytadi.
"""


def P(tasnif, ishlash, oqish, kod=None, qollash=()):
    return {"tasnif": list(tasnif), "ishlash": list(ishlash),
            "oqish": list(oqish), "kod": kod, "qollash": list(qollash)}


PASPORT = {

# ============================================================ ASOSIY CHIQISH
"LED": P(
    tasnif=[
        "To'liq nomi: Light Emitting Diode — yorug'lik chiqaruvchi diod.",
        "Ishchi kuchlanishi (tushish kuchlanishi Uf): qizil 1,8-2,2 V; sariq va yashil 2,0-2,4 V; ko'k va oq 3,0-3,4 V.",
        "Nominal tok: 20 mA. 5 mA da ham yaxshi ko'rinadi, 30 mA dan oshsa umri qisqaradi.",
        "Qutbliligi bor: uzun oyoq — anod (+), kalta oyoq va korpusning yassi qirrasi — katod (-).",
        "Arduino pinining chegarasi: bitta pindan 40 mA (xavfsizi 20 mA), butun platadan 200 mA.",
    ],
    ishlash=[
        "LED ichida ikki xil yarimo'tkazgich qatlami tutashadi. Tok o'tganda elektron energiyasini yo'qotib, o'sha energiya YORUG'LIK sifatida chiqadi.",
        "Chiqadigan rang materialga bog'liq, kuchlanishga emas: ko'proq kuchlanish bersangiz rang o'zgarmaydi, LED kuyadi.",
        "Diod bo'lgani uchun tokni faqat bir tomonga o'tkazadi. Teskari ulansa yonmaydi (lekin buzilmaydi).",
    ],
    oqish=[
        "Rezistorni hisoblash: R = (Umanba - Uled) / I.",
        "Misol: 5 V plata, qizil LED (2 V), 20 mA -> R = (5 - 2) / 0,02 = 150 Om. Amalda 220 Om olinadi — biroz xiraroq, lekin xavfsizroq.",
        "Ko'k LED uchun: R = (5 - 3,2) / 0,02 = 90 Om, amalda 100-150 Om.",
        "Yorqinlikni boshqarish uchun analogWrite(pin, 0..255) — PWM (~) belgisi bor pinlarda.",
    ],
    kod="""// LED miltillashi va yorqinligini boshqarish
const int LED = 9;            // PWM pin (~ belgisi bor)

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  // 1) oddiy miltillash
  digitalWrite(LED, HIGH);  delay(500);
  digitalWrite(LED, LOW);   delay(500);

  // 2) asta yorishish (PWM)
  for (int y = 0; y <= 255; y++) { analogWrite(LED, y); delay(5); }
  for (int y = 255; y >= 0; y--) { analogWrite(LED, y); delay(5); }
}""",
    qollash=["Indikatorlar", "svetofor", "yoritish", "ekran orqa yorug'ligi", "pult signali"]),

"RGB LED (umumiy katod)": P(
    tasnif=[
        "Bitta korpusda uchta LED: qizil, yashil, ko'k. Oyog'i 4 ta.",
        "Umumiy katod turi: eng uzun oyoq GND ga. Umumiy anod turi: eng uzun oyoq 5V ga (mantiq teskari bo'ladi).",
        "Har bir rangga alohida rezistor: qizilga 220 Om, yashil va ko'kka 150-220 Om.",
        "Uchala pin ham PWM bo'lishi kerak: Uno'da 3, 5, 6, 9, 10, 11.",
    ],
    ishlash=[
        "Ko'z uchta yaqin turgan nurni ajratmaydi va ularni bitta rang deb qabul qiladi — bu ADDITIV rang aralashtirish.",
        "Har bir rangning yorqinligini PWM bilan 0 dan 255 gacha o'zgartirib, 256 x 256 x 256 = 16,7 million tus olinadi.",
        "Aynan shu prinsip telefon va televizor ekranida ham ishlaydi: har bir piksel uchta mayda R, G, B nuqtadan iborat.",
    ],
    oqish=[
        "Qizil = (255, 0, 0); Yashil = (0, 255, 0); Ko'k = (0, 0, 255).",
        "Sariq = qizil + yashil = (255, 255, 0). Moviy (cyan) = (0, 255, 255). Siyohrang = (255, 0, 255). Oq = (255, 255, 255).",
        "Umumiy ANOD turida qiymat teskari yoziladi: analogWrite(pin, 255 - qiymat).",
    ],
    kod="""// RGB LED — rang aralashtirish (umumiy KATOD)
const int R = 9, G = 10, B = 11;

void rang(int r, int g, int b) {
  analogWrite(R, r);  analogWrite(G, g);  analogWrite(B, b);
}

void setup() {
  pinMode(R, OUTPUT); pinMode(G, OUTPUT); pinMode(B, OUTPUT);
}

void loop() {
  rang(255, 0, 0);    delay(700);   // qizil
  rang(0, 255, 0);    delay(700);   // yashil
  rang(0, 0, 255);    delay(700);   // ko'k
  rang(255, 255, 0);  delay(700);   // sariq  = q + y
  rang(0, 255, 255);  delay(700);   // moviy  = y + k
  rang(255, 0, 255);  delay(700);   // siyoh  = q + k
  rang(255, 255, 255); delay(700);  // oq     = hammasi
}""",
    qollash=["Ekranlar", "kayfiyat chiroqlari", "holat indikatori", "dekorativ yoritish"]),

"Passiv zummer": P(
    tasnif=[
        "Ichida pyezoelektrik plastinka bor. Generator YO'Q — chastotani dastur berishi kerak.",
        "Ishchi kuchlanishi: 3-5 V. Tok: 20-30 mA (pin chegarasida, shuning uchun 100 Om qo'yish tavsiya etiladi).",
        "Chastota oralig'i: 100 Hz - 5000 Hz. Eng baland tovush 2000-3000 Hz atrofida chiqadi.",
        "Aktiv zummerdan farqi: aktivga faqat kuchlanish berilsa yetadi, u bitta ohangda \"biq\" qiladi; passivda esa istalgan nota chiqariladi.",
    ],
    ishlash=[
        "Pyezoplastinkaga kuchlanish berilsa u biroz egiladi, olinsa qaytadi. Sekundiga 440 marta egilsa — havoda 440 Hz to'lqin hosil bo'ladi, quloq buni \"lya\" notasi deb eshitadi.",
        "Chastota — sekundiga necha marta tebranish. Chastota katta bo'lsa tovush INGICHKA, kichik bo'lsa YO'G'ON.",
        "Nota bir oktava yuqori bo'lsa chastota ROSA IKKI BARAVAR ortadi: lya = 440 Hz, keyingi lya = 880 Hz.",
    ],
    oqish=[
        "tone(pin, chastota) — tovushni boshlaydi va o'zi davom etadi (loopni to'xtatmaydi).",
        "tone(pin, chastota, davomiylik) — belgilangan millisekunddan keyin o'zi to'xtaydi.",
        "noTone(pin) — to'xtatadi.",
        "Nota chastotalari: do 262, re 294, mi 330, fa 349, sol 392, lya 440, si 494, do2 523 Hz.",
    ],
    kod="""// Passiv zummer: gamma va qisqa melodiya
const int Z = 8;
// do   re   mi   fa   sol  lya  si   do2
int gamma[8] = {262, 294, 330, 349, 392, 440, 494, 523};

void setup() {
  pinMode(Z, OUTPUT);

  // 1) gammani yuqoriga chalish
  for (int i = 0; i < 8; i++) {
    tone(Z, gamma[i]);
    delay(300);
  }
  noTone(Z);
  delay(500);
}

// 2) melodiya: nota va davomiyliklar massivi
int nota[]  = {392, 392, 440, 392, 523, 494};
int vaqt[]  = {400, 400, 400, 400, 400, 800};

void loop() {
  for (int i = 0; i < 6; i++) {
    tone(Z, nota[i], vaqt[i]);
    delay(vaqt[i] * 1.3);      // notalar orasida kichik tanaffus
  }
  delay(2000);
}""",
    qollash=["Ogohlantirish signali", "budilnik", "tugma bosilganini bildirish", "parkovka radari"]),

"7-segment indikator (1 razryad)": P(
    tasnif=[
        "Sakkizta LED: a, b, c, d, e, f, g segmentlari va DP (nuqta).",
        "Ikki turi bor: umumiy KATOD (COM -> GND, segment HIGH da yonadi) va umumiy ANOD (COM -> 5V, segment LOW da yonadi).",
        "Har bir segmentga alohida 220 Om rezistor — jami 7-8 ta.",
        "Bir segment 20 mA tortadi; \"8\" raqamida hammasi yonadi va 160 mA bo'ladi — bu plata chegarasiga yaqin.",
    ],
    ishlash=[
        "Har bir raqam ma'lum segmentlar to'plamidan yig'iladi: 1 = b va c; 7 = a, b, c; 8 = hammasi.",
        "Turini aniqlash: multimetrni diod rejimiga qo'yib, COM ga qora shchupni tegizing — segmentlar yonsa umumiy katod.",
    ],
    oqish=[
        "Raqamlar jadval (massiv) ko'rinishida saqlanadi: har bir raqam uchun 7 ta 0/1 qiymat.",
        "0 -> abcdef; 1 -> bc; 2 -> abdeg; 3 -> abcdg; 4 -> bcfg; 5 -> acdfg; 6 -> acdefg; 7 -> abc; 8 -> hammasi; 9 -> abcdfg.",
    ],
    kod="""// 7-segment (umumiy KATOD) — 0..9 raqamlari
const int seg[7] = {2, 3, 4, 5, 6, 7, 8};   // a b c d e f g

//                a  b  c  d  e  f  g
byte raqam[10][7] = {
  {1, 1, 1, 1, 1, 1, 0},   // 0
  {0, 1, 1, 0, 0, 0, 0},   // 1
  {1, 1, 0, 1, 1, 0, 1},   // 2
  {1, 1, 1, 1, 0, 0, 1},   // 3
  {0, 1, 1, 0, 0, 1, 1},   // 4
  {1, 0, 1, 1, 0, 1, 1},   // 5
  {1, 0, 1, 1, 1, 1, 1},   // 6
  {1, 1, 1, 0, 0, 0, 0},   // 7
  {1, 1, 1, 1, 1, 1, 1},   // 8
  {1, 1, 1, 1, 0, 1, 1}    // 9
};

void korsat(int n) {
  for (int i = 0; i < 7; i++) digitalWrite(seg[i], raqam[n][i]);
}

void setup() {
  for (int i = 0; i < 7; i++) pinMode(seg[i], OUTPUT);
}

void loop() {
  for (int n = 0; n <= 9; n++) { korsat(n); delay(800); }
}""",
    qollash=["Soat", "hisoblagich", "tarozi ko'rsatkichi", "navbat raqami"]),

"74HC595 siljish registri": P(
    tasnif=[
        "Kirish: 3 pin (DATA, CLOCK, LATCH). Chiqish: 8 pin (Q0...Q7).",
        "Ta'minot: 2-6 V. Bitta chiqish maksimum 35 mA, butun mikrosxema 70 mA.",
        "Ketma-ket ulash mumkin: birinchisining Q7' pini ikkinchisining DATA piniga — 3 pin bilan 16, 24, 32 chiqish.",
        "Ish tezligi: 100 MHz gacha, ya'ni Arduino uchun cheklov emas.",
    ],
    ishlash=[
        "Ichida 8 ta xotira katagi navbat bo'lib turadi. CLOCK har ko'tarilganda navbat bir qadam siljiydi va DATA pinidagi qiymat boshiga kiradi.",
        "8 marta siljitilgandan keyin LATCH ko'tariladi — shundagina 8 ta qiymat bir vaqtda chiqishga uzatiladi.",
        "LATCH shuning uchun kerak: usiz chiqishlar siljish paytida ko'z oldida \"yugurib\" ko'rinardi.",
    ],
    oqish=[
        "shiftOut(dataPin, clockPin, MSBFIRST, qiymat) — bitta baytni yuboradi.",
        "Bayt bitlari chiqishlarga mos keladi: B10000000 -> faqat Q7 yonadi, B00000001 -> faqat Q0.",
        "Ketma-ketlik doim bir xil: LATCH LOW -> shiftOut -> LATCH HIGH.",
    ],
    kod="""// 74HC595 — 3 pin bilan 8 ta LED
const int DATA = 11, CLOCK = 12, LATCH = 8;

void yubor(byte qiymat) {
  digitalWrite(LATCH, LOW);                       // yozishni to'xtatib turamiz
  shiftOut(DATA, CLOCK, MSBFIRST, qiymat);        // 8 bitni siljitamiz
  digitalWrite(LATCH, HIGH);                      // hammasini birdan chiqaramiz
}

void setup() {
  pinMode(DATA, OUTPUT); pinMode(CLOCK, OUTPUT); pinMode(LATCH, OUTPUT);
}

void loop() {
  // yuguruvchi olov
  for (int i = 0; i < 8; i++) { yubor(1 << i); delay(120); }
  // ikkilik sanoq: 0 dan 255 gacha
  for (int n = 0; n < 256; n++) { yubor(n); delay(60); }
}""",
    qollash=["Ko'p LEDli tablo", "7-segmentli soat", "pin yetishmaganda kengaytirish"]),

"LED matritsa 8x8 (MAX7219)": P(
    tasnif=[
        "64 ta LED (8 qator x 8 ustun), bitta MAX7219 boshqaruvchi mikrosxema bilan.",
        "Ta'minot: 5 V, modul to'liq yorqinlikda 300 mA gacha tortadi.",
        "Yorqinlik 16 pog'onali: setIntensity(0...15).",
        "Bir necha modulni ketma-ket ulash mumkin (yuguruvchi qator uchun).",
    ],
    ishlash=[
        "64 ta LEDni bir vaqtda yoqib bo'lmaydi — MAX7219 qatorlarni juda tez navbat bilan yoqadi (multipleks).",
        "Bir qator ~1 ms yonadi, sekundiga 800 marta aylanadi. Ko'z bu tezlikni ilg'amaydi va hamma nuqta doim yonib turgandek ko'rinadi.",
        "Aynan shu prinsip televizor va monitorda ham qo'llaniladi.",
    ],
    oqish=[
        "lc.setLed(0, qator, ustun, holat) — bitta nuqtani yoqadi/o'chiradi.",
        "lc.setRow(0, qator, B10101010) — butun qatorni bir baytda beradi.",
        "Rasm 8 ta baytdan iborat massiv sifatida saqlanadi — daftarga katakli chizib, keyin 0/1 ga aylantirish qulay.",
    ],
    kod="""// MAX7219 8x8 matritsa — yurakcha rasmi
#include <LedControl.h>
//                 DIN  CLK  CS  modullar soni
LedControl lc = LedControl(12, 11, 10, 1);

byte yurak[8] = {
  B00000000,
  B01100110,
  B11111111,
  B11111111,
  B11111111,
  B01111110,
  B00111100,
  B00011000
};

void setup() {
  lc.shutdown(0, false);     // uyqu rejimidan chiqarish
  lc.setIntensity(0, 4);     // yorqinlik 0..15
  lc.clearDisplay(0);
}

void loop() {
  for (int q = 0; q < 8; q++) lc.setRow(0, q, yurak[q]);
  delay(1000);
  lc.clearDisplay(0);
  delay(400);
}""",
    qollash=["Yuguruvchi yozuv", "o'yin ekrani", "smaylik indikator", "reklama tablosi"]),

"WS2812 adreslanadigan LED lenta": P(
    tasnif=[
        "Har bir LED ichida o'z boshqaruvchi mikrosxemasi bor — shuning uchun 100 ta LEDni BITTA sim bilan alohida-alohida boshqarish mumkin.",
        "Ta'minot: 5 V. Bitta LED to'liq oq rangda 60 mA (3 x 20 mA) tortadi.",
        "8 LED = 0,5 A; 30 LED = 1,8 A — bunda tashqi 5 V manba SHART, USB yetmaydi.",
        "Ma'lumot pini bitta va yo'nalishi bor: DIN tomondan kiradi, DOUT tomondan chiqadi.",
    ],
    ishlash=[
        "Ma'lumot zanjir bo'ylab uzatiladi: birinchi LED o'ziga tegishli 24 bitni olib qoladi, qolganini keyingisiga o'tkazadi.",
        "Har bir LED uchun 24 bit = 8 bit qizil + 8 bit yashil + 8 bit ko'k.",
        "Uzatish juda tez (800 kbit/s), shuning uchun vaqt talabi qat'iy — kutubxonasiz yozib bo'lmaydi.",
    ],
    oqish=[
        "strip.setPixelColor(nomer, strip.Color(r, g, b)) — xotiraga yozadi, hali ko'rinmaydi.",
        "strip.show() — xotiradagi hammasini lentaga uzatadi. BU CHAQIRILMASA hech narsa o'zgarmaydi.",
        "strip.setBrightness(0..255) — umumiy yorqinlik, tokni cheklash uchun 50-80 qo'yish tavsiya etiladi.",
    ],
    kod="""// WS2812 — kamalak effekti
#include <Adafruit_NeoPixel.h>
#define PIN 6
#define SONI 8
Adafruit_NeoPixel lenta(SONI, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  lenta.begin();
  lenta.setBrightness(60);   // tokni cheklash uchun
  lenta.show();              // hammasini o'chirib boshlaymiz
}

void loop() {
  // 1) birma-bir qizil yondirish
  for (int i = 0; i < SONI; i++) {
    lenta.setPixelColor(i, lenta.Color(255, 0, 0));
    lenta.show();
    delay(120);
  }
  lenta.clear(); lenta.show(); delay(300);

  // 2) kamalak
  for (int siljish = 0; siljish < 256; siljish++) {
    for (int i = 0; i < SONI; i++) {
      int tus = (i * 65536L / SONI + siljish * 256L) % 65536;
      lenta.setPixelColor(i, lenta.gamma32(lenta.ColorHSV(tus)));
    }
    lenta.show();
    delay(20);
  }
}""",
    qollash=["Dekorativ yoritish", "holat chizig'i", "robot ko'zlari", "yangi yil chiroqlari"]),

"LCD 1602 (I2C moduli bilan)": P(
    tasnif=[
        "16 belgi x 2 qator. Har bir belgi 5x8 nuqtadan iborat.",
        "Ta'minot: 5 V, 20-25 mA (orqa yorug'lik bilan birga).",
        "I2C moduli (PCF8574) bilan atigi 4 sim kerak; usiz 12 sim kerak bo'lardi.",
        "I2C manzili: odatda 0x27 yoki 0x3F — modulga qarab farq qiladi.",
    ],
    ishlash=[
        "Ekranda suyuq kristall molekulalari kuchlanish ta'sirida buriladi va yorug'likni o'tkazmay qo'yadi — shu joy qora ko'rinadi.",
        "Ekran o'zi yorug'lik chiqarmaydi, orqadan LED yoritib turadi. Shuning uchun quyoshda ham yaxshi ko'rinadi va kam quvvat sarflaydi.",
        "I2C moduli 8 ta parallel simni 2 ta simga aylantirib beradi (kengaytirgich mikrosxema).",
    ],
    oqish=[
        "lcd.setCursor(ustun, qator) — 0 dan boshlanadi: chap yuqori burchak = (0, 0).",
        "lcd.print(qiymat) — matn yoki son yozadi. Eski matn AVTOMATIK o'chmaydi.",
        "Qiymat qisqarganda \"12\" o'rnida \"123\" dan qolgan \"3\" turib qoladi — shuning uchun lcd.print(\"    \") bilan ustidan bo'sh joy yoziladi.",
    ],
    kod="""// LCD 1602 I2C — harorat va sanoqni ko'rsatish
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);   // manzil ishlamasa 0x3F ni sinang

int sanoq = 0;

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Tarbion maktabi");
  delay(1500);
  lcd.clear();
}

void loop() {
  lcd.setCursor(0, 0);
  lcd.print("Sanoq:");

  lcd.setCursor(0, 1);
  lcd.print(sanoq);
  lcd.print("    ");        // eski raqam qoldig'ini o'chirish

  sanoq++;
  delay(500);
}""",
    qollash=["Meteostansiya", "menyu", "o'lchov asboblari", "sanoq tablosi"]),

"OLED ekran 0.96\" (SSD1306, I2C)": P(
    tasnif=[
        "128 x 64 piksel, o'lchami 0,96 dyuym. 0,91\" (128x32) turi ham bor.",
        "Ta'minot: 3,3 V yoki 5 V (modulda stabilizator bo'lsa). Tok: 10-20 mA.",
        "I2C manzili: 0x3C (ba'zan 0x3D).",
        "Rangi: bir rangli (oq/ko'k) yoki ikki zonali (yuqori qator sariq, qolgani ko'k).",
    ],
    ishlash=[
        "OLED = Organic Light Emitting Diode. Har bir piksel O'ZI yorug'lik chiqaradi — orqa yoritish kerak emas.",
        "Qora piksel — butunlay o'chgan piksel. Shuning uchun qorasi chinakam qora va kontrast juda yuqori.",
        "LCD dan farqi: LCD da orqa lampa doim yonadi, OLED da esa faqat kerakli nuqtalar yonadi — bu quvvat tejaydi.",
    ],
    oqish=[
        "Chizish buyruqlari faqat XOTIRAGA yozadi. display.display() chaqirilmaguncha ekranda hech narsa o'zgarmaydi.",
        "display.clearDisplay() — xotirani tozalaydi (eski rasm ustiga yozilib ketmasligi uchun har safar kerak).",
        "setTextSize(1) = 6x8 piksel (21 belgi x 8 qator); setTextSize(2) = ikki barobar katta.",
        "Grafik: drawLine, drawRect, fillRect, drawCircle, drawBitmap.",
    ],
    kod="""// OLED SSD1306 — matn va oddiy grafik
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
Adafruit_SSD1306 ekran(128, 64, &Wire, -1);

int qiymat = 0;

void setup() {
  Serial.begin(9600);
  if (!ekran.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED topilmadi! Manzilni (0x3C/0x3D) tekshiring.");
    while (true);
  }
  ekran.clearDisplay();
  ekran.setTextColor(SSD1306_WHITE);
}

void loop() {
  ekran.clearDisplay();

  ekran.setTextSize(1);
  ekran.setCursor(0, 0);
  ekran.print("Harorat:");

  ekran.setTextSize(2);
  ekran.setCursor(0, 16);
  ekran.print(qiymat);
  ekran.print(" C");

  // pastda progress chizig'i
  ekran.drawRect(0, 50, 128, 10, SSD1306_WHITE);
  ekran.fillRect(0, 50, map(qiymat, 0, 50, 0, 128), 10, SSD1306_WHITE);

  ekran.display();          // ENG MUHIM QATOR — usiz ekran bo'sh qoladi

  qiymat = (qiymat + 1) % 51;
  delay(200);
}""",
    qollash=["Kichik o'lchov asboblari", "soatlar", "robot yuzi", "menyu ekrani"]),

# ============================================================ KIRISH
"Tugma (push button)": P(
    tasnif=[
        "Taktil tugma (tact switch) — 4 oyoqli, lekin aslida 2 ta kontakt: qarama-qarshi oyoqlar juft-juft ulangan.",
        "Bosilganda kontakt ulanadi, qo'yib yuborilganda prujina uni ochadi.",
        "Kontakt sakrashi (bounce): bir marta bosishda kontakt 5-50 millisekund davomida bir necha marta ulanib-uzilib turadi.",
        "Ichki tortuvchi rezistor (INPUT_PULLUP) qiymati: Arduino'da 20-50 kOm.",
    ],
    ishlash=[
        "Rezistorsiz ulangan pin havoda \"suzadi\": unga tegishmagan holatda ham atrofdagi elektr maydonidan tasodifiy 0 va 1 o'qiladi.",
        "Tortuvchi rezistor pinni tinch holatda aniq bir darajaga tortib turadi. INPUT_PULLUP da pin 5 V ga tortiladi, ya'ni tinch holat = HIGH.",
        "Shuning uchun INPUT_PULLUP bilan tugma BOSILGANDA LOW o'qiladi — mantiq teskari ko'ringani bilan bu eng ishonchli usul.",
    ],
    oqish=[
        "digitalRead(pin) — HIGH yoki LOW qaytaradi.",
        "Bosilish LAHZASINI ushlash uchun oldingi holat bilan solishtiriladi (front detection).",
        "Sakrashni yo'qotish: holat o'zgargandan keyin 30-50 ms kutish yoki millis() bilan filtr qo'yish.",
    ],
    kod="""// Tugma: INPUT_PULLUP, sakrashni filtrlash va bosilish sonini sanash
const int TUGMA = 2, LED = 9;

int oldingi = HIGH;
unsigned long ozgargan = 0;
const unsigned long FILTR = 40;   // millisekund
int sanoq = 0;
bool yongan = false;

void setup() {
  pinMode(TUGMA, INPUT_PULLUP);   // ichki rezistor yoqiladi
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int hozir = digitalRead(TUGMA);

  if (hozir != oldingi) {          // holat o'zgardi — vaqtni belgilaymiz
    ozgargan = millis();
    oldingi = hozir;
  }

  // o'zgargandan keyin FILTR vaqt o'tgan bo'lsa, bu haqiqiy bosish
  if (millis() - ozgargan == FILTR && hozir == LOW) {
    sanoq++;
    yongan = !yongan;              // har bosishda LED holatini almashtiramiz
    digitalWrite(LED, yongan);
    Serial.print("Bosildi: ");
    Serial.println(sanoq);
  }
}""",
    qollash=["Boshqaruv paneli", "start/stop", "menyu", "eshik qo'ng'irog'i"]),

"Potensiometr 10 kOm": P(
    tasnif=[
        "O'zgaruvchan rezistor. Nominal 10 kOm — chetdagi ikki oyoq orasidagi qarshilik doim 10 kOm.",
        "O'rta oyoq (surgich) buralganda 0 dan 10 kOm gacha siljiydi.",
        "Burilish burchagi: odatda 270 daraja (bir aylanmaydi).",
        "Arduino'ning ADC si 10 bitli: 0-5 V oralig'i 0-1023 ga aylanadi, ya'ni bir qadam 5/1024 = 4,9 mV.",
    ],
    ishlash=[
        "Potensiometr — bu tayyor KUCHLANISH BO'LUVCHI. Surgich yuqoriroqda bo'lsa chiqishda kuchlanish katta, pastroqda bo'lsa kichik.",
        "Qarshilik emas, KUCHLANISH o'lchanadi: plata analog pindagi kuchlanishni raqamga aylantiradi.",
        "ESP32 da ADC 12 bitli (0-4095) va kirish 3,3 V — 5 V berish taqiqlanadi.",
    ],
    oqish=[
        "analogRead(A0) -> 0...1023 (Uno) yoki 0...4095 (ESP32).",
        "Kuchlanishga aylantirish: U = analogRead(A0) * 5.0 / 1023.",
        "Boshqa oraliqqa o'tkazish: map(qiymat, 0, 1023, 0, 255) — masalan LED yorqinligi uchun.",
        "map(qiymat, 0, 1023, 0, 180) — servo burchagi uchun.",
    ],
    kod="""// Potensiometr: xom qiymat, kuchlanish va LED yorqinligi
const int POT = A0, LED = 9;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int xom = analogRead(POT);                 // 0..1023
  float u  = xom * 5.0 / 1023.0;             // voltga aylantirish
  int yorq = map(xom, 0, 1023, 0, 255);      // PWM oralig'iga

  analogWrite(LED, yorq);

  Serial.print("xom=");   Serial.print(xom);
  Serial.print("  U=");   Serial.print(u, 2);
  Serial.print(" V  yorqinlik="); Serial.println(yorq);

  delay(200);
}""",
    qollash=["Ovoz balandligi", "yorqinlik sozlagich", "sozlash tugmasi", "robot qo'li burchagi"]),

"Fotorezistor (LDR)": P(
    tasnif=[
        "LDR = Light Dependent Resistor. Qarshiligi YORUG'LIKKA bog'liq.",
        "Qorong'ida: 200 kOm - 1 MOm. Yorug'da: 1-10 kOm. To'g'ridan-to'g'ri chiroq ostida: 100-500 Om.",
        "Qutbliligi YO'Q — istalgan tomonga ulanadi.",
        "Javob tezligi sekin: 10-100 ms. Tez o'zgarishlarni (masalan lampa miltillashini) ilg'amaydi.",
    ],
    ishlash=[
        "Ichidagi kadmiy sulfid (CdS) qatlamiga foton tushganda elektronlar bo'shab qoladi va material tokni yaxshiroq o'tkazadi.",
        "Yorug'lik ko'p -> erkin elektron ko'p -> qarshilik KICHIK. Qorong'i -> qarshilik KATTA.",
        "Plata qarshilikni o'lchay olmaydi, faqat kuchlanishni o'lchaydi — shuning uchun LDR ni 10 kOm rezistor bilan BO'LUVCHI qilib ulash SHART.",
    ],
    oqish=[
        "Sxema: 5V -> LDR -> (A0 nuqtasi) -> 10 kOm -> GND.",
        "Bu ulanishda yorug'da A0 qiymati KATTA, qorong'ida KICHIK bo'ladi.",
        "Kalibrlash: xonada, chiroq yoqilganda va qo'l bilan yopilganda qiymatlarni yozib olib, chegara (masalan 400) tanlanadi.",
        "Chegara atrofida chiroq \"titrab\" qolmasligi uchun GISTEREZIS qo'yiladi: 350 dan past bo'lsa yoqadi, 450 dan yuqori bo'lsa o'chiradi.",
    ],
    kod="""// Fotorezistor: gisterezisli tungi chiroq
const int LDR = A0, LED = 9;
const int QORONGI = 350;   // shu qiymatdan PAST bo'lsa — yoqamiz
const int YORUG   = 450;   // shu qiymatdan YUQORI bo'lsa — o'chiramiz

bool yongan = false;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int q = analogRead(LDR);

  // GISTEREZIS: ikki xil chegara chiroqning titrashini yo'qotadi
  if (!yongan && q < QORONGI) { yongan = true;  }
  if ( yongan && q > YORUG)   { yongan = false; }

  digitalWrite(LED, yongan);

  Serial.print("yorug'lik="); Serial.print(q);
  Serial.print("  chiroq=");  Serial.println(yongan ? "YONIQ" : "O'CHIQ");
  delay(200);
}""",
    qollash=["Ko'cha chiroqlari", "telefon ekrani yorqinligi", "avtomatik parda", "chiziq bo'ylab yuruvchi robot"]),

"NTC termistor": P(
    tasnif=[
        "NTC = Negative Temperature Coefficient: harorat OSHSA qarshilik KAMAYADI.",
        "Nominal qiymat 25 °C da beriladi — maktab to'plamlarida odatda 10 kOm.",
        "B koeffitsienti: 3435 K (formulada ishlatiladi, datasheetda yoziladi).",
        "O'lchov oralig'i: -40 dan +125 °C gacha. Aniqlik: ±1-2 °C (kalibrlanmagan holda).",
    ],
    ishlash=[
        "Termistor — yarimo'tkazgich. Isiganda ichidagi erkin elektronlar soni ortadi va tokni yaxshiroq o'tkazadi.",
        "Bog'liqlik CHIZIQLI EMAS — shuning uchun analogRead qiymatini to'g'ridan-to'g'ri gradus deb olib bo'lmaydi.",
        "Fotorezistor bilan bir xil sxema: bo'luvchi kerak, chunki plata faqat kuchlanishni o'qiy oladi.",
    ],
    oqish=[
        "1-qadam: qarshilikni topish. R = 10000 * (1023.0 / analogRead(A0) - 1).",
        "2-qadam: Shteynhart-Xart (soddalashtirilgan B-formula) bilan haroratga o'tish.",
        "1/T = 1/T0 + (1/B) * ln(R/R0), bu yerda T0 = 298,15 K (25 °C), R0 = 10000 Om, B = 3435.",
        "3-qadam: Kelvindan Selsiyga: T(°C) = T(K) - 273,15.",
        "Soddaroq yo'l (5-6-sinf uchun): muzli suv (0 °C) va iliq suv (~40 °C) da qiymat yozib olib, map() bilan oraliqni chizmalash.",
    ],
    kod="""// NTC termistor -> gradus (B-formula)
const int PIN = A0;
const float R0 = 10000.0;    // 25 C dagi qarshilik
const float B  = 3435.0;     // datasheetdan
const float T0 = 298.15;     // 25 C = 298,15 K
const float RD = 10000.0;    // bo'luvchidagi doimiy rezistor

void setup() { Serial.begin(9600); }

void loop() {
  int xom = analogRead(PIN);

  // 1) termistor qarshiligi
  float R = RD * (1023.0 / xom - 1.0);

  // 2) qarshilikdan haroratga
  float T = 1.0 / (1.0 / T0 + (1.0 / B) * log(R / R0));

  // 3) Kelvin -> Selsiy
  float C = T - 273.15;

  Serial.print("xom="); Serial.print(xom);
  Serial.print("  R=");  Serial.print(R, 0); Serial.print(" Om");
  Serial.print("  T=");  Serial.print(C, 1); Serial.println(" C");
  delay(1000);
}""",
    qollash=["Termostat", "3D printer ekstruderi", "muzlatgich", "isitgich himoyasi"]),

"DHT22 (harorat va namlik)": P(
    tasnif=[
        "To'liq nomi: DHT22 / AM2302 — raqamli harorat va nisbiy namlik sensori.",
        "Harorat oralig'i: -40 dan +80 °C gacha. Aniqlik: ±0,5 °C. Qadam (rezolyutsiya): 0,1 °C.",
        "Namlik oralig'i: 0 dan 100 % gacha. Aniqlik: ±2-5 %. Qadam: 0,1 %.",
        "Ta'minot: 3,3-6 V. Tok: o'lchash paytida 1-1,5 mA, kutish holatida 40-50 mkA.",
        "O'lchash tezligi: SEKUNDIGA BIR MARTA (0,5 Hz). Tezroq so'ralsa eski qiymat yoki nan qaytadi.",
        "Oyoqlari (old tomondan, panjara qarshimizda): 1-VCC, 2-DATA, 3-NC (ulanmaydi), 4-GND.",
        "DHT11 dan farqi: DHT11 arzonroq, lekin oralig'i 0-50 °C, aniqligi ±2 °C va qadami butun son.",
    ],
    ishlash=[
        "Ichida ikkita sezgir element bor. Harorat uchun — termistor. Namlik uchun — ikki plastinka orasidagi namlik yutuvchi qatlam (kondensator sig'imi namlikka qarab o'zgaradi).",
        "Muhimi: bu qiymatlarni PLATA emas, SENSORNING O'ZI hisoblaydi. Ichida kichik mikrosxema bor, u o'lchaydi, hisoblaydi va tayyor RAQAM yuboradi.",
        "Shuning uchun DHT22 — RAQAMLI sensor. analogRead bilan o'qib bo'lmaydi, analogRead unda ma'nosiz qiymat beradi.",
        "Bitta DATA simi ikki tomonlama ishlaydi: avval plata \"boshla\" degan signal yuboradi, keyin sensor 40 bit ma'lumot qaytaradi.",
        "Bit uzunligi impuls kengligi bilan ifodalanadi: qisqa impuls = 0, uzun impuls = 1. Bu vaqt juda aniq (mikrosekundlarda) o'lchanishi kerak — shuning uchun KUTUBXONA SHART.",
        "40 bit tarkibi: 16 bit namlik + 16 bit harorat + 8 bit tekshirish yig'indisi (checksum).",
    ],
    oqish=[
        "Kutubxona: \"DHT sensor library\" (Adafruit) + u talab qiladigan \"Adafruit Unified Sensor\".",
        "E'lon qilish: DHT dht(2, DHT22); — birinchi son DATA pini, ikkinchisi sensor turi.",
        "setup() da: dht.begin();",
        "Harorat: float t = dht.readTemperature();  — Selsiyda.",
        "Farengeytda kerak bo'lsa: dht.readTemperature(true).",
        "Namlik: float h = dht.readHumidity();  — foizda.",
        "Har o'qishdan keyin isnan(t) bilan TEKSHIRISH shart — sensor javob bermasa nan qaytadi va uni ekranga chiqarish xato ko'rsatkich beradi.",
        "\"His qilinadigan harorat\" ni ham hisoblaydi: dht.computeHeatIndex(t, h, false).",
        "DATA va VCC orasiga 10 kOm tortuvchi rezistor qo'yilmasa, o'qish ko'p hollarda nan qaytaradi.",
    ],
    kod="""// DHT22 — harorat va namlikni o'qish (xatoni tekshirish bilan)
#include <DHT.h>

#define DHTPIN  2          // DATA pini
#define DHTTUR  DHT22      // DHT11 bo'lsa: DHT11
DHT dht(DHTPIN, DHTTUR);

unsigned long oxirgi = 0;
const unsigned long ORALIQ = 2000;   // DHT22 uchun eng kami 1000 ms

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("DHT22 ishga tushdi. Harorat / Namlik:");
}

void loop() {
  // delay() o'rniga millis() — dastur boshqa ishni ham bajara olsin
  if (millis() - oxirgi < ORALIQ) return;
  oxirgi = millis();

  float h = dht.readHumidity();       // namlik, %
  float t = dht.readTemperature();    // harorat, C

  // MAJBURIY tekshiruv: sensor javob bermasa nan qaytadi
  if (isnan(h) || isnan(t)) {
    Serial.println("XATO: sensordan javob yo'q. Simlarni va 10 kOm rezistorni tekshiring.");
    return;
  }

  float his = dht.computeHeatIndex(t, h, false);   // his qilinadigan harorat

  Serial.print("Harorat: "); Serial.print(t, 1); Serial.print(" C   ");
  Serial.print("Namlik: ");  Serial.print(h, 1); Serial.print(" %   ");
  Serial.print("His: ");     Serial.print(his, 1); Serial.println(" C");

  if (h > 70) Serial.println("  -> Havo nam. Shamollatish kerak.");
  if (t > 30) Serial.println("  -> Issiq. Ventilyatorni yoqish mumkin.");
}""",
    qollash=["Meteostansiya", "issiqxona nazorati", "konditsioner avtomatikasi", "ombor namligini kuzatish"]),

"HC-SR04 (ultratovush masofa)": P(
    tasnif=[
        "O'lchov oralig'i: 2 sm dan 400 sm gacha. Amalda ishonchli oraliq — 3 sm dan 200 sm gacha.",
        "Aniqlik: ±3 mm. Ko'rish burchagi: 15 daraja.",
        "Ta'minot: 5 V, tok 15 mA. 3,3 V da ishonchsiz ishlaydi.",
        "Chastota: 40 kHz — bu tovush inson qulog'iga eshitilmaydi (ultratovush).",
        "O'lchash tezligi: sekundiga 20 martagacha (har o'lchov orasida 60 ms qo'yish tavsiya etiladi).",
        "Oyoqlari: VCC, TRIG (chiqish), ECHO (kirish), GND.",
    ],
    ishlash=[
        "Modulda ikkita silindr bor: biri tovush YUBORADI (T), ikkinchisi QABUL QILADI (R).",
        "TRIG piniga 10 mikrosekundlik HIGH berilsa, modul 8 ta 40 kHz impuls yuboradi.",
        "Tovush buyumga urilib qaytadi. Qaytgan paytda ECHO pini HIGH bo'lib turadi.",
        "ECHO qancha vaqt HIGH turgani — tovushning BORIB-KELISH vaqti.",
        "Havoda tovush tezligi 20 °C da 343 m/s = 0,0343 sm/mkrs. Shuning uchun formulada 0,034 ishlatiladi.",
        "Bu ko'rshapalak va delfin ishlatadigan EXOLOKATSIYA prinsipi.",
    ],
    oqish=[
        "1) TRIG ni 2 mkrs LOW, keyin 10 mkrs HIGH, keyin LOW qilish.",
        "2) vaqt = pulseIn(ECHO, HIGH) — ECHO necha mikrosekund HIGH turganini qaytaradi.",
        "3) masofa = vaqt * 0.034 / 2.",
        "IKKIGA BO'LISH SHART: tovush borib va qaytib, ya'ni masofani IKKI MARTA bosib o'tdi.",
        "Buyum yo'q bo'lsa pulseIn kutib qoladi — timeout qo'yish kerak: pulseIn(ECHO, HIGH, 30000).",
        "Yumshoq mato, gilam va qiyshiq sirt tovushni qaytarmaydi — o'lchov noto'g'ri chiqadi.",
    ],
    kod="""// HC-SR04 — masofa o'lchash va parkovka radari
const int TRIG = 9, ECHO = 10, ZUMMER = 8;

float masofaOlch() {
  digitalWrite(TRIG, LOW);   delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);  delayMicroseconds(10);   // 10 mkrs impuls
  digitalWrite(TRIG, LOW);

  // 30000 mkrs = ~5 m; buyum bo'lmasa cheksiz kutib qolmaslik uchun
  long vaqt = pulseIn(ECHO, HIGH, 30000);
  if (vaqt == 0) return -1;                  // javob kelmadi

  return vaqt * 0.034 / 2.0;                 // borib-kelgani uchun 2 ga bo'lamiz
}

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  float d = masofaOlch();

  if (d < 0) {
    Serial.println("Buyum topilmadi (juda uzoq yoki tovushni qaytarmaydi)");
  } else {
    Serial.print("Masofa: "); Serial.print(d, 1); Serial.println(" sm");

    // masofa kamaygan sari signal tez-tez chiqadi
    if (d < 50) {
      int tanaffus = map((int)d, 5, 50, 60, 700);
      tone(ZUMMER, 2000, 50);
      delay(tanaffus);
      return;
    }
  }
  delay(200);
}""",
    qollash=["Parkovka radari", "to'siqdan qochuvchi robot", "suv sathini o'lchash", "avtomatik eshik"]),

"PIR HC-SR501 (harakat)": P(
    tasnif=[
        "PIR = Passive InfraRed. \"Passiv\" — o'zi hech narsa nurlantirmaydi, faqat tinglaydi.",
        "Sezish masofasi: 3 dan 7 metrgacha (moduldagi vint bilan sozlanadi).",
        "Ko'rish burchagi: 100-110 daraja.",
        "Ta'minot: 4,5-20 V (5 V qulay). Tok: 50 mkA — juda kam.",
        "Chiqish signali: raqamli, 3,3 V. Harakat bor -> HIGH, yo'q -> LOW.",
        "Isinish vaqti: yoqilgandan keyin 30-60 sekund. Bu vaqtda noto'g'ri signal beradi.",
        "Ikki vint: Sx — sezgirlik (masofa), Tx — signal necha sekund HIGH turishi (0,3 s dan 5 minutgacha).",
    ],
    ishlash=[
        "Har qanday issiq jism infraqizil nur chiqaradi. Inson tanasi ~10 mikrometr to'lqin uzunligida nurlanadi.",
        "Sensor ichida ikkita sezgir maydon bor. Ular ko'radigan nurlanish TENG bo'lsa — signal yo'q.",
        "Odam harakatlanganda avval bitta maydonga, keyin ikkinchisiga issiqlik tushadi. FARQ paydo bo'ladi — mana shu farq \"harakat bor\" degan signalni beradi.",
        "Shuning uchun PIR qimirlamay turgan odamni SEZMAYDI — u harakatni sezadi, issiqlikni emas.",
        "Ustidagi oq linza (Frenel linzasi) ko'rish maydonini bir necha sektorga bo'lib beradi.",
    ],
    oqish=[
        "digitalRead(pin) — HIGH bo'lsa harakat bor.",
        "Modul o'zi ushlab turadi: bir marta sezsa, Tx vinti bilan sozlangan vaqt davomida HIGH turadi. Dasturda qo'shimcha taymer shart emas.",
        "Ikki rejim jumperi: H (repeat) — harakat davom etsa vaqt qayta boshlanadi; L (single) — bir marta ishlab, keyin pauza.",
        "Sinovda: quyosh nuri, isitgich va konditsioner oqimi noto'g'ri ishlashiga sabab bo'ladi.",
    ],
    kod="""// PIR — harakatni sezib chiroqni yoqish (isinish hisobga olingan)
const int PIR = 2, LED = 9;
unsigned long boshlangan;
const unsigned long ISINISH = 40000;   // 40 sekund

void setup() {
  pinMode(PIR, INPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  boshlangan = millis();
  Serial.println("PIR isiyapti, 40 sekund kuting...");
}

void loop() {
  // isinish tugamaguncha signalga ishonmaymiz
  if (millis() - boshlangan < ISINISH) {
    digitalWrite(LED, LOW);
    return;
  }

  int harakat = digitalRead(PIR);
  digitalWrite(LED, harakat);

  static int oldingi = LOW;
  if (harakat != oldingi) {
    Serial.println(harakat == HIGH ? "HARAKAT SEZILDI" : "harakat tugadi");
    oldingi = harakat;
  }
}""",
    qollash=["Avtomatik chiroq", "signalizatsiya", "avtomatik kran", "odam sanagich"]),

"Tuproq namligi datchigi": P(
    tasnif=[
        "Ikki xil turi bor: rezistiv (ikki metall vilka) va sig'imli (capacitive, bir butun plastina).",
        "Ta'minot: 3,3-5 V. Tok: 5-20 mA.",
        "Chiqish: analog (A0) va raqamli (D0, moduldagi potensiometr bilan sozlanadigan chegara).",
        "Rezistiv turi tez korroziyaga uchraydi — bir necha oyda ishdan chiqadi. Sig'imli turi ancha uzoq xizmat qiladi.",
        "Namunaviy qiymatlar (rezistiv, 5 V): quruq havo ~1023, quruq tuproq ~800, nam tuproq ~400, suvda ~250.",
    ],
    ishlash=[
        "Rezistiv turida: quruq tuproq yomon o'tkazgich, nam tuproq esa (ichidagi tuz eritmasi tufayli) yaxshi o'tkazgich. Ikki vilka orasidagi qarshilik namlikka qarab o'zgaradi.",
        "Doimiy kuchlanish berilganda elektroliz boshlanadi: metall eriydi va vilkaga oq g'ubor o'tiradi — bu korroziya.",
        "Sig'imli turida metall tuproqqa TEGMAYDI, o'lchash elektr maydoni orqali boradi — shuning uchun korroziya bo'lmaydi.",
    ],
    oqish=[
        "analogRead(A0) — son KATTA bo'lsa tuproq QURUQ (rezistiv turida).",
        "Foizga aylantirish: namlik = map(xom, 1023, 300, 0, 100) — chetlari o'lchab, o'z to'plamingizga moslanadi.",
        "Kalibrlash SHART: havoda va bir stakan suvda qiymat yozib olinadi, shu ikki chet oraliq deb qabul qilinadi.",
        "Korroziyani kamaytirish: VCC ni raqamli pinga ulab, faqat o'lchash lahzasida yoqish (masalan 10 daqiqada bir marta).",
    ],
    kod="""// Tuproq namligi — kalibrlangan va nasosni boshqaradigan
const int SENSOR = A0;
const int QUVVAT = 7;      // sensorga quvvat — faqat o'lchash paytida
const int NASOS  = 8;      // rele orqali nasos

const int QURUQ = 1010;    // havoda o'lchangan qiymat
const int HOL    = 300;    // suvda o'lchangan qiymat

int namlikFoiz() {
  digitalWrite(QUVVAT, HIGH);
  delay(300);                        // sensor barqarorlashsin
  int xom = analogRead(SENSOR);
  digitalWrite(QUVVAT, LOW);         // korroziyani kamaytiramiz

  int foiz = map(xom, QURUQ, HOL, 0, 100);
  return constrain(foiz, 0, 100);
}

void setup() {
  pinMode(QUVVAT, OUTPUT);
  pinMode(NASOS, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int n = namlikFoiz();
  Serial.print("Tuproq namligi: "); Serial.print(n); Serial.println(" %");

  if (n < 30) {
    Serial.println("  -> Quruq. Sug'orish yoqildi.");
    digitalWrite(NASOS, HIGH);
    delay(3000);                     // 3 sekund sug'oramiz
    digitalWrite(NASOS, LOW);
  }
  delay(10000);                      // 10 sekundda bir tekshiramiz
}""",
    qollash=["Avtomatik sug'orish", "issiqxona", "gulzor nazorati", "qishloq xo'jaligi IoT"]),

"Suv sathi datchigi": P(
    tasnif=[
        "Bir nechta parallel o'tkazgich yo'lakdan iborat plastina.",
        "Ta'minot: 3,3-5 V. Tok: 20 mA gacha.",
        "Chiqish: analog. Sensorning suvga botgan qismi qancha ko'p bo'lsa, qiymat shuncha katta.",
        "Ish balandligi: odatda 40 mm.",
        "Doimiy suvda turishi tavsiya etilmaydi — korroziya boshlanadi.",
    ],
    ishlash=[
        "Plastinada ikki xil yo'lak navbat bilan joylashgan: bittasi quvvatga, ikkinchisi o'lchov chiqishiga ulangan.",
        "Suv ikki yo'lakni tutashtiradi. Qancha ko'p yo'lak suv ostida qolsa, umumiy qarshilik shuncha kichik va chiqish kuchlanishi shuncha katta.",
        "Ya'ni bu ham aslida qarshilik o'lchash — faqat qarshilikni suvning o'zi hosil qiladi.",
        "Distillangan suv tokni deyarli o'tkazmaydi — sensor faqat oddiy (tuzli) suvda ishlaydi.",
    ],
    oqish=[
        "analogRead(A0): quruq ~0, bir oz botgan ~300, to'liq botgan ~600-700.",
        "Kalibrlash: quruq holatda va to'liq botgan holatda qiymat yozib olinadi.",
        "Sathni sm ga aylantirish: map(xom, quruq, toliq, 0, 4) — sensor balandligi 4 sm bo'lsa.",
    ],
    kod="""// Suv sathi — bak to'lganini kuzatish
const int SATH = A0, ZUMMER = 8, LED = 9;
const int QURUQ = 20, TOLIQ = 650;    // kalibrlashda o'lchangan

void setup() {
  pinMode(ZUMMER, OUTPUT); pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int xom  = analogRead(SATH);
  int foiz = constrain(map(xom, QURUQ, TOLIQ, 0, 100), 0, 100);

  Serial.print("xom="); Serial.print(xom);
  Serial.print("  sath="); Serial.print(foiz); Serial.println(" %");

  if (foiz > 90) {                       // to'lib ketmoqda
    digitalWrite(LED, HIGH);
    tone(ZUMMER, 1500, 200);
  } else if (foiz < 10) {                // bo'shab qoldi
    digitalWrite(LED, LOW);
    tone(ZUMMER, 500, 200);
  } else {
    digitalWrite(LED, LOW);
  }
  delay(1000);
}""",
    qollash=["Suv baki nazorati", "yomg'ir sezgichi", "toshqin signalizatsiyasi", "avtomatik nasos"]),

"Ovoz (mikrofon) datchigi": P(
    tasnif=[
        "Modulda elektret mikrofon va LM393 taqqoslagich bor.",
        "Ta'minot: 3,3-5 V. Tok: 4-5 mA.",
        "Ikki chiqish: AO — tovush kuchining analog qiymati; DO — chegaradan oshganda 0/1.",
        "Moduldagi potensiometr DO chegarasini sozlaydi (AO ga ta'sir qilmaydi).",
        "Chastota oralig'i: 50 Hz - 20 kHz.",
    ],
    ishlash=[
        "Elektret mikrofon ichida juda yupqa membrana bor. Tovush to'lqini unga urilib tebratadi.",
        "Membrana tebranishi sig'imni o'zgartiradi, bu esa kichik o'zgaruvchan kuchlanish hosil qiladi.",
        "Signal juda kuchsiz (millivoltlarda) — shuning uchun modulda kuchaytirgich bor.",
        "AO chiqishida tinch holatda ~512 (o'rta nuqta) turadi va tovushda shu nuqta atrofida tebranadi.",
    ],
    oqish=[
        "Bir marta analogRead qilish YETARLI EMAS — tovush tebranish, tasodifan nol nuqtaga tushib qolish mumkin.",
        "To'g'ri usul: 50 ms davomida ko'p marta o'qib, ENG KATTA va ENG KICHIK qiymatni topish. Farqi — tovush kuchi.",
        "Qarsakni aniqlash: shu farq keskin chegaradan oshsa. Filtr sifatida oxirgi qarsakdan keyin 300 ms kutiladi.",
    ],
    kod="""// Mikrofon — qarsak bilan chiroqni yoqib-o'chirish
const int MIC = A0, LED = 9;
const int CHEGARA = 120;          // sinovda tanlanadi
bool yongan = false;
unsigned long oxirgiQarsak = 0;

int tovushKuchi() {
  unsigned long boshi = millis();
  int engKatta = 0, engKichik = 1023;

  while (millis() - boshi < 50) {          // 50 ms tinglaymiz
    int q = analogRead(MIC);
    if (q > engKatta)  engKatta  = q;
    if (q < engKichik) engKichik = q;
  }
  return engKatta - engKichik;             // tebranish kengligi
}

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int kuch = tovushKuchi();
  Serial.println(kuch);

  // 300 ms filtr: bitta qarsak ikki marta sanalmasin
  if (kuch > CHEGARA && millis() - oxirgiQarsak > 300) {
    oxirgiQarsak = millis();
    yongan = !yongan;
    digitalWrite(LED, yongan);
    Serial.println("  -> QARSAK!");
  }
}""",
    qollash=["Qarsakli chiroq", "shovqin darajasini o'lchash", "ovoz bilan boshqarish", "AI uchun ovoz yig'ish"]),

"Reed datchigi (magnit kalit)": P(
    tasnif=[
        "Shisha kolbaga solingan ikkita elastik metall til.",
        "Magnit yaqinlashganda tillar bir-biriga tortiladi va kontakt ulanadi.",
        "Ishga tushish masofasi: 10-20 mm (magnit kuchiga bog'liq).",
        "Kommutatsiya: 100 V gacha, 0,5 A gacha. Xizmat muddati: 10 million marta ulanish.",
        "Qutbliligi yo'q, oddiy tugma kabi ulanadi.",
    ],
    ishlash=[
        "Tillar ferromagnit materialdan. Magnit maydoniga tushganda ular o'zlari magnitlanadi — biri shimoliy, ikkinchisi janubiy qutbga aylanadi.",
        "Qarama-qarshi qutblar tortishadi va tillar tegib, zanjirni ulaydi.",
        "Magnit olib qo'yilsa tillar o'z elastikligi bilan qaytadi va zanjir uziladi.",
        "Ichida vakuum yoki inert gaz bor — shuning uchun kontakt kuymaydi va uzoq ishlaydi.",
    ],
    oqish=[
        "Tugma bilan bir xil: pinMode(pin, INPUT_PULLUP) va digitalRead(pin).",
        "Magnit yonida = LOW (ulangan), magnit yo'q = HIGH (uzilgan).",
        "Eshik/deraza signalizatsiyasida: magnit — qanotga, datchik — romga o'rnatiladi.",
        "Aylanish tezligini o'lchash uchun: g'ildirakka magnit yopishtiriladi, har aylanishda bitta signal keladi.",
    ],
    kod="""// Reed datchigi — eshik ochilganini aniqlash va signal berish
const int REED = 2, ZUMMER = 8, LED = 9;
int oldingi = LOW;

void setup() {
  pinMode(REED, INPUT_PULLUP);
  pinMode(ZUMMER, OUTPUT); pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // magnit yonida LOW; eshik ochilsa magnit uzoqlashadi -> HIGH
  int ochiq = digitalRead(REED);

  if (ochiq != oldingi) {
    oldingi = ochiq;
    if (ochiq == HIGH) {
      Serial.println("ESHIK OCHILDI!");
      digitalWrite(LED, HIGH);
      for (int i = 0; i < 3; i++) { tone(ZUMMER, 2000, 150); delay(300); }
    } else {
      Serial.println("Eshik yopildi.");
      digitalWrite(LED, LOW);
    }
    delay(50);      // kontakt sakrashiga qarshi
  }
}""",
    qollash=["Eshik signalizatsiyasi", "velosiped spidometri", "suv hisoblagichi", "noutbuk qopqog'i datchigi"]),

"Hall datchigi": P(
    tasnif=[
        "Magnit maydonini elektr signalga aylantiradi. Ikki turi bor: raqamli (bor/yo'q) va analog (kuchini o'lchaydi).",
        "Ta'minot: 3,3-5 V (A3144 uchun 4,5-24 V). Tok: 5-10 mA.",
        "Javob tezligi: mikrosekundlarda — Reed datchigidan ancha tez, minglab ayl/min ni bemalol sanaydi.",
        "Ko'p turlari QUTBGA sezgir: faqat janubiy (yoki faqat shimoliy) qutbga javob beradi.",
        "Mexanik kontakt yo'q — cheksiz uzoq ishlaydi va sakrash (bounce) bermaydi.",
    ],
    ishlash=[
        "Hall effekti: tok o'tayotgan yassi plastinka magnit maydoniga qo'yilsa, magnit kuchi elektronlarni bir chetga siqib qo'yadi.",
        "Natijada plastinkaning ikki cheti orasida kichik kuchlanish paydo bo'ladi — bu Hall kuchlanishi.",
        "U magnit maydon kuchiga TO'G'RI PROPORSIONAL, shuning uchun analog turida maydonni o'lchash mumkin.",
        "Raqamli turida ichidagi taqqoslagich bu kuchlanishni chegara bilan solishtirib, 0 yoki 1 beradi.",
    ],
    oqish=[
        "Raqamli tur: digitalRead(pin). Ko'p modullarda magnit yonida LOW.",
        "Analog tur: analogRead(A0). Magnitsiz ~512, bir qutb yaqinlashsa oshadi, ikkinchisi yaqinlashsa kamayadi.",
        "Aylanish tezligini o'lchash: aylanishlarni 1 sekund sanab, keyin 60 ga ko'paytirish -> ayl/min (RPM).",
        "Tez aylanishda sanoqni uzilish (interrupt) bilan olish kerak: attachInterrupt.",
    ],
    kod="""// Hall datchigi — aylanish tezligini (RPM) o'lchash
const int HALL = 2;              // Uno'da uzilish pini
volatile unsigned int impuls = 0;
unsigned long oxirgi = 0;

void sanash() { impuls++; }      // uzilishda chaqiriladi — juda qisqa bo'lishi kerak

void setup() {
  pinMode(HALL, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(HALL), sanash, FALLING);
  Serial.begin(9600);
}

void loop() {
  if (millis() - oxirgi >= 1000) {          // har sekundda hisoblaymiz
    oxirgi = millis();

    noInterrupts();
    unsigned int n = impuls;
    impuls = 0;
    interrupts();

    unsigned int rpm = n * 60;              // g'ildirakda 1 ta magnit bo'lsa

    Serial.print("Sekundiga aylanish: "); Serial.print(n);
    Serial.print("   RPM: ");              Serial.println(rpm);
  }
}""",
    qollash=["Velosiped/avtomobil spidometri", "ventilyator tezligi", "motor enkoderi", "kontaktsiz tugma"]),

"Qiyalik (tilt) datchigi": P(
    tasnif=[
        "Metall silindr ichida kichik o'tkazuvchi sharcha (yoki simob tomchisi) bor.",
        "Ta'minot kerak emas — oddiy kalit kabi ishlaydi.",
        "Ishga tushish burchagi: odatda 15-30 daraja.",
        "Faqat BOR/YO'Q beradi — burchakni o'lchamaydi. Burchak kerak bo'lsa MPU6050 ishlatiladi.",
    ],
    ishlash=[
        "Tik holatda sharcha pastga tushib, ikkita kontaktni tutashtiradi — zanjir ulangan.",
        "Qiyaltirilganda sharcha yumalab ketadi va kontakt uziladi.",
        "Silkitilganda sharcha ichkarida sakraydi — signal bir necha marta ulanib-uziladi. Shuning uchun dasturiy filtr kerak.",
    ],
    oqish=[
        "Tugma bilan bir xil: INPUT_PULLUP va digitalRead(pin).",
        "Silkitishni aniqlash: qisqa vaqt ichida holat necha marta o'zgarganini sanash.",
        "Barqaror qiyalikni aniqlash: holat 200 ms davomida o'zgarmay tursa — bu haqiqiy qiyalik.",
    ],
    kod="""// Tilt datchigi — qiyalik va silkitishni ajratish
const int TILT = 2, LED = 9, ZUMMER = 8;

int oldingi = HIGH;
unsigned long ozgargan = 0;
int ozgarishSoni = 0;
unsigned long oyna = 0;

void setup() {
  pinMode(TILT, INPUT_PULLUP);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int hozir = digitalRead(TILT);

  if (hozir != oldingi) {
    oldingi = hozir;
    ozgargan = millis();
    ozgarishSoni++;
  }

  // 1 sekundlik oynada 5 dan ko'p o'zgarish bo'lsa — SILKITISH
  if (millis() - oyna >= 1000) {
    if (ozgarishSoni > 5) {
      Serial.println("SILKITILDI!");
      tone(ZUMMER, 1200, 200);
    }
    ozgarishSoni = 0;
    oyna = millis();
  }

  // 200 ms barqaror tursa — haqiqiy QIYALIK
  if (millis() - ozgargan > 200) digitalWrite(LED, hozir == LOW);
}""",
    qollash=["O'g'irlik signalizatsiyasi", "yiqilishni aniqlash", "o'yin pulti", "qutini ochishni sezish"]),

"Olov (flame) datchigi": P(
    tasnif=[
        "Infraqizil fotodiod (odatda ko'k rangli) 760-1100 nm to'lqin uzunligiga sezgir.",
        "Sezish masofasi: 80 sm gacha (sham olovi uchun ~30-50 sm).",
        "Ko'rish burchagi: 60 daraja.",
        "Ta'minot: 3,3-5 V. Ikki chiqish: AO (olov kuchi) va DO (bor/yo'q).",
        "Javob tezligi: 15 mikrosekund — juda tez.",
    ],
    ishlash=[
        "Olov ko'zga ko'rinadigan yorug'likdan tashqari kuchli INFRAQIZIL nur ham chiqaradi.",
        "Fotodiod aynan shu infraqizil oraliqda sezgir. Unga IQ nur tushsa, chiqish kuchlanishi o'zgaradi.",
        "Muammo: quyosh nuri, cho'g'lanma lampa va isitgich ham IQ nur chiqaradi — ular ham signal beradi.",
        "Shuning uchun ishonchli yong'in tizimida olov datchigi YOLG'IZ ishlatilmaydi: tutun (MQ-2) va harorat datchiklari bilan birga qo'shib qaror qilinadi.",
    ],
    oqish=[
        "DO: digitalRead(pin) — ko'p modullarda olov bo'lsa LOW.",
        "AO: analogRead(A0) — olov qancha yaqin/kuchli bo'lsa qiymat shuncha KICHIK (fotodiod qarshiligi tushadi).",
        "Chegara sinov yo'li bilan tanlanadi: xonada odatiy qiymat yozib olinib, shamni turli masofada sinaladi.",
        "Ishonchliroq qilish: 3 ta ketma-ket o'lchov ham chegaradan o'tsagina signal berish.",
    ],
    kod="""// Olov datchigi — ikki bosqichli tekshiruv bilan yong'in signali
const int OLOV_A = A0, OLOV_D = 3, ZUMMER = 8, LED = 9;
int chegara = 300;          // sinovda aniqlanadi
int ketmaKet = 0;

void setup() {
  pinMode(OLOV_D, INPUT);
  pinMode(ZUMMER, OUTPUT); pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int kuch = analogRead(OLOV_A);      // KICHIK qiymat = olov yaqin
  Serial.print("olov qiymati: "); Serial.println(kuch);

  if (kuch < chegara) ketmaKet++;
  else                ketmaKet = 0;

  // uch marta ketma-ket tasdiqlansagina signal beramiz (yolg'on signalga qarshi)
  if (ketmaKet >= 3) {
    digitalWrite(LED, HIGH);
    tone(ZUMMER, 2500, 300);
    Serial.println("  -> YONG'IN XAVFI!");
  } else {
    digitalWrite(LED, LOW);
  }
  delay(200);
}""",
    qollash=["Yong'in signalizatsiyasi", "olovni o'chiruvchi robot", "gaz plitasi nazorati"]),

"MQ-2 (gaz va tutun)": P(
    tasnif=[
        "Sezadigan moddalar: LPG (suyultirilgan gaz), propan, metan, vodorod, spirt tug'lari va TUTUN.",
        "Sezish oralig'i: 300-10000 ppm (million ulushdagi zarracha).",
        "Ta'minot: 5 V SHART — ichidagi qizdirgich uchun kerak. Tok: 150 mA gacha.",
        "Isinish vaqti: qisqa sinov uchun 2-3 daqiqa, aniq o'lchov uchun 24-48 soat (burn-in).",
        "Modul ishlaganda sezilarli isiydi — bu normal holat, nosozlik emas.",
        "Chiqish: AO (konsentratsiya) va DO (chegaradan oshsa).",
    ],
    ishlash=[
        "Ichida qalay dioksidi (SnO2) qatlami va uni 200-300 °C gacha qizdiradigan spiral bor.",
        "Toza havoda kislorod molekulalari sirtga o'tirib, elektronlarni ushlab turadi — qarshilik KATTA.",
        "Yonuvchi gaz kelsa, u kislorod bilan reaksiyaga kirishadi va ushlab turilgan elektronlarni bo'shatadi — qarshilik KESKIN KAMAYADI.",
        "Shuning uchun qizdirgich shart: reaksiya faqat yuqori haroratda boradi.",
        "Sensor gaz TURINI ajratmaydi — u faqat \"yonuvchi nimadir bor\" deydi. Turini ajratish uchun boshqa (qimmatroq) sensorlar kerak.",
    ],
    oqish=[
        "analogRead(A0) — qiymat KATTA bo'lsa gaz KO'P.",
        "Toza havodagi qiymatni (R0) o'lchab olish kerak — bu har bir sensorda boshqacha.",
        "Aniq ppm hisoblash uchun datasheetdagi egri chiziq va Rs/R0 nisbati ishlatiladi; maktab darajasida NISBIY qiymat (ortdi/kamaydi) yetarli.",
        "Sinov: yoqilgan gugurtni o'chirib, tutunini sensorga yaqinlashtirish (o't emas, TUTUN).",
    ],
    kod="""// MQ-2 — isinishni kutib, keyin gaz/tutunni kuzatish
const int MQ = A0, ZUMMER = 8, LED = 9;
const unsigned long ISINISH = 180000;   // 3 daqiqa
int tozaHavo = 0;                       // isinishdan keyin o'lchanadi

void setup() {
  pinMode(ZUMMER, OUTPUT); pinMode(LED, OUTPUT);
  Serial.begin(9600);

  Serial.println("MQ-2 isiyapti (3 daqiqa)...");
  unsigned long boshi = millis();
  while (millis() - boshi < ISINISH) {
    digitalWrite(LED, (millis() / 500) % 2);   // kutayotganini bildiramiz
  }
  digitalWrite(LED, LOW);

  tozaHavo = analogRead(MQ);          // etalon qiymat
  Serial.print("Toza havo qiymati: "); Serial.println(tozaHavo);
}

void loop() {
  int q = analogRead(MQ);
  int ortish = q - tozaHavo;

  Serial.print("qiymat="); Serial.print(q);
  Serial.print("  toza havodan ortishi="); Serial.println(ortish);

  if (ortish > 150) {
    digitalWrite(LED, HIGH);
    tone(ZUMMER, 2500, 400);
    Serial.println("  -> GAZ/TUTUN ANIQLANDI! Xonani shamollating.");
  } else {
    digitalWrite(LED, LOW);
  }
  delay(500);
}""",
    qollash=["Gaz sizishi signalizatsiyasi", "yong'in datchigi", "havo sifati stansiyasi", "oshxona xavfsizligi"]),

"Joystik moduli": P(
    tasnif=[
        "Ikkita 10 kOm potensiometr (X va Y o'qlari uchun) va bitta bosish tugmasi.",
        "Ta'minot: 5 V (yoki 3,3 V). Tok: 5 mA dan kam.",
        "Chiqish: VRx va VRy — analog; SW — raqamli (bosilganda GND ga ulanadi).",
        "O'rta holatdagi qiymat: Uno'da 500-520 atrofida (har bir modulda biroz farq qiladi).",
        "Harakat oralig'i: 0 dan 1023 gacha, lekin chetlarga to'liq yetmasligi mumkin (masalan 5...1018).",
    ],
    ishlash=[
        "Har bir o'q uchun alohida potensiometr bor. Tayoqcha surilganda uning surgichi buriladi.",
        "Ya'ni joystik — bu ikkita potensiometrning bitta korpusda birlashtirilgani.",
        "Prujina tayoqchani doim markazga qaytaradi — shuning uchun qo'yib yuborilsa qiymat o'rtaga qaytadi.",
        "Tayoqchani bosish alohida mikrotugmani ishga tushiradi.",
    ],
    oqish=[
        "int x = analogRead(A0); int y = analogRead(A1); int bosildi = !digitalRead(2);",
        "Markazni topish: dastur boshida (tayoqchaga tegmasdan) o'qib, uni \"nol\" sifatida saqlash.",
        "O'lik zona (dead zone) qo'yish SHART: markazdan ±40 ichidagi o'zgarish e'tiborga olinmaydi, aks holda joystik tegmasa ham \"qimirlaydi\".",
        "Yo'nalishga aylantirish: markazdan farq musbat/manfiy ekaniga qarab yuqori/past, o'ng/chap aniqlanadi.",
    ],
    kod="""// Joystik — yo'nalishni aniqlash (o'lik zona bilan)
const int VRX = A0, VRY = A1, SW = 2;
int markazX, markazY;
const int OLIK = 40;      // o'lik zona

void setup() {
  pinMode(SW, INPUT_PULLUP);
  Serial.begin(9600);

  delay(200);
  markazX = analogRead(VRX);      // tayoqchaga TEGMASDAN kalibrlanadi
  markazY = analogRead(VRY);
  Serial.print("Markaz: "); Serial.print(markazX);
  Serial.print(", ");            Serial.println(markazY);
}

void loop() {
  int dx = analogRead(VRX) - markazX;
  int dy = analogRead(VRY) - markazY;

  String yonalish = "markaz";
  if (dx >  OLIK) yonalish = "O'NG";
  if (dx < -OLIK) yonalish = "CHAP";
  if (dy >  OLIK) yonalish = "PAST";
  if (dy < -OLIK) yonalish = "YUQORI";

  Serial.print(yonalish);
  if (digitalRead(SW) == LOW) Serial.print("  + BOSILDI");
  Serial.println();

  delay(150);
}""",
    qollash=["Robot pulti", "o'yin boshqaruvi", "kamera burish", "menyu bo'ylab harakat"]),

"Klaviatura 4x4 (keypad)": P(
    tasnif=[
        "16 tugma, lekin atigi 8 pin: 4 qator (R1-R4) va 4 ustun (C1-C4).",
        "Ta'minot kerak emas — passiv matritsa, faqat tugmalar va o'tkazgichlar.",
        "4x3 turi ham bor (12 tugma, 7 pin).",
        "Har bir tugma o'z qatori va ustuni kesishmasida turadi.",
    ],
    ishlash=[
        "Agar har bir tugmaga alohida pin bersak, 16 pin kerak bo'lardi — Arduino Uno'da esa hammasi bo'lib 20 ta pin bor.",
        "Matritsa skanerlash: plata qatorlarni BIRMA-BIR pastga tortadi va shu payt ustunlarni o'qiydi.",
        "Agar 2-qator pastga tortilganda 3-ustun ham past bo'lib qolsa — demak (2, 3) kesishmasidagi tugma bosilgan.",
        "Butun skanerlash bir necha mikrosekundda tugaydi va sekundiga minglab marta takrorlanadi — shuning uchun tugma bosilishi darhol sezilaadi.",
        "Bu usul monitor, LED tablo va kompyuter klaviaturasida ham ishlatiladi.",
    ],
    oqish=[
        "Keypad kutubxonasi bilan: char tugma = keypad.getKey(); — bosilmagan bo'lsa NO_KEY qaytadi.",
        "Tugmalar xaritasi kodda 2 o'lchamli massiv sifatida beriladi va haqiqiy klaviaturaga mos kelishi kerak.",
        "Parol yig'ish: bosilgan belgilarni String yoki massivga to'plab, '#' bosilganda solishtiriladi.",
        "'*' odatda o'chirish (tozalash) uchun ishlatiladi.",
    ],
    kod="""// 4x4 klaviatura — parolli kirish nazorati
#include <Keypad.h>

const byte QATOR = 4, USTUN = 4;
char xarita[QATOR][USTUN] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte qatorPin[QATOR] = {9, 8, 7, 6};
byte ustunPin[USTUN] = {5, 4, 3, 2};

Keypad kp = Keypad(makeKeymap(xarita), qatorPin, ustunPin, QATOR, USTUN);

const String PAROL = "1234";
String kiritilgan = "";
const int LED_YASHIL = 10, LED_QIZIL = 11, ZUMMER = 12;

void setup() {
  pinMode(LED_YASHIL, OUTPUT); pinMode(LED_QIZIL, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
  Serial.println("Parolni kiriting va # bosing:");
}

void loop() {
  char t = kp.getKey();
  if (!t) return;

  tone(ZUMMER, 1500, 40);            // har bosishda qisqa signal

  if (t == '#') {                    // tasdiqlash
    if (kiritilgan == PAROL) {
      Serial.println("KIRISHGA RUXSAT");
      digitalWrite(LED_YASHIL, HIGH); delay(2000); digitalWrite(LED_YASHIL, LOW);
    } else {
      Serial.println("PAROL NOTO'G'RI");
      digitalWrite(LED_QIZIL, HIGH); delay(1000); digitalWrite(LED_QIZIL, LOW);
    }
    kiritilgan = "";
  } else if (t == '*') {             // tozalash
    kiritilgan = "";
    Serial.println("tozalandi");
  } else {
    kiritilgan += t;
    Serial.print("*");               // parol ko'rinmasin
  }
}""",
    qollash=["Kodli qulf", "signalizatsiya paneli", "kalkulyator", "lift tugmalari"]),

"Rotatsion enkoder": P(
    tasnif=[
        "Cheksiz buraladigan tutqich (potensiometrdan farqi — cheti yo'q).",
        "Odatda bir aylanishda 20 qadam (detent). Har qadamda \"tiq\" etadi.",
        "Uchta signal pini: CLK (A), DT (B) va SW (bosish tugmasi).",
        "Ta'minot: 3,3-5 V.",
        "Kontakt sakrashi juda kuchli — filtrsiz bitta burashda 3-5 qadam sanaladi.",
    ],
    ishlash=[
        "Ichida ikkita kontakt bor, ular biroz SILJITIB joylashtirilgan.",
        "Burashda A va B signallari navbat bilan o'zgaradi. Qaysi biri OLDIN o'zgargani burash YO'NALISHINI ko'rsatadi.",
        "O'ngga burashda A oldin tushadi, chapga burashda B oldin tushadi.",
        "Shuning uchun ikkita pin kerak: bitta pin bilan faqat \"buraldi\" ni bilish mumkin, yo'nalishni emas.",
        "Bu usul kvadratura kodlash deb ataladi va motor enkoderlarida ham ishlatiladi.",
    ],
    oqish=[
        "CLK o'zgargan lahzada DT ni o'qish kerak: teng bo'lsa bir yo'nalish, teng bo'lmasa ikkinchisi.",
        "Ishonchli o'qish uchun uzilish (interrupt) ishlatiladi: attachInterrupt(digitalPinToInterrupt(2), ..., CHANGE).",
        "Soddaroq yo'l — Encoder yoki RotaryEncoder kutubxonasi.",
        "Bosish tugmasi (SW) INPUT_PULLUP bilan oddiy tugma kabi o'qiladi.",
    ],
    kod="""// Rotatsion enkoder — qiymatni oshirish/kamaytirish
const int CLK = 2, DT = 3, SW = 4;

volatile int qiymat = 0;
int oldingiCLK;

void burildi() {
  int hozirCLK = digitalRead(CLK);
  if (hozirCLK != oldingiCLK && hozirCLK == LOW) {
    // DT bilan solishtirib yo'nalishni aniqlaymiz
    if (digitalRead(DT) != hozirCLK) qiymat++;
    else                             qiymat--;
  }
  oldingiCLK = hozirCLK;
}

void setup() {
  pinMode(CLK, INPUT_PULLUP);
  pinMode(DT,  INPUT_PULLUP);
  pinMode(SW,  INPUT_PULLUP);
  oldingiCLK = digitalRead(CLK);
  attachInterrupt(digitalPinToInterrupt(CLK), burildi, CHANGE);
  Serial.begin(9600);
}

void loop() {
  static int korsatilgan = 0;
  if (qiymat != korsatilgan) {
    korsatilgan = qiymat;
    Serial.print("Qiymat: "); Serial.println(korsatilgan);
  }
  if (digitalRead(SW) == LOW) {
    qiymat = 0;
    Serial.println("Nolga qaytarildi");
    delay(300);
  }
}""",
    qollash=["Menyu boshqaruvi", "ovoz sozlagich", "3D printer paneli", "motor holatini o'lchash"]),

# ============================================================ HARAKAT
"Servo SG90": P(
    tasnif=[
        "Burilish burchagi: 0 dan 180 gradusgacha (360 gradus aylanadigan turi ham bor, lekin u burchakni emas, tezlikni boshqaradi).",
        "Ta'minot: 4,8-6 V. Tinch holatda 10 mA, harakatda 100-250 mA, tiqilib qolganda 700 mA gacha.",
        "Moment: 1,8 kg*sm (5 V da) — ya'ni 1 sm richagda 1,8 kg ko'tara oladi.",
        "Tezlik: 60 gradusni 0,1 sekundda buriladi.",
        "Og'irligi: 9 gramm. Shuning uchun \"9g servo\" deb ham ataladi.",
        "Simlari: jigarrang/qora = GND, qizil = quvvat, sariq/to'q sariq = signal.",
    ],
    ishlash=[
        "Ichida to'rt qism bor: DC motor, tishli reduktor, potensiometr va boshqaruv platasi.",
        "Potensiometr chiqish valiga ulangan — u SERVOGA O'ZI hozir qaysi burchakda turganini bildiradi.",
        "Boshqaruv platasi \"kerakli burchak\" bilan \"hozirgi burchak\" ni doim solishtiradi va farqni yo'qotish tomonga motorni aylantiradi. Bu — TESKARI BOG'LANISH (feedback).",
        "Kerakli burchak PWM impuls KENGLIGI bilan beriladi: har 20 ms da bitta impuls yuboriladi.",
        "1,0 ms impuls = 0 daraja; 1,5 ms = 90 daraja; 2,0 ms = 180 daraja.",
        "Servo ishga tushganda tok keskin ortadi va kuchlanish cho'kadi — shuning uchun plata qayta yuklanib ketishi mumkin. Yechim: alohida 5 V manba va quvvat liniyasiga 100-470 mkF kondensator.",
    ],
    oqish=[
        "Kutubxona: Servo (Arduino IDE bilan birga keladi). ESP32 uchun — ESP32Servo.",
        "Servo s; s.attach(9); s.write(burchak);",
        "s.write(90) — 90 gradusga buriladi. Servo o'sha yerda TURIB QOLADI (ushlab turadi).",
        "s.read() — oxirgi berilgan burchakni qaytaradi (haqiqiy holatni emas!).",
        "Silliq harakat uchun burchakni bittalab oshirib borish kerak: for (int b = 0; b <= 180; b++) { s.write(b); delay(15); }",
        "MUHIM: Servo kutubxonasi 9 va 10-pinlardagi analogWrite (PWM) ni ishdan chiqaradi.",
    ],
    kod="""// Servo — potensiometr bilan boshqarish va avtomatik shlagbaum
#include <Servo.h>
Servo servo;
const int POT = A0, TUGMA = 2;

void setup() {
  servo.attach(9);           // signal simi D9 ga
  pinMode(TUGMA, INPUT_PULLUP);
  Serial.begin(9600);
  servo.write(0);            // boshlang'ich holat: yopiq
  delay(500);
}

void loop() {
  // 1) tugma bosilsa — shlagbaum silliq ochilib, keyin yopiladi
  if (digitalRead(TUGMA) == LOW) {
    Serial.println("Shlagbaum ochilmoqda...");
    for (int b = 0; b <= 90; b++) { servo.write(b); delay(15); }
    delay(3000);
    Serial.println("Yopilmoqda...");
    for (int b = 90; b >= 0; b--) { servo.write(b); delay(15); }
    return;
  }

  // 2) tugma bosilmasa — potensiometr burchakni boshqaradi
  int burchak = map(analogRead(POT), 0, 1023, 0, 180);
  servo.write(burchak);
  Serial.print("burchak: "); Serial.println(burchak);
  delay(50);
}""",
    qollash=["Shlagbaum", "robot qo'li", "eshik qulfi", "kamera burgichi", "robot oyoqlari"]),

"DC motor (tranzistor orqali)": P(
    tasnif=[
        "Oddiy kollektorli motor. Kuchlanishi: 3-6 V (maktab to'plamlarida).",
        "Bo'sh yurishda 70-150 mA, yuk ostida 300-500 mA, tiqilib qolganda 1 A dan ortiq.",
        "Arduino pinidan maksimum 40 mA olish mumkin — ya'ni motorni PLATAGA TO'G'RIDAN-TO'G'RI ULASH MUMKIN EMAS.",
        "Boshqarish uchun kalit kerak: NPN tranzistor (BC547, 2N2222) yoki MOSFET (IRLZ44N).",
        "Himoya diodi: 1N4007 — motorga PARALLEL, teskari qutblab ulanadi.",
    ],
    ishlash=[
        "Motor ichida g'altak (rotor) va doimiy magnitlar bor. G'altakdan tok o'tganda u magnitga aylanadi va doimiy magnitlar bilan tortishib-itarishib aylanadi.",
        "Kollektor va cho'tkalar har yarim aylanishda tok yo'nalishini almashtiradi — shuning uchun aylanish to'xtamaydi.",
        "Tranzistor — elektron kalit: bazasiga kichik tok (1 mA) berilsa, kollektor orqali katta tok (500 mA) o'tkazadi.",
        "NEGA DIOD KERAK: motor g'altagi — g'altak (induktivlik). Tok to'satdan uzilganda g'altak o'zida yuqori teskari kuchlanish (o'z-o'zidan induksiya EYuK) hosil qiladi — bu 100 voltdan oshishi mumkin va tranzistorni teshib yuboradi.",
        "Diod bu teskari kuchlanish uchun yo'l ochib beradi va u xavfsiz so'nadi. Diodsiz sxema bir necha marta ishlab, keyin buziladi.",
    ],
    oqish=[
        "Yoqish/o'chirish: digitalWrite(baza_pini, HIGH/LOW).",
        "Tezlikni boshqarish: analogWrite(baza_pini, 0..255) — PWM.",
        "Motor 60-70 dan past PWM da odatda umuman aylanmaydi (ishga tushish momenti yetmaydi) — bu normal.",
        "Ishga tushirishning ishonchli usuli: avval qisqa vaqt 255 berib \"turtib\" yuborish, keyin kerakli tezlikka tushirish.",
        "Bu sxema motorni faqat BIR YO'NALISHDA aylantiradi. Yo'nalish kerak bo'lsa — H-ko'prik (L298N).",
    ],
    kod="""// DC motor tranzistor orqali — tezlikni boshqarish
const int MOTOR = 9;      // tranzistor bazasiga 1 kOm orqali
const int POT   = A0;

void setup() {
  pinMode(MOTOR, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int tezlik = map(analogRead(POT), 0, 1023, 0, 255);

  // motor past PWM da ishga tushmaydi — "turtki" beramiz
  static bool aylanyapti = false;
  if (!aylanyapti && tezlik > 20) {
    analogWrite(MOTOR, 255);
    delay(120);
    aylanyapti = true;
  }
  if (tezlik <= 20) aylanyapti = false;

  analogWrite(MOTOR, tezlik);

  Serial.print("PWM: "); Serial.print(tezlik);
  Serial.print("  ("); Serial.print(tezlik * 100 / 255); Serial.println(" %)");
  delay(100);
}""",
    qollash=["Ventilyator", "nasos", "g'ildirakli robot", "konveyer lentasi"]),

"L298N motor drayveri": P(
    tasnif=[
        "Ikkita DC motorni (yoki bitta qadamli motorni) mustaqil boshqaradi.",
        "Motor kuchlanishi: 5-35 V. Bir kanaldan doimiy 2 A, qisqa muddatga 3 A.",
        "Ichida 5 V stabilizator bor: motor manbai 7-12 V bo'lsa, jumper turgan holda drayver Arduino'ni ham quvvatlay oladi.",
        "12 V dan yuqori manbada jumperni OLIB TASHLASH shart, aks holda stabilizator kuyadi.",
        "Kamchiligi: har kanalda ~1,4 V yo'qoladi (issiqlikka aylanadi). 6 V bersangiz motorga 4,6 V yetadi.",
        "Radiator qizishi normal — 1 A dan yuqori tokda majburiy.",
    ],
    ishlash=[
        "Ichida H-KO'PRIK sxemasi bor: to'rtta elektron kalit \"H\" harfi shaklida joylashgan, motor esa o'rtadagi ko'ndalang chiziqda.",
        "Chap yuqori va o'ng past kalit ochilsa — tok bir tomonga oqadi, motor o'ngga aylanadi.",
        "O'ng yuqori va chap past kalit ochilsa — tok TESKARI oqadi, motor chapga aylanadi.",
        "Ikkala past kalit ochilsa — motor uchlari qisqa tutashadi va motor keskin TORMOZLANADI.",
        "Hamma kalitlar yopiq bo'lsa — motor bo'sh aylanib to'xtaydi (inersiya bilan).",
        "XAVFLI holat: bitta ustundagi yuqori va past kalit bir vaqtda ochilsa — qisqa tutashuv. L298N ichida bunga qarshi himoya bor.",
        "ENA/ENB pinlari PWM bilan tezlikni boshqaradi: ular butun ko'prikni tez-tez yoqib-o'chiradi.",
    ],
    oqish=[
        "Yo'nalish: IN1=HIGH, IN2=LOW -> oldinga. IN1=LOW, IN2=HIGH -> orqaga. Ikkalasi bir xil -> to'xtaydi.",
        "Tezlik: analogWrite(ENA, 0..255).",
        "UMUMIY GND — eng muhim shart. Arduino GND si va drayver GND si BIRLASHTIRILMASA boshqaruv signali ishlamaydi.",
        "Robot to'g'ri yurmasa — bu normal: ikki motor bir xil emas. Yechim: bir tomonga bir oz kamroq PWM berish (masalan chapga 200, o'ngga 190).",
    ],
    kod="""// L298N — ikki motorli robot: oldinga, orqaga, burilish
const int ENA = 10, IN1 = 8,  IN2 = 9;    // chap motor
const int ENB = 5,  IN3 = 7,  IN4 = 6;    // o'ng motor

void chap(int t) {                 // t: -255..255
  digitalWrite(IN1, t >= 0); digitalWrite(IN2, t < 0);
  analogWrite(ENA, abs(t));
}
void ong(int t) {
  digitalWrite(IN3, t >= 0); digitalWrite(IN4, t < 0);
  analogWrite(ENB, abs(t));
}
void toxta() { analogWrite(ENA, 0); analogWrite(ENB, 0); }

void setup() {
  int pinlar[6] = {ENA, IN1, IN2, ENB, IN3, IN4};
  for (int i = 0; i < 6; i++) pinMode(pinlar[i], OUTPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.println("oldinga");
  chap(200); ong(190); delay(2000);        // o'ng motor kuchliroq -> 190

  Serial.println("orqaga");
  chap(-200); ong(-190); delay(2000);

  Serial.println("joyida o'ngga burilish");
  chap(180); ong(-180); delay(700);        // g'ildiraklar qarama-qarshi

  Serial.println("to'xtash");
  toxta(); delay(1500);
}""",
    qollash=["G'ildirakli robot", "chiziq bo'ylab yuruvchi robot", "avtomatik darvoza", "konveyer"]),

"Qadamli motor 28BYJ-48 + ULN2003": P(
    tasnif=[
        "Kuchlanish: 5 V. Tok: 200-300 mA (Arduino 5V pinidan olish chegarada — tashqi manba yaxshiroq).",
        "Ichki reduktor nisbati: 1:64.",
        "To'liq qadam rejimida bir aylanish = 2048 qadam. Yarim qadam rejimida = 4096.",
        "Ya'ni bitta qadam = 360 / 2048 = 0,176 daraja — juda aniq.",
        "Aylanish tezligi: 15 ayl/min gacha. Sekin, lekin momenti katta.",
        "ULN2003 — drayver: 7 ta Darlington tranzistor to'plami, ichida himoya diodlari ham bor.",
    ],
    ishlash=[
        "Qadamli motorda kollektor va cho'tka YO'Q. Uning o'rniga statorda bir nechta g'altak bor.",
        "G'altaklar NAVBAT BILAN yoqiladi. Rotor har safar yoqilgan g'altakka tortiladi va aniq bir qadam siljiydi.",
        "Shuning uchun datchiksiz ham aniq burchakka burish mumkin: qadamlarni sanash yetarli.",
        "Bu — OCHIQ HALQALI boshqaruv. Kamchiligi: yuk juda og'ir bo'lsa motor qadamni \"o'tkazib yuboradi\" va dastur buni sezmaydi.",
        "Servodan farqi: servo 180 daraja ichida ishlaydi va o'z holatini biladi; qadamli motor esa cheksiz aylanadi va holatni faqat dastur sanaydi.",
    ],
    oqish=[
        "Kutubxona: Stepper (IDE bilan birga keladi).",
        "E'lon: Stepper motor(2048, 8, 10, 9, 11); — PIN TARTIBI 8, 10, 9, 11 (IN1, IN3, IN2, IN4).",
        "TARTIB BUZILSA motor aylanmaydi, faqat titraydi — bu eng ko'p uchraydigan xato.",
        "motor.setSpeed(10); — ayl/min (28BYJ-48 uchun 15 dan oshirmang).",
        "motor.step(2048) — bir to'liq aylanish. motor.step(-512) — teskari tomonga chorak aylanish.",
        "Kerakli burchakka burish: qadam = burchak * 2048 / 360.",
    ],
    kod="""// 28BYJ-48 — aniq burchakka burish
#include <Stepper.h>

const int QADAM = 2048;                 // bir to'liq aylanish
// DIQQAT: pin tartibi IN1, IN3, IN2, IN4
Stepper motor(QADAM, 8, 10, 9, 11);

void burchakka(float daraja) {
  long q = (long)(daraja * QADAM / 360.0);
  motor.step(q);
}

void setup() {
  motor.setSpeed(12);                   // ayl/min
  Serial.begin(9600);
}

void loop() {
  Serial.println("90 daraja o'ngga");
  burchakka(90);  delay(1000);

  Serial.println("45 daraja chapga");
  burchakka(-45); delay(1000);

  Serial.println("to'liq aylanish");
  motor.step(QADAM); delay(2000);
}""",
    qollash=["3D printer", "CNC dastgoh", "avtomatik parda", "aniq burilish mexanizmlari", "soat mexanizmi"]),

"Rele moduli": P(
    tasnif=[
        "Elektromagnit kalit: kuchsiz signal bilan kuchli yuklamani ulaydi.",
        "G'altak: 5 V, 70-90 mA (shuning uchun to'g'ridan-to'g'ri pindan quvvatlanmaydi — modulda tranzistor bor).",
        "Kontakt: 250 V AC / 10 A yoki 30 V DC / 10 A.",
        "Uchta kontakt: COM (umumiy), NO (normally open — odatda uzuq), NC (normally closed — odatda ulangan).",
        "Ko'p modullar TESKARI mantiqda: IN piniga LOW berilganda rele ulanadi.",
        "Modulda optopara bo'lsa — boshqaruv va kuchli tomon ELEKTR JIHATDAN AJRATILGAN bo'ladi, bu xavfsizroq.",
    ],
    ishlash=[
        "Ichida g'altak va temir yakor bor. G'altakdan tok o'tsa u elektromagnitga aylanadi va yakorni tortadi.",
        "Yakor kontaktni COM-NC holatidan COM-NO holatiga o'tkazadi. Tok uzilsa prujina uni qaytaradi.",
        "Eng muhim afzallik: 5 V li plata 220 V li zanjirni ulaydi, lekin ular bir-biriga ELEKTR JIHATDAN ULANMAGAN. Ular orasidagi yagona bog'liqlik — magnit maydon.",
        "Kontakt ulanish-uzilish paytida uchqun chiqadi — shuning uchun relening umri cheklangan (100 mingdan 10 milliongacha).",
        "\"Tiq\" tovushi — yakorning tortilishi. Bu rele ishlaganining eng oson belgisi.",
    ],
    oqish=[
        "digitalWrite(pin, LOW) — ko'p modullarda ULAYDI. digitalWrite(pin, HIGH) — uzadi.",
        "Modulingiz qaysi mantiqda ishlashini sinovda aniqlang: LED yonganda va \"tiq\" eshitilganda rele ulangan.",
        "XAVFSIZLIK: 220 V bilan ishlash faqat O'QITUVCHI NAZORATIDA va faqat NAMOYISH tarzida. O'quvchilar 220 V ga tegmaydi.",
        "Darsda 220 V o'rniga past kuchlanishli chiroq (12 V) yoki batareyali yuklama ishlatiladi — o'rganish uchun bu yetarli.",
        "Rele tez-tez ulanib-uzilmasligi uchun dasturda gisterezis yoki minimal kutish vaqti qo'yiladi.",
    ],
    kod="""// Rele — haroratga qarab isitgichni boshqarish (gisterezis bilan)
const int RELE = 7;               // ko'p modullarda LOW = ULANADI
const int SENSOR = A0;

const float YOQ  = 22.0;          // shu haroratdan past bo'lsa yoqamiz
const float OCHIR = 25.0;         // shu haroratdan yuqori bo'lsa o'chiramiz

bool ishlayapti = false;

void setup() {
  pinMode(RELE, OUTPUT);
  digitalWrite(RELE, HIGH);       // boshida O'CHIQ
  Serial.begin(9600);
}

void loop() {
  // soddalashtirilgan: analog qiymatni gradusga chizmalash
  float t = map(analogRead(SENSOR), 0, 1023, 0, 50);

  // GISTEREZIS: ikki chegara relening tez-tez "tiqillashini" yo'qotadi
  if (!ishlayapti && t < YOQ)   { ishlayapti = true;  }
  if ( ishlayapti && t > OCHIR) { ishlayapti = false; }

  digitalWrite(RELE, ishlayapti ? LOW : HIGH);

  Serial.print("Harorat: "); Serial.print(t, 1);
  Serial.print(" C   Isitgich: "); Serial.println(ishlayapti ? "YONIQ" : "O'CHIQ");
  delay(1000);
}""",
    qollash=["Aqlli rozetka", "isitgich avtomatikasi", "sug'orish nasosi", "ko'cha yoritgichi"]),

"Lazer moduli": P(
    tasnif=[
        "To'lqin uzunligi: 650 nm (qizil). Quvvati: 5 mW (1-sinf, past quvvatli).",
        "Ta'minot: 3-5 V. Tok: 30-40 mA.",
        "Nur diametri: ~1 mm, uzoq masofada ham deyarli tarqalmaydi.",
        "XAVFSIZLIK: nurga to'g'ridan-to'g'ri qaramaslik. Faqat pastga yoki devorga qaratib ishlatiladi.",
    ],
    ishlash=[
        "Oddiy LED nurni HAR TOMONGA sochadi. Lazerda esa nur ikkita ko'zgu orasida qayta-qayta aks etib kuchayadi.",
        "Natijada hosil bo'lgan nur KOGERENT: hamma to'lqinlar bir xil uzunlikda va bir xil qadamda harakatlanadi.",
        "Shuning uchun lazer nuri tarqalmaydi va uzoqqa aniq nuqta bo'lib boradi.",
        "Modulda kollimator linza bor — u nurni yanada ingichka qiladi.",
    ],
    oqish=[
        "Oddiy raqamli chiqish: digitalWrite(pin, HIGH) — yonadi.",
        "\"Lazer to'siq\": lazer bir tomonda, fotorezistor qarshisida. Nur to'silsa LDR qiymati keskin tushadi.",
        "Chegarani sinovda aniqlash kerak: nur tushib turganda va qo'l bilan to'silganda qiymatlarni yozib olish.",
    ],
    kod="""// Lazer + fotorezistor — "lazer to'siq" signalizatsiyasi
const int LAZER = 8, LDR = A0, ZUMMER = 12, LED = 9;
int nurBor;      // kalibrlashda o'lchanadi

void setup() {
  pinMode(LAZER, OUTPUT); pinMode(ZUMMER, OUTPUT); pinMode(LED, OUTPUT);
  Serial.begin(9600);

  digitalWrite(LAZER, HIGH);
  delay(500);
  nurBor = analogRead(LDR);          // nur to'silmagan holatdagi qiymat
  Serial.print("Etalon qiymat: "); Serial.println(nurBor);
}

void loop() {
  int q = analogRead(LDR);

  // nur to'silsa qiymat keskin tushadi
  if (q < nurBor - 150) {
    Serial.println("TO'SIQ! Kimdir o'tdi.");
    digitalWrite(LED, HIGH);
    tone(ZUMMER, 2000, 300);
    delay(500);
  } else {
    digitalWrite(LED, LOW);
  }
  delay(50);
}""",
    qollash=["Lazerli signalizatsiya", "buyum sanagich", "musobaqa finish chizig'i", "lazer arfa"]),

# ============================================================ ALOQA
"IR qabul qilgich VS1838": P(
    tasnif=[
        "Qabul chastotasi: 38 kHz (eng keng tarqalgan standart).",
        "To'lqin uzunligi: 940 nm — infraqizil, ko'zga ko'rinmaydi.",
        "Ta'minot: 2,7-5,5 V. Tok: 1,5 mA.",
        "Masofa: 10-15 metrgacha. Ko'rish burchagi: ±45 daraja.",
        "Pin tartibi (linza oldimizda): OUT - GND - VCC. Teskari ulansa qiziydi va buziladi.",
        "Ichida kuchaytirgich, filtr va demodulyator bor — chiqishda tayyor raqamli signal beradi.",
    ],
    ishlash=[
        "Pult IQ diodini shunchaki yoqmaydi — u sekundiga 38 000 marta miltillatib turadi (modulyatsiya).",
        "Nega shunday: quyosh va lampa ham IQ nur chiqaradi. Qabul qilgich ichidagi filtr faqat 38 kHz da tebranayotgan signalni o'tkazadi, doimiy fonni esa rad etadi.",
        "Ma'lumot esa shu 38 kHz \"tashuvchi\" ni uzun va qisqa bo'laklarga bo'lish orqali uzatiladi: uzun bo'lak = 1, qisqa = 0.",
        "Eng keng tarqalgan protokol — NEC: 32 bit (8 bit manzil + 8 bit teskari manzil + 8 bit buyruq + 8 bit teskari buyruq).",
        "Teskari nusxa xatoni tekshirish uchun: agar buyruq va uning teskarisi mos kelmasa, signal buzilgan.",
    ],
    oqish=[
        "Kutubxona: IRremote (versiya 3 va 4 da sintaksis farq qiladi — namunani IDE misolidan olish qulay).",
        "1-QADAM: har bir pultning kodlari BOSHQACHA. Avval kodlarni Serial monitorda chiqarib, daftarga yozib olish kerak.",
        "IrReceiver.decode() — signal kelganini bildiradi; IrReceiver.decodedIRData.command — buyruq kodi.",
        "IrReceiver.resume() — keyingi signalni kutishga qaytaradi. Chaqirilmasa dastur bitta buyruqda qotib qoladi.",
        "Tugma bosib turilganda \"takror\" (repeat) kodi keladi — u odatda 0 bo'ladi va uni alohida hisobga olish kerak.",
    ],
    kod="""// IR pult — avval kodlarni yozib oling, keyin ishlating
#include <IRremote.hpp>
const int IR_PIN = 2, LED = 9, ZUMMER = 8;

// O'Z pultingiz kodlarini shu yerga yozing (1-qadamda aniqlanadi)
const uint8_t TUGMA_1 = 0x45;
const uint8_t TUGMA_2 = 0x46;

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IR_PIN, ENABLE_LED_FEEDBACK);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.println("Pult tugmalarini bosing — kodlar chiqadi:");
}

void loop() {
  if (IrReceiver.decode()) {
    uint8_t kod = IrReceiver.decodedIRData.command;

    Serial.print("Kod: 0x"); Serial.println(kod, HEX);   // 1-QADAM: yozib oling

    if (kod == TUGMA_1) { digitalWrite(LED, HIGH); Serial.println(" -> LED yoqildi"); }
    if (kod == TUGMA_2) { digitalWrite(LED, LOW);  Serial.println(" -> LED o'chirildi"); }

    tone(ZUMMER, 1500, 40);
    IrReceiver.resume();      // MAJBURIY: keyingi signalga tayyorlanish
  }
}""",
    qollash=["Televizor pulti", "robot boshqaruvi", "masofadan yoqish", "konditsioner boshqaruvi"]),

"Bluetooth HC-05 / JDY-31": P(
    tasnif=[
        "Bluetooth 2.0 SPP (Serial Port Profile) — simsiz COM port kabi ishlaydi.",
        "Masofa: 10 metrgacha (ochiq joyda).",
        "Ta'minot: 3,6-6 V. Tok: ulanish paytida 30-40 mA, ulangandan keyin 8 mA.",
        "Mantiq darajasi: 3,3 V. Modulning RX pini 5 V ga BEVOSITA ulanmaydi — kuchlanish bo'luvchi kerak.",
        "Standart tezlik: 9600 boud. Standart parol: 1234 yoki 0000.",
        "HC-05 master ham, slave ham bo'la oladi; HC-06 faqat slave.",
        "BLE emas — iPhone bilan ishlamaydi. iPhone kerak bo'lsa BLE moduli (HM-10) yoki ESP32 ishlatiladi.",
    ],
    ishlash=[
        "Modul ma'lumotni radio to'lqin orqali uzatadi, lekin plata uchun bu oddiy SERIAL aloqadan farq qilmaydi.",
        "Ya'ni plata Serial.print bilan yozadi — modul uni radio orqali telefonga uzatadi. Bu abstraksiya deyiladi: murakkab ish yashiringan.",
        "TX va RX doim KESIB ulanadi: modulning TX (yuborish) pini platanining RX (qabul qilish) piniga.",
        "Ikkita qurilma bir xil tezlikda (boud) gaplashishi shart, aks holda ma'nosiz belgilar keladi.",
        "AT rejimi: modul EN pini HIGH holatda yoqilsa, sozlash buyruqlarini qabul qiladi (nom, parol, tezlikni o'zgartirish).",
    ],
    oqish=[
        "SoftwareSerial bilan: SoftwareSerial bt(10, 11); — 10 = RX, 11 = TX.",
        "bt.available() — kelgan belgi bor-yo'qligini bildiradi.",
        "bt.read() — bitta belgi o'qiydi. bt.readStringUntil('\\n') — butun qatorni o'qiydi.",
        "bt.println(\"matn\") — telefonga yuboradi.",
        "Telefonda \"Serial Bluetooth Terminal\" ilovasi ishlatiladi: avval sozlamalarda juftlash, keyin ilovada ulanish.",
        "Dastur yuklashda modulni UZIB QO'YISH kerak (0 va 1-pinlarga ulangan bo'lsa) — aks holda yuklash muvaffaqiyatsiz tugaydi.",
    ],
    kod="""// Bluetooth — telefondan buyruq qabul qilish
#include <SoftwareSerial.h>
SoftwareSerial bt(10, 11);      // RX, TX  (modul TX -> D10, modul RX -> D11)

const int LED = 9, ZUMMER = 8;

void setup() {
  bt.begin(9600);
  Serial.begin(9600);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  bt.println("Qurilma tayyor. Buyruqlar: YOQ / OCHIR / SIGNAL");
}

void loop() {
  if (bt.available()) {
    String buyruq = bt.readStringUntil('\\n');
    buyruq.trim();                       // ortiqcha bo'sh joy va \\r ni olib tashlash
    buyruq.toUpperCase();

    Serial.print("Kelgan buyruq: "); Serial.println(buyruq);

    if (buyruq == "YOQ") {
      digitalWrite(LED, HIGH);  bt.println("LED yoqildi");
    } else if (buyruq == "OCHIR") {
      digitalWrite(LED, LOW);   bt.println("LED o'chirildi");
    } else if (buyruq == "SIGNAL") {
      tone(ZUMMER, 2000, 300);  bt.println("Signal berildi");
    } else {
      bt.println("Noma'lum buyruq: " + buyruq);
    }
  }
}""",
    qollash=["Telefondan robot boshqarish", "simsiz ma'lumot yig'ish", "aqlli uy pulti"]),

"RFID RC522": P(
    tasnif=[
        "Chastota: 13,56 MHz (MIFARE standarti).",
        "O'qish masofasi: 2-5 sm. Ko'proq masofa uchun boshqa (qimmatroq) modullar kerak.",
        "Ta'minot: 3,3 V — 5 V BERILSA MODUL KUYADI. Bu eng ko'p uchraydigan va tuzatib bo'lmaydigan xato.",
        "Interfeys: SPI (SDA/SS, SCK, MOSI, MISO, RST).",
        "Kartadagi UID: 4 yoki 7 bayt — har bir kartada noyob.",
        "Karta xotirasi: MIFARE Classic 1K — 1024 bayt, 16 sektor.",
    ],
    ishlash=[
        "Kartada BATAREYA YO'Q. Unda faqat mayda mikrosxema va o'ram (antenna) bor.",
        "O'qigich doimiy ravishda 13,56 MHz elektromagnit maydon chiqarib turadi.",
        "Karta shu maydonga kirganda uning o'ramida tok INDUKSIYALANADI — mana shu tok mikrosxemani quvvatlaydi. Bu transformator prinsipi bilan bir xil.",
        "Quvvat olgan mikrosxema o'z raqamini (UID) javob qilib yuboradi.",
        "Shuning uchun karta cheksiz uzoq ishlaydi va zaryadlash kerak emas.",
        "Xuddi shu texnologiya bank kartalarining kontaktsiz to'lovida, pasport va transport kartalarida ishlatiladi.",
    ],
    oqish=[
        "Kutubxona: MFRC522. Kerak: #include <SPI.h> va #include <MFRC522.h>.",
        "rfid.PICC_IsNewCardPresent() — yangi karta qo'yildimi.",
        "rfid.PICC_ReadCardSerial() — UID ni o'qiydi.",
        "UID rfid.uid.uidByte[] massivida, uzunligi rfid.uid.size da.",
        "Ruxsat berilgan kartalar ro'yxati kodda saqlanadi va kelgan UID shu ro'yxat bilan solishtiriladi.",
        "rfid.PICC_HaltA() — kartani \"uxlatadi\", aks holda bitta karta qayta-qayta o'qiladi.",
        "XAVFSIZLIK ESLATMASI: MIFARE Classic ning himoyasi buzilgan — jiddiy tizimlarda ishlatilmaydi. Bu darsda faqat prinsipni o'rganish uchun.",
    ],
    kod="""// RFID RC522 — kartani o'qib, ruxsatni tekshirish
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
MFRC522 rfid(SS_PIN, RST_PIN);

const int LED_YASHIL = 6, LED_QIZIL = 7, ZUMMER = 8;

// Ruxsat berilgan kartalar (1-qadamda o'z kartangiz UID sini yozib oling)
byte ruxsat[][4] = {
  {0xDE, 0xAD, 0xBE, 0xEF},
  {0x12, 0x34, 0x56, 0x78}
};
const int RUXSAT_SONI = 2;

bool tekshir(byte *uid) {
  for (int i = 0; i < RUXSAT_SONI; i++) {
    bool mos = true;
    for (int j = 0; j < 4; j++) if (uid[j] != ruxsat[i][j]) mos = false;
    if (mos) return true;
  }
  return false;
}

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  pinMode(LED_YASHIL, OUTPUT); pinMode(LED_QIZIL, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.println("Kartani yaqinlashtiring...");
}

void loop() {
  if (!rfid.PICC_IsNewCardPresent()) return;
  if (!rfid.PICC_ReadCardSerial())  return;

  Serial.print("UID: ");
  for (byte i = 0; i < rfid.uid.size; i++) {
    Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(rfid.uid.uidByte[i], HEX);
  }
  Serial.println();

  if (tekshir(rfid.uid.uidByte)) {
    Serial.println("  -> RUXSAT BERILDI");
    digitalWrite(LED_YASHIL, HIGH); tone(ZUMMER, 2000, 150);
    delay(1500); digitalWrite(LED_YASHIL, LOW);
  } else {
    Serial.println("  -> RUXSAT YO'Q");
    digitalWrite(LED_QIZIL, HIGH);  tone(ZUMMER, 400, 600);
    delay(1500); digitalWrite(LED_QIZIL, LOW);
  }

  rfid.PICC_HaltA();       // kartani uxlatish — qayta-qayta o'qilmasin
}""",
    qollash=["Kirish nazorati", "davomat tizimi", "kutubxona kitob hisobi", "kontaktsiz to'lov"]),

"microSD kart moduli": P(
    tasnif=[
        "Interfeys: SPI (CS, SCK, MOSI, MISO).",
        "Kart formati: FAT16 yoki FAT32 SHART. exFAT va NTFS ishlamaydi.",
        "Sig'imi: 32 GB gacha ishonchli ishlaydi.",
        "Ta'minot: modulda 3,3 V stabilizator va daraja o'zgartirgich bo'lsa 5 V dan quvvatlanadi.",
        "Fayl nomi: 8.3 formatida (masalan DATA.CSV) — uzun nomlar ishlamaydi.",
        "Yozish tezligi: Arduino uchun sekundiga bir necha yuz qator — ma'lumot yig'ish uchun yetarli.",
    ],
    ishlash=[
        "Ichida flesh xotira mikrosxemasi va kontroller bor. Kontroller SPI buyruqlarini xotira blokiga aylantiradi.",
        "Kutubxona esa bloklar ustiga FAYL TIZIMINI quradi — shuning uchun kompyuter ham bu faylni o'qiy oladi.",
        "Ma'lumot avval bufferga to'planadi va faqat file.close() (yoki flush) da haqiqatan diskka yoziladi.",
        "Shuning uchun close() qilinmasa yoki quvvat to'satdan o'chsa — oxirgi yozuvlar YO'QOLADI.",
    ],
    oqish=[
        "SD.begin(CS_pin) — modulni ishga tushiradi, false qaytarsa ulanish yoki format xato.",
        "File f = SD.open(\"DATA.CSV\", FILE_WRITE); — yozish uchun ochadi (fayl oxiriga qo'shadi).",
        "f.println(qator); — bitta qator yozadi.",
        "f.close(); — MAJBURIY. Usiz ma'lumot saqlanmaydi.",
        "CSV formati qulay: qiymatlar vergul bilan ajratiladi va Excel bu faylni to'g'ridan-to'g'ri ochadi.",
        "O'qish: SD.open(\"DATA.CSV\") va while (f.available()) f.read().",
    ],
    kod="""// microSD — o'lchovlarni CSV faylga yozish (Excel'da ochiladi)
#include <SPI.h>
#include <SD.h>

const int CS = 4, SENSOR = A0;
unsigned long boshlangan;

void setup() {
  Serial.begin(9600);

  if (!SD.begin(CS)) {
    Serial.println("XATO: kart topilmadi. Format FAT32 ekanini va simlarni tekshiring.");
    while (true);
  }
  Serial.println("Kart tayyor.");

  // sarlavha qatorini bir marta yozamiz
  File f = SD.open("DATA.CSV", FILE_WRITE);
  if (f) { f.println("vaqt_s,qiymat,kuchlanish_V"); f.close(); }

  boshlangan = millis();
}

void loop() {
  int q = analogRead(SENSOR);
  float u = q * 5.0 / 1023.0;
  unsigned long t = (millis() - boshlangan) / 1000;

  File f = SD.open("DATA.CSV", FILE_WRITE);
  if (f) {
    f.print(t); f.print(",");
    f.print(q); f.print(",");
    f.println(u, 3);
    f.close();                       // MAJBURIY — usiz saqlanmaydi
    Serial.print("Yozildi: "); Serial.print(t); Serial.print("s  "); Serial.println(q);
  } else {
    Serial.println("Faylni ochib bo'lmadi");
  }

  delay(5000);                       // 5 sekundda bir yozamiz
}""",
    qollash=["Ma'lumot yig'ish (data logging)", "meteostansiya arxivi", "sozlamalarni saqlash", "ovoz fayllari"]),

"RTC DS3231 (real vaqt soati)": P(
    tasnif=[
        "Aniqligi: yiliga ±2 daqiqa (ichida termokompensatsiyali kvars bor).",
        "DS1307 dan afzalligi: DS1307 yiliga 30 daqiqagacha adashadi, DS3231 esa harorat o'zgarsa ham aniq yuradi.",
        "Batareya: CR2032. Asosiy quvvat o'chsa ham 5-10 yil vaqtni saqlaydi.",
        "Interfeys: I2C, manzil 0x68.",
        "Ta'minot: 2,3-5,5 V. Tok: 200 mkA (batareyada esa 3 mkA).",
        "Qo'shimcha: ichida harorat sensori (±3 °C) va budilnik funksiyasi bor.",
    ],
    ishlash=[
        "Ichida kvars kristalli 32 768 Hz chastotada tebranadi. Bu son bejiz emas: 32768 = 2 ning 15-darajasi.",
        "Shuning uchun tebranishlarni 15 marta ikkiga bo'lish orqali aniq 1 Hz — ya'ni SEKUND olinadi.",
        "Kvars harorat o'zgarganda chastotasini biroz o'zgartiradi. DS3231 haroratni o'lchab, xatoni AVTOMATIK to'g'irlaydi — aniqligining siri shunda.",
        "Batareya faqat vaqtni yurgizib turadi, boshqa hech narsani quvvatlamaydi — shuning uchun juda uzoq yetadi.",
        "Nima uchun millis() yetarli emas: millis() plata yoqilganidan beri o'tgan vaqtni sanaydi va quvvat o'chsa NOLDAN boshlanadi. RTC esa haqiqiy sana va vaqtni biladi.",
    ],
    oqish=[
        "Kutubxona: RTClib (Adafruit).",
        "rtc.begin() — ishga tushirish.",
        "VAQTNI O'RNATISH: rtc.adjust(DateTime(F(__DATE__), F(__TIME__))) — kompyuter vaqtini oladi.",
        "MUHIM: bu qatorni BIR MARTA yuklab, keyin IZOHGA OLISH kerak. Aks holda har qayta yuklashda vaqt kompilyatsiya vaqtiga qaytadi.",
        "O'qish: DateTime hozir = rtc.now();",
        "Qismlari: hozir.year(), .month(), .day(), .hour(), .minute(), .second(), .dayOfTheWeek().",
        "Harorat: rtc.getTemperature().",
    ],
    kod="""// DS3231 — vaqt bo'yicha avtomatik yoritish
#include <Wire.h>
#include <RTClib.h>
RTC_DS3231 rtc;
const int CHIROQ = 7;

void setup() {
  Serial.begin(9600);
  pinMode(CHIROQ, OUTPUT);

  if (!rtc.begin()) {
    Serial.println("RTC topilmadi! SDA/SCL ni tekshiring.");
    while (true);
  }

  // FAQAT BIR MARTA ishga tushiring, keyin bu qatorni izohga oling:
  // rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));

  if (rtc.lostPower()) {
    Serial.println("Quvvat uzilgan — vaqtni qayta o'rnating.");
  }
}

void loop() {
  DateTime hozir = rtc.now();

  Serial.print(hozir.day());    Serial.print(".");
  Serial.print(hozir.month());  Serial.print(".");
  Serial.print(hozir.year());   Serial.print("  ");
  if (hozir.hour()   < 10) Serial.print("0");  Serial.print(hozir.hour());   Serial.print(":");
  if (hozir.minute() < 10) Serial.print("0");  Serial.print(hozir.minute()); Serial.print(":");
  if (hozir.second() < 10) Serial.print("0");  Serial.print(hozir.second());
  Serial.print("   Harorat: "); Serial.print(rtc.getTemperature(), 1); Serial.println(" C");

  // 18:00 dan 23:00 gacha chiroq yonadi
  bool kech = (hozir.hour() >= 18 && hozir.hour() < 23);
  digitalWrite(CHIROQ, kech);

  delay(1000);
}""",
    qollash=["Soat va budilnik", "vaqt bo'yicha sug'orish", "ma'lumotga vaqt belgisi qo'yish", "davomat tizimi"]),

# ============================================================ ILG'OR / AI
"MPU6050 (akselerometr va giroskop)": P(
    tasnif=[
        "6 o'qli: 3 o'q akselerometr (tezlanish) + 3 o'q giroskop (burilish tezligi).",
        "Akselerometr oralig'i: ±2g, ±4g, ±8g, ±16g (sozlanadi). 1g = 9,8 m/s2.",
        "Giroskop oralig'i: ±250, ±500, ±1000, ±2000 daraja/sekund.",
        "Interfeys: I2C, manzil 0x68 (AD0 pini GND da) yoki 0x69 (AD0 pini VCC da).",
        "Ta'minot: modulda stabilizator bor, 3,3-5 V. Tok: 4 mA.",
        "Ichida harorat sensori ham bor (asosan ichki kompensatsiya uchun).",
        "Namuna olish tezligi: 1000 Hz gacha. AI uchun odatda 50-100 Hz olinadi.",
    ],
    ishlash=[
        "MEMS texnologiyasi: kremniy plastinkasiga mikroskopik mexanik tuzilmalar o'yib chiqilgan.",
        "Akselerometrda kichkina osilgan massa bor. Qurilma tezlanganda massa inersiya bilan biroz siljiydi va sig'im o'zgaradi — shu o'zgarish o'lchanadi.",
        "MUHIM: qimirlamay yotgan sensor ham Z o'qida 1g ko'rsatadi — chunki YER TORTISHI ham tezlanish. Aynan shu tufayli QIYALIKNI o'lchash mumkin.",
        "Giroskopda tebranib turadigan mikroskopik tuzilma bor. Qurilma burilganda Koriolis kuchi uni yon tomonga siljitadi — bu siljish burilish tezligini beradi.",
        "Akselerometr — sekin, lekin uzoq muddatda to'g'ri. Giroskop — tez, lekin vaqt o'tishi bilan \"suzib ketadi\" (drift).",
        "Shuning uchun ikkalasi BIRLASHTIRILADI (komplementar yoki Kalman filtri): giroskopdan tezkorlik, akselerometrdan barqarorlik olinadi.",
    ],
    oqish=[
        "Kutubxona: Adafruit MPU6050 + Adafruit Unified Sensor.",
        "sensors_event_t a, g, temp; mpu.getEvent(&a, &g, &temp);",
        "Tezlanish: a.acceleration.x / .y / .z — m/s2 da.",
        "Burilish tezligi: g.gyro.x / .y / .z — rad/s da.",
        "Qiyalik burchagi (faqat akselerometrdan): burchak = atan2(a.acceleration.y, a.acceleration.z) * 180 / PI.",
        "AI UCHUN MUHIM: ma'lumot yig'ishda namuna olish tezligi (masalan 100 Hz) BUTUN yig'ish davomida bir xil bo'lishi shart. O'zgarib qolsa model noto'g'ri o'rganadi.",
        "Ma'lumot yig'ish formati: har qator — vaqt, ax, ay, az, gx, gy, gz. Bu Edge Impulse ga to'g'ridan-to'g'ri yuklanadi.",
    ],
    kod="""// MPU6050 — qiyalik burchagi va imo-ishora uchun ma'lumot yig'ish
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
const unsigned long ORALIQ = 10;      // 10 ms = 100 Hz
unsigned long oxirgi = 0;

void setup() {
  Serial.begin(115200);
  if (!mpu.begin()) {
    Serial.println("MPU6050 topilmadi! SDA/SCL va AD0 ni tekshiring.");
    while (true);
  }
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  Serial.println("vaqt,ax,ay,az,gx,gy,gz");   // CSV sarlavhasi
}

void loop() {
  // AI uchun: namuna olish tezligi QAT'IY bir xil bo'lishi kerak
  if (millis() - oxirgi < ORALIQ) return;
  oxirgi = millis();

  sensors_event_t a, g, t;
  mpu.getEvent(&a, &g, &t);

  // CSV qatori — Edge Impulse ga yuklash uchun
  Serial.print(millis());               Serial.print(",");
  Serial.print(a.acceleration.x, 3);    Serial.print(",");
  Serial.print(a.acceleration.y, 3);    Serial.print(",");
  Serial.print(a.acceleration.z, 3);    Serial.print(",");
  Serial.print(g.gyro.x, 3);            Serial.print(",");
  Serial.print(g.gyro.y, 3);            Serial.print(",");
  Serial.println(g.gyro.z, 3);

  // qiyalik burchagi (faqat akselerometrdan)
  // float burchak = atan2(a.acceleration.y, a.acceleration.z) * 180.0 / PI;
}""",
    qollash=["Imo-ishorani tanish (AI)", "qadam sanagich", "kvadrokopter", "o'yin pulti", "yiqilishni aniqlash"]),

"BMP280 (bosim va balandlik)": P(
    tasnif=[
        "Bosim oralig'i: 300-1100 hPa (gektopaskal). Aniqlik: ±1 hPa.",
        "Balandlik hisoblash aniqligi: ±1 metr.",
        "Harorat: -40 dan +85 °C, aniqlik ±1 °C.",
        "Interfeys: I2C (manzil 0x76 yoki 0x77) yoki SPI.",
        "Ta'minot: 1,8-3,6 V (modulda stabilizator bo'lsa 5 V ham mumkin). Tok: 2,7 mkA.",
        "BME280 dan farqi: BME280 da NAMLIK ham bor, BMP280 da yo'q.",
    ],
    ishlash=[
        "Ichida juda yupqa kremniy membrana bor, uning bir tomonida vakuum.",
        "Tashqi bosim membranani egadi. Egilish miqdori piezorezistiv element qarshiligini o'zgartiradi.",
        "Balandlik qanday hisoblanadi: yuqoriga ko'tarilgan sari ustimizdagi havo qatlami yupqalashadi va bosim TUSHADI.",
        "Har 8 metr ko'tarilishda bosim taxminan 1 hPa kamayadi.",
        "MUHIM: ob-havo o'zgarganda bosim ham o'zgaradi. Shuning uchun aniq balandlik uchun o'sha kundagi dengiz sathi bosimini kiritish kerak.",
        "Sensor shu qadar sezgirki, uni stol ustidan polga tushirsangiz ham farqni ko'rsatadi.",
    ],
    oqish=[
        "Kutubxona: Adafruit BMP280.",
        "bmp.begin(0x76) — manzil 0x77 bo'lishi ham mumkin.",
        "bmp.readPressure() — paskalda (Pa). hPa ga o'tish uchun 100 ga bo'linadi.",
        "bmp.readTemperature() — Selsiyda.",
        "bmp.readAltitude(1013.25) — metrda. Qavs ichidagi son — dengiz sathi bosimi.",
        "Nisbiy balandlikni aniq o'lchash: boshlang'ich nuqtadagi bosimni saqlab, keyin farqni hisoblash.",
    ],
    kod="""// BMP280 — bosim, harorat va NISBIY balandlik
#include <Wire.h>
#include <Adafruit_BMP280.h>
Adafruit_BMP280 bmp;

float boshlangichBosim;

void setup() {
  Serial.begin(9600);
  if (!bmp.begin(0x76)) {                 // ishlamasa 0x77 ni sinang
    Serial.println("BMP280 topilmadi!");
    while (true);
  }
  delay(500);
  boshlangichBosim = bmp.readPressure() / 100.0;   // hPa
  Serial.print("Boshlang'ich bosim: "); Serial.print(boshlangichBosim); Serial.println(" hPa");
}

void loop() {
  float bosim  = bmp.readPressure() / 100.0;
  float t      = bmp.readTemperature();

  // nisbiy balandlik: boshlang'ich nuqtadan necha metr yuqori
  float balandlik = 44330.0 * (1.0 - pow(bosim / boshlangichBosim, 0.1903));

  Serial.print("Bosim: ");    Serial.print(bosim, 2);     Serial.print(" hPa   ");
  Serial.print("Harorat: ");  Serial.print(t, 1);         Serial.print(" C   ");
  Serial.print("Balandlik: ");Serial.print(balandlik, 1); Serial.println(" m");

  delay(1000);
}""",
    qollash=["Meteostansiya", "balandlik o'lchagich", "kvadrokopter", "ob-havo bashorati"]),

"INA219 (tok va quvvat o'lchagich)": P(
    tasnif=[
        "O'lchaydi: kuchlanish (0-26 V), tok (±3,2 A) va quvvat.",
        "Aniqlik: tokda 0,8 mA qadam, kuchlanishda 4 mV qadam.",
        "Ichida 0,1 Om shunt rezistor bor.",
        "Interfeys: I2C, manzil 0x40 (jumperlar bilan 0x41, 0x44, 0x45 qilish mumkin — 4 ta modulni birga ulash uchun).",
        "Ta'minot: 3-5,5 V. Tok: 1 mA.",
    ],
    ishlash=[
        "Tokni to'g'ridan-to'g'ri o'lchab bo'lmaydi. Buning o'rniga zanjirga juda kichik (0,1 Om) rezistor ketma-ket qo'yiladi.",
        "Om qonuni bo'yicha shu rezistorda kuchlanish tushishi hosil bo'ladi: U = I x R.",
        "1 A tok o'tsa: U = 1 x 0,1 = 0,1 V. Modul shu 0,1 V ni o'lchab, tokni HISOBLAB chiqaradi.",
        "Rezistor shuning uchun kichik: zanjirga xalaqit bermasligi va o'zi ko'p issiqlik chiqarmasligi kerak.",
        "Quvvat esa oddiy ko'paytirish: P = U x I. Modul buni o'zi hisoblab beradi.",
        "Modul zanjirga KETMA-KET ulanadi — xuddi multimetrni tok o'lchash rejimida ulagandek.",
    ],
    oqish=[
        "Kutubxona: Adafruit INA219.",
        "ina.getBusVoltage_V() — yuklamadagi kuchlanish (V).",
        "ina.getCurrent_mA() — tok (mA).",
        "ina.getPower_mW() — quvvat (mW).",
        "ina.getShuntVoltage_mV() — shunt rezistordagi tushish (mV).",
        "Batareya necha soat yetishini hisoblash: soat = batareya_sigimi_mAh / o'rtacha_tok_mA.",
        "Manfiy qiymat chiqsa — VIN+ va VIN- almashtirilgan.",
    ],
    kod="""// INA219 — qurilma qancha tok va quvvat sarflayotganini o'lchash
#include <Wire.h>
#include <Adafruit_INA219.h>
Adafruit_INA219 ina;

float jamiEnergiya_mWh = 0;
unsigned long oxirgi = 0;

void setup() {
  Serial.begin(9600);
  if (!ina.begin()) { Serial.println("INA219 topilmadi!"); while (true); }
  Serial.println("kuchlanish(V)  tok(mA)  quvvat(mW)");
  oxirgi = millis();
}

void loop() {
  float u = ina.getBusVoltage_V();
  float i = ina.getCurrent_mA();
  float p = ina.getPower_mW();

  // sarflangan energiyani to'plab boramiz
  unsigned long hozir = millis();
  jamiEnergiya_mWh += p * (hozir - oxirgi) / 3600000.0;
  oxirgi = hozir;

  Serial.print(u, 3); Serial.print(" V   ");
  Serial.print(i, 1); Serial.print(" mA   ");
  Serial.print(p, 1); Serial.print(" mW   ");
  Serial.print("jami: "); Serial.print(jamiEnergiya_mWh, 3); Serial.println(" mWh");

  // 2000 mAh batareya bilan necha soat ishlaydi
  if (i > 1) {
    Serial.print("  -> 2000 mAh batareya ~");
    Serial.print(2000.0 / i, 1);
    Serial.println(" soat yetadi");
  }
  delay(1000);
}""",
    qollash=["Quvvat tejashni o'lchash", "batareya umrini bashorat qilish", "quyosh paneli monitoringi", "nosozlik topish"]),

"HX711 + tenzodatchik (og'irlik)": P(
    tasnif=[
        "HX711 — 24 bitli ADC, aynan tenzodatchik uchun mo'ljallangan.",
        "Tenzodatchik turlari: 1 kg, 5 kg, 20 kg, 50 kg.",
        "Aniqlik: yaxshi kalibrlangan holda 1 grammgacha.",
        "Ta'minot: 2,7-5,5 V. Tok: 1,5 mA.",
        "O'qish tezligi: 10 Hz yoki 80 Hz (moduldagi kontakt bilan tanlanadi).",
        "Simlar rangi: qizil = E+, qora = E-, yashil = A+, oq = A- (ba'zi datchiklarda oq va yashil almashgan).",
    ],
    ishlash=[
        "Tenzodatchik ichida metall balka bor va unga juda yupqa zigzag simli plyonka (tenzorezistor) yopishtirilgan.",
        "Yuk qo'yilganda balka MIKRON darajasida egiladi. Sim biroz cho'ziladi — cho'zilgan sim INGICHKALASHADI va uzunlashadi, ya'ni qarshiligi ORTADI.",
        "Qarshilik o'zgarishi juda kichik: 0,1 % dan ham kam. Shuning uchun to'rtta tenzorezistor Uitston ko'prigi sxemasida ulanadi.",
        "Ko'prik chiqishida millivoltning mingdan bir ulushi darajasidagi signal hosil bo'ladi — oddiy ADC buni umuman ko'rmaydi.",
        "HX711 aynan shu uchun kerak: u signalni 128 marta kuchaytiradi va 24 bit aniqlikda o'qiydi (Arduino ADC si esa atigi 10 bit).",
        "Balka QATTIQ asosga mahkamlanishi shart — bo'shashgan bo'lsa ko'rsatkich suzib turadi.",
    ],
    oqish=[
        "Kutubxona: HX711 (bogde yoki Rob Tillaart versiyasi).",
        "scale.tare() — hozirgi og'irlikni NOL deb belgilaydi (idish og'irligini hisobdan chiqarish).",
        "scale.get_units(10) — 10 ta o'lchov o'rtachasini qaytaradi (shovqin kamayadi).",
        "KALIBRLASH — eng muhim qadam: 1) tare() qiling; 2) ANIQ ma'lum og'irlikni qo'ying (masalan 500 g); 3) xom qiymatni 500 ga bo'ling; 4) chiqqan sonni set_scale() ga bering.",
        "Har bir tenzodatchikning koeffitsienti BOSHQACHA — internetdan olib bo'lmaydi, o'zingiz topasiz.",
        "Harorat o'zgarsa ko'rsatkich biroz suzadi — aniq o'lchovdan oldin 10-15 daqiqa yoqib qo'yish kerak.",
    ],
    kod="""// HX711 — elektron tarozi (kalibrlash bilan)
#include "HX711.h"

const int DT = 3, SCK = 2;
HX711 tarozi;

// KALIBRLASH KOEFFITSIENTI — o'z datchigingiz uchun topiladi
float koef = 420.0;

void setup() {
  Serial.begin(9600);
  tarozi.begin(DT, SCK);

  Serial.println("Tarozini BO'SH qoldiring...");
  delay(2000);
  tarozi.set_scale();
  tarozi.tare();                    // nolni belgilaymiz
  tarozi.set_scale(koef);
  Serial.println("Tayyor. Yukni qo'ying.");
  Serial.println("Kalibrlash uchun: 'k' bosing va ma'lum og'irlikni qo'ying.");
}

void loop() {
  if (Serial.available() && Serial.read() == 'k') {
    Serial.println("500 g qo'ying va 5 sekund kuting...");
    tarozi.set_scale();
    delay(5000);
    float xom = tarozi.get_units(20);
    koef = xom / 500.0;                       // 500 g uchun
    tarozi.set_scale(koef);
    Serial.print("Yangi koeffitsient: "); Serial.println(koef, 2);
  }

  float ogirlik = tarozi.get_units(10);       // 10 o'lchov o'rtachasi
  Serial.print("Og'irlik: "); Serial.print(ogirlik, 1); Serial.println(" g");
  delay(500);
}""",
    qollash=["Elektron tarozi", "yuk nazorati", "to'lgan qutini aniqlash", "oziq-ovqat porsiyasi"]),

"TCS3200 (rang datchigi)": P(
    tasnif=[
        "8x8 = 64 ta fotodiod matritsasi: 16 tasi qizil filtrli, 16 tasi yashil, 16 tasi ko'k, 16 tasi filtrsiz.",
        "Chiqish: CHASTOTA (kuchlanish emas!). Rang qancha yorqin bo'lsa, chastota shuncha yuqori.",
        "Ta'minot: 2,7-5,5 V. Tok: 1,4 mA.",
        "Ish masofasi: buyumdan 1-3 sm. Uzoqroqda atrof yorug'ligi xalaqit beradi.",
        "S0/S1 — chastota bo'luvchi (0%, 2%, 20%, 100%). Arduino uchun 20 % qulay.",
        "S2/S3 — qaysi rang filtri o'qilishini tanlaydi.",
        "Modulda 4 ta oq LED bor — ular buyumni doim bir xil yoritib turadi.",
    ],
    ishlash=[
        "Har bir fotodiod oldiga rangli filtr qo'yilgan. Qizil filtr faqat qizil nurni o'tkazadi, qolganini to'sadi.",
        "Oq buyum uch rangni ham qaytaradi — uchala kanalda ham chastota yuqori.",
        "Qizil buyum faqat qizil nurni qaytaradi, yashil va ko'kni yutadi — shuning uchun R kanali yuqori, G va B past.",
        "Qora buyum hamma nurni yutadi — uchala kanal ham past.",
        "Ya'ni ko'z ham xuddi shunday ishlaydi: to'r pardada uch xil rangga sezgir kolbachalar bor.",
        "Chastota chiqishi shovqinga chidamli: uzun simda ham qiymat buzilmaydi (kuchlanish esa buziladi).",
    ],
    oqish=[
        "S2/S3 bilan filtr tanlanadi, keyin pulseIn(OUT, LOW) bilan impuls DAVOMIYLIGI o'lchanadi.",
        "Filtr jadvali: qizil S2=LOW S3=LOW; ko'k S2=LOW S3=HIGH; yashil S2=HIGH S3=HIGH; filtrsiz S2=HIGH S3=LOW.",
        "DIQQAT: pulseIn davomiylikni qaytaradi, ya'ni qiymat KICHIK bo'lsa rang KUCHLI.",
        "KALIBRLASH SHART: oq qog'oz va qora qog'ozda qiymatlarni o'lchab, map() bilan 0-255 oralig'iga chizmalanadi.",
        "Rangni aniqlash: R, G, B qiymatlaridan qaysi biri eng katta ekaniga qarab qaror qilinadi.",
        "Xona yorug'ligi o'zgarsa kalibrlashni QAYTA qilish kerak.",
    ],
    kod="""// TCS3200 — buyum rangini aniqlash
const int S0=4, S1=5, S2=6, S3=7, OUT=8;

// KALIBRLASH: oq va qora qog'ozda o'lchangan qiymatlar
int oqR=25, oqG=27, oqB=22;          // oq qog'ozda (eng kichik)
int qoraR=170, qoraG=180, qoraB=150; // qora qog'ozda (eng katta)

int olch(bool s2, bool s3) {
  digitalWrite(S2, s2); digitalWrite(S3, s3);
  delay(60);
  return pulseIn(OUT, LOW);
}

void setup() {
  pinMode(S0, OUTPUT); pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT); pinMode(S3, OUTPUT);
  pinMode(OUT, INPUT);
  digitalWrite(S0, HIGH); digitalWrite(S1, LOW);   // chastota 20 %
  Serial.begin(9600);
}

void loop() {
  int r = map(olch(LOW,  LOW ), oqR, qoraR, 255, 0);
  int g = map(olch(HIGH, HIGH), oqG, qoraG, 255, 0);
  int b = map(olch(LOW,  HIGH), oqB, qoraB, 255, 0);
  r = constrain(r,0,255); g = constrain(g,0,255); b = constrain(b,0,255);

  Serial.print("R="); Serial.print(r);
  Serial.print(" G="); Serial.print(g);
  Serial.print(" B="); Serial.print(b);

  // eng katta kanal rangni aytadi
  if (r > g && r > b && r > 60)      Serial.println("  -> QIZIL");
  else if (g > r && g > b && g > 60) Serial.println("  -> YASHIL");
  else if (b > r && b > g && b > 60) Serial.println("  -> KO'K");
  else if (r > 150 && g > 150 && b > 150) Serial.println("  -> OQ");
  else                               Serial.println("  -> QORA / noaniq");

  delay(400);
}""",
    qollash=["Buyumlarni rang bo'yicha saralash", "chiziq bo'ylab yuruvchi robot", "rang o'lchagich", "sifat nazorati"]),

"XIAO ESP32S3 Sense (kamera va mikrofon)": P(
    tasnif=[
        "Protsessor: ESP32-S3, ikki yadroli, 240 MHz. AI hisoblari uchun maxsus buyruqlari bor.",
        "Xotira: 8 MB PSRAM + 8 MB Flash. Kamera tasviri uchun PSRAM SHART.",
        "Kamera: OV2640, 2 megapiksel. Model o'rgatish uchun odatda 96x96 yoki 160x160 ga kichraytiriladi.",
        "Mikrofon: raqamli PDM mikrofon, platada o'rnatilgan.",
        "Aloqa: WiFi va Bluetooth 5 (BLE).",
        "O'lchami: 21 x 17,5 mm — bosh barmoq tirnog'idek.",
        "microSD slot bor — ma'lumot yig'ish uchun qulay.",
        "Ta'minot: USB-C yoki batareya (platada zaryadlash sxemasi bor).",
    ],
    ishlash=[
        "Bu plata AI darslari uchun tanlangan asosiy sabab: kamera ham, mikrofon ham PLATADA — qo'shimcha sim va modul kerak emas.",
        "Model qurilmaning O'ZIDA ishlaydi (TinyML). Internetga ulanish shart emas, ma'lumot hech qayerga yuborilmaydi.",
        "Bu ikki katta afzallik beradi: javob tez (kechikish 100 ms dan kam) va shaxsiy ma'lumot qurilmadan chiqmaydi.",
        "Ish tartibi: 1) ma'lumot yig'ish; 2) Edge Impulse'da belgilash; 3) model o'rgatish; 4) modelni siqish (kvantlash); 5) ZIP kutubxona sifatida yuklab olish; 6) IDE'ga qo'shib, plataga yuklash.",
        "Kvantlash: model sonlari 32 bitli kasrdan 8 bitli butun songa aylantiriladi. Model 4 marta kichrayadi, tezligi ortadi, aniqligi esa juda oz tushadi.",
    ],
    oqish=[
        "Arduino IDE sozlamalari: Board = XIAO_ESP32S3, PSRAM = OPI PSRAM (YOQILGAN BO'LISHI SHART).",
        "Model kutubxonasi: Edge Impulse > Deployment > Arduino library > ZIP yuklab olish.",
        "IDE'da: Sketch > Include Library > Add .ZIP Library.",
        "Kodda: #include <loyiha_nomi_inferencing.h>",
        "Natija ei_impulse_result_t tuzilmasida keladi: har bir sinf uchun ehtimollik (0 dan 1 gacha).",
        "Qaror qabul qilish: eng katta ehtimollikli sinf tanlanadi, lekin u chegaradan (masalan 0,7) yuqori bo'lishi kerak. Aks holda \"noaniq\" deb javob berilgan ma'qul.",
        "Kechikish (latency) natija bilan birga chiqadi — modelning tezligini shundan bilasiz.",
    ],
    kod="""// XIAO ESP32S3 Sense — Edge Impulse modelini ishlatish
// (model ZIP kutubxona sifatida IDE ga qo'shilgan bo'lishi kerak)
#include <loyiha_nomi_inferencing.h>

const int LED = D0, ZUMMER = D1;
const float CHEGARA = 0.70;          // ishonch chegarasi

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  while (!Serial);
  Serial.println("Model yuklandi. Sinflar:");
  for (size_t i = 0; i < EI_CLASSIFIER_LABEL_COUNT; i++) {
    Serial.print("  - "); Serial.println(ei_classifier_inferencing_categories[i]);
  }
}

void loop() {
  ei_impulse_result_t natija = { 0 };

  // ... bu yerda sensor/kamera ma'lumoti signal ga to'ldiriladi ...
  // run_classifier(&signal, &natija, false);

  // eng ishonchli sinfni topamiz
  float engKatta = 0;
  const char* sinf = "noaniq";
  for (size_t i = 0; i < EI_CLASSIFIER_LABEL_COUNT; i++) {
    if (natija.classification[i].value > engKatta) {
      engKatta = natija.classification[i].value;
      sinf = natija.classification[i].label;
    }
  }

  Serial.print("Sinf: "); Serial.print(sinf);
  Serial.print("  ishonch: "); Serial.print(engKatta * 100, 1); Serial.print(" %");
  Serial.print("  kechikish: "); Serial.print(natija.timing.classification); Serial.println(" ms");

  // CHEGARA: past ishonchda qaror QABUL QILMAYMIZ
  if (engKatta >= CHEGARA) {
    digitalWrite(LED, HIGH);
    tone(ZUMMER, 1800, 100);
  } else {
    digitalWrite(LED, LOW);
    Serial.println("  -> ishonch past, javob berilmaydi");
  }
  delay(200);
}""",
    qollash=["Ovoz buyrug'i bilan boshqarish", "buyumni tanish", "imo-ishorani tanish", "odam sanash", "sifat nazorati"]),

"ESP32-CAM": P(
    tasnif=[
        "Protsessor: ESP32, 240 MHz, 4 MB PSRAM.",
        "Kamera: OV2640, 2 MP. Maksimal ruxsat: 1600x1200 (UXGA).",
        "microSD slot bor.",
        "Ta'minot: 5 V, 200-300 mA (kamera ishlaganda). 3,3 V da tok yetmaydi.",
        "USB YO'Q — dastur USB-TTL (FTDI) adapter orqali yuklanadi.",
        "Yuklash tartibi: IO0 ni GND ga ulash -> RESET bosish -> Upload -> yuklangach IO0 ni uzish.",
        "Platada yorqin LED (GPIO4) va kichik qizil indikator bor.",
    ],
    ishlash=[
        "Kamera matritsasi — millionlab mayda fotodiod. Har biri o'ziga tushgan yorug'lik miqdorini kuchlanishga aylantiradi.",
        "Har bir piksel oldida rangli filtr bor (Bayer filtri): 50 % yashil, 25 % qizil, 25 % ko'k. Ko'z yashil rangga eng sezgir bo'lgani uchun shunday.",
        "Protsessor bu ma'lumotni JPEG ga siqadi va WiFi orqali yuboradi.",
        "Video oqim (stream) aslida ketma-ket yuborilayotgan alohida rasmlar: sekundiga 10-25 kadr.",
        "Kamera shlangi juda mo'rt — qayta-qayta uzib-ulash tavsiya etilmaydi.",
    ],
    oqish=[
        "Namuna: File > Examples > ESP32 > Camera > CameraWebServer.",
        "Kodda kamera modelini tanlash kerak: #define CAMERA_MODEL_AI_THINKER.",
        "WiFi nomi va parolini kiritib yuklanadi; Serial monitorda IP manzil chiqadi.",
        "Brauzerda shu IP ochiladi — jonli tasvir va sozlamalar paneli ko'rinadi.",
        "Rasmni saqlash: esp_camera_fb_get() bilan kadr olinadi, keyin SD kartga yoziladi va esp_camera_fb_return() bilan buffer bo'shatiladi.",
        "Buffer qaytarilmasa xotira tugaydi va plata qayta yuklanadi — bu eng ko'p uchraydigan xato.",
    ],
    kod="""// ESP32-CAM — WiFi orqali jonli tasvir (CameraWebServer misolining qisqartmasi)
#include "esp_camera.h"
#include <WiFi.h>

#define CAMERA_MODEL_AI_THINKER
#include "camera_pins.h"

const char* WIFI_NOM   = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";

void startCameraServer();     // kutubxona misolidan keladi

void setup() {
  Serial.begin(115200);

  camera_config_t cfg;
  // ... pin sozlamalari camera_pins.h dan keladi ...
  cfg.frame_size   = FRAMESIZE_VGA;    // 640x480 — tarmoq uchun qulay
  cfg.jpeg_quality = 12;               // kichik son = yaxshi sifat, katta fayl
  cfg.fb_count     = 2;                // PSRAM bo'lsa 2 ta buffer

  if (esp_camera_init(&cfg) != ESP_OK) {
    Serial.println("Kamera ishga tushmadi! PSRAM va shlangni tekshiring.");
    return;
  }

  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }

  startCameraServer();
  Serial.print("\\nBrauzerda oching: http://");
  Serial.println(WiFi.localIP());
}

void loop() {
  delay(10000);      // butun ish veb-server ichida boradi
}""",
    qollash=["Video kuzatuv", "eshik ko'zi", "robot ko'zi", "hayvonlarni kuzatish", "AI tasvir tanish"]),
}


# ---------------------------------------------------------------- foydalanish
def olish(nom):
    """ulanish.py kaliti bo'yicha pasportni qaytaradi (bo'lmasa None)."""
    return PASPORT.get(nom)


if __name__ == "__main__":
    from ulanish import ULANISH
    yoq = [k for k in ULANISH if k not in PASPORT]
    ortiqcha = [k for k in PASPORT if k not in ULANISH]
    print("ULANISH:", len(ULANISH), " PASPORT:", len(PASPORT))
    print("pasporti yo'q:", yoq or "—")
    print("ortiqcha kalit:", ortiqcha or "—")
    jami = sum(len(v["tasnif"]) + len(v["ishlash"]) + len(v["oqish"]) for v in PASPORT.values())
    kod = sum(1 for v in PASPORT.values() if v["kod"])
    print("jami band:", jami, " kod namunasi:", kod)
