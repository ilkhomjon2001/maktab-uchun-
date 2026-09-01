const TYPE_LABELS = {qurish:"Qurish", nazorat:"Nazorat / Musobaqa", loyiha:"Loyiha", dasturlash:"Dasturlash", spike:"SPIKE",
                     elektronika:"Elektronika", arduino:"Arduino", esp32:"ESP32", ai:"Sun'iy intellekt"};

/* ============================================================
   KONFIGURATSIYA — vaqtincha yashiriladigan bo'limlar
   ============================================================
   2-yil, 2- va 3-sinfdagi "3-chorak (Dasturlash)" va "4-chorak (Dasturlash)"
   choraklari VAQTINCHA yashirilgan (2026-08-10, foydalanuvchi so'rovi:
   dasturlash kursi alohida qo'shiladi).

   Ma'lumot O'CHIRILMAGAN — 38 ta dars tree_data.js va sample_lessons.js da
   o'z joyida turibdi. Faqat ro'yxatda ko'rsatilmaydi, qidiruvga tushmaydi va
   "tayyor darslar" hisobiga qo'shilmaydi.

   QAYTARISH: quyidagi qiymatni true qilish yetarli, boshqa hech narsa
   o'zgartirilmaydi. */
const DASTURLASH_KORINSIN = false;
const YASHIRIN_CHORAK = /\(Dasturlash\)/;

function chorakKorinsinmi(chorak){
  return DASTURLASH_KORINSIN || !YASHIRIN_CHORAK.test(chorak);
}
// Sinf ichidagi KO'RINADIGAN choraklar ro'yxati (tartibi tree_data.js dagidek)
function choraklarRoyxati(yil, sinf){
  return Object.keys(TREE_DATA[yil][sinf]).filter(chorakKorinsinmi);
}

/* ============================================================
   HOLAT
   ============================================================ */
let activeFan = null;        // null = bosh sahifa (fanlar ro'yxati)
let activeYil = "1-yil";
let activeKey = null;
let activeSinf = null;       // "yil|sinf" — sinfning yillik rejasi ochilgan

const FANLAR = window.FANLAR || [];
function fanTopilsin(id){
  for (const f of FANLAR) if (f.id === id) return f;
  return null;
}
// Kartochka belgisi ostidagi yumshoq fon — fanning o'z rangidan hosil qilinadi
function yumshoqRang(hex, alfa){
  const m = /^#?([0-9a-f]{6})$/i.exec(String(hex || ''));
  if (!m) return 'var(--brand-soft)';
  const n = parseInt(m[1], 16);
  return `rgba(${(n>>16)&255}, ${(n>>8)&255}, ${n&255}, ${alfa})`;
}

/* ============================================================
   MARSHRUT (havolada saqlanadi)
   ============================================================
   #/robototexnika                                  — fan ochilgan
   #/robototexnika/1-yil/0-sinf                     — sinfning yillik rejasi
   #/robototexnika/1-yil/0-sinf/1-chorak/3          — aniq dars
   Shu sababli dars havolasini o'qituvchiga yuborish mumkin va sahifa
   yangilanganda ham o'sha dars ochiladi. */
let hashOzimYozdim = false;

function marshrutYoz(){
  const qism = ['#'];
  if (activeFan){
    qism.push(encodeURIComponent(activeFan));
    if (activeKey) activeKey.split('|').forEach(p => qism.push(encodeURIComponent(p)));
    else if (activeSinf) activeSinf.split('|').forEach(p => qism.push(encodeURIComponent(p)));
  }
  const h = qism.join('/');
  if (location.hash === h || (!location.hash && h === '#/')) return;
  hashOzimYozdim = true;
  location.hash = h;
  setTimeout(()=>{ hashOzimYozdim = false; }, 0);
}

