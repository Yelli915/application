from pathlib import Path
from PIL import Image, ImageDraw
from step_1 import IN_DIR, OUT_DIR
from step_2_2 import read_text

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.png"
PROB = 0.75

def read_text_and_draw_line(path:Path) :
    parsed = read_text(path)
    img = Image.open(path)
    draw = ImageDraw.Draw(img,"RGB")
    for row in parsed :
        bbox, text, prob = row
        box = [(x,y) for x,y in bbox]
        draw.polygon(box,outline=(255,0,0) if prob>= PROB else(0,255,0),
        width=10,)
    img.save(OUT_2_3)

if __name__ == "__main__" :
    path = IN_DIR/"ocr.jpg"
    read_text_and_draw_line(path)