# -*- coding: utf-8 -*-
"""
Komponentlarning ULANISH SXEMASI va KUTUBXONALARI ma'lumotnomasi.

Har bir komponent uchun:
    kutubxona  — Arduino IDE'da o'rnatiladigan kutubxona nomi (yoki None)
    include    — koddagi #include qatori
    uno        — Arduino Uno bilan ulanish: [(komponent pini, plata pini, izoh)]
    esp32      — ESP32 bilan ulanish (agar farq qilsa)
    diqqat     — xatoga olib keladigan joylar

Dars rejasida bu ma'lumot 08-bo'lim sifatida chiqadi
(CLAUDE.md qoidasi: qo'shimcha bo'limlar faqat 07 dan KEYIN qo'shiladi).
"""

from pasport import olish as pasport_olish


# ------------------------------------------------------------------ yordamchi
def C(kutubxona, include, uno, esp32=None, diqqat=None, kalitlar=()):
    return {"kutubxona": kutubxona, "include": include, "uno": uno,
            "esp32": esp32, "diqqat": diqqat, "kalitlar": list(kalitlar)}


ULANISH = {

# ============================================================ ASOSIY CHIQISH
"LED": C(
    None, None,
    [("Uzun oyoq (anod, +)", "D9 (yoki istalgan raqamli pin)", "220 Om rezistor orqali"),
     ("Kalta oyoq (katod, -)", "GND", "to'g'ridan-to'g'ri")],
    diqqat="Rezistorsiz ulash LEDni ham, plata pinini ham kuydiradi. "
           "220 Om — 5V uchun standart qiymat.",
    kalitlar=["led", "svetofor", "miltill", "yorug'lik chiqar"]),

"RGB LED (umumiy katod)": C(
    None, None,
    [("R oyoq", "D9 (PWM)", "220 Om rezistor orqali"),
     ("G oyoq", "D10 (PWM)", "220 Om rezistor orqali"),
     ("B oyoq", "D11 (PWM)", "220 Om rezistor orqali"),
     ("Eng uzun oyoq (umumiy katod)", "GND", "")],
    diqqat="Uchta pin ham PWM (~ belgisi bor) bo'lishi kerak, aks holda rang "
           "aralashtirilmaydi. Umumiy ANOD turida GND o'rniga 5V ga ulanadi.",
    kalitlar=["rgb", "rang aralash"]),

"Passiv zummer": C(
    None, None,
    [("+ (uzun oyoq)", "D8", "to'g'ridan-to'g'ri yoki 100 Om orqali"),
     ("- (kalta oyoq)", "GND", "")],
    diqqat="Passiv zummer o'zi tovush chiqarmaydi — tone() funksiyasi bilan "
           "chastota berish kerak. Aktiv zummerga esa faqat kuchlanish berilsa yetadi.",
    kalitlar=["zummer", "buzzer", "melodiya", "nota", "tovush chiqar"]),

"7-segment indikator (1 razryad)": C(
    None, None,
    [("a, b, c, d, e, f, g segmentlari", "D2...D8", "har biri 220 Om rezistor orqali"),
     ("Umumiy katod (COM)", "GND", "umumiy anod turida 5V ga")],
    diqqat="7 ta rezistor kerak — har segmentga bittadan. Umumiy katod va umumiy "
           "anod turlari teskari ishlaydi, avval multimetr bilan aniqlang.",
    kalitlar=["7-segment", "segment", "raqam ko'rsat"]),

"74HC595 siljish registri": C(
    None, None,
    [("DS / SER (14-pin)", "D11", "ma'lumot (data)"),
     ("SH_CP / SRCLK (11-pin)", "D12", "siljish taktı (clock)"),
     ("ST_CP / RCLK (12-pin)", "D8", "yozish (latch)"),
     ("VCC (16-pin)", "5V", ""),
     ("GND (8-pin)", "GND", ""),
     ("OE (13-pin)", "GND", "chiqishni yoqib turadi"),
     ("MR (10-pin)", "5V", "tozalashni o'chirib turadi")],
    diqqat="OE va MR pinlarini ulashni unutish eng ko'p uchraydigan xato — "
           "ularsiz chiqish umuman ishlamaydi.",
    kalitlar=["74hc595", "siljish registri", "shift regist"]),

"LED matritsa 8x8 (MAX7219)": C(
    "LedControl", "#include <LedControl.h>",
    [("DIN", "D12", "ma'lumot"),
     ("CLK", "D11", "takt"),
     ("CS / LOAD", "D10", "tanlash"),
     ("VCC", "5V", ""),
     ("GND", "GND", "")],
    diqqat="Yorqinlik setIntensity(0..15) bilan sozlanadi — maksimalda modul "
           "ko'p tok tortadi.",
    kalitlar=["led matritsa", "max7219", "8x8"]),

"WS2812 adreslanadigan LED lenta": C(
    "Adafruit NeoPixel", "#include <Adafruit_NeoPixel.h>",
    [("DIN (ma'lumot)", "D6", "330-470 Om rezistor orqali"),
     ("VCC / 5V", "5V", "8 LEDdan ko'p bo'lsa alohida quvvat manbai"),
     ("GND", "GND", "quvvat manbai GND si bilan BIRLASHTIRILADI")],
    diqqat="Har bir LED to'liq yorqinlikda ~60 mA tortadi. 8 LED = 0.5 A — "
           "Arduino'ning USB quvvati chegarasida. Ko'proq LED uchun tashqi 5V manba shart.",
    kalitlar=["ws2812", "neopixel", "lenta"]),

"LCD 1602 (I2C moduli bilan)": C(
    "LiquidCrystal I2C", "#include <LiquidCrystal_I2C.h>",
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("SDA", "A4", "Uno'da SDA = A4"),
     ("SCL", "A5", "Uno'da SCL = A5")],
    esp32=[("VCC", "3.3V yoki 5V", "modul ikkisida ham ishlaydi"),
           ("GND", "GND", ""),
           ("SDA", "GPIO21", ""),
           ("SCL", "GPIO22", "")],
    diqqat="I2C manzili odatda 0x27 yoki 0x3F. Ekran yonib turib matn "
           "ko'rinmasa — manzil noto'g'ri yoki kontrast vintini burash kerak.",
    kalitlar=["lcd", "1602", "i2c"]),

