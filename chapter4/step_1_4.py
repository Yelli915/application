from pathlib import Path
import qrcode
from step_1_1 import OUT_DIR

#파일로 저장하기

img_hello = qrcode.make("안녕나 큐알이에요")
img_hello.save(OUT_DIR / f"{Path(__file__).stem}_hello.png")
img_naver = qrcode.make("https://www.naver.com/")
img_naver.save(OUT_DIR / f"{Path(__file__).stem}_naver.png")

#__file__은 "진짜 파일"로 실행할 때만 생기는 변수라서, 대화형 환경에서는 사용불가
# 실행 버튼 / Interactive 창 / Jupyter (실패아님) VS Run Cell 버튼 누르기, Shift+Enter로 실행하기
# 결과: 파이썬이 "나는 지금 파일 전체를 실행하는 게 아니라, 메모리에 있는 코드 조각을 실행 중이구나"라고 생각합니다. -> __file__ (파일 경로 정보)을 만들지 않음.