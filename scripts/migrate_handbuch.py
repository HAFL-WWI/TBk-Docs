# -*- coding: utf-8 -*-
"""Migrate TBk Handbuch (docx) chapters into MkDocs markdown, DE + FR."""
import docx
import os
import re
from docx.oxml.ns import qn

R_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
BLIP = qn("a:blip")
HYPERLINK = qn("w:hyperlink")

DOCX_DE = r"C:\Users\hbh1\Projects\H07_TBk\01_TBk\Dokumentation\Handbuch\TBk_Manuel_V11_DE.docx"
DOCX_FR = r"C:\Users\hbh1\Projects\H07_TBk\01_TBk\Dokumentation\Handbuch\TBk_Manuel_V11_FR.docx"
DOCS = r"C:\Users\hbh1\Projects\H07_TBk\01_TBk\Dokumentation\Mkdocs\docs"

IMG_COUNTER = {}  # per-chapter-slug counter, DE pass only


def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def iter_body_items(document):
    para_by_elem = {id(p._p): p for p in document.paragraphs}
    table_by_elem = {id(t._tbl): t for t in document.tables}
    for child in document.element.body.iterchildren():
        tag = child.tag.split("}")[-1]
        if tag == "p":
            p = para_by_elem.get(id(child))
            if p is not None:
                yield ("p", p)
        elif tag == "tbl":
            t = table_by_elem.get(id(child))
            if t is not None:
                yield ("tbl", t)


WEBSAFE_EXTS = {"png", "jpg", "jpeg", "gif", "bmp", "svg", "webp"}


def para_images(document, p, chapter_slug, extract):
    """Return list of markdown strings (image tag or a not-web-safe note) for all blips in this paragraph."""
    out = []
    for blip in p._p.findall(".//" + BLIP):
        path, ext = embed_image(document, blip, chapter_slug, extract)
        if ext not in WEBSAFE_EXTS:
            out.append(f'!!! warning "Grafik nicht migriert"\n    Bild im Format `.{ext}` (Vektorgrafik aus Word, z.B. WordArt/Clipart) wird von Browsern nicht dargestellt und wurde nicht automatisch konvertiert. Original-Datei liegt unter `{path}`.')
        else:
            out.append(f"![Abbildung]({path})")
    return out


def embed_image(document, blip_el, chapter_slug, extract):
    rid = blip_el.get(R_NS + "embed")
    part = document.part.related_parts[rid]
    IMG_COUNTER[chapter_slug] = IMG_COUNTER.get(chapter_slug, 0) + 1
    n = IMG_COUNTER[chapter_slug]
    # use partname extension directly - part.image.ext fails on EMF/WMF (format sniffing)
    ext = part.partname.ext.lstrip(".").lower()
    fname = f"img-{n}.{ext}"
    rel_path = f"assets/img/{chapter_slug}/{fname}"
    if extract:
        img_dir = os.path.join(DOCS, "assets", "img", chapter_slug)
        os.makedirs(img_dir, exist_ok=True)
        with open(os.path.join(img_dir, fname), "wb") as f:
            f.write(part.blob)
    return rel_path, ext


def cell_hyperlink(document, cell):
    h = cell._tc.find(".//" + HYPERLINK)
    if h is not None:
        rid = h.get(qn("r:id"))
        rel = document.part.rels.get(rid)
        if rel is not None:
            return rel.target_ref
    return None


def render_table(document, table, chapter_slug, extract):
    rows_md = []
    ncols = len(table.columns)
    for r in table.rows:
        cells_md = []
        for c in r.cells:
            parts = []
            text = c.text.strip().replace("\n", "<br>")
            link = cell_hyperlink(document, c)
            imgs = c._tc.findall(".//" + BLIP)
            for blip in imgs:
                img_path, ext = embed_image(document, blip, chapter_slug, extract)
                if ext not in WEBSAFE_EXTS:
                    parts.append(f"*(Grafik `.{ext}` nicht darstellbar)*")
                else:
                    parts.append(f"![]({img_path})")
            if link:
                label = text if text and text != ">" and "link" not in text.lower() else "Video ansehen"
                parts.append(f"[{label} \u2197]({link})")
            elif text:
                parts.append(text)
            cells_md.append(" ".join(parts) if parts else "")
        rows_md.append(cells_md)
    if not rows_md:
        return ""
    header = rows_md[0]
    body_rows = rows_md[1:]
    lines = []
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * ncols) + " |")
    for row in body_rows:
        row = row + [""] * (ncols - len(row))
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def render_items(document, items, chapter_slug, extract, base_heading_level=1):
    """items: list of ('p', Paragraph) | ('tbl', Table). Returns list of markdown lines."""
    lines = []
    i = 0
    while i < len(items):
        kind, obj = items[i]
        if kind == "tbl":
            lines.append(render_table(document, obj, chapter_slug, extract))
            lines.append("")
            i += 1
            continue
        # paragraph
        style = obj.style.name
        text = obj.text.strip()
        imgs = para_images(document, obj, chapter_slug, extract)

        if style.startswith("Heading"):
            level = int(style.split()[-1])
            # re-level relative to base_heading_level (page's own H1)
            md_level = min(level - 1 + base_heading_level, 6)
            if text:
                lines.append("#" * md_level + " " + text)
                lines.append("")
            i += 1
            continue

        if imgs:
            for img in imgs:
                lines.append(img)
                lines.append("")
            if text:
                lines.append(f"*{text}*")
                lines.append("")
            i += 1
            continue

        if not text:
            i += 1
            continue

        if style == "List Paragraph":
            flat = " ".join(line.strip() for line in text.split("\n") if line.strip())
            lines.append(f"- {flat}")
        else:
            lines.append(text)
        lines.append("")
        i += 1
    return lines