"OLED ekran 0.96\" (SSD1306, I2C)": C(
    "Adafruit SSD1306 + Adafruit GFX",
    "#include <Adafruit_SSD1306.h>\n#include <Adafruit_GFX.h>",
    [("VCC", "5V (ba'zi modullarda 3.3V)", ""),
     ("GND", "GND", ""),
     ("SDA", "A4", ""),
     ("SCL", "A5", "")],
    esp32=[("VCC", "3.3V", ""),
           ("GND", "GND", ""),
           ("SDA", "GPIO21", ""),
           ("SCL", "GPIO22", "")],
    diqqat="I2C manzili 0x3C (ba'zan 0x3D). display.display() chaqirilmasa "
           "ekranda hech narsa ko'rinmaydi — bu eng ko'p uchraydigan xato.",
    kalitlar=["oled", "ssd1306"]),

# ============================================================ KIRISH
"Tugma (push button)": C(
    None, None,
    [("Bir oyoq", "D2", "10 kOm tortuvchi rezistor bilan 5V ga, yoki INPUT_PULLUP"),
     ("Ikkinchi oyoq", "GND", "")],
    diqqat="Rezistorsiz ulansa pin \"suzib\" qoladi va tasodifiy qiymat o'qiladi. "
           "Eng oson yo'l: pinMode(2, INPUT_PULLUP) — ichki rezistor ishlatiladi, "
           "bu holda bosilganda LOW o'qiladi.",
    kalitlar=["tugma", "button", "debounce", "digitalread"]),

"Potensiometr 10 kOm": C(
    None, None,
    [("Chap chetdagi oyoq", "GND", ""),
     ("O'rtadagi oyoq (chiqish)", "A0", "analog pin"),
     ("O'ng chetdagi oyoq", "5V", "")],
    esp32=[("Chap oyoq", "GND", ""),
           ("O'rta oyoq", "GPIO34", "faqat kirish uchun ishlatiladigan ADC pin"),
           ("O'ng oyoq", "3.3V", "5V BERILMAYDI")],
    diqqat="O'rta oyoq albatta analog pinga ulanadi. Chetdagi ikki oyoq "
           "o'rin almashsa, faqat burash yo'nalishi teskari bo'ladi — zarari yo'q.",
    kalitlar=["potensiometr", "o'zgaruvchan rezistor", "analogread"]),

"Fotorezistor (LDR)": C(
    None, None,
    [("Bir oyoq", "5V", ""),
     ("Ikkinchi oyoq", "A0", "shu nuqtadan 10 kOm rezistor GND ga — kuchlanish bo'luvchi")],
    diqqat="LDR yolg'iz ishlamaydi — u 10 kOm rezistor bilan kuchlanish bo'luvchi "
           "hosil qilishi kerak, aks holda A0 da o'zgarish bo'lmaydi.",
    kalitlar=["fotorezistor", "ldr", "yorug'lik sez", "tungi chiroq"]),

