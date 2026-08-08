# -*- coding: utf-8 -*-
"""
Makerzoid qurish instruksiyalarini zipdan chiqarib, veb uchun siqadi.

  zip: .../<bo'lim>/<N>.<Model>/<qadam>.png   (2133x1200 PNG, ~190 KB)
  ->   site/instructions/makerzoid/<slug>/001.webp ... (max 1100 px, WebP q82, ~15 KB)

Bir vaqtning o'zida bitta sinf ustida ishlash uchun mo'ljallangan (foydalanuvchi
talabi: "1-yil 1-sinf tugagandan keyin keyingi sinfga o't").

Ishlatish:
  python build_instructions.py --yil 1-yil --sinf 0-sinf
  python build_instructions.py --all
  python build_instructions.py --yil 1-yil --sinf 0-sinf --dry-run

Allaqachon chiqarilgan modellar qayta ishlanmaydi (--force bilan majburlash mumkin).
"""

import argparse
import io
import json
import os
import re
import sys
import zipfile
from concurrent.futures import ProcessPoolExecutor

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from instructions_map import scan_zips, build_map, slug  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
# curriculum/ sayt repo'sining ichida yotadi, shuning uchun sayt ildizi = ota-papka
SITE = os.path.dirname(HERE)
TREE = os.path.join(SITE, "tree_data.js")
OUT_ROOT = os.path.join(SITE, "instructions", "makerzoid")
INDEX_JS = os.path.join(SITE, "instructions_index.js")

# Rasm avval bo'sh chetlaridan qirqiladi (yuza ~45% ga tushadi), shuning uchun
# 900 px qirqilgan rasm 1100 px qirqilmagan rasmdan ANIQROQ ko'rinadi.
MAX_PX = 900       # uzun tomoni bo'yicha eng katta o'lcham
QUALITY = 80       # WebP sifati — detal raqamlari va "x1" belgilar o'qilarli qoladi
MANBA = "Makerzoid Robot Master (PM)"


def load_tree():
    with io.open(TREE, encoding="utf-8") as f:
        c = f.read().replace("window.TREE_DATA = ", "", 1).rstrip(";\n \t\r")
    return json.loads(c)


def models_for(yil=None, sinf=None):
    """Berilgan yil/sinfda ishlatiladigan modellar (tartib bilan, takrorsiz)."""
    tree = load_tree()
    seen, out = set(), []
    for y, grades in tree.items():
        if yil and y != yil:
            continue
        for s, choraks in grades.items():
            if sinf and s != sinf:
                continue
            for _, lessons in choraks.items():
                for l in lessons:
                    if l["type"] == "qurish" and l.get("model") and l["model"] not in seen:
                        seen.add(l["model"])
                        out.append(l["model"])
    return out


def _open(zp, entry):
    with zipfile.ZipFile(zp) as z, z.open(entry) as fh:
        return Image.open(io.BytesIO(fh.read()))


def _content_bbox(im):
    """Rasmning bo'sh (shaffof yoki oq) chetlarisiz chegarasi."""
    if im.mode in ("RGBA", "LA"):
        bb = im.getbbox()
        if bb:
            return bb
    g = im.convert("L")
    return g.point(lambda p: 255 if p < 250 else 0).getbbox()


def _bbox_job(job):
    """(model, zip, entry) -> (model, bbox|None)"""
    model, zp, entry = job
    try:
        return model, _content_bbox(_open(zp, entry))
    except Exception:                            # noqa: BLE001
        return model, None


def _convert(job):
    """(zip, entry, chiqish_fayli, crop) -> (ok, bayt)"""
    zp, entry, dest, crop = job
    try:
        im = _open(zp, entry)
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[3])
            im = bg
        else:
            im = im.convert("RGB")
        if crop:
            im = im.crop(crop)
        im.thumbnail((MAX_PX, MAX_PX), Image.LANCZOS)
        im.save(dest, "WEBP", quality=QUALITY, method=5)
        return True, os.path.getsize(dest)
    except Exception as e:                      # noqa: BLE001
        return False, "%s: %s" % (entry, e)


def _union_boxes(zf, mapping, models, workers):
    """Har bir model uchun BARCHA qadamlarning umumiy chegarasi.

    Qadamlar alohida-alohida qirqilsa, model qadamdan qadamga kattalashib-kichrayib
    ko'rinadi va masshtab hissi yo'qoladi — shuning uchun bitta umumiy chegara olinadi.
    """
    jobs = []
    for model in models:
        key = mapping.get(model)
        if not key:
            continue
        for st in sorted(zf[key]["files"]):
            zp, entry, _ = zf[key]["files"][st]
            jobs.append((model, zp, entry))
    if not jobs:
        return {}
    print("  chegaralar hisoblanmoqda (%d rasm)..." % len(jobs))
    union = {}
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for model, bb in ex.map(_bbox_job, jobs, chunksize=8):
            if not bb:
                continue
            u = union.get(model)
            union[model] = bb if u is None else (min(u[0], bb[0]), min(u[1], bb[1]),
                                                 max(u[2], bb[2]), max(u[3], bb[3]))
    # kichik hoshiya qo'shamiz, aks holda model ramkaga tegib turadi
    out = {}
    for model, (x1, y1, x2, y2) in union.items():
        key = mapping[model]
        st = sorted(zf[key]["files"])[0]
        with zipfile.ZipFile(zf[key]["files"][st][0]) as z:
            with z.open(zf[key]["files"][st][1]) as fh:
                w, h = Image.open(io.BytesIO(fh.read())).size
        px = max(8, int((x2 - x1) * 0.015))
        py = max(8, int((y2 - y1) * 0.015))
        out[model] = (max(0, x1 - px), max(0, y1 - py), min(w, x2 + px), min(h, y2 + py))
    return out


