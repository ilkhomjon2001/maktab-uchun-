/*
 * ROBOTOTEXNIKA 0-4 QAYTA QURISH (asosiy Tarbion sayti)
 * =====================================================
 * Ishga tushirish (repo ildizidan):
 *     node tools/qayta_qur.js
 *
 * NIMA QILADI
 *   tools/manba/ dagi TOZA nusxadan o'qiydi, robototexnika fanining
 *   0-4-sinf darslariga to'rtta qatlamni qo'yadi va ildizdagi
 *   tree_data.js + sample_lessons.js fayllarini qayta yozadi.
 *
 *   Qatlamlar (hammasi tools/ da, 0-4 platformasi bilan bir xil):
 *     reja.js      - qaysi sinf qaysi dasturdan (Makerzoid / SPIKE)
 *     taqsimot.js  - modellarni sinflar bo'yicha TAKRORSIZ bo'lish
 *                    (1-yil yoyilgan, 2-yil siqilgan doimiy variant)
 *     nazorat.js   - har sinf-yil uchun alohida chorak nazorat ishi
 *     loyiha.js    - har sinf-yil uchun alohida chorak loyihasi
 *
 * NIMAGA TEGMAYDI
 *   5-8-sinf (elektronika / Arduino / ESP32 / AI) - bir bayt ham
 *   o'zgarmaydi, tekshiriladi va tasdiqlanadi.
 *   Boshqa 18 fan, app.js, index.html, instructions/ - tegilmaydi.
 *
 * NEGA NODE, PYTHON EMAS
 *   curriculum/ dagi Python konveyeri bu mashinada ishga tushmaydi
 *   (Python o'rnatilmagan). Shuning uchun tuzatish Python manbasini
 *   o'zgartirish o'rniga USTIGA QO'YILADIGAN qatlam sifatida yozilgan.
 *
 * PYTHON GENERATOR QAYTA ISHLASA
 *   1) node tools/manba_saqla.js   - yangi chiqishni toza nusxa qilib oladi
 *   2) node tools/qayta_qur.js     - qatlamlarni qaytadan qo'yadi
 */

const fs = require('fs');
const path = require('path');

const ILDIZ = path.join(__dirname, '..');
const MANBA = path.join(__dirname, 'manba');

const REJA = require('./reja.js');
const TAQ  = require('./taqsimot.js');
const NAZ  = require('./nazorat.js');
const LOY  = require('./loyiha.js');

// Shu skript faqat robototexnikaning boshlang'ich sinflariga tegadi.
const SINFLAR = ['0-sinf', '1-sinf', '2-sinf', '3-sinf', '4-sinf'];

// ------------------------------------------------------------- manbani o'qish

function manbaOqi(fayl) {
  const p = path.join(MANBA, fayl);
  if (!fs.existsSync(p)) {
    console.error('XATO: toza nusxa topilmadi -> ' + p);
    console.error('Avval `node tools/manba_saqla.js` ni ishga tushiring.');
    process.exit(1);
  }
  return p;
}

global.window = {};
require(manbaOqi('tree_data.js'));
require(manbaOqi('sample_lessons.js'));
require(path.join(ILDIZ, 'instructions_index.js'));

const TREE_MANBA    = global.window.TREE_DATA;
const LESSONS_MANBA = global.window.LESSON_CONTENT;
const IX            = global.window.INSTRUCTION_INDEX;

function nusxa(o) { return JSON.parse(JSON.stringify(o)); }

// Natija — manbaning to'liq nusxasi; faqat 0-4 qismi almashtiriladi.
const tree    = nusxa(TREE_MANBA);
const lessons = nusxa(LESSONS_MANBA);

const stat = { almashgan: 0, tegilmagan: 0, nazorat: 0, loyiha: 0, kirish: 0 };
const taqsimotStat = {};

// ------------------------------------------------------ Makerzoid dars hovuzi

