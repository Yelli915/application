from PIL import Image,ImageDraw
from step_1_1 import IMG_DIR

img = Image.open(IMG_DIR/"img_001.jpg")

draw = ImageDraw.Draw(img)
draw.text(xy=(10,100),text="Hello World!",fill=(255,255,255),font_size=100,)
img.show()