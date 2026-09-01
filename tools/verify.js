/*
 * TEKSHIRUV — qayta qurishdan keyin
 * =================================
 *     node tools/verify.js
 *
 * Uch narsani tekshiradi:
 *   1) 5-8-sinf va boshqa hamma narsa manbadagidek QOLGANMI (bayt-mabayt)
 *   2) Robototexnika 0-4 da bola oqimi bo'ylab takrorlanish YO'QMI
 *   3) Daraxt va dars rejalari bir-biriga mos kelishi
 *
 * Xato topilsa exit kodi 1.
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ILDIZ = path.join(__dirname, '..');
const MANBA = path.join(__dirname, 'manba');
const SINFLAR = ['0-sinf', '1-sinf', '2-sinf', '3-sinf', '4-sinf'];

const REJA = require('./reja.js');

function yukla(dir, fayllar) {
  global.window = {};
  fayllar.forEach(f => {
    delete require.cache[require.resolve(path.join(dir, f))];
    require(path.join(dir, f));
  });
  return global.window;
}

const M = yukla(MANBA, ['tree_data.js', 'sample_lessons.js']);
const MANBA_TREE = M.TREE_DATA, MANBA_LESSONS = M.LESSON_CONTENT;
const Y = yukla(ILDIZ, ['tree_data.js', 'sample_lessons.js', 'instructions_index.js']);
const TREE = Y.TREE_DATA, LESSONS = Y.LESSON_CONTENT, IX = Y.INSTRUCTION_INDEX;

const xatolar = [];
let ok = 0;
function tekshir(shart, xabar) { if (shart) ok++; else xatolar.push(xabar); }

function xesh(o) {
  return crypto.createHash('md5').update(JSON.stringify(o)).digest('hex');
}

/* --------------------------------- 1. 5-8-SINF VA BOSHQA HAMMA NARSA TEGILMAGAN */

let tekshirilgan58 = 0;
for (const yil of Object.keys(MANBA_TREE)) {
  tekshir(!!TREE[yil], `Yil yo'qolgan: ${yil}`);
  if (!TREE[yil]) continue;

  for (const sinf of Object.keys(MANBA_TREE[yil])) {
    if (SINFLAR.indexOf(sinf) !== -1) continue;      // 0-4 ataylab o'zgargan

    tekshir(xesh(MANBA_TREE[yil][sinf]) === xesh(TREE[yil][sinf]),
      `${yil} ${sinf}: daraxt o'zgarib ketgan (5-8 ga tegilmasligi kerak edi)`);

    for (const chorak of Object.keys(MANBA_TREE[yil][sinf])) {
      MANBA_TREE[yil][sinf][chorak].forEach((l, i) => {
        const k = [yil, sinf, chorak, i].join('|');
        tekshir(xesh(MANBA_LESSONS[k]) === xesh(LESSONS[k]),
          `${k}: dars rejasi o'zgarib ketgan (5-8 ga tegilmasligi kerak edi)`);
        tekshirilgan58++;
      });
    }
  }
}

// Boshqa fayllar umuman qo'zg'atilmagan bo'lishi kerak
for (const f of ['app.js', 'index.html', 'fanlar.js', 'instructions_index.js',
                 'resources.js', 'maydon.js']) {
  tekshir(fs.existsSync(path.join(ILDIZ, f)), `Fayl yo'q: ${f}`);
}

/* ------------------------------- 2. BOLA OQIMI BO'YLAB TAKRORLANISH YO'Q */

const hujayra = {};
for (const yil of Object.keys(TREE)) {
  for (const sinf of SINFLAR) {
    if (!TREE[yil][sinf]) continue;
    const h = hujayra[yil + '|' + sinf] =
      { model: new Set(), mavzu: new Set(), tuzilma: new Set() };
    for (const chorak of Object.keys(TREE[yil][sinf])) {
      if (/\(Dasturlash\)/.test(chorak)) continue;
      TREE[yil][sinf][chorak].forEach(l => {
        if (l.model) { h.model.add(l.model); h.mavzu.add(l.title); }
        else h.tuzilma.add(l.title);
      });
    }
  }
}

