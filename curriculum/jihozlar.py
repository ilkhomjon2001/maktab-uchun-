# -*- coding: utf-8 -*-
"""
5-8-sinf robototexnika/elektronika kursi uchun jihoz ro'yxati.

Ikkita to'plam:
  SET A — 5-6-sinf  (elektronika asoslari + Arduino, blokli dasturlash)
  SET B — 7-8-sinf  (SET A ustiga: ilg'or Arduino + ESP32 + AI integratsiyasi)

Miqdorlar BITTA TO'PLAM uchun (1 to'plam = 2 o'quvchi, ya'ni juftlikda ishlash).
Sinf 12 o'quvchidan iborat bo'lsa -> 6 to'plam.

"mavzu" ustuni: shu komponent qaysi dars mavzusini ochishini ko'rsatadi.
84 dars/yil tuzilishini to'ldirish uchun har bir komponent kamida bitta
mustaqil mavzu berishi kerak — ro'yxat shu tamoyil bo'yicha tuzilgan.
"""

# (kategoriya, nom, soni, birlik, mavzu/izoh)

SET_A = [
    # --- Boshqaruv va prototiplash ---
    ("Boshqaruv", "Arduino Uno R3 (DIP korpus)", 1, "dona",
     "Asosiy plata. DIP korpus — mikrokontroller kuysa, almashtirish mumkin"),
    ("Boshqaruv", "USB kabel (A-B)", 1, "dona", "Plataga ulanish va quvvat"),
    ("Prototiplash", "Breadboard 830 nuqta", 1, "dona", "Asosiy yig'ish maydoni"),
    ("Prototiplash", "Breadboard 400 nuqta", 1, "dona", "Qo'shimcha/ajratilgan tugun"),
    ("Prototiplash", "Jumper sim M-M (65 dona)", 1, "to'plam", "Breadboard ulanishlari"),
    ("Prototiplash", "Jumper sim M-F (40 dona)", 1, "to'plam", "Modullarni ulash"),
    ("Prototiplash", "Bir tomirli montaj simi", 1, "to'plam", "Toza yig'ish madaniyati"),
    ("Prototiplash", "Montaj taglik (plata + breadboard uchun)", 1, "dona",
     "Yig'ilgan sxema buzilmasdan saqlanadi"),

    # --- O'lchov: Arduino rasmiy dasturida MAJBURIY ---
    ("O'lchov", "Raqamli multimetr", 1, "dona",
     "Om qonuni, kuchlanish/tok/qarshilik o'lchash. Arduino sillabusida 2-dars"),
    ("O'lchov", "Krokodil ulagichli sim", 1, "juft", "Multimetr bilan o'lchash"),

    # --- Passiv komponentlar ---
    ("Passiv", "Rezistor 220 Om", 20, "dona", "LED cheklovchi rezistor"),
    ("Passiv", "Rezistor 330 Om", 10, "dona", "LED, umumiy maqsad"),
    ("Passiv", "Rezistor 1 kOm", 10, "dona", "Tranzistor bazasi, bo'luvchi"),
    ("Passiv", "Rezistor 4.7 kOm", 5, "dona", "I2C tortuvchi, rezistor zinasi"),
    ("Passiv", "Rezistor 10 kOm", 10, "dona", "Tugma tortuvchisi, kuchlanish bo'luvchi"),
    ("Passiv", "Rezistor 100 kOm", 5, "dona", "Yuqori qarshilikli bo'luvchi"),
    ("Passiv", "Kondensator 100 uF (elektrolit)", 4, "dona",
     "Servo/motor ishlaganda kuchlanish cho'kishini oldini oladi"),
    ("Passiv", "Kondensator 10 uF (elektrolit)", 4, "dona", "Filtrlash, RC zanjir"),
    ("Passiv", "Kondensator 100 nF (keramik)", 5, "dona", "Shovqin bostirish"),
    ("Passiv", "Diod 1N4007", 5, "dona", "Qutblanish himoyasi, tokning bir yo'nalishi"),
    ("Passiv", "Tranzistor BC547 (NPN)", 5, "dona", "Kalit sifatida tranzistor"),
    ("Passiv", "Tranzistor BC557 (PNP)", 3, "dona", "NPN/PNP farqi"),
    ("Passiv", "Stabilitron (Zener) 5.1V", 2, "dona", "Kuchlanish barqarorlashtirish"),

    # --- Chiqish: yorug'lik ---
    ("Chiqish/yorug'lik", "LED 5mm qizil", 5, "dona", "Birinchi zanjir, qutblanish"),
    ("Chiqish/yorug'lik", "LED 5mm yashil", 5, "dona", "Svetofor loyihasi"),
    ("Chiqish/yorug'lik", "LED 5mm sariq", 5, "dona", "Svetofor loyihasi"),
    ("Chiqish/yorug'lik", "LED 5mm ko'k", 5, "dona", "Turli rangda kuchlanish farqi"),
    ("Chiqish/yorug'lik", "LED 5mm oq", 5, "dona", "Yorug'lik intensivligi"),
    ("Chiqish/yorug'lik", "RGB LED (umumiy katod)", 2, "dona", "Rang aralashtirish, PWM"),
    ("Chiqish/yorug'lik", "7-segment indikator, 1 razryad", 2, "dona", "Raqam ko'rsatish"),
    ("Chiqish/yorug'lik", "7-segment indikator, 4 razryad", 1, "dona", "Sanoq, taymer, soat"),
    ("Chiqish/yorug'lik", "LCD 1602 ekran", 1, "dona", "Matn chiqarish"),
    ("Chiqish/yorug'lik", "I2C moduli (LCD uchun)", 1, "dona", "I2C protokoli, 2 sim bilan ulash"),
    ("Chiqish/yorug'lik", "LED matritsa 8x8 (MAX7219)", 1, "dona", "Animatsiya, belgi chizish"),
    ("Chiqish/yorug'lik", "WS2812 adreslanadigan LED lenta (8 LED)", 1, "dona",
     "Har bir LED alohida boshqariladi — massiv mavzusi"),

    # --- Chiqish: tovush ---
    ("Chiqish/tovush", "Passiv zummer", 2, "dona", "Chastota, nota, musiqa"),
    ("Chiqish/tovush", "Aktiv zummer", 2, "dona", "Signal berish, aktiv/passiv farqi"),
    ("Chiqish/tovush", "Kichik dinamik 8 Om", 1, "dona", "Tovush to'lqini"),

    # --- Chiqish: harakat ---
    ("Harakat", "Servo SG90", 2, "dona", "Burchak boshqaruvi, PWM"),
    ("Harakat", "DC motor 130 + g'ildirak", 2, "dona", "Aylanish, tezlik"),
    ("Harakat", "L298N motor drayveri", 1, "dona", "Ikki motorni yo'nalish bilan boshqarish"),
    ("Harakat", "Qadamli motor 28BYJ-48 + ULN2003", 1, "to'plam", "Aniq burchakli aylanish"),

    # --- Kirish: mexanik ---
    ("Kirish/mexanik", "Tugma (tactile)", 10, "dona", "Raqamli kirish, debounce"),
    ("Kirish/mexanik", "Ikki holatli vklyuchatel", 3, "dona", "Holatni saqlash"),
    ("Kirish/mexanik", "Potensiometr 10 kOm", 3, "dona", "Analog kirish, kuchlanish bo'luvchi"),
    ("Kirish/mexanik", "Joystik moduli", 1, "dona", "Ikki o'qli analog kirish"),
    ("Kirish/mexanik", "Membranali klaviatura 4x4", 1, "dona", "Matritsa skanerlash, parol"),
    ("Kirish/mexanik", "Rotatsion enkoder", 1, "dona", "Aylanishni sanash, menyu"),
    ("Kirish/mexanik", "Qiyalik (tilt) datchigi", 2, "dona", "Holat aniqlash"),
    ("Kirish/mexanik", "Reed (magnit) datchigi + magnit", 2, "dona", "Eshik ochilishini aniqlash"),

    # --- Kirish: muhit sensorlari ---
    ("Sensorlar", "Fotorezistor (LDR)", 4, "dona", "Yorug'lik o'lchash, tungi chiroq"),
    ("Sensorlar", "Fototranzistor", 2, "dona", "Tez yorug'lik datchigi"),
    ("Sensorlar", "DHT22 harorat va namlik", 1, "dona", "Raqamli sensor protokoli"),
    ("Sensorlar", "NTC termistor", 2, "dona", "Analog harorat, kalibrlash"),
    ("Sensorlar", "Suv sathi datchigi", 1, "dona", "Suv bosishidan ogohlantirish"),
    ("Sensorlar", "Tuproq namligi datchigi", 1, "dona", "Avtomatik sug'orish loyihasi"),
    ("Sensorlar", "Ovoz (mikrofon) datchigi", 1, "dona", "Qarsakka javob beruvchi chiroq"),
    ("Sensorlar", "HC-SR04 ultratovush masofa", 1, "dona", "Masofa o'lchash, parkovka radari"),
    ("Sensorlar", "PIR HC-SR501 harakat datchigi", 1, "dona", "Odam harakatini aniqlash"),
    ("Sensorlar", "Hall (magnit maydon) datchigi", 1, "dona", "Aylanish tezligini o'lchash"),
    ("Sensorlar", "Olov (flame) datchigi", 1, "dona", "Yong'in signalizatsiyasi"),

    # --- Aloqa ---
    ("Aloqa", "IR qabul qilgich VS1838", 2, "dona", "Pultdan signal qabul qilish"),
    ("Aloqa", "IR pult", 1, "dona", "Masofadan boshqarish"),

    # --- Mantiq ---
    ("Mantiq", "Siljish registri 74HC595", 2, "dona",
     "3 pin bilan 8 chiqish — pin yetishmasligi muammosi"),
    ("Mantiq", "Rele moduli 1 kanal", 1, "dona", "Kuchli yuklamani boshqarish"),

    # --- Quvvat ---
    ("Quvvat", "Krona 9V + shteker", 1, "to'plam", "Mustaqil quvvat"),
    ("Quvvat", "Batareya bloki 4xAA", 1, "dona", "Motor uchun alohida quvvat"),
    ("Quvvat", "5V 2A adapter", 1, "dona", "Barqaror stol quvvati"),

    # --- Saqlash ---
    ("Saqlash", "Komponent qutisi (bo'lmali)", 1, "dona", "To'plam tarqalib ketmasligi uchun"),
]

