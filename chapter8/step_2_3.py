import time
from pathlib import Path
import pandas as pd
from tqdm import tqdm
from step_1_1 import OUT_DIR
from step_1_2 import query_naver_shop
from step_2_2 import OUT_2_2

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.csv"

def shop_cnt_to_csv() :
    df_raw = pd.read_csv(OUT_2_2)
    kwd_list = df_raw["키워드"].to_list()
    item_cnt = []
    with tqdm(total=len(kwd_list)) as pbar :
        for kwd in kwd_list :
            resp = query_naver_shop(query=kwd)
            total = resp.get("total",0)
            item_cnt.append({"키워드":kwd,"상품수":total})
            time.sleep(0.5)
            pbar.set_description(kwd)
            pbar.update()
    df_raw = pd.DataFrame(item_cnt)
    df_raw.to_csv(OUT_2_3, index=False)

if __name__ == "__main__" :
    shop_cnt_to_csv()