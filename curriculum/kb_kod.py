# -*- coding: utf-8 -*-
"""
DASTURLASH MAVZULARI uchun kod bazasi.

pasport.py komponentga bog'langan darslarni qoplaydi. Bu yerda esa
komponentsiz "sof dasturlash" mavzulari bor: o'zgaruvchi, sikl, funksiya,
WiFi, MQTT, model o'rgatish va h.k.

Har bir yozuvda:
    nom     — kod namunasining nomi
    izoh    — kod nima qilishi, bir gapda
    kod     — to'liq, yuklasa ishlaydigan sketch
    amaliy  — AGAR berilgan bo'lsa, sillabusdagi amaliy ish shu bilan
              ALMASHTIRILADI. Maqsad: "sof nazariya" darsi qolmasin,
              har bir tushuncha TEMIR ustida ko'rsatilsin.

Kalit — sillabusdagi mavzu satri (kb_kalit bilan bir xil).
"""


def K(nom, izoh, kod, amaliy=None):
    return {"nom": nom, "izoh": izoh, "kod": kod, "amaliy": amaliy}


KODLAR = {

# ==================================================== ARDUINO — ILK QADAMLAR
"Arduino IDE va platani ulash": K(
    "Plata ulanganini tekshiruvchi eng qisqa dastur",
    "Platani ulagach birinchi tekshiruv: platadagi L diodi (D13) miltillasa, "
    "port va drayver to'g'ri ishlayapti.",
    """// Ulanish tekshiruvi — hech qanday sim kerak emas.
// Platadagi "L" yozuvli diod D13 pinga ulangan.

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);     // = D13
  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("YONDI");
  delay(300);

  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("o'chdi");
  delay(300);
}""",
    amaliy="Platani ulab, ichki D13 diodini miltillatish va Serial monitorda "
           "yozuv chiqishiga erishish, keyin tashqi LEDni 220 Om bilan ulab, "
           "ikkalasini bir vaqtda ishlatish"),

"Arduino platasi va IDE": K(
    "Plata ulanganini tekshiruvchi eng qisqa dastur",
    "Birinchi darsda maqsad — zanjir emas, ALOQA: kompyuter platani ko'ryaptimi.",
    """// Birinchi dastur: ichki diod + Serial aloqa
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Salom! Plata ishlayapti.");
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); delay(500);
  digitalWrite(LED_BUILTIN, LOW);  delay(500);
  Serial.println("bir sikl tugadi");
}""",
    amaliy="Platani kompyuterga ulab, drayver va portni sozlash, ichki diodni "
           "miltillatish va tashqi LEDni D9 ga ulab tekshirish"),

"Arduino Uno platasi: pinlar xaritasi": K(
    "Har bir pin turini sinab ko'ruvchi dastur",
    "Raqamli, PWM va analog pinlar farqini bitta dasturda yonma-yon ko'rsatadi.",
    """// Pin turlarini yonma-yon sinash
// D7  — oddiy raqamli chiqish (faqat yoq/o'chir)
// D9  — PWM chiqish (~ belgisi bor: yorqinlikni o'zgartiradi)
// A0  — analog kirish (0..1023 o'qiydi)

const int ODDIY = 7, PWM_PIN = 9, ANALOG = A0;

void setup() {
  pinMode(ODDIY, OUTPUT);
  pinMode(PWM_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("D7 = oddiy | D9 = PWM | A0 = analog");
}

void loop() {
  // 1) oddiy pin: faqat ikki holat
  digitalWrite(ODDIY, HIGH); delay(400);
  digitalWrite(ODDIY, LOW);  delay(400);

  // 2) PWM pin: oraliq qiymatlar
  for (int y = 0; y <= 255; y += 51) {
    analogWrite(PWM_PIN, y);
    Serial.print("PWM = "); Serial.println(y);
    delay(300);
  }

  // 3) analog kirish
  Serial.print("A0 o'qidi: "); Serial.println(analogRead(ANALOG));
  delay(500);
}""",
    amaliy="D7 ga oddiy LED, D9 ga PWM LED va A0 ga potensiometr ulab, uch xil "
           "pinning farqini bir sxemada ko'rish va pin xaritasini daftarga chizish"),

"pinMode va digitalWrite": K(
    "Kirish va chiqish pinlari bitta sxemada",
    "pinMode pinni KIRISH yoki CHIQISH qilib belgilaydi; digitalWrite faqat "
    "CHIQISH pinida ma'noga ega.",
    """// pinMode: pin nima qilishini oldindan aytamiz
const int LED = 9;        // CHIQISH: plata bu pinga kuchlanish beradi
const int TUGMA = 2;      // KIRISH:  plata bu pinni o'qiydi

void setup() {
  pinMode(LED, OUTPUT);            // chiqish
  pinMode(TUGMA, INPUT_PULLUP);    // kirish + ichki tortuvchi rezistor
  Serial.begin(9600);
}

void loop() {
  int holat = digitalRead(TUGMA);      // KIRISHNI o'qiymiz

  // INPUT_PULLUP da: bosilgan = LOW
  if (holat == LOW) {
    digitalWrite(LED, HIGH);           // CHIQISHGA yozamiz
    Serial.println("bosildi -> LED yoniq");
  } else {
    digitalWrite(LED, LOW);
  }
  delay(50);
}""",
    amaliy="D9 ga LED (220 Om bilan), D2 ga tugma ulab, pinMode ni ataylab "
           "noto'g'ri qo'yib ko'rish va nima uchun ishlamasligini tushuntirish"),

"pinMode, digitalWrite, delay": K(
    "Uchta asosiy buyruq bitta sxemada",
    "Bu uchtasi Arduino dasturlarining 80 % ini tashkil qiladi.",
    """// Uchta asosiy buyruq: pinMode, digitalWrite, delay
const int QIZIL = 7, SARIQ = 8, YASHIL = 9;   // svetofor

void setup() {
  pinMode(QIZIL, OUTPUT);
  pinMode(SARIQ, OUTPUT);
  pinMode(YASHIL, OUTPUT);
}

void loop() {
  digitalWrite(QIZIL, HIGH);  delay(4000);    // 4 sekund qizil
  digitalWrite(SARIQ, HIGH);  delay(1000);    // qizil+sariq
  digitalWrite(QIZIL, LOW);
  digitalWrite(SARIQ, LOW);

  digitalWrite(YASHIL, HIGH); delay(4000);    // 4 sekund yashil
  digitalWrite(YASHIL, LOW);

  digitalWrite(SARIQ, HIGH);  delay(1000);    // sariq
  digitalWrite(SARIQ, LOW);
}""",
    amaliy="Uchta LEDdan svetofor yig'ib, haqiqiy svetofor tartibida "
           "ishlatish va vaqtlarni o'zgartirib natijani kuzatish"),

"Blink: birinchi dastur": K(
    "Blink va uni sekinlashtirish/tezlashtirish",
    "Birinchi dastur — lekin uni O'ZGARTIRIB ko'rish o'rganishning asosi.",
    """// Blink — va uni o'zgartirib sinash
const int LED = 9;
int kutish = 500;          // shu sonni o'zgartirib ko'ring

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(kutish);
  digitalWrite(LED, LOW);
  delay(kutish);

  // TAJRIBA: kutish qiymatini asta kamaytiramiz
  kutish = kutish - 20;
  if (kutish < 20) kutish = 500;      // yana boshidan

  Serial.print("kutish = "); Serial.println(kutish);
  // 30 ms dan pastda ko'z miltillashni ilg'amay qoladi — LED xira yonadi
}""",
    amaliy="LEDni 220 Om rezistor bilan yig'ib, kechikishni 500 dan 10 ms gacha "
           "kamaytirib borish va ko'z qaysi qiymatdan boshlab miltillashni "
           "ilg'amay qolishini aniqlash"),

"Blink va dastur tuzilishi": K(
    "setup va loop farqi bitta sxemada ko'rinadi",
    "setup bir marta, loop cheksiz — buni Serial monitorda ko'z bilan ko'rish mumkin.",
    """// setup BIR MARTA, loop CHEKSIZ ishlaydi
const int LED = 9;
int sanoq = 0;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== SETUP ishga tushdi (faqat bir marta) ===");

  // isbot: setup da uch marta miltillatamiz
  for (int i = 0; i < 3; i++) {
    digitalWrite(LED, HIGH); delay(120);
    digitalWrite(LED, LOW);  delay(120);
  }
}

void loop() {
  sanoq++;
  Serial.print("loop ");
  Serial.print(sanoq);
  Serial.println("-marta bajarildi");

  digitalWrite(LED, HIGH); delay(400);
  digitalWrite(LED, LOW);  delay(400);
  // RESET tugmasini bosing — sanoq qaytadan 1 dan boshlanadi
}""",
    amaliy="LEDni ulab, setup ichida uch marta tez miltillatib, keyin loopda "
           "sekin miltillashini ko'rish; RESET bosib setup qayta ishga "
           "tushishini kuzatish"),

"Dastur tuzilishi: setup() va loop()": K(
    "setup va loop farqini ko'rsatuvchi tajriba",
    "Bir xil kod setup va loop ichida butunlay boshqacha natija beradi.",
    """// AYNI kod ikki joyda — natija boshqacha
const int LED = 9, ZUMMER = 8;
int sanoq = 0;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);

  // SETUP ichida: bir marta salom signali
  tone(ZUMMER, 1200, 200);
  Serial.println("Qurilma yoqildi (bu yozuv BIR MARTA chiqadi)");
  delay(500);
}

void loop() {
  // LOOP ichida: bu qism to'xtovsiz takrorlanadi
  sanoq++;
  Serial.print("takrorlanish: "); Serial.println(sanoq);

  digitalWrite(LED, HIGH); delay(300);
  digitalWrite(LED, LOW);  delay(300);

  // Har 10-takrorlanishda signal
  if (sanoq % 10 == 0) tone(ZUMMER, 1800, 150);
}""",
    amaliy="LED va zummer yig'ib, salomlashish signalini setup ga, miltillashni "
           "loop ga joylash; keyin ikkalasini almashtirib, natija qanday "
           "o'zgarishini kuzatish"),

"delay() va vaqt boshqaruvi": K(
    "delay() va uning kamchiligi — millis() bilan solishtirish",
    "delay ishlaganda plata BOSHQA HECH NARSA qila olmaydi. Buni tugma bilan "
    "isbotlash mumkin.",
    """// delay() ning kamchiligini KO'RSATUVCHI tajriba
const int LED1 = 9, LED2 = 10, TUGMA = 2;
unsigned long oxirgi = 0;

void setup() {
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT);
  pinMode(TUGMA, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // --- 1) delay bilan: 2 sekund davomida tugma SEZILMAYDI ---
  digitalWrite(LED1, HIGH);
  delay(2000);                    // plata shu yerda "muzlab" turadi
  digitalWrite(LED1, LOW);
  delay(2000);

  // --- 2) millis bilan: plata bo'sh qolmaydi ---
  if (millis() - oxirgi >= 500) {
    oxirgi = millis();
    digitalWrite(LED2, !digitalRead(LED2));
  }

  // Tugmani delay ishlayotgan paytda bosib ko'ring — sezilmaydi.
  if (digitalRead(TUGMA) == LOW) Serial.println("TUGMA BOSILDI");
}""",
    amaliy="Ikki LED va tugma yig'ib, delay ishlayotgan paytda tugma bosilishi "
           "sezilmasligini tajribada isbotlash, keyin millis() ga o'tkazib "
           "farqni ko'rish"),

# ==================================================== O'ZGARUVCHI VA TURLAR
"O'zgaruvchi (variable) tushunchasi": K(
    "O'zgaruvchisiz va o'zgaruvchi bilan yozilgan kod",
    "O'zgaruvchining foydasi: qiymatni BIR joyda o'zgartirsangiz butun dastur "
    "o'zgaradi.",
    """// O'zgaruvchining foydasi — potensiometr bilan jonli ko'rinadi
const int LED = 9;
const int POT = A0;

int tezlik = 500;          // O'ZGARUVCHI: bitta joydan boshqaramiz

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // potensiometr o'zgaruvchining qiymatini jonli o'zgartiradi
  tezlik = map(analogRead(POT), 0, 1023, 50, 1000);

  digitalWrite(LED, HIGH); delay(tezlik);
  digitalWrite(LED, LOW);  delay(tezlik);

  Serial.print("tezlik o'zgaruvchisi = "); Serial.println(tezlik);

  // TAJRIBA: agar o'zgaruvchi bo'lmasa, delay(500) ni 4 joyda
  // qo'lda o'zgartirish kerak bo'lardi va bittasi esdan chiqardi.
}""",
    amaliy="LED va potensiometr yig'ib, miltillash tezligini o'zgaruvchi orqali "
           "boshqarish; keyin o'zgaruvchini olib tashlab, qiymatni har joyda "
           "qo'lda o'zgartirishga urinib, farqni his qilish"),

"Ma'lumot turlari: int, float, bool": K(
    "Har bir tur uchun alohida TEMIR namoyish",
    "int — sanoq, float — o'lchov, bool — holat, long — vaqt, byte — xotira. "
    "Har biri o'z sxemasida ko'rsatiladi.",
    """// Har bir tur qayerda kerakligini TEMIRDA ko'rsatamiz
const int POT = A0, TUGMA = 2, LED = 9;

int   bosishSoni = 0;        // int   — SANOQ (butun son)
float kuchlanish = 0.0;      // float — O'LCHOV (kasrli)
bool  yongan     = false;    // bool  — HOLAT (yoq/o'chiq)
long  ishVaqti   = 0;        // long  — millis() uchun (int ga sig'maydi)
byte  yorqinlik  = 0;        // byte  — 0..255, PWM uchun aynan mos

void setup() {
  pinMode(TUGMA, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // float: analog qiymatni voltga aylantirish — bu yerda int ishlamaydi
  int xom = analogRead(POT);
  kuchlanish = xom * 5.0 / 1023.0;

  // byte: PWM uchun aynan 0..255 kerak
  yorqinlik = map(xom, 0, 1023, 0, 255);
  analogWrite(LED, yorqinlik);

  // bool + int: tugma holati va bosishlar soni
  if (digitalRead(TUGMA) == LOW) {
    bosishSoni++;
    yongan = !yongan;
    delay(200);
  }

  // long: millis() 50 kundan keyin ham to'lib ketmaydi, int esa 33 sekundda to'ladi
  ishVaqti = millis() / 1000;

  Serial.print("int bosish=");   Serial.print(bosishSoni);
  Serial.print("  float U=");    Serial.print(kuchlanish, 2); Serial.print(" V");
  Serial.print("  byte PWM=");   Serial.print(yorqinlik);
  Serial.print("  bool=");       Serial.print(yongan ? "true" : "false");
  Serial.print("  long vaqt=");  Serial.print(ishVaqti); Serial.println(" s");

  // TAJRIBA — int ning to'lib ketishi (overflow):
  // int kichik = 32767;  kichik = kichik + 1;   -> natija -32768 bo'ladi!
  delay(300);
}""",
    amaliy="Potensiometr, tugma va LED yig'ib, bitta sxemada beshta turni birga "
           "ishlatish: float bilan kuchlanishni voltda chiqarish, byte bilan "
           "yorqinlikni boshqarish, int bilan bosishlarni sanash va int ning "
           "32767 da to'lib ketishini Serial monitorda ko'rsatish"),

"O'zgaruvchi va ma'lumot turlari": K(
    "Turlar va ular egallaydigan xotira",
    "Turlarning xotira sarfini o'lchab, nima uchun \"hamma joyda float\" "
    "yomon fikr ekanini ko'rsatadi.",
    """// Turlar va XOTIRA sarfi — sizeof bilan o'lchaymiz
const int POT = A0, LED = 9;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);

  Serial.println("Tur      | bayt | oralig'i");
  Serial.println("---------|------|------------------------");
  Serial.print("bool     |  ");  Serial.print(sizeof(bool));   Serial.println("   | true / false");
  Serial.print("byte     |  ");  Serial.print(sizeof(byte));   Serial.println("   | 0 .. 255");
  Serial.print("int      |  ");  Serial.print(sizeof(int));    Serial.println("   | -32768 .. 32767");
  Serial.print("long     |  ");  Serial.print(sizeof(long));   Serial.println("   | +-2 mlrd");
  Serial.print("float    |  ");  Serial.print(sizeof(float));  Serial.println("   | kasrli, 6-7 raqam");

  // TO'LIB KETISHNI ko'rsatamiz
  int chegara = 32767;
  Serial.print("32767 + 1 = ");
  Serial.println(chegara + 1);        // -32768 chiqadi!
}

void loop() {
  int xom = analogRead(POT);

  // float sekin hisoblanadi — buni o'lchab ko'ramiz
  unsigned long t1 = micros();
  float f = xom * 5.0 / 1023.0;
  unsigned long floatVaqt = micros() - t1;

  t1 = micros();
  int i = xom * 5 / 1023;
  unsigned long intVaqt = micros() - t1;

  analogWrite(LED, map(xom, 0, 1023, 0, 255));

  Serial.print("float natija="); Serial.print(f, 3);
  Serial.print(" (");            Serial.print(floatVaqt); Serial.print(" mkrs)   ");
  Serial.print("int natija=");   Serial.print(i);
  Serial.print(" (");            Serial.print(intVaqt);   Serial.println(" mkrs)");
  delay(500);
}""",
    amaliy="Potensiometr va LED yig'ib, sizeof bilan har bir turning xotira "
           "sarfini o'lchash, int ning to'lib ketishini ko'rsatish va float "
           "bilan int hisoblash tezligini micros() bilan solishtirish"),

"Arifmetik amallar": K(
    "Butun va kasrli bo'lish farqi — o'lchovda ko'rinadi",
    "5/2 = 2, lekin 5.0/2 = 2.5. Bu farq sensor qiymatini voltga "
    "aylantirganda darhol sezilib qoladi.",
    """// Arifmetika: eng ko'p uchraydigan xato — BUTUN BO'LISH
const int POT = A0, LED = 9;

void setup() { pinMode(LED, OUTPUT); Serial.begin(9600); }

void loop() {
  int xom = analogRead(POT);       // 0..1023

  // XATO: hammasi butun son -> natija ham butun, kasr yo'qoladi
  int xato = xom * 5 / 1023;

  // TO'G'RI: bittasi kasrli bo'lsa yetadi (5.0)
  float togri = xom * 5.0 / 1023.0;

  // Foizga aylantirish
  int foiz = map(xom, 0, 1023, 0, 100);

  // Qoldiqli bo'lish (%) — har 10-qadamda signal berish uchun qulay
  if (foiz % 10 == 0) digitalWrite(LED, HIGH);
  else                digitalWrite(LED, LOW);

  Serial.print("xom=");        Serial.print(xom);
  Serial.print("  XATO(int)="); Serial.print(xato);
  Serial.print("  TO'G'RI=");   Serial.print(togri, 3);
  Serial.print(" V  foiz=");    Serial.print(foiz); Serial.println(" %");
  delay(300);
}""",
    amaliy="Potensiometrni ulab, kuchlanishni avval butun sonlar bilan, keyin "
           "kasrli sonlar bilan hisoblab, multimetr ko'rsatkichi bilan "
           "solishtirish va qaysi biri to'g'ri ekanini aniqlash"),

# ==================================================== SHART VA MANTIQ
"if sharti": K(
    "Yorug'lik chegarasidan o'tganda chiroq yonadi",
    "if — dasturga qaror qabul qilishni o'rgatadigan birinchi konstruksiya.",
    """// if — shartga qarab qaror
const int LDR = A0, LED = 9;
const int CHEGARA = 400;

void setup() { pinMode(LED, OUTPUT); Serial.begin(9600); }

void loop() {
  int yoruglik = analogRead(LDR);

  if (yoruglik < CHEGARA) {          // qorong'i bo'lsa
    digitalWrite(LED, HIGH);
    Serial.print("QORONG'I -> chiroq yondi   ");
  } else {                            // aks holda
    digitalWrite(LED, LOW);
    Serial.print("yorug'            ");
  }

  Serial.print("qiymat="); Serial.println(yoruglik);
  delay(200);
}""",
    amaliy="Fotorezistorni 10 kOm bilan bo'luvchi qilib ulab, chegarani "
           "tajriba yo'li bilan topish va qo'l bilan yopganda chiroq yonishiga "
           "erishish"),

"if / else if / else": K(
    "Uch bosqichli yorug'lik indikatori",
    "else if bilan bir nechta oraliqni ajratish mumkin — birinchi mos kelgan "
    "shart bajariladi, qolganlari TEKSHIRILMAYDI.",
    """// if / else if / else — uch oraliq, uch LED
const int LDR = A0;
const int YASHIL = 7, SARIQ = 8, QIZIL = 9;

void setup() {
  pinMode(YASHIL, OUTPUT); pinMode(SARIQ, OUTPUT); pinMode(QIZIL, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int q = analogRead(LDR);

  digitalWrite(YASHIL, LOW); digitalWrite(SARIQ, LOW); digitalWrite(QIZIL, LOW);

  // TARTIB MUHIM: birinchi to'g'ri kelgan shart ishlaydi
  if (q > 700) {
    digitalWrite(YASHIL, HIGH);
    Serial.print("juda yorug'  ");
  } else if (q > 400) {
    digitalWrite(SARIQ, HIGH);
    Serial.print("o'rtacha     ");
  } else {
    digitalWrite(QIZIL, HIGH);
    Serial.print("qorong'i     ");
  }

  Serial.print("qiymat="); Serial.println(q);
  delay(250);
}""",
    amaliy="Fotorezistor va uchta LED yig'ib, yorug'likni uch darajaga ajratish; "
           "shartlar tartibini ataylab buzib, nima uchun natija noto'g'ri "
           "chiqishini tushuntirish"),

"else va else if": K(
    "Harorat bo'yicha uch rejimli boshqaruv",
    "else — qolgan HAMMA holat uchun. Uni oxirida qoldirish odat bo'lishi kerak.",
    """// else if — harorat bo'yicha rejim tanlash
const int SENSOR = A0;
const int ISITGICH = 7, VENTILYATOR = 8, YASHIL = 9;

void setup() {
  pinMode(ISITGICH, OUTPUT); pinMode(VENTILYATOR, OUTPUT); pinMode(YASHIL, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int t = map(analogRead(SENSOR), 0, 1023, 0, 50);   // taxminiy gradus

  digitalWrite(ISITGICH, LOW); digitalWrite(VENTILYATOR, LOW); digitalWrite(YASHIL, LOW);

  if (t < 18) {
    digitalWrite(ISITGICH, HIGH);
    Serial.print("SOVUQ -> isitgich   ");
  } else if (t > 26) {
    digitalWrite(VENTILYATOR, HIGH);
    Serial.print("ISSIQ -> ventilyator");
  } else {
    digitalWrite(YASHIL, HIGH);           // qolgan hamma holat
    Serial.print("NORMAL              ");
  }

  Serial.print("  t="); Serial.print(t); Serial.println(" C");
  delay(400);
}""",
    amaliy="Termistorli bo'luvchi va uch LED yig'ib, sovuq/normal/issiq "
           "rejimlarini qo'l bilan isitib va sovutib sinash"),

"Ikki shartni birlashtirish (VA / YOKI)": K(
    "Ikki sensor birga qaror qabul qiladi",
    "&& — ikkalasi ham bajarilishi kerak. || — bittasi yetadi.",
    """// && (VA) va || (YOKI) — ikki sensordan aqlli qaror
const int LDR = A0, PIR = 2;
const int CHIROQ = 9, ZUMMER = 8;

void setup() {
  pinMode(PIR, INPUT);
  pinMode(CHIROQ, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  bool qorongi = (analogRead(LDR) < 400);
  bool harakat = (digitalRead(PIR) == HIGH);

  // VA: chiroq FAQAT qorong'i BO'LSA VA harakat BO'LSA yonadi
  if (qorongi && harakat) {
    digitalWrite(CHIROQ, HIGH);
    Serial.println("qorong'i VA harakat -> chiroq yondi");
  } else {
    digitalWrite(CHIROQ, LOW);
  }

  // YOKI: signal ikki sababdan bittasi bo'lsa ham chiqadi
  if (harakat || !qorongi) {
    // ... kuzatuv yozuvi
  }

  Serial.print("qorong'i="); Serial.print(qorongi);
  Serial.print("  harakat="); Serial.println(harakat);
  delay(300);
}""",
    amaliy="Fotorezistor va PIR datchigini birga ulab, chiroq faqat qorong'ida "
           "VA harakat bo'lganda yonadigan tizim yig'ish; keyin && ni || ga "
           "almashtirib, xatti-harakat qanday o'zgarishini kuzatish"),

"Mantiqiy amallar: && || !": K(
    "Uch mantiqiy amal bitta xavfsizlik tizimida",
    "! (EMAS) shartni teskariga aylantiradi.",
    """// &&, ||, ! — xavfsizlik tizimi mantiqi
const int ESHIK = 2, HARAKAT = 3, KALIT = 4;
const int SIGNAL = 8, LED = 9;

void setup() {
  pinMode(ESHIK, INPUT_PULLUP);
  pinMode(HARAKAT, INPUT);
  pinMode(KALIT, INPUT_PULLUP);
  pinMode(SIGNAL, OUTPUT); pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  bool eshikOchiq = (digitalRead(ESHIK) == HIGH);
  bool harakatBor = (digitalRead(HARAKAT) == HIGH);
  bool qorovulYoq = !(digitalRead(KALIT) == LOW);    // ! = EMAS

  // Signal: qorovul YO'Q bo'lsa VA (eshik ochiq YOKI harakat bor)
  bool xavf = qorovulYoq && (eshikOchiq || harakatBor);

  digitalWrite(LED, xavf);
  if (xavf) tone(SIGNAL, 2200, 200);

  Serial.print("eshik=");   Serial.print(eshikOchiq);
  Serial.print(" harakat="); Serial.print(harakatBor);
  Serial.print(" rejim=");   Serial.print(qorovulYoq ? "qo'riqlash" : "o'chiq");
  Serial.print(" -> xavf="); Serial.println(xavf);
  delay(300);
}""",
    amaliy="Tugma (eshik), PIR (harakat) va kalit (rejim) ulab, uch mantiqiy "
           "amaldan foydalanadigan signalizatsiya yig'ish va rostlik jadvalini "
           "amalda to'ldirish"),

"Mantiqiy amallar: VA, YOKI, EMAS": K(
    "Rostlik jadvalini LED bilan ko'rsatish",
    "Ikki tugma — to'rtta kombinatsiya. Har biri uchun natija LEDda ko'rinadi.",
    """// Rostlik jadvalini TEMIRDA ko'rsatish
const int A_TUGMA = 2, B_TUGMA = 3;
const int LED_VA = 7, LED_YOKI = 8, LED_EMAS = 9;

void setup() {
  pinMode(A_TUGMA, INPUT_PULLUP); pinMode(B_TUGMA, INPUT_PULLUP);
  pinMode(LED_VA, OUTPUT); pinMode(LED_YOKI, OUTPUT); pinMode(LED_EMAS, OUTPUT);
  Serial.begin(9600);
  Serial.println("A  B | VA  YOKI  EMAS(A)");
}

void loop() {
  bool a = (digitalRead(A_TUGMA) == LOW);    // bosilgan = rost
  bool b = (digitalRead(B_TUGMA) == LOW);

  digitalWrite(LED_VA,   a && b);
  digitalWrite(LED_YOKI, a || b);
  digitalWrite(LED_EMAS, !a);

  Serial.print(a); Serial.print("  "); Serial.print(b);
  Serial.print(" |  "); Serial.print(a && b);
  Serial.print("    ");  Serial.print(a || b);
  Serial.print("     ");  Serial.println(!a);
  delay(250);
}""",
    amaliy="Ikkita tugma va uchta LED yig'ib, VA/YOKI/EMAS rostlik jadvalining "
           "to'rtta qatorini qo'l bilan bosib chiqib, daftarga to'ldirish"),

"Shart (agar ... bo'lsa) blogi": K(
    "Blokli muhitda shart — matnli kod bilan yonma-yon",
    "mBlock blogi va Arduino kodi bir xil ishni bajaradi. Ikkalasini yonma-yon "
    "ko'rsatish o'tishni osonlashtiradi.",
    """// Blokli dasturdagi "agar ... bo'lsa" blogining matnli ko'rinishi
const int DATCHIK = A0, LED = 9;

void setup() { pinMode(LED, OUTPUT); Serial.begin(9600); }

void loop() {
  int q = analogRead(DATCHIK);

  // BLOK:  agar <datchik < 400> bo'lsa
  //            <LEDni yoq>
  if (q < 400) {
    digitalWrite(LED, HIGH);
  }

  Serial.println(q);
  delay(200);
}""",
    amaliy="Fotorezistor va LEDni ulab, avval mBlock'da shart blogi bilan, "
           "keyin AYNI vazifani matnli kod bilan bajarish va ikki yechimni "
           "yonma-yon solishtirish"),

"Aks holda (else) blogi": K(
    "Ikki holat uchun ikki javob",
    "else blogi — \"qolgan hamma holat\". Usiz chiroq bir marta yonib, "
    "hech qachon o'chmaydi.",
    """// else blogi: yoqish VA o'chirish
const int DATCHIK = A0, LED = 9, ZUMMER = 8;

void setup() { pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT); Serial.begin(9600); }

void loop() {
  int q = analogRead(DATCHIK);

  if (q < 400) {
    digitalWrite(LED, HIGH);
    tone(ZUMMER, 1000, 80);
    Serial.println("qorong'i -> yoqildi");
  } else {
    digitalWrite(LED, LOW);        // ELSE bo'lmasa LED hech qachon o'chmaydi
    Serial.println("yorug'   -> o'chirildi");
  }
  delay(250);
}""",
    amaliy="Fotorezistor va LEDni ulab, avval else'siz yozib, chiroq bir marta "
           "yonib o'chmay qolishini ko'rish, keyin else qo'shib tuzatish"),

# ==================================================== SIKLLAR
"for sikli": K(
    "Yuguruvchi olov — sikl bilan va siklsiz",
    "Beshta LED uchun 20 qator kod bitta sikl bilan 3 qatorga tushadi.",
    """// for sikli — yuguruvchi olov
const int LED[5] = {5, 6, 7, 8, 9};

void setup() {
  // sikl bilan pinlarni bir zumda sozlaymiz
  for (int i = 0; i < 5; i++) pinMode(LED[i], OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // oldinga
  for (int i = 0; i < 5; i++) {
    digitalWrite(LED[i], HIGH);
    delay(120);
    digitalWrite(LED[i], LOW);
  }
  // orqaga: i-- bilan teskari sikl
  for (int i = 4; i >= 0; i--) {
    digitalWrite(LED[i], HIGH);
    delay(120);
    digitalWrite(LED[i], LOW);
  }

  // SIKLSIZ bu 20 qator bo'lardi:
  //   digitalWrite(5,HIGH); delay(120); digitalWrite(5,LOW);
  //   digitalWrite(6,HIGH); delay(120); digitalWrite(6,LOW);  ... va h.k.
}""",
    amaliy="Beshta LEDni ketma-ket ulab, avval siklsiz (20 qator) yuguruvchi "
           "olov yozish, keyin for sikliga o'tkazib, ikki kodning uzunligini "
           "solishtirish"),

"while sikli": K(
    "Shart bajarilguncha kutish — tugma bosilishini kutish",
    "for oldindan necha marta ekanini biladi, while esa BILMAYDI — u shartga "
    "qarab ishlaydi.",
    """// while — necha marta ekani oldindan noma'lum
const int TUGMA = 2, LED = 9, POT = A0;

void setup() {
  pinMode(TUGMA, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.println("Boshlash uchun tugmani bosing...");

  // tugma bosilmaguncha KUTAMIZ — necha marta aylanishi noma'lum
  while (digitalRead(TUGMA) == HIGH) {
    digitalWrite(LED, (millis() / 300) % 2);   // kutayotganini bildiramiz
  }

  Serial.println("Boshlandi!");

  // potensiometr chegaradan oshguncha ishlaymiz
  while (analogRead(POT) < 800) {
    digitalWrite(LED, HIGH); delay(100);
    digitalWrite(LED, LOW);  delay(100);
    Serial.print("pot="); Serial.println(analogRead(POT));
  }

  Serial.println("Chegaraga yetdi — to'xtadi.");
  digitalWrite(LED, LOW);
  delay(1000);
}""",
    amaliy="Tugma, potensiometr va LED yig'ib, tugma bosilishini while bilan "
           "kutish, keyin potensiometr chegaradan oshguncha miltillatish; for "
           "bilan buni yozib bo'lmasligini muhokama qilish"),

"for va while sikllari": K(
    "Bir xil vazifa — ikki sikl",
    "for: takrorlanish soni MA'LUM. while: shart bilan boshqariladi.",
    """// Bir xil vazifani ikki xil sikl bilan bajaramiz
const int LED = 9, POT = A0, TUGMA = 2;

void setup() {
  pinMode(LED, OUTPUT); pinMode(TUGMA, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // --- FOR: aniq 5 marta miltillatish ---
  Serial.println("for: aniq 5 marta");
  for (int i = 1; i <= 5; i++) {
    digitalWrite(LED, HIGH); delay(200);
    digitalWrite(LED, LOW);  delay(200);
    Serial.print("  "); Serial.println(i);
  }
  delay(800);

  // --- WHILE: qorong'i bo'lguncha (necha marta — noma'lum) ---
  Serial.println("while: yorug' bo'lguncha");
  int n = 0;
  while (analogRead(POT) < 500) {
    digitalWrite(LED, HIGH); delay(150);
    digitalWrite(LED, LOW);  delay(150);
    n++;
    if (n > 100) break;          // cheksiz siklga qarshi himoya
  }
  Serial.print("  jami "); Serial.print(n); Serial.println(" marta");
  delay(1000);
}""",
    amaliy="LED va potensiometr yig'ib, ayni vazifani avval for, keyin while "
           "bilan bajarib, qaysi holatda qaysi biri qulayligini jadvalga yozish"),

"Takrorlash (sikl) blogi": K(
    "Blokli muhitdagi takrorlash — matnli ko'rinishi",
    "Takrorlash blogi kodni qisqartiradi va xatoni kamaytiradi.",
    """// "10 marta takrorla" blogining matnli ko'rinishi
const int LED = 9, ZUMMER = 8;

void setup() { pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT); }

void loop() {
  // BLOK:  <10 marta takrorla>
  //            <LEDni yoq> <0.2 s kut> <LEDni o'chir> <0.2 s kut>
  for (int i = 0; i < 10; i++) {
    digitalWrite(LED, HIGH); delay(200);
    digitalWrite(LED, LOW);  delay(200);
  }

  tone(ZUMMER, 1500, 300);      // sikl tugaganini bildiradi
  delay(1500);
}""",
    amaliy="LED va zummerni ulab, mBlock'da takrorlash blogi bilan miltillash "
           "dasturini qisqartirish, keyin ayni natijani matnli for sikli bilan "
           "olish"),

"Massiv bilan tanishuv": K(
    "Beshta LED — bitta massiv",
    "Massiv — bir turdagi qiymatlarni bitta nom ostida saqlash. Indeks 0 dan "
    "boshlanadi.",
    """// Massiv: beshta pinni bitta nom bilan boshqaramiz
const int LED[5] = {5, 6, 7, 8, 9};      // indeks: 0 1 2 3 4
const int SONI = 5;

void setup() {
  for (int i = 0; i < SONI; i++) pinMode(LED[i], OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // 1) hammasini yoqish
  for (int i = 0; i < SONI; i++) digitalWrite(LED[i], HIGH);
  delay(500);

  // 2) hammasini o'chirish
  for (int i = 0; i < SONI; i++) digitalWrite(LED[i], LOW);
  delay(500);

  // 3) faqat juft indekslilarni yoqish
  for (int i = 0; i < SONI; i += 2) {
    digitalWrite(LED[i], HIGH);
    Serial.print("LED["); Serial.print(i); Serial.print("] = pin ");
    Serial.println(LED[i]);
  }
  delay(700);
  for (int i = 0; i < SONI; i++) digitalWrite(LED[i], LOW);
  delay(500);

  // DIQQAT: LED[5] YO'Q — indeks 0 dan 4 gacha. LED[5] xotiraning
  // begona joyiga murojaat qiladi va dastur g'alati ishlaydi.
}""",
    amaliy="Beshta LEDni ulab, pin raqamlarini massivga yig'ish va sikl bilan "
           "boshqarish; LED[5] ga murojaat qilib, chegaradan chiqish qanday "
           "natija berishini ko'rish"),

"Massiv (array) bilan ishlash": K(
    "O'lchov tarixini massivda saqlash va o'rtacha topish",
    "Massiv nafaqat pinlarni, o'lchov natijalarini ham saqlaydi — bu "
    "ma'lumotni silliqlashning asosi.",
    """// Massivda o'lchov tarixi va o'rtacha qiymat
const int SENSOR = A0, LED = 9;
const int N = 10;
int tarix[N];               // oxirgi 10 ta o'lchov
int joy = 0;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  for (int i = 0; i < N; i++) tarix[i] = analogRead(SENSOR);  // to'ldiramiz
}

void loop() {
  // yangi o'lchovni eng eski o'rniga yozamiz (aylanma buffer)
  tarix[joy] = analogRead(SENSOR);
  joy = (joy + 1) % N;

  // o'rtacha, eng katta va eng kichik
  long yigindi = 0;
  int katta = 0, kichik = 1023;
  for (int i = 0; i < N; i++) {
    yigindi += tarix[i];
    if (tarix[i] > katta)  katta  = tarix[i];
    if (tarix[i] < kichik) kichik = tarix[i];
  }
  int ortacha = yigindi / N;

  analogWrite(LED, map(ortacha, 0, 1023, 0, 255));

  Serial.print("hozir=");    Serial.print(tarix[(joy + N - 1) % N]);
  Serial.print("  o'rtacha="); Serial.print(ortacha);
  Serial.print("  eng katta="); Serial.print(katta);
  Serial.print("  eng kichik="); Serial.println(kichik);
  delay(200);
}""",
    amaliy="Fotorezistor va LED yig'ib, oxirgi 10 o'lchovni massivda saqlash, "
           "o'rtachasini hisoblash va xom qiymat bilan o'rtacha qiymatning "
           "qanchalik farq qilishini kuzatish"),

"Massiv va sikl bilan ishlash": K(
    "Melodiya: ikki massiv birga ishlaydi",
    "Nota va davomiylik massivlari bir xil uzunlikda bo'lishi va bir indeks "
    "bilan o'qilishi kerak.",
    """// Ikki massiv birga: nota va davomiylik
const int ZUMMER = 8;
const int LED[3] = {9, 10, 11};

int nota[] = {262, 294, 330, 349, 392, 440, 494, 523};
int vaqt[] = {300, 300, 300, 300, 300, 300, 300, 600};
const int N = 8;

void setup() {
  pinMode(ZUMMER, OUTPUT);
  for (int i = 0; i < 3; i++) pinMode(LED[i], OUTPUT);
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < N; i++) {
    tone(ZUMMER, nota[i], vaqt[i]);

    // har notaga mos LED yonadi (3 ta LEDni aylantiramiz)
    digitalWrite(LED[i % 3], HIGH);

    Serial.print(i); Serial.print(": ");
    Serial.print(nota[i]); Serial.print(" Hz, ");
    Serial.print(vaqt[i]); Serial.println(" ms");

    delay(vaqt[i]);
    digitalWrite(LED[i % 3], LOW);
    delay(60);
  }
  delay(1500);
}""",
    amaliy="Zummer va uchta LED yig'ib, nota hamda davomiylik massivlari bilan "
           "gamma chalish; massivlardan birini qisqartirib, chegaradan chiqish "
           "qanday xatoga olib kelishini ko'rish"),

"Massiv va sikl birga": K(
    "Bir necha sensorni massiv bilan o'qish",
    "To'rtta sensor uchun to'rtta alohida o'zgaruvchi emas, bitta massiv.",
    """// To'rt analog sensorni massiv bilan o'qish
const int SENSOR[4] = {A0, A1, A2, A3};
const int LED[4]    = {6, 7, 8, 9};
const int N = 4;
int qiymat[4];

void setup() {
  for (int i = 0; i < N; i++) pinMode(LED[i], OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int engKatta = 0, engKattaIdx = 0;

  for (int i = 0; i < N; i++) {
    qiymat[i] = analogRead(SENSOR[i]);
    if (qiymat[i] > engKatta) { engKatta = qiymat[i]; engKattaIdx = i; }

    Serial.print("S"); Serial.print(i);
    Serial.print("="); Serial.print(qiymat[i]); Serial.print("  ");
  }

  // eng katta qiymatli sensorning LEDi yonadi
  for (int i = 0; i < N; i++) digitalWrite(LED[i], i == engKattaIdx);

  Serial.print(" -> eng katta: S"); Serial.println(engKattaIdx);
  delay(300);
}""",
    amaliy="To'rtta fotorezistorni A0-A3 ga ulab, qaysi biriga ko'proq yorug'lik "
           "tushayotganini aniqlaydigan va mos LEDni yoqadigan tizim yig'ish"),

# ==================================================== FUNKSIYA
"O'z funksiyangni yozish": K(
    "Takrorlanadigan kodni funksiyaga chiqarish",
    "Funksiya — nom berilgan va qayta ishlatiladigan kod bo'lagi.",
    """// Funksiya: bir marta yozib, ko'p marta ishlatamiz
const int QIZIL = 7, SARIQ = 8, YASHIL = 9, ZUMMER = 6;

// --- o'z funksiyalarimiz ---
void ochir() {
  digitalWrite(QIZIL, LOW); digitalWrite(SARIQ, LOW); digitalWrite(YASHIL, LOW);
}

void yoq(int pin, int vaqt) {          // parametrli funksiya
  ochir();
  digitalWrite(pin, HIGH);
  delay(vaqt);
}

void signal(int marta) {
  for (int i = 0; i < marta; i++) { tone(ZUMMER, 1800, 80); delay(160); }
}

void setup() {
  pinMode(QIZIL, OUTPUT); pinMode(SARIQ, OUTPUT);
  pinMode(YASHIL, OUTPUT); pinMode(ZUMMER, OUTPUT);
}

void loop() {
  yoq(QIZIL, 3000);   signal(1);
  yoq(SARIQ, 1000);
  yoq(YASHIL, 3000);  signal(2);
  yoq(SARIQ, 1000);
}""",
    amaliy="Svetofor sxemasini yig'ib, avval hamma kodni loop ichiga yozish, "
           "keyin takrorlanadigan qismni yoq() va ochir() funksiyalariga "
           "chiqarib, kod uzunligini solishtirish"),

"O'z funksiyangni yozish va qayta ishlatish": K(
    "Qiymat qaytaruvchi funksiya",
    "void — hech narsa qaytarmaydi. int/float — natija qaytaradi va uni "
    "o'zgaruvchiga yozish mumkin.",
    """// Qiymat QAYTARUVCHI funksiya
const int SENSOR = A0, LED = 9, ZUMMER = 8;

// float qaytaradi — natijani ishlatish mumkin
float voltOlch(int pin) {
  int xom = analogRead(pin);
  return xom * 5.0 / 1023.0;
}

// o'rtachani qaytaradi — shovqinni kamaytiradi
int ortacha(int pin, int marta) {
  long yigindi = 0;
  for (int i = 0; i < marta; i++) { yigindi += analogRead(pin); delay(2); }
  return yigindi / marta;
}

// void — faqat ish bajaradi, qaytarmaydi
void ogohlantir(int marta) {
  for (int i = 0; i < marta; i++) {
    digitalWrite(LED, HIGH); tone(ZUMMER, 2000, 100);
    delay(200); digitalWrite(LED, LOW); delay(200);
  }
}

void setup() {
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  float u = voltOlch(SENSOR);              // natijani ISHLATAMIZ
  int   o = ortacha(SENSOR, 10);

  Serial.print("U = "); Serial.print(u, 3); Serial.print(" V   ");
  Serial.print("o'rtacha = "); Serial.println(o);

  if (u > 4.0) ogohlantir(3);
  delay(400);
}""",
    amaliy="Potensiometr, LED va zummer yig'ib, kuchlanishni qaytaruvchi "
           "voltOlch() va shovqinni kamaytiruvchi ortacha() funksiyalarini "
           "yozish; multimetr bilan tekshirib, funksiya to'g'ri ishlashini "
           "isbotlash"),

"Funksiyaga qiymat uzatish": K(
    "Parametrli funksiya — bitta funksiya, ko'p vazifa",
    "Parametr funksiyani UNIVERSAL qiladi: bitta miltillash funksiyasi "
    "istalgan pin va tezlikda ishlaydi.",
    """// Parametr: bitta funksiya — har xil natija
const int LED[3] = {7, 8, 9};
const int ZUMMER = 6;

void miltilla(int pin, int marta, int tezlik) {
  for (int i = 0; i < marta; i++) {
    digitalWrite(pin, HIGH); delay(tezlik);
    digitalWrite(pin, LOW);  delay(tezlik);
  }
}

// ikki parametr + qaytarilgan qiymat
int foizga(int xom, int chegara) {
  return map(constrain(xom, 0, chegara), 0, chegara, 0, 100);
}

void setup() {
  for (int i = 0; i < 3; i++) pinMode(LED[i], OUTPUT);
  pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  miltilla(LED[0], 3, 100);      // tez, 3 marta
  miltilla(LED[1], 2, 400);      // sekin, 2 marta
  miltilla(LED[2], 5,  60);      // juda tez, 5 marta

  int f = foizga(analogRead(A0), 1023);
  Serial.print("potensiometr: "); Serial.print(f); Serial.println(" %");

  tone(ZUMMER, map(f, 0, 100, 200, 2000), 150);
  delay(600);
}""",
    amaliy="Uchta LED va zummer yig'ib, bitta miltilla(pin, marta, tezlik) "
           "funksiyasi bilan uchta turli effekt hosil qilish; parametrsiz "
           "variantda necha marta kod nusxalanishini sanash"),

"Kodni bo'laklarga bo'lish": K(
    "Katta dasturni funksiyalarga ajratish",
    "Har bir funksiya BITTA ish qilsin — shunda xatoni topish oson bo'ladi.",
    """// Katta dastur — kichik, tushunarli bo'laklarga bo'lingan
const int LDR = A0, TERMISTOR = A1;
const int CHIROQ = 7, VENTILYATOR = 8, ZUMMER = 9;

// --- 1) O'LCHASH ---
int yoruglikOlch() { return analogRead(LDR); }
int haroratOlch()  { return map(analogRead(TERMISTOR), 0, 1023, 0, 50); }

// --- 2) QAROR QABUL QILISH ---
bool chiroqKerakmi(int yoruglik) { return yoruglik < 400; }
bool sovutishKerakmi(int t)      { return t > 27; }

// --- 3) BAJARISH ---
void boshqar(bool chiroq, bool sovutish) {
  digitalWrite(CHIROQ, chiroq);
  digitalWrite(VENTILYATOR, sovutish);
  if (sovutish) tone(ZUMMER, 1500, 60);
}

// --- 4) KO'RSATISH ---
void korsat(int y, int t, bool c, bool s) {
  Serial.print("yorug'lik="); Serial.print(y);
  Serial.print("  harorat="); Serial.print(t);
  Serial.print("  chiroq=");  Serial.print(c);
  Serial.print("  sovutish="); Serial.println(s);
}

void setup() {
  pinMode(CHIROQ, OUTPUT); pinMode(VENTILYATOR, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int y = yoruglikOlch();
  int t = haroratOlch();
  bool c = chiroqKerakmi(y);
  bool s = sovutishKerakmi(t);

  boshqar(c, s);
  korsat(y, t, c, s);
  delay(500);
}""",
    amaliy="Fotorezistor va termistorli tizimni yig'ib, dasturni to'rt qismga "
           "(o'lchash, qaror, bajarish, ko'rsatish) ajratish va bitta "
           "funksiyani ataylab buzib, xato qayerdaligini tez topishni sinash"),

# ==================================================== SERIAL VA NOSOZLIK
"Serial monitor: plata bilan gaplashish": K(
    "Ikki tomonlama Serial aloqa",
    "Serial nafaqat chiqarish, kompyuterdan buyruq QABUL QILISH uchun ham kerak.",
    """// Serial: ikki tomonlama aloqa
const int LED = 9, ZUMMER = 8, POT = A0;

void setup() {
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
  Serial.println("Buyruqlar: y = yoq, o = o'chir, s = signal, q = qiymat");
}

void loop() {
  // --- kompyuterdan buyruq qabul qilamiz ---
  if (Serial.available()) {
    char buyruq = Serial.read();

    if (buyruq == 'y') { digitalWrite(LED, HIGH); Serial.println("LED yoqildi"); }
    if (buyruq == 'o') { digitalWrite(LED, LOW);  Serial.println("LED o'chirildi"); }
    if (buyruq == 's') { tone(ZUMMER, 2000, 300); Serial.println("Signal berildi"); }
    if (buyruq == 'q') {
      Serial.print("A0 qiymati: "); Serial.println(analogRead(POT));
    }
  }
}""",
    amaliy="LED, zummer va potensiometr yig'ib, Serial monitorning yuqori "
           "qatoridan y/o/s/q buyruqlarini yuborib qurilmani boshqarish"),

"Serial monitor bilan kuzatish": K(
    "Sensor qiymatini kuzatish va grafikda ko'rish",
    "Serial Plotter (Tools > Serial Plotter) qiymatni GRAFIK bo'lib chizadi — "
    "sensor shovqinini shunda ko'rish oson.",
    """// Serial Plotter uchun: faqat sonlar, probel bilan ajratilgan
const int LDR = A0, TERM = A1, LED = 9;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int y = analogRead(LDR);
  int t = analogRead(TERM);

  // Serial Plotter uchun format: sonlar probel bilan, oxirida yangi qator
  Serial.print(y);
  Serial.print(" ");
  Serial.println(t);

  analogWrite(LED, map(y, 0, 1023, 0, 255));
  delay(50);              // 50 ms = sekundiga 20 nuqta
}

// Tools > Serial Plotter oching — ikkita chiziq jonli chiziladi.
// Fotorezistorni qo'l bilan yopib ko'ring: grafik darhol tushadi.""",
    amaliy="Fotorezistor va termistorni ulab, Serial Plotter'da ikki grafikni "
           "jonli kuzatish, qo'l bilan yopib va isitib, grafikning javob "
           "tezligini solishtirish"),

"Qiymatlarni Serial monitorda kuzatish": K(
    "Xom qiymat, hisoblangan qiymat va holatni birga chiqarish",
    "Yaxshi log — nosozlikni topishning eng tez yo'li.",
    """// Tushunarli log: xom qiymat + hisoblangan + qaror
const int SENSOR = A0, LED = 9;
const int CHEGARA = 500;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("vaqt(s) | xom | volt | foiz | holat");
}

void loop() {
  int   xom  = analogRead(SENSOR);
  float volt = xom * 5.0 / 1023.0;
  int   foiz = map(xom, 0, 1023, 0, 100);
  bool  yoq  = (xom > CHEGARA);

  digitalWrite(LED, yoq);

  Serial.print(millis() / 1000); Serial.print("      | ");
  Serial.print(xom);             Serial.print(" | ");
  Serial.print(volt, 2);         Serial.print(" | ");
  Serial.print(foiz);            Serial.print("   | ");
  Serial.println(yoq ? "YONIQ" : "o'chiq");

  delay(500);
}""",
    amaliy="Potensiometr va LED yig'ib, ustunli log formatida chiqarish; "
           "qiymatlarni multimetr ko'rsatkichi bilan solishtirib, hisoblash "
           "to'g'riligini tekshirish"),

"Serial orqali qiymat yuborish": K(
    "Kompyuterdan son yuborib, qurilmani sozlash",
    "parseInt() bilan matn ko'rinishidagi son o'qiladi va sozlama sifatida "
    "ishlatiladi.",
    """// Kompyuterdan SON yuborib chegarani sozlash
const int SENSOR = A0, LED = 9;
int chegara = 500;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Chegarani o'zgartirish uchun son yuboring (0-1023):");
}

void loop() {
  // --- kompyuterdan son qabul qilamiz ---
  if (Serial.available()) {
    int yangi = Serial.parseInt();
    if (yangi > 0 && yangi <= 1023) {
      chegara = yangi;
      Serial.print("Yangi chegara: "); Serial.println(chegara);
    }
    while (Serial.available()) Serial.read();     // buferni tozalash
  }

  int q = analogRead(SENSOR);
  digitalWrite(LED, q > chegara);

  Serial.print("qiymat="); Serial.print(q);
  Serial.print("  chegara="); Serial.print(chegara);
  Serial.println(q > chegara ? "  -> YONIQ" : "");
  delay(400);
}""",
    amaliy="Fotorezistor va LED yig'ib, chegarani Serial monitordan son "
           "yuborib sozlash; kodni qayta yuklamasdan sozlash mumkinligining "
           "afzalligini muhokama qilish"),

"Serial monitor va nosozlik topish": K(
    "Bosqichma-bosqich log bilan xatoni topish",
    "Har bosqichda log qoldirish — dastur qayerda \"o'lganini\" aniq ko'rsatadi.",
    """// Nosozlik topish: har bosqichda "men shu yerdaman" deb yozamiz
const int SENSOR = A0, TUGMA = 2, LED = 9;

void setup() {
  Serial.begin(9600);
  Serial.println("[1] setup boshlandi");

  pinMode(TUGMA, INPUT_PULLUP);
  Serial.println("[2] tugma pini sozlandi");

  pinMode(LED, OUTPUT);
  Serial.println("[3] LED pini sozlandi");

  int sinov = analogRead(SENSOR);
  Serial.print("[4] sensor sinovi: "); Serial.println(sinov);
  if (sinov == 0 || sinov == 1023) {
    Serial.println("    OGOHLANTIRISH: sensor ulanmagan bo'lishi mumkin!");
  }

  Serial.println("[5] setup tugadi\\n");
}

void loop() {
  static unsigned long n = 0;
  n++;

  int q = analogRead(SENSOR);
  bool bosildi = (digitalRead(TUGMA) == LOW);

  digitalWrite(LED, bosildi);

  // har 20-siklda holat hisoboti
  if (n % 20 == 0) {
    Serial.print("loop #"); Serial.print(n);
    Serial.print("  sensor="); Serial.print(q);
    Serial.print("  tugma=");  Serial.println(bosildi ? "BOSILGAN" : "bo'sh");
  }
  delay(50);
}""",
    amaliy="Sensor va tugmani ulab, o'qituvchi ataylab bitta simni uzib qo'yadi; "
           "o'quvchilar log yozuvlariga qarab xato qayerdaligini topadi"),

"Nosozlik topish: kod va sxemani birga tekshirish": K(
    "Sxema va kodni ketma-ket tekshiruvchi diagnostika dasturi",
    "Tartib doim bir xil: 1) quvvat, 2) GND, 3) pin raqami, 4) mantiq.",
    """// DIAGNOSTIKA: har bir pinni alohida sinaydi
const int LED[3] = {7, 8, 9};
const int TUGMA = 2, SENSOR = A0;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 3; i++) pinMode(LED[i], OUTPUT);
  pinMode(TUGMA, INPUT_PULLUP);

  Serial.println("=== SXEMA DIAGNOSTIKASI ===");

  // 1) Har bir LEDni alohida sinaymiz
  Serial.println("1) LEDlar sinovi — har biri 1 sekund yonadi");
  for (int i = 0; i < 3; i++) {
    Serial.print("   pin "); Serial.print(LED[i]); Serial.println(" ...");
    digitalWrite(LED[i], HIGH); delay(1000); digitalWrite(LED[i], LOW);
  }
  Serial.println("   Yonmagan LED bo'lsa: qutbini va rezistorini tekshiring.");

  // 2) Sensor sinovi
  int q = analogRead(SENSOR);
  Serial.print("2) A0 qiymati: "); Serial.println(q);
  if (q < 5)         Serial.println("   -> 0 ga yaqin: sensor GND ga qisqa tutashgan?");
  else if (q > 1018) Serial.println("   -> 1023 ga yaqin: sensor umuman ulanmagan?");
  else               Serial.println("   -> normal oraliqda, sensor ishlayapti.");

  // 3) Tugma sinovi
  Serial.println("3) Tugmani 3 sekund ichida bosing...");
  bool sezildi = false;
  unsigned long boshi = millis();
  while (millis() - boshi < 3000) {
    if (digitalRead(TUGMA) == LOW) { sezildi = true; break; }
  }
  Serial.println(sezildi ? "   -> tugma ISHLAYAPTI" : "   -> tugma sezilmadi: simlarni tekshiring");

  Serial.println("=== Diagnostika tugadi ===");
}

void loop() { }""",
    amaliy="Xatosi oldindan qo'yilgan sxemani (teskari LED, uzilgan GND, "
           "noto'g'ri pin) diagnostika dasturi yordamida bosqichma-bosqich "
           "tekshirib, uchta xatoni ham topish"),

"Xatoni topish va tuzatish": K(
    "Ataylab xato qilingan kod — topib tuzatish uchun",
    "Beshta tipik xato bitta dasturda yig'ilgan.",
    """// BU KODDA 5 TA XATO BOR — toping va tuzating!
const int LED = 9;
const int TUGMA = 2;

void setup() {
  pinMode(LED, INPUT);          // XATO 1: LED chiqish bo'lishi kerak (OUTPUT)
  pinMode(TUGMA, INPUT);        // XATO 2: INPUT_PULLUP bo'lmasa pin "suzadi"
  Serial.begin(9600)            // XATO 3: nuqta-vergul yo'q
}

void loop() {
  int holat = digitalRead(TUGMA);

  if (holat = LOW) {            // XATO 4: = emas, == bo'lishi kerak
    digitalWrite(LED, HIGH);
  }
                                // XATO 5: else yo'q — LED hech qachon o'chmaydi
  Serial.println(holat);
}

/* TO'G'RI VARIANT:

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(TUGMA, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int holat = digitalRead(TUGMA);
  if (holat == LOW) digitalWrite(LED, HIGH);
  else              digitalWrite(LED, LOW);
  Serial.println(holat);
}
*/""",
    amaliy="Tugma va LED sxemasini yig'ib, xatolari bor kodni yuklab ko'rish, "
           "kompilyator xabarlarini o'qib beshta xatoni birma-bir topish va "
           "har bir tuzatishdan keyin natijani sinash"),

"Dasturdagi xatoni topish": K(
    "Blokli muhitda xatoni bosqichma-bosqich izlash",
    "Bloklarni birma-bir o'chirib sinash — eng ishonchli usul.",
    """// Xatoni izolyatsiya qilish usuli: qismlarni birma-bir yoqib sinash
const int LED = 9, ZUMMER = 8, SENSOR = A0;

// Har bir qismni alohida yoqib/o'chirib sinash mumkin
const bool SINOV_LED    = true;
const bool SINOV_ZUMMER = false;
const bool SINOV_SENSOR = false;

void setup() {
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
  Serial.println("Faqat yoqilgan qismlar ishlaydi — xatoni shunday izolyatsiya qilamiz");
}

void loop() {
  if (SINOV_LED) {
    digitalWrite(LED, HIGH); delay(300);
    digitalWrite(LED, LOW);  delay(300);
    Serial.println("LED qismi ishladi");
  }

  if (SINOV_ZUMMER) {
    tone(ZUMMER, 1500, 200); delay(400);
    Serial.println("Zummer qismi ishladi");
  }

  if (SINOV_SENSOR) {
    Serial.print("sensor="); Serial.println(analogRead(SENSOR));
    delay(300);
  }
}""",
    amaliy="Uch qismli (LED, zummer, sensor) sxemani yig'ib, xatoni topish "
           "uchun qismlarni birma-bir yoqib sinash usulini amalda qo'llash"),

"Dasturni tartibli va tushunarli yozish": K(
    "Chalkash kod va uning toza varianti",
    "Bir xil ishni bajaradigan ikki kod — biri o'qib bo'lmaydi, ikkinchisi "
    "o'zini o'zi tushuntiradi.",
    """// --- CHALKASH VARIANT (shunday YOZMANG) ---
// int a=9;int b=A0;void setup(){pinMode(a,1);Serial.begin(9600);}
// void loop(){int c=analogRead(b);if(c>500){digitalWrite(a,1);}else{
// digitalWrite(a,0);}Serial.println(c);delay(100);}

// --- TOZA VARIANT (shunday yozing) ---

const int CHIROQ_PIN     = 9;      // LED chiqishi
const int YORUGLIK_PIN   = A0;     // fotorezistor kirishi
const int QORONGI_CHEGARA = 500;   // shundan past bo'lsa qorong'i

void setup() {
  pinMode(CHIROQ_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int yoruglik = analogRead(YORUGLIK_PIN);

  // Qorong'i bo'lsa chiroqni yoqamiz
  bool qorongi = (yoruglik < QORONGI_CHEGARA);
  digitalWrite(CHIROQ_PIN, qorongi ? HIGH : LOW);

  Serial.print("yorug'lik = "); Serial.print(yoruglik);
  Serial.println(qorongi ? "  -> chiroq YONIQ" : "  -> chiroq o'chiq");

  delay(100);
}""",
    amaliy="Chalkash yozilgan tayyor kodni yuklab ishlatib ko'rish, keyin uni "
           "ma'noli nomlar, doimiylar va izohlar bilan qayta yozib, ayni "
           "natijani olish"),

"Kodni toza yozish: nom berish va izoh": K(
    "Yomon va yaxshi nom berish yonma-yon",
    "Yaxshi nom izohni ham keraksiz qiladi.",
    """// Nom berish qoidalari — amalda
// YOMON: a, b, x1, temp2, qiymat
// YAXSHI: yoruglikQiymati, QORONGI_CHEGARA, chiroqYoqilgan

const int CHIROQ_PIN      = 9;
const int YORUGLIK_PIN    = A0;
const int HARAKAT_PIN     = 2;

const int QORONGI_CHEGARA = 400;      // katta harf = DOIMIY
const unsigned long YONIQ_VAQT = 10000;   // 10 sekund

bool  chiroqYoqilgan   = false;
unsigned long yoqilganVaqt = 0;

void setup() {
  pinMode(CHIROQ_PIN, OUTPUT);
  pinMode(HARAKAT_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  int  yoruglikQiymati = analogRead(YORUGLIK_PIN);
  bool qorongiMi       = (yoruglikQiymati < QORONGI_CHEGARA);
  bool harakatBormi    = (digitalRead(HARAKAT_PIN) == HIGH);

  // Qorong'ida harakat sezilsa — chiroqni belgilangan vaqtga yoqamiz
  if (qorongiMi && harakatBormi) {
    chiroqYoqilgan = true;
    yoqilganVaqt   = millis();
  }

  // Vaqt tugasa — o'chiramiz
  if (chiroqYoqilgan && millis() - yoqilganVaqt > YONIQ_VAQT) {
    chiroqYoqilgan = false;
  }

  digitalWrite(CHIROQ_PIN, chiroqYoqilgan);
}""",
    amaliy="Fotorezistor, PIR va LED yig'ib, avval qisqa nomlar bilan yozish, "
           "keyin bir hafta o'tgan bo'lsa tushunish qiyinligini muhokama qilib, "
           "kodni ma'noli nomlar bilan qayta yozish"),

# ==================================================== ANALOG VA PWM
"PWM va analogWrite": K(
    "PWM ni ko'z bilan va o'lchov bilan ko'rish",
    "PWM — pinni tez-tez yoqib-o'chirish. O'rtacha quvvat shu bilan boshqariladi.",
    """// PWM: yoqib-o'chirish nisbati (duty cycle)
const int LED = 9, MOTOR = 10, POT = A0;

void setup() {
  pinMode(LED, OUTPUT); pinMode(MOTOR, OUTPUT);
  Serial.begin(9600);
  Serial.println("PWM | foiz | o'rtacha kuchlanish (5V da)");
}

void loop() {
  int pwm = map(analogRead(POT), 0, 1023, 0, 255);

  analogWrite(LED, pwm);
  analogWrite(MOTOR, pwm);

  int   foiz = pwm * 100 / 255;
  float u    = 5.0 * pwm / 255.0;      // multimetr shuni ko'rsatadi

  Serial.print(pwm);   Serial.print("   | ");
  Serial.print(foiz);  Serial.print(" % | ");
  Serial.print(u, 2);  Serial.println(" V");

  delay(200);
}

// TAJRIBA: multimetrni LED ga parallel ulang.
// PWM = 128 bo'lganda multimetr ~2,5 V ko'rsatadi — lekin pin aslida
// faqat 0 V va 5 V beradi! Multimetr O'RTACHASINI ko'rsatyapti.""",
    amaliy="LED va motorni PWM pinlarga ulab, potensiometr bilan boshqarish; "
           "multimetrni parallel ulab, PWM qiymati va o'rtacha kuchlanish "
           "orasidagi bog'liqlik jadvalini tuzish"),

"PWM: yorqinlikni sekin o'zgartirish": K(
    "Silliq yorishish va ko'zning chiziqsizligi",
    "Ko'z yorqinlikni CHIZIQLI sezmaydi: 0 dan 50 gacha o'zgarish 200 dan 250 "
    "gacha o'zgarishdan ancha sezilarli.",
    """// Silliq yorishish va ko'zning chiziqsizligi
const int LED = 9, LED2 = 10;

void setup() {
  pinMode(LED, OUTPUT); pinMode(LED2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // 1) CHIZIQLI: teng qadam bilan — lekin ko'zga notekis ko'rinadi
  for (int y = 0; y <= 255; y++) { analogWrite(LED, y); delay(8); }
  for (int y = 255; y >= 0; y--) { analogWrite(LED, y); delay(8); }

  // 2) KVADRATIK: ko'zga tekis ko'rinadi
  for (int i = 0; i <= 255; i++) {
    int y = (i * i) / 255;              // egri chiziq
    analogWrite(LED2, y);
    delay(8);
  }
  for (int i = 255; i >= 0; i--) {
    analogWrite(LED2, (i * i) / 255);
    delay(8);
  }
}

// Ikki LEDni yonma-yon qo'ying: birinchisi "sakraydi", ikkinchisi silliq.""",
    amaliy="Ikki LEDni yonma-yon qo'yib, birini chiziqli, ikkinchisini "
           "kvadratik qonun bilan yoritish va ko'z qaysi birini tekisroq "
           "sezishini aniqlash"),

"map() funksiyasi": K(
    "map() bilan oraliqni moslashtirish",
    "map bir oraliqdagi sonni boshqa oraliqqa proporsional ko'chiradi.",
    """// map(): 0..1023 -> boshqa oraliqlarga
#include <Servo.h>
Servo servo;
const int POT = A0, LED = 9, ZUMMER = 8;

void setup() {
  servo.attach(11);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int xom = analogRead(POT);                       // 0 .. 1023

  int yorqinlik = map(xom, 0, 1023, 0, 255);       // PWM oralig'i
  int burchak   = map(xom, 0, 1023, 0, 180);       // servo oralig'i
  int chastota  = map(xom, 0, 1023, 200, 2000);    // tovush oralig'i
  int foiz      = map(xom, 0, 1023, 0, 100);       // foiz

  analogWrite(LED, yorqinlik);
  servo.write(burchak);
  tone(ZUMMER, chastota, 50);

  Serial.print("xom=");      Serial.print(xom);
  Serial.print("  PWM=");    Serial.print(yorqinlik);
  Serial.print("  burchak=");Serial.print(burchak);
  Serial.print("  Hz=");     Serial.print(chastota);
  Serial.print("  foiz=");   Serial.println(foiz);

  delay(100);
}

// map TESKARI ham ishlaydi: map(xom, 0, 1023, 255, 0)""",
    amaliy="Bitta potensiometrni ulab, uning qiymatini map() bilan bir vaqtda "
           "LED yorqinligiga, servo burchagiga va tovush chastotasiga "
           "aylantirish"),

"map() funksiyasi: qiymatni moslash": K(
    "map() va constrain() birga",
    "map chegaradan tashqariga ham chiqaradi — shuning uchun constrain kerak.",
    """// map + constrain: xavfsiz moslashtirish
const int SENSOR = A0, LED = 9;

// sensorning HAQIQIY oralig'i (kalibrlashda o'lchanadi)
const int PAST = 200, BALAND = 800;

void setup() { pinMode(LED, OUTPUT); Serial.begin(9600); }

void loop() {
  int xom = analogRead(SENSOR);

  // XAVFLI: xom 200 dan kichik bo'lsa natija MANFIY chiqadi
  int xavfli = map(xom, PAST, BALAND, 0, 255);

  // XAVFSIZ: constrain chegaradan chiqishga yo'l qo'ymaydi
  int xavfsiz = constrain(map(xom, PAST, BALAND, 0, 255), 0, 255);

  analogWrite(LED, xavfsiz);

  Serial.print("xom=");         Serial.print(xom);
  Serial.print("  map=");       Serial.print(xavfli);
  Serial.print("  constrain="); Serial.println(xavfsiz);

  if (xavfli != xavfsiz) Serial.println("   ^^^ chegaradan chiqdi!");
  delay(200);
}""",
    amaliy="Fotorezistorni ulab, uning haqiqiy oralig'ini o'lchab olish, "
           "map() bilan moslashtirish va constrain'siz qiymat chegaradan "
           "chiqib ketishini Serial monitorda ko'rsatish"),

"map() va qiymatlarni moslash": K(
    "Ikki sensorni bir o'lchovga keltirish",
    "Har bir sensorning oralig'i boshqacha — ularni solishtirish uchun avval "
    "bir xil o'lchovga (0-100 %) keltirish kerak.",
    """// Turli sensorlarni BIR o'lchovga keltirish
const int LDR = A0, TUPROQ = A1;
const int LED1 = 9, LED2 = 10;

// har bir sensor uchun O'ZINING kalibrlangan chegarasi
const int LDR_PAST = 30,  LDR_BALAND = 950;
const int TUP_PAST = 300, TUP_BALAND = 1010;

int foizga(int xom, int past, int baland) {
  return constrain(map(xom, past, baland, 0, 100), 0, 100);
}

void setup() {
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int yoruglik = foizga(analogRead(LDR),    LDR_PAST, LDR_BALAND);
  int quruqlik = foizga(analogRead(TUPROQ), TUP_PAST, TUP_BALAND);

  analogWrite(LED1, map(yoruglik, 0, 100, 0, 255));
  analogWrite(LED2, map(quruqlik, 0, 100, 0, 255));

  // endi ikkalasi ham 0..100 — ularni SOLISHTIRISH mumkin
  Serial.print("yorug'lik="); Serial.print(yoruglik); Serial.print(" %   ");
  Serial.print("quruqlik=");  Serial.print(quruqlik); Serial.println(" %");
  delay(400);
}""",
    amaliy="Fotorezistor va tuproq namligi datchigini birga ulab, har birini "
           "alohida kalibrlash va ikkalasini 0-100 % oralig'iga keltirib "
           "solishtirish"),

"Tortuvchi (pull-up) rezistor": K(
    "Tortuvchisiz pinning \"suzishini\" ko'rsatish",
    "Rezistorsiz pin tasodifiy qiymat o'qiydi — buni tajribada ko'rsatish mumkin.",
    """// Tortuvchi rezistorning KERAKLIGINI isbotlash
const int OCHIQ = 2;      // hech narsaga ulanmagan pin (suzadi)
const int PULLUP = 3;     // tugma + ichki tortuvchi
const int LED = 9;

void setup() {
  pinMode(OCHIQ, INPUT);            // TORTUVCHISIZ — xato variant
  pinMode(PULLUP, INPUT_PULLUP);    // TORTUVCHI BILAN — to'g'ri variant
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("suzuvchi pin | pullup pin");
}

void loop() {
  int suzuvchi = digitalRead(OCHIQ);    // tasodifiy 0/1 chiqadi
  int barqaror = digitalRead(PULLUP);   // tinch holatda doim 1

  digitalWrite(LED, barqaror == LOW);

  Serial.print("      "); Serial.print(suzuvchi);
  Serial.print("      |    ");           Serial.println(barqaror);

  // D2 simiga qo'lingizni yaqinlashtiring — qiymat sakray boshlaydi.
  // D3 esa qo'l tekkizsangiz ham o'zgarmaydi.
  delay(200);
}""",
    amaliy="Bitta pinni ochiq qoldirib, ikkinchisini INPUT_PULLUP bilan tugmaga "
           "ulash; ochiq pinga qo'lni yaqinlashtirib, qiymat sakrashini Serial "
           "monitorda ko'rsatish"),

# ==================================================== ESP32 — ASOSLAR
"IDE'ga ESP32 platasini qo'shish": K(
    "ESP32 ulanganini tekshiruvchi birinchi dastur",
    "Board Manager URL qo'shilgach, birinchi tekshiruv — chip ma'lumotini "
    "chiqarish.",
    """// ESP32 ulanganini tekshirish va chip ma'lumotini chiqarish
const int LED = 2;          // ko'p ESP32 platalarda ichki LED GPIO2 da

void setup() {
  Serial.begin(115200);     // ESP32 uchun odatda 115200
  pinMode(LED, OUTPUT);
  delay(1000);

  Serial.println("=== ESP32 ishga tushdi ===");
  Serial.print("Chip modeli: ");   Serial.println(ESP.getChipModel());
  Serial.print("Yadrolar soni: "); Serial.println(ESP.getChipCores());
  Serial.print("Chastota: ");      Serial.print(ESP.getCpuFreqMHz()); Serial.println(" MHz");
  Serial.print("Bo'sh xotira: ");  Serial.print(ESP.getFreeHeap());   Serial.println(" bayt");
  Serial.print("Flash hajmi: ");   Serial.print(ESP.getFlashChipSize() / 1048576); Serial.println(" MB");
}

void loop() {
  digitalWrite(LED, HIGH); delay(400);
  digitalWrite(LED, LOW);  delay(400);
}""",
    amaliy="Board Manager URL ni qo'shib ESP32 ni o'rnatish, platani ulab chip "
           "ma'lumotini chiqarish va ichki LEDni miltillatish; Arduino Uno "
           "bilan xotira hamda chastotani solishtirib jadval tuzish"),

"IDE'ga ESP32 qo'shish va birinchi yuklash": K(
    "ESP32 birinchi yuklash va BOOT tugmasi",
    "Ba'zi platalarda yuklash boshlanganda BOOT tugmasini bosib turish kerak.",
    """// ESP32 birinchi dastur — yuklash muvaffaqiyatli bo'lganini tasdiqlaydi
const int LED = 2;
int sanoq = 0;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  Serial.println("\\nYuklash muvaffaqiyatli!");
  Serial.println("Agar bu yozuv chiqmasa: tezlik 115200 ekanini tekshiring.");
}

void loop() {
  sanoq++;
  digitalWrite(LED, HIGH); delay(200);
  digitalWrite(LED, LOW);  delay(800);
  Serial.print("ishlayapti, sikl: "); Serial.println(sanoq);
}

// Yuklashda "Connecting....." da qotib qolsa:
//   1) BOOT tugmasini bosib turing, 2) EN (RESET) ni bir marta bosing,
//   3) yuklash boshlangach BOOT ni qo'yib yuboring.""",
    amaliy="ESP32 ni ulab birinchi dasturni yuklash, Serial tezligini 115200 ga "
           "qo'yish va yuklash paytida BOOT/EN tugmalari tartibini amalda "
           "mashq qilish"),

"Birinchi dastur va Serial aloqa": K(
    "ESP32 va Arduino Uno farqi bitta dasturda",
    "3,3 V mantiq, 12 bitli ADC va 115200 tezlik — uch asosiy farq.",
    """// ESP32 va Arduino Uno FARQLARI — sonlar bilan
const int LED = 2, POT = 34;      // GPIO34 — faqat kirish uchun ADC pin

void setup() {
  Serial.begin(115200);           // Uno'da odatda 9600
  pinMode(LED, OUTPUT);

  Serial.println("Farq | Arduino Uno | ESP32");
  Serial.println("-----|-------------|-------");
  Serial.println("Mantiq |   5 V     | 3.3 V");
  Serial.println("ADC    | 10 bit    | 12 bit");
  Serial.println("Oraliq | 0..1023   | 0..4095");
  Serial.println("Tezlik | 16 MHz    | 240 MHz");
}

void loop() {
  int xom = analogRead(POT);              // 0..4095
  float u = xom * 3.3 / 4095.0;           // 3.3 V ga bo'linadi, 5 V ga EMAS

  digitalWrite(LED, xom > 2048);

  Serial.print("xom="); Serial.print(xom);
  Serial.print("  U=");  Serial.print(u, 3); Serial.println(" V");
  delay(300);
}""",
    amaliy="ESP32 ga potensiometrni 3,3 V bilan ulab, analogRead qiymati "
           "0-4095 oralig'ida ekanini ko'rsatish va Uno bilan yonma-yon "
           "solishtirish jadvalini to'ldirish"),

"ESP32 arxitekturasi va Arduino'dan farqi": K(
    "Ikki yadro va xotira — o'lchab ko'rish",
    "ESP32 ikki yadroli: bitta vazifa bir yadroda, boshqasi ikkinchisida "
    "ishlashi mumkin.",
    """// Ikki yadro: qaysi vazifa qaysi yadroda ishlayotganini ko'rsatamiz
const int LED1 = 2, LED2 = 4;

void vazifa1(void *p) {
  for (;;) {
    digitalWrite(LED1, HIGH); vTaskDelay(200 / portTICK_PERIOD_MS);
    digitalWrite(LED1, LOW);  vTaskDelay(200 / portTICK_PERIOD_MS);
    Serial.print("vazifa1 -> yadro "); Serial.println(xPortGetCoreID());
  }
}

void vazifa2(void *p) {
  for (;;) {
    digitalWrite(LED2, HIGH); vTaskDelay(700 / portTICK_PERIOD_MS);
    digitalWrite(LED2, LOW);  vTaskDelay(700 / portTICK_PERIOD_MS);
    Serial.print("vazifa2 -> yadro "); Serial.println(xPortGetCoreID());
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT);

  Serial.print("Bo'sh xotira: "); Serial.println(ESP.getFreeHeap());

  // ikki vazifani IKKI YADROGA taqsimlaymiz
  xTaskCreatePinnedToCore(vazifa1, "v1", 2048, NULL, 1, NULL, 0);   // yadro 0
  xTaskCreatePinnedToCore(vazifa2, "v2", 2048, NULL, 1, NULL, 1);   // yadro 1
}

void loop() { }      // asosiy loop bo'sh — hamma ish vazifalarda""",
    amaliy="Ikki LEDni ulab, ularni ikki yadroga taqsimlangan alohida "
           "vazifalarda turli tezlikda miltillatish; Serial monitorda qaysi "
           "vazifa qaysi yadroda ishlayotganini kuzatish"),

"ESP32 arxitekturasi: ikki yadro va xotira": K(
    "Xotira turlari va ularni o'lchash",
    "Heap, PSRAM va Flash — uchtasi uch xil maqsad uchun.",
    """// ESP32 xotirasini o'lchash
void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("=== XOTIRA HISOBOTI ===");
  Serial.print("Heap (ish xotirasi):  "); Serial.print(ESP.getFreeHeap()); Serial.println(" bayt");
  Serial.print("Eng katta bo'lak:     "); Serial.print(ESP.getMaxAllocHeap()); Serial.println(" bayt");
  Serial.print("PSRAM bormi:          "); Serial.println(psramFound() ? "HA" : "yo'q");
  if (psramFound()) {
    Serial.print("Bo'sh PSRAM:          "); Serial.print(ESP.getFreePsram()); Serial.println(" bayt");
  }
  Serial.print("Flash:                "); Serial.print(ESP.getFlashChipSize()); Serial.println(" bayt");
  Serial.print("Sketch hajmi:         "); Serial.print(ESP.getSketchSize()); Serial.println(" bayt");
  Serial.print("Yadrolar:             "); Serial.println(ESP.getChipCores());
}

void loop() {
  // xotira "oqib ketishini" kuzatish uchun
  Serial.print("bo'sh heap: "); Serial.println(ESP.getFreeHeap());
  delay(3000);
}""",
    amaliy="ESP32 xotirasini o'lchash, keyin katta massiv e'lon qilib bo'sh "
           "xotira kamayishini kuzatish va Arduino Uno ning 2 KB xotirasi bilan "
           "solishtirish"),

"ESP32 pinlari va 3.3V mantiq darajasi": K(
    "3,3 V mantiq va xavfsiz ulash",
    "5 V signalni to'g'ridan-to'g'ri ESP32 piniga berish pinni shikastlaydi.",
    """// 3.3 V mantiq — xavfsiz pinlar bilan ishlash
const int CHIQISH = 2;      // ichki LED
const int KIRISH  = 4;      // tugma uchun
const int ADC_PIN = 34;     // faqat KIRISH uchun ADC pini

void setup() {
  Serial.begin(115200);
  pinMode(CHIQISH, OUTPUT);
  pinMode(KIRISH, INPUT_PULLUP);
  // GPIO34-39 da INPUT_PULLUP YO'Q — tashqi rezistor kerak

  Serial.println("XAVFSIZLIK QOIDALARI:");
  Serial.println(" - ESP32 pini 3.3 V, 5 V berilsa shikastlanadi");
  Serial.println(" - Bir pindan maks. 12 mA (Uno'da 20 mA)");
  Serial.println(" - GPIO34..39 faqat KIRISH, chiqish qila olmaydi");
  Serial.println(" - GPIO6..11 flesh xotiraga band, ISHLATILMAYDI");
  Serial.println(" - GPIO0, 2, 12, 15 yuklashga ta'sir qiladi (strapping)");
}

void loop() {
  int xom = analogRead(ADC_PIN);            // 0..4095
  float u = xom * 3.3 / 4095.0;

  digitalWrite(CHIQISH, digitalRead(KIRISH) == LOW);

  Serial.print("ADC="); Serial.print(xom);
  Serial.print("  U=");  Serial.print(u, 2); Serial.println(" V");
  delay(300);
}""",
    amaliy="ESP32 ga tugma va potensiometrni 3,3 V bilan ulab, pin xaritasini "
           "chizish; qaysi pinlar band, qaysilari faqat kirish ekanini "
           "belgilab, xavfsiz pinlar ro'yxatini tuzish"),

"Pinlar xaritasi va 3.3V mantiq": K(
    "Xavfsiz pinlarni sinovdan o'tkazish",
    "Har bir GPIO ni sinab, ishlaydiganlar ro'yxatini tuzish.",
    """// Xavfsiz GPIO larni birma-bir sinash
int sinov[] = {2, 4, 5, 13, 14, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 32, 33};
const int N = sizeof(sinov) / sizeof(sinov[0]);

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Har bir pinga LED ulab sinang — 1 sekunddan yonadi");

  for (int i = 0; i < N; i++) pinMode(sinov[i], OUTPUT);
}

void loop() {
  for (int i = 0; i < N; i++) {
    Serial.print("Hozir sinalyapti: GPIO"); Serial.println(sinov[i]);
    digitalWrite(sinov[i], HIGH);
    delay(1000);
    digitalWrite(sinov[i], LOW);
    delay(200);
  }
  Serial.println("--- sikl tugadi ---\\n");
  delay(2000);
}""",
    amaliy="ESP32 ning har bir chiqish pinini LED bilan birma-bir sinab, "
           "ishlaydigan pinlar ro'yxatini tuzish va bandlarini (GPIO6-11) "
           "chetlab o'tishni amalda ko'rsatish"),

"Raqamli kirish va chiqish": K(
    "ESP32 da tugma va LED",
    "Uno bilan bir xil, faqat pin nomlari GPIO va mantiq 3,3 V.",
    """// ESP32: raqamli kirish va chiqish
const int TUGMA = 4, LED = 2, ZUMMER = 5;
bool yongan = false;
unsigned long oxirgi = 0;

void setup() {
  pinMode(TUGMA, INPUT_PULLUP);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (digitalRead(TUGMA) == LOW && millis() - oxirgi > 250) {
    oxirgi = millis();
    yongan = !yongan;
    digitalWrite(LED, yongan);
    tone(ZUMMER, yongan ? 2000 : 800, 100);
    Serial.println(yongan ? "YOQILDI" : "o'chirildi");
  }
}""",
    amaliy="ESP32 ga tugma, LED va zummer ulab, tugma bosilganda holatni "
           "almashtiruvchi dastur yozish va 3,3 V mantiqda LED rezistorini "
           "qayta hisoblash"),

"ESP32'da raqamli kirish va chiqish": K(
    "GPIO chiqish quvvati va rezistor hisobi",
    "ESP32 pini 12 mA beradi (Uno 20 mA) — rezistorni shunga qarab tanlash kerak.",
    """// 3.3 V uchun rezistorni QAYTA hisoblaymiz
// R = (3.3 - Uled) / I
//   qizil LED (2.0 V), 10 mA -> R = (3.3-2.0)/0.010 = 130 Om -> 150 Om
//   ko'k  LED (3.0 V), 10 mA -> R = (3.3-3.0)/0.010 = 30 Om  -> 100 Om (xavfsizroq)

const int LED_Q = 2, LED_K = 4, TUGMA = 5;

void setup() {
  pinMode(LED_Q, OUTPUT); pinMode(LED_K, OUTPUT);
  pinMode(TUGMA, INPUT_PULLUP);
  Serial.begin(115200);
  Serial.println("3.3 V mantiqda LED rezistorlari 5 V dagidan KICHIKROQ");
}

void loop() {
  bool bosildi = (digitalRead(TUGMA) == LOW);
  digitalWrite(LED_Q, bosildi);
  digitalWrite(LED_K, !bosildi);

  Serial.println(bosildi ? "qizil yoniq" : "ko'k yoniq");
  delay(200);
}""",
    amaliy="ESP32 uchun LED rezistorlarini 3,3 V ga qayta hisoblab, qizil va "
           "ko'k LEDni ulash; multimetr bilan tokni o'lchab, 12 mA chegarasidan "
           "oshmayotganini tekshirish"),

"ADC: analog o'qish va uning xususiyatlari": K(
    "ESP32 ADC ning chiziqsizligi",
    "ESP32 ADC si Uno nikidan aniqroq (12 bit), lekin chetlarida CHIZIQSIZ — "
    "buni o'lchab ko'rish kerak.",
    """// ESP32 ADC: 12 bit, lekin chetlarida chiziqsiz
const int ADC_PIN = 34;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);              // 0..4095 (standart)
  analogSetAttenuation(ADC_11db);        // 0..3.3 V oralig'i uchun
  Serial.println("xom | hisoblangan U | multimetr U (qo'lda yozing)");
}

void loop() {
  // shovqinni kamaytirish uchun o'rtacha olamiz
  long yigindi = 0;
  for (int i = 0; i < 16; i++) { yigindi += analogRead(ADC_PIN); delay(2); }
  int xom = yigindi / 16;

  float u = xom * 3.3 / 4095.0;

  Serial.print(xom);   Serial.print("  |  ");
  Serial.print(u, 3);  Serial.println(" V");

  // TAJRIBA: potensiometrni chetlarga burang.
  // 0.15 V dan past va 3.1 V dan yuqori qismda ADC "yassilashadi" —
  // aniq o'lchov uchun shu oraliqlardan qochish kerak.
  delay(500);
}""",
    amaliy="ESP32 ga potensiometrni ulab, ADC qiymati va multimetr ko'rsatkichini "
           "10 nuqtada yozib olib, grafik chizish va chetlaridagi chiziqsizlikni "
           "aniqlash"),

"ESP32'da analog o'qish (ADC)": K(
    "12 bitli ADC va o'rtachalash",
    "Bitta o'qish shovqinli, 16 ta o'qishning o'rtachasi ancha barqaror.",
    """// ESP32 ADC: bitta o'qish va o'rtacha o'qish farqi
const int ADC_PIN = 34, LED = 2;

int bittaOqish() { return analogRead(ADC_PIN); }

int ortachaOqish(int marta) {
  long y = 0;
  for (int i = 0; i < marta; i++) { y += analogRead(ADC_PIN); delayMicroseconds(200); }
  return y / marta;
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  analogReadResolution(12);
  Serial.println("bitta | o'rtacha(32) | farq");
}

void loop() {
  int a = bittaOqish();
  int b = ortachaOqish(32);

  analogWrite(LED, map(b, 0, 4095, 0, 255));

  Serial.print(a); Serial.print("   | ");
  Serial.print(b); Serial.print("        | ");
  Serial.println(abs(a - b));
  delay(200);
}""",
    amaliy="Potensiometrni ulab, bitta o'qish va 32 o'qish o'rtachasini yonma-yon "
           "chiqarish; Serial Plotter'da ikki chiziqni solishtirib, shovqin "
           "qanchalik kamayganini ko'rsatish"),

"Pinlar, ADC va DAC xususiyatlari": K(
    "DAC — haqiqiy analog chiqish",
    "PWM analog EMAS, u tez yoqib-o'chirish. DAC esa HAQIQIY oraliq kuchlanish "
    "beradi. ESP32 da GPIO25 va GPIO26 — DAC pinlari.",
    """// DAC va PWM farqini multimetr bilan ko'rsatish
const int DAC_PIN = 25;     // HAQIQIY analog chiqish
const int PWM_PIN = 2;      // PWM (yoqib-o'chirish)

void setup() {
  Serial.begin(115200);
  ledcAttach(PWM_PIN, 5000, 8);      // 5 kHz, 8 bit
  Serial.println("DAC (0..255) -> haqiqiy kuchlanish | PWM -> o'rtacha kuchlanish");
}

void loop() {
  for (int q = 0; q <= 255; q += 51) {
    dacWrite(DAC_PIN, q);            // haqiqiy analog: 0..3.3 V
    ledcWrite(PWM_PIN, q);           // PWM: 0/3.3 V ni almashtiradi

    float kutilgan = q * 3.3 / 255.0;
    Serial.print("qiymat="); Serial.print(q);
    Serial.print("  kutilgan U="); Serial.print(kutilgan, 2); Serial.println(" V");

    delay(2000);   // multimetr bilan IKKALA pinni o'lchang
  }
}

// Ossilograf bo'lsa farq yaqqol ko'rinadi:
//   DAC — tekis chiziq;  PWM — to'rtburchak impulslar.""",
    amaliy="GPIO25 (DAC) va GPIO2 (PWM) ga multimetrni navbat bilan ulab, bir "
           "xil qiymatda ikkalasi qanday kuchlanish ko'rsatishini o'lchash va "
           "farqini tushuntirish"),

"Touch (sensorli) pinlar": K(
    "Sensorli tugma — mexanik tugmasiz",
    "ESP32 da 10 ta touch pin bor. Ular sig'imni o'lchaydi: barmoq "
    "yaqinlashganda sig'im ortadi va qiymat TUSHADI.",
    """// Touch pin — barmoq tegishini sig'im orqali sezish
const int TOUCH_PIN = T0;     // GPIO4
const int LED = 2, ZUMMER = 5;
int chegara;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);

  // KALIBRLASH: tegmasdan turgan qiymatni o'lchaymiz
  long y = 0;
  for (int i = 0; i < 20; i++) { y += touchRead(TOUCH_PIN); delay(20); }
  int tinch = y / 20;
  chegara = tinch * 0.6;         // 40 % tushsa — teginish deb hisoblaymiz

  Serial.print("Tinch qiymat: "); Serial.print(tinch);
  Serial.print("   Chegara: ");   Serial.println(chegara);
}

void loop() {
  int q = touchRead(TOUCH_PIN);
  bool tegdi = (q < chegara);

  digitalWrite(LED, tegdi);
  if (tegdi) tone(ZUMMER, 1800, 50);

  Serial.print("touch="); Serial.print(q);
  Serial.println(tegdi ? "  -> TEGDI" : "");
  delay(150);
}""",
    amaliy="GPIO4 ga folga yoki metall varaq ulab sensorli tugma yasash, tinch "
           "qiymatni kalibrlash va barmoq yaqinlashganda qiymat qanday "
           "tushishini Serial Plotter'da kuzatish"),

# ==================================================== ESP32 — WIFI VA VEB
"WiFi tarmog'iga ulanish": K(
    "WiFi ga ulanish va holatni LED bilan ko'rsatish",
    "Ulanish holati LED orqali ko'rinadi: miltillash — ulanmoqda, doim yoniq — "
    "ulandi.",
    """// WiFi ga ulanish + holat indikatori
#include <WiFi.h>

const char* WIFI_NOM   = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const int LED = 2;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);

  Serial.print("Ulanmoqda: "); Serial.println(WIFI_NOM);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);

  int urinish = 0;
  while (WiFi.status() != WL_CONNECTED && urinish < 40) {
    digitalWrite(LED, !digitalRead(LED));    // miltillash = ulanmoqda
    delay(500);
    Serial.print(".");
    urinish++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    digitalWrite(LED, HIGH);                 // doim yoniq = ulandi
    Serial.println("\\nULANDI!");
    Serial.print("IP manzil: ");   Serial.println(WiFi.localIP());
    Serial.print("Signal kuchi: ");Serial.print(WiFi.RSSI()); Serial.println(" dBm");
    Serial.print("MAC manzil: ");  Serial.println(WiFi.macAddress());
  } else {
    digitalWrite(LED, LOW);
    Serial.println("\\nULANMADI. Nom va parolni tekshiring.");
  }
}

void loop() {
  // aloqa uzilsa qayta ulanamiz
  if (WiFi.status() != WL_CONNECTED) {
    digitalWrite(LED, LOW);
    Serial.println("Aloqa uzildi, qayta ulanmoqda...");
    WiFi.reconnect();
    delay(3000);
  }
  delay(1000);
}""",
    amaliy="ESP32 ni maktab WiFi tarmog'iga ulab, IP manzil va signal kuchini "
           "chiqarish; LED bilan ulanish holatini ko'rsatish va xonaning turli "
           "nuqtalarida RSSI ni o'lchab, signal kartasini tuzish"),

"IP manzil va tarmoq asoslari": K(
    "Tarmoqni skanerlash va IP ma'lumotini chiqarish",
    "IP, maska va shlyuz — uchtasi birga tarmoqni tashkil qiladi.",
    """// Tarmoq ma'lumoti va atrofdagi WiFi tarmoqlarini skanerlash
#include <WiFi.h>

const char* WIFI_NOM   = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const int LED = 2;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);

  // 1) Atrofdagi tarmoqlarni skanerlaymiz
  Serial.println("Atrofdagi WiFi tarmoqlari:");
  int n = WiFi.scanNetworks();
  for (int i = 0; i < n; i++) {
    Serial.print("  "); Serial.print(i + 1); Serial.print(") ");
    Serial.print(WiFi.SSID(i));
    Serial.print("   signal: "); Serial.print(WiFi.RSSI(i)); Serial.print(" dBm");
    Serial.println(WiFi.encryptionType(i) == WIFI_AUTH_OPEN ? "   [OCHIQ]" : "   [parolli]");
  }

  // 2) Ulanamiz va tarmoq sozlamalarini ko'ramiz
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  digitalWrite(LED, HIGH);

  Serial.println("\\n=== TARMOQ SOZLAMALARI ===");
  Serial.print("IP manzil:  "); Serial.println(WiFi.localIP());
  Serial.print("Maska:      "); Serial.println(WiFi.subnetMask());
  Serial.print("Shlyuz:     "); Serial.println(WiFi.gatewayIP());
  Serial.print("DNS:        "); Serial.println(WiFi.dnsIP());
}

void loop() { delay(10000); }""",
    amaliy="ESP32 bilan xonadagi WiFi tarmoqlarini skanerlab ro'yxatini "
           "chiqarish, o'z tarmog'iga ulanib IP/maska/shlyuzni yozib olish va "
           "telefon hamda kompyuter IP lari bilan solishtirib, tarmoq xaritasini "
           "chizish"),

"IP manzil, port va tarmoq asoslari": K(
    "Port tushunchasi — bitta IP, ko'p xizmat",
    "IP — uyning manzili, port — o'sha uydagi xonaning raqami.",
    """// Bitta IP, ikki xil port — ikki xil xizmat
#include <WiFi.h>

const char* WIFI_NOM   = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";

WiFiServer server80(80);      // veb-sahifa uchun standart port
WiFiServer server8080(8080);  // ikkinchi xizmat uchun

const int LED = 2;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }

  server80.begin();
  server8080.begin();

  Serial.println("\\nIkki xizmat ishga tushdi:");
  Serial.print("  Sahifa:  http://"); Serial.print(WiFi.localIP()); Serial.println("/");
  Serial.print("  Xizmat:  http://"); Serial.print(WiFi.localIP()); Serial.println(":8080/");
}

void loop() {
  WiFiClient c1 = server80.available();
  if (c1) {
    c1.println("HTTP/1.1 200 OK");
    c1.println("Content-Type: text/html\\n");
    c1.println("<h1>80-port: asosiy sahifa</h1>");
    c1.stop();
    digitalWrite(LED, HIGH); delay(100); digitalWrite(LED, LOW);
  }

  WiFiClient c2 = server8080.available();
  if (c2) {
    c2.println("HTTP/1.1 200 OK");
    c2.println("Content-Type: text/plain\\n");
    c2.print("8080-port: sensor qiymati = ");
    c2.println(analogRead(34));
    c2.stop();
  }
}""",
    amaliy="ESP32 da ikki portda ikki xizmat ishga tushirib, brauzerdan ikkalasini "
           "ham ochish va bitta IP orqali bir nechta xizmat ishlashini amalda "
           "ko'rsatish"),

"Veb-server yaratish": K(
    "Brauzerdan LEDni boshqaruvchi veb-server",
    "ESP32 brauzerga HTML sahifa yuboradi, sahifadagi havolalar esa "
    "qurilmani boshqaradi.",
    """// Veb-server: brauzerdan LEDni boshqarish
#include <WiFi.h>

const char* WIFI_NOM   = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";

WiFiServer server(80);
const int LED = 2;
bool yongan = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);

  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }

  server.begin();
  Serial.print("\\nBrauzerda oching: http://");
  Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient client = server.available();
  if (!client) return;

  String sorov = client.readStringUntil('\\r');
  client.readStringUntil('\\n');

  // manzilga qarab qaror qabul qilamiz
  if (sorov.indexOf("GET /yoq") >= 0)   { yongan = true;  }
  if (sorov.indexOf("GET /ochir") >= 0) { yongan = false; }
  digitalWrite(LED, yongan);

  // javob: HTTP sarlavhasi + HTML sahifa
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html; charset=utf-8");
  client.println("Connection: close");
  client.println();
  client.println("<!DOCTYPE html><html><head><meta charset='utf-8'>");
  client.println("<meta name='viewport' content='width=device-width,initial-scale=1'>");
  client.println("<style>body{font-family:sans-serif;text-align:center;padding:40px}");
  client.println("a{display:inline-block;padding:16px 34px;margin:10px;border-radius:10px;");
  client.println("color:#fff;text-decoration:none;font-size:20px}");
  client.println(".y{background:#2e7d32}.o{background:#c62828}</style></head><body>");
  client.println("<h1>ESP32 boshqaruvi</h1>");
  client.print("<p>Holat: <b>");
  client.print(yongan ? "YONIQ" : "O'CHIQ");
  client.println("</b></p>");
  client.println("<a class='y' href='/yoq'>YOQISH</a>");
  client.println("<a class='o' href='/ochir'>O'CHIRISH</a>");
  client.println("</body></html>");

  client.stop();
  Serial.println(yongan ? "LED yoqildi" : "LED o'chirildi");
}""",
    amaliy="ESP32 ga LED ulab veb-server ishga tushirish, telefon brauzeridan "
           "sahifani ochib LEDni yoqib-o'chirish va sinf ichidagi boshqa "
           "o'quvchilar ham shu sahifaga kira olishini sinash"),

"HTML sahifani platadan yuborish": K(
    "Stilli va sensor qiymati bilan sahifa",
    "HTML — sahifaning skeleti, CSS — ko'rinishi. Ikkalasi ham oddiy matn "
    "sifatida yuboriladi.",
    """// To'liq HTML sahifa: stil + sensor qiymati
#include <WiFi.h>
const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiServer server(80);
const int SENSOR = 34;

String sahifa() {
  int xom = analogRead(SENSOR);
  int foiz = map(xom, 0, 4095, 0, 100);

  String h = "<!DOCTYPE html><html><head><meta charset='utf-8'>";
  h += "<meta name='viewport' content='width=device-width,initial-scale=1'>";
  h += "<meta http-equiv='refresh' content='3'>";     // 3 sekundda yangilanadi
  h += "<title>Sensor</title><style>";
  h += "body{font-family:sans-serif;background:#f4f6f5;margin:0;padding:30px;text-align:center}";
  h += ".karta{background:#fff;max-width:420px;margin:0 auto;padding:26px;";
  h += "border-radius:14px;box-shadow:0 2px 12px rgba(0,0,0,.08)}";
  h += ".son{font-size:56px;font-weight:700;color:#2e7d32}";
  h += ".chiziq{height:14px;background:#e0e0e0;border-radius:8px;overflow:hidden;margin-top:18px}";
  h += ".ichi{height:100%;background:#2e7d32}";
  h += "</style></head><body><div class='karta'>";
  h += "<h2>Yorug'lik darajasi</h2>";
  h += "<div class='son'>" + String(foiz) + " %</div>";
  h += "<div class='chiziq'><div class='ichi' style='width:" + String(foiz) + "%'></div></div>";
  h += "<p>Xom qiymat: " + String(xom) + " / 4095</p>";
  h += "</div></body></html>";
  return h;
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  server.begin();
  Serial.print("http://"); Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient c = server.available();
  if (!c) return;
  c.readStringUntil('\\n');
  c.println("HTTP/1.1 200 OK");
  c.println("Content-Type: text/html; charset=utf-8");
  c.println("Connection: close\\n");
  c.println(sahifa());
  c.stop();
}""",
    amaliy="Fotorezistorni ESP32 ga ulab, qiymatini stilli veb-sahifada progress "
           "chizig'i bilan ko'rsatish; sensorni qo'l bilan yopib, sahifadagi "
           "raqam o'zgarishini kuzatish"),

"CSS bilan sahifani chiroyli qilish": K(
    "Bir xil sahifa — stilsiz va stil bilan",
    "CSS mazmunni o'zgartirmaydi, faqat ko'rinishini boshqaradi.",
    """// Stilsiz va stil bilan — ikki sahifani solishtirish
#include <WiFi.h>
const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiServer server(80);
const int SENSOR = 34, LED = 2;

String stilsiz(int q) {
  return "<html><body><h1>Sensor</h1><p>Qiymat: " + String(q) + "</p>"
         "<a href='/yoq'>Yoqish</a> <a href='/ochir'>O'chirish</a></body></html>";
}

String stilBilan(int q) {
  String h = "<!DOCTYPE html><html><head><meta charset='utf-8'>";
  h += "<meta name='viewport' content='width=device-width,initial-scale=1'><style>";
  h += "*{box-sizing:border-box}";
  h += "body{font-family:system-ui,sans-serif;background:#eef2f0;margin:0;padding:24px}";
  h += ".k{background:#fff;max-width:460px;margin:0 auto;padding:28px;border-radius:16px;";
  h += "box-shadow:0 4px 20px rgba(0,0,0,.08)}";
  h += "h1{margin:0 0 6px;font-size:22px;color:#1b3b2a}";
  h += ".q{font-size:52px;font-weight:700;color:#2e7d32;margin:10px 0}";
  h += ".tugmalar{display:flex;gap:12px;margin-top:20px}";
  h += "a{flex:1;text-align:center;padding:15px;border-radius:10px;color:#fff;";
  h += "text-decoration:none;font-weight:600}";
  h += ".y{background:#2e7d32}.o{background:#b23b3b}";
  h += "@media(max-width:420px){.tugmalar{flex-direction:column}}";
  h += "</style></head><body><div class='k'>";
  h += "<h1>Yorug'lik sensori</h1>";
  h += "<div class='q'>" + String(q) + "</div>";
  h += "<div class='tugmalar'><a class='y' href='/yoq'>YOQISH</a>";
  h += "<a class='o' href='/ochir'>O'CHIRISH</a></div>";
  h += "</div></body></html>";
  return h;
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  server.begin();
  Serial.print("http://"); Serial.println(WiFi.localIP());
  Serial.println("Stilsiz variant: /oddiy");
}

void loop() {
  WiFiClient c = server.available();
  if (!c) return;
  String s = c.readStringUntil('\\r');
  c.readStringUntil('\\n');

  if (s.indexOf("/yoq") > 0)   digitalWrite(LED, HIGH);
  if (s.indexOf("/ochir") > 0) digitalWrite(LED, LOW);

  int q = analogRead(SENSOR);
  c.println("HTTP/1.1 200 OK");
  c.println("Content-Type: text/html; charset=utf-8\\n");
  c.println(s.indexOf("/oddiy") > 0 ? stilsiz(q) : stilBilan(q));
  c.stop();
}""",
    amaliy="Bitta ESP32 da ikki sahifa (stilsiz va stilli) chiqarib, telefon "
           "brauzerida ikkalasini yonma-yon ochish va CSS ning ta'sirini "
           "muhokama qilish"),

"Sensor qiymatini veb-sahifada ko'rsatish": K(
    "Sensor qiymati sahifada, avtomatik yangilanadi",
    "meta refresh — eng oson usul. Butun sahifa qayta yuklanadi.",
    """// Sensor qiymati sahifada — har 2 sekundda yangilanadi
#include <WiFi.h>
const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiServer server(80);
const int LDR = 34, TERM = 35;

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  server.begin();
  Serial.print("http://"); Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient c = server.available();
  if (!c) return;
  c.readStringUntil('\\n');

  int yoruglik = map(analogRead(LDR),  0, 4095, 0, 100);
  int harorat  = map(analogRead(TERM), 0, 4095, 0, 50);

  c.println("HTTP/1.1 200 OK");
  c.println("Content-Type: text/html; charset=utf-8\\n");
  c.println("<!DOCTYPE html><html><head><meta charset='utf-8'>");
  c.println("<meta http-equiv='refresh' content='2'>");   // 2 sekundda yangilash
  c.println("<style>body{font-family:sans-serif;padding:30px;background:#f2f5f3}");
  c.println("table{border-collapse:collapse;margin:0 auto;background:#fff;");
  c.println("box-shadow:0 2px 10px rgba(0,0,0,.08);border-radius:10px;overflow:hidden}");
  c.println("td,th{padding:14px 26px;border-bottom:1px solid #eee;font-size:18px}");
  c.println("th{background:#2e7d32;color:#fff}</style></head><body>");
  c.println("<table><tr><th>Ko'rsatkich</th><th>Qiymat</th></tr>");
  c.print("<tr><td>Yorug'lik</td><td>"); c.print(yoruglik); c.println(" %</td></tr>");
  c.print("<tr><td>Harorat</td><td>");   c.print(harorat);  c.println(" C</td></tr>");
  c.print("<tr><td>Ish vaqti</td><td>"); c.print(millis()/1000); c.println(" s</td></tr>");
  c.println("</table></body></html>");
  c.stop();
}""",
    amaliy="Fotorezistor va termistorni ESP32 ga ulab, ikkala qiymatni jadval "
           "ko'rinishida sahifada chiqarish va sahifa avtomatik yangilanishini "
           "sinash"),

"Sahifani avtomatik yangilash (AJAX g'oyasi)": K(
    "Faqat SONNI yangilash — butun sahifani emas",
    "meta refresh butun sahifani qayta yuklaydi (miltillaydi). AJAX faqat "
    "kerakli qiymatni oladi — sahifa silliq yangilanadi.",
    """// AJAX: sahifa bir marta yuklanadi, keyin faqat SON yangilanadi
#include <WiFi.h>
const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiServer server(80);
const int SENSOR = 34;

const char* SAHIFA =
"<!DOCTYPE html><html><head><meta charset='utf-8'>"
"<meta name='viewport' content='width=device-width,initial-scale=1'>"
"<style>body{font-family:sans-serif;text-align:center;padding:40px;background:#f2f5f3}"
".q{font-size:64px;font-weight:700;color:#2e7d32}</style></head><body>"
"<h2>Sensor qiymati</h2><div class='q' id='q'>...</div>"
"<script>"
"setInterval(function(){"
"  fetch('/qiymat').then(r=>r.text()).then(t=>{document.getElementById('q').textContent=t;});"
"}, 500);"          // yarim sekundda bir marta — sahifa miltillamaydi
"</script></body></html>";

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  server.begin();
  Serial.print("http://"); Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient c = server.available();
  if (!c) return;
  String s = c.readStringUntil('\\r');
  c.readStringUntil('\\n');

  if (s.indexOf("GET /qiymat") >= 0) {
    // FAQAT son yuboriladi — bir necha bayt
    c.println("HTTP/1.1 200 OK");
    c.println("Content-Type: text/plain\\n");
    c.println(analogRead(SENSOR));
  } else {
    c.println("HTTP/1.1 200 OK");
    c.println("Content-Type: text/html; charset=utf-8\\n");
    c.println(SAHIFA);
  }
  c.stop();
}""",
    amaliy="Avval meta refresh bilan, keyin AJAX bilan sahifa yasab, ikkalasini "
           "telefon brauzerida ochish; sahifa miltillashi va yuklanadigan "
           "ma'lumot hajmidagi farqni muhokama qilish"),

"Brauzerdan qurilmani boshqarish": K(
    "Slayder bilan yorqinlik va tugmalar bilan rele",
    "HTML forma elementlari qurilmaning haqiqiy sozlamalariga bog'lanadi.",
    """// Brauzerdan: slayder -> LED yorqinligi, tugma -> rele
#include <WiFi.h>
const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiServer server(80);

const int LED = 2, RELE = 5;
int yorqinlik = 0;
bool releYoniq = false;

void setup() {
  Serial.begin(115200);
  pinMode(RELE, OUTPUT);
  ledcAttach(LED, 5000, 8);

  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  server.begin();
  Serial.print("http://"); Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient c = server.available();
  if (!c) return;
  String s = c.readStringUntil('\\r');
  c.readStringUntil('\\n');

  // /yorqinlik?q=180 ko'rinishidagi so'rovni ajratamiz
  int p = s.indexOf("/yorqinlik?q=");
  if (p >= 0) {
    yorqinlik = s.substring(p + 13, s.indexOf(' ', p + 13)).toInt();
    ledcWrite(LED, yorqinlik);
  }
  if (s.indexOf("/rele") >= 0) {
    releYoniq = !releYoniq;
    digitalWrite(RELE, releYoniq);
  }

  c.println("HTTP/1.1 200 OK");
  c.println("Content-Type: text/html; charset=utf-8\\n");
  c.println("<!DOCTYPE html><html><head><meta charset='utf-8'>");
  c.println("<meta name='viewport' content='width=device-width,initial-scale=1'>");
  c.println("<style>body{font-family:sans-serif;padding:30px;text-align:center}");
  c.println("input[type=range]{width:90%;height:34px}");
  c.println("a{display:inline-block;padding:14px 30px;background:#2e7d32;color:#fff;");
  c.println("border-radius:10px;text-decoration:none;margin-top:20px}</style></head><body>");
  c.println("<h2>Qurilma boshqaruvi</h2>");
  c.print("<p>Yorqinlik: <b id='v'>"); c.print(yorqinlik); c.println("</b></p>");
  c.print("<input type='range' min='0' max='255' value='"); c.print(yorqinlik);
  c.println("' oninput=\\"document.getElementById('v').textContent=this.value;");
  c.println("fetch('/yorqinlik?q='+this.value)\\">");
  c.print("<br><a href='/rele'>Rele: ");
  c.print(releYoniq ? "YONIQ" : "O'CHIQ");
  c.println("</a></body></html>");
  c.stop();
}""",
    amaliy="ESP32 ga LED va rele modulini ulab, brauzerdagi slayder bilan "
           "yorqinlikni, tugma bilan relени boshqarish; telefondan boshqarib "
           "kechikishni o'lchash"),

"Veb-server va API tushunchasi": K(
    "Sahifa va API — ikki xil javob",
    "Sahifa ODAM uchun (HTML), API esa DASTUR uchun (JSON).",
    """// Bitta qurilma, ikki xil javob: odamga HTML, dasturga JSON
#include <WiFi.h>
const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiServer server(80);
const int LDR = 34, TERM = 35;

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  server.begin();
  Serial.print("Sahifa (odam uchun): http://"); Serial.println(WiFi.localIP());
  Serial.print("API (dastur uchun):  http://"); Serial.print(WiFi.localIP());
  Serial.println("/api");
}

void loop() {
  WiFiClient c = server.available();
  if (!c) return;
  String s = c.readStringUntil('\\r');
  c.readStringUntil('\\n');

  int y = analogRead(LDR), t = analogRead(TERM);

  if (s.indexOf("GET /api") >= 0) {
    // DASTUR uchun: JSON — mashina o'qishiga qulay
    c.println("HTTP/1.1 200 OK");
    c.println("Content-Type: application/json");
    c.println("Access-Control-Allow-Origin: *\\n");
    c.print("{\\"yoruglik\\":");  c.print(y);
    c.print(",\\"harorat\\":");   c.print(t);
    c.print(",\\"vaqt\\":");      c.print(millis() / 1000);
    c.println("}");
  } else {
    // ODAM uchun: HTML — o'qishga qulay
    c.println("HTTP/1.1 200 OK");
    c.println("Content-Type: text/html; charset=utf-8\\n");
    c.println("<html><body style='font-family:sans-serif;padding:30px'>");
    c.print("<h2>Yorug'lik: "); c.print(y); c.println("</h2>");
    c.print("<h2>Harorat: ");   c.print(t); c.println("</h2>");
    c.println("<p><a href='/api'>API javobini ko'rish (JSON)</a></p>");
    c.println("</body></html>");
  }
  c.stop();
}""",
    amaliy="ESP32 da bitta manzilda HTML, boshqasida JSON javob beruvchi server "
           "yasash; ikkalasini brauzerda ochib, farqini ko'rish va JSON ni "
           "boshqa dastur qanday o'qishini muhokama qilish"),

"JSON formati bilan ishlash": K(
    "JSON tuzish va o'qish (ArduinoJson)",
    "JSON — qurilmalar o'rtasida ma'lumot almashishning standart formati.",
    """// ArduinoJson: JSON tuzish va o'qish
#include <ArduinoJson.h>
const int LDR = 34, TERM = 35, LED = 2;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
}

void loop() {
  // --- 1) JSON TUZISH ---
  JsonDocument doc;
  doc["qurilma"]  = "meteo-01";
  doc["vaqt"]     = millis() / 1000;
  doc["yoruglik"] = analogRead(LDR);
  doc["harorat"]  = analogRead(TERM) * 50.0 / 4095.0;

  JsonArray tarix = doc["tarix"].to<JsonArray>();
  tarix.add(analogRead(LDR));
  tarix.add(analogRead(LDR));

  String matn;
  serializeJson(doc, matn);
  Serial.print("Tuzilgan JSON: "); Serial.println(matn);

  // --- 2) JSON O'QISH ---
  String kelgan = "{\\"buyruq\\":\\"yoq\\",\\"yorqinlik\\":200}";
  JsonDocument kirish;
  DeserializationError xato = deserializeJson(kirish, kelgan);

  if (xato) {
    Serial.print("JSON xatosi: "); Serial.println(xato.c_str());
  } else {
    const char* buyruq = kirish["buyruq"];
    int yorq = kirish["yorqinlik"];
    Serial.print("Buyruq: "); Serial.print(buyruq);
    Serial.print("  yorqinlik: "); Serial.println(yorq);

    if (String(buyruq) == "yoq") digitalWrite(LED, HIGH);
  }
  delay(3000);
}""",
    amaliy="ESP32 da sensor qiymatlaridan JSON tuzib Serial monitorda chiqarish, "
           "keyin tayyor JSON matnni o'qib, undagi buyruq bilan LEDni "
           "boshqarish"),

"HTTP so'rov yuborish": K(
    "ESP32 tashqi serverdan ma'lumot oladi",
    "Bu safar ESP32 — mijoz (client), server emas.",
    """// ESP32 tashqi serverga so'rov yuboradi
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const int LED = 2;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println("\\nUlandi.");
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) { delay(2000); return; }

  HTTPClient http;

  // GET so'rov: serverdan ma'lumot OLAMIZ
  http.begin("http://worldtimeapi.org/api/timezone/Asia/Tashkent");
  int kod = http.GET();

  Serial.print("HTTP javob kodi: "); Serial.println(kod);
  // 200 = muvaffaqiyat, 404 = topilmadi, 500 = server xatosi

  if (kod == 200) {
    digitalWrite(LED, HIGH);
    String javob = http.getString();
    Serial.println("Javob (birinchi 200 belgi):");
    Serial.println(javob.substring(0, 200));
  } else {
    digitalWrite(LED, LOW);
    Serial.println("So'rov muvaffaqiyatsiz");
  }

  http.end();          // MAJBURIY — aloqani yopadi, aks holda xotira tugaydi
  delay(15000);
}""",
    amaliy="ESP32 ni internetga ulab, ochiq API dan vaqt ma'lumotini olish, "
           "javob kodini LED bilan ko'rsatish va turli xato kodlarini ataylab "
           "hosil qilib (noto'g'ri manzil) natijani kuzatish"),

"HTTP GET va POST so'rovlari": K(
    "GET — olish, POST — yuborish",
    "GET so'rovda ma'lumot manzilda ko'rinadi, POST da esa yashirin tanada "
    "yuboriladi.",
    """// GET va POST farqi
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const int SENSOR = 34;

void getSorov() {
  HTTPClient http;
  // ma'lumot MANZILDA ko'rinadi — hamma ko'radi
  http.begin("http://httpbin.org/get?qurilma=esp32&qiymat=" + String(analogRead(SENSOR)));
  int kod = http.GET();
  Serial.print("GET javob: "); Serial.println(kod);
  if (kod == 200) Serial.println(http.getString().substring(0, 200));
  http.end();
}

void postSorov() {
  HTTPClient http;
  http.begin("http://httpbin.org/post");
  http.addHeader("Content-Type", "application/json");

  // ma'lumot TANADA — manzilda ko'rinmaydi
  String tana = "{\\"qurilma\\":\\"esp32\\",\\"qiymat\\":" + String(analogRead(SENSOR)) + "}";
  int kod = http.POST(tana);

  Serial.print("POST javob: "); Serial.println(kod);
  if (kod == 200) Serial.println(http.getString().substring(0, 250));
  http.end();
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println("Ulandi.");
}

void loop() {
  Serial.println("\\n--- GET ---");  getSorov();
  delay(5000);
  Serial.println("\\n--- POST ---"); postSorov();
  delay(15000);
}""",
    amaliy="Sensorni ulab, uning qiymatini avval GET, keyin POST bilan sinov "
           "serveriga yuborish; server javobidan ma'lumot qayerda "
           "ko'rinayotganini topib, ikki usulning farqini yozib olish"),

"HTTP so'rov yuborish (client)": K(
    "Sensor qiymatini serverga muntazam yuborish",
    "Xatoga chidamlilik: so'rov muvaffaqiyatsiz bo'lsa dastur to'xtamasligi kerak.",
    """// Sensor qiymatini serverga muntazam yuborish (xatoga chidamli)
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const int SENSOR = 34, LED_OK = 2, LED_XATO = 4;

unsigned long oxirgi = 0;
const unsigned long ORALIQ = 30000;    // 30 sekundda bir
int yuborilgan = 0, xatolar = 0;

void setup() {
  Serial.begin(115200);
  pinMode(LED_OK, OUTPUT); pinMode(LED_XATO, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println("Ulandi.");
}

void loop() {
  if (millis() - oxirgi < ORALIQ) return;
  oxirgi = millis();

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi yo'q — qayta ulanmoqda");
    WiFi.reconnect();
    return;
  }

  HTTPClient http;
  http.begin("http://httpbin.org/post");
  http.addHeader("Content-Type", "application/json");
  http.setTimeout(8000);                   // 8 sekunddan ko'p kutmaymiz

  String tana = "{\\"qiymat\\":" + String(analogRead(SENSOR)) +
                ",\\"vaqt\\":" + String(millis() / 1000) + "}";
  int kod = http.POST(tana);
  http.end();

  if (kod == 200) {
    yuborilgan++;
    digitalWrite(LED_OK, HIGH); delay(200); digitalWrite(LED_OK, LOW);
  } else {
    xatolar++;
    digitalWrite(LED_XATO, HIGH); delay(200); digitalWrite(LED_XATO, LOW);
  }

  Serial.print("kod="); Serial.print(kod);
  Serial.print("  yuborilgan="); Serial.print(yuborilgan);
  Serial.print("  xato=");       Serial.println(xatolar);
}""",
    amaliy="Sensorni ulab, qiymatni 30 sekundda bir serverga yuborish; WiFi ni "
           "ataylab o'chirib, dastur to'xtamasligini va qayta ulanishini "
           "tekshirish"),

"Bulut xizmatiga ma'lumot yuborish": K(
    "ThingSpeak ga o'lchov yuborish",
    "Bulut xizmati ma'lumotni saqlaydi va grafikda ko'rsatadi.",
    """// ThingSpeak ga sensor qiymatini yuborish
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const char* API_KALIT = "SIZNING_WRITE_API_KEY";   // ThingSpeak kanalidan

const int LDR = 34, TERM = 35, LED = 2;
unsigned long oxirgi = 0;
const unsigned long ORALIQ = 20000;   // ThingSpeak bepul: 15 sekunddan tez emas

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println("Ulandi. Ma'lumot yuborish boshlandi.");
}

void loop() {
  if (millis() - oxirgi < ORALIQ) return;
  oxirgi = millis();

  int yoruglik = analogRead(LDR);
  float harorat = analogRead(TERM) * 50.0 / 4095.0;

  String url = "http://api.thingspeak.com/update?api_key=";
  url += API_KALIT;
  url += "&field1=" + String(yoruglik);
  url += "&field2=" + String(harorat, 1);

  HTTPClient http;
  http.begin(url);
  int kod = http.GET();
  String javob = http.getString();
  http.end();

  // ThingSpeak javob sifatida yozuv raqamini qaytaradi; 0 = xato
  Serial.print("kod="); Serial.print(kod);
  Serial.print("  yozuv raqami="); Serial.println(javob);

  digitalWrite(LED, javob.toInt() > 0);
}""",
    amaliy="ThingSpeak da bepul kanal ochib, ESP32 dan yorug'lik va harorat "
           "qiymatlarini 20 sekundda bir yuborish va bulutdagi grafik jonli "
           "to'lib borishini kuzatish"),

"Bulut platformasiga ulanish": K(
    "Kanal sozlash va birinchi yozuv",
    "Har bir bulut xizmatida uch narsa bo'ladi: kanal, kalit va maydonlar.",
    """// Bulutga ulanish: kanal, kalit, maydonlar
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const char* YOZISH_KALIT = "SIZNING_WRITE_API_KEY";
const char* OQISH_KALIT  = "SIZNING_READ_API_KEY";
const char* KANAL_ID     = "0000000";

void yubor(float f1, float f2) {
  HTTPClient http;
  String url = "http://api.thingspeak.com/update?api_key=" + String(YOZISH_KALIT)
             + "&field1=" + String(f1, 2) + "&field2=" + String(f2, 2);
  http.begin(url);
  Serial.print("Yuborildi, javob: "); Serial.println(http.GET());
  http.end();
}

void oqi() {
  HTTPClient http;
  String url = "http://api.thingspeak.com/channels/" + String(KANAL_ID)
             + "/feeds/last.json?api_key=" + String(OQISH_KALIT);
  http.begin(url);
  if (http.GET() == 200) {
    Serial.print("Oxirgi yozuv: ");
    Serial.println(http.getString());
  }
  http.end();
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println("Ulandi.");
}

void loop() {
  yubor(analogRead(34) * 100.0 / 4095.0, analogRead(35) * 50.0 / 4095.0);
  delay(3000);
  oqi();                 // yozganimizni QAYTA O'QIB tekshiramiz
  delay(20000);
}""",
    amaliy="Bulut kanalini ochib, yozish va o'qish kalitlarini olish, ikki "
           "sensordan ma'lumot yuborish va yuborilgan yozuvni qayta o'qib "
           "tekshirish"),

"Bulutda grafik ko'rish va tahlil qilish": K(
    "Ma'lumotni tahlil qilish uchun tayyorlash",
    "Grafikda ma'noli xulosa chiqishi uchun o'lchov ORALIG'I bir xil bo'lishi "
    "va ortiqcha shovqin filtrlanishi kerak.",
    """// Bulutga TOZALANGAN ma'lumot yuborish
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const char* API_KALIT = "SIZNING_WRITE_API_KEY";
const int SENSOR = 34;

const int N = 20;
float tarix[N];
int joy = 0;
unsigned long oxirgi = 0;

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  for (int i = 0; i < N; i++) tarix[i] = analogRead(SENSOR);
}

void loop() {
  // 1) tez-tez o'lchaymiz va tarixni to'ldiramiz
  tarix[joy] = analogRead(SENSOR);
  joy = (joy + 1) % N;
  delay(500);

  // 2) 30 sekundda bir marta — TOZALANGAN qiymatni yuboramiz
  if (millis() - oxirgi < 30000) return;
  oxirgi = millis();

  // o'rtacha, eng katta, eng kichik
  float y = 0, katta = 0, kichik = 4095;
  for (int i = 0; i < N; i++) {
    y += tarix[i];
    if (tarix[i] > katta)  katta  = tarix[i];
    if (tarix[i] < kichik) kichik = tarix[i];
  }
  float ortacha = y / N;

  HTTPClient http;
  String url = "http://api.thingspeak.com/update?api_key=" + String(API_KALIT)
             + "&field1=" + String(ortacha, 1)
             + "&field2=" + String(katta, 0)
             + "&field3=" + String(kichik, 0);
  http.begin(url);
  int kod = http.GET();
  http.end();

  Serial.print("o'rtacha="); Serial.print(ortacha, 1);
  Serial.print(" katta=");   Serial.print(katta, 0);
  Serial.print(" kichik=");  Serial.print(kichik, 0);
  Serial.print("  javob=");  Serial.println(kod);
}""",
    amaliy="Sensordan yarim sekundda o'lchab, 30 sekundlik o'rtacha, eng katta "
           "va eng kichik qiymatni bulutga yuborish; xom qiymat grafigi bilan "
           "tozalangan grafikni yonma-yon solishtirish"),

"Bulutda grafik va tahlil": K(
    "Kunlik o'lchov va xulosа chiqarish",
    "Grafikdan xulosa chiqarish — ma'lumotni yig'ishdan ham muhimroq bosqich.",
    """// Kun davomida o'lchash va statistika yuborish
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const char* API_KALIT = "SIZNING_WRITE_API_KEY";
const int SENSOR = 34;

unsigned long oxirgi = 0;
long yigindi = 0; int soni = 0;
int engKatta = 0, engKichik = 4095;

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println("Kuzatuv boshlandi.");
}

void loop() {
  int q = analogRead(SENSOR);
  yigindi += q; soni++;
  if (q > engKatta)  engKatta  = q;
  if (q < engKichik) engKichik = q;
  delay(1000);

  if (millis() - oxirgi < 60000) return;    // daqiqada bir marta
  oxirgi = millis();

  float ortacha = (float)yigindi / soni;
  float tebranish = engKatta - engKichik;   // qanchalik beqaror

  HTTPClient http;
  String url = "http://api.thingspeak.com/update?api_key=" + String(API_KALIT)
             + "&field1=" + String(ortacha, 1)
             + "&field2=" + String(tebranish, 0);
  http.begin(url); http.GET(); http.end();

  Serial.print("daqiqa yakuni -> o'rtacha="); Serial.print(ortacha, 1);
  Serial.print("  tebranish=");               Serial.println(tebranish);

  // yangi daqiqa uchun nolga qaytaramiz
  yigindi = 0; soni = 0; engKatta = 0; engKichik = 4095;
}""",
    amaliy="Sensordan bir necha soat ma'lumot yig'ib, bulutdagi grafikni tahlil "
           "qilish: qaysi vaqtda qiymat eng katta bo'lgan, tebranish qachon "
           "ortgan degan savollarga grafik asosida javob yozish"),

"Ma'lumotni vizualizatsiya qilish": K(
    "Qurilmaning o'zida grafik chizish",
    "Bulutsiz ham grafik chizish mumkin — OLED ekranda yoki veb-sahifada.",
    """// OLED ekranda jonli grafik chizish
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
Adafruit_SSD1306 ekran(128, 64, &Wire, -1);

const int SENSOR = 34;
int grafik[128];        // ekran kengligicha nuqta
int joy = 0;

void setup() {
  Serial.begin(115200);
  ekran.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  ekran.setTextColor(SSD1306_WHITE);
  for (int i = 0; i < 128; i++) grafik[i] = 0;
}

void loop() {
  // yangi qiymatni oxiriga qo'shamiz, eskilarni chapga suramiz
  for (int i = 0; i < 127; i++) grafik[i] = grafik[i + 1];
  grafik[127] = map(analogRead(SENSOR), 0, 4095, 0, 45);

  ekran.clearDisplay();

  // sarlavha
  ekran.setTextSize(1);
  ekran.setCursor(0, 0);
  ekran.print("Sensor: ");
  ekran.print(grafik[127]);

  // grafik: har bir nuqtani chizamiz
  for (int i = 0; i < 127; i++) {
    ekran.drawLine(i, 63 - grafik[i], i + 1, 63 - grafik[i + 1], SSD1306_WHITE);
  }
  ekran.drawFastHLine(0, 63, 128, SSD1306_WHITE);    // asos chizig'i

  ekran.display();
  delay(100);
}""",
    amaliy="OLED ekran va sensorni ESP32 ga ulab, ekranda siljib boruvchi jonli "
           "grafik chizish; sensorni qo'l bilan yopib, grafikning javob "
           "tezligini kuzatish"),

"Ma'lumotni filtrlash (o'rtacha, silliqlash)": K(
    "Uch xil filtr yonma-yon",
    "Xom qiymat, oddiy o'rtacha va eksponensial silliqlash — uchtasi bir "
    "grafikda.",
    """// Uch xil filtrni SOLISHTIRISH (Serial Plotter uchun)
const int SENSOR = 34;

const int N = 10;
int tarix[N]; int joy = 0;
float silliq = 0;
const float ALFA = 0.15;      // kichik alfa = kuchli silliqlash

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < N; i++) tarix[i] = analogRead(SENSOR);
  silliq = analogRead(SENSOR);
}

void loop() {
  int xom = analogRead(SENSOR);

  // 1) siljuvchi o'rtacha — oxirgi N qiymat o'rtachasi
  tarix[joy] = xom;
  joy = (joy + 1) % N;
  long y = 0;
  for (int i = 0; i < N; i++) y += tarix[i];
  int ortacha = y / N;

  // 2) eksponensial silliqlash — xotira kam, javob tez
  silliq = ALFA * xom + (1 - ALFA) * silliq;

  // Serial Plotter uchun uch chiziq
  Serial.print(xom);      Serial.print(" ");
  Serial.print(ortacha);  Serial.print(" ");
  Serial.println((int)silliq);

  delay(50);
}

// Plotterda: xom chiziq "tishli", o'rtacha silliqroq,
// eksponensial esa silliq lekin o'zgarishga tezroq javob beradi.""",
    amaliy="Sensorni ulab, xom qiymat, siljuvchi o'rtacha va eksponensial "
           "silliqlashni Serial Plotter'da uch chiziq bilan solishtirish; ALFA "
           "koeffitsientini o'zgartirib, javob tezligi va silliqlik "
           "muvozanatini topish"),

# ==================================================== ESP32 — MQTT, TELEGRAM, QUVVAT
"MQTT protokoli": K(
    "MQTT bilan xabar yuborish va qabul qilish",
    "MQTT — IoT uchun yengil protokol: qurilma broker orqali mavzuga "
    "(topic) yozadi va obuna bo'ladi.",
    """// MQTT: mavzuga yozish va obuna bo'lish
#include <WiFi.h>
#include <PubSubClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const char* BROKER = "broker.hivemq.com";     // bepul ochiq broker

WiFiClient wifi;
PubSubClient mqtt(wifi);

const int LED = 2, SENSOR = 34;
unsigned long oxirgi = 0;

// broker xabar yuborganda shu funksiya chaqiriladi
void kelganXabar(char* mavzu, byte* xabar, unsigned int uzunlik) {
  String matn;
  for (unsigned int i = 0; i < uzunlik; i++) matn += (char)xabar[i];

  Serial.print("Kelgan xabar ["); Serial.print(mavzu);
  Serial.print("]: "); Serial.println(matn);

  if (matn == "yoq")   digitalWrite(LED, HIGH);
  if (matn == "ochir") digitalWrite(LED, LOW);
}

void ulan() {
  while (!mqtt.connected()) {
    Serial.print("MQTT ga ulanmoqda...");
    String id = "tarbion-" + String(random(0xffff), HEX);
    if (mqtt.connect(id.c_str())) {
      Serial.println(" ulandi!");
      mqtt.subscribe("tarbion/buyruq");        // OBUNA bo'lamiz
    } else {
      Serial.print(" xato="); Serial.println(mqtt.state());
      delay(3000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  mqtt.setServer(BROKER, 1883);
  mqtt.setCallback(kelganXabar);
}

void loop() {
  if (!mqtt.connected()) ulan();
  mqtt.loop();                                 // MAJBURIY

  if (millis() - oxirgi > 5000) {
    oxirgi = millis();
    String q = String(analogRead(SENSOR));
    mqtt.publish("tarbion/sensor", q.c_str()); // mavzuga YOZAMIZ
    Serial.print("Yuborildi: "); Serial.println(q);
  }
}""",
    amaliy="ESP32 ni ochiq MQTT brokerga ulab, sensor qiymatini mavzuga yozish "
           "va telefondagi MQTT ilovasidan buyruq yuborib LEDni boshqarish"),

"MQTT protokoli haqida tushuncha": K(
    "Broker, mavzu, obuna — uch tushuncha amalda",
    "MQTT da qurilmalar bir-birini BILMAYDI. Ular faqat brokerni va mavzu "
    "nomini biladi.",
    """// MQTT uch tushunchasi: broker, mavzu, obuna
#include <WiFi.h>
#include <PubSubClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const char* BROKER = "broker.hivemq.com";

WiFiClient wifi;
PubSubClient mqtt(wifi);
const int LED = 2, ZUMMER = 5, SENSOR = 34;

void kelgan(char* mavzu, byte* x, unsigned int n) {
  String m = String(mavzu), matn;
  for (unsigned int i = 0; i < n; i++) matn += (char)x[i];

  Serial.print("["); Serial.print(m); Serial.print("] -> "); Serial.println(matn);

  // MAVZUGA qarab har xil ish qilamiz
  if (m == "tarbion/chiroq") digitalWrite(LED, matn == "1");
  if (m == "tarbion/signal") tone(ZUMMER, matn.toInt(), 300);
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  mqtt.setServer(BROKER, 1883);
  mqtt.setCallback(kelgan);

  if (mqtt.connect("tarbion-sinf")) {
    // BIR NECHTA mavzuga obuna bo'lamiz
    mqtt.subscribe("tarbion/chiroq");
    mqtt.subscribe("tarbion/signal");
    Serial.println("Obuna bo'lindi: tarbion/chiroq, tarbion/signal");
  }
}

void loop() {
  mqtt.loop();
  static unsigned long t = 0;
  if (millis() - t > 10000) {
    t = millis();
    mqtt.publish("tarbion/sensor", String(analogRead(SENSOR)).c_str());
  }
}""",
    amaliy="Ikki juftlik ikkita ESP32 ni bir brokerga ulab, biri mavzuga yozib, "
           "ikkinchisi obuna bo'lib buyruqni qabul qilishini sinash; brokerni "
           "o'chirib, aloqa uzilishini kuzatish"),

"MQTT: broker, mavzu (topic), obuna": K(
    "Mavzu daraxti va joker belgilar",
    "Mavzu papkaga o'xshaydi: uy/oshxona/harorat. + va # joker belgilari "
    "bir necha mavzuga birdan obuna bo'lishga imkon beradi.",
    """// Mavzu daraxti va joker belgilar
#include <WiFi.h>
#include <PubSubClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiClient wifi;
PubSubClient mqtt(wifi);

void kelgan(char* mavzu, byte* x, unsigned int n) {
  String matn;
  for (unsigned int i = 0; i < n; i++) matn += (char)x[i];
  Serial.print(mavzu); Serial.print(" = "); Serial.println(matn);
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  mqtt.setServer("broker.hivemq.com", 1883);
  mqtt.setCallback(kelgan);
  mqtt.connect("tarbion-joker");

  // JOKER BELGILAR:
  mqtt.subscribe("tarbion/+/harorat");   // + = bitta daraja (oshxona, yotoqxona...)
  mqtt.subscribe("tarbion/#");           // # = qolgan HAMMA daraja
  Serial.println("Obuna: tarbion/+/harorat va tarbion/#");
}

void loop() {
  mqtt.loop();
  static unsigned long t = 0;
  if (millis() - t > 8000) {
    t = millis();
    // mavzu daraxtiga yozamiz
    mqtt.publish("tarbion/oshxona/harorat",   String(random(18, 30)).c_str());
    mqtt.publish("tarbion/yotoqxona/harorat", String(random(18, 30)).c_str());
    mqtt.publish("tarbion/oshxona/namlik",    String(random(30, 70)).c_str());
  }
}""",
    amaliy="Bir ESP32 dan uch xil mavzuga ma'lumot yuborib, joker belgi bilan "
           "obuna bo'lish natijasini kuzatish va mavzu daraxtini xonalar "
           "bo'yicha loyihalash"),

"MQTT bilan ikki tomonlama boshqaruv": K(
    "Qurilma ham yozadi, ham buyruq qabul qiladi",
    "Ikki tomonlama tizimda holat ham qaytariladi — buyruq bajarilganini "
    "tasdiqlash uchun.",
    """// Ikki tomonlama: buyruq qabul qilish + holatni qaytarish
#include <WiFi.h>
#include <PubSubClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiClient wifi;
PubSubClient mqtt(wifi);

const int LED = 2, RELE = 5, SENSOR = 34;
bool releYoniq = false;
int yorqinlik = 0;

void holatniYubor() {
  String h = "{\\"rele\\":" + String(releYoniq ? 1 : 0)
           + ",\\"yorqinlik\\":" + String(yorqinlik)
           + ",\\"sensor\\":" + String(analogRead(SENSOR)) + "}";
  mqtt.publish("tarbion/qurilma/holat", h.c_str());
  Serial.print("Holat yuborildi: "); Serial.println(h);
}

void kelgan(char* mavzu, byte* x, unsigned int n) {
  String m = String(mavzu), matn;
  for (unsigned int i = 0; i < n; i++) matn += (char)x[i];

  if (m == "tarbion/qurilma/rele") {
    releYoniq = (matn == "1");
    digitalWrite(RELE, releYoniq);
  }
  if (m == "tarbion/qurilma/yorqinlik") {
    yorqinlik = constrain(matn.toInt(), 0, 255);
    ledcWrite(LED, yorqinlik);
  }
  holatniYubor();                 // buyruq bajarilgach TASDIQ yuboramiz
}

void setup() {
  Serial.begin(115200);
  pinMode(RELE, OUTPUT);
  ledcAttach(LED, 5000, 8);

  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  mqtt.setServer("broker.hivemq.com", 1883);
  mqtt.setCallback(kelgan);
  if (mqtt.connect("tarbion-qurilma")) {
    mqtt.subscribe("tarbion/qurilma/rele");
    mqtt.subscribe("tarbion/qurilma/yorqinlik");
    holatniYubor();
  }
}

void loop() {
  if (!mqtt.connected()) { mqtt.connect("tarbion-qurilma"); delay(2000); return; }
  mqtt.loop();

  static unsigned long t = 0;
  if (millis() - t > 15000) { t = millis(); holatniYubor(); }
}""",
    amaliy="ESP32 ga LED va rele ulab, telefondan MQTT orqali buyruq yuborish va "
           "qurilmadan qaytgan tasdiq xabarini kuzatish; buyruq va tasdiq "
           "orasidagi vaqtni o'lchash"),

"Ikki ESP32 o'rtasida aloqa": K(
    "ESP-NOW: to'g'ridan-to'g'ri, WiFi tarmog'isiz",
    "ESP-NOW da router kerak emas — ikki plata bir-biri bilan bevosita "
    "gaplashadi. Masofa 100 metrgacha.",
    """// ESP-NOW: YUBORUVCHI plata
#include <esp_now.h>
#include <WiFi.h>

// QABUL QILUVCHI platanning MAC manzili (uni Serial monitordan oling)
uint8_t qabulMAC[] = {0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF};

typedef struct {
  int sensor;
  float harorat;
  bool tugma;
} Xabar;

Xabar xabar;
const int SENSOR = 34, TUGMA = 4;

void yuborildi(const uint8_t *mac, esp_now_send_status_t holat) {
  Serial.println(holat == ESP_NOW_SEND_SUCCESS ? "yuborildi" : "XATO");
}

void setup() {
  Serial.begin(115200);
  pinMode(TUGMA, INPUT_PULLUP);
  WiFi.mode(WIFI_STA);

  Serial.print("Mening MAC manzilim: "); Serial.println(WiFi.macAddress());

  if (esp_now_init() != ESP_OK) { Serial.println("ESP-NOW ishga tushmadi"); return; }
  esp_now_register_send_cb(yuborildi);

  esp_now_peer_info_t juft = {};
  memcpy(juft.peer_addr, qabulMAC, 6);
  juft.channel = 0;
  juft.encrypt = false;
  if (esp_now_add_peer(&juft) != ESP_OK) { Serial.println("Juftlik qo'shilmadi"); return; }
}

void loop() {
  xabar.sensor  = analogRead(SENSOR);
  xabar.harorat = analogRead(35) * 50.0 / 4095.0;
  xabar.tugma   = (digitalRead(TUGMA) == LOW);

  esp_now_send(qabulMAC, (uint8_t *)&xabar, sizeof(xabar));
  delay(1000);
}

/* QABUL QILUVCHI platada:
void kelgan(const uint8_t *mac, const uint8_t *data, int len) {
  Xabar x;  memcpy(&x, data, sizeof(x));
  Serial.print("sensor="); Serial.print(x.sensor);
  Serial.print(" harorat="); Serial.println(x.harorat);
}
setup() ichida:  esp_now_register_recv_cb(kelgan);
*/""",
    amaliy="Ikki ESP32 ni ESP-NOW bilan bog'lab, birida tugma va sensor, "
           "ikkinchisida LED va ekran qo'yib, WiFi routersiz aloqa o'rnatish va "
           "ishonchli aloqa masofasini koridorda o'lchash"),

"Ikki qurilma o'rtasida aloqa": K(
    "Ikki qurilma — yuboruvchi va qabul qiluvchi",
    "Har bir qurilmaning MAC manzili — uning noyob raqami. Uni bilmasdan "
    "ESP-NOW ishlamaydi.",
    """// ESP-NOW QABUL QILUVCHI plata
#include <esp_now.h>
#include <WiFi.h>

typedef struct {
  int sensor;
  float harorat;
  bool tugma;
} Xabar;

Xabar kelganXabar;
const int LED = 2, ZUMMER = 5;
unsigned long oxirgiXabar = 0;

void kelgan(const esp_now_recv_info *info, const uint8_t *data, int len) {
  memcpy(&kelganXabar, data, sizeof(kelganXabar));
  oxirgiXabar = millis();

  Serial.print("sensor=");    Serial.print(kelganXabar.sensor);
  Serial.print("  harorat="); Serial.print(kelganXabar.harorat, 1);
  Serial.print("  tugma=");   Serial.println(kelganXabar.tugma ? "BOSILGAN" : "bo'sh");

  digitalWrite(LED, kelganXabar.tugma);
  if (kelganXabar.harorat > 30) tone(ZUMMER, 2000, 200);
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  WiFi.mode(WIFI_STA);

  // BU MANZILNI yuboruvchi plataga yozing:
  Serial.print("Mening MAC manzilim: "); Serial.println(WiFi.macAddress());

  if (esp_now_init() != ESP_OK) { Serial.println("Xato"); return; }
  esp_now_register_recv_cb(kelgan);
  Serial.println("Xabar kutilmoqda...");
}

void loop() {
  // 5 sekund xabar kelmasa — aloqa uzilgan
  if (millis() - oxirgiXabar > 5000) {
    Serial.println("ALOQA YO'Q");
    digitalWrite(LED, (millis() / 200) % 2);
    delay(500);
  }
}""",
    amaliy="Ikki ESP32 dan biriga yuboruvchi, ikkinchisiga qabul qiluvchi "
           "dasturni yuklab, MAC manzillarni almashtirish; aloqa uzilganda "
           "qabul qiluvchi buni sezishini sinash"),

"Bir nechta qurilmali tarmoq (mesh g'oyasi)": K(
    "Bir yuboruvchi — bir necha qabul qiluvchi",
    "ESP-NOW da bitta qurilma bir necha juftlikka birdan xabar yubora oladi "
    "(broadcast).",
    """// Broadcast: bitta xabar — hamma qurilmaga
#include <esp_now.h>
#include <WiFi.h>

// FF:FF:FF:FF:FF:FF — "hammaga" degani
uint8_t HAMMAGA[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};

typedef struct { int id; int qiymat; char buyruq[16]; } Xabar;
Xabar x;

const int MENING_ID = 1;      // har bir platada boshqacha son
const int SENSOR = 34, LED = 2;

void kelgan(const esp_now_recv_info *info, const uint8_t *data, int len) {
  Xabar k; memcpy(&k, data, sizeof(k));
  if (k.id == MENING_ID) return;          // o'z xabarimizni e'tiborsiz qoldiramiz

  Serial.print("Qurilma "); Serial.print(k.id);
  Serial.print(" dan: qiymat="); Serial.print(k.qiymat);
  Serial.print(" buyruq=");      Serial.println(k.buyruq);

  if (String(k.buyruq) == "yoq") digitalWrite(LED, HIGH);
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  WiFi.mode(WIFI_STA);
  esp_now_init();
  esp_now_register_recv_cb(kelgan);

  esp_now_peer_info_t juft = {};
  memcpy(juft.peer_addr, HAMMAGA, 6);
  juft.channel = 0; juft.encrypt = false;
  esp_now_add_peer(&juft);

  Serial.print("Qurilma ID: "); Serial.println(MENING_ID);
}

void loop() {
  x.id = MENING_ID;
  x.qiymat = analogRead(SENSOR);
  strcpy(x.buyruq, x.qiymat > 2000 ? "yoq" : "ochir");

  esp_now_send(HAMMAGA, (uint8_t *)&x, sizeof(x));   // HAMMAGA yuboramiz
  delay(2000);
}""",
    amaliy="Sinfdagi uch-to'rt ESP32 ga bir xil dasturni (faqat ID ni "
           "o'zgartirib) yuklab, hammasi bir-birining xabarini olishini "
           "ko'rsatish va tarmoq sxemasini doskaga chizish"),

"Telegram bot bilan tanishuv": K(
    "Botni yaratish va birinchi xabar yuborish",
    "BotFather'dan token olinadi, chat ID esa @userinfobot dan.",
    """// Telegram: qurilmadan xabar yuborish
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";

// @BotFather dan olingan token
#define BOT_TOKEN "0000000000:AAAA-BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
// @userinfobot dan olingan chat ID
#define CHAT_ID   "000000000"

WiFiClientSecure xavfsiz;
UniversalTelegramBot bot(BOT_TOKEN, xavfsiz);
const int TUGMA = 4, SENSOR = 34;

void setup() {
  Serial.begin(115200);
  pinMode(TUGMA, INPUT_PULLUP);

  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  xavfsiz.setInsecure();          // sertifikat tekshiruvini o'tkazib yuboradi

  bot.sendMessage(CHAT_ID, "Qurilma ishga tushdi!", "");
  Serial.println("Birinchi xabar yuborildi.");
}

void loop() {
  // tugma bosilganda xabar yuboramiz
  if (digitalRead(TUGMA) == LOW) {
    String matn = "Tugma bosildi!\\nSensor qiymati: " + String(analogRead(SENSOR));
    bot.sendMessage(CHAT_ID, matn, "");
    Serial.println("Xabar yuborildi");
    delay(2000);
  }
}""",
    amaliy="BotFather orqali bot yaratib token olish, ESP32 ga tugma ulab, tugma "
           "bosilganda telefonga Telegram xabari kelishiga erishish"),

"Telegram bot yaratish": K(
    "Bot buyruqlarini qabul qilish",
    "Bot nafaqat yuboradi, telefondan kelgan buyruqni ham o'qiydi.",
    """// Telegram: buyruq qabul qilish
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
#define BOT_TOKEN "SIZNING_TOKEN"

WiFiClientSecure xavfsiz;
UniversalTelegramBot bot(BOT_TOKEN, xavfsiz);

const int LED = 2, SENSOR = 34;
unsigned long oxirgi = 0;
const int ORALIQ = 1500;      // 1,5 sekundda bir marta yangi xabar so'raymiz

void xabarlarniOqi(int soni) {
  for (int i = 0; i < soni; i++) {
    String chat  = bot.messages[i].chat_id;
    String matn  = bot.messages[i].text;
    String kimdan = bot.messages[i].from_name;

    Serial.print(kimdan); Serial.print(": "); Serial.println(matn);

    if (matn == "/start") {
      bot.sendMessage(chat, "Buyruqlar:\\n/yoq\\n/ochir\\n/holat", "");
    }
    if (matn == "/yoq") {
      digitalWrite(LED, HIGH);
      bot.sendMessage(chat, "Chiroq yoqildi", "");
    }
    if (matn == "/ochir") {
      digitalWrite(LED, LOW);
      bot.sendMessage(chat, "Chiroq o'chirildi", "");
    }
    if (matn == "/holat") {
      String h = "Sensor: " + String(analogRead(SENSOR))
               + "\\nChiroq: " + (digitalRead(LED) ? "yoniq" : "o'chiq")
               + "\\nIsh vaqti: " + String(millis() / 1000) + " s";
      bot.sendMessage(chat, h, "");
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  xavfsiz.setInsecure();
}

void loop() {
  if (millis() - oxirgi < ORALIQ) return;
  oxirgi = millis();

  int soni = bot.getUpdates(bot.last_message_received + 1);
  while (soni) {
    xabarlarniOqi(soni);
    soni = bot.getUpdates(bot.last_message_received + 1);
  }
}""",
    amaliy="Telegram botga /yoq, /ochir va /holat buyruqlarini qo'shib, "
           "telefondan yozib qurilmani boshqarish va sensor qiymatini so'rash"),

"Telegram orqali qurilmani boshqarish": K(
    "Tugmali klaviatura bilan boshqaruv",
    "Matn yozish o'rniga tayyor tugmalar — foydalanish ancha qulay.",
    """// Telegram: tugmali klaviatura bilan boshqaruv
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
#define BOT_TOKEN "SIZNING_TOKEN"

WiFiClientSecure xavfsiz;
UniversalTelegramBot bot(BOT_TOKEN, xavfsiz);

const int CHIROQ = 2, RELE = 5, SENSOR = 34;
unsigned long oxirgi = 0;

void klaviaturaKorsat(String chat) {
  String tugmalar = "[[\\"/yoq\\",\\"/ochir\\"],[\\"/rele\\",\\"/holat\\"]]";
  bot.sendMessageWithReplyKeyboard(chat, "Qurilma boshqaruvi:", "",
                                   tugmalar, true);
}

void setup() {
  Serial.begin(115200);
  pinMode(CHIROQ, OUTPUT); pinMode(RELE, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  xavfsiz.setInsecure();
}

void loop() {
  if (millis() - oxirgi < 1500) return;
  oxirgi = millis();

  int n = bot.getUpdates(bot.last_message_received + 1);
  for (int i = 0; i < n; i++) {
    String chat = bot.messages[i].chat_id;
    String matn = bot.messages[i].text;

    if (matn == "/start")  klaviaturaKorsat(chat);
    if (matn == "/yoq")   { digitalWrite(CHIROQ, HIGH); bot.sendMessage(chat, "Chiroq YONDI", ""); }
    if (matn == "/ochir") { digitalWrite(CHIROQ, LOW);  bot.sendMessage(chat, "Chiroq o'chdi", ""); }
    if (matn == "/rele")  {
      digitalWrite(RELE, !digitalRead(RELE));
      bot.sendMessage(chat, digitalRead(RELE) ? "Rele YONIQ" : "Rele o'chiq", "");
    }
    if (matn == "/holat") {
      bot.sendMessage(chat, "Sensor: " + String(analogRead(SENSOR)), "");
    }
  }
}""",
    amaliy="ESP32 ga chiroq va rele ulab, Telegram botga tugmali klaviatura "
           "qo'shish va telefondan tugma bosib qurilmani boshqarish"),

"Telegram orqali boshqarish": K(
    "Parol bilan himoyalangan boshqaruv",
    "Bot havolasi topilsa kim bo'lsa ham boshqara oladi — shuning uchun chat ID "
    "tekshiruvi kerak.",
    """// Telegram: FAQAT ruxsat berilgan foydalanuvchi boshqara oladi
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
#define BOT_TOKEN "SIZNING_TOKEN"

// Ruxsat berilgan chat ID lar
const char* RUXSAT[] = {"111111111", "222222222"};
const int RUXSAT_SONI = 2;

WiFiClientSecure xavfsiz;
UniversalTelegramBot bot(BOT_TOKEN, xavfsiz);
const int CHIROQ = 2;
unsigned long oxirgi = 0;

bool ruxsatBormi(String chat) {
  for (int i = 0; i < RUXSAT_SONI; i++) if (chat == RUXSAT[i]) return true;
  return false;
}

void setup() {
  Serial.begin(115200);
  pinMode(CHIROQ, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  xavfsiz.setInsecure();
}

void loop() {
  if (millis() - oxirgi < 1500) return;
  oxirgi = millis();

  int n = bot.getUpdates(bot.last_message_received + 1);
  for (int i = 0; i < n; i++) {
    String chat = bot.messages[i].chat_id;
    String matn = bot.messages[i].text;

    if (!ruxsatBormi(chat)) {
      bot.sendMessage(chat, "Sizda ruxsat yo'q.", "");
      Serial.print("Ruxsatsiz urinish, chat ID: "); Serial.println(chat);
      continue;
    }

    if (matn == "/yoq")   { digitalWrite(CHIROQ, HIGH); bot.sendMessage(chat, "Yoqildi", ""); }
    if (matn == "/ochir") { digitalWrite(CHIROQ, LOW);  bot.sendMessage(chat, "O'chirildi", ""); }
  }
}""",
    amaliy="Botga ruxsat ro'yxatini qo'shib, boshqa o'quvchining telefonidan "
           "boshqarishga urinib ko'rish va ruxsat rad etilishini kuzatish"),

"Telegram orqali xabar yuborish": K(
    "Sensor chegaradan oshganda avtomatik xabar",
    "Muhim: har o'lchovda emas, faqat HOLAT O'ZGARGANDA xabar yuboriladi.",
    """// Avtomatik ogohlantirish — spam bo'lmasligi uchun filtr bilan
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
#define BOT_TOKEN "SIZNING_TOKEN"
#define CHAT_ID   "000000000"

WiFiClientSecure xavfsiz;
UniversalTelegramBot bot(BOT_TOKEN, xavfsiz);
const int SENSOR = 34, ZUMMER = 5;

const int CHEGARA = 3000;
bool xavfHolati = false;                    // hozirgi holat
unsigned long oxirgiXabar = 0;
const unsigned long ENG_KAM = 60000;        // bir daqiqada bir martadan ko'p emas

void setup() {
  Serial.begin(115200);
  pinMode(ZUMMER, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  xavfsiz.setInsecure();
  bot.sendMessage(CHAT_ID, "Kuzatuv tizimi ishga tushdi", "");
}

void loop() {
  int q = analogRead(SENSOR);
  bool yangiHolat = (q > CHEGARA);

  // FAQAT holat o'zgarganda va vaqt o'tgan bo'lsa xabar yuboramiz
  if (yangiHolat != xavfHolati && millis() - oxirgiXabar > ENG_KAM) {
    xavfHolati = yangiHolat;
    oxirgiXabar = millis();

    if (xavfHolati) {
      bot.sendMessage(CHAT_ID, "OGOHLANTIRISH!\\nQiymat chegaradan oshdi: "
                      + String(q), "");
      tone(ZUMMER, 2500, 500);
    } else {
      bot.sendMessage(CHAT_ID, "Holat normallashdi: " + String(q), "");
    }
  }

  Serial.print("q="); Serial.print(q);
  Serial.println(xavfHolati ? "  [XAVF]" : "");
  delay(1000);
}""",
    amaliy="Sensorni ulab, chegaradan oshganda telefonga bitta xabar kelishiga "
           "erishish; filtrsiz variantda sekundiga xabar kelib spam bo'lishini "
           "ko'rsatib, filtr nima uchun kerakligini tushuntirish"),

"Telegram orqali xabar va ogohlantirish": K(
    "Ikki darajali ogohlantirish tizimi",
    "Diqqat va Xavf — ikki daraja, har biri o'z xabarini yuboradi.",
    """// Ikki darajali ogohlantirish
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
#define BOT_TOKEN "SIZNING_TOKEN"
#define CHAT_ID   "000000000"

WiFiClientSecure xavfsiz;
UniversalTelegramBot bot(BOT_TOKEN, xavfsiz);
const int SENSOR = 34, LED_SARIQ = 2, LED_QIZIL = 4, ZUMMER = 5;

const int DIQQAT = 2500, XAVF = 3500;
int daraja = 0;                     // 0 = normal, 1 = diqqat, 2 = xavf

void setup() {
  Serial.begin(115200);
  pinMode(LED_SARIQ, OUTPUT); pinMode(LED_QIZIL, OUTPUT); pinMode(ZUMMER, OUTPUT);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  xavfsiz.setInsecure();
}

void loop() {
  int q = analogRead(SENSOR);

  int yangi = 0;
  if (q > XAVF)        yangi = 2;
  else if (q > DIQQAT) yangi = 1;

  if (yangi != daraja) {
    daraja = yangi;

    digitalWrite(LED_SARIQ, daraja == 1);
    digitalWrite(LED_QIZIL, daraja == 2);

    if (daraja == 2) {
      bot.sendMessage(CHAT_ID, "XAVF! Qiymat: " + String(q) + "\\nDarhol tekshiring.", "");
      tone(ZUMMER, 2800, 1000);
    } else if (daraja == 1) {
      bot.sendMessage(CHAT_ID, "Diqqat: qiymat ko'tarilmoqda (" + String(q) + ")", "");
      tone(ZUMMER, 1500, 200);
    } else {
      bot.sendMessage(CHAT_ID, "Holat normal (" + String(q) + ")", "");
    }
  }
  delay(1500);
}""",
    amaliy="Sensor, ikki LED va zummer ulab, ikki darajali ogohlantirish tizimi "
           "yasash; har bir darajaga o'tishda telefonga mos xabar kelishini "
           "sinash"),

"Deep sleep va quvvat tejash": K(
    "Deep sleep — batareya umrini o'nlab marta uzaytiradi",
    "Oddiy rejimda ESP32 ~80 mA, deep sleep da esa ~10 mikroamper tortadi.",
    """// Deep sleep: o'lchaydi, yuboradi va uxlaydi
#include <WiFi.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";

#define MKS_SONIYADA 1000000ULL
#define UYQU_VAQTI   300              // 5 daqiqa

// RTC xotirasi — deep sleep dan keyin ham SAQLANADI
RTC_DATA_ATTR int uyganishSoni = 0;

void setup() {
  Serial.begin(115200);
  delay(500);

  uyganishSoni++;
  Serial.print("Uyg'onish #"); Serial.println(uyganishSoni);

  // sabab: taymer, tugma yoki birinchi yoqilish
  esp_sleep_wakeup_cause_t sabab = esp_sleep_get_wakeup_cause();
  if (sabab == ESP_SLEEP_WAKEUP_TIMER) Serial.println("Sabab: taymer");
  else if (sabab == ESP_SLEEP_WAKEUP_EXT0) Serial.println("Sabab: tugma");
  else Serial.println("Sabab: birinchi yoqilish");

  // ISHNI TEZ BAJARAMIZ
  int qiymat = analogRead(34);
  Serial.print("O'lchandi: "); Serial.println(qiymat);

  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  int urinish = 0;
  while (WiFi.status() != WL_CONNECTED && urinish++ < 20) delay(300);
  if (WiFi.status() == WL_CONNECTED) Serial.println("Yuborildi");
  WiFi.disconnect(true);
  WiFi.mode(WIFI_OFF);

  // UXLASHGA KETAMIZ
  Serial.print("Uyquga ketmoqda, "); Serial.print(UYQU_VAQTI); Serial.println(" sekund");
  Serial.flush();

  esp_sleep_enable_timer_wakeup(UYQU_VAQTI * MKS_SONIYADA);
  esp_sleep_enable_ext0_wakeup(GPIO_NUM_33, 0);   // tugma bilan ham uyg'onadi
  esp_deep_sleep_start();
  // BU YERDAN KEYINGI KOD HECH QACHON BAJARILMAYDI
}

void loop() { }      // deep sleep bilan loop ishlatilmaydi""",
    amaliy="ESP32 ni deep sleep rejimida ishlatib, INA219 bilan uyqu va ish "
           "rejimidagi tokni o'lchash; 2000 mAh batareya bilan qurilma necha "
           "kun ishlashini hisoblash"),

"Deep sleep va batareya hisobi": K(
    "Batareya umrini hisoblash",
    "O'rtacha tok = (ish toki x ish vaqti + uyqu toki x uyqu vaqti) / umumiy vaqt.",
    """// Batareya umrini hisoblash va o'lchash
#include <WiFi.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina;
RTC_DATA_ATTR int sikl = 0;
RTC_DATA_ATTR float jamiEnergiya = 0;

#define UYQU 60                          // sekund
#define MKS  1000000ULL

void setup() {
  Serial.begin(115200);
  delay(300);
  sikl++;

  unsigned long boshi = millis();
  ina.begin();

  // --- ish bosqichi: tokni o'lchaymiz ---
  float jamiTok = 0; int n = 0;
  for (int i = 0; i < 20; i++) { jamiTok += ina.getCurrent_mA(); n++; delay(50); }
  float ishToki = jamiTok / n;
  float ishVaqti = (millis() - boshi) / 1000.0;

  const float UYQU_TOKI = 0.01;          // 10 mkA = 0,01 mA

  // o'rtacha tok
  float ortacha = (ishToki * ishVaqti + UYQU_TOKI * UYQU) / (ishVaqti + UYQU);

  const float BATAREYA = 2000.0;         // mAh
  float soat = BATAREYA / ortacha;

  Serial.print("Sikl #");        Serial.println(sikl);
  Serial.print("  ish toki:  "); Serial.print(ishToki, 1);  Serial.println(" mA");
  Serial.print("  ish vaqti: "); Serial.print(ishVaqti, 1); Serial.println(" s");
  Serial.print("  o'rtacha:  "); Serial.print(ortacha, 3);  Serial.println(" mA");
  Serial.print("  BATAREYA: "); Serial.print(soat / 24, 1); Serial.println(" kun yetadi");

  Serial.println("  -> uyquga");
  Serial.flush();
  esp_sleep_enable_timer_wakeup(UYQU * MKS);
  esp_deep_sleep_start();
}

void loop() { }""",
    amaliy="INA219 bilan ESP32 ning ish va uyqu rejimidagi tokini o'lchab, "
           "o'rtacha tokni hisoblash va uyqu vaqtini o'zgartirib batareya "
           "umri qanday o'zgarishini jadvalga yozish"),

"Quvvat tejash: deep sleep rejimi": K(
    "Uch rejim: aktiv, light sleep, deep sleep",
    "Har bir rejimda tok va uyg'onish tezligi boshqacha.",
    """// Uch quvvat rejimini SOLISHTIRISH
#include <WiFi.h>
#define MKS 1000000ULL
RTC_DATA_ATTR int bosqich = 0;

void setup() {
  Serial.begin(115200);
  delay(500);

  Serial.println("\\n=== QUVVAT REJIMLARI ===");
  Serial.println("Aktiv (WiFi yoniq): ~150-250 mA");
  Serial.println("Aktiv (WiFi o'chiq): ~40-50 mA");
  Serial.println("Light sleep:         ~0.8 mA  (RAM saqlanadi, tez uyg'onadi)");
  Serial.println("Deep sleep:          ~0.01 mA (RAM o'chadi, setup dan boshlanadi)");

  bosqich++;

  if (bosqich == 1) {
    Serial.println("\\n1) WiFi yoqilgan holat — 10 sekund, tokni o'lchang");
    WiFi.begin("MaktabWiFi", "parol12345");
    delay(10000);
    WiFi.disconnect(true); WiFi.mode(WIFI_OFF);
  }

  if (bosqich == 2) {
    Serial.println("\\n2) LIGHT SLEEP — 10 sekund");
    Serial.flush();
    esp_sleep_enable_timer_wakeup(10 * MKS);
    esp_light_sleep_start();          // shu yerdan DAVOM etadi
    Serial.println("   light sleep dan uyg'ondik (kod shu yerdan davom etdi)");
  }

  Serial.println("\\n3) DEEP SLEEP — 10 sekund");
  Serial.flush();
  esp_sleep_enable_timer_wakeup(10 * MKS);
  esp_deep_sleep_start();             // setup DAN BOSHLANADI
}

void loop() { }""",
    amaliy="INA219 yoki multimetr bilan ESP32 ning uch rejimidagi tokini "
           "o'lchab jadval to'ldirish va light sleep hamda deep sleep dan "
           "uyg'onishda kod qayerdan davom etishini kuzatish"),

"Batareyada mustaqil ishlaydigan qurilma": K(
    "To'liq avtonom o'lchov stansiyasi",
    "Batareya kuchlanishini ham o'lchab, past bo'lganda ogohlantirish kerak.",
    """// Avtonom stansiya: o'lchaydi, yuboradi, batareyani kuzatadi, uxlaydi
#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const char* API_KALIT = "SIZNING_KEY";

#define MKS 1000000ULL
#define UYQU 600                        // 10 daqiqa

const int SENSOR = 34;
const int BATAREYA_PIN = 35;            // 2 rezistorli bo'luvchi orqali

RTC_DATA_ATTR int sikl = 0;

float batareyaVolt() {
  // bo'luvchi 1:2 -> o'lchangan kuchlanishni 2 ga ko'paytiramiz
  int xom = analogRead(BATAREYA_PIN);
  return xom * 3.3 / 4095.0 * 2.0;
}

void setup() {
  Serial.begin(115200);
  delay(300);
  sikl++;

  int qiymat = analogRead(SENSOR);
  float bat = batareyaVolt();

  Serial.print("Sikl #"); Serial.print(sikl);
  Serial.print("  sensor="); Serial.print(qiymat);
  Serial.print("  batareya="); Serial.print(bat, 2); Serial.println(" V");

  // batareya juda past bo'lsa — uzoqroq uxlaymiz
  unsigned long uyqu = (bat < 3.4) ? UYQU * 4 : UYQU;
  if (bat < 3.2) {
    Serial.println("BATAREYA JUDA PAST — faqat uxlaymiz");
    esp_sleep_enable_timer_wakeup(3600ULL * MKS);
    esp_deep_sleep_start();
  }

  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  int u = 0;
  while (WiFi.status() != WL_CONNECTED && u++ < 25) delay(300);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = "http://api.thingspeak.com/update?api_key=" + String(API_KALIT)
               + "&field1=" + String(qiymat)
               + "&field2=" + String(bat, 2)
               + "&field3=" + String(sikl);
    http.begin(url); http.GET(); http.end();
    Serial.println("Yuborildi");
  }
  WiFi.disconnect(true); WiFi.mode(WIFI_OFF);

  Serial.flush();
  esp_sleep_enable_timer_wakeup(uyqu * MKS);
  esp_deep_sleep_start();
}

void loop() { }""",
    amaliy="ESP32 ni batareyaga ulab, kuchlanish bo'luvchi orqali batareya "
           "zaryadini o'lchash, ma'lumotni bulutga yuborib deep sleep ga "
           "o'tkazish va bir sutkada batareya qancha kamayganini o'lchash"),

"Quvvat manbai va stabilizator": K(
    "Kuchlanishni o'lchash va himoya",
    "5 V dan 3,3 V ga tushirish uchun stabilizator kerak. Rezistorli bo'luvchi "
    "faqat O'LCHOV uchun, quvvat berish uchun emas.",
    """// Kuchlanish bo'luvchi bilan batareyani kuzatish
const int BAT_PIN = 35;

// Bo'luvchi: R1 = 100 kOm (batareyadan), R2 = 100 kOm (GND ga)
// O'lchangan kuchlanish = haqiqiy / 2
const float KOEF = 2.0;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
  analogSetAttenuation(ADC_11db);
  Serial.println("xom | pin_U | batareya_U | zaryad");
}

void loop() {
  long y = 0;
  for (int i = 0; i < 32; i++) { y += analogRead(BAT_PIN); delay(2); }
  int xom = y / 32;

  float pinU = xom * 3.3 / 4095.0;
  float batU = pinU * KOEF;

  // Li-ion: 4.2 V = to'la, 3.0 V = bo'sh
  int zaryad = constrain(map((int)(batU * 100), 300, 420, 0, 100), 0, 100);

  Serial.print(xom);       Serial.print(" | ");
  Serial.print(pinU, 3);   Serial.print(" V | ");
  Serial.print(batU, 2);   Serial.print(" V | ");
  Serial.print(zaryad);    Serial.println(" %");

  delay(2000);
}

// DIQQAT: bo'luvchisiz batareyani (4.2 V) to'g'ridan-to'g'ri
// ADC piniga ulash pinni SHIKASTLAYDI — pin maksimum 3.3 V.""",
    amaliy="Ikki 100 kOm rezistordan bo'luvchi yasab, batareya kuchlanishini "
           "ESP32 bilan o'lchash va multimetr ko'rsatkichi bilan solishtirib, "
           "koeffitsientni aniqlashtirish"),

# ==================================================== ESP32 — TIZIM VA NOSOZLIK
"Nosozlikka chidamlilik (qayta ulanish)": K(
    "Aloqa uzilsa o'zi tiklanadigan tizim",
    "Ishonchli IoT qurilma — bu hech qachon qotib qolmaydigan qurilma. "
    "Watchdog va qayta ulanish shart.",
    """// Nosozlikka chidamli: qayta ulanish + watchdog
#include <WiFi.h>
#include <esp_task_wdt.h>

const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
const int LED_OK = 2, LED_XATO = 4;

unsigned long oxirgiUlanish = 0;
int uzilishSoni = 0;

bool wifiTekshir() {
  if (WiFi.status() == WL_CONNECTED) return true;

  uzilishSoni++;
  Serial.print("Aloqa uzildi (#"); Serial.print(uzilishSoni); Serial.println("), tiklanmoqda...");
  digitalWrite(LED_OK, LOW);
  digitalWrite(LED_XATO, HIGH);

  WiFi.disconnect();
  WiFi.begin(WIFI_NOM, WIFI_PAROL);

  int u = 0;
  while (WiFi.status() != WL_CONNECTED && u++ < 20) {
    delay(500);
    esp_task_wdt_reset();          // watchdog ni "boqamiz"
  }

  bool ok = (WiFi.status() == WL_CONNECTED);
  digitalWrite(LED_OK, ok);
  digitalWrite(LED_XATO, !ok);

  // 10 marta tiklanmasa — platani qayta yuklaymiz
  if (!ok && uzilishSoni > 10) {
    Serial.println("Tiklanmadi — qayta yuklanmoqda");
    ESP.restart();
  }
  return ok;
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_OK, OUTPUT); pinMode(LED_XATO, OUTPUT);

  esp_task_wdt_config_t cfg = { .timeout_ms = 15000, .trigger_panic = true };
  esp_task_wdt_init(&cfg);
  esp_task_wdt_add(NULL);

  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) { delay(500); esp_task_wdt_reset(); }
  digitalWrite(LED_OK, HIGH);
}

void loop() {
  esp_task_wdt_reset();            // dastur tirikligini bildiramiz

  if (wifiTekshir()) {
    Serial.print("ishlayapti | uzilishlar: "); Serial.print(uzilishSoni);
    Serial.print(" | ish vaqti: "); Serial.print(millis() / 1000); Serial.println(" s");
  }
  delay(3000);
}""",
    amaliy="ESP32 ni WiFi ga ulab, routerni ataylab o'chirib-yoqib, qurilma "
           "o'zi qayta ulanishini kuzatish; uzilishlar sonini hisoblash va LED "
           "bilan holatni ko'rsatish"),

"Loglash va diagnostika": K(
    "Darajali log tizimi",
    "Yaxshi log — muammoni telefon orqali ham tushuntirib bera oladigan log.",
    """// Darajali log: XATO, OGOH, MA'LUMOT, TAFSILOT
#include <WiFi.h>

enum Daraja { XATO = 0, OGOH = 1, MALUMOT = 2, TAFSILOT = 3 };
Daraja HOZIRGI = MALUMOT;         // shundan pastdagilar chiqadi

void log_(Daraja d, String matn) {
  if (d > HOZIRGI) return;

  const char* nom[] = {"XATO   ", "OGOH   ", "MA'LUMOT", "TAFSILOT"};

  Serial.print("[");
  Serial.print(millis() / 1000);
  Serial.print("s][");
  Serial.print(nom[d]);
  Serial.print("] ");
  Serial.println(matn);
}

const int SENSOR = 34, LED = 2;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  delay(500);

  log_(MALUMOT, "Qurilma ishga tushdi");
  log_(TAFSILOT, "Bo'sh xotira: " + String(ESP.getFreeHeap()));

  int sinov = analogRead(SENSOR);
  if (sinov == 0 || sinov == 4095) {
    log_(XATO, "Sensor ulanmagan bo'lishi mumkin, qiymat: " + String(sinov));
  } else {
    log_(MALUMOT, "Sensor ishlayapti, qiymat: " + String(sinov));
  }
}

void loop() {
  int q = analogRead(SENSOR);

  log_(TAFSILOT, "o'lchov: " + String(q));

  if (q > 3500)      log_(OGOH, "Qiymat yuqori: " + String(q));
  if (ESP.getFreeHeap() < 20000) log_(XATO, "Xotira tugayapti!");

  digitalWrite(LED, q > 2000);
  delay(2000);
}""",
    amaliy="Sensorli qurilmaga darajali log qo'shib, sensor simini ataylab "
           "uzganda XATO darajasidagi xabar chiqishini ko'rsatish va log "
           "darajasini o'zgartirib chiqadigan xabarlar hajmini boshqarish"),

"Nosozlik topish: mantiqiy analiz": K(
    "Nosozlikni bosqichma-bosqich toraytirish",
    "Tartib: quvvat -> aloqa -> sensor -> mantiq. Har bosqich alohida "
    "tekshiriladi.",
    """// Bosqichma-bosqich diagnostika
#include <WiFi.h>
#include <Wire.h>

const int SENSOR = 34, LED = 2;

bool quvvatTekshir() {
  float u = analogRead(35) * 3.3 / 4095.0 * 2.0;
  Serial.print("1) Quvvat: "); Serial.print(u, 2); Serial.println(" V");
  return u > 3.2;
}

bool i2cTekshir() {
  Wire.begin();
  int topildi = 0;
  Serial.println("2) I2C skaner:");
  for (byte a = 1; a < 127; a++) {
    Wire.beginTransmission(a);
    if (Wire.endTransmission() == 0) {
      Serial.print("   qurilma topildi: 0x");
      Serial.println(a, HEX);
      topildi++;
    }
  }
  if (!topildi) Serial.println("   hech narsa topilmadi — SDA/SCL ni tekshiring");
  return topildi > 0;
}

bool sensorTekshir() {
  int q = analogRead(SENSOR);
  Serial.print("3) Sensor: "); Serial.println(q);
  if (q == 0)    { Serial.println("   -> GND ga tutashgan?"); return false; }
  if (q == 4095) { Serial.println("   -> ulanmagan yoki VCC ga tutashgan?"); return false; }
  return true;
}

bool wifiTekshir() {
  Serial.print("4) WiFi: ");
  WiFi.begin("MaktabWiFi", "parol12345");
  int u = 0;
  while (WiFi.status() != WL_CONNECTED && u++ < 20) delay(300);
  bool ok = WiFi.status() == WL_CONNECTED;
  Serial.println(ok ? WiFi.localIP().toString() : "ULANMADI");
  return ok;
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  delay(1000);
  Serial.println("\\n=== BOSQICHMA-BOSQICH DIAGNOSTIKA ===");

  // Bosqich muvaffaqiyatsiz bo'lsa, keyingisini tekshirish MA'NOSIZ
  if (!quvvatTekshir()) { Serial.println("TO'XTASH: quvvat yetarli emas"); return; }
  if (!sensorTekshir()) { Serial.println("TO'XTASH: sensor muammosi"); return; }
  i2cTekshir();
  if (!wifiTekshir())   { Serial.println("TO'XTASH: tarmoq muammosi"); return; }

  Serial.println("=== HAMMA BOSQICH O'TDI ===");
  digitalWrite(LED, HIGH);
}

void loop() { }""",
    amaliy="O'qituvchi tizimga uch xil nosozlik (past quvvat, uzilgan sensor, "
           "noto'g'ri WiFi paroli) qo'yadi; o'quvchilar diagnostika dasturi "
           "yordamida har birini topib tuzatadi"),

"ESP32 xatolarini topish (boot muammolari)": K(
    "Yuklash xatolari va ularning sabablari",
    "ESP32 ning eng ko'p uchraydigan muammosi — yuklanmasligi yoki "
    "qayta-qayta yuklanib turishi (boot loop).",
    """// Qayta yuklanish sababini aniqlash
#include <esp_system.h>

RTC_DATA_ATTR int yuklanishSoni = 0;

void sababniKorsat() {
  esp_reset_reason_t s = esp_reset_reason();
  Serial.print("Qayta yuklanish sababi: ");
  switch (s) {
    case ESP_RST_POWERON:  Serial.println("quvvat berildi (normal)"); break;
    case ESP_RST_SW:       Serial.println("dastur ESP.restart() chaqirdi"); break;
    case ESP_RST_PANIC:    Serial.println("DASTUR XATOSI (panic) — kodni tekshiring!"); break;
    case ESP_RST_INT_WDT:  Serial.println("WATCHDOG — dastur qotib qoldi"); break;
    case ESP_RST_TASK_WDT: Serial.println("VAZIFA WATCHDOG — loop juda uzoq ishladi"); break;
    case ESP_RST_BROWNOUT: Serial.println("QUVVAT CHO'KDI — manba kuchsiz yoki motor tortdi"); break;
    case ESP_RST_DEEPSLEEP:Serial.println("deep sleep dan uyg'ondi (normal)"); break;
    default:               Serial.println("noma'lum"); break;
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  yuklanishSoni++;
  Serial.println("\\n=== YUKLANISH TAHLILI ===");
  Serial.print("Yuklanish soni: "); Serial.println(yuklanishSoni);
  sababniKorsat();

  Serial.print("Bo'sh xotira: "); Serial.println(ESP.getFreeHeap());

  if (yuklanishSoni > 5) {
    Serial.println("OGOHLANTIRISH: qurilma qayta-qayta yuklanmoqda (boot loop).");
    Serial.println("Tekshiring: 1) quvvat manbai kuchi, 2) GPIO0/2/12/15 ulanishi,");
    Serial.println("            3) motor/servo tortayotgan tok, 4) kodda cheksiz sikl.");
  }
}

void loop() {
  Serial.print("ishlayapti: "); Serial.print(millis() / 1000); Serial.println(" s");
  delay(5000);
}""",
    amaliy="ESP32 ga servo ulab, ishga tushganda kuchlanish cho'kib brownout "
           "qayta yuklanishini hosil qilish, keyin kondensator qo'yib "
           "muammoni bartaraf etish"),

"Tarmoq xavfsizligi asoslari": K(
    "Parolni koddan ajratish va HTTPS",
    "Parol kodda ochiq yozilsa, kodni ulashganda parol ham ketadi.",
    """// Xavfsizlik: parolni ajratish, HTTPS, kirish nazorati
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <Preferences.h>

Preferences sozlama;          // parolni flesh xotirada saqlaymiz
WiFiClientSecure xavfsiz;

void setup() {
  Serial.begin(115200);

  // 1) PAROLNI KODDAN AJRATISH
  sozlama.begin("wifi", false);
  String nom   = sozlama.getString("nom", "");
  String parol = sozlama.getString("parol", "");

  if (nom == "") {
    Serial.println("WiFi sozlanmagan. Serial orqali kiriting:");
    Serial.println("Format: NOM,PAROL");
    while (!Serial.available()) delay(100);
    String kirish = Serial.readStringUntil('\\n');
    int v = kirish.indexOf(',');
    nom   = kirish.substring(0, v);       nom.trim();
    parol = kirish.substring(v + 1);      parol.trim();
    sozlama.putString("nom", nom);
    sozlama.putString("parol", parol);
    Serial.println("Saqlandi. Endi parol kodda EMAS, xotirada.");
  }

  WiFi.begin(nom.c_str(), parol.c_str());
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println("\\nUlandi");

  // 2) HTTPS ishlatish (http emas)
  xavfsiz.setInsecure();       // o'quv maqsadida; jiddiy loyihada sertifikat qo'yiladi

  Serial.println("\\nXAVFSIZLIK QOIDALARI:");
  Serial.println(" - Parolni kodga yozmang, xotirada saqlang");
  Serial.println(" - Kodni ulashishdan oldin parol va tokenni olib tashlang");
  Serial.println(" - Ochiq brokerdan foydalansangiz, mavzu nomi noyob bo'lsin");
  Serial.println(" - Boshqaruv sahifasiga parol qo'ying");
  Serial.println(" - Iloji bo'lsa http emas, https ishlating");
}

void loop() { delay(10000); }""",
    amaliy="ESP32 ning WiFi parolini koddan olib tashlab, Preferences xotirasiga "
           "saqlash; kodni boshqa o'quvchiga berib, parol koddan "
           "topilmasligini tekshirish"),

"SPI protokoli haqida tushuncha": K(
    "SPI va I2C ni solishtirish",
    "SPI tez, lekin ko'p sim talab qiladi. I2C sekin, lekin faqat 2 sim.",
    """// SPI va I2C — ikkalasini bir dasturda ishlatib solishtirish
#include <SPI.h>
#include <Wire.h>
#include <SD.h>

const int SD_CS = 5;

void setup() {
  Serial.begin(115200);
  delay(500);

  Serial.println("SPI va I2C SOLISHTIRISH");
  Serial.println("           | SPI          | I2C");
  Serial.println("Simlar     | 4 + har qurilmaga CS | 2 (SDA, SCL)");
  Serial.println("Tezlik     | 10-80 MHz    | 100-400 kHz");
  Serial.println("Manzil     | CS pin bilan | 7 bitli manzil");
  Serial.println("Ishlatish  | SD, ekran, RFID | sensor, RTC, OLED");

  // --- I2C: shinadagi qurilmalarni topamiz ---
  Wire.begin();
  Serial.println("\\nI2C qurilmalari:");
  for (byte a = 1; a < 127; a++) {
    Wire.beginTransmission(a);
    if (Wire.endTransmission() == 0) {
      Serial.print("  0x"); Serial.println(a, HEX);
    }
  }

  // --- SPI: SD kartani ishga tushiramiz ---
  Serial.println("\\nSPI (SD kart):");
  if (SD.begin(SD_CS)) {
    Serial.print("  Kart hajmi: ");
    Serial.print(SD.cardSize() / (1024 * 1024));
    Serial.println(" MB");

    // tezlikni o'lchaymiz
    unsigned long t = millis();
    File f = SD.open("/sinov.txt", FILE_WRITE);
    for (int i = 0; i < 100; i++) f.println("sinov qatori 1234567890");
    f.close();
    Serial.print("  100 qator yozish: "); Serial.print(millis() - t); Serial.println(" ms");
  } else {
    Serial.println("  kart topilmadi");
  }
}

void loop() { }""",
    amaliy="ESP32 ga SD kart (SPI) va OLED ekran (I2C) ni birga ulab, ikkala "
           "protokolni bir vaqtda ishlatish; sim sonini sanab, tezlikni o'lchab "
           "solishtirish jadvalini to'ldirish"),

"Vazifalarni bo'lish (FreeRTOS g'oyasi)": K(
    "Bir vaqtda bir necha ish",
    "FreeRTOS vazifalarni navbat bilan (yoki ikki yadroda) bajaradi — bitta "
    "sekin ish boshqalarini to'xtatmaydi.",
    """// FreeRTOS: uch vazifa bir vaqtda ishlaydi
const int LED1 = 2, LED2 = 4, SENSOR = 34;

// 1-vazifa: tez miltillash
void miltillash(void *p) {
  pinMode(LED1, OUTPUT);
  for (;;) {
    digitalWrite(LED1, HIGH); vTaskDelay(150 / portTICK_PERIOD_MS);
    digitalWrite(LED1, LOW);  vTaskDelay(150 / portTICK_PERIOD_MS);
  }
}

// 2-vazifa: sekin o'lchash
void olchash(void *p) {
  for (;;) {
    Serial.print("sensor = "); Serial.println(analogRead(SENSOR));
    vTaskDelay(2000 / portTICK_PERIOD_MS);
  }
}

// 3-vazifa: uzoq davom etadigan ish
void uzunIsh(void *p) {
  pinMode(LED2, OUTPUT);
  for (;;) {
    digitalWrite(LED2, HIGH);
    vTaskDelay(3000 / portTICK_PERIOD_MS);     // "og'ir" ish
    digitalWrite(LED2, LOW);
    vTaskDelay(1000 / portTICK_PERIOD_MS);
    Serial.println("  uzun ish tugadi");
  }
}

void setup() {
  Serial.begin(115200);

  //                  funksiya    nom     stek  param ustunlik  handle yadro
  xTaskCreatePinnedToCore(miltillash, "led", 2048, NULL, 1, NULL, 0);
  xTaskCreatePinnedToCore(olchash,    "olch", 2048, NULL, 1, NULL, 1);
  xTaskCreatePinnedToCore(uzunIsh,    "uzun", 2048, NULL, 1, NULL, 1);

  Serial.println("Uch vazifa ishga tushdi — LED1 uzun ish davomida ham miltillaydi");
}

void loop() { vTaskDelay(1000 / portTICK_PERIOD_MS); }""",
    amaliy="Ikki LED va sensorni ulab, uchta vazifani bir vaqtda ishlatish; "
           "keyin ayni ishni oddiy loop va delay bilan yozib, uzun ish "
           "miltillashni to'xtatib qo'yishini ko'rsatish"),

"Kodni modullarga bo'lish": K(
    "Loyihani bir necha faylga ajratish",
    "Katta loyihada hamma kodni bitta faylga yozish — xatolarni topishni "
    "qiyinlashtiradi.",
    """// ASOSIY FAYL (loyiha.ino)
#include "sensorlar.h"
#include "tarmoq.h"
#include "korsatish.h"

void setup() {
  Serial.begin(115200);
  sensorlarniIshgaTushir();
  tarmoqqaUlan();
  ekranniIshgaTushir();
}

void loop() {
  Olchov o = olchovOl();          // sensorlar.h dan
  ekrandaKorsat(o);               // korsatish.h dan
  if (o.harorat > 30) yubor(o);   // tarmoq.h dan
  delay(2000);
}

/* ---------- sensorlar.h ----------
#ifndef SENSORLAR_H
#define SENSORLAR_H

struct Olchov { float harorat; int yoruglik; };

void sensorlarniIshgaTushir();
Olchov olchovOl();

#endif
*/

/* ---------- sensorlar.cpp ----------
#include "sensorlar.h"
#include <Arduino.h>

const int LDR = 34, TERM = 35;

void sensorlarniIshgaTushir() {
  analogReadResolution(12);
}

Olchov olchovOl() {
  Olchov o;
  o.yoruglik = analogRead(LDR);
  o.harorat  = analogRead(TERM) * 50.0 / 4095.0;
  return o;
}
*/""",
    amaliy="Ishlayotgan bitta fayldan iborat loyihani uch faylga (sensorlar, "
           "tarmoq, ko'rsatish) ajratib, ayni natijani olish va bitta modulni "
           "buzib, xato qayerdaligini tez topishni sinash"),

"Kutubxona yozish asoslari": K(
    "O'z kutubxonangni yozish",
    "Bir necha loyihada takrorlanadigan kodni kutubxonaga chiqarish kerak.",
    """// O'Z KUTUBXONAMIZ: Chegara.h
/*
#ifndef CHEGARA_H
#define CHEGARA_H
#include <Arduino.h>

class Chegara {
  public:
    Chegara(int pin, int past, int baland);
    void boshla();
    int  oqi();
    bool oshdimi();
    int  foiz();

  private:
    int _pin, _past, _baland;
    bool _holat;
};
#endif
*/

/* ---------- Chegara.cpp ----------
#include "Chegara.h"

Chegara::Chegara(int pin, int past, int baland) {
  _pin = pin; _past = past; _baland = baland; _holat = false;
}

void Chegara::boshla() { pinMode(_pin, INPUT); }

int Chegara::oqi() { return analogRead(_pin); }

bool Chegara::oshdimi() {
  int q = oqi();
  // gisterezis ichkarida — foydalanuvchi bu haqda o'ylamaydi
  if (!_holat && q > _baland) _holat = true;
  if ( _holat && q < _past)   _holat = false;
  return _holat;
}

int Chegara::foiz() { return map(oqi(), 0, 4095, 0, 100); }
*/

// --- ISHLATISH: kod juda soddalashadi ---
#include "Chegara.h"

Chegara yoruglik(34, 1500, 2500);
Chegara harorat(35, 2000, 3000);
const int LED = 2, ZUMMER = 5;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  yoruglik.boshla();
  harorat.boshla();
}

void loop() {
  digitalWrite(LED, yoruglik.oshdimi());
  if (harorat.oshdimi()) tone(ZUMMER, 2000, 200);

  Serial.print("yorug'lik: "); Serial.print(yoruglik.foiz()); Serial.print(" %  ");
  Serial.print("harorat: ");   Serial.print(harorat.foiz());  Serial.println(" %");
  delay(1000);
}""",
    amaliy="Gisterezisli chegara mantiqini o'z kutubxonangizga chiqarib, uni "
           "ikki sensor uchun ishlatish; kutubxonasiz va kutubxona bilan "
           "yozilgan kod uzunligini solishtirish"),

"5V va 3.3V mos kelmasligi muammosi": K(
    "Kuchlanish bo'luvchi bilan darajani moslash",
    "5 V signalni 3,3 V piniga berish pinni shikastlaydi. Ikki rezistor bu "
    "muammoni hal qiladi.",
    """// 5V -> 3.3V: kuchlanish bo'luvchi hisobi va sinovi
// Uout = Uin * R2 / (R1 + R2)
// 5 V -> 3.3 V uchun: R1 = 1 kOm, R2 = 2 kOm
//   Uout = 5 * 2000 / 3000 = 3.33 V  -> to'g'ri

const int ECHO_PIN = 18;     // HC-SR04 ECHO (bo'luvchi orqali)
const int TRIG_PIN = 5;
const int OLCHOV   = 34;     // bo'luvchi chiqishini tekshirish uchun

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  analogReadResolution(12);

  Serial.println("Bo'luvchi hisobi:");
  Serial.println("  R1 = 1 kOm (signaldan), R2 = 2 kOm (GND ga)");
  Serial.println("  Uout = Uin * R2/(R1+R2) = 5 * 2/3 = 3.33 V");
  Serial.println("Chiqishni tekshirish uchun bo'luvchi chiqishini GPIO34 ga ham ulang.");
}

void loop() {
  // bo'luvchi chiqishidagi kuchlanishni tekshiramiz
  float u = analogRead(OLCHOV) * 3.3 / 4095.0;
  Serial.print("Bo'luvchi chiqishi: "); Serial.print(u, 2); Serial.println(" V");
  if (u > 3.4) Serial.println("  XAVF! Rezistor qiymatlarini tekshiring.");

  // HC-SR04 ni o'qiymiz
  digitalWrite(TRIG_PIN, LOW);  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH); delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long t = pulseIn(ECHO_PIN, HIGH, 30000);
  Serial.print("Masofa: "); Serial.print(t * 0.034 / 2); Serial.println(" sm");

  delay(1000);
}""",
    amaliy="1 kOm va 2 kOm rezistorlardan bo'luvchi yasab, HC-SR04 ning ECHO "
           "signalini ESP32 ga xavfsiz ulash; bo'luvchi chiqishini multimetr "
           "bilan o'lchab, 3,3 V dan oshmasligini tasdiqlash"),

"3.3V va 5V mos kelmasligi: nima qilish kerak": K(
    "Uch yechim: bo'luvchi, daraja o'zgartirgich, optopara",
    "Har bir yechimning o'z o'rni bor.",
    """// Uch yechimni solishtirish
const int SINOV = 34;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);

  Serial.println("=== 5V va 3.3V ni MOSLASH USULLARI ===\\n");

  Serial.println("1) KUCHLANISH BO'LUVCHI (2 rezistor)");
  Serial.println("   + arzon, oddiy");
  Serial.println("   - faqat KIRISH uchun (5V -> 3.3V)");
  Serial.println("   - sekin signalda ishlaydi, tez signalda buziladi");
  Serial.println("   R1=1k, R2=2k\\n");

  Serial.println("2) DARAJA O'ZGARTIRGICH (level shifter, TXS0108E)");
  Serial.println("   + IKKI TOMONLAMA ishlaydi");
  Serial.println("   + tez signal (I2C, SPI) uchun mos");
  Serial.println("   - qo'shimcha modul kerak\\n");

  Serial.println("3) OPTOPARA");
  Serial.println("   + zanjirlarni butunlay AJRATADI");
  Serial.println("   + kuchli shovqinli muhitda eng ishonchli");
  Serial.println("   - sekin, har signal uchun alohida element\\n");

  Serial.println("QOIDA: ESP32 dan 5V qurilmaga signal berish odatda ishlaydi");
  Serial.println("(5V qurilma 3.3V ni HIGH deb qabul qiladi), lekin teskarisi");
  Serial.println("XAVFLI — 5V signal 3.3V pinni shikastlaydi.");
}

void loop() {
  float u = analogRead(SINOV) * 3.3 / 4095.0;
  Serial.print("Kirish kuchlanishi: "); Serial.print(u, 2); Serial.println(" V");
  if (u > 3.3) Serial.println("  XAVF: chegaradan oshdi!");
  delay(2000);
}""",
    amaliy="Uch usulni (bo'luvchi, daraja o'zgartirgich, optopara) yig'ib, "
           "har birining chiqish kuchlanishini o'lchash va qaysi holatda "
           "qaysi biri mos kelishini jadvalga yozish"),

"Sensorlarni ESP32'ga ulash": K(
    "Bir necha sensorni birga ulash",
    "I2C sensorlarni bitta shinaga ulash mumkin — manzillari har xil bo'lsa.",
    """// Bir necha sensorni ESP32 ga birga ulash
#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <DHT.h>

Adafruit_BMP280 bmp;                 // I2C, 0x76
DHT dht(4, DHT22);                   // 1 sim, GPIO4
const int LDR = 34, TUPROQ = 35;     // analog

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);                // SDA=21, SCL=22
  analogReadResolution(12);

  dht.begin();
  if (!bmp.begin(0x76)) Serial.println("BMP280 topilmadi (0x77 ni sinang)");

  Serial.println("harorat | namlik | bosim | yorug'lik | tuproq");
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  float p = bmp.readPressure() / 100.0;
  int   y = map(analogRead(LDR), 0, 4095, 0, 100);
  int   tu = map(analogRead(TUPROQ), 4095, 1200, 0, 100);

  if (isnan(t) || isnan(h)) {
    Serial.println("DHT22 javob bermadi — 10 kOm rezistorni tekshiring");
  } else {
    Serial.print(t, 1);  Serial.print(" C | ");
    Serial.print(h, 1);  Serial.print(" % | ");
    Serial.print(p, 1);  Serial.print(" hPa | ");
    Serial.print(y);     Serial.print(" % | ");
    Serial.print(tu);    Serial.println(" %");
  }
  delay(2000);
}""",
    amaliy="ESP32 ga DHT22, BMP280, fotorezistor va tuproq datchigini birga "
           "ulab, to'rt sensordan bir vaqtda ma'lumot olish; I2C skaneri bilan "
           "shinadagi qurilmalarni tekshirish"),

"Sensorlarni kalibrlash va aniqlik": K(
    "Ikki nuqtali kalibrlash",
    "Har bir sensor o'z xatosiga ega. Ikki ma'lum nuqta bo'yicha to'g'rilash — "
    "eng oddiy va samarali usul.",
    """// Ikki nuqtali kalibrlash
const int SENSOR = 34;

// Kalibrlashda o'lchangan qiymatlar (o'z sensoringiz uchun toping)
const int  XOM_PAST   = 820;    // etalon PAST nuqtada o'lchangan xom qiymat
const float HAQ_PAST  = 0.0;    // shu nuqtaning HAQIQIY qiymati
const int  XOM_BALAND = 3210;   // etalon BALAND nuqtada
const float HAQ_BALAND = 100.0;

float kalibrlangan() {
  int xom = analogRead(SENSOR);
  // ikki nuqta orqali chiziq: y = y1 + (x-x1)*(y2-y1)/(x2-x1)
  return HAQ_PAST + (xom - XOM_PAST) * (HAQ_BALAND - HAQ_PAST)
                    / (float)(XOM_BALAND - XOM_PAST);
}

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
  Serial.println("KALIBRLASH TARTIBI:");
  Serial.println(" 1) Sensorni ETALON past nuqtaga qo'ying, xom qiymatni yozing");
  Serial.println(" 2) Etalon baland nuqtaga qo'ying, xom qiymatni yozing");
  Serial.println(" 3) Ikkalasini koddagi doimiylarga kiriting");
  Serial.println(" 4) Uchinchi, O'RTA nuqtada tekshiring\\n");
  Serial.println("xom | kalibrlangan | xato");
}

void loop() {
  int xom = analogRead(SENSOR);
  float k = kalibrlangan();

  Serial.print(xom);    Serial.print("  |  ");
  Serial.print(k, 1);   Serial.print("  |  ");

  // etalon qiymatni qo'lda kiriting va farqni ko'ring
  Serial.println("(etalon bilan solishtiring)");
  delay(1000);
}""",
    amaliy="Termistorni muzli suv (0 °C) va qaynoq suvdan olingan iliq suvda "
           "(termometr bilan o'lchangan) kalibrlash, uchinchi haroratda "
           "tekshirib xatoni hisoblash"),

"Sensor qiymatini sahifada ko'rsatish": K(
    "Bir necha sensor — bitta boshqaruv paneli",
    "Panel — bir qarashda hamma ko'rsatkichni ko'rsatadigan sahifa.",
    """// Boshqaruv paneli: to'rt ko'rsatkich bir sahifada
#include <WiFi.h>
const char* WIFI_NOM = "MaktabWiFi";
const char* WIFI_PAROL = "parol12345";
WiFiServer server(80);
const int LDR = 34, TERM = 35;

String kartochka(String nom, String qiymat, String birlik, int foiz) {
  String s = "<div class='k'>";
  s += "<div class='n'>" + nom + "</div>";
  s += "<div class='q'>" + qiymat + "<span class='b'>" + birlik + "</span></div>";
  s += "<div class='ch'><div class='i' style='width:" + String(foiz) + "%'></div></div>";
  s += "</div>";
  return s;
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_NOM, WIFI_PAROL);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  server.begin();
  Serial.print("http://"); Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient c = server.available();
  if (!c) return;
  c.readStringUntil('\\n');

  int y = map(analogRead(LDR), 0, 4095, 0, 100);
  int t = map(analogRead(TERM), 0, 4095, 0, 50);

  c.println("HTTP/1.1 200 OK");
  c.println("Content-Type: text/html; charset=utf-8\\n");
  c.println("<!DOCTYPE html><html><head><meta charset='utf-8'>");
  c.println("<meta name='viewport' content='width=device-width,initial-scale=1'>");
  c.println("<meta http-equiv='refresh' content='3'><style>");
  c.println("body{font-family:sans-serif;background:#eef2f0;padding:20px;margin:0}");
  c.println(".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;max-width:760px;margin:0 auto}");
  c.println(".k{background:#fff;padding:18px;border-radius:14px;box-shadow:0 2px 10px rgba(0,0,0,.07)}");
  c.println(".n{font-size:13px;color:#777;text-transform:uppercase;letter-spacing:1px}");
  c.println(".q{font-size:38px;font-weight:700;color:#2e7d32;margin:6px 0}");
  c.println(".b{font-size:16px;color:#999;margin-left:4px}");
  c.println(".ch{height:8px;background:#e8e8e8;border-radius:5px;overflow:hidden}");
  c.println(".i{height:100%;background:#2e7d32}");
  c.println("</style></head><body><div class='grid'>");
  c.println(kartochka("Yorug'lik", String(y), "%", y));
  c.println(kartochka("Harorat", String(t), "C", t * 2));
  c.println(kartochka("Ish vaqti", String(millis()/1000), "s", 50));
  c.println(kartochka("Xotira", String(ESP.getFreeHeap()/1024), "KB", 60));
  c.println("</div></body></html>");
  c.stop();
}""",
    amaliy="Ikki sensorni ESP32 ga ulab, to'rt kartochkali boshqaruv panelini "
           "yasash va telefondan ochib, sensorlarga ta'sir qilib qiymatlar "
           "o'zgarishini kuzatish"),

"Ogohlantirish tizimi (alert)": K(
    "Chegara, gisterezis va kechikish birga",
    "Yaxshi ogohlantirish tizimi yolg'on signal bermaydi.",
    """// Ishonchli ogohlantirish: gisterezis + tasdiqlash + minimal oraliq
const int SENSOR = 34, LED = 2, ZUMMER = 5;

const int YOQ_CHEGARA   = 3000;    // shundan yuqori — xavf
const int OCHIR_CHEGARA = 2500;    // shundan past  — normal (gisterezis)
const int TASDIQ_SONI   = 3;       // ketma-ket shuncha marta tasdiqlansin
const unsigned long ENG_KAM_ORALIQ = 30000;

bool xavf = false;
int  ketmaKet = 0;
unsigned long oxirgiSignal = 0;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT); pinMode(ZUMMER, OUTPUT);
  analogReadResolution(12);
}

void loop() {
  int q = analogRead(SENSOR);

  // 1) TASDIQLASH: bitta sakragan qiymat signal bermaydi
  if (!xavf && q > YOQ_CHEGARA)        ketmaKet++;
  else if (xavf && q < OCHIR_CHEGARA)  ketmaKet++;
  else                                 ketmaKet = 0;

  // 2) GISTEREZIS: ikki chegara chegara atrofidagi "titrashni" yo'qotadi
  if (ketmaKet >= TASDIQ_SONI) {
    ketmaKet = 0;
    xavf = !xavf;

    // 3) MINIMAL ORALIQ: signal juda tez-tez takrorlanmasin
    if (millis() - oxirgiSignal > ENG_KAM_ORALIQ) {
      oxirgiSignal = millis();
      if (xavf) { tone(ZUMMER, 2500, 800); Serial.println("*** OGOHLANTIRISH ***"); }
      else      { Serial.println("holat normallashdi"); }
    }
  }

  digitalWrite(LED, xavf);
  Serial.print("q="); Serial.print(q);
  Serial.print(" tasdiq="); Serial.print(ketmaKet);
  Serial.println(xavf ? "  [XAVF]" : "");
  delay(300);
}""",
    amaliy="Sensor, LED va zummer yig'ib, avval oddiy chegarali signal yozish va "
           "chegarada titrashini ko'rish, keyin gisterezis va tasdiqlash "
           "qo'shib, yolg'on signallar yo'qolishini o'lchash"),

}

# 2-qism alohida faylda (bu fayl juda kattalashmasligi uchun).
from kb_kod2 import KODLAR2 as _K2

for _k, _v in _K2.items():
    if _k in KODLAR:
        raise ValueError("kb_kod: kalit ikki faylda takrorlangan: " + _k)
    KODLAR[_k] = _v


if __name__ == "__main__":
    print("kod namunasi:", len(KODLAR))
    print("amaliy ishi qayta yozilgan:", sum(1 for v in KODLAR.values() if v["amaliy"]))
    print("kod qatorlari:", sum(v["kod"].count(chr(10)) + 1 for v in KODLAR.values()))
