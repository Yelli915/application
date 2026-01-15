import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from step_3_2 import OUT_3_2


df_raw = pd.read_excel(OUT_3_2)

sns.set_theme(context="poster",style="whitegrid",font="Malgun Gothic")
sns.set_style({"grid.linestyle" : "--", "grid.color" : "#EEEEEE"})

fig,ax = plt.subplots(figsize=(16,9),dpi=100)

sns.barplot(data=df_raw,x="분류",y="누적금액",hue="분류",ax=ax)
sns.despine(top=True,right=True,bottom=True,left=True)
ax.set_ylim(10000, 1000000)
fig.suptitle("분류별 누적 사용금액")
plt.show()