import json
from pathlib import Path
from datakart import NaverAd
from step_1_1 import OUT_DIR

from dotenv import load_dotenv
import os 
import pip_system_certs.wrapt_requests
import requests

def query_keywords_tool(keywords : str, event : int = None) -> list :
    load_dotenv()
    AD_KEY = os.environ.get("liscence")
    AD_SEC = os.environ.get("secret_key")
    AD_CUST_ID = os.environ.get("search_Client_ID")
    naver_ad = NaverAd(AD_KEY,AD_SEC,AD_CUST_ID)
    resp = naver_ad.keywords_tool(keywords=keywords,event=event,show_detail=True)
    return resp.get("keywordList",[])

if __name__ == "__main__" :
    keywords = "원피스"
    resp = query_keywords_tool(keywords)
    with open(OUT_DIR/f"{Path(__file__).stem}.json","w",encoding="utf-8") as fp :
        json.dump(resp,fp,ensure_ascii=False,indent=2)