def write_md(path, title, body_lines, note=None):
    lines = [f"# {title}", ""]
    if note:
        lines.append(f'!!! info "{note[0]}"')
        lines.append(f"    {note[1]}")
        lines.append("")
    lines.extend(body_lines)
    content = "\n".join(lines).rstrip() + "\n"

    # fix relative image paths for pages nested in subfolders (e.g. tbk-karten/grundlagen.md
    # needs "../assets/..." since "assets/..." would resolve relative to tbk-karten/)
    rel_dir = os.path.relpath(os.path.dirname(path), DOCS)
    depth = 0 if rel_dir == "." else rel_dir.count(os.sep) + 1
    if depth:
        content = content.replace("](assets/img/", "](" + "../" * depth + "assets/img/")

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def get_h1_sections(document):
    """Split body items into a list of (heading_text, items[]) per top-level H1 chapter (Glossar excluded, handled separately below via same generic mechanism actually included)."""
    sections = []
    current_title = None
    current_items = []
    for kind, obj in iter_body_items(document):
        if kind == "p" and obj.style.name == "Heading 1":
            if current_title is not None:
                sections.append((current_title, current_items))
            current_title = obj.text.strip()
            current_items = []
        else:
            if current_title is not None:
                current_items.append((kind, obj))
    if current_title is not None:
        sections.append((current_title, current_items))
    return sections


def split_by_h2(items):
    """Split a list of body items (within one H1) into sub-sections by Heading 2."""
    subs = []
    current_title = None
    current_items = []
    for kind, obj in items:
        if kind == "p" and obj.style.name == "Heading 2":
            if current_title is not None:
                subs.append((current_title, current_items))
            elif current_items:
                subs.append((None, current_items))  # intro before first h2
            current_title = obj.text.strip()
            current_items = []
        else:
            current_items.append((kind, obj))
    if current_title is not None or current_items:
        subs.append((current_title, current_items))
    return subs


def process(document, lang, extract_images):
    IMG_COUNTER.clear()
    sections = get_h1_sections(document)
    # sections[0] = Glossar, [1] = Einfuehrung, [2] = TBk-Karten, [3] = Abgrenzung,
    # [4] = Datenquellen, [5..7] = 3x Anhang
    assert len(sections) == 8, f"expected 8 H1 sections, got {len(sections)}: {[s[0] for s in sections]}"

    suffix = "" if lang == "de" else f".{lang}"

    def out(rel):
        base, ext = os.path.splitext(rel)
        return os.path.join(DOCS, base + suffix + ext)

    # --- 0: Glossar ---
    title, items = sections[0]
    lines = render_items(document, items, "glossar", extract_images)
    write_md(out("glossar.md"), title, lines)

    # --- 1: Einfuehrung ---
    title, items = sections[1]
    lines = render_items(document, items, "einfuehrung", extract_images)
    write_md(out("einfuehrung.md"), title, lines)

    # --- 2: TBk-Karten -> 4 files by H2 ---
    _, items = sections[2]
    subs = split_by_h2(items)
    targets = ["tbk-karten/grundlagen.md", "tbk-karten/veraenderungen-oberschicht.md",
               "tbk-karten/vertikale-struktur.md", "tbk-karten/zusatzinfos.md"]
    slugs = ["tbk-karten-grundlagen", "tbk-karten-veraenderungen", "tbk-karten-vertikale-struktur", "tbk-karten-zusatzinfos"]
    subs = [s for s in subs if s[0] is not None]
    assert len(subs) == len(targets), f"TBk-Karten: expected {len(targets)} H2 subs, got {len(subs)}"
    for (h2title, h2items), target, slug in zip(subs, targets, slugs):
        lines = render_items(document, h2items, slug, extract_images)
        write_md(out(target), h2title, lines)

    # --- 3: Abgrenzung -> 3 files by H2 ---
    _, items = sections[3]
    subs = split_by_h2(items)
    subs = [s for s in subs if s[0] is not None]
    targets = ["abgrenzung-beschreibung/grundprinzipien.md",
               "abgrenzung-beschreibung/funktionsweise.md",
               "abgrenzung-beschreibung/darstellung.md"]
    slugs = ["abgrenzung-grundprinzipien", "abgrenzung-funktionsweise", "abgrenzung-darstellung"]
    assert len(subs) == len(targets), f"Abgrenzung: expected {len(targets)} H2 subs, got {len(subs)}"
    for (h2title, h2items), target, slug in zip(subs, targets, slugs):
        lines = render_items(document, h2items, slug, extract_images)
        write_md(out(target), h2title, lines)

    # --- 4: Datenquellen -> 2 files by H2 ---
    _, items = sections[4]
    subs = split_by_h2(items)
    subs = [s for s in subs if s[0] is not None]
    targets = ["datenquellen/vhm.md", "datenquellen/wichtigste-quellen.md"]
    slugs = ["datenquellen-vhm", "datenquellen-quellen"]
    assert len(subs) == len(targets), f"Datenquellen: expected {len(targets)} H2 subs, got {len(subs)}"
    for (h2title, h2items), target, slug in zip(subs, targets, slugs):
        lines = render_items(document, h2items, slug, extract_images)
        write_md(out(target), h2title, lines)

    # --- 5,6,7: Anhang x3, each its own H1 ---
    anhang_targets = ["anhang/videos.md", "anhang/entwicklungsstufen.md", "anhang/vorratsschaetzung.md"]
    anhang_slugs = ["anhang-videos", "anhang-entwicklungsstufen", "anhang-vorratsschaetzung"]
    for idx, target, slug in zip([5, 6, 7], anhang_targets, anhang_slugs):
        title, items = sections[idx]
        lines = render_items(document, items, slug, extract_images)
        write_md(out(target), title, lines)

    print(f"[{lang}] done, {len(sections)} H1 sections processed")
    return dict(IMG_COUNTER)


