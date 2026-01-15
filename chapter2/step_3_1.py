import pandas as pd
from step_2_2 import OUT_2_2

df_raw = pd.read_excel(OUT_2_2)
df_pivot_1 = pd.pivot_table(df_raw,index="분류",values="사용금액",aggfunc="sum")

df_raw["거래연월"] = df_raw["거래일시"].str.slice(0,7)

df_pivot_2 = pd.pivot_table(df_raw,index="분류",columns="거래연월",values="사용금액",aggfunc="sum")
df_pivot_2["누적금액"] = df_pivot_2.sum(axis=1)

df_sort = df_pivot_2.sort_values("누적금액",ascending=False)

df_reindex = df_sort.reset_index()