"NTC termistor": C(
    None, None,
    [("Bir oyoq", "5V", ""),
     ("Ikkinchi oyoq", "A0", "shu nuqtadan 10 kOm rezistor GND ga")],
    diqqat="Fotorezistor bilan bir xil sxema. Haroratni gradusga aylantirish "
           "uchun Shteynhart-Xart formulasi yoki jadval kerak.",
    kalitlar=["termistor", "ntc", "harorat sens"]),

"DHT22 (harorat va namlik)": C(
    "DHT sensor library (Adafruit)", "#include <DHT.h>",
    [("VCC (1-pin)", "5V", "3.3V da ham ishlaydi"),
     ("DATA (2-pin)", "D2", "VCC bilan orasiga 10 kOm tortuvchi rezistor"),
     ("NC (3-pin)", "—", "ulanmaydi"),
     ("GND (4-pin)", "GND", "")],
    esp32=[("VCC", "3.3V", ""),
           ("DATA", "GPIO4", "10 kOm tortuvchi rezistor bilan"),
           ("GND", "GND", "")],
    diqqat="Tortuvchi rezistorsiz o'qish \"nan\" qaytaradi. DHT22 sekundda "
           "faqat bir marta o'qiladi — tezroq so'rov qilsa eski qiymat keladi.",
    kalitlar=["dht", "harorat va namlik", "namlik va harorat", "meteo", "ob-havo"]),

"HC-SR04 (ultratovush masofa)": C(
    None, None,
    [("VCC", "5V", "3.3V da ishonchsiz ishlaydi"),
     ("TRIG", "D9", "chiqish — impuls yuboriladi"),
     ("ECHO", "D10", "kirish — qaytgan vaqt o'lchanadi"),
     ("GND", "GND", "")],
    esp32=[("VCC", "5V", "VIN pinidan"),
           ("TRIG", "GPIO5", ""),
           ("ECHO", "GPIO18", "kuchlanish bo'luvchi orqali (5V -> 3.3V)"),
           ("GND", "GND", "")],
    diqqat="ESP32 da ECHO to'g'ridan-to'g'ri ulanmaydi: 5V signal 3.3V pinni "
           "shikastlaydi. Ikki rezistor (1 kOm + 2 kOm) bilan bo'luvchi qo'yiladi. "
           "Masofa = vaqt * 0.034 / 2.",
    kalitlar=["hc-sr04", "ultratovush", "masofa", "radar", "parkovka"]),

"PIR HC-SR501 (harakat)": C(
    None, None,
    [("VCC", "5V", ""),
     ("OUT", "D2", "raqamli kirish, HIGH = harakat bor"),
     ("GND", "GND", "")],
    diqqat="Yoqilgandan keyin 30-60 sekund \"isinadi\" — bu vaqtda noto'g'ri "
           "signal beradi. Moduldagi ikki vint sezgirlik va kechikishni sozlaydi.",
    kalitlar=["pir", "harakat datchi", "harakatni aniqlash", "hc-sr501"]),

"Tuproq namligi datchigi": C(
    None, None,
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("A0 (analog chiqish)", "A0", "namlik darajasi"),
     ("D0 (raqamli chiqish)", "D3", "chegaradan o'tganda, ixtiyoriy")],
    diqqat="Doimiy kuchlanish berilsa elektrodlar tez korroziyaga uchraydi — "
           "VCC ni raqamli pinga ulab, faqat o'lchash paytida yoqish tavsiya etiladi.",
    kalitlar=["tuproq", "namlik datch", "sug'orish"]),

"Suv sathi datchigi": C(
    None, None,
    [("VCC / +", "5V", ""),
     ("GND / -", "GND", ""),
     ("S (signal)", "A0", "suv qancha baland bo'lsa, qiymat katta")],
    diqqat="Datchik faqat suvga tegib turgan qismini o'lchaydi. Kalibrlash uchun "
           "quruq va to'liq botgan holatdagi qiymatlar yozib olinadi.",
    kalitlar=["suv sath", "suv datch"]),

"Ovoz (mikrofon) datchigi": C(
    None, None,
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("OUT / AO", "A0", "analog — tovush kuchi"),
     ("DO", "D4", "raqamli — chegaradan oshganda, ixtiyoriy")],
    diqqat="Moduldagi potensiometr sezgirlikni sozlaydi. Qarsakni aniqlash uchun "
           "raqamli chiqish qulayroq.",
    kalitlar=["ovoz datch", "mikrofon", "qarsak"]),

