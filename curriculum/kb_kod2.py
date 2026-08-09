# -*- coding: utf-8 -*-
"""
KOD BAZASI — 2-qism.

kb_kod.py da qamrab olinmagan mavzular: sillabusda boshqacha nom bilan
yozilgan takroriy mavzular, blokli dasturlash darslari va bir necha
qolgan mavzu. Tuzilishi kb_kod.py bilan aynan bir xil.
"""


# K() shu yerda qayta e'lon qilinadi: kb_kod dan import qilinsa aylanma
# import hosil bo'lardi (kb_kod oxirida kb_kod2 ni chaqiradi).
def K(nom, izoh, kod, amaliy=None):
    return {"nom": nom, "izoh": izoh, "kod": kod, "amaliy": amaliy}


KODLAR2 = {

# ==================================================== PLATA VA MUHIT
"Arduino platasi bilan tanishuv": K(
    "Plata bo'limlarini birma-bir sinaydigan dastur",
    "Plataning har bir qismi (raqamli pin, PWM pin, analog pin, ichki LED, "
    "Serial) alohida sinab ko'riladi.",
    """// Plataning har bir qismini birma-bir sinash
const int ODDIY = 7;      // oddiy raqamli chiqish
const int PWM_P = 9;      // ~ belgisi bor pin
const int ANALOG = A0;    // analog kirish

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(ODDIY, OUTPUT);
  pinMode(PWM_P, OUTPUT);
  Serial.begin(9600);

  Serial.println("=== PLATA SINOVI ===");
  Serial.println("1) Ichki LED (D13)");
  for (int i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH); delay(200);
    digitalWrite(LED_BUILTIN, LOW);  delay(200);
  }
}

void loop() {
  Serial.println("2) Oddiy raqamli pin D7 — faqat yoq/o'chir");
  digitalWrite(ODDIY, HIGH); delay(600);
  digitalWrite(ODDIY, LOW);  delay(600);

  Serial.println("3) PWM pin D9 — oraliq yorqinlik");
  for (int y = 0; y <= 255; y += 51) {
    analogWrite(PWM_P, y);
    Serial.print("   PWM = "); Serial.println(y);
    delay(300);
  }
  analogWrite(PWM_P, 0);

  Serial.print("4) Analog kirish A0 = ");
  Serial.println(analogRead(ANALOG));
  Serial.println();
  delay(1000);
}""",
    amaliy="Platani ulab, D7 ga oddiy LED, D9 ga PWM LED va A0 ga potensiometr "
           "ulash; uch xil pinning farqini bir sxemada ko'rib, plata xaritasini "
           "daftarga chizish"),

"Arduino Uno: pinlar va imkoniyatlar": K(
    "Pin turlarini va ularning chegaralarini ko'rsatuvchi dastur",
    "Uno da 14 raqamli pin (shundan 6 tasi PWM) va 6 analog pin bor. "
    "Har birining o'z chegarasi va vazifasi bor.",
    """// Uno pinlari: turlari va chegaralari
// D0, D1  — Serial (USB bilan band, imkon qadar ishlatilmaydi)
// D2, D3  — uzilish (interrupt) pinlari
// D3,5,6,9,10,11 — PWM (~ belgisi bor)
// D13     — ichki LED ulangan
// A0..A5  — analog kirish; A4=SDA, A5=SCL (I2C)

const int PWM_PIN[6] = {3, 5, 6, 9, 10, 11};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 6; i++) pinMode(PWM_PIN[i], OUTPUT);

  Serial.println("=== ARDUINO UNO PIN XARITASI ===");
  Serial.println("Raqamli pin: 14 ta (D0..D13)");
  Serial.println("  shundan PWM: D3, D5, D6, D9, D10, D11");
  Serial.println("  uzilish:     D2, D3");
  Serial.println("  ichki LED:   D13");
  Serial.println("Analog pin: 6 ta (A0..A5), ADC 10 bitli -> 0..1023");
  Serial.println("  I2C: A4 = SDA, A5 = SCL");
  Serial.println();
  Serial.println("CHEGARALAR:");
  Serial.println("  bitta pin: 40 mA (xavfsizi 20 mA)");
  Serial.println("  butun plata: 200 mA");
  Serial.println("  5V pin: taxminan 400-500 mA (USB dan)");
}

void loop() {
  // hamma PWM pinni navbat bilan sinaymiz
  for (int i = 0; i < 6; i++) {
    Serial.print("PWM sinovi: D"); Serial.println(PWM_PIN[i]);
    for (int y = 0; y <= 255; y += 15) { analogWrite(PWM_PIN[i], y); delay(20); }
    for (int y = 255; y >= 0; y -= 15) { analogWrite(PWM_PIN[i], y); delay(20); }
  }
}""",
    amaliy="Har bir PWM pinga navbat bilan LED ulab sinash, PWM va oddiy pin "
           "farqini ko'rsatish; pin chegaralarini jadvalga yozib, nechta LEDni "
           "bir vaqtda yoqish mumkinligini hisoblash"),

"Plataning pinlari va ularning vazifasi": K(
    "Kirish va chiqish pinlarini bir sxemada solishtirish",
    "Pin KIRISH bo'lsa plata uni o'qiydi, CHIQISH bo'lsa unga kuchlanish "
    "beradi. Bir pin bir vaqtda ikkisi bo'la olmaydi.",
    """// Kirish va chiqish pinlari yonma-yon
const int KIRISH_R = 2;    // raqamli kirish (tugma)
const int KIRISH_A = A0;   // analog kirish (potensiometr)
const int CHIQISH_R = 7;   // raqamli chiqish (LED)
const int CHIQISH_P = 9;   // PWM chiqish (LED)

void setup() {
  pinMode(KIRISH_R, INPUT_PULLUP);
  pinMode(CHIQISH_R, OUTPUT);
  pinMode(CHIQISH_P, OUTPUT);
  // analog kirish uchun pinMode SHART EMAS
  Serial.begin(9600);
  Serial.println("raqamli kirish | analog kirish | chiqishlar");
}

void loop() {
  // KIRISHLARNI O'QIYMIZ
  int tugma = digitalRead(KIRISH_R);      // 0 yoki 1
  int pot   = analogRead(KIRISH_A);       // 0..1023

  // CHIQISHLARGA YOZAMIZ
  digitalWrite(CHIQISH_R, tugma == LOW);           // faqat yoq/o'chir
  analogWrite(CHIQISH_P, map(pot, 0, 1023, 0, 255)); // oraliq qiymat

  Serial.print(tugma == LOW ? "BOSILGAN" : "bo'sh  ");
  Serial.print("  |  pot=");  Serial.print(pot);
  Serial.print("  |  PWM=");  Serial.println(map(pot, 0, 1023, 0, 255));
  delay(200);
}""",
    amaliy="Tugma, potensiometr va ikki LED yig'ib, ikki kirish va ikki chiqish "
           "pinini bir sxemada ishlatish; chiqish pinini ataylab INPUT qilib "
           "qo'yib, LED nima uchun yonmasligini tushuntirish"),

"IDE bilan tanishuv (matnli muhit)": K(
    "IDE ning asosiy tugmalarini sinaydigan dastur",
    "Verify (tekshirish) va Upload (yuklash) — ikki asosiy tugma. Verify "
    "faqat xatoni topadi, Upload esa plataga yozadi.",
    """// IDE bilan tanishuv: ataylab xato qo'yib, Verify ni sinash
const int LED = 9;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Bu yozuv Serial monitorda ko'rinadi.");
  Serial.println("Monitor tezligi 9600 ga qo'yilgan bo'lishi kerak!");
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(500);
  digitalWrite(LED, LOW);
  delay(500);

  Serial.println("sikl tugadi");

  // TAJRIBA 1: quyidagi qatorning nuqta-vergulini o'chiring va Verify bosing.
  //            Kompilyator xato qatorini ko'rsatadi.
  // int x = 5

  // TAJRIBA 2: delay(500) ni delay(50) ga o'zgartiring va Upload bosing.
  //            O'zgarish faqat Upload dan keyin ko'rinadi, Verify dan keyin emas.
}""",
    amaliy="IDE ni ochib, kodni yuklash va Serial monitorni ochish; ataylab "
           "nuqta-vergulni o'chirib Verify bosish va kompilyator xato qatorini "
           "qanday ko'rsatishini o'rganish"),

"Birinchi dasturni plataga yuklash": K(
    "Yuklash muvaffaqiyatli bo'lganini tasdiqlovchi dastur",
    "Yuklash tugagach ikki belgi bo'lishi kerak: LED miltillaydi va Serial "
    "monitorda yozuv chiqadi.",
    """// Yuklash tekshiruvi: ikki belgi bilan tasdiqlanadi
const int LED = 9;
int sanoq = 0;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);

  // 1-belgi: uch marta tez miltillash — dastur ishga tushdi
  for (int i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH); delay(100);
    digitalWrite(LED_BUILTIN, LOW);  delay(100);
  }
  // 2-belgi: Serial monitorda yozuv
  Serial.println("YUKLASH MUVAFFAQIYATLI!");
}

void loop() {
  sanoq++;
  digitalWrite(LED, HIGH); delay(400);
  digitalWrite(LED, LOW);  delay(400);
  Serial.print("ishlayapti, sikl: "); Serial.println(sanoq);
}

// YUKLASH XATOLARI VA SABABLARI:
//  "Port not found"        -> kabel yoki drayver muammosi
//  "Board not in sync"     -> Tools > Board noto'g'ri tanlangan
//  "Access denied"         -> port boshqa dastur tomonidan band
//  Ma'nosiz belgilar       -> Serial monitor tezligi mos emas""",
    amaliy="Platani ulab, port va plata turini sozlash, dasturni yuklash va "
           "ikki belgini (miltillash + Serial yozuvi) tasdiqlash; keyin "
           "noto'g'ri port tanlab, xato xabarini ko'rish"),

"setup() va loop() nima qiladi": K(
    "Ikki funksiya farqini isbotlovchi tajriba",
    "setup bir marta, loop cheksiz. Buni sanoq va RESET tugmasi bilan "
    "ko'z bilan ko'rish mumkin.",
    """// setup BIR MARTA, loop CHEKSIZ — sanoq bilan isbotlaymiz
const int LED = 9, ZUMMER = 8;
int setupSoni = 0;      // bu har RESET da 0 dan boshlanadi
int loopSoni = 0;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);

  setupSoni++;
  Serial.println("=====================================");
  Serial.print("SETUP bajarildi. setupSoni = ");
  Serial.println(setupSoni);       // DOIM 1 chiqadi
  Serial.println("=====================================");

  tone(ZUMMER, 1500, 200);         // yoqilganini bildiruvchi signal
  delay(500);
}

void loop() {
  loopSoni++;
  Serial.print("loop #"); Serial.println(loopSoni);   // 1, 2, 3, ... o'sib boradi

  digitalWrite(LED, HIGH); delay(300);
  digitalWrite(LED, LOW);  delay(300);
}

// TAJRIBA: RESET tugmasini bosing.
//   setupSoni yana 1 bo'ladi, loopSoni esa 1 dan qayta boshlanadi.
//   Bu setup ning faqat bir marta ishlashini isbotlaydi.""",
    amaliy="LED va zummer yig'ib, setup ichida bir martalik signal, loop ichida "
           "takrorlanuvchi miltillash yozish; RESET bosib, sanoqlarning "
           "qanday qayta boshlanishini kuzatish"),

"Birinchi dastur: Blink": K(
    "Blink va uni o'zgartirib sinash",
    "Blink — birinchi dastur, lekin uning qiymatlarini O'ZGARTIRIB ko'rish "
    "o'rganishning asosiy usuli.",
    """// Blink va tajribalar
const int LED = 9;
int yoniq = 500;      // yonib turish vaqti
int ochiq = 500;      // o'chib turish vaqti

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("yoniq(ms) | o'chiq(ms)");
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(yoniq);
  digitalWrite(LED, LOW);
  delay(ochiq);

  Serial.print(yoniq); Serial.print("       | "); Serial.println(ochiq);

  // TAJRIBA: kechikishni asta kamaytiramiz
  yoniq -= 25;
  ochiq -= 25;
  if (yoniq < 15) { yoniq = 500; ochiq = 500; Serial.println("--- qayta boshlandi ---"); }

  // 30-40 ms dan pastda ko'z miltillashni ILG'AMAY qoladi:
  // LED xira, lekin doim yonib turgandek ko'rinadi. Bu PWM ning asosi.
}""",
    amaliy="LEDni 220 Om rezistor bilan ulab, kechikishni 500 dan 15 ms gacha "
           "kamaytirib borish va ko'z qaysi qiymatdan boshlab miltillashni "
           "ilg'amay qolishini aniq o'lchash"),

"delay va vaqt": K(
    "delay() va millis() ni yonma-yon solishtirish",
    "delay ishlaganda plata boshqa hech narsa qila olmaydi. millis() esa "
    "vaqtni sanaydi va dasturni to'xtatmaydi.",
    """// delay va millis: farqni tugma bilan isbotlaymiz
const int LED1 = 9, LED2 = 10, TUGMA = 2;
unsigned long oxirgi = 0;
bool holat2 = false;

void setup() {
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT);
  pinMode(TUGMA, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("delay ishlayotganda tugmani bosib ko'ring — sezilmaydi");
}

void loop() {
  // --- LED2: millis bilan, dasturni TO'XTATMAYDI ---
  if (millis() - oxirgi >= 250) {
    oxirgi = millis();
    holat2 = !holat2;
    digitalWrite(LED2, holat2);
  }

  // --- tugmani doim tekshiramiz ---
  if (digitalRead(TUGMA) == LOW) Serial.println("TUGMA BOSILDI");

  // --- LED1: delay bilan, plata shu yerda 1,5 sekund MUZLAB turadi ---
  digitalWrite(LED1, HIGH);
  delay(1500);                  // shu paytda tugma ham, LED2 ham ishlamaydi
  digitalWrite(LED1, LOW);
  delay(1500);
}""",
    amaliy="Ikki LED va tugma yig'ib, delay ishlayotgan paytda tugma bosilishi "
           "va ikkinchi LED miltillashi to'xtab qolishini tajribada isbotlash, "
           "keyin ikkalasini millis() ga o'tkazib farqni ko'rish"),

"Kutubxona (library) ishlatish": K(
    "Kutubxonasiz va kutubxona bilan yozilgan kod",
    "Kutubxona murakkab ishni bir necha buyruqqa qisqartiradi. Farqni "
    "servo misolida ko'rish oson.",
    """// Kutubxonaning foydasi: servo misolida
#include <Servo.h>
Servo servo;
const int POT = A0;

void setup() {
  servo.attach(9);
  Serial.begin(9600);
}

void loop() {
  int burchak = map(analogRead(POT), 0, 1023, 0, 180);
  servo.write(burchak);           // BITTA qator — hammasi tayyor
  Serial.println(burchak);
  delay(50);
}

/*  KUTUBXONASIZ AYNI ISH shunday bo'lardi:
    her 20 ms da aniq uzunlikdagi impuls yuborish kerak,
    impuls uzunligi esa burchakka bog'liq (1000..2000 mikrosekund):

    void servoYuborr(int pin, int burchak) {
      int uzunlik = map(burchak, 0, 180, 1000, 2000);
      digitalWrite(pin, HIGH);
      delayMicroseconds(uzunlik);
      digitalWrite(pin, LOW);
      delayMicroseconds(20000 - uzunlik);
    }
    Va buni loop ichida TO'XTOVSIZ chaqirib turish kerak edi.
*/

// KUTUBXONA O'RNATISH:
//  Sketch > Include Library > Manage Libraries
//  Nom bo'yicha qidirish -> Install
//  Ishni DOIM File > Examples ichidagi misoldan boshlash kerak.""",
    amaliy="Servo motorni potensiometr bilan boshqarish uchun avval Servo "
           "kutubxonasidan foydalanish, keyin kutubxonasiz impuls yuborishga "
           "urinib ko'rish va ikki kod uzunligini solishtirish"),

# ==================================================== BLOKLI DASTURLASH
"Kutish (delay) blogi": K(
    "Kutish blogining matnli ko'rinishi",
    "Blokli muhitdagi kutish blogi Arduino'dagi delay() ga to'g'ri keladi.",
    """// Kutish blogi = delay()
const int LED = 9, ZUMMER = 8;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(ZUMMER, OUTPUT);
}

void loop() {
  // BLOK:  <LEDni yoq>  <1 soniya kut>  <LEDni o'chir>  <1 soniya kut>
  digitalWrite(LED, HIGH);
  delay(1000);
  digitalWrite(LED, LOW);
  delay(1000);

  // Kutish vaqtini o'zgartirib naqsh yasash:
  // qisqa-qisqa-uzun
  digitalWrite(LED, HIGH); delay(150); digitalWrite(LED, LOW); delay(150);
  digitalWrite(LED, HIGH); delay(150); digitalWrite(LED, LOW); delay(150);
  digitalWrite(LED, HIGH); delay(600); digitalWrite(LED, LOW); delay(600);

  tone(ZUMMER, 1200, 100);
}""",
    amaliy="LED va zummerni ulab, mBlock'da kutish blogi bilan turli tezlikdagi "
           "miltillash naqshlarini yasash, keyin ayni natijani matnli kodda "
           "delay() bilan takrorlash"),

"Ikki blokni ketma-ket qo'yish": K(
    "Ketma-ketlik: tartib natijani belgilaydi",
    "Bloklar yuqoridan pastga qat'iy tartibda bajariladi. Tartibni "
    "o'zgartirsangiz natija ham o'zgaradi.",
    """// Ketma-ketlik: tartib muhim
const int QIZIL = 7, YASHIL = 8, ZUMMER = 9;

void setup() {
  pinMode(QIZIL, OUTPUT); pinMode(YASHIL, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // 1-VARIANT: signal, keyin chiroq
  Serial.println("1-variant: avval signal, keyin chiroq");
  tone(ZUMMER, 1500, 200);
  delay(400);
  digitalWrite(YASHIL, HIGH);
  delay(1000);
  digitalWrite(YASHIL, LOW);
  delay(1000);

  // 2-VARIANT: chiroq, keyin signal — AYNI bloklar, boshqa TARTIB
  Serial.println("2-variant: avval chiroq, keyin signal");
  digitalWrite(QIZIL, HIGH);
  delay(1000);
  tone(ZUMMER, 1500, 200);
  delay(400);
  digitalWrite(QIZIL, LOW);
  delay(1000);

  // Ikki variant BIR XIL bloklardan iborat, lekin natija boshqacha.
}""",
    amaliy="Ikki LED va zummer yig'ib, bir xil bloklarni ikki xil tartibda "
           "qo'yib natijani solishtirish; svetofor tartibini ataylab buzib, "
           "nima uchun ketma-ketlik muhimligini ko'rsatish"),

"O'zgaruvchi blogi bilan tanishuv": K(
    "O'zgaruvchi bilan bir joydan boshqarish",
    "O'zgaruvchi — nomlangan qiymat. Uni bir joyda o'zgartirsangiz, u "
    "ishlatilgan hamma joyda o'zgaradi.",
    """// O'zgaruvchi blogi: bir joydan hamma narsani boshqarish
const int LED1 = 7, LED2 = 8, LED3 = 9;
const int POT = A0;

int tezlik = 300;        // O'ZGARUVCHI — hamma kechikish shundan olinadi

void setup() {
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT); pinMode(LED3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // potensiometr o'zgaruvchini jonli o'zgartiradi
  tezlik = map(analogRead(POT), 0, 1023, 50, 800);

  digitalWrite(LED1, HIGH); delay(tezlik); digitalWrite(LED1, LOW);
  digitalWrite(LED2, HIGH); delay(tezlik); digitalWrite(LED2, LOW);
  digitalWrite(LED3, HIGH); delay(tezlik); digitalWrite(LED3, LOW);

  Serial.print("tezlik o'zgaruvchisi = "); Serial.println(tezlik);

  // O'zgaruvchisiz bo'lsa: delay(300) ni UCH joyda qo'lda o'zgartirish
  // kerak bo'lardi va bittasi doim esdan chiqardi.
}""",
    amaliy="Uch LED va potensiometr yig'ib, miltillash tezligini bitta "
           "o'zgaruvchi orqali boshqarish; o'zgaruvchini olib tashlab, "
           "qiymatni har joyda qo'lda o'zgartirishga urinib farqni his qilish"),

"Sanoqni ekranda ko'rish": K(
    "Sanoq o'zgaruvchisini ekranda kuzatish",
    "Sanoq — har hodisada bittaga oshadigan o'zgaruvchi. Uni ekranda "
    "ko'rsatish tugma va LCD bilan qilinadi.",
    """// Sanoq: tugma bosilishlarini sanab, LCD ekranda ko'rsatish
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

const int TUGMA = 2, LED = 9;
int sanoq = 0;
int oldingi = HIGH;

void setup() {
  pinMode(TUGMA, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
  lcd.init(); lcd.backlight();
  Serial.begin(9600);

  lcd.setCursor(0, 0);
  lcd.print("Bosishlar soni:");
  lcd.setCursor(0, 1);
  lcd.print(sanoq);
}

void loop() {
  int hozir = digitalRead(TUGMA);

  // bosilish LAHZASINI ushlaymiz (HIGH dan LOW ga o'tish)
  if (oldingi == HIGH && hozir == LOW) {
    sanoq++;

    lcd.setCursor(0, 1);
    lcd.print(sanoq);
    lcd.print("      ");        // eski raqam qoldig'ini o'chirish

    digitalWrite(LED, HIGH); delay(80); digitalWrite(LED, LOW);
    Serial.print("sanoq = "); Serial.println(sanoq);
    delay(50);                 // kontakt sakrashiga qarshi
  }
  oldingi = hozir;
}""",
    amaliy="Tugma, LED va LCD ekran yig'ib, tugma bosilishlarini sanab ekranda "
           "ko'rsatish; eski raqam qoldig'ini o'chirmasdan sinab, nima uchun "
           "bo'sh joy yozish kerakligini ko'rsatish"),

"Sensor qiymatini ekranda kuzatish": K(
    "Sensor qiymatini ekranda jonli ko'rsatish",
    "Serial monitor kompyuterga bog'liq. Ekran esa qurilmani mustaqil "
    "qiladi — bu tayyor mahsulotga birinchi qadam.",
    """// Sensor qiymatini LCD ekranda jonli ko'rsatish
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

const int LDR = A0, TERM = A1;
unsigned long oxirgi = 0;

void setup() {
  lcd.init(); lcd.backlight();
  Serial.begin(9600);
  lcd.setCursor(0, 0); lcd.print("Yorug'lik:");
  lcd.setCursor(0, 1); lcd.print("Harorat:");
}

void loop() {
  // ekranni tez-tez yangilash uni "titratadi" — 300 ms yetarli
  if (millis() - oxirgi < 300) return;
  oxirgi = millis();

  int y = map(analogRead(LDR), 0, 1023, 0, 100);
  int t = map(analogRead(TERM), 0, 1023, 0, 50);

  lcd.setCursor(11, 0);
  lcd.print(y); lcd.print("%  ");      // orqadagi probellar eski raqamni o'chiradi

  lcd.setCursor(11, 1);
  lcd.print(t); lcd.print("C  ");

  Serial.print("yorug'lik="); Serial.print(y);
  Serial.print("  harorat="); Serial.println(t);
}""",
    amaliy="Fotorezistor, termistor va LCD ekran yig'ib, ikki qiymatni ekranda "
           "jonli ko'rsatish; USB kabelni uzib, qurilma batareyada mustaqil "
           "ishlashini tekshirish"),

"Haroratli ogohlantirish": K(
    "Chegaradan oshganda signal beruvchi tizim",
    "Gisterezis va tasdiqlash bilan — yolg'on signal bermaydigan qilib "
    "yoziladi.",
    """// Haroratli ogohlantirish: gisterezis + tasdiqlash bilan
const int TERM = A0;
const int LED_YASHIL = 7, LED_QIZIL = 8, ZUMMER = 9;

const int YOQ_CHEGARA   = 30;    // shundan yuqori — ogohlantirish
const int OCHIR_CHEGARA = 27;    // shundan past  — normal (gisterezis)
const int TASDIQ = 3;            // ketma-ket shuncha marta tasdiqlansin

bool xavf = false;
int ketmaKet = 0;

int haroratOlch() {
  long y = 0;
  for (int i = 0; i < 10; i++) { y += analogRead(TERM); delay(5); }
  return map(y / 10, 0, 1023, 0, 50);      // soddalashtirilgan chizmalash
}

void setup() {
  pinMode(LED_YASHIL, OUTPUT); pinMode(LED_QIZIL, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int t = haroratOlch();

  // TASDIQLASH: bitta sakragan qiymat signal bermaydi
  if (!xavf && t > YOQ_CHEGARA)        ketmaKet++;
  else if (xavf && t < OCHIR_CHEGARA)  ketmaKet++;
  else                                  ketmaKet = 0;

  if (ketmaKet >= TASDIQ) { ketmaKet = 0; xavf = !xavf; }

  digitalWrite(LED_QIZIL, xavf);
  digitalWrite(LED_YASHIL, !xavf);
  if (xavf) tone(ZUMMER, 2200, 200);

  Serial.print("t="); Serial.print(t); Serial.print(" C  ");
  Serial.println(xavf ? "[OGOHLANTIRISH]" : "normal");
  delay(500);
}""",
    amaliy="Termistorli bo'luvchi, ikki LED va zummer yig'ib, ogohlantirish "
           "tizimini yasash; avval bitta chegara bilan sinab, chegarada "
           "titrashini ko'rish, keyin gisterezis qo'shib muammoni bartaraf etish"),

"Bir nechta sensorni birga o'qish": K(
    "Uch sensorni bir dasturda o'qish va vaqtni boshqarish",
    "Har bir sensorning o'z o'qish tezligi bor: DHT22 sekundiga bir marta, "
    "fotorezistorni esa tez-tez o'qish mumkin.",
    """// Uch sensor, uch xil o'qish tezligi — millis bilan boshqariladi
#include <DHT.h>
DHT dht(2, DHT22);

const int LDR = A0, TRIG = 9, ECHO = 10;

unsigned long tDht = 0, tLdr = 0, tMasofa = 0;
float harorat = 0, namlik = 0;
int yoruglik = 0;
float masofa = 0;

float masofaOlch() {
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long v = pulseIn(ECHO, HIGH, 30000);
  return v ? v * 0.034 / 2.0 : -1;
}

void setup() {
  pinMode(TRIG, OUTPUT); pinMode(ECHO, INPUT);
  dht.begin();
  Serial.begin(9600);
  Serial.println("harorat | namlik | yorug'lik | masofa");
}

void loop() {
  // DHT22 — sekundiga BIR MARTA (tezroq so'ralsa nan qaytaradi)
  if (millis() - tDht > 2000) {
    tDht = millis();
    float h = dht.readHumidity(), t = dht.readTemperature();
    if (!isnan(h) && !isnan(t)) { namlik = h; harorat = t; }
  }

  // Fotorezistor — tez-tez o'qish mumkin
  if (millis() - tLdr > 100) { tLdr = millis(); yoruglik = analogRead(LDR); }

  // HC-SR04 — o'lchovlar orasida 60 ms kerak
  if (millis() - tMasofa > 200) { tMasofa = millis(); masofa = masofaOlch(); }

  // Chiqarish — alohida tezlikda
  static unsigned long tChiq = 0;
  if (millis() - tChiq > 1000) {
    tChiq = millis();
    Serial.print(harorat, 1); Serial.print(" C | ");
    Serial.print(namlik, 1);  Serial.print(" % | ");
    Serial.print(yoruglik);   Serial.print(" | ");
    Serial.print(masofa, 1);  Serial.println(" sm");
  }
}""",
    amaliy="DHT22, fotorezistor va HC-SR04 ni bir plataga ulab, har birini o'z "
           "tezligida o'qish; hammasini delay bilan o'qishga urinib, DHT22 nan "
           "qaytarishini va masofa o'lchovi buzilishini ko'rsatish"),

# ==================================================== ESP32 VA AI
"BLE bilan telefonga ulanish": K(
    "BLE orqali telefondan boshqarish",
    "BLE — kam quvvat sarflaydigan Bluetooth. iPhone bilan ham ishlaydi "
    "(HC-05 esa ishlamaydi).",
    """// BLE: telefondan buyruq qabul qilish
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

#define XIZMAT_UUID "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define XUSUS_UUID  "beb5483e-36e1-4688-b7f5-ea07361b26a8"

const int LED = 2, ZUMMER = 5, SENSOR = 34;
BLECharacteristic *xusus;
bool ulangan = false;

class ServerCB : public BLEServerCallbacks {
  void onConnect(BLEServer* s)    { ulangan = true;  Serial.println("Telefon ulandi"); }
  void onDisconnect(BLEServer* s) { ulangan = false; Serial.println("Uzildi");
                                    s->getAdvertising()->start(); }
};

class XususCB : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic *x) {
    String buyruq = x->getValue().c_str();
    Serial.print("Buyruq: "); Serial.println(buyruq);
    if (buyruq == "yoq")    digitalWrite(LED, HIGH);
    if (buyruq == "ochir")  digitalWrite(LED, LOW);
    if (buyruq == "signal") tone(ZUMMER, 2000, 300);
  }
};

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);

  BLEDevice::init("Tarbion-Qurilma");        // telefonda shu nom ko'rinadi
  BLEServer *server = BLEDevice::createServer();
  server->setCallbacks(new ServerCB());

  BLEService *xizmat = server->createService(XIZMAT_UUID);
  xusus = xizmat->createCharacteristic(XUSUS_UUID,
            BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE |
            BLECharacteristic::PROPERTY_NOTIFY);
  xusus->addDescriptor(new BLE2902());
  xusus->setCallbacks(new XususCB());

  xizmat->start();
  server->getAdvertising()->start();
  Serial.println("BLE tayyor. Telefonda 'nRF Connect' ilovasidan qidiring.");
}

void loop() {
  // ulangan bo'lsa sensor qiymatini telefonga yuboramiz
  if (ulangan) {
    String q = String(analogRead(SENSOR));
    xusus->setValue(q.c_str());
    xusus->notify();
  }
  delay(1000);
}""",
    amaliy="ESP32 ga LED va zummer ulab BLE serverini ishga tushirish, "
           "telefondagi nRF Connect ilovasi orqali ulanib buyruq yuborish va "
           "sensor qiymatini telefonda jonli ko'rish"),

"Loyiha yaratish va qurilmani ulash": K(
    "Ma'lumot yig'ish uchun qurilmani tayyorlash",
    "Edge Impulse ga ulashdan oldin sensor to'g'ri ishlayotganini va namuna "
    "olish tezligi barqarorligini tekshirish kerak.",
    """// Ma'lumot yig'ishdan OLDINGI tekshiruv
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
const int ORALIQ = 10;          // 10 ms = 100 Hz
unsigned long oxirgi = 0;
int namunaSoni = 0;
unsigned long boshlangan;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  if (!mpu.begin()) {
    Serial.println("XATO: MPU6050 topilmadi. SDA/SCL va AD0 ni tekshiring.");
    while (true);
  }
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);

  Serial.println("Sensor tayyor. 5 sekundlik tekshiruv boshlandi...");
  boshlangan = millis();
}

void loop() {
  if (millis() - oxirgi < ORALIQ) return;
  oxirgi = millis();

  sensors_event_t a, g, t;
  mpu.getEvent(&a, &g, &t);
  namunaSoni++;

  Serial.print(a.acceleration.x, 2); Serial.print(",");
  Serial.print(a.acceleration.y, 2); Serial.print(",");
  Serial.println(a.acceleration.z, 2);

  // 5 sekunddan keyin HAQIQIY tezlikni hisoblaymiz
  if (millis() - boshlangan >= 5000) {
    float hz = namunaSoni / 5.0;
    Serial.print("\\n=== Haqiqiy namuna olish tezligi: ");
    Serial.print(hz, 1); Serial.println(" Hz ===");
    if (hz < 90 || hz > 110) {
      Serial.println("OGOHLANTIRISH: tezlik 100 Hz dan uzoq!");
      Serial.println("Ma'lumot yig'ishdan oldin buni tuzatish SHART.");
    } else {
      Serial.println("Tezlik barqaror — ma'lumot yig'ishga tayyor.");
    }
    namunaSoni = 0;
    boshlangan = millis();
  }
}""",
    amaliy="MPU6050 ni ESP32 ga ulab, namuna olish tezligini o'lchash va uni "
           "aniq 100 Hz ga sozlash; Serial ga chiqarishni ataylab sekinlashtirib, "
           "tezlik qanday buzilishini ko'rsatish"),

"AI + IoT: natijani internetga yuborish": K(
    "Model natijasini bulutga yuborish",
    "Model qurilmada ishlaydi, faqat NATIJA (sinf nomi va ishonch) tarmoqqa "
    "yuboriladi — xom ma'lumot emas.",
    """// AI natijasini bulutga yuborish (ma'lumotning O'ZI yuborilmaydi)
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const char* API_KALIT = "SIZNING_WRITE_API_KEY";

const int LED = 2;
const float CHEGARA = 0.70;

unsigned long oxirgiYuborish = 0;
const unsigned long ENG_KAM = 20000;    // bulut chegarasi
String oxirgiSinf = "";

void natijaniYubor(String sinf, float ishonch, int kechikish) {
  if (WiFi.status() != WL_CONNECTED) return;
  if (millis() - oxirgiYuborish < ENG_KAM) return;
  oxirgiYuborish = millis();

  HTTPClient http;
  String url = "http://api.thingspeak.com/update?api_key=" + String(API_KALIT)
             + "&field1=" + String(ishonch, 3)
             + "&field2=" + String(kechikish)
             + "&status=" + sinf;          // FAQAT sinf nomi, xom ma'lumot emas

  http.begin(url);
  int kod = http.GET();
  http.end();

  Serial.print("Yuborildi: "); Serial.print(sinf);
  Serial.print(" ("); Serial.print(ishonch * 100, 1); Serial.print(" %)");
  Serial.print("  javob="); Serial.println(kod);
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println("\\nUlandi. Model natijalari yuboriladi.");
}

void loop() {
  // ... bu yerda run_classifier chaqiriladi va natija olinadi ...
  String sinf = "noaniq";
  float ishonch = 0.0;
  int kechikish = 0;

  if (ishonch >= CHEGARA) {
    digitalWrite(LED, HIGH);
    // FAQAT holat o'zgarganda yuboramiz — trafikni tejaymiz
    if (sinf != oxirgiSinf) {
      oxirgiSinf = sinf;
      natijaniYubor(sinf, ishonch, kechikish);
    }
  } else {
    digitalWrite(LED, LOW);
  }
  delay(200);
}""",
    amaliy="AI modeli yuklangan qurilmani WiFi ga ulab, model natijasini "
           "(sinf nomi va ishonch foizi) bulutga yuborish; xom ovoz yoki "
           "tasvir yuborilmasligini kod bo'yicha ko'rsatib, maxfiylik "
           "afzalligini muhokama qilish"),

"Taqdimot va himoyaga tayyorgarlik": K(
    "Namoyish uchun qurilmani tayyorlash",
    "Taqdimot rejimi: qurilma yoqilishi bilan o'zini ko'rsatadigan holatga "
    "o'tadi va sozlash talab qilmaydi.",
    """// TAQDIMOT REJIMI: yoqilishi bilan o'zini ko'rsatadi
const int LED_YASHIL = 7, LED_QIZIL = 8, ZUMMER = 9;
const int SENSOR = A0, TUGMA = 2;

bool namoyishRejimi = true;

void salomlash() {
  // qurilma tayyorligini bildiruvchi ketma-ketlik
  for (int i = 0; i < 3; i++) {
    digitalWrite(LED_YASHIL, HIGH); tone(ZUMMER, 1200 + i * 300, 120);
    delay(180);
    digitalWrite(LED_YASHIL, LOW);
    delay(120);
  }
}

void oziniSinash() {
  Serial.println("=== O'ZINI SINASH ===");
  int q = analogRead(SENSOR);
  Serial.print("Sensor: "); Serial.println(q);

  bool ok = (q > 10 && q < 1010);
  digitalWrite(LED_YASHIL, ok);
  digitalWrite(LED_QIZIL, !ok);

  Serial.println(ok ? "Qurilma TAYYOR" : "XATO: sensorni tekshiring!");
  delay(1500);
  digitalWrite(LED_YASHIL, LOW); digitalWrite(LED_QIZIL, LOW);
}

void setup() {
  pinMode(LED_YASHIL, OUTPUT); pinMode(LED_QIZIL, OUTPUT);
  pinMode(ZUMMER, OUTPUT); pinMode(TUGMA, INPUT_PULLUP);
  Serial.begin(9600);

  salomlash();         // 1) tayyorligini bildiradi
  oziniSinash();       // 2) o'zini tekshiradi
}

void loop() {
  int q = analogRead(SENSOR);
  bool ishlagan = (q > 500);

  digitalWrite(LED_YASHIL, !ishlagan);
  digitalWrite(LED_QIZIL, ishlagan);
  if (ishlagan) tone(ZUMMER, 2000, 100);

  // Tugma — namoyish uchun qo'lda ishga tushirish
  if (digitalRead(TUGMA) == LOW) {
    Serial.println("Qo'lda ishga tushirildi (namoyish uchun)");
    tone(ZUMMER, 2500, 400);
    delay(600);
  }
  delay(200);
}""",
    amaliy="Loyiha qurilmasiga taqdimot rejimini qo'shish: yoqilganda "
           "salomlashish ketma-ketligi, o'zini sinash va qo'lda ishga tushirish "
           "tugmasi; namoyishni uch marta mashq qilib, sekundomer bilan "
           "vaqtini o'lchash"),

}
