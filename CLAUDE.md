# Robbit Academy — Robototexnika Dasturi va Dars Rejalari Loyihasi

## Loyiha haqida
Robbit Academy (Toshkent, O'zbekiston) uchun 0–4-sinf robototexnika va IT dasturi.
Ikkita asosiy natija tayyorlanmoqda:
1. **Excel dastur fayli** (`Dastur_0-4sinf_Makerzoid_SPIKE.xlsx`) — to'liq o'quv rejasi, tayyor va tasdiqlangan.
2. **Dars rejalar sayti** (`site/`) — har bir darsning to'liq ishlanmasi (maqsad, lug'at, soft skill, resurslar, nazariya, amaliyot, uyga vazifa). **878/878 dars TAYYOR.** Har bir qurish darsiga bosqichma-bosqich rasmli instruksiya biriktirilgan (666/666).

**Jonli sayt:** http://169.58.130.201:8081 (Docker `nginx:alpine`, `/opt/robbit-academy` bind-mount).
Server o'sha papkada git ishchi nusxasi — **yangilash uchun `cd /opt/robbit-academy && git pull`** yetarli.

## Papka tuzilishi
```
site/                  — Dars rejalar sayti (statik HTML/JS). GIT REPO = AYNAN SHU PAPKA.
  index.html              — asosiy sahifa + barcha CSS
  app.js                  — navigatsiya, qidiruv, dars ko'rsatish, instruksiya galereyasi
  tree_data.js            — barcha 878 ta darsning tuzilishi (sinf/yil/chorak/mavzu/model)
  sample_lessons.js       — 878 ta to'liq dars rejasi (kalit: "yil|sinf|chorak|index")
  resources.js            — SPIKE uchun LEGO rasmiy instruksiya havolalari (18 dars)
  instructions_index.js   — Makerzoid instruksiyalari ko'rsatkichi (AVTOMATIK, qo'lda tegmang)
  instructions/makerzoid/ — 241 model x qadamlar = 16 681 WebP rasm (~323 MB)
  maydon.js               — 4 ta musobaqa maydonchasi chizmasi (SVG)
  README.md               — serverga joylash yo'riqnomasi
  CLAUDE.md               — SHU FAYL (2026-08-08 da project_bundle dan bu yerga ko'chirildi)

site/curriculum/       — Excel dasturini generatsiya qiluvchi Python skriptlar
  models_catalog.py      — 281 ta Makerzoid Robot Master (Premium) modeli, 11 bo'lim
  model_themes.py        — har bir modelning STEAM temasi + o'qituvchi qo'llanmasi (226 model -> 20 tema)
  year1_model_pools.py   — 1-yil uchun har sinf/chorak bo'yicha 18 tadan model (jami 72/yil)
  year1_generator.py     — Year1 dasturini generatsiya qiladi (ALL_GRADES_Y1_NEW)
  curriculum_data.py     — SPIKE (2-yil 4-sinf) dasturi + Year1 ni import qiladi
  dasturlash_track.py    — 2-yil, 2-3-sinf, 3-4-chorak uchun Scratch dasturlash kursi (19 dars)
  musobaqa_nazorat.py    — 1-yil har chorak uchun musobaqa-nazorat matnlari (RoboRace/RoboLift/RoboSense/RoboChampionship)
  amaliy_tags.py          — SPIKE grade uchun amaliy natija teglari
  steam_notes.py         — (eskirgan, endi model_themes.py ishlatiladi)
  build_xlsx.py          — hammasini yig'ib Excel faylni yaratadi

  --- dars rejalarini generatsiya qiluvchi qism ---
  generate_lessons.py    — BARCHA 878 darsni yig'ib site/sample_lessons.js ga yozadi
  lesson_templates.py    — 18 tema x 3 daraja (A=0-1-sinf, B=2-3, C=4) kontent bazasi
  lesson_subtopics.py + lesson_subtopics2.py — 178 ta sub-mavzu (takrorlanishning oldini oladi)
  lesson_templates_special.py / _nazorat_loyiha.py / _dasturlash.py / _spike.py
  missions.py            — 4 ta SPIKE missiyasi: aniq vazifa, koordinatalar, ball taqsimoti

  --- instruksiya rasmlari ---
  instructions_map.py    — 281 katalog modelini zip papkalariga bog'laydi (25 tasi qo'lda)
  build_instructions.py  — zipdan chiqarib, qirqib, WebP ga siqadi (--yil / --sinf / --all)
  list_models.py         — yordamchi: qaysi modelda instruksiya bor/yo'q

output/                — repo'DAN TASHQARIDA (project_bundle/output)
  Dastur_0-4sinf_Makerzoid_SPIKE.xlsx  — yakuniy Excel fayl

D:\maktab uchun sayt\Robot master(PM) instruction-*.zip  — manba rasmlar (2 ta zip, 3.5 GB)
```

