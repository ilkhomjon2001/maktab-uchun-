# Robbit Academy — Robototexnika Dars Rejalari

Robbit Academy uchun 0-4-sinf robototexnika va IT dasturi bo'yicha to'liq dars rejalari bazasi.

## Tarkib
- `index.html` — asosiy sayt
- `app.js` — sayt logikasi (navigatsiya, qidiruv)
- `tree_data.js` — barcha 878 ta darsning tuzilishi (sinf/yil/chorak)
- `sample_lessons.js` — 878 ta to'liq dars rejasi
- `instructions/makerzoid/` — qurish instruksiyalari rasmlari (241 model, 16 681 WebP)
- `curriculum/` — dastur va dars rejalarini generatsiya qiluvchi Python skriptlar
  (saytning bir qismi emas, faqat manba kodi)

## Qayta generatsiya qilish
Shu papkadan turib:
```
python curriculum/generate_lessons.py      # sample_lessons.js ni qayta yozadi
python curriculum/build_instructions.py --all --dry-run
```

## Lokal ishga tushirish
`index.html` faylini istalgan brauzerda oching (internet aloqasi shrift yuklash uchun kerak).

## Serverga joylash

Jonli sayt: http://169.58.130.201:8081
Docker `nginx:alpine`, `/opt/robbit-academy` papkasi bind-mount qilingan va o'sha papkaning
o'zi shu reponing git ishchi nusxasi.

Yangilash:
1. Lokalda o'zgarishlarni commit qilib, `master` ga push qiling
2. Serverda:
   ```
   cd /opt/robbit-academy && git pull
   ```

Nginx statik fayllarni to'g'ridan-to'g'ri o'qiydi — konteynerni qayta ishga tushirish shart emas.
Eski nusxa: `/opt/robbit-academy.bak-20260808`
