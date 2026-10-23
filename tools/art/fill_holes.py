"""Rellena los agujeros transparentes encerrados dentro de un PNG recortado.

Uso: python -I fill_holes.py <entrada.png> <salida.png> [r,g,b]
Los píxeles transparentes conectados al borde de la imagen quedan transparentes;
los que quedan encerrados (agujeros) se pintan opacos con el color dado.
"""
import sys
from PIL import Image, ImageDraw

src, dst = sys.argv[1], sys.argv[2]
color = tuple(int(v) for v in (sys.argv[3] if len(sys.argv) > 3 else "26,20,24").split(","))
im = Image.open(src).convert("RGBA")
w, h = im.size
alpha = im.split()[-1]
# máscara: 255 = transparente, 0 = opaco; con un marco transparente de 1 px
mask = Image.new("L", (w + 2, h + 2), 255)
mask.paste(alpha.point(lambda a: 255 if a < 128 else 0), (1, 1))
ImageDraw.floodfill(mask, (0, 0), 128)  # todo lo transparente conectado al exterior
holes = mask.crop((1, 1, w + 1, h + 1)).point(lambda v: 255 if v == 255 else 0)
fill = Image.new("RGBA", (w, h), (*color, 255))
out = im.copy()
out.paste(fill, (0, 0), holes)
out.save(dst)
print(f"agujeros rellenados: {sum(1 for v in holes.get_flattened_data() if v)} px")
