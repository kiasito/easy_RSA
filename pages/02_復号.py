import streamlit as st
import pandas as pd

# Streamlitのページ設定
st.set_page_config(page_title="RSA暗号体験（復号）", layout="wide")

# ヘッダーと説明
st.title("RSA暗号体験（復号）")
st.caption("Created by Dit-Lab.(Daiki Ito)")
st.write("")
st.subheader("RSA暗号の「復号」プロセスを体験することができます")
st.write("復号には、暗号化された数値と秘密鍵が必要です")

# ポケベル暗号リストを読み込む
pocketbell_df = pd.read_excel("ポケベル暗号リスト.xlsx")
pocketbell_dict = {v: k for k, v in dict(zip(pocketbell_df['文字'], pocketbell_df['数字'])).items()}

# 秘密鍵の入力
n = st.number_input("公開鍵( n )を入力してください", min_value=1, value=1, step=1)
d = st.number_input("秘密鍵( d )を入力してください", min_value=1, value=1, step=1)

# 暗号化されたテキストの入力
encrypted_text_input = st.text_area("暗号化された数値をスペース区切りで入力してください")
encrypted_text = [int(num) for num in encrypted_text_input.split() if num.isdigit()]

if st.button("復号実行"):
    # RSA復号処理
    decrypted_text = [pow(num, d, n) for num in encrypted_text]

    # 復号された数値をポケベル暗号で文字に変換
    decrypted_chars = [pocketbell_dict.get(num, '?') for num in decrypted_text]
    
    # 復号された文字をデータフレームで表示（転置してカラム名を設定）
    decrypted_df = pd.DataFrame({'復号された文字': decrypted_chars}).T
    decrypted_df.columns = ['文字' + str(i+1) for i in range(len(decrypted_chars))]  # 新しいカラム名を設定
    st.write(decrypted_df)

st.write('ご意見・ご要望は→', 'https://forms.gle/G5sMYm7dNpz2FQtU9', 'まで')
st.markdown('© 2022-2023 Dit-Lab.(Daiki Ito). All Rights Reserved.')
