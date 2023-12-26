import streamlit as st

st.set_page_config(page_title="RSA暗号体験（暗号化）", layout="wide")

st.title("RSA暗号体験（鍵生成）")
st.caption("Created by Dit-Lab.(Daiki Ito)")
st.write("")
st.subheader("ブラウザでRSA暗号の「鍵生成」→「暗号化」→「復号」まで体験することができます")
st.subheader("")
st.subheader("鍵生成")

sp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
      61, 67, 71, 73, 79, 83, 89, 97]

sq = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
      61, 67, 71, 73, 79, 83, 89, 97]

st.write("①　0~100 内の素数( p )を選択")
p = st.selectbox("素数 p を選択してください", sp)
st.write("②　0~100 内の素数( q )を選択")
q = st.selectbox("素数 q を選択してください", sq)

if p == q:
    st.error("【エラー】 p と q が同じ数字のため、鍵生成を実行できません。pとqは別々の数字にしてください。")
elif p * q < 143:
    st.warning("【エラー】 p と q が小さい or 近すぎるため、鍵生成を実行できません。")
    st.warning("【エラー】 p と q < 143 になるような数字にしてください。")
else:
    st.success("条件を満たしています。次のステップに進みます。")
    n = p * q
    z = (p - 1) * (q - 1)

    st.write(f"③　n = p × q を求めます。 p ( {p} ) × q ( {q} ) のため、 n は {n} になります。")
    st.write(f"④　z = ( p - 1 ) × ( q - 1 ) を求めます。 p - 1 = {p - 1}、 q - 1 = {q - 1} のため、z は {z} になります。")

    st.write("⑤　z を割ることのできない素数( e )を選んでください。")
    se = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97]

    e = st.selectbox("e を選択してください", se)

    if z % e == 0:
        st.error(f"e ( {e} ) は z ( {z} ) を割ることができます。")
        st.error(f"z ( {z} ) ÷ e ( {e} ) = {z // e}")
    else:
        st.success("条件を満たしています。次のステップに進みます。")
        st.write("⑥　m ( p - 1 )( q - 1 )  ≡ 1 （ mod e ）となる数（ m ）を求める（1≦m≦e-1）")
        st.write(f"z ( {z} ) × m と -1 を e ( {e} ) で割って、余りが等しくなる数 ( m ) を求めます。")
        st.write(f"ただし、m は 1 以上、e - 1 ( {e - 1} ) 以下でないといけません。 ( 1 ≦ m ≦ {e - 1} )")
        st.write("つまり、「zm を e で割った余り」と「-1 を e で割った余り」が等しくなるような m を見つけてください")
        st.write(f"-1 を e ( {e} ) で割った余りは {(-1 % e)} です。")
        st.write(f"→ {z}  × m を e ( {e} ) で割った余りが {(-1 % e)} になるような m を探してください。")

        sm = range(1, e, 1)

        m = st.selectbox("m を選択してください（1 ≦ m ≦ " + str(e - 1) + "）", sm)

        if (-1 % e) != (z * m % e):
            st.error("【エラー】「zm を e で割った余り」と「-1 を e で割った余り」が等しくありません")
        else:
            st.success("条件を満たしています。")
            d = (m * z + 1) // e
            st.write(f"⑦　m ( {m} ) × ( p - 1 )( q - 1 ) + 1 を e ( {e} ) で割った商（ d ）を求めます。d は {d} です。")
            st.write("")
            st.write("公開鍵（n,e）と秘密鍵（p,q,d）の生成が完了しました。")
            st.subheader("公開鍵（相手に教える値）")
            st.markdown(f"<h3>n = {n}、e = {e}</h3>", unsafe_allow_html=True)
            st.subheader("秘密鍵（教えてはいけない値 ）")
            st.markdown(f"<h3>p = {p}、q = {q}、d = {d}</h3>", unsafe_allow_html=True)

st.write('ご意見・ご要望は→', 'https://forms.gle/G5sMYm7dNpz2FQtU9', 'まで')
st.markdown('© 2022-2023 Dit-Lab.(Daiki Ito). All Rights Reserved.')