function hovuzYig() {
  const h = [];
  const yil = TAQ.manbaYil;
  for (const sinf of SINFLAR) {
    const sd = TREE_MANBA[yil] && TREE_MANBA[yil][sinf];
    if (!sd) continue;
    for (const chorak of Object.keys(sd)) {
      sd[chorak].forEach((l, idx) => {
        if (!l.model) return;
        const ct = LESSONS_MANBA[[yil, sinf, chorak, idx].join('|')];
        if (!ct) return;
        h.push({
          dars: l, kontent: ct, model: l.model, mavzu: l.title,
          qism: TAQ.kichikMavzu(ct, l.title),
          qadam: IX[l.model] ? IX[l.model].qadam : 0
        });
      });
    }
  }
  return h;
}

const HOVUZ = hovuzYig();

const BIR_YIL_KETMA = SINFLAR.reduce((a, s) => a.concat(
  TAQ.tartibla(HOVUZ, TAQ.TAQSIMOT[s].mavzular)
     .map(x => Object.assign({}, x, { yangiSinf: s }))), []);

let IKKI_YIL = null;
try {
  IKKI_YIL = TAQ.ikkinchiYil(BIR_YIL_KETMA, m => (IX[m] ? IX[m].qadam : 0));
} catch (e) {
  console.error('XATO: 2-yil taqsimoti qurilmadi — ' + e.message);
  process.exit(1);
}

// ------------------------------------------------------------ sinfni qayta qurish

