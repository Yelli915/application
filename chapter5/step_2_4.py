from pathlib import Path
import streamlit as st
from step_1 import IN_DIR, OUT_DIR
from step_2_3 import OUT_2_3,read_text_and_draw_line

st.title("#만들면서 배우는 문자인식 웹앱")

uploaded = st.file_uploader("인식할 이미지를 선택하세요")

if uploaded is not None :
    tmp_path = OUT_DIR/f"{Path(__file__).stem}.tmp"
    tmp_path.write_bytes(uploaded.getvalue())

    col_left,col_right = st.columns(2)
    with col_left :
        st.subheader("원본이미지")
        st.image(tmp_path.as_posix())
    with col_right : 
        st.subheader("문자 인식 결과")
        with st.spinner(text="문자를 인식하는 중입니다") : 
            read_text_and_draw_line(tmp_path)
        st.image(OUT_2_3.as_posix())