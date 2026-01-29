from qrcode.image.styledpil import StyledPilImage
from qrcode.main import QRCode
from step_1_1 import IN_DIR
from step_2_2 import OUT_2_2_VCF

with open(OUT_2_2_VCF,encoding="utf-8") as fp :
    vcf = fp.read()

qr = QRCode()
qr.add_data(vcf)
img = qr.make(image_factory = StyledPilImage, embeded_image_path = IN_DIR/"phone.png",)
# 삽입하는 이미지 필요해요
img