"Reed datchigi (magnit kalit)": C(
    None, None,
    [("Bir oyoq", "D2", "INPUT_PULLUP bilan"),
     ("Ikkinchi oyoq", "GND", "")],
    diqqat="Oddiy tugma kabi ishlaydi — magnit yaqinlashganda ulanadi. "
           "Eshik/deraza ochilishini aniqlash uchun ishlatiladi.",
    kalitlar=["reed", "magnit kalit"]),

"Hall datchigi": C(
    None, None,
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("OUT", "D2", "raqamli turida; analog turida A0 ga")],
    diqqat="Magnitning qaysi qutbi yaqinlashganiga sezgir bo'lgan turlari bor — "
           "ishlamasa magnitni teskari o'girib ko'ring.",
    kalitlar=["hall", "magnit maydon", "aylanish tezlig"]),

"Qiyalik (tilt) datchigi": C(
    None, None,
    [("Bir oyoq", "D2", "INPUT_PULLUP bilan"),
     ("Ikkinchi oyoq", "GND", "")],
    diqqat="Ichidagi sharcha zanjirni ulaydi — qattiq silkitilganda ham signal "
           "beradi, shuning uchun dasturda kichik kechikish qo'yish kerak.",
    kalitlar=["tilt", "qiyalik", "og'ish"]),

"Olov (flame) datchigi": C(
    None, None,
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("AO", "A0", "olov kuchi"),
     ("DO", "D3", "olov bor/yo'q")],
    diqqat="Infraqizil nurga sezgir — quyosh nuri va lampa ham signal berishi "
           "mumkin. Sinovda oddiy chiroqdan uzoqroqda tekshiring.",
    kalitlar=["olov", "flame", "yong'in"]),

"MQ-2 (gaz va tutun)": C(
    None, None,
    [("VCC", "5V", "modul isishi uchun 5V shart"),
     ("GND", "GND", ""),
     ("AO", "A0", "gaz konsentratsiyasi"),
     ("DO", "D3", "chegaradan oshganda")],
    diqqat="Birinchi ishlatishda 24 soatgacha \"isinish\" (burn-in) kerak, aks "
           "holda ko'rsatkich suzib turadi. Modul sezilarli isiydi — bu normal.",
    kalitlar=["mq-2", "gaz", "tutun", "havo sifat"]),

"Joystik moduli": C(
    None, None,
    [("VCC / +5V", "5V", ""),
     ("GND", "GND", ""),
     ("VRx", "A0", "gorizontal o'q"),
     ("VRy", "A1", "vertikal o'q"),
     ("SW", "D2", "bosish tugmasi, INPUT_PULLUP bilan")],
    diqqat="O'rta holatda qiymat ~512 (Uno'da). Aniq markazni topib, uni dasturda "
           "\"nol\" deb olish kerak — har bir joystikda biroz farq qiladi.",
    kalitlar=["joystik", "joystick"]),

"Klaviatura 4x4 (keypad)": C(
    "Keypad", "#include <Keypad.h>",
    [("R1, R2, R3, R4 (qatorlar)", "D9, D8, D7, D6", "chiqish sifatida skanerlanadi"),
     ("C1, C2, C3, C4 (ustunlar)", "D5, D4, D3, D2", "kirish sifatida o'qiladi")],
    diqqat="8 pin bilan 16 tugma aniqlanadi — bu matritsa skanerlash usuli. "
           "Simlar tartibi chalkashsa, tugmalar noto'g'ri javob beradi.",
    kalitlar=["klaviatura", "keypad", "matritsa klaviatura", "parol"]),

"Rotatsion enkoder": C(
    None, None,
    [("CLK / A", "D2", "uzilish (interrupt) pini bo'lishi yaxshi"),
     ("DT / B", "D3", ""),
     ("SW", "D4", "bosish tugmasi, INPUT_PULLUP"),
     ("+", "5V", ""),
     ("GND", "GND", "")],
    diqqat="Sakrash (dırıltı) juda ko'p — dasturda filtr yoki uzilish ishlatish "
           "kerak, aks holda bitta burashda bir necha qadam sanaladi.",
    kalitlar=["enkoder", "rotatsion"]),

# ============================================================ HARAKAT
"Servo SG90": C(
    "Servo", "#include <Servo.h>",
    [("Qizil sim", "5V", "3 dan ko'p servo bo'lsa tashqi 5V manba"),
     ("Jigarrang / qora sim", "GND", "tashqi manba GND si bilan birlashtiriladi"),
     ("Sariq / to'q sariq sim", "D9", "PWM pin")],
    esp32=[("Qizil", "5V (VIN)", "3.3V da kuchi yetmaydi"),
           ("Qora", "GND", ""),
           ("Sariq", "GPIO13", "ESP32Servo kutubxonasi ishlatiladi")],
    diqqat="Servo ishga tushganda kuchlanish cho'kadi va plata qayta yuklanadi — "
           "shuning uchun quvvat liniyasiga 100 uF kondensator qo'yiladi. "
           "ESP32 uchun \"ESP32Servo\" kutubxonasi kerak.",
    kalitlar=["servo", "sg90", "shlagbaum"]),

