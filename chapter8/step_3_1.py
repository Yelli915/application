import pandas as pd
import streamlit as st
from step_2_1 import rel_kwd_to_csv
from step_2_2 import data_cleaning
from step_2_3 import shop_cnt_to_csv
from step_2_4 import OUT_2_4,comp_lev_to_csv

def init_page() :
    st.set_page_config(layout="wide")
    st.header("만들며 배우는 파이썬")
    if "keywords" not in st.session_state : #keywords 저장소에 없다면
        st.session_state["keywords"] = "" # 공백으로 표시
    with st.form(key="my_form",border = False) :
        col_1, col_2 = st.columns([3,1])
        with col_1 : 
            st.text_input("키워드",key="keywords",label_visibility="collapsed")
        with col_2 :
            st.form_submit_button(label="분석하기", use_container_width=True)

def analyze_keywords(keywords : str=None, event:int=None) :
    rel_kwd_to_csv(keywords=keywords, event=event)
    data_cleaning()
    shop_cnt_to_csv()
    comp_lev_to_csv()

def print_dataframe(keywords:str=None) :
    if keywords :
        with st.spinner("waiting...") :
            analyze_keywords(st.session_state["keywords"])
        df_result = pd.read_csv(OUT_2_4)
        st.dataframe(df_result,use_container_width=True)

if __name__ == "__main__" :
    init_page()
    keywords = st.session_state["keywords"]
    print_dataframe(keywords=keywords)