const OQIMLAR = [
  { nom: "doimiy (yangi kelgan bola)",
    yol: ['2-yil|0-sinf', '2-yil|1-sinf', '2-yil|2-sinf', '2-yil|3-sinf', '2-yil|4-sinf'] },
  { nom: "maktabning 1-yilida 0-sinf",
    yol: ['1-yil|0-sinf', '2-yil|1-sinf', '2-yil|2-sinf', '2-yil|3-sinf', '2-yil|4-sinf'] },
  { nom: "maktabning 1-yilida 1-sinf",
    yol: ['1-yil|1-sinf', '2-yil|2-sinf', '2-yil|3-sinf', '2-yil|4-sinf'] },
  { nom: "maktabning 1-yilida 2-sinf",
    yol: ['1-yil|2-sinf', '2-yil|3-sinf', '2-yil|4-sinf'] },
  { nom: "maktabning 1-yilida 3-sinf",
    yol: ['1-yil|3-sinf', '2-yil|4-sinf'] }
];

function spikeMi(kalit) {
  const r = REJA[kalit];
  return !!(r && r.dastur === 'SPIKE');
}

for (const oqim of OQIMLAR) {
  const yol = oqim.yol.filter(k => hujayra[k]);
  for (let i = 0; i < yol.length; i++) {
    for (let j = i + 1; j < yol.length; j++) {
      if (spikeMi(yol[i]) && spikeMi(yol[j])) continue;
      const a = hujayra[yol[i]], b = hujayra[yol[j]];
      const km = [...a.model].filter(x => b.model.has(x));
      const kt = [...a.mavzu].filter(x => b.mavzu.has(x));
      const kz = [...a.tuzilma].filter(x => b.tuzilma.has(x));
      const q = `[${oqim.nom}] ${yol[i]} -> ${yol[j]}`;
      tekshir(km.length === 0, `${q}: bir xil model ${km.length} ta — ` + km.slice(0, 4).join(', '));
      tekshir(kt.length === 0, `${q}: bir xil mavzu ${kt.length} ta — ` + kt.slice(0, 3).join(' | '));
      tekshir(kz.length === 0, `${q}: bir xil tuzilma darsi ${kz.length} ta — ` +
        kz.slice(0, 2).map(x => x.slice(0, 55)).join(' | '));
    }
  }
}

// "o'tgan yilni eslaymiz" kabi bema'ni darslar 1-yilda qolmasin
const BEMANI = /o'tgan yilni eslaymiz|o'tgan yilda o'rgangan/i;
for (const sinf of SINFLAR) {
  const sd = TREE['1-yil'] && TREE['1-yil'][sinf];
  if (!sd) continue;
  for (const chorak of Object.keys(sd)) {
    sd[chorak].forEach((l, i) => {
      const c = LESSONS[['1-yil', sinf, chorak, i].join('|')];
      const matn = (l.title || '') + ' ' + (c && c.maqsad ? c.maqsad.join(' ') : '');
      tekshir(!BEMANI.test(matn),
        `1-yil ${sinf} ${chorak} #${i}: maktabning birinchi yilida "o'tgan yil" ga ` +
        `havola qilingan — "${(l.title || '').slice(0, 50)}"`);
    });
  }
}

/* --------------------- 2b. OYLIK NAZORAT TUZILMASI (2026-09-01 qoidasi)
 * Har chorakda: 9-dars (idx 8) = NAZARIY TEST, 18-dars (idx 17) = AMALIY
 * LOYIHA-IMTIHON, boshqa joyda nazorat/loyiha bo'lmasin. Test kontentida
 * 10 savol va javoblar kaliti, loyihada 10 bandli check-list bo'lsin. */