"DC motor (tranzistor orqali)": C(
    None, None,
    [("Motor bir chiqishi", "5V yoki tashqi +", ""),
     ("Motor ikkinchi chiqishi", "Tranzistor kollektori (BC547)", ""),
     ("Tranzistor bazasi", "D9", "1 kOm rezistor orqali"),
     ("Tranzistor emitteri", "GND", ""),
     ("Motor uchlariga", "1N4007 diod", "teskari qutblab — himoya uchun")],
    diqqat="Diodsiz ulash tranzistorni kuydiradi: motor to'xtaganda teskari "
           "kuchlanish (EMK) hosil bo'ladi. Motorni to'g'ridan-to'g'ri plata piniga "
           "ULASH MUMKIN EMAS — pin 40 mA, motor esa bir necha yuz mA tortadi.",
    kalitlar=["dc motor", "motor tranzistor"]),

"L298N motor drayveri": C(
    None, None,
    [("VCC / +12V", "Tashqi 6-12V manba +", "batareya bloki"),
     ("GND", "GND", "Arduino GND si bilan BIRLASHTIRILADI"),
     ("5V", "Arduino 5V", "jumper turgan bo'lsa drayver o'zi 5V beradi"),
     ("IN1", "D8", "1-motor yo'nalishi"),
     ("IN2", "D9", "1-motor yo'nalishi"),
     ("ENA", "D10 (PWM)", "1-motor tezligi"),
     ("IN3", "D6", "2-motor yo'nalishi"),
     ("IN4", "D7", "2-motor yo'nalishi"),
     ("ENB", "D5 (PWM)", "2-motor tezligi"),
     ("OUT1, OUT2", "1-motor simlari", ""),
     ("OUT3, OUT4", "2-motor simlari", "")],
    diqqat="Umumiy GND eng muhim shart — Arduino va drayver GND si ulanmasa "
           "boshqaruv signali ishlamaydi. IN1=HIGH, IN2=LOW -> bir yo'nalish; "
           "teskarisi -> ikkinchi yo'nalish; ikkisi bir xil -> to'xtaydi.",
    kalitlar=["l298n", "motor drayver", "shassi", "ikki motor"]),

"Qadamli motor 28BYJ-48 + ULN2003": C(
    "Stepper", "#include <Stepper.h>",
    [("IN1", "D8", ""),
     ("IN2", "D9", ""),
     ("IN3", "D10", ""),
     ("IN4", "D11", ""),
     ("VCC (+)", "5V", "tashqi 5V manba yaxshiroq"),
     ("GND (-)", "GND", ""),
     ("Motor shlangi", "ULN2003 rozetkasi", "faqat bir tomonga kiradi")],
    diqqat="Stepper kutubxonasida pin tartibi 8, 10, 9, 11 tarzida beriladi "
           "(IN1, IN3, IN2, IN4) — tartib buzilsa motor titraydi, aylanmaydi. "
           "Bir to'liq aylanish 2048 qadam (yarim qadam rejimida 4096).",
    kalitlar=["qadamli", "stepper", "28byj", "uln2003"]),

"Rele moduli": C(
    None, None,
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("IN / S", "D7", "raqamli chiqish"),
     ("COM, NO, NC", "Yuklama zanjiri", "kuchli tomon — plataga ULANMAYDI")],
    diqqat="Ko'p modullar TESKARI mantiqda ishlaydi: LOW berilganda ulanadi. "
           "220V bilan ishlash O'QITUVCHI NAZORATIDA va faqat namoyish tarzida "
           "bo'lishi kerak — o'quvchilarga 220V tegishi mumkin emas.",
    kalitlar=["rele", "relay", "rozetka", "kuchli yuklama"]),

"Lazer moduli": C(
    None, None,
    [("VCC / +", "5V", ""),
     ("GND / -", "GND", ""),
     ("S / SIG", "D8", "yoqish/o'chirish")],
    diqqat="Lazer nuriga to'g'ridan-to'g'ri qaramaslik kerak — ko'zga xavfli. "
           "Darsda faqat pastga yoki devorga qaratib ishlatiladi.",
    kalitlar=["lazer", "laser"]),

