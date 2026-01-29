from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from step_1_1 import IN_DIR, OUT_DIR
from step_3_2 import OUT_3_2

img_raw = Image.open(OUT_3_2)
text = "2026년의 삿포로, 그 멋진 순간들"
font = ImageFont.truetype(IN_DIR / "malgun.ttf",size=100)
left, top, right, bottom = font.getbbox(text)

pad = 20
bg_width = pad + right + pad
bg_height = pad + bottom + pad

img_bg = Image.new("RGBA",size=img_raw.size)
draw_bg = ImageDraw.Draw(img_bg)
draw_bg.rectangle(xy=(0,0,bg_width,bg_height),fill=(0,0,0,200))

img_final = Image.alpha_composite(img_raw.convert("RGBA"),img_bg)
draw_final = ImageDraw.Draw(img_final)
draw_final.text(xy=(pad,pad),text=text, fill=(255,255,255),font=font)

img_final.convert("RGB").save(OUT_DIR/f"{Path(__file__).stem}.jpg")