function makerzoidQur(yil, sinf, sinfData) {
  const belgi = TAQ.belgi(yil, sinf);
  const ikkinchiMi = !!(IKKI_YIL[sinf] && yil === '2-yil');
  const tanlangan = ikkinchiMi
    ? IKKI_YIL[sinf]
    : TAQ.tartibla(HOVUZ, TAQ.TAQSIMOT[sinf].mavzular);

  if (tanlangan.length !== TAQ.MODELLI * 4) {
    console.error('XATO: ' + yil + ' ' + sinf + ' uchun taqsimot ' +
      tanlangan.length + ' dars berdi, kerak ' + (TAQ.MODELLI * 4));
    process.exit(1);
  }

  const korilgan = {};
  const almashStat = { sinov: 0, takomil: 0 };
  const yangiSinf = {};
  const choraklar = Object.keys(sinfData);
  let oqim = 0;

  choraklar.forEach((chorak, ci) => {
    const asl = sinfData[chorak];

    // Yashirin "(Dasturlash)" choraklari o'zgarishsiz o'tadi
    if (/\(Dasturlash\)/.test(chorak)) {
      yangiSinf[chorak] = nusxa(asl);
      return;
    }

    const chorakNo = ci + 1;
    const modul = belgi.modullar[ci] || belgi.modullar[belgi.modullar.length - 1];

    const tuzilma = [];
    asl.forEach((l, idx) => { if (!l.model) tuzilma.push({ dars: l, idx }); });
    const kirish  = tuzilma.find(t => t.dars.type === 'qurish');
    const nazorat = tuzilma.find(t => t.dars.type === 'nazorat');
    const loyiha  = tuzilma.find(t => t.dars.type === 'loyiha');

    const tuzilmaQoy = (t, almash) => {
      if (!t) return null;
      const d = nusxa(t.dars);
      let kt = LESSONS_MANBA[[yil, sinf, chorak, t.idx].join('|')] || null;
      if (almash) {
        d.title = almash.nom;
        kt = kt ? nusxa(kt) : {};
        for (const m of Object.keys(almash.kontent)) kt[m] = almash.kontent[m];
      }
      return { dars: d, kontent: kt };
    };

    const kirAlmash = TAQ.kirishDarsi(yil, sinf, chorakNo);
    const kirishB = tuzilmaQoy(kirish, kirAlmash);
    if (kirAlmash) stat.kirish++;

    const qurishlar = [];
    for (let k = 0; k < TAQ.MODELLI; k++) {
      const x = tanlangan[oqim++];
      const kalit = x.model + '|' + x.qism;
      korilgan[kalit] = (korilgan[kalit] || 0) + 1;
      const almash = TAQ.almashtir(x.kontent, x.model, x.qism, korilgan[kalit]);

      const d = nusxa(x.dars);
      d.title = almash ? almash.nom : x.qism;
      if (almash) {
        if (korilgan[kalit] === 2) almashStat.sinov++; else almashStat.takomil++;
      }
      const kt = nusxa(x.kontent);
      if (almash) for (const m of Object.keys(almash.kontent)) kt[m] = almash.kontent[m];
      qurishlar.push({ dars: d, kontent: kt });
    }

    const nazAlmash = NAZ.nazoratDarsi(yil, sinf, chorakNo);
    if (nazorat && !nazAlmash) {
      console.error('XATO: ' + yil + ' ' + sinf + ' ' + chorakNo +
                    '-chorak uchun nazorat testi tools/nazorat.js da yo\'q.');
      process.exit(1);
    }
    const nazB = tuzilmaQoy(nazorat, nazAlmash);
    if (nazAlmash) stat.nazorat++;

    const loyAlmash = LOY.loyihaDarsi(yil, sinf, chorakNo);
    if (loyiha && !loyAlmash) {
      console.error('XATO: ' + yil + ' ' + sinf + ' ' + chorakNo +
                    '-chorak uchun loyiha tools/loyiha.js da yo\'q.');
      process.exit(1);
    }
    const loyB = tuzilmaQoy(loyiha, loyAlmash);
    if (loyAlmash) stat.loyiha++;

    // Chorak tartibi (2026-09-01 dan): baho chorak oxirida emas, HAR OYda —
    //   1-dars kirish, 9-dars NAZARIY TEST (1-oy bahosi),
    //   18-dars AMALIY LOYIHA-IMTIHON (2-oy bahosi), qolgani qurish.
    const bolak = [kirishB]
      .concat(qurishlar.slice(0, 7), [nazB],
              qurishlar.slice(7, 15), [loyB],
              qurishlar.slice(15))
      .filter(Boolean);

    const royxat = [];
    bolak.forEach((b, idx) => {
      royxat.push(b.dars);
      const key = [yil, sinf, chorak, idx].join('|');
      if (b.kontent) {
        const kt = nusxa(b.kontent);
        if (kt.meta) {
          kt.meta.sinf = sinf;
          kt.meta.yil = yil;
          kt.meta.chorak = TAQ.haftaMatni(chorakNo, idx);
          kt.meta.darsRaqami = TAQ.darsRaqami(chorakNo, idx);
          if (b.dars.model) kt.meta.modul = modul;
        }
        lessons[key] = kt;
      }
      stat.almashgan++;
    });
    yangiSinf[chorak] = royxat;
  });

  taqsimotStat[yil + '|' + sinf] = {
    yonalish: belgi.yonalish,
    siqilgan: ikkinchiMi,
    model: new Set(tanlangan.map(x => x.model)).size,
    sinov: almashStat.sinov,
    takomil: almashStat.takomil
  };
  return yangiSinf;
}

// ------------------------------------------------------------------ asosiy sikl

const qollanganReja = [];