# SET B = SET A + quyidagilar (7-8-sinf: ilg'or Arduino + ESP32 + AI)
SET_B_EXTRA = [
    # --- ESP32 platformasi ---
    ("ESP32", "ESP32 DevKit v1 + USB kabel", 1, "to'plam",
     "WiFi/Bluetooth, veb-server, IoT"),
    ("ESP32", "XIAO ESP32S3 Sense (kamera + mikrofon)", 1, "dona",
     "AI: tasvir va ovoz tanish uchun ASOSIY plata (Edge Impulse/TinyML)"),
    ("ESP32", "OLED ekran 0.96\" I2C (SSD1306)", 1, "dona", "Grafik chiqish, sensor grafigi"),

    # --- AI uchun sensorlar ---
    ("AI sensorlari", "MPU6050 akselerometr + giroskop", 1, "dona",
     "Imo-ishorani tanish (gesture recognition) — AI modelining kirish ma'lumoti"),
    ("AI sensorlari", "Rang datchigi TCS3200", 1, "dona", "Rang bo'yicha saralash"),
    ("AI sensorlari", "Chiziq datchigi (IR juft)", 2, "dona", "Chiziq bo'ylab yuruvchi robot"),

    # --- Ilg'or sensorlar ---
    ("Ilg'or sensorlar", "Gaz datchigi MQ-2", 1, "dona", "Havo sifati, gaz sizishi"),
    ("Ilg'or sensorlar", "BMP280 bosim va balandlik", 1, "dona", "Ob-havo stansiyasi"),
    ("Ilg'or sensorlar", "HX711 + tenzodatchik (yuk)", 1, "to'plam", "Elektron tarozi"),
    ("Ilg'or sensorlar", "INA219 tok va kuchlanish datchigi", 1, "dona",
     "Quvvat iste'molini o'lchash — muhandislik tahlili"),

    # --- Ma'lumot va vaqt ---
    ("Ma'lumot", "MicroSD kart moduli + 8GB karta", 1, "to'plam",
     "Ma'lumotni yozib borish (data logging)"),
    ("Ma'lumot", "RTC DS3231 real vaqt soati", 1, "dona", "Vaqt bo'yicha avtomatlashtirish"),

    # --- Aloqa ---
    ("Aloqa+", "RFID RC522 + karta/brelok", 1, "to'plam", "Identifikatsiya, kirish nazorati"),
    ("Aloqa+", "Bluetooth moduli JDY-31", 1, "dona", "Telefondan boshqarish"),

    # --- Harakat (kuchliroq) ---
    ("Harakat+", "Servo MG90S (metall tishli)", 2, "dona", "Kuchli, aniq harakat"),
    ("Harakat+", "L293D motor drayveri", 1, "dona", "Muqobil drayver, IC darajasi"),
    ("Harakat+", "Lazer moduli", 1, "dona", "Nur uzatish, to'siqni aniqlash"),
    ("Harakat+", "Rele moduli 2 kanal", 1, "dona", "Ikki qurilmani boshqarish"),

    # --- Quvvat ---
    ("Quvvat+", "18650 akkumulyator + blok + zaryadlagich", 1, "to'plam",
     "Mustaqil ishlaydigan qurilma"),
    ("Quvvat+", "Kuchlanish stabilizatori AMS1117 (3.3V)", 2, "dona",
     "5V va 3.3V mantiq darajalari farqi"),
]

