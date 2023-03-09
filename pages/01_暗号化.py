import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="RSA暗号体験（暗号化）", layout="wide")

st.title("RSA暗号体験（暗号化）")
st.caption("Created by Daiki Ito")
st.write("")
st.subheader("ブラウザでRSA暗号の「鍵生成」→「暗号化」→「復号」まで体験することができます")
st.write("暗号化には便宜上ポケベル暗号を使っています")

st.subheader("")
st.subheader("暗号化")

raw_text = st.text_input("暗号化したい文字列を入力")
if str(raw_text) == "":
    st.write(
        '<span style="color:red">【エラー】暗号化したい文字列を入力してください。</span>',
        unsafe_allow_html=True)
else:
    st.write("①　あなたが暗号化したい文章は「" + raw_text + "」です。")

    # if st.button(label='次のステップ'):
    pocket_bell_text = 1111

    st.write("②　上記の平文を暗号化すると、「" + str(pocket_bell_text) + "」になります。")
    st.write("受け取った「公開鍵（ n、e ）」を入力してください。")
    n = st.number_input("公開鍵( n )を入力してください。", 0)
    e = st.number_input("公開鍵( e )を入力してください。", 0)