# ============================================================ ALOQA
"IR qabul qilgich VS1838": C(
    "IRremote", "#include <IRremote.h>",
    [("OUT (signal)", "D2", "modul oldidan qaraganda chap pin"),
     ("GND", "GND", "o'rta pin"),
     ("VCC", "5V", "o'ng pin")],
    diqqat="Pin tartibi ko'p modullarda OUT-GND-VCC — teskari ulansa qiziydi. "
           "Avval pult kodlarini Serial monitorda chiqarib yozib olish kerak, "
           "har bir pultda kodlar boshqacha.",
    kalitlar=["ir qabul", "vs1838", "pult", "infraqizil"]),

"Bluetooth HC-05 / JDY-31": C(
    "SoftwareSerial", "#include <SoftwareSerial.h>",
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("TXD", "D10 (RX)", "modul TX -> plata RX"),
     ("RXD", "D11 (TX)", "kuchlanish bo'luvchi orqali (5V -> 3.3V)")],
    diqqat="TX va RX KESIB ulanadi: modulning TX i platanining RX iga. "
           "Modulning RX pini 3.3V mantiqda — 5V to'g'ridan-to'g'ri berilsa "
           "shikastlanadi. Standart parol: 1234 yoki 0000.",
    kalitlar=["bluetooth", "hc-05", "jdy-31"]),

"RFID RC522": C(
    "MFRC522", "#include <MFRC522.h>\n#include <SPI.h>",
    [("SDA / SS", "D10", ""),
     ("SCK", "D13", "SPI takt"),
     ("MOSI", "D11", ""),
     ("MISO", "D12", ""),
     ("IRQ", "—", "ulanmaydi"),
     ("GND", "GND", ""),
     ("RST", "D9", ""),
     ("3.3V", "3.3V", "5V BERILMAYDI — modul kuyadi")],
    diqqat="RC522 faqat 3.3V bilan ishlaydi. 5V ga ulash eng ko'p uchraydigan "
           "va modulni butunlay ishdan chiqaradigan xato.",
    kalitlar=["rfid", "rc522", "karta", "kirish nazorat"]),

"microSD kart moduli": C(
    "SD", "#include <SD.h>\n#include <SPI.h>",
    [("CS", "D4", ""),
     ("SCK", "D13", ""),
     ("MOSI", "D11", ""),
     ("MISO", "D12", ""),
     ("VCC", "5V", "modulda stabilizator bo'lsa"),
     ("GND", "GND", "")],
    diqqat="Karta FAT32 formatida bo'lishi kerak. Fayl nomi 8.3 formatida "
           "(masalan DATA.TXT) — uzun nomlar ishlamaydi. Yozgandan keyin "
           "file.close() qilinmasa ma'lumot saqlanmaydi.",
    kalitlar=["sd kart", "microsd", "data log", "ma'lumot yoz"]),

"RTC DS3231 (real vaqt soati)": C(
    "RTClib (Adafruit)", "#include <RTClib.h>\n#include <Wire.h>",
    [("VCC", "5V", "3.3V da ham ishlaydi"),
     ("GND", "GND", ""),
     ("SDA", "A4", ""),
     ("SCL", "A5", "")],
    esp32=[("VCC", "3.3V", ""), ("GND", "GND", ""),
           ("SDA", "GPIO21", ""), ("SCL", "GPIO22", "")],
    diqqat="Ichida CR2032 batareya bo'lishi kerak — u bo'lmasa quvvat o'chganda "
           "vaqt nolga qaytadi. Vaqtni bir marta o'rnatib, keyin o'rnatish kodini "
           "izohga olish kerak.",
    kalitlar=["rtc", "ds3231", "real vaqt", "soat"]),

# ============================================================ ILG'OR / AI
"MPU6050 (akselerometr va giroskop)": C(
    "Adafruit MPU6050 + Adafruit Unified Sensor",
    "#include <Adafruit_MPU6050.h>\n#include <Wire.h>",
    [("VCC", "5V", "modulda stabilizator bor"),
     ("GND", "GND", ""),
     ("SDA", "A4", ""),
     ("SCL", "A5", ""),
     ("AD0", "GND", "I2C manzilini 0x68 qiladi")],
    esp32=[("VCC", "3.3V", ""), ("GND", "GND", ""),
           ("SDA", "GPIO21", ""), ("SCL", "GPIO22", ""),
           ("AD0", "GND", "")],
    diqqat="AI uchun ma'lumot yig'ishda namuna olish tezligi (masalan 100 Hz) "
           "butun yig'ish davomida BIR XIL bo'lishi kerak — aks holda model "
           "noto'g'ri o'rganadi.",
    kalitlar=["mpu6050", "akselerometr", "giroskop", "imo-ishora", "gesture"]),

