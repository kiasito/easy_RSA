import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="RSA暗号体験（暗号化）", layout="wide")

st.title("RSA暗号体験（暗号化）")
st.caption("Created by Daiki Ito")
st.write("")
st.subheader("ブラウザでRSA暗号の「暗号化」→「複合」まで体験することができます")
st.write("暗号化には便宜上ポケベル暗号を使っています")

raw_text = st.text_input("暗号化したい文字列を入力")

st.write("①　あなたが暗号化したい文章は「" + raw_text + "」です。")

pocket_bell_text = 1111

st.write("②　上記の平文を暗号化すると、「" + str(pocket_bell_text) + "」になります。")

sp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
      71,
      73, 79, 83, 89, 97]

sq = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
      71,
      73, 79, 83, 89, 97]
p = st.selectbox("③　0~100 内の素数( p )を選択", sp)
q = st.selectbox("④　0~100 内の素数( q )を選択", sq)

# if p == q:
#    st.write("pとqが同じ数字のため、暗号化を実行できません。pとqは別々の数字にしてください。")
# else:
#    st.write("p=" + p + "、q=" + q)

n = p * q

st.write("⑤　n=pq　nは" + str(p) + "×" + str(q) + "で" + str(n) + "になります。")
