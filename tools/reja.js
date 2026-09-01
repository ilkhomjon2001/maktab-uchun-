/*
 * 0–4 O'QUV REJASI — qaysi sinf qaysi dasturdan va qaysi uslubda o'qiydi
 * =====================================================================
 * Standart holat: har bir sinf-yil asosiy bazadagi O'Z darslarini oladi.
 * Quyidagi jadval ISTISNOLARNI belgilaydi.
 *
 * Maydonlar:
 *   manba    — boshqa sinf-yilning butun dasturini oladi ("<yil>|<sinf>").
 *              Dars rejalari nusxa olinadi, meta.sinf/meta.yil moslanadi.
 *   dastur   — to'plam nomi (interfeysda belgi sifatida chiqadi)
 *   uslub    — dasturlash uslubi: "blokli" yoki "matnli"
 *   qoplama  — dars kontentiga qo'yiladigan qoplama moduli (tools/ ichida).
 *              Qoplama faqat ko'rsatilgan darslarni va faqat ko'rsatilgan
 *              maydonlarni almashtiradi.
 *
 * QAROR (2026-09-01, foydalanuvchi bilan kelishilgan):
 *   0–2-sinf : Makerzoid — o'zgarishsiz, ikkala yilda ham
 *   3–4-sinf : 2-yilda SPIKE dasturi
 *   1-yil    : butunlay Makerzoid (bolalar birinchi yil konstruktordan boshlaydi)
 *
 * QAROR (2026-09-01, ikkinchi bosqich):
 *   3-sinf va 4-sinf BIR XIL robotlarni quradi, lekin DASTURLASH USLUBI
 *   boshqacha — shu tufayli takrorlanish yo'qoladi:
 *     3-sinf -> BLOKLI dasturlash (SPIKE ilovasidagi bloklar)
 *     4-sinf -> MATNLI dasturlash (Python, SPIKE App 3 API)
 *
 * Natijada:
 *           1-yil        2-yil
 *   0-sinf  Makerzoid    Makerzoid
 *   1-sinf  Makerzoid    Makerzoid
 *   2-sinf  Makerzoid    Makerzoid
 *   3-sinf  Makerzoid    SPIKE · blokli
 *   4-sinf  Makerzoid    SPIKE · matnli (Python)
 *
 * ⚠️ Bu fayl `data/` ni QO'LDA tahrirlashning o'rnini bosadi. `extract.js`
 * har ishga tushganda `data/` ni boshidan yozadi, shuning uchun o'quv reja
 * o'zgarishi AYNAN shu yerda (yoki qoplama modulida) yozilishi kerak.
 */

module.exports = {
  '2-yil|3-sinf': {
    manba: '2-yil|4-sinf',
    dastur: 'SPIKE',
    uslub: 'blokli',
    izoh: "Manba kontenti allaqachon blok atamalarida yozilgan — qoplama kerak emas"
  },

  '2-yil|4-sinf': {
    dastur: 'SPIKE',
    uslub: 'matnli',
    qoplama: 'qoplama_python',
    izoh: "Bir xil robotlar, lekin Python (SPIKE App 3) da matnli kod yoziladi"
  }
};