"BMP280 (bosim va balandlik)": C(
    "Adafruit BMP280", "#include <Adafruit_BMP280.h>\n#include <Wire.h>",
    [("VCC / VIN", "3.3V", ""),
     ("GND", "GND", ""),
     ("SDA / SDI", "A4", ""),
     ("SCL / SCK", "A5", "")],
    diqqat="I2C manzili 0x76 yoki 0x77. Balandlikni hisoblash uchun joydagi "
           "dengiz sathi bosimini kiritish kerak, aks holda xato katta bo'ladi.",
    kalitlar=["bmp280", "bosim", "balandlik"]),

"INA219 (tok va quvvat o'lchagich)": C(
    "Adafruit INA219", "#include <Adafruit_INA219.h>\n#include <Wire.h>",
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("SDA", "A4", ""),
     ("SCL", "A5", ""),
     ("VIN+", "Manba +", "o'lchanadigan zanjir kirishi"),
     ("VIN-", "Yuklama +", "o'lchanadigan zanjir chiqishi")],
    diqqat="Modul zanjirga KETMA-KET ulanadi (tok o'lchash uchun), parallel emas. "
           "VIN+ va VIN- ni almashtirish manfiy qiymat beradi.",
    kalitlar=["ina219", "tok o'lch", "quvvat o'lch"]),

"HX711 + tenzodatchik (og'irlik)": C(
    "HX711", "#include <HX711.h>",
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("DT / DOUT", "D3", ""),
     ("SCK", "D2", ""),
     ("E+, E-, A+, A-", "Tenzodatchik simlari", "qizil-qora-yashil-oq tartibda")],
    diqqat="Har bir tenzodatchik uchun kalibrlash koeffitsientini o'zi topish "
           "kerak: ma'lum og'irlikni qo'yib, qiymatni shunga bo'lish. "
           "Tenzodatchik qattiq asosga mahkamlanmasa ko'rsatkich suzadi.",
    kalitlar=["hx711", "og'irlik", "tarozi", "yuk datch"]),

"TCS3200 (rang datchigi)": C(
    None, None,
    [("VCC", "5V", ""),
     ("GND", "GND", ""),
     ("S0", "D4", "chastota bo'luvchi"),
     ("S1", "D5", "chastota bo'luvchi"),
     ("S2", "D6", "rang filtri tanlash"),
     ("S3", "D7", "rang filtri tanlash"),
     ("OUT", "D8", "chastota chiqishi"),
     ("LED", "5V", "yorug'lik diodlarini yoqadi")],
    diqqat="Har bir rang uchun o'z qiymat oralig'ini kalibrlash kerak — xona "
           "yorug'ligi natijaga kuchli ta'sir qiladi. Datchik buyumga 1-2 sm "
           "masofada turishi kerak.",
    kalitlar=["tcs3200", "rang datch", "saralash"]),

"XIAO ESP32S3 Sense (kamera va mikrofon)": C(
    "Edge Impulse chiqargan Arduino kutubxonasi",
    "#include <loyiha_nomi_inferencing.h>",
    [("Kamera", "Plataga o'rnatilgan shlang orqali", "alohida sim kerak emas"),
     ("Mikrofon", "Plataga o'rnatilgan", "alohida sim kerak emas"),
     ("USB-C", "Kompyuter", "dastur yuklash va quvvat"),
     ("Qo'shimcha sensor SDA", "D5 (GPIO6)", "I2C uchun"),
     ("Qo'shimcha sensor SCL", "D4 (GPIO5)", "I2C uchun")],
    diqqat="Kamera va mikrofon plataning o'zida — bu AI darslari uchun tanlangan "
           "asosiy sabab. Model Edge Impulse'da o'rgatiladi va ZIP kutubxona "
           "sifatida yuklab olinadi, keyin IDE'ga qo'shiladi. "
           "PSRAM sozlamasi yoqilgan bo'lishi kerak, aks holda kamera ishlamaydi.",
    kalitlar=["xiao", "esp32s3", "kamera", "mikrofondan", "tasvir tan", "ovoz tan",
              "tasvir ma'lumot", "ovoz buyruq", "ovoz modeli"]),

"ESP32-CAM": C(
    None, "#include <esp_camera.h>",
    [("5V", "5V", "3.3V da ishlamaydi — tok yetmaydi"),
     ("GND", "GND", ""),
     ("U0T (TX)", "USB-TTL RX", "dastur yuklash uchun"),
     ("U0R (RX)", "USB-TTL TX", "dastur yuklash uchun"),
     ("IO0", "GND", "FAQAT dastur yuklash paytida")],
    diqqat="Platada USB yo'q — dastur USB-TTL adapter orqali yuklanadi. "
           "Yuklashdan oldin IO0 ni GND ga ulash, yuklagandan keyin uzish shart. "
           "Kamera shlangi juda mo'rt.",
    kalitlar=["esp32-cam", "kamera modul", "video oqim", "stream"]),
}


