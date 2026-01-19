from pathlib import Path
from step_1_1 import OUT_DIR
import qrcode

data = [
    "BEGIN:VCARD", #vCard 시작
    "VERSION:3.0", #버전
    "N:혼자 만들며 배우는; 파이썬;;; ", #성;이름;미들네임;접두어;접미어
    "FN:혼자 만들며 배우는 파이썬", #전체이름
    "TEL;type=CELL:+82 10-1234-5678",
    "END:VCARD" #vCard 종료
]

vcf = "\n".join(data)
with open(OUT_DIR / f"{Path(__file__).stem}.vcf","w",encoding="utf-8") as fp :
    fp.write(vcf)

img = qrcode.make(vcf)
img