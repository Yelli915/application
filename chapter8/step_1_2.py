import json
from pathlib import Path
from datakart import Naver
from step_1_1 import OUT_DIR
from dotenv import load_dotenv
import os 
import pip_system_certs.wrapt_requests
import requests

def query_naver_shop(query:str,display:int = 1) ->dict :
    load_dotenv()
    Naver_KEY = os.environ.get("Client_ID")
    Naver_SEC = os.environ.get("Client_Secret")
    naver = Naver(Naver_KEY,Naver_SEC)
    return naver.shop(query=query, display=display)

if __name__ == "__main__" :
    query = "원피스"
    resp = query_naver_shop(query)
    # 파일 저장 코드 (주석 포함)
    with open(OUT_DIR / f"{Path(__file__).stem}.json", "w", encoding="utf-8") as fp:  # 쓰기 모드로, 파일 열기 (utf-8: 한글 깨짐 방지 및 호환성 확보)
        json.dump(resp, fp, ensure_ascii=False, indent=2)  # JSON 파일로 저장 (ensure_ascii=False: 한글을 있는 그대로 저장, indent=2: 들여쓰기)