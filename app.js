const TYPE_LABELS = {qurish:"Qurish", nazorat:"Nazorat / Musobaqa", loyiha:"Loyiha", dasturlash:"Dasturlash", spike:"SPIKE",
                     elektronika:"Elektronika", arduino:"Arduino", esp32:"ESP32", ai:"Sun'iy intellekt"};
let activeYil = "1-yil";
let activeKey = null;

// --- Telefon: darslar ro'yxati chetdan chiqadigan panel sifatida ochiladi ---
// (860px dan keng ekranda panel doim ko'rinib turadi va bu funksiya hech narsaga ta'sir qilmaydi)
function setNav(open){
  const nav = document.getElementById('treeNav');
  const bd  = document.getElementById('navBackdrop');
  const btn = document.getElementById('navToggle');
  nav.classList.toggle('mobile-open', open);
  bd.classList.toggle('on', open);
  btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  document.body.style.overflow = open ? 'hidden' : '';
}
function isMobile(){ return window.matchMedia('(max-width: 860px)').matches; }

// Sarlavha balandligini o'lchab CSS ga uzatadi (telefonda u ikki qatorga bo'linadi,
// shuning uchun qiymat qat'iy yozib qo'yilmaydi).
function syncHeaderHeight(){
  const h = document.querySelector('header').offsetHeight;
  document.documentElement.style.setProperty('--hdr', h + 'px');
}

// Noyob kalit: yil|sinf|chorak|index. Bir xil model bir nechta sinf/choraqda takrorlansa ham
// (masalan "Crane" 0/1/2-sinfda), har birining joylashuvi bo'yicha ALOHIDA kalit hosil bo'ladi —
// shu sababli har bir sinf darajasiga mos alohida kontent yozish mumkin (title+model kaliti bilan
// avval bularning barchasi bitta yozuvga to'qnashardi).
function lessonKey(yil, sinf, chorak, idx){ return yil + "|" + sinf + "|" + chorak + "|" + idx; }

function countAll(){
  let total = 0, ready = 0;
  for (const yil in TREE_DATA){
    for (const sinf in TREE_DATA[yil]){
      for (const chorak in TREE_DATA[yil][sinf]){
        TREE_DATA[yil][sinf][chorak].forEach((l, idx)=>{
          total++;
          if (LESSON_CONTENT[lessonKey(yil, sinf, chorak, idx)]) ready++;
        });
      }
    }
  }
  document.getElementById('totalCount').textContent = total;
  document.getElementById('readyCount').textContent = ready;
}

function renderTree(){
  const nav = document.getElementById('treeNav');
  nav.innerHTML = '';

  const tabs = document.createElement('div');
  tabs.className = 'yil-tabs';
  ['1-yil','2-yil'].forEach(yil=>{
    const t = document.createElement('div');
    t.className = 'yil-tab' + (yil===activeYil ? ' active':'');
    t.textContent = yil.toUpperCase();
    t.onclick = ()=>{ activeYil = yil; renderTree(); };
    tabs.appendChild(t);
  });
  nav.appendChild(tabs);

  const grades = TREE_DATA[activeYil];
  Object.keys(grades).forEach(sinf=>{
    const block = document.createElement('div');
    block.className = 'sinf-block';

    let sinfLessonCount = 0;
    Object.values(grades[sinf]).forEach(arr=> sinfLessonCount += arr.length);

    const head = document.createElement('div');
    head.className = 'sinf-head';
    head.innerHTML = `<span class="chevron">▸</span><span>${sinf.toUpperCase()}</span><span class="sinf-count">${sinfLessonCount}</span>`;
    block.appendChild(head);

    const chorakList = document.createElement('div');
    chorakList.className = 'chorak-list';

    Object.keys(grades[sinf]).forEach(chorak=>{
      const cHead = document.createElement('div');
      cHead.className = 'chorak-head';
      cHead.innerHTML = `<span class="chevron">▸</span><span>${chorak}</span>`;
      chorakList.appendChild(cHead);

      const darsList = document.createElement('div');
      darsList.className = 'dars-list';

      grades[sinf][chorak].forEach((l, idx)=>{
        const key = lessonKey(activeYil, sinf, chorak, idx);
        const item = document.createElement('div');
        const isReady = !!LESSON_CONTENT[key];
        item.className = 'dars-item' + (isReady ? ' ready':'') + (key===activeKey ? ' active':'');
        const label = l.model ? `${l.title} <span style="color:var(--text-faint)">— ${l.model}</span>` : l.title;
        item.innerHTML = `<span class="dnum">${idx+1}.</span><span>${label}</span>`;
        item.onclick = ()=> selectLesson(l, key, item);
        darsList.appendChild(item);
      });

      cHead.onclick = ()=>{
        cHead.classList.toggle('open');
        darsList.classList.toggle('open');
      };
      chorakList.appendChild(darsList);
    });

    head.onclick = ()=>{
      head.classList.toggle('open');
      chorakList.classList.toggle('open');
    };

    block.appendChild(chorakList);
    nav.appendChild(block);
  });
}