def load_index():
    if not os.path.exists(INDEX_JS):
        return {}
    with io.open(INDEX_JS, encoding="utf-8") as f:
        c = f.read()
    m = re.search(r"window\.INSTRUCTION_INDEX\s*=\s*(\{.*\});", c, re.S)
    return json.loads(m.group(1)) if m else {}


def save_index(idx):
    header = (
        "/*\n"
        " * Makerzoid qurish instruksiyalari ko'rsatkichi — AVTOMATIK YARATILADI.\n"
        " * Qo'lda tahrirlamang: curriculum/build_instructions.py qayta yozadi.\n"
        " *\n"
        " * Rasmlar: site/instructions/makerzoid/<slug>/001.webp ... <qadam>.webp\n"
        " * Manba:   Robot master(PM) instruction (Makerzoid rasmiy to'plami)\n"
        " */\n"
        "window.INSTRUCTION_INDEX = "
    )
    with io.open(INDEX_JS, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(json.dumps(idx, ensure_ascii=False, indent=1, sort_keys=True))
        f.write(";\n")


def export(models, zf, mapping, force=False, dry=False, workers=6):
    idx = load_index()
    jobs, planned = [], []

    for model in models:
        key = mapping.get(model)
        if not key:
            print("  [!] moslik yo'q:", model)
            continue
        steps = sorted(zf[key]["files"])
        if not steps:
            print("  [!] bo'sh papka:", model, "->", key)
            continue
        sl = slug(model)
        dest_dir = os.path.join(OUT_ROOT, sl)
        have = idx.get(model)
        if have and have.get("qadam") == len(steps) and os.path.isdir(dest_dir) and not force:
            continue
        planned.append((model, sl, len(steps)))

    if dry:
        tot = sum(n for _, _, n in planned)
        print("  Rejalashtirilgan: %d model, %d rasm" % (len(planned), tot))
        for m, s, n in planned:
            print("     %-36s %3d qadam  -> instructions/makerzoid/%s/" % (m, n, s))
        return 0, 0

    if not planned:
        print("  Hammasi allaqachon tayyor.")
        return 0, 0

    todo = [m for m, _, _ in planned]
    boxes = _union_boxes(zf, mapping, todo, workers)

    for model, sl, _ in planned:
        key = mapping[model]
        dest_dir = os.path.join(OUT_ROOT, sl)
        os.makedirs(dest_dir, exist_ok=True)
        steps = sorted(zf[key]["files"])
        crop = boxes.get(model)
        for i, st in enumerate(steps, 1):
            zp, entry, _ = zf[key]["files"][st]
            jobs.append((zp, entry, os.path.join(dest_dir, "%03d.webp" % i), crop))
        idx[model] = {"slug": sl, "qadam": len(steps), "manba": MANBA, "zip": key}

    print("  %d model, %d rasm siqilmoqda..." % (len(planned), len(jobs)))
    ok = err = 0
    total_bytes = 0
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for i, (good, res) in enumerate(ex.map(_convert, jobs, chunksize=8), 1):
            if good:
                ok += 1
                total_bytes += res
            else:
                err += 1
                print("     XATO:", res)
            if i % 500 == 0:
                print("     ... %d / %d" % (i, len(jobs)))
    save_index(idx)
    print("  Tayyor: %d rasm, %.1f MB (%d xato)" % (ok, total_bytes / 1048576.0, err))
    return ok, total_bytes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--yil")
    ap.add_argument("--sinf")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()

    if not a.all and not (a.yil and a.sinf):
        ap.error("--yil va --sinf bering, yoki --all")

    scope = "BARCHA" if a.all else "%s / %s" % (a.yil, a.sinf)
    print("Qamrov:", scope)

    models = models_for(None if a.all else a.yil, None if a.all else a.sinf)
    print("Modellar:", len(models))

    zf = scan_zips()
    mapping, missing = build_map(zf)
    if missing:
        print("  Diqqat: %d model bog'lanmagan (instructions_map.py ga qarang)" % len(missing))

    export(models, zf, mapping, force=a.force, dry=a.dry_run, workers=a.workers)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
