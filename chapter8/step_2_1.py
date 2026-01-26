from pathlib import Path
import pandas as pd
from step_1_1 import OUT_DIR
from step_1_3 import query_keywords_tool

OUT_2_1 = OUT_DIR / f"{Path(__file__).stem}.csv"

def rel_kwd_to_csv(keywords : str = None, event : int = None) :
    # 변수이름, 이 변수에는 문자열이 올거라는 힌트, 기본값 <- 으로 구성됨 
    resp=query_keywords_tool(keywords=keywords, event=event)
    df_raw = pd.DataFrame(resp)
    df_raw.columns = ["키워드","검색수PC","검색수M","클릭수PC","클릭수M","클릭률PC","클릭률M","광고수","경쟁정도"]
    df_raw.to_csv(OUT_2_1,index=False)

if __name__ == "__main__" :
    rel_kwd_to_csv("나이키")