for (const yil of Object.keys(TREE_MANBA)) {
  for (const sinf of Object.keys(TREE_MANBA[yil])) {
    if (SINFLAR.indexOf(sinf) === -1) {         // 5-8-sinf — tegilmaydi
      let n = 0;
      for (const ch of Object.keys(TREE_MANBA[yil][sinf])) n += TREE_MANBA[yil][sinf][ch].length;
      stat.tegilmagan += n;
      continue;
    }

    const rejaKalit = yil + '|' + sinf;
    const almash = REJA[rejaKalit];
    const [mYil, mSinf] = (almash && almash.manba)
      ? almash.manba.split('|') : [yil, sinf];

    const sinfData = TREE_MANBA[mYil] && TREE_MANBA[mYil][mSinf];
    if (!sinfData) {
      console.error('XATO: reja manbasi topilmadi -> ' + almash.manba);
      process.exit(1);
    }
    if (almash) qollanganReja.push({ kalit: rejaKalit, ...almash });

    // SPIKE sinflari: manbadan nusxa olinadi, taqsimot qo'llanmaydi
    if (almash && almash.dastur === 'SPIKE') {
      let QOP = null;
      if (almash.qoplama) {
        try { QOP = require('./' + almash.qoplama + '.js'); }
        catch (e) {
          console.error('XATO: qoplama yuklanmadi -> tools/' + almash.qoplama +
                        '.js\n  ' + e.message);
          process.exit(1);
        }
      }
      const yangi = {};
      Object.keys(sinfData).forEach((chorak, ci) => {
        // Yashirin "(Dasturlash)" choraklari o'zgarishsiz o'tadi
        if (/\(Dasturlash\)/.test(chorak)) {
          yangi[chorak] = nusxa(sinfData[chorak]);
          sinfData[chorak].forEach((l, idx) => {
            const ct = LESSONS_MANBA[[mYil, mSinf, chorak, idx].join('|')];
            if (!ct) return;
            const kt = nusxa(ct);
            if (kt.meta) { kt.meta.sinf = sinf; kt.meta.yil = yil; }
            lessons[[yil, sinf, chorak, idx].join('|')] = kt;
            stat.almashgan++;
          });
          return;
        }

        const chorakNo = ci + 1;

        // Manbadan nusxa: dars + kontent + qoplama (eski indeks bo'yicha)
        const royxat = sinfData[chorak].map((l, idx) => {
          let kt = LESSONS_MANBA[[mYil, mSinf, chorak, idx].join('|')] || null;
          if (kt) {
            kt = nusxa(kt);
            const ustama = QOP && QOP.darslar && QOP.darslar[chorak + '|' + idx];
            if (ustama) for (const m of Object.keys(ustama)) kt[m] = ustama[m];
          }
          return { dars: nusxa(l), kontent: kt };
        });

        // Nazorat -> 9-dars (test), loyiha -> 18-dars (check-listli imtihon).
        // Yangi kontent nazorat.js / loyiha.js dan olinadi (SPIKE to'plamlari).
        const naz = royxat.find(b => b.dars.type === 'nazorat');
        const loy = royxat.find(b => b.dars.type === 'loyiha');
        const qolgan = royxat.filter(b => b !== naz && b !== loy);

        const almashQoy = (b, almash) => {
          if (!b || !almash) return;
          b.dars.title = almash.nom;
          b.kontent = b.kontent ? b.kontent : {};
          for (const m of Object.keys(almash.kontent)) b.kontent[m] = almash.kontent[m];
        };
        const nazAlmash = NAZ.nazoratDarsi(yil, sinf, chorakNo);
        if (naz && !nazAlmash) {
          console.error('XATO: ' + yil + ' ' + sinf + ' ' + chorakNo +
                        '-chorak (SPIKE) uchun test tools/nazorat.js da yo\'q.');
          process.exit(1);
        }
        almashQoy(naz, nazAlmash);
        if (naz && nazAlmash) stat.nazorat++;

        const loyAlmash = LOY.loyihaDarsi(yil, sinf, chorakNo);
        if (loy && !loyAlmash) {
          console.error('XATO: ' + yil + ' ' + sinf + ' ' + chorakNo +
                        '-chorak (SPIKE) uchun loyiha tools/loyiha.js da yo\'q.');
          process.exit(1);
        }
        almashQoy(loy, loyAlmash);
        if (loy && loyAlmash) stat.loyiha++;

        const tartib = [].concat(
          qolgan.slice(0, 8), naz ? [naz] : [],
          qolgan.slice(8, 16), loy ? [loy] : [],
          qolgan.slice(16));

        const chorakRoyxat = [];
        tartib.forEach((b, idx) => {
          chorakRoyxat.push(b.dars);
          if (b.kontent) {
            const kt = b.kontent;
            if (kt.meta) {
              kt.meta.sinf = sinf;
              kt.meta.yil = yil;
              kt.meta.chorak = TAQ.haftaMatni(chorakNo, idx);
              kt.meta.darsRaqami = TAQ.darsRaqami(chorakNo, idx);
            }
            lessons[[yil, sinf, chorak, idx].join('|')] = kt;
            stat.almashgan++;
          }
        });
        yangi[chorak] = chorakRoyxat;
      });
      // eski chorak kalitlari qolmasin
      tree[yil][sinf] = yangi;
      continue;
    }

    tree[yil][sinf] = makerzoidQur(yil, sinf, TREE_MANBA[yil][sinf]);
  }
}

