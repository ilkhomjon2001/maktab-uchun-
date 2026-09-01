/*
 * LOKAL SERVER
 * ============
 * Platformani brauzerda ochish uchun. Tashqi kutubxona kerak emas.
 *
 *     node tools/server.js            -> http://localhost:8080
 *     node tools/server.js 9000       -> boshqa port
 *
 * Ishlab chiqarishda nginx ishlatiladi — bu faqat lokal ko'rish uchun.
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const ILDIZ = path.join(__dirname, '..');
const PORT = Number(process.argv[2]) || 8080;

const TUR = {
  '.html':'text/html; charset=utf-8',
  '.js'  :'text/javascript; charset=utf-8',
  '.css' :'text/css; charset=utf-8',
  '.json':'application/json; charset=utf-8',
  '.webp':'image/webp',
  '.png' :'image/png',
  '.jpg' :'image/jpeg',
  '.svg' :'image/svg+xml',
  '.xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  '.md'  :'text/markdown; charset=utf-8'
};

http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p === '/' || p === '') p = '/index.html';

  // Papkadan chiqib ketishning oldini olish
  const fayl = path.join(ILDIZ, path.normalize(p).replace(/^[\\/]+/, ''));
  if (!fayl.startsWith(ILDIZ)) {
    res.writeHead(403); res.end('Taqiqlangan'); return;
  }

  fs.stat(fayl, (xato, st) => {
    if (xato || !st.isFile()) {
      res.writeHead(404, {'Content-Type':'text/plain; charset=utf-8'});
      res.end('Topilmadi: ' + p);
      return;
    }
    const kengaytma = path.extname(fayl).toLowerCase();
    res.writeHead(200, {
      'Content-Type': TUR[kengaytma] || 'application/octet-stream',
      'Content-Length': st.size,
      // Rasmlar o'zgarmaydi — brauzer keshlab tursin
      'Cache-Control': kengaytma === '.webp' ? 'public, max-age=604800' : 'no-cache'
    });
    fs.createReadStream(fayl).pipe(res);
  });
}).listen(PORT, () => {
  console.log('Tarbion 0–4 platformasi:  http://localhost:' + PORT + '/');
  console.log("To'xtatish: Ctrl+C");
});
