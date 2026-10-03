"""Render Sinhala taglines to SVG outlines with the legacy font Tharu Digital Mahee.

The font is not Unicode: Sinhala glyphs sit on Latin keys (Wijesekara layout), so each line
below is the key sequence that draws it, with the real Unicode text alongside for reference.
The output SVGs are plain glyph outlines, so the website needs no font file, and the font
itself is NOT stored in this repo.

Usage:  python tools/sinhala_art.py <path-to-tharu_digital_mahee.ttf>
Writes: assets/sinhala/<name>.svg  (+ prints the aspect ratio for the CSS)
"""
import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

LINES = {
    "tagline-accounting": ("Tnf.a jsYajikSh .sKqualrK iylrqjd",          "ඔබගේ විශ්වසනීය ගිණුම්කරණ සහකරුවා"),
    "tagline-tax":        ("Tnf.a noq .eg,qjg fyd|u jsi|qu wfmka",        "ඔබගේ බදු ගැටලුවට හොඳම විසඳුම අපෙන්"),
}
SPACE = 280  # word gap, font units (1000 per em)

def main():
    ttf = sys.argv[1]
    font = TTFont(ttf); gs = font.getGlyphSet(); cmap = font.getBestCmap(); hmtx = font["hmtx"]
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "sinhala")
    os.makedirs(out_dir, exist_ok=True)
    for name, (keys, meaning) in LINES.items():
        x, placed = 0, []
        for ch in keys:
            if ch == " ":
                x += SPACE; continue
            g = cmap[ord(ch)]; placed.append((g, x)); x += hmtx[g][0]
        bp = BoundsPen(gs)
        for g, px in placed: gs[g].draw(TransformPen(bp, (1, 0, 0, -1, px, 0)))
        x0, y0, x1, y1 = bp.bounds
        pad = 20
        vb = (x0 - pad, y0 - pad, (x1 - x0) + 2 * pad, (y1 - y0) + 2 * pad)
        sp = SVGPathPen(gs)
        for g, px in placed: gs[g].draw(TransformPen(sp, (1, 0, 0, -1, px, 0)))
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]:.0f} {vb[1]:.0f} {vb[2]:.0f} {vb[3]:.0f}">'
               f'<path fill="#000" d="{sp.getCommands()}"/></svg>')
        with open(os.path.join(out_dir, name + ".svg"), "w", encoding="utf-8") as fh: fh.write(svg)
        print(f"{name}: aspect {vb[2]/vb[3]:.3f}  ({vb[2]:.0f}x{vb[3]:.0f})  {len(svg)//1024} KB  <- {meaning}")

if __name__ == "__main__":
    main()