⚠️ **Yo'l qoidasi:** `curriculum/` sayt repo'sining ICHIDA. Skriptlarda sayt ildizi
`os.path.dirname(HERE)` (ota-papka) orqali topiladi — `HERE/../site` DEYILMAYDI.
`output/` esa repo'dan tashqarida: `HERE/../../output`.

## MUHIM QARORLAR (o'zgartirmaslik kerak, foydalanuvchi bilan kelishilgan)

- **1-yil = 100% qurish, dasturlash YO'Q.** Har chorak 18 ta turli robot (har biri BITTA darsda: yig'ish+sinov, chunki jihozlar keyingi darsga saqlanmaydi).
- **Har yil 84 dars** (4 chorak x 21 dars: 1 kirish + 18 model + 1 nazorat + 1 loyiha).
- **Dasturlash faqat 2-yil, 2-sinfdan boshlab**, 3-4-chorakda (haftaning YANGI 3-soatida, Scratch-uslub). 0-1-sinfda 2-yilda ham dasturlash yo'q — 1-yil bilan AYNAN bir xil.
- **1-chorak nazorat = "RoboRace"** (2m masofa, vaqt bo'yicha 5/4/3/2/FAILED — foydalanuvchi bergan aniq mezon). 2-4-chorak — shu uslubda taklif etilgan (RoboLift/RoboSense/RoboChampionship), aniq vaqt me'yorlari sinov orqali moslashtirilishi mumkin.
- **"Dars mavzusi" va "Amaliy ish" AJRATILGAN**: mavzu = ilmiy/STEAM tema (masalan "Ishqalanish kuchi"), amaliy ish = model nomi (masalan "Little Lantern 1"). Buni hech qachon birlashtirmaslik kerak.
- **SPIKE (2-yil 4-sinf)**: 1-chorak = 100% qurish (LEGO rasmiy nomlari: Driving Base 1/2/3, StarterBot, Robot Arm va h.k., education.lego.com dan). 3-4-chorak = to'liq missiya-asosida (Missiya 1-4), nazoratlar ball tizimi bilan (FLL uslubida).
- **Dars reja shabloni**: 7 bo'lim — Maqsad (3 band), Lug'at (5 ta), Soft skill, Resurslar, Nazariya qismi (kichik bo'limlarga bo'lingan, har birida daqiqa ko'rsatilgan), Amaliy ishlar (xuddi shunday), Uyga vazifa. Bu format foydalanuvchi tomonidan TASDIQLANGAN, **01–07 raqamlari o'zgarmaydi**. Qo'shimcha bo'limlar faqat 07 dan KEYIN qo'shiladi va ketma-ket raqamlanadi (08, 09, ...).
- **Bir xil temadagi darslar HAR XIL narsa o'rgatadi.** 5 ta "Richag qonuni" darsi bo'lsa, har biri richagning boshqa jihatini beradi (`lesson_subtopics*.py`, 178 sub-mavzu; `generate_lessons.py` dagi `theme_counter` har sinf ichida navbat bilan aylantiradi). Yangi dars qo'shilsa shu tizim buzilmasligi kerak.
- **Missiyalar aniq va bosqichma-bosqich** (`missions.py`): 4 missiya x 4 kichik topshiriq x 25 ball = 100 ball (4-chorak nazorati bilan mos). Har missiyaning 6 darsi n.A (qog'ozda) → n.F (rasmiy urinish) tarzida qiyinlashadi. Maydoncha 200x100 sm, koordinata boshi chap past burchak; `site/maydon.js` dagi chizma va `missions.py` dagi koordinatalar BIRGA o'zgarishi kerak.

## Ish oqimi (nima o'zgarsa nima qilinadi)

Buyruqlar `site/` papkasidan turib bajariladi (repo ildizi):

```
Dars kontenti o'zgardi        -> python curriculum/generate_lessons.py
Yangi model / yangi sinf      -> python curriculum/build_instructions.py --yil 1-yil --sinf 2-sinf
Hammasini tekshirish          -> python curriculum/build_instructions.py --all --dry-run
Excel                         -> cd curriculum && python build_xlsx.py
                                 (build_xlsx.py qo'shni modullarni to'g'ridan-to'g'ri import
                                  qiladi, shuning uchun AYNAN shu papkadan ishga tushiriladi)
Deploy                        -> site/ da commit + push, keyin serverda:
                                 cd /opt/robbit-academy && git pull
```

## Git holati
- Repo = **`site/` papkasining o'zi** (repo ildizi = veb ildizi). `https://github.com/ilkhomjon2001/maktab-uchun-.git`, branch `master`.
- **`curriculum/` endi shu reponing ichida** (2026-08-08 da `project_bundle/curriculum` dan `site/curriculum` ga ko'chirildi). Generatorlar ham zaxiralanadi.
- ⚠️ Repo ildizi = veb ildizi, shuning uchun repodagi HAR QANDAY fayl internetdan
  yuklab olinadi. `.py` va `.md` fayllar saytga kerak emas — nginx'da yopilsin:
  ```
  location ^~ /curriculum/ { deny all; return 404; }
  location ~* \.(md|py)$   { deny all; return 404; }
  ```
  `CLAUDE.md` da server IP, `/opt` yo'llari va ichki qarorlar bor — bu qoida ayniqsa
  o'sha fayl uchun kerak.
- Serverda `/opt/robbit-academy` — shu reponing `--depth 1` ishchi nusxasi. Eski fayllar `/opt/robbit-academy.bak-20260808` da.
- Git 2.55 o'rnatilgan (`D:\Git\cmd\git.exe`). Repo ichida identity sozlangan:
  `Robbit Admin <teamlead.robbit@gmail.com>` (oldingi commitlar bilan bir xil).

## Ish muhiti (2026-08-08 da o'rnatildi)
- **Python 3.13.15** — `%LOCALAPPDATA%\Programs\Python\Python313\python.exe`, PATH ga qo'shilgan
  (yangi terminal ochilgandan keyin oddiy `python` ishlaydi).
- **Kutubxonalar:** `openpyxl` 3.1.5 (Excel), `Pillow` 12.3.0 (rasm qirqish/WebP).
  Boshqa tashqi bog'liqlik YO'Q — qolgan hamma narsa stdlib.

## KEYINGI QADAMLAR (aniqlanmagan / qaror kutmoqda)

1. **Missiya vaqt me'yorlari** (35/35/40/40 s) sinovda tekshirilishi kerak.
   Sinovdan keyin `missions.py` dagi raqamlar va ball taqsimoti moslashtiriladi.
2. **Serverda nginx qoidasi qo'shilib, `git pull` qilinishi kerak** (yuqoridagi "Git holati").

**Hosting bo'yicha qaror:** sayt faqat o'z serverimizda (169.58.130.201:8081) turadi.
Vercel/GitHub Pages kabi tashqi hosting KERAK EMAS — bu masala yopilgan.

**SPIKE model nomlari bo'yicha qaror (2026-08-08):** norasmiy/o'zbekcha nomlar QOLADI
(StarterBot, Ultrasonic sensor mount, Bumper, Tractor, Catapult, Scoop, Ball Shooter,
Kriket, Sensor arm). Rasmiy LEGO nomiga o'zgartirilmaydi — havolalar eng yaqin rasmiy
modelga ishora qilib turaveradi. Bu masala YOPILGAN.

## Foydalanuvchi haqida
Ikrom — Robbit Academy'da o'qituvchi tayyorlash, kurikulum va platforma ishlari bilan shug'ullanadi, robototexnika bo'yicha metodist sifatida ham ishlaydi. Windows'da Claude Code bilan ishlaydi, dual-account workflow va CLAUDE.md orqali kontekst uzatishga odatlangan (shuning uchun bu fayl unga tanish format). O'zbek tilida so'zlashadi, texnik jihatdan ancha bilimdon (Python, Git, FastAPI, Telegram botlar bilan tajribasi bor).