# ---------------------------------------------------------------- qidirish
def topish(mavzu):
    """Dars mavzusiga mos komponentlarni qaytaradi (ko'pi bilan 3 ta)."""
    m = mavzu.lower().replace("'", "'")
    natija = []
    for nom, d in ULANISH.items():
        if nom.lower().split(" (")[0] in m:
            natija.append((nom, d))
            continue
        for k in d["kalitlar"]:
            if k in m:
                natija.append((nom, d))
                break
    return natija[:3]


def bolim(mavzu, esp=False, plata=True):
    """Komponent bo'limi uchun ma'lumot: [{nom, tasnif, ishlash, oqish, ...}].

    plata=False bo'lsa (5-6-sinfning platasiz elektronika darslari) pin
    xaritasi va Arduino kodi BERILMAYDI — ular o'sha darsda ma'nosiz.
    Lekin komponentning texnik pasporti (tasnif, ichida nima sodir bo'ladi,
    hayotda qayerda uchraydi) baribir kerak va u qoladi.

    Sarlavhada raqam YO'Q — bo'lim raqami (08, 09, ...) app.js da beriladi,
    shunda boshqa bo'lim qo'shilsa tartib buzilmaydi."""
    topilgan = topish(mavzu)
    if not topilgan:
        return []
    bloklar = []
    for nom, d in topilgan:
        if not plata:
            p = pasport_olish(nom)
            if not p:
                continue
            bloklar.append({
                "nom": nom,
                "tasnif": list(p["tasnif"]),
                "ishlash": list(p["ishlash"]),
                "qollash": list(p["qollash"]),
            })
            continue
        points = []
        kut = d["kutubxona"]
        if kut:
            points.append(f"Kutubxona: {kut} — Arduino IDE > Sketch > "
                          f"Include Library > Manage Libraries orqali o'rnatiladi.")
            if d["include"]:
                points.append("Kodda: " + d["include"].replace("\n", " va "))
        else:
            points.append("Kutubxona kerak emas — oddiy pin buyruqlari bilan ishlaydi.")
        # ESP32 yo'nalishida: modulga xos ESP32 xaritasi bo'lsa o'sha, bo'lmasa
        # Uno xaritasi ko'rsatiladi, lekin pin nomini moslashtirish kerakligi aytiladi.
        esp_bor = bool(d["esp32"])
        pinlar = d["esp32"] if (esp and esp_bor) else d["uno"]
        plata = "ESP32" if (esp and esp_bor) else "Arduino Uno"
        for pin, port, izoh in pinlar:
            s = f"{pin} -> {plata} {port}"
            if izoh:
                s += f" ({izoh})"
            points.append(s)
        if esp and not esp_bor:
            points.append("ESP32 da: D2, D9 kabi raqamli pinlar o'rniga bo'sh GPIO "
                          "(masalan GPIO4, GPIO5) olinadi; 5V o'rniga VIN, mantiq "
                          "darajasi esa 3.3V ekanini hisobga olish kerak.")
        if d["diqqat"]:
            points.append("DIQQAT: " + d["diqqat"])
        # Chizma uchun strukturali ma'lumot. app.js shundan SVG sxema chizadi —
        # matn ro'yxati bilan bir xil manbadan, shuning uchun ular hech qachon
        # bir-biridan farq qilib qolmaydi.
        blok = {
            "nom": nom,
            "points": points,
            "plata": plata,
            "pinlar": [[pin, port, izoh] for pin, port, izoh in pinlar],
        }
        # To'liq texnik pasport: tasnif, ichida nima sodir bo'lishi, qiymatni
        # o'qish tartibi va ishlaydigan kod namunasi (pasport.py).
        p = pasport_olish(nom)
        if p:
            blok["tasnif"] = list(p["tasnif"])
            blok["ishlash"] = list(p["ishlash"])
            blok["oqish"] = list(p["oqish"])
            if p["kod"]:
                blok["kod"] = p["kod"]
            if p["qollash"]:
                blok["qollash"] = list(p["qollash"])
        bloklar.append(blok)
    return bloklar


if __name__ == "__main__":
    print("Komponentlar:", len(ULANISH))
    for m in ["DHT22 — aniq harorat/namlik", "HC-SR04: masofa o'lchash",
              "Servo motorni boshqarish", "RFID RC522: identifikatsiya"]:
        got = topish(m)
        print(f"\n{m} -> {[g[0] for g in got]}")