function esc(s){ const d=document.createElement('div'); d.textContent=s; return d.innerHTML; }

// Dars uchun qurish instruksiyasini topadi.
// Makerzoid darslarida kalit = model nomi; SPIKE darslarida model bo'sh, shuning uchun
// sarlavhadan " — yig'ish (1 darslik)" qismini olib tashlab qidiriladi.
function findResources(l){
  const R = window.LESSON_RESOURCES || {};
  if (l.model && R[l.model]) return R[l.model];
  const base = l.title.split(' — ')[0].trim();
  if (R[base]) return R[base];
  return null;
}

function resourceList(l){
  const res = findResources(l);
  if (!res || !res.length) return '';
  const items = res.map(r=>{
    const icon = r.tur === 'pdf' ? 'PDF' : (r.tur === 'video' ? 'VIDEO' : (r.tur === 'lokal' ? 'FAYL' : 'WEB'));
    return `<li class="res-item">
      <a class="res-link" href="${esc(r.url)}" target="_blank" rel="noopener noreferrer">
        <span class="res-type ${r.tur}">${icon}</span>
        <span class="res-name">${esc(r.nom)}</span>
      </a>
      <span class="res-src">${esc(r.manba)}</span>
    </li>`;
  }).join('');
  return `<ul class="res-list">${items}</ul>`;
}

// Makerzoid modellari uchun bosqichma-bosqich rasmli instruksiya (zipdan chiqarilgan WebP).
const INSTR = { slug:null, n:0, i:1 };

function findInstruction(l){
  const IX = window.INSTRUCTION_INDEX || {};
  return (l.model && IX[l.model]) ? IX[l.model] : null;
}

function instrSrc(slug, i){
  return 'instructions/makerzoid/' + slug + '/' + String(i).padStart(3, '0') + '.webp';
}

function galleryHtml(info){
  const thumbs = [];
  for (let i = 1; i <= info.qadam; i++){
    thumbs.push(`<button class="ig-thumb" data-i="${i}" type="button">
      <img loading="lazy" src="${instrSrc(info.slug, i)}" alt="${i}-qadam">
      <span>${i}</span>
    </button>`);
  }
  return `
    <div class="instr" data-slug="${esc(info.slug)}" data-n="${info.qadam}">
      <div class="instr-bar">
        <span class="instr-src">${esc(info.manba)}</span>
        <span class="instr-count">${info.qadam} qadam</span>
      </div>
      <div class="instr-stage">
        <img id="igMain" src="${instrSrc(info.slug, 1)}" alt="1-qadam">
      </div>
      <div class="instr-nav">
        <button class="ig-btn" id="igPrev" type="button">◀ Oldingi</button>
        <span class="ig-pos"><b id="igNow">1</b> / ${info.qadam}</span>
        <button class="ig-btn" id="igNext" type="button">Keyingi ▶</button>
        <button class="ig-btn ig-toggle" id="igAll" type="button">Barcha qadamlar</button>
        <button class="ig-btn ig-full" id="igFull" type="button">⛶ To'liq ekran</button>
      </div>
      <div class="instr-grid" id="igGrid" hidden>${thumbs.join('')}</div>
    </div>`;
}

