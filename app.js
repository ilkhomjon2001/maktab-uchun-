const TYPE_LABELS = {qurish:"Qurish", nazorat:"Nazorat / Musobaqa", loyiha:"Loyiha", dasturlash:"Dasturlash", spike:"SPIKE"};
let activeYil = "1-yil";
let activeKey = null;

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

function selectLesson(l, key, itemEl){
  activeKey = key;
  document.querySelectorAll('.dars-item.active').forEach(e=>e.classList.remove('active'));
  if (itemEl) itemEl.classList.add('active');

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
        Hozircha 5 ta namunaviy dars to'liq ishlangan — chapdagi ● belgili darslarni ko'ring.</p>
      </div>`;
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
  `;
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
});

renderTree();
countAll();
