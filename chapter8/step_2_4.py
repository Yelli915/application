import time
from pathlib import Path
import pandas as pd
from step_1_1 import OUT_DIR
from step_2_2 import OUT_2_2
from step_2_3 import OUT_2_3

OUT_2_4 = OUT_DIR / f"{Path(__file__).stem}.csv"

def comp_lev_to_csv() :
    df_kwd = pd.read_csv(OUT_2_2)
    df_shop = pd.read_csv(OUT_2_3)
    df_merged = pd.merge(df_kwd,df_shop,left_on="키워드",right_on ="키워드")
    df_merged["경쟁강도"] = (df_merged["상품수"]/df_merged["검색수M"]).round(6)
    df_filtered = df_merged.filter(["키워드","검색수M","클릭수M","클릭률M","상품수","경쟁강도"])
    df_sorted = df_filtered.sort_values("경쟁강도",ascending=False)
    df_sorted.to_csv(OUT_2_4, index=False)

if __name__ == "__main__" :
    comp_lev_to_csv()