// Daraxtdan chiqib ketgan dars kalitlari tozalanadi (masalan SPIKE ga o'tgan
// sinfning eski "Dasturlash" choraklari) — aks holda lessons/ da yetim qoladi.
const boriKalit = new Set();
for (const yil of Object.keys(tree))
  for (const sinf of Object.keys(tree[yil]))
    for (const chorak of Object.keys(tree[yil][sinf]))
      tree[yil][sinf][chorak].forEach((l, i) =>
        boriKalit.add([yil, sinf, chorak, i].join('|')));

let yetim = 0;
for (const k of Object.keys(lessons)) {
  if (!boriKalit.has(k)) { delete lessons[k]; yetim++; }
}

// ---------------------------------------------------------------------- yozish

function yoz(fayl, globalNom, obj, sarlavha) {
  const bosh =
    '/* ' + sarlavha + '\n' +
    ' * DIQQAT: 0-4-sinf robototexnika qismi `node tools/qayta_qur.js` bilan\n' +
    ' * qayta yaratiladi. Qo\'lda tahrirlamang — o\'zgarish tools/ dagi\n' +
    ' * qatlam fayllarida (reja/taqsimot/nazorat/loyiha) yoziladi.\n' +
    ' * 5-8-sinf va boshqa fanlar bu skript tomonidan o\'zgartirilmaydi.\n' +
    ' */\n';
  const p = path.join(ILDIZ, fayl);
  fs.writeFileSync(p, bosh + 'window.' + globalNom + ' = ' +
                   JSON.stringify(obj, null, 1) + ';\n', 'utf8');
  console.log('  ' + fayl.padEnd(22) +
              (fs.statSync(p).size / 1024).toFixed(0).padStart(7) + ' KB');
}

console.log('Manba : ' + MANBA);
console.log('Chiqish: ' + ILDIZ + '\n');
yoz('tree_data.js', 'TREE_DATA', tree, 'Barcha darslarning tuzilishi (sinf/yil/chorak/mavzu/model).');
yoz('sample_lessons.js', 'LESSON_CONTENT', lessons, 'Dars rejalari. Kalit: "yil|sinf|chorak|index".');

// --------------------------------------------------------------------- hisobot

console.log('\nO\'QUV REJASI (robototexnika 0-4)');
qollanganReja.forEach(r =>
  console.log('  ' + r.kalit.replace('|', ' ') +
              (r.manba ? '  <-  ' + r.manba.replace('|', ' ') : '  (o\'z kontenti) ') +
              '  [' + r.dastur + ' · ' + r.uslub + ']'));

console.log('\nMODEL TAQSIMOTI');
for (const [k, s] of Object.entries(taqsimotStat)) {
  console.log('  ' + k.replace('|', ' ').padEnd(14) + String(s.model).padStart(3) +
    ' model  ' + (s.siqilgan ? 'SIQILGAN ' : 'yoyilgan ') +
    'sinov:' + String(s.sinov).padStart(2) + ' takomil:' + String(s.takomil).padStart(2) +
    '   ' + s.yonalish);
}

console.log('\nHISOBOT');
console.log('  Qayta qurilgan dars (0-4)  : ' + stat.almashgan);
console.log('  Tegilmagan dars (5-8)      : ' + stat.tegilmagan);
console.log('  Yangi chorak kirishi       : ' + stat.kirish);
console.log('  Yangi nazorat ishi         : ' + stat.nazorat);
console.log('  Yangi loyiha               : ' + stat.loyiha);
console.log('  Tozalangan yetim dars      : ' + yetim);