function marshrutOqi(){
  const raw = location.hash.replace(/^#\/?/, '');
  if (!raw) return {fan:null, key:null, sinf:null};
  let p;
  try { p = raw.split('/').map(decodeURIComponent); }
  catch(e){ return {fan:null, key:null, sinf:null}; }
  return {
    fan:  p[0] || null,
    key:  p.length >= 5 ? p.slice(1, 5).join('|') : null,
    sinf: p.length === 3 ? p.slice(1, 3).join('|') : null
  };
}

// Kalitdan dars yozuvini topadi (havoladan tiklanganda kerak)
function darsTop(key){
  const p = String(key || '').split('|');
  if (p.length !== 4) return null;
  const [yil, sinf, chorak, idx] = p;
  const arr = TREE_DATA[yil] && TREE_DATA[yil][sinf] && TREE_DATA[yil][sinf][chorak];
  if (!arr) return null;
  const l = arr[Number(idx)];
  return l ? {l, yil, sinf, chorak, idx: Number(idx)} : null;
}

/* ============================================================
   KO'RINISHLAR
   ============================================================ */
function korinish(nom){ document.body.dataset.view = nom; }

function render(){
  const fan = activeFan ? fanTopilsin(activeFan) : null;
  const main = document.getElementById('mainContent');

  if (!fan){
    activeKey = null;
    korinish('home');
    renderHome(main);
    marshrutYoz();
    return;
  }

  const pill = document.getElementById('fanPill');
  document.getElementById('fanPillIco').textContent = fan.belgi || '📘';
  document.getElementById('fanPillNom').textContent = fan.qisqa || fan.nom;
  pill.style.setProperty('--fan-rang', fan.rang || 'var(--brand)');

  if (fan.holat !== 'tayyor'){
    activeKey = null;
    korinish('reja');
    renderFanReja(main, fan);
    marshrutYoz();
    return;
  }

  korinish('darslar');
  const dars = activeKey ? darsTop(activeKey) : null;
  if (dars) activeYil = dars.yil;
  else if (activeSinf) activeYil = activeSinf.split('|')[0];
  renderTree();
  if (dars){
    selectLesson(dars.l, activeKey, null);
    treeFokus(activeKey);
  } else if (activeSinf){
    const [sy, ss] = activeSinf.split('|');
    renderSinfSahifa(main, fan, sy, ss);
  } else {
    renderFanBosh(main, fan);
  }
  marshrutYoz();
}

function fanOch(id){
  activeFan = id;
  activeKey = null;
  activeSinf = null;
  render();
  window.scrollTo(0, 0);
}
function fanlarga(){
  activeFan = null;
  activeKey = null;
  activeSinf = null;
  render();
}

/* --- Bosh sahifa: fanlar ro'yxati --- */
function fanCard(fan){
  const tayyor = fan.holat === 'tayyor';
  const s = (tayyor && fan.manba === 'tree') ? sanoq() : null;
  const son = s ? `<span class="fc-son"><b>${s.ready}</b> ta dars rejasi</span>` : '';
  return `<button class="fan-card ${tayyor ? 'tayyor' : 'reja'}" type="button" data-fan="${esc(fan.id)}"
      style="--fan-rang:${esc(fan.rang || '#22A03C')}; --fan-yumshoq:${yumshoqRang(fan.rang, 0.14)}">
    <div class="fc-top">
      <div class="fc-ico" aria-hidden="true">${esc(fan.belgi || '📘')}</div>
      <div>
        <div class="fc-nom">${esc(fan.nom)}</div>
        <div class="fc-sinf">${esc(fan.sinflar || '')}</div>
      </div>
    </div>
    <div class="fc-tav">${esc(fan.tavsif || '')}</div>
    <div class="fc-foot">
      <span class="holat ${tayyor ? 'tayyor' : 'reja'}">${tayyor ? 'Tayyor' : 'Tayyorlanmoqda'}</span>
      ${son}
    </div>
  </button>`;
}

function renderHome(main){
  const s = sanoq();
  const tayyorFan = FANLAR.filter(f => f.holat === 'tayyor').length;
  const guruhlar = (window.FAN_GURUHLARI || []).slice();
  // Ro'yxatdagi noma'lum guruh oxirida chiqadi — fan hech qachon yo'qolib qolmaydi
  FANLAR.forEach(f=>{ if (guruhlar.indexOf(f.guruh) === -1) guruhlar.push(f.guruh || 'Boshqa fanlar'); });

  const bloklar = guruhlar.map(g=>{
    const ichida = FANLAR.filter(f => (f.guruh || 'Boshqa fanlar') === g);
    if (!ichida.length) return '';
    return `<section class="fan-guruh">
      <h2>${esc(g)}</h2>
      <div class="fan-grid">${ichida.map(fanCard).join('')}</div>
    </section>`;
  }).join('');

  main.innerHTML = `
    <div class="home">
      <div class="hero">
        <div class="hero-eyebrow">Tarbion xususiy maktabi</div>
        <h1>Dars rejalar <em>bazasi</em></h1>
        <p>Maktabning barcha fanlari bo'yicha to'liq dars ishlanmalari bitta joyda:
           darsning maqsadi, lug'ati, nazariy qismi, sinfda bajariladigan amaliy ishlar,
           baholash mezonlari va uyga vazifa. Fanni tanlang.</p>
        <div class="hero-stats">
          <div class="hs"><div class="n">${FANLAR.length}</div><div class="k">Fan</div></div>
          <div class="hs"><div class="n">${tayyorFan}</div><div class="k">Kontenti tayyor</div></div>
          <div class="hs"><div class="n">${s.ready}</div><div class="k">Tayyor dars rejasi</div></div>
        </div>
        <div class="hero-actions">
          <button class="btn btn-primary" type="button" data-fan="robototexnika">Robototexnika darslarini ochish →</button>
          <a class="btn btn-ghost" href="jihozlar_5-8-sinf.xlsx" download>⤓ 5–8-sinf jihozlari ro'yxati</a>
        </div>
      </div>
      ${bloklar}
    </div>`;
  main.scrollTop = 0;
}

/* --- Kontenti hali tayyorlanmagan fan --- */
function renderFanReja(main, fan){
  main.innerHTML = `
    <div class="fan-soon" style="--fan-yumshoq:${yumshoqRang(fan.rang, 0.14)}">
      <div class="fs-ico" aria-hidden="true">${esc(fan.belgi || '📘')}</div>
      <h1>${esc(fan.nom)}</h1>
      <div class="fs-sinf">${esc(fan.sinflar || '')}</div>
      <p>${esc(fan.tavsif || '')}</p>
      <p>Bu fanning dars rejalari hali tayyorlanmagan. Fan ro'yxatga kiritilgan —
         kontent bazasi tayyor bo'lgach, darslar xuddi robototexnika kabi
         sinf → chorak → dars tartibida ochiladi.</p>
      <div class="fs-list">
        <div class="fsl-h">Har bir dars rejasida bo'ladi</div>
        <ul>
          <li>Darsning maqsadi va lug'ati</li>
          <li>Soft skill va kerakli resurslar</li>
          <li>Nazariy qism — o'qituvchi aytadigan to'liq matn</li>
          <li>Sinfda bajariladigan amaliy ishlar</li>
          <li>Baholash mezonlari va uyga vazifa</li>
        </ul>
      </div>
      <div><button class="btn btn-ghost" type="button" data-home="1">← Fanlar ro'yxatiga qaytish</button></div>
    </div>`;
  main.scrollTop = 0;
}

/* --- Fan ochildi, lekin dars hali tanlanmagan --- */
/* --- Sinfning yillik rejasi: choraklar bo'yicha dars KARTOCHKALARI ---
   Yon paneldagi sinf nomi bosilganda ochiladi. O'qituvchi butun yilni
   bitta ekranda ko'radi: qurish darslarida tayyor modelning rasmi,
   kirish/nazorat/loyihada esa turiga bo'yalgan blok — shunda chorakning
   bosqichlari ko'zga tashlanadi.
   5-8-sinfda "model" — amaliy ish tavsifi (rasm yo'q), shuning uchun
   rasm faqat INSTRUCTION_INDEX da yozuvi bor modelga chiziladi. */
function sinfSanoq(yil, sinf){
  const chorakNomlar = choraklarRoyxati(yil, sinf);
  let dars = 0, model = new Set(), instr = 0, spike = 0;
  chorakNomlar.forEach(ch=>{
    (TREE_DATA[yil][sinf][ch] || []).forEach(l=>{
      dars++;
      if (l.type === 'spike') spike++;
      if (l.model){ model.add(l.model); if (INSTRUCTION_INDEX[l.model]) instr++; }
    });
  });
  return {chorak: chorakNomlar.length, dars, model: model.size, instr, spike};
}

function renderSinfSahifa(main, fan, yil, sinf){
  if (!(TREE_DATA[yil] && TREE_DATA[yil][sinf])){
    renderFanBosh(main, fan);
    return;
  }
  const c = sinfSanoq(yil, sinf);

  const bloklar = choraklarRoyxati(yil, sinf).map(chorak=>{
    const list = TREE_DATA[yil][sinf][chorak] || [];
    const kartlar = list.map((l, i)=>{
      const info = l.model ? INSTRUCTION_INDEX[l.model] : null;
      const tayyor = !!LESSON_CONTENT[lessonKey(yil, sinf, chorak, i)];
      const rasm = info
        ? `<img loading="lazy" src="${instrSrc(info.slug, info.qadam)}" alt="${esc(l.model)}">`
        : `<span class="dk-yoq ${esc(l.type)}">${esc(TYPE_LABELS[l.type] || l.type)}</span>`;
      // Nazorat/loyiha sarlavhasida butun baholash mezoni yozilgan — qisqartiriladi
      const mavzu = l.title.length > 96 ? l.title.slice(0, 94) + '…' : l.title;
      const model = l.model && l.model.length > 46 ? l.model.slice(0, 44) + '…' : l.model;
      return `
        <button class="dars-kart${tayyor ? ' tayyor' : ''}" type="button"
                data-chorak="${esc(chorak)}" data-idx="${i}">
          <span class="dk-rasm">${rasm}</span>
          <span class="dk-tan">
            <span class="dk-yuqori"><span class="dk-nr">${i+1}</span>
              <span class="dk-teg ${esc(l.type)}">${esc(TYPE_LABELS[l.type] || l.type)}</span></span>
            <span class="dk-mavzu">${esc(mavzu)}</span>
            ${model ? `<span class="dk-model">▸ ${esc(model)}</span>` : ''}
            ${info ? `<span class="dk-qadam">▤ ${info.qadam} qadam</span>` : ''}
          </span>
        </button>`;
    }).join('');
    return `
      <div class="chorak-blok">
        <div class="chorak-sarlavha"><h3>${esc(chorak)}</h3>
          <span class="mini">${list.length} dars</span></div>
        <div class="dars-grid">${kartlar}</div>
      </div>`;
  }).join('');

  main.innerHTML = `
    <div class="sinf-hero">
      <div class="sinf-hero-eyebrow">${esc(fan.qisqa || fan.nom)} · ${esc(yil)}</div>
      <h1>${esc(sinf)} — yillik reja</h1>
      <p>${c.chorak} chorak, ${c.dars} dars${c.model ? `, ${c.model} ta model` : ''}${
        c.instr ? `, ${c.instr} darsda rasmli instruksiya` : ''}.
        Darsni ochish uchun kartochkani bosing.</p>
    </div>
    ${bloklar}`;

  main.querySelectorAll('.dars-kart').forEach(b=>{
    b.onclick = ()=>{
      const chorak = b.dataset.chorak, idx = Number(b.dataset.idx);
      const l = TREE_DATA[yil][sinf][chorak][idx];
      selectLesson(l, lessonKey(yil, sinf, chorak, idx), null);
    };
  });
  main.scrollTop = 0;
}

function renderFanBosh(main, fan){
  main.innerHTML = `
    <div class="empty-state">
      <div class="big-icon">${esc(fan.belgi || '◧')}</div>
      <h2>Dars tanlang</h2>
      <p>Ro'yxatdan yil → sinf → chorak → dars bo'yicha tanlang.<br>
         Yashil nuqta (●) — to'liq tayyorlangan dars rejasi.</p>
      <button class="open-nav-btn" type="button" onclick="setNav(true)">Darslar ro'yxatini ochish</button>
    </div>`;
  main.scrollTop = 0;
}

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

// Jami va tayyor darslar soni. Yashirilgan choraklar hisobga OLINMAYDI —
// aks holda "878 dan 878 tayyor" degan hisob noto'g'ri ko'rinardi.
function sanoq(){
  let total = 0, ready = 0;
  for (const yil in TREE_DATA){
    for (const sinf in TREE_DATA[yil]){
      for (const chorak in TREE_DATA[yil][sinf]){
        if (!chorakKorinsinmi(chorak)) continue;
        TREE_DATA[yil][sinf][chorak].forEach((l, idx)=>{
          total++;
          if (LESSON_CONTENT[lessonKey(yil, sinf, chorak, idx)]) ready++;
        });
      }
    }
  }
  return {total, ready};
}

function countAll(){
  const s = sanoq();
  document.getElementById('totalCount').textContent = s.total;
  document.getElementById('readyCount').textContent = s.ready;
}

// Havoladan tiklanganda: darsni ro'yxatda topib, ustidagi bo'limlarni ochadi.
function treeFokus(key){
  const el = document.querySelector('.dars-item[data-key="' + key + '"]');
  if (!el) return;
  document.querySelectorAll('.dars-item.active').forEach(e=>e.classList.remove('active'));
  el.classList.add('active');
  const dl = el.closest('.dars-list');
  dl.classList.add('open');
  dl.previousElementSibling.classList.add('open');
  const blok = el.closest('.sinf-block');
  blok.querySelector('.chorak-list').classList.add('open');
  blok.querySelector('.sinf-head').classList.add('open');
  el.scrollIntoView({block:'center'});
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
    t.onclick = ()=>{
      activeYil = yil;
      renderTree();
      // Ochiq dars shu yilda bo'lsa, ro'yxatda yana belgilanib turadi
      if (activeKey && activeKey.split('|')[0] === yil) treeFokus(activeKey);
    };
    tabs.appendChild(t);
  });
  nav.appendChild(tabs);

  const grades = TREE_DATA[activeYil];
  Object.keys(grades).forEach(sinf=>{
    const block = document.createElement('div');
    block.className = 'sinf-block';

    const korinadigan = choraklarRoyxati(activeYil, sinf);
    let sinfLessonCount = 0;
    korinadigan.forEach(ch=> sinfLessonCount += grades[sinf][ch].length);

    const head = document.createElement('div');
    head.className = 'sinf-head';
    head.innerHTML = `<span class="chevron">▸</span><span>${sinf.toUpperCase()}</span><span class="sinf-count">${sinfLessonCount}</span>`;
    block.appendChild(head);

    const chorakList = document.createElement('div');
    chorakList.className = 'chorak-list';

    korinadigan.forEach(chorak=>{
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
        item.dataset.key = key;
        // 5-8-sinfda "model" — amaliy ish tavsifi, u uzun bo'lishi mumkin.
        // Ro'yxatda qisqartiriladi, to'liq matni dars sahifasida ko'rinadi.
        const qisqa = l.model && l.model.length > 46 ? l.model.slice(0, 44) + '…' : l.model;
        const label = l.model
          ? `${esc(l.title)} <span style="color:var(--text-faint)">— ${esc(qisqa)}</span>`
          : esc(l.title);
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

    // Sinf nomi bosilganda: yon panelda choraklar ochiladi VA asosiy maydonda
    // sinfning yillik rejasi kartochkalar bilan chiziladi.
    head.onclick = ()=>{
      head.classList.toggle('open');
      chorakList.classList.toggle('open');
      activeKey = null;
      activeSinf = activeYil + '|' + sinf;
      const fan = fanTopilsin(activeFan);
      if (fan) renderSinfSahifa(document.getElementById('mainContent'), fan, activeYil, sinf);
      nav.querySelectorAll('.sinf-head.tanlangan').forEach(h=>h.classList.remove('tanlangan'));
      head.classList.add('tanlangan');
      marshrutYoz();
      if (isMobile()) setNav(false);
    };
    if (activeSinf === activeYil + '|' + sinf) head.classList.add('tanlangan');

    block.appendChild(chorakList);
    nav.appendChild(block);
  });
}

function esc(s){ const d=document.createElement('div'); d.textContent=s; return d.innerHTML; }

// Ro'yxat bandi. "Sarlavha: matn" ko'rinishidagi bandda birinchi qism qalin
// qilinadi — uzun nazariy matn shunda ancha oson o'qiladi.
// Faqat qisqa va gap ichida turmagan sarlavhalar ajratiladi.
function li(p){
  const s = String(p == null ? '' : p);
  const i = s.indexOf(': ');
  if (i > 0 && i <= 46 && !/[.!?—]/.test(s.slice(0, i))) {
    return `<li><b>${esc(s.slice(0, i + 1))}</b>${esc(s.slice(i + 1))}</li>`;
  }
  return `<li>${esc(s)}</li>`;
}

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
// 5-8-sinfda "model" maydoni amaliy ishni bildiradi (0-4 da — qurilgan model nomi).
// Mavzu va amaliy ish ajratilgani sarlavhada ham ko'rinib turishi kerak.
function modelLabel(key){
  const sinf = String(key || '').split('|')[1] || '';
  return /^[5-8]-sinf$/.test(sinf) ? 'Amaliy ish: ' : '';
}

// 5-8-sinf: o'qituvchi uchun metodik ko'rsatma — mavzuni qanday tushuntirish
// kerakligi va shu mavzuda o'quvchilar ko'p qiladigan xato.
function qollanmaSection(content, num){
  const q = content && content.qollanma;
  if (!q || !q.matn) return '';
  const xato = q.xato
    ? `<div class="xato-box"><b>Ko'p uchraydigan xato:</b> ${esc(q.xato)}</div>` : '';
  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>O'qituvchi uchun qo'llanma</h2>
      <div class="soft-skill-box"><p>${esc(q.matn)}</p></div>
      ${xato}
    </div>`;
}

// Nazorat-musobaqa va loyiha uchun aniq baholash jadvali.
function mezonSection(content, num){
  const m = content && content.mezon;
  if (!m || !m.qatorlar || !m.qatorlar.length) return '';
  const sarlavha = m.turi === 'loyiha' ? 'Loyihani baholash mezonlari'
                                       : 'Baholash mezonlari';
  const rows = m.qatorlar.map(r=>`
    <tr><td class="tk">${esc(String(r[0]))}</td><td>${esc(String(r[1]))}</td></tr>`).join('');
  const jami = m.turi === 'loyiha'
    ? `<tfoot><tr><td></td><td>Jami — ${m.qatorlar.reduce((s,r)=>s+(Number(r[1])||0),0)} ball</td></tr></tfoot>`
    : (m.vaqt ? `<tfoot><tr><td></td><td>Umumiy vaqt chegarasi — ${Math.round(m.vaqt/60)} daqiqa</td></tr></tfoot>` : '');
  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>${sarlavha}</h2>
      <div class="subhead">${esc(m.nom)}</div>
      <div class="score-wrap">
        <table class="score-table mezon-table">
          <thead><tr><th>${esc(m.ustunlar[0])}</th><th>${esc(m.ustunlar[1])}</th></tr></thead>
          <tbody>${rows}</tbody>
          ${jami}
        </table>
      </div>
    </div>`;
}

// Ulanish chizmasi. Matn ro'yxati bilan bir xil manbadan (b.pinlar) chiziladi,
// shuning uchun chizma va matn hech qachon bir-biridan farq qilib qolmaydi.
function wireClass(port){
  const p = (port || '').toUpperCase();
  if (/\b(5V|3\.3V|VIN|VCC)\b/.test(p)) return 'wd-pwr';    // quvvat — qizil
  if (/GND/.test(p)) return 'wd-gnd';                        // yer — qora
  if (/^—|^-$/.test(p.trim())) return 'wd-none';             // ulanmaydi
  return 'wd-sig';                                           // signal — ko'k
}

function wiringSvg(blok){
  const pins = blok.pinlar || [];
  if (!pins.length) return '';
  const W = 640, ROW = 44, TOP = 62;
  const H = TOP + pins.length * ROW + 14;
  const bx = 16, bw = 168, cx = 456, cw = 168;
  const boxTop = TOP - 30, boxH = pins.length * ROW + 12;

  const rows = pins.map((p, i)=>{
    const y = TOP + i * ROW;
    const [pin, port, izoh] = p;
    const cls = wireClass(port);
    const nechta = cls === 'wd-none'
      ? `<line class="wd-wire wd-none" x1="${bx+bw}" y1="${y}" x2="${cx}" y2="${y}"/>`
      : `<line class="wd-wire ${cls}" x1="${bx+bw}" y1="${y}" x2="${cx}" y2="${y}"/>
         <circle class="wd-dot ${cls}" cx="${bx+bw}" cy="${y}" r="4"/>
         <circle class="wd-dot ${cls}" cx="${cx}" cy="${y}" r="4"/>`;
    const note = izoh ? `<text class="wd-note" x="${(bx+bw+cx)/2}" y="${y-8}" text-anchor="middle">${esc(izoh.length>46 ? izoh.slice(0,44)+'…' : izoh)}</text>` : '';
    return `${nechta}${note}
      <text class="wd-port" x="${bx+bw-12}" y="${y+4}" text-anchor="end">${esc(port)}</text>
      <text class="wd-pin"  x="${cx+12}" y="${y+4}">${esc(pin)}</text>`;
  }).join('');

  return `<div class="wd-wrap"><svg class="wd" viewBox="0 0 ${W} ${H}" role="img"
      aria-label="${esc(blok.nom)} — ${esc(blok.plata||'')} bilan ulanish sxemasi">
      <rect class="wd-box wd-board" x="${bx}" y="${boxTop}" width="${bw}" height="${boxH}" rx="8"/>
      <rect class="wd-box wd-comp"  x="${cx}" y="${boxTop}" width="${cw}" height="${boxH}" rx="8"/>
      <text class="wd-cap" x="${bx+bw/2}" y="${boxTop-10}" text-anchor="middle">${esc(blok.plata||'Plata')}</text>
      <text class="wd-cap" x="${cx+cw/2}" y="${boxTop-10}" text-anchor="middle">${esc(blok.nom)}</text>
      ${rows}
    </svg></div>
    <div class="scroll-hint">← chizmani yon tomonga surib ko'ring →</div>`;
}

function ulanishSection(content, num){
  // Platasiz elektronika darsida blokda pin xaritasi bo'lmaydi — u yerda
  // faqat komponent pasporti ko'rsatiladi, ulanish bo'limi esa chiqmaydi.
  const u = (content && content.ulanish || []).filter(b => b.pinlar && b.pinlar.length);
  if (!u.length) return '';
  const bloklar = u.map((b, i)=>`
    <div class="subhead">${parseInt(num,10)}.${i+1}. ${esc(b.nom)} — ulanish va kutubxona</div>
    ${wiringSvg(b)}
    <ul>${b.points.map(p=>li(p)).join('')}</ul>`).join('');
  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>Ulanish sxemasi va kutubxona</h2>
      ${bloklar}
    </div>`;
}

// Komponentning to'liq texnik pasporti: tasnif, ichida nima sodir bo'ladi,
// qiymatni qanday o'qish kerak. Manba — curriculum/pasport.py.
function pasportSection(content, num){
  const u = content && content.ulanish;
  if (!u || !u.length) return '';
  const bor = u.filter(b => (b.tasnif && b.tasnif.length) || (b.ishlash && b.ishlash.length));
  if (!bor.length) return '';

  const guruh = (nom, arr)=> (arr && arr.length)
    ? `<div class="pas-h">${nom}</div><ul>${arr.map(p=>li(p)).join('')}</ul>` : '';

  const bloklar = bor.map((b, i)=>`
    <div class="subhead">${parseInt(num,10)}.${i+1}. ${esc(b.nom)}</div>
    ${guruh("Texnik tasnif", b.tasnif)}
    ${guruh("Ichida nima sodir bo'ladi", b.ishlash)}
    ${guruh("Qiymatni qanday o'qiladi", b.oqish)}
    ${(b.qollash && b.qollash.length)
        ? `<div class="pas-h">Hayotda qayerda uchraydi</div>
           <div class="chips">${b.qollash.map(q=>`<span class="chip">${esc(q)}</span>`).join('')}</div>`
        : ''}`).join('');

  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>Komponent pasporti — to'liq texnik ma'lumot</h2>
      ${bloklar}
    </div>`;
}

// Ishlaydigan kod namunasi. O'qituvchi doskaga chiqaradi yoki ko'chirib beradi.
function kodSection(content, num){
  const manba = [];
  if (content && content.kod) manba.push({nom: content.kod.nom || 'Dars kodi',
                                          kod: content.kod.matn, izoh: content.kod.izoh});
  const u = (content && content.ulanish) || [];
  u.forEach(b=>{ if (b.kod) manba.push({nom: b.nom, kod: b.kod}); });
  if (!manba.length) return '';

  const bloklar = manba.map((m, i)=>`
    <div class="subhead">${parseInt(num,10)}.${i+1}. ${esc(m.nom)}</div>
    ${m.izoh ? `<ul>${li(m.izoh)}</ul>` : ''}
    <div class="kod-wrap"><pre class="kod"><code>${esc(m.kod)}</code></pre></div>`).join('');

  return `
    <div class="section">
      <div class="section-num">${num}</div>
      <h2>Tayyor kod namunasi</h2>
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
    push(k=> qollanmaSection(content, k));
    push(k=> mezonSection(content, k));
    push(k=> pasportSection(content, k));
    push(k=> ulanishSection(content, k));
    push(k=> kodSection(content, k));
  }
  push(k=> instructionSection(l, k));
  return parts.join('');
}

// Yo'l ko'rsatkich: Fan › yil › sinf › chorak. Fan nomi bosilsa fanlar ro'yxatiga qaytadi.
function crumbs(key){
  const p = String(key || '').split('|');
  const fan = activeFan ? fanTopilsin(activeFan) : null;
  const qismlar = [
    `<a data-home="1">${esc(fan ? fan.nom : 'Fanlar')}</a>`,
    esc(p[0] || ''), esc(p[1] || ''), esc(p[2] || '')
  ].filter(Boolean);
  return `<div class="crumbs">${qismlar.join('<span class="sep">›</span>')}</div>`;
}

function selectLesson(l, key, itemEl){
  activeKey = key;
  activeSinf = key.split('|').slice(0, 2).join('|');   // sinf sahifasiga qaytish uchun
  document.querySelectorAll('.dars-item.active').forEach(e=>e.classList.remove('active'));
  if (itemEl) itemEl.classList.add('active');
  if (isMobile()) setNav(false);   // telefonda dars tanlangach panel yopiladi

  const main = document.getElementById('mainContent');
  const content = LESSON_CONTENT[key];
  const bosh = `
      ${crumbs(key)}
      <div class="lesson-header">
        <div class="badge-row">
          <span class="type-badge ${l.type}">${TYPE_LABELS[l.type]||l.type}</span>
          <button class="print-btn" type="button" onclick="window.print()">⎙ Chop etish</button>
        </div>
        <div class="lesson-title">${esc(l.title)}</div>
        ${l.model ? `<div class="lesson-model">▸ ${modelLabel(key)}${esc(l.model)}</div>` : ''}
      </div>`;

  if (!content){
    main.innerHTML = `<div class="lesson-wrap">
      ${bosh}
      <div class="not-ready">
        <div class="tag">TAYYORLANMOQDA</div>
        <p>Bu darsning to'liq ishlanmasi (maqsad, lug'at, nazariya, amaliyot, uyga vazifa) hali tayyorlanmagan.<br>
        Iltimos, boshqa darsni tanlang.</p>
      </div>
      ${extraSections(l, null)}</div>`;
    initGallery();
    main.scrollTop = 0;
    marshrutYoz();
    return;
  }

  const m = content.meta;
  main.innerHTML = `<div class="lesson-wrap">
    ${bosh}

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
      ${content.nazariya.map(sec=>`<div class="subhead">${esc(sec.title)}</div><ul>${sec.points.map(p=>li(p)).join('')}</ul>`).join('')}
    </div>

    <div class="section">
      <div class="section-num">06</div>
      <h2>Sinfda bajariladigan amaliy ishlar</h2>
      ${content.amaliy.map(sec=>`<div class="subhead">${esc(sec.title)}</div><ul>${sec.points.map(p=>li(p)).join('')}</ul>`).join('')}
    </div>

    <div class="section">
      <div class="section-num">07</div>
      <h2>Uyga vazifalar</h2>
      <ol>${content.uyga.map(t=>`<li>${esc(t)}</li>`).join('')}</ol>
    </div>

    ${extraSections(l, content)}
  </div>`;
  initGallery();
  main.scrollTop = 0;
  marshrutYoz();
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

/* --- Fan tanlash: bosh sahifadagi kartochkalar, sarlavhadagi logotip va yorliq ---
   Kartochkalar har safar qaytadan chiziladi, shuning uchun hodisa main ga
   biriktiriladi (delegatsiya) — har bir tugmaga alohida ulash shart emas. */
document.getElementById('mainContent').addEventListener('click', (e)=>{
  const home = e.target.closest('[data-home]');
  if (home){ fanlarga(); return; }
  const kart = e.target.closest('[data-fan]');
  if (kart){ fanOch(kart.dataset.fan); }
});
document.getElementById('brandHome').addEventListener('click', fanlarga);
document.getElementById('fanPill').addEventListener('click', fanlarga);

// Brauzerning "orqaga" tugmasi va tashqaridan kelgan havola
window.addEventListener('hashchange', ()=>{
  if (hashOzimYozdim) return;
  const m = marshrutOqi();
  activeFan = m.fan;
  activeKey = m.key;
  activeSinf = m.key ? m.key.split('|').slice(0, 2).join('|') : m.sinf;
  render();
});

// --- Ishga tushirish ---
const boshlangich = marshrutOqi();
activeFan = boshlangich.fan && fanTopilsin(boshlangich.fan) ? boshlangich.fan : null;
activeKey = activeFan ? boshlangich.key : null;
activeSinf = activeFan
  ? (activeKey ? activeKey.split('|').slice(0, 2).join('|') : boshlangich.sinf)
  : null;
countAll();
render();
syncHeaderHeight();
// Shriftlar yuklangach sarlavha balandligi biroz o'zgarishi mumkin
if (document.fonts && document.fonts.ready) document.fonts.ready.then(syncHeaderHeight);