function instructionSection(l, num){
  const info = findInstruction(l);
  const links = resourceList(l);
  if (!info && !links) return '';
  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>Qurish instruksiyasi</h2>
      ${info ? galleryHtml(info) : ''}
      ${links}
    </div>`;
}

// --- Galereyaning to'liq ekran rejimi ---
// Asosiy yo'l — brauzerning Fullscreen API'si. iPhone Safari oddiy element uchun
// uni bermaydi, shuning uchun zaxira sifatida .ig-fs klassi (position:fixed) ishlatiladi.
function igFsEl(){
  return document.fullscreenElement || document.webkitFullscreenElement || null;
}

function igFsActive(){
  const root = document.querySelector('.instr');
  return !!root && (igFsEl() === root || root.classList.contains('ig-fs'));
}

function igSyncFullBtn(){
  const b = document.getElementById('igFull');
  if (!b) return;
  const on = igFsActive();
  b.textContent = on ? '✕ Chiqish' : '⛶ To\'liq ekran';
  b.classList.toggle('on', on);
}

function igEnterFs(){
  const root = document.querySelector('.instr');
  if (!root) return;
  const req = root.requestFullscreen || root.webkitRequestFullscreen;
  if (req){
    try {
      const p = req.call(root);
      // Ruxsat berilmasa yoki qo'llab-quvvatlanmasa — zaxira rejimga tushamiz
      if (p && p.catch) p.catch(igFallbackOn); else igSyncFullBtn();
      return;
    } catch (e) { /* pastda zaxira rejim */ }
  }
  igFallbackOn();
}

function igFallbackOn(){
  const root = document.querySelector('.instr');
  if (root) root.classList.add('ig-fs');
  document.body.classList.add('ig-fs-open');
  igSyncFullBtn();
}

function igExitFs(){
  const root = document.querySelector('.instr');
  if (igFsEl()){
    const ex = document.exitFullscreen || document.webkitExitFullscreen;
    if (ex) ex.call(document);
  }
  if (root) root.classList.remove('ig-fs');
  document.body.classList.remove('ig-fs-open');
  igSyncFullBtn();
}

// Bir marta ulanadi: initGallery har darsda chaqiriladi, listener to'planib qolmasligi kerak.
document.addEventListener('fullscreenchange', igSyncFullBtn);
document.addEventListener('webkitfullscreenchange', igSyncFullBtn);   // eski Safari/Chrome

// innerHTML almashtirilgandan keyin galereyani jonlantiradi.
function initGallery(){
  const root = document.querySelector('.instr');
  // Boshqa darsga o'tilganda zaxira rejimning izlari qolib ketmasin
  document.body.classList.remove('ig-fs-open');
  if (!root) { INSTR.slug = null; return; }
  INSTR.slug = root.dataset.slug;
  INSTR.n = parseInt(root.dataset.n, 10);
  INSTR.i = 1;

  const main = document.getElementById('igMain');
  const now  = document.getElementById('igNow');
  const grid = document.getElementById('igGrid');

  function show(i){
    INSTR.i = Math.min(Math.max(i, 1), INSTR.n);
    main.src = instrSrc(INSTR.slug, INSTR.i);
    main.alt = INSTR.i + '-qadam';
    now.textContent = INSTR.i;
    if (INSTR.i < INSTR.n) new Image().src = instrSrc(INSTR.slug, INSTR.i + 1);  // keyingisini oldindan yuklash
  }

  document.getElementById('igPrev').onclick = ()=> show(INSTR.i - 1);
  document.getElementById('igNext').onclick = ()=> show(INSTR.i + 1);

  // Telefonda barmoq bilan chapga/o'ngga surib qadam almashtirish
  const stage = root.querySelector('.instr-stage');
  let sx = 0, sy = 0, moved = false;
  stage.addEventListener('touchstart', (e)=>{
    sx = e.touches[0].clientX; sy = e.touches[0].clientY; moved = false;
  }, {passive:true});
  stage.addEventListener('touchmove', (e)=>{
    if (Math.abs(e.touches[0].clientX - sx) > 12) moved = true;
  }, {passive:true});
  stage.addEventListener('touchend', (e)=>{
    const dx = e.changedTouches[0].clientX - sx;
    const dy = e.changedTouches[0].clientY - sy;
    if (!moved || Math.abs(dx) < 45 || Math.abs(dx) < Math.abs(dy)) return;  // vertikal aylantirishga xalaqit bermaslik
    show(INSTR.i + (dx < 0 ? 1 : -1));
  }, {passive:true});
  document.getElementById('igAll').onclick = (e)=>{
    grid.hidden = !grid.hidden;
    e.currentTarget.classList.toggle('on', !grid.hidden);
  };
  grid.querySelectorAll('.ig-thumb').forEach(b=>{
    b.onclick = ()=>{ show(parseInt(b.dataset.i, 10)); root.scrollIntoView({block:'start', behavior:'smooth'}); };
  });
  document.getElementById('igFull').onclick = ()=> igFsActive() ? igExitFs() : igEnterFs();
  igSyncFullBtn();

  // Rasmni bosish = keyingi qadam. Svaypdan keyin click ham otiladi — shuning uchun tekshiramiz.
  main.onclick = ()=>{ if (!moved) show(INSTR.i + 1); moved = false; };
}

document.addEventListener('keydown', (e)=>{
  if (!INSTR.slug) return;
  if (document.activeElement && document.activeElement.id === 'searchInput') return;
  if (e.key === 'ArrowRight') document.getElementById('igNext')?.click();
  else if (e.key === 'ArrowLeft') document.getElementById('igPrev')?.click();
  // Brauzerning o'z to'liq ekrani Escape'ni o'zi ushlaydi; bu zaxira rejim uchun
  else if (e.key === 'Escape' && document.querySelector('.instr.ig-fs')) igExitFs();
  else if (e.key === 'f' || e.key === 'F') document.getElementById('igFull')?.click();
});

// Missiya darslari uchun: shu darsning aniq topshirig'i + butun missiyaning ball jadvali.
// Topshiriqlar darsdan darsga qiyinlashadi (n.A qog'ozda -> n.F rasmiy urinish).
function topshiriqSection(content, num){
  const t = content.topshiriq;
  if (!t) return '';
  const talablar = t.talablar.map(x=>`<li>${esc(x)}</li>`).join('');
  const rows = t.ballJadvali.map(r=>`
    <tr>
      <td class="tk">${esc(r.kod)}</td>
      <td>${esc(r.matn)}</td>
      <td class="tb">${r.ball}</td>
    </tr>`).join('');
  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>Dars topshirig'i</h2>
      <div class="task-box">
        <div class="task-head">
          <span class="task-code">${esc(t.kod)}</span>
          <span class="task-title">${esc(t.sarlavha)}</span>
        </div>
        <ol class="task-list">${talablar}</ol>
        <div class="task-mezon"><b>Muvaffaqiyat mezoni:</b> ${esc(t.mezon)}</div>
      </div>
      <div class="subhead">${t.missiya}-missiya ("${esc(t.missiyaNomi)}") — to'liq ball jadvali</div>
      <div class="score-wrap">
        <table class="score-table">
          <thead><tr><th>Kod</th><th>Topshiriq</th><th>Ball</th></tr></thead>
          <tbody>${rows}</tbody>
          <tfoot><tr><td></td><td>Jami · vaqt cheklovi ${t.vaqt} soniya</td><td class="tb">${t.jamiBall}</td></tr></tfoot>
        </table>
      </div>
    </div>`;
}

