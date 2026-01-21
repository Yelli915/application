import vobject
from pathlib import Path
from step_1_1 import OUT_DIR
import qrcode

vcard = vobject.vCard()
fn = vcard.add("FN")
fn.value = "혼자 만들며 배우는 파이썬"
name = vcard.add("N")
name.value = vobject.vcard.Name(family="혼자 만들며 배우는",given="파이썬")
tel_call = vcard.add("TEL")
tel_call.value = "+82(10)1234-5678"
tel_call.type_param = "CELL"

tel_work = vcard.add("TEL")
tel_work.value = "+82(2)1234-5678"
tel_work.type_param = "WORK"

email = vcard.add("EMAIL")
email.value = "email@example.com"
email.type_param = "WORK"
title = vcard.add("TITLE")
title.value = "programmer"

org = vcard.add("ORG")
org.value = ["(직장) 종로구청","(부서)디지털행정팀"]

url = vcard.add("URL")
url.value = "https://data.seoul.go.kr/SeoulRtd/list"

with open(OUT_DIR/f"{Path(__file__).stem}.vcf","w",encoding="utf-8") as fp :
    fp.write(vcard.serialize())

qr = qrcode.make(vcard.serialize())
qr.save(OUT_DIR/f"{Path(__file__).stem}.png")