import streamlit as st
import unicodedata

st.set_page_config(page_title="RSA暗号体験（暗号化）", layout="wide")

st.title("RSA暗号体験（暗号化）")
st.caption("Created by Daiki Ito")
st.write("")
st.subheader("ブラウザでRSA暗号の「鍵生成」→「暗号化」→「復号」まで体験することができます")
st.write("暗号化には便宜上ポケベル暗号を使っています")

st.subheader("")
st.subheader("暗号化")


def is_hiragana(ch):
    try:
        name = unicodedata.name(ch)
        return "HIRAGANA LETTER" in name
    except ValueError:
        return False


raw_text = st.text_input("暗号化したい文字列を入力")

if str(raw_text) == "":
    st.error("【エラー】暗号化したい文字列を入力してください。")
else:
    if all(is_hiragana(ch) for ch in raw_text):
        st.success("ひらがなで入力されています")
        st.write("①　あなたが暗号化したい文章は「" + raw_text + "」です。")
    else:
        st.error("【エラー】入力された文字列にはひらがな以外の文字が含まれています。")

    if st.button(label='次のステップ'):
        # ポケベル暗号化関数をここで呼び出し、raw_textを暗号化
        # pocket_bell_text = your_function_to_encrypt(raw_text)
        pocket_bell_text = 1111  # 仮の値

        st.write("②　上記の平文を暗号化すると、「" + str(pocket_bell_text) + "」になります。")
        st.write("受け取った「公開鍵（ n、e ）」を入力してください。")
        n = st.number_input("公開鍵( n )を入力してください。", min_value=1, value=1, step=1)
        e = st.number_input("公開鍵( e )を入力してください。", min_value=1, value=1, step=1)
