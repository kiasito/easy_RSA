import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="RSA暗号体験（復号）", layout="wide")

st.title("RSA暗号体験（復号）")
st.caption("Created by Daiki Ito")
st.write("")
st.subheader("ブラウザでRSA暗号の「鍵生成」→「暗号化」→「複合」まで体験することができます")
st.write("暗号化には便宜上ポケベル暗号を使っています")
st.subheader("")
st.subheader("復号")