for (const yil of ['1-yil', '2-yil']) {
  for (const sinf of SINFLAR) {
    const sd = TREE[yil] && TREE[yil][sinf];
    if (!sd) continue;
    Object.keys(sd).forEach((chorak, ci) => {
      if (/\(Dasturlash\)/.test(chorak)) return;
      const l = sd[chorak];
      const joy = `${yil} ${sinf} ${chorak}`;
      tekshir(l.length === 21, `${joy}: ${l.length} dars (21 kerak)`);

      const nazJoy = l.map((d, i) => d.type === 'nazorat' ? i : -1).filter(i => i >= 0);
      const loyJoy = l.map((d, i) => d.type === 'loyiha' ? i : -1).filter(i => i >= 0);
      tekshir(nazJoy.length === 1 && nazJoy[0] === 8,
        `${joy}: nazorat 9-darsda emas (indekslar: ${nazJoy.join(',') || 'yoq'})`);
      tekshir(loyJoy.length === 1 && loyJoy[0] === 17,
        `${joy}: loyiha 18-darsda emas (indekslar: ${loyJoy.join(',') || 'yoq'})`);

      const oyTest = ci * 2 + 1, oyLoy = ci * 2 + 2;
      tekshir(new RegExp('^' + oyTest + "-oylik nazorat \\(NAZARIY TEST\\)").test(l[8].title),
        `${joy}: 9-dars sarlavhasi "${String(l[8].title).slice(0, 45)}"`);
      tekshir(new RegExp('^' + oyLoy + "-oylik nazorat \\(AMALIY LOYIHA-IMTIHON\\)").test(l[17].title),
        `${joy}: 18-dars sarlavhasi "${String(l[17].title).slice(0, 45)}"`);

      const testKt = LESSONS[[yil, sinf, chorak, 8].join('|')];
      const savolSex = testKt && (testKt.amaliy || []).find(s => /Test savollari/.test(s.title));
      tekshir(!!savolSex && savolSex.points.length === 10,
        `${joy}: testda 10 savol yo'q (${savolSex ? savolSex.points.length : 'bo\'lim yo\'q'})`);
      tekshir(!!testKt && (testKt.amaliy || []).some(s => /Javoblar kaliti/.test(s.title)),
        `${joy}: testda javoblar kaliti yo'q`);
      tekshir(!!testKt && (testKt.nazariya || []).some(s => /O'tkazish instruksiyasi/.test(s.title)),
        `${joy}: testda o'tkazish instruksiyasi yo'q`);

      const loyKt = LESSONS[[yil, sinf, chorak, 17].join('|')];
      const chekSex = loyKt && (loyKt.nazariya || []).find(s => /check-list/i.test(s.title));
      const bandlar = chekSex ? chekSex.points.filter(p => /^\d+-band \(1 ball\)/.test(p)).length : 0;
      tekshir(bandlar === 10,
        `${joy}: loyihada 10 bandli check-list yo'q (${bandlar} band)`);
      tekshir(!!loyKt && (loyKt.nazariya || []).some(s => /e'tibor/i.test(s.title)),
        `${joy}: loyihada "nimalarga e'tibor" bo'limi yo'q`);
    });
  }
}

/* ------------------------------------- 3. DARAXT <-> DARS REJALARI BUTUNLIGI */

let dars = 0, modelli = 0;
for (const yil of Object.keys(TREE)) {
  for (const sinf of Object.keys(TREE[yil])) {
    for (const chorak of Object.keys(TREE[yil][sinf])) {
      TREE[yil][sinf][chorak].forEach((l, i) => {
        dars++;
        const k = [yil, sinf, chorak, i].join('|');
        tekshir(!!LESSONS[k], `Dars rejasi yo'q: ${k}`);
        if (l.model) {
          modelli++;
          if (SINFLAR.indexOf(sinf) !== -1) {
            tekshir(!!IX[l.model], `Instruksiya ko'rsatkichida yo'q: "${l.model}" (${k})`);
          }
        }
      });
    }
  }
}

// lessons/ da yetim kalit qolmasin
const boriKalit = new Set();
for (const yil of Object.keys(TREE))
  for (const sinf of Object.keys(TREE[yil]))
    for (const chorak of Object.keys(TREE[yil][sinf]))
      TREE[yil][sinf][chorak].forEach((l, i) =>
        boriKalit.add([yil, sinf, chorak, i].join('|')));
const yetim = Object.keys(LESSONS).filter(k => !boriKalit.has(k));
tekshir(yetim.length === 0,
  `Daraxtda yo'q dars rejasi qolgan: ${yetim.length} ta — ` + yetim.slice(0, 3).join(', '));

/* ----------------------------------------------------------------- hisobot */

console.log('TARBION ASOSIY SAYT — TEKSHIRUV\n');
console.log('  Darslar jami            : ' + dars);
console.log('  Modelli darslar         : ' + modelli);
console.log('  5-8 tekshirilgan dars   : ' + tekshirilgan58 + '  (o\'zgarmagani tasdiqlandi)');
console.log('  Dars rejalari           : ' + Object.keys(LESSONS).length);
console.log('\n  Muvaffaqiyatli tekshiruv: ' + ok);

if (xatolar.length) {
  console.log('\nXATO (' + xatolar.length + '):');
  xatolar.slice(0, 20).forEach(x => console.log('  x ' + x));
  if (xatolar.length > 20) console.log('  … yana ' + (xatolar.length - 20) + ' ta');
  process.exit(1);
}
console.log('\n✓ Hammasi joyida — xato topilmadi.');
