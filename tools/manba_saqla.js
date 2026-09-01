/*
 * TOZA NUSXANI YANGILASH
 * ======================
 * Ishga tushirish (repo ildizidan):
 *     node tools/manba_saqla.js
 *
 * Ildizdagi tree_data.js va sample_lessons.js ni tools/manba/ ga ko'chiradi.
 * Bu — qatlamlar QO'YILMAGAN toza manba; qayta_qur.js aynan shundan o'qiydi.
 *
 * QACHON ISHLATILADI
 *   Faqat curriculum/ dagi Python generatori qayta ishga tushib, ildizdagi
 *   fayllarni YANGIDAN yozganda. Ketma-ketlik:
 *       python curriculum/generate_lessons.py   (yoki tegishli skript)
 *       node tools/manba_saqla.js
 *       node tools/qayta_qur.js
 *
 * XAVFSIZLIK
 *   Ildizdagi fayl allaqachon qayta_qur.js tomonidan yozilgan bo'lsa
 *   (sarlavhasida ogohlantirish bor), ko'chirish TO'XTATILADI — aks holda
 *   qayta ishlangan ma'lumot "toza manba" bo'lib qolib, qatlamlar ikki
 *   marta qo'yilardi.
 */

const fs = require('fs');
const path = require('path');

const ILDIZ = path.join(__dirname, '..');
const MANBA = path.join(__dirname, 'manba');
const FAYLLAR = ['tree_data.js', 'sample_lessons.js'];

const BELGI = 'qayta_qur.js';

fs.mkdirSync(MANBA, { recursive: true });

let xato = false;
for (const f of FAYLLAR) {
  const p = path.join(ILDIZ, f);
  if (!fs.existsSync(p)) {
    console.error('XATO: ' + f + ' topilmadi.');
    xato = true; continue;
  }
  const bosh = fs.readFileSync(p, 'utf8').slice(0, 600);
  if (bosh.indexOf(BELGI) !== -1) {
    console.error('XATO: ' + f + ' allaqachon qayta ishlangan (sarlavhasida "' +
                  BELGI + '" bor).');
    console.error('  Toza manba sifatida saqlash mumkin emas — qatlamlar ikki');
    console.error('  marta qo\'yilib ketardi. Avval Python generatorini');
    console.error('  ishga tushiring yoki git orqali asl faylni tiklang.');
    xato = true;
  }
}
if (xato) process.exit(1);

for (const f of FAYLLAR) {
  fs.copyFileSync(path.join(ILDIZ, f), path.join(MANBA, f));
  const kb = (fs.statSync(path.join(MANBA, f)).size / 1024).toFixed(0);
  console.log('  saqlandi: tools/manba/' + f.padEnd(20) + kb.padStart(7) + ' KB');
}
console.log('\nEndi: node tools/qayta_qur.js');