# Sinf uchun UMUMIY jihoz (har to'plamga emas, butun sinfga)
UMUMIY = [
    ("Kavsharlash", "Kavsharlash stansiyasi (harorat rostlanadigan)", 3, "dona",
     "7-8-sinf: prototipdan qurilmaga o'tish"),
    ("Kavsharlash", "Qalay (0.8mm) + kanifol", 3, "to'plam", "Kavsharlash sarfi"),
    ("Kavsharlash", "Kavshar so'rg'ich / oplyotka", 3, "dona", "Xatoni tuzatish"),
    ("Kavsharlash", "Uchinchi qo'l (lupa bilan)", 3, "dona", "Kavsharlashda ushlab turish"),
    ("Kavsharlash", "Prototip plata (PCB) 5x7 sm", 20, "dona", "Doimiy montaj"),
    ("Kavsharlash", "Termousadka trubka to'plami", 1, "to'plam", "Ulanishni izolyatsiya qilish"),
    ("Asbob", "Sim kesgich (bokorez)", 6, "dona", "Sim tayyorlash"),
    ("Asbob", "Sim tozalagich (striper)", 6, "dona", "Izolyatsiyani tozalash"),
    ("Asbob", "Pinset", 6, "dona", "Mayda komponent bilan ishlash"),
    ("Asbob", "Otvertka to'plami (mayda)", 3, "to'plam", "Korpus yig'ish"),
    ("Xavfsizlik", "Himoya ko'zoynagi", 12, "dona", "Kavsharlash va kesishda majburiy"),
    ("Xavfsizlik", "Tutun so'rg'ich / ventilyator", 2, "dona", "Kavshar tutunini chiqarish"),
    ("Xavfsizlik", "Birinchi yordam quti", 1, "dona", "Kuyish holatlari uchun"),
    ("Zaxira", "Zaxira Arduino Uno", 2, "dona", "Kuygan platani almashtirish"),
    ("Zaxira", "Zaxira ESP32", 2, "dona", "Kuygan platani almashtirish"),
    ("Zaxira", "Zaxira LED / rezistor / sim to'plami", 1, "to'plam", "Yo'qolgan mayda komponent"),
]


def set_b_full():
    """SET B = SET A ning hammasi + qo'shimchalar."""
    return SET_A + SET_B_EXTRA


def stats():
    a = len(SET_A)
    b = len(set_b_full())
    return {
        "SET A pozitsiya": a,
        "SET B pozitsiya": b,
        "Umumiy jihoz pozitsiya": len(UMUMIY),
        "SET A dona": sum(x[2] for x in SET_A),
        "SET B dona": sum(x[2] for x in set_b_full()),
    }


if __name__ == "__main__":
    for k, v in stats().items():
        print(f"{k}: {v}")