if __name__ == "__main__":
    d_de = docx.Document(DOCX_DE)
    de_counts = process(d_de, "de", extract_images=True)

    d_fr = docx.Document(DOCX_FR)
    fr_counts = process(d_fr, "fr", extract_images=False)

    print("\n--- image count comparison (DE vs FR) per chapter slug ---")
    all_slugs = sorted(set(de_counts) | set(fr_counts))
    mismatches = []
    for slug in all_slugs:
        de_n = de_counts.get(slug, 0)
        fr_n = fr_counts.get(slug, 0)
        flag = "  <-- MISMATCH" if de_n != fr_n else ""
        if flag:
            mismatches.append(slug)
        print(f"{slug:35s} DE={de_n:3d}  FR={fr_n:3d}{flag}")
    if mismatches:
        print("\nWARNING: mismatched chapters, FR image references will be WRONG for:", mismatches)
    else:
        print("\nAll chapters match - FR image references reused from DE are safe.")

    # --- known fix: DE docx is missing "Abb. 4.2" image in datenquellen-vhm (source content gap) ---
    # FR docx *does* have the equivalent Fig. 4.2 image - borrow it for both DE and (already-correct) FR page.
    fr_vhm_p = d_fr.paragraphs[227]
    blip = fr_vhm_p._p.findall(".//" + BLIP)[0]
    rid = blip.get(R_NS + "embed")
    part = d_fr.part.related_parts[rid]
    ext = part.partname.ext.lstrip(".").lower()
    img_dir = os.path.join(DOCS, "assets", "img", "datenquellen-vhm")
    os.makedirs(img_dir, exist_ok=True)
    with open(os.path.join(img_dir, f"img-2.{ext}"), "wb") as f:
        f.write(part.blob)

    vhm_md_path = os.path.join(DOCS, "datenquellen", "vhm.md")
    with open(vhm_md_path, encoding="utf-8") as f:
        content = f.read()
    caption_marker = "Abb. 4.2 TBk-Bestandeskarten generiert"
    if caption_marker in content and f"img-2.{ext}" not in content:
        content = content.replace(
            caption_marker,
            f"![Abbildung](../assets/img/datenquellen-vhm/img-2.{ext})\n\n" + caption_marker,
        )
        content = content.rstrip("\n") + (
            "\n\n"
            '!!! note "Migrations-Hinweis"\n'
            f"    Diese Abbildung fehlt im Original-Handbuch `TBk_Manuel_V11_DE.docx` (Bild nicht eingebettet, nur die Bildunterschrift ist vorhanden) und wurde stattdessen aus der französischen Fassung (`TBk_Manuel_V11_FR.docx`, Fig. 4.2) übernommen. Lohnt sich, im Original-docx zu ergänzen.\n"
        )
        with open(vhm_md_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("\nApplied known fix: borrowed FR Fig. 4.2 image for DE datenquellen-vhm (source docx gap).")

    # --- known fix: glossary table has an empty header row in the source docx ---
    for md_file, header in [("glossar.md", "| Begriff | Definition |"),
                             ("glossar.fr.md", "| Terme | Définition |")]:
        p = os.path.join(DOCS, md_file)
        with open(p, encoding="utf-8") as f:
            content = f.read()
        content = content.replace("|  |  |\n| --- | --- |", f"{header}\n| --- | --- |", 1)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
    print("Applied known fix: added glossary table header (DE+FR).")
