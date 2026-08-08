/*
 * Musobaqa maydonchasi chizmalari (SPIKE Prime missiyalari, 2-yil 4-sinf).
 *
 * Maydoncha: 200 x 100 sm. Koordinata boshi (0,0) — CHAP PAST burchak.
 * SVG viewBox "0 0 240 140": maydon x 20..220, y 20..120 oralig'ida.
 * Aylantirish:  svgX = 20 + fx      svgY = 120 - fy
 * Ya'ni 1 SVG birligi = 1 sm, shuning uchun chizmadan to'g'ridan-to'g'ri o'lchab bo'ladi.
 *
 * Manba ma'lumot: curriculum/missions.py (MISSIONS[n]["elementlar"]).
 * Chizma o'zgarsa — missions.py dagi koordinatalar ham o'zgarishi kerak.
 */
(function () {
  // Yorug' tema palitrasi — index.html dagi :root o'zgaruvchilariga mos.
  var C = {
    bg: '#ffffff',
    field: '#f3f7f3',
    border: '#bed0c1',
    grid: 'rgba(21,104,60,0.14)',
    cyan: '#15683C',   // asosiy urg'u — brend yashili
    amber: '#9a6410',
    green: '#17804a',
    red: '#c0392b',
    blue: '#0b6b8f',
    purple: '#6b3fa0',
    text: '#16261b',
    dim: '#5c6d62'
  };

  // Maydon koordinatasidan (sm) SVG koordinatasiga
  function X(v) { return 20 + v; }
  function Y(v) { return 120 - v; }

  function grid() {
    var s = '';
    for (var x = 0; x <= 200; x += 20) {
      s += '<line x1="' + X(x) + '" y1="' + Y(0) + '" x2="' + X(x) + '" y2="' + Y(100) +
           '" stroke="' + C.grid + '" stroke-width="0.4"/>';
    }
    for (var y = 0; y <= 100; y += 20) {
      s += '<line x1="' + X(0) + '" y1="' + Y(y) + '" x2="' + X(200) + '" y2="' + Y(y) +
           '" stroke="' + C.grid + '" stroke-width="0.4"/>';
    }
    return s;
  }

  function rulers() {
    var s = '';
    for (var x = 0; x <= 200; x += 40) {
      s += '<text x="' + X(x) + '" y="' + (Y(0) + 11) + '" fill="' + C.dim +
           '" font-size="6" text-anchor="middle" font-family="monospace">' + x + '</text>';
    }
    for (var y = 0; y <= 100; y += 20) {
      s += '<text x="' + (X(0) - 5) + '" y="' + (Y(y) + 2) + '" fill="' + C.dim +
           '" font-size="6" text-anchor="end" font-family="monospace">' + y + '</text>';
    }
    s += '<text x="' + X(100) + '" y="' + (Y(0) + 19) + '" fill="' + C.dim +
         '" font-size="6" text-anchor="middle" font-family="monospace">200 sm</text>';
    return s;
  }

  // Baza yorliqlari QUTINING YUQORI qismida turadi, chunki robot yo'llari
  // odatda y=20 sm balandlikda bazadan chiqadi va pastki qismni band qiladi.
  function base() {
    return '<rect x="' + X(0) + '" y="' + Y(40) + '" width="40" height="40" ' +
           'fill="rgba(21,104,60,0.10)" stroke="' + C.cyan + '" stroke-width="0.9" stroke-dasharray="3 2"/>' +
           '<text x="' + X(20) + '" y="' + Y(32) + '" fill="' + C.cyan +
           '" font-size="7" text-anchor="middle" font-weight="600">BAZA</text>' +
           '<text x="' + X(20) + '" y="' + Y(26) + '" fill="' + C.dim +
           '" font-size="5" text-anchor="middle" font-family="monospace">40x40</text>';
  }

  function frame(title, subtitle) {
    return '<rect x="0" y="0" width="240" height="140" fill="' + C.bg + '" rx="4"/>' +
           '<rect x="' + X(0) + '" y="' + Y(100) + '" width="200" height="100" fill="' + C.field +
           '" stroke="' + C.border + '" stroke-width="1.2"/>' +
           grid() + rulers() +
           '<text x="12" y="9" fill="' + C.text + '" font-size="8" font-weight="700">' + title + '</text>' +
           // viewBox eni 240 — izoh matni 70 belgidan uzun bo'lsa kesiladi.
           '<text x="12" y="17" fill="' + C.dim + '" font-size="5" font-family="monospace">' +
           subtitle + '</text>';
  }

  // Yo'l (robot harakati) — nuqtalar ro'yxati maydon koordinatasida
  function path(pts, color, dash) {
    var d = pts.map(function (p, i) { return (i ? 'L' : 'M') + X(p[0]) + ' ' + Y(p[1]); }).join(' ');
    return '<path d="' + d + '" fill="none" stroke="' + color + '" stroke-width="1.1" ' +
           'stroke-dasharray="' + (dash || '4 2.5') + '" marker-end="url(#arw)" opacity="0.85"/>';
  }

  function defs() {
    return '<defs><marker id="arw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" ' +
           'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="' + C.amber + '"/></marker></defs>';
  }

  function box(fx, fy, w, h, fill, stroke, label, labelColor) {
    var s = '<rect x="' + X(fx - w / 2) + '" y="' + Y(fy + h / 2) + '" width="' + w + '" height="' + h +
            '" fill="' + fill + '" stroke="' + stroke + '" stroke-width="0.9"/>';
    if (label) {
      s += '<text x="' + X(fx) + '" y="' + (Y(fy + h / 2) - 3) + '" fill="' + (labelColor || stroke) +
           '" font-size="6" text-anchor="middle" font-weight="600">' + label + '</text>';
    }
    return s;
  }

  function dot(fx, fy, r, color, label) {
    var s = '<circle cx="' + X(fx) + '" cy="' + Y(fy) + '" r="' + r + '" fill="' + color + '"/>';
    if (label) {
      s += '<text x="' + X(fx) + '" y="' + (Y(fy) - r - 3) + '" fill="' + color +
           '" font-size="6" text-anchor="middle" font-weight="600">' + label + '</text>';
    }
    return s;
  }

  // ---------------------------------------------------------------- MISSIYA 1
  function m1() {
    return '<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" role="img" ' +
      'aria-label="1-missiya maydonchasi: baza, yuk zonasi va robot yo\'li">' + defs() +
      frame('MISSIYA 1 — YUK TASHISH', '200x100 sm maydon · o\'lchamlar sm da · baza chap past burchakda') +
      base() +
      box(90, 20, 20, 20, 'rgba(154,100,16,0.12)', C.amber, 'YUK ZONASI') +
      dot(90, 20, 3.2, C.amber) +
      '<text x="' + X(150) + '" y="' + (Y(20) + 2) + '" fill="' + C.dim +
      '" font-size="5.5" text-anchor="middle" font-family="monospace">yuk 5x5 sm — (90, 20)</text>' +
      path([[20, 20], [82, 20]], C.green) +
      path([[82, 9], [22, 9]], C.cyan) +
      '<text x="' + X(52) + '" y="' + (Y(20) - 4) + '" fill="' + C.green +
      '" font-size="5.5" text-anchor="middle">1. borish</text>' +
      '<text x="' + X(122) + '" y="' + (Y(9) + 2) + '" fill="' + C.cyan +
      '" font-size="5.5" text-anchor="middle">3. yuk bilan qaytish</text>' +
      '</svg>';
  }

  // ---------------------------------------------------------------- MISSIYA 2
  function m2() {
    return '<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" role="img" ' +
      'aria-label="2-missiya maydonchasi: qora chiziq, yashil belgi va yetkazish zonasi">' + defs() +
      frame('MISSIYA 2 — CHIZIQ BO\'YLAB YETKAZISH', 'Qora chiziq eni 2 sm · yashil belgi (110,20) · zona (150,75)') +
      base() +
      // Qora chiziq: oq halo + to'q yadro -> yorug' maydonda katak chiziqlari ustida ham aniq ko'rinadi
      '<path d="M' + X(40) + ' ' + Y(20) + ' L' + X(150) + ' ' + Y(20) + ' L' + X(150) + ' ' + Y(75) +
      '" fill="none" stroke="#ffffff" stroke-width="4.2" stroke-linecap="square" stroke-linejoin="miter"/>' +
      '<path d="M' + X(40) + ' ' + Y(20) + ' L' + X(150) + ' ' + Y(20) + ' L' + X(150) + ' ' + Y(75) +
      '" fill="none" stroke="#16261b" stroke-width="2.4" stroke-linecap="square" stroke-linejoin="miter"/>' +
      box(150, 75, 30, 30, 'rgba(11,107,143,0.12)', C.blue, 'YETKAZISH ZONASI') +
      // yashil belgi
      '<rect x="' + X(107.5) + '" y="' + Y(22.5) + '" width="5" height="5" fill="' + C.green + '"/>' +
      '<text x="' + X(114) + '" y="' + (Y(13) + 1) + '" fill="' + C.green +
      '" font-size="5.5" text-anchor="start" font-weight="600">yashil belgi</text>' +
      dot(98, 32, 2.8, C.amber, 'yuk') +
      path([[20, 20], [105, 20]], C.green) +
      path([[115, 20], [148, 20], [148, 68]], C.cyan) +
      '<text x="' + X(66) + '" y="' + (Y(20) + 9) + '" fill="' + C.green +
      '" font-size="5.5" text-anchor="middle">1. chiziqni kuzatib borish</text>' +
      '<text x="' + X(62) + '" y="' + (Y(8) + 2) + '" fill="' + C.dim +
      '" font-size="5" text-anchor="middle" font-family="monospace">qora lenta, eni 2 sm</text>' +
      '<text x="' + X(170) + '" y="' + Y(50) + '" fill="' + C.cyan +
      '" font-size="5.5" text-anchor="middle">3. yukni qo\'yish</text>' +
      '</svg>';
  }

  // ---------------------------------------------------------------- MISSIYA 3
  function m3() {
    return '<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" role="img" ' +
      'aria-label="3-missiya maydonchasi: ikkita to\'siq va richag">' + defs() +
      frame('MISSIYA 3 — TO\'SIQLI YO\'L VA RICHAG', 'Zigzag majburiy: 1-to\'siq YUQORIDAN, 2-to\'siq PASTDAN aylanadi') +
      base() +
      // 1-to'siq: x 65..75, y 0..55 (pastdan)
      '<rect x="' + X(65) + '" y="' + Y(55) + '" width="10" height="55" fill="rgba(192,57,43,0.16)" stroke="' +
      C.red + '" stroke-width="0.9"/>' +
      '<text x="' + X(70) + '" y="' + (Y(55) - 4) + '" fill="' + C.red +
      '" font-size="6" text-anchor="middle" font-weight="600">1-to\'siq</text>' +
      '<text x="' + X(70) + '" y="' + Y(28) + '" fill="' + C.red +
      '" font-size="5" text-anchor="middle" font-family="monospace" transform="rotate(-90 ' + X(70) + ' ' + Y(28) + ')">h=55</text>' +
      // 2-to'siq: x 110..120, y 45..100 (yuqoridan)
      '<rect x="' + X(110) + '" y="' + Y(100) + '" width="10" height="55" fill="rgba(192,57,43,0.16)" stroke="' +
      C.red + '" stroke-width="0.9"/>' +
      '<text x="' + X(115) + '" y="' + (Y(45) + 9) + '" fill="' + C.red +
      '" font-size="6" text-anchor="middle" font-weight="600">2-to\'siq</text>' +
      // richag
      box(175, 25, 16, 16, 'rgba(107,63,160,0.13)', C.purple, 'RICHAG') +
      '<line x1="' + X(170) + '" y1="' + Y(25) + '" x2="' + X(180) + '" y2="' + Y(32) +
      '" stroke="' + C.purple + '" stroke-width="1.6" stroke-linecap="round"/>' +
      '<text x="' + X(175) + '" y="' + (Y(17) + 6) + '" fill="' + C.dim +
      '" font-size="5" text-anchor="middle" font-family="monospace">(175,25) qizil-&gt;yashil</text>' +
      // yo'l: zigzag
      path([[20, 20], [55, 20]], C.green) +
      path([[55, 20], [55, 70], [90, 70], [90, 25], [166, 25]], C.amber, '3 2') +
      '<text x="' + X(28) + '" y="' + Y(7) + '" fill="' + C.green +
      '" font-size="5.5" text-anchor="middle">3.1 sezish</text>' +
      '<text x="' + X(72) + '" y="' + (Y(70) - 4) + '" fill="' + C.amber +
      '" font-size="5.5" text-anchor="middle">3.2 yuqoridan</text>' +
      '<text x="' + X(128) + '" y="' + (Y(25) + 9) + '" fill="' + C.amber +
      '" font-size="5.5" text-anchor="middle">3.3 pastdan</text>' +
      '</svg>';
  }

  // ---------------------------------------------------------------- MISSIYA 4
  function m4() {
    return '<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" role="img" ' +
      'aria-label="4-missiya maydonchasi: signal kartochkasi, ikkita yuk va platforma">' + defs() +
      frame('MISSIYA 4 — AQLLI SARALASH VA KO\'TARISH', 'Signal QIZIL -> A yuk · KO\'K -> B yuk · platforma 10 sm baland') +
      base() +
      // signal kartochkasi
      '<rect x="' + X(55) + '" y="' + Y(55) + '" width="10" height="10" fill="url(#sig)" stroke="' + C.text +
      '" stroke-width="0.7"/>' +
      '<defs><linearGradient id="sig" x1="0" y1="0" x2="1" y2="0">' +
      '<stop offset="50%" stop-color="' + C.red + '"/><stop offset="50%" stop-color="' + C.blue + '"/>' +
      '</linearGradient></defs>' +
      '<text x="' + X(60) + '" y="' + (Y(55) - 4) + '" fill="' + C.text +
      '" font-size="6" text-anchor="middle" font-weight="600">SIGNAL</text>' +
      '<text x="' + X(72) + '" y="' + (Y(50) + 2) + '" fill="' + C.dim +
      '" font-size="5" text-anchor="start" font-family="monospace">(60,50)</text>' +
      // yuklar
      box(120, 80, 12, 12, 'rgba(192,57,43,0.14)', C.red, 'A yuk') +
      box(120, 20, 12, 12, 'rgba(11,107,143,0.14)', C.blue, 'B yuk') +
      // platforma
      box(175, 50, 25, 25, 'rgba(23,128,74,0.13)', C.green, 'PLATFORMA') +
      '<text x="' + X(175) + '" y="' + Y(46) + '" fill="' + C.green +
      '" font-size="5" text-anchor="middle" font-family="monospace">h = 10 sm</text>' +
      // yo'llar
      path([[20, 20], [52, 45]], C.text, '2 2') +
      path([[66, 55], [110, 78]], C.red) +
      path([[66, 48], [110, 22]], C.blue) +
      path([[128, 78], [163, 54]], C.amber, '3 2') +
      path([[128, 22], [163, 46]], C.amber, '3 2') +
      '<text x="' + X(88) + '" y="' + (Y(70) - 3) + '" fill="' + C.red +
      '" font-size="5.5" text-anchor="middle">qizil bo\'lsa</text>' +
      '<text x="' + X(88) + '" y="' + (Y(30) + 8) + '" fill="' + C.blue +
      '" font-size="5.5" text-anchor="middle">ko\'k bo\'lsa</text>' +
      '</svg>';
  }

  window.MISSION_FIELDS = {
    1: {
      nom: 'Yuk tashish',
      izoh: 'Robot bazadan chiqib, yuk zonasidagi yukni oladi va yuk bilan bazaga qaytadi. ' +
            'Sensorsiz ham bajarish mumkin — faqat masofa va vaqt bo\'yicha.',
      svg: m1()
    },
    2: {
      nom: 'Chiziq bo\'ylab yetkazish',
      izoh: 'Robot qora chiziqni kuzatib boradi, yashil belgida to\'xtaydi, yukni oladi va ' +
            'chiziq oxiridagi ko\'k zonaga qo\'yib, bazaga qaytadi.',
      svg: m2()
    },
    3: {
      nom: 'To\'siqli yo\'l va richag',
      izoh: '1-to\'siq pastdan 55 sm, 2-to\'siq yuqoridan 55 sm baland — shuning uchun robot ' +
            'majburan zigzag qiladi. Har bir burilish gyroskop bilan aniq 90° bo\'lishi kerak.',
      svg: m3()
    },
    4: {
      nom: 'Aqlli saralash va ko\'tarish',
      izoh: 'Signal kartochkasi har urinishdan oldin tasodifiy almashtiriladi, shuning uchun robot ' +
            'yo\'lni oldindan bilmaydi — qarorni sensor asosida o\'zi qabul qilishi kerak.',
      svg: m4()
    }
  };
})();
