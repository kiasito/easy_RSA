import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="RSA暗号体験", layout="wide")

st.title("RSA暗号体験")
st.caption("Created by Dit-Lab.(Daiki Ito)")
st.write("")
st.subheader("ブラウザでRSA暗号の「鍵生成」→「暗号化」→「復号」まで体験することができます")
st.subheader("RSA暗号とは")
st.write("➀　ペアで「受信者」「送信者」の役割を決める")
st.write("RSA暗号…公開鍵暗号方式で使われる代表的な暗号アルゴリズム")
st.write("　→　コンピュータで素因数分解しようとしても、大きな数であれば膨大な時間がかかる仕組みを利用した暗号")
st.write("")
st.subheader("RSA暗号体験Webアプリケーションの使い方")
st.write("➀　ペアで「受信者」「送信者」の役割を決める")
st.write("➁　受信者は「鍵生成」ページで「秘密鍵（開ける鍵）」 「公開鍵（閉める鍵）」を作成")
st.write("➂　受信者は「公開鍵（閉める鍵）」を送信者に渡す")
st.write("④　送信者は、「暗号化」ページで暗号化したい文字（ねむい　等）を決める（平文）")
st.write("※便宜上　ポケベル暗号を使用します　本来は文字コードで行われます。")
st.write("➄　送信者は、平文を公開鍵を使って暗号化する")
st.write("➅　送信者は、暗号化した文字を受信者に渡す")
st.write("➆　受信者は、「復号」ページで受け取った暗号文を、秘密鍵を使って復号する")

