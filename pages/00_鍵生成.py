import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="RSA暗号体験（暗号化）", layout="wide")

st.title("RSA暗号体験（暗号化）")
st.caption("Created by Daiki Ito")
st.write("")
st.subheader("ブラウザでRSA暗号の「鍵生成」→「暗号化」→「複合」まで体験することができます")
st.write("暗号化には便宜上ポケベル暗号を使っています")

sp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
      61, 67, 71, 73, 79, 83, 89, 97]

sq = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
      61, 67, 71, 73, 79, 83, 89, 97]

st.write("③　0~100 内の素数( p )を選択")
p = st.selectbox("素数 p を選択してください", sp)
st.write("④　0~100 内の素数( q )を選択")
q = st.selectbox("素数 q を選択してください", sq)

if p == q:
    st.write(
        '<span style="color:red">【エラー】p と q が同じ数字のため、暗号化を実行できません。pとq'
        'は別々の数字にしてください。</span>',
        unsafe_allow_html=True)
else:
    n = p * q

    st.write("⑤　n = p q　 を求めます。")
    st.write(
        "p ( " + str(p) + " ) × q ( " + str(q) + " ) のため、 n は " + str(
            n) + " になります。")

    z = (p - 1) * (q - 1)
    st.write("⑥　z = ( p - 1 ) × ( q - 1 )　を求めます。")
    st.write(" p - 1 =" + str(p - 1) + "、 q - 1 =" + str(
        q - 1) + " のため、z は " + str(z) + " になります。")

    st.write("⑦　z ( " + str(z) + " )を割ることのできない素数( e )を選んでください。")
    se = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97]

    e = st.selectbox("e を選択してください", se)

    if z % e == 0:
        st.write(
            " e ( " + str(e) + " ) は z ( " + str(z) + " ) を割ることができます。")
        st.write(
            " z ( " + str(z) + " )÷ e ( " + str(e) + " ) = " + str(z // e))
    else:
        st.write(
            "⑧　m ( p - 1 )( q - 1 )  ≡ 1 （ mod e ）となる数（ m ）を求める（1≦m≦e-1）")
        st.write("z ( " + str(z) + " ) × m と -1 を e (" + str(
            e) + " ) で割って、余りが等しくなる数 ( m ) を求めます。")
        st.write("ただし、m は 1 以上、e - 1 ( " + str(
            e - 1) + " ) 以下でないといけません。 ( 1 ≦ m ≦ " + str(e - 1) + " )")
        st.write("つまり、「 zm を e で割った余り 」と")
        st.write("「 -1 を e で割った余り 」が等しくなるような m を見つけてください")
        st.write(
            "-1 を e ( " + str(e) + " )で割った余りは " + str(-1 % e) + " です。")
        st.write("→ " + str(z) + "  × m を e ( " + str(
            e) + " ) で割った余りが" + str(-1 % e) + " になるような m を探してください。")

        sm = range(1, e, 1)

        m = st.selectbox("m を選択してください（1 ≦ m ≦ " + str(e - 1) + "）", sm)

        if (-1 % e) != (z * m % e):
            st.write(
                "【エラー】「 zm を e で割った余り 」と「 -1 を e で割った余り 」が等しくありません")
        else:
            st.write("⑨　m ( p - 1 )( q - 1 )  + 1　を e で割った商（ d ）を求めます")
            d = (m * z + 1) // e
            st.write(" d は " + str(d) + " です。")
            st.write("")
            st.write("公開鍵（n,e）と秘密鍵（p,q,d）の生成が完了しました。")
            st.write("公開鍵（相手に教える値）")
            st.write("n = " + str(n) + " 、e = " + str(e))
            st.write("秘密鍵（教えてはいけない値 ）")
            st.write(
                "p = " + str(p) + " 、q = " + str(q) + " 、d = " + str(d))
