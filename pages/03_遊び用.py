import streamlit as st
import rsa

st.title("RSA暗号化Webアプリケーション")

# RSA鍵の生成
def generate_keys():
    (pubkey, privkey) = rsa.newkeys(512)
    return pubkey, privkey

# メッセージの暗号化
def encrypt_message(message, pubkey):
    encrypted_message = rsa.encrypt(message.encode(), pubkey)
    return encrypted_message

# メッセージの復号化
def decrypt_message(encrypted_message, privkey):
    decrypted_message = rsa.decrypt(encrypted_message, privkey)
    return decrypted_message.decode()

# ユーザー入力のインターフェース
message = st.text_input("ここにメッセージを入力してください")

if st.button('鍵の生成'):
    pubkey, privkey = generate_keys()
    st.write("公開鍵: ", pubkey)
    st.write("秘密鍵: ", privkey)

if st.button('メッセージの暗号化'):
    if message and pubkey:
        encrypted_message = encrypt_message(message, pubkey)
        st.write("暗号化されたメッセージ: ", encrypted_message)
    else:
        st.write("鍵を生成し、メッセージを入力してください")

if st.button('メッセージの復号化'):
    if encrypted_message and privkey:
        decrypted_message = decrypt_message(encrypted_message, privkey)
        st.write("復号化されたメッセージ: ", decrypted_message)
    else:
        st.write("鍵を生成し、メッセージを入力し、それを暗号化してください")
