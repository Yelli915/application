import pandas as pd
import streamlit as st
from streamlit.column_config import NumberColumn, ProgressColumn
from step_2_4 import OUT_2_4
from step_3_1 import analyze_keywords,init_page

def print_dataframe_with_style(keywords:str=None,event:int=None) :
    if keywords or event is not None : 
        with st.spinner("waiting...") :
            analyze_keywords(keywords=keywords,event=event)
        df_result = pd.read_csv(OUT_2_4)
        max_values = df_result.max().to_dict()
        st.dataframe(df_result,use_container_width=True,hide_index=True,column_config={
            "검색수M" : ProgressColumn(width="small",max_value=max_values.get("검색수M",1),format=""),
            "클릭수M" : ProgressColumn(width="small",max_value=max_values.get("클릭수M",1),format=""),
            "클릭률M" : ProgressColumn(width="small",max_value=max_values.get("클릭률M",1),format=""),
            "상품수" : ProgressColumn(width="small",max_value=max_values.get("상품수",1),format=""),
            "경쟁강도" : ProgressColumn(width="small",max_value=max_values.get("경쟁강도",1),format=""),
        },)

if __name__ == "__main__" : 
    init_page()
    keywords = st.session_state["keywords"]
    print_dataframe_with_style(keywords=keywords)