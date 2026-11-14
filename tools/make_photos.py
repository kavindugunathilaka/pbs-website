"""Create the website's photo crops from the original team photos.

The originals (2000x1125 JPGs, numbered 1-6) are kept OUTSIDE this repo, e.g. D:/VOYAGE/PBS/photos.
Usage:  python tools/make_photos.py D:/VOYAGE/PBS/photos
Writes WebP crops (and one JPG for social sharing) into assets/images/team/.

Photo guide
  1  four team members at a laptop        4  three at a laptop, one pointing
  2  the illuminated PBS sign              5  three seated + one standing
  3  the full team of nine                 6  four team members (closer shot)
"""
import os
import sys

from PIL import Image

src = sys.argv[1]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "images", "team")
os.makedirs(out, exist_ok=True)


def load(n):
    return Image.open(os.path.join(src, f"{n}.jpg")).convert("RGB")


def save(im, name, size, quality=78, fmt="WEBP"):
    im = im.resize(size, Image.LANCZOS)
    path = os.path.join(out, name)
    if fmt == "WEBP":
        im.save(path, "WEBP", quality=quality, method=6)
    else:
        im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"{name:22s} {size[0]}x{size[1]}  {os.path.getsize(path) // 1024} KB")


def crop(im, box):
    return im.crop(box)


# Home hero: photo 6, full frame for desktop, a 4:3 crop that keeps all four faces for phones
save(load(6), "hero-wide.webp", (1920, 1080), 76)
save(crop(load(6), (250, 0, 1750, 1125)), "hero-mobile.webp", (1000, 750), 76)

# "Why Panambara": photo 4, 4:5 portrait crop on the three faces
save(crop(load(4), (460, 0, 1360, 1125)), "why-arch.webp", (800, 1000), 78)

# About page: the full team (photo 3) and the sign (photo 2, cropped to the sign only,
# which also leaves the framed certificates on either side out of the picture)
save(load(3), "team-full.webp", (1600, 900), 78)
save(crop(load(2), (270, 175, 1790, 960)), "sign.webp", (1400, 723), 80)

# Page-header photo cards (16:10)
cards = {
    "card-1.webp": (1, (140, 0, 1940, 1125)),
    "card-3.webp": (3, (100, 0, 1900, 1125)),
    "card-4.webp": (4, (0, 0, 1800, 1125)),
    "card-5.webp": (5, (100, 0, 1900, 1125)),
    "card-6.webp": (6, (130, 0, 1930, 1125)),
}
for name, (n, box) in cards.items():
    save(crop(load(n), box), name, (1200, 750), 78)

# Social share image (1200x630) from photo 6
save(crop(load(6), (0, 40, 2000, 1090)), "og-share.jpg", (1200, 630), 84, fmt="JPEG")
