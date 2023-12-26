import streamlit as st
import pandas as pd

# Streamlitのページ設定
st.set_page_config(page_title="RSA暗号体験（暗号化）", layout="wide")

# ヘッダーと説明
st.title("RSA暗号体験（暗号化）")
st.caption("Created by Dit-Lab.(Daiki Ito)")
st.write("")
st.subheader("ブラウザでRSA暗号の「鍵生成」→「暗号化」→「復号」まで体験することができます")
st.write("暗号化には便宜上ポケベル暗号を使っています")

# ポケベル暗号リストを読み込む
pocketbell_df = pd.read_excel("ポケベル暗号リスト.xlsx")
pocketbell_dict = dict(zip(pocketbell_df['文字'], pocketbell_df['数字']))

# 平文の入力
raw_text = st.text_input("暗号化したい文字列を入力")

if str(raw_text) == "":
    st.error("【エラー】暗号化したい文字列を入力してください。")
else:
    # 平文をポケベル暗号に変換
    pocket_bell_text = []
    unknown_chars = False
    for ch in raw_text:
        if ch in pocketbell_dict:
            pocket_bell_text.append(pocketbell_dict[ch])
        else:
            unknown_chars = True
            break
    if unknown_chars:
        st.warning("【エラー】リストにない文字が含まれているため、数値化できません。")
    else:
        # 平文と数値のマッピングをデータフレームで表示
        df = pd.DataFrame({'平文': list(raw_text), '数値': pocket_bell_text})
        st.write(df)
            
        st.write("②　上記の平文を数値化すると、「" + ' '.join(map(str, pocket_bell_text)) + "」になります。")

        # 公開鍵の入力
        st.write("受け取った「公開鍵（ n、e ）」を入力してください。")
        n = st.number_input("公開鍵( n )を入力してください。", min_value=1, value=1, step=1)
        e = st.number_input("公開鍵( e )を入力してください。", min_value=1, value=1, step=1)

        if st.button("暗号化実行"):
            # RSA暗号化処理
            encrypted_text = [pow(num, e, n) for num in pocket_bell_text]
            st.write("暗号化されたテキスト：", encrypted_text)

st.write('ご意見・ご要望は→', 'https://forms.gle/G5sMYm7dNpz2FQtU9', 'まで')
st.markdown('© 2022-2023 Dit-Lab.(Daiki Ito). All Rights Reserved.')