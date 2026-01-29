from pathlib import Path
from PIL import Image
from step_1_1 import IN_DIR,OUT_DIR
from step_2_2 import OUT_2_2_PNG

OUT_3_2 = OUT_DIR / f"{Path(__file__).stem}.png"

if __name__ == "__main__" : 
    qr = Image.open(OUT_2_2_PNG).convert("RGBA")
    width_qr,height_qr = qr.size
    icon = Image.open(IN_DIR/"phone.png")
    width_icon = int(width_qr*0.2)
    height_icon = int(height_qr*0.2)
    icon_resize = icon.resize((width_icon,height_icon))

    pad = 50
    icon_x = width_qr - width_icon - pad
    icon_y = height_qr - height_icon - pad

    qr.paste(icon_resize,box=(icon_x,icon_y),mask = icon_resize)
    qr.save(OUT_3_2)