function maydonSection(content, num){
  const F = window.MISSION_FIELDS || {};
  const f = F[content.maydon];
  if (!f) return '';
  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>Musobaqa maydonchasi</h2>
      <div class="field-wrap">${f.svg}</div>
      <div class="scroll-hint">← chizmani yon tomonga surib ko'ring →</div>
      <p class="field-note">${esc(f.izoh)}</p>
    </div>`;
}

// 5-8-sinf darslari uchun: komponentni qaysi portga ulash va qaysi kutubxona kerak.
// Kichik bo'lim raqamlari (8.1, 8.2 ...) shu yerda beriladi — ma'lumotda raqam yo'q,
// shuning uchun bo'lim tartibi o'zgarsa raqamlar o'zi to'g'rilanadi.
function ulanishSection(content, num){
  const u = content && content.ulanish;
  if (!u || !u.length) return '';
  const bloklar = u.map((b, i)=>`
    <div class="subhead">${parseInt(num,10)}.${i+1}. ${esc(b.nom)} — ulanish va kutubxona</div>
    <ul>${b.points.map(p=>`<li>${esc(p)}</li>`).join('')}</ul>`).join('');
  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>Ulanish sxemasi va kutubxona</h2>
      ${bloklar}
    </div>`;
}

// 01–07 — tasdiqlangan asosiy shablon (o'zgarmaydi).
// Undan keyingi bo'limlar bor bo'lsa, ketma-ket raqamlanadi: 08, 09, 10...
function extraSections(l, content){
  let n = 7;
  const num = ()=> String(++n).padStart(2, '0');
  const parts = [];
  const push = (fn)=>{ const h = fn(num()); if (h) parts.push(h); else n--; };
  if (content) {
    push(k=> topshiriqSection(content, k));
    push(k=> maydonSection(content, k));
    push(k=> ulanishSection(content, k));
  }
  push(k=> instructionSection(l, k));
  return parts.join('');
}

function selectLesson(l, key, itemEl){
  activeKey = key;
  document.querySelectorAll('.dars-item.active').forEach(e=>e.classList.remove('active'));
  if (itemEl) itemEl.classList.add('active');
  if (isMobile()) setNav(false);   // telefonda dars tanlangach panel yopiladi

  const main = document.getElementById('mainContent');
  const content = LESSON_CONTENT[key];

  if (!content){
    main.innerHTML = `
      <div class="lesson-header">
        <div class="badge-row"><span class="type-badge ${l.type}">${TYPE_LABELS[l.type]||l.type}</span></div>
        <div class="lesson-title">${esc(l.title)}</div>
        ${l.model ? `<div class="lesson-model">▸ ${esc(l.model)}</div>` : ''}
      </div>
      <div class="not-ready">
        <div class="tag">TAYYORLANMOQDA</div>
        <p>Bu darsning to'liq ishlanmasi (maqsad, lug'at, nazariya, amaliyot, uyga vazifa) hali tayyorlanmagan.<br>
        Iltimos, boshqa darsni tanlang.</p>
      </div>
      ${extraSections(l, null)}`;
    initGallery();
    main.scrollTop = 0;
    return;
  }

  const m = content.meta;
  main.innerHTML = `
    <div class="lesson-header">
      <div class="badge-row"><span class="type-badge ${l.type}">${TYPE_LABELS[l.type]||l.type}</span></div>
      <div class="lesson-title">${esc(l.title)}</div>
      ${l.model ? `<div class="lesson-model">▸ ${esc(l.model)}</div>` : ''}
    </div>

    <div class="meta-grid">
      <div class="meta-cell"><div class="k">Sinf / Yil</div><div class="v">${m.sinf}, ${m.yil}</div></div>
      <div class="meta-cell"><div class="k">Chorak</div><div class="v">${m.chorak}</div></div>
      <div class="meta-cell"><div class="k">Dars raqami</div><div class="v">${m.darsRaqami}</div></div>
      <div class="meta-cell"><div class="k">Modul</div><div class="v">${m.modul}</div></div>
      <div class="meta-cell"><div class="k">Jihoz</div><div class="v">${m.jihoz}</div></div>
      <div class="meta-cell"><div class="k">Davomiyligi</div><div class="v">${m.davomiyligi}</div></div>
    </div>

    <div class="section">
      <div class="section-num">01</div>
      <h2>Darsning maqsadi</h2>
      <ol>${content.maqsad.map(t=>`<li>${esc(t)}</li>`).join('')}</ol>
    </div>

    <div class="section">
      <div class="section-num">02</div>
      <h2>Lug'at</h2>
      <ol>${content.lugat.map(t=>`<li>${esc(t)}</li>`).join('')}</ol>
    </div>

    <div class="section">
      <div class="section-num">03</div>
      <h2>Soft skill</h2>
      <div class="soft-skill-box"><p>${esc(content.softSkill)}</p></div>
    </div>

    <div class="section">
      <div class="section-num">04</div>
      <h2>Darsga kerakli resurslar</h2>
      <ol>${content.resurslar.map(t=>`<li>${esc(t)}</li>`).join('')}</ol>
    </div>

    <div class="section">
      <div class="section-num">05</div>
      <h2>Darsning nazariya qismi</h2>
      ${content.nazariya.map(sec=>`<div class="subhead">${esc(sec.title)}</div><ul>${sec.points.map(p=>`<li>${esc(p)}</li>`).join('')}</ul>`).join('')}
    </div>

    <div class="section">
      <div class="section-num">06</div>
      <h2>Sinfda bajariladigan amaliy ishlar</h2>
      ${content.amaliy.map(sec=>`<div class="subhead">${esc(sec.title)}</div><ul>${sec.points.map(p=>`<li>${esc(p)}</li>`).join('')}</ul>`).join('')}
    </div>

    <div class="section">
      <div class="section-num">07</div>
      <h2>Uyga vazifalar</h2>
      <ol>${content.uyga.map(t=>`<li>${esc(t)}</li>`).join('')}</ol>
    </div>

    ${extraSections(l, content)}
  `;
  initGallery();
  main.scrollTop = 0;
}

document.getElementById('searchInput').addEventListener('input', (e)=>{
  const q = e.target.value.trim().toLowerCase();
  document.querySelectorAll('.dars-item').forEach(item=>{
    const text = item.textContent.toLowerCase();
    const match = !q || text.includes(q);
    item.style.display = match ? '' : 'none';
    if (q && match){
      const dl = item.closest('.dars-list');
      dl.classList.add('open');
      dl.previousElementSibling.classList.add('open');
      item.closest('.sinf-block').querySelector('.chorak-list').classList.add('open');
      item.closest('.sinf-block').querySelector('.sinf-head').classList.add('open');
    }
  });
  // Telefonda qidirilganda natijani ko'rish uchun panel o'zi ochiladi
  if (q && isMobile()) setNav(true);
});

// --- Panel boshqaruvi ---
document.getElementById('navToggle').addEventListener('click', ()=>{
  setNav(!document.getElementById('treeNav').classList.contains('mobile-open'));
});
document.getElementById('navBackdrop').addEventListener('click', ()=> setNav(false));
document.addEventListener('keydown', (e)=>{
  if (e.key === 'Escape') setNav(false);
});
// Telefondan planshet/kompyuterga o'tilsa (ekran burilishi) holat tozalanadi
window.matchMedia('(max-width: 860px)').addEventListener('change', (e)=>{
  if (!e.matches) setNav(false);
});
window.addEventListener('resize', syncHeaderHeight);
window.addEventListener('orientationchange', syncHeaderHeight);

renderTree();
countAll();
syncHeaderHeight();
// Shriftlar yuklangach sarlavha balandligi biroz o'zgarishi mumkin
if (document.fonts && document.fonts.ready) document.fonts.ready.then(syncHeaderHeight);
