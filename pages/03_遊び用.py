import streamlit as st
import rsa

st.title("RSA Encryption Web Application")

# Generate RSA keys
def generate_keys():
    (pubkey, privkey) = rsa.newkeys(512)
    return pubkey, privkey

# Encrypt message
def encrypt_message(message, pubkey):
    encrypted_message = rsa.encrypt(message.encode(), pubkey)
    return encrypted_message

# Decrypt message
def decrypt_message(encrypted_message, privkey):
    decrypted_message = rsa.decrypt(encrypted_message, privkey)
    return decrypted_message.decode()

# Interface to get user input
message = st.text_input("Enter your message here")

if st.button('Generate Keys'):
    pubkey, privkey = generate_keys()
    st.write("Public Key: ", pubkey)
    st.write("Private Key: ", privkey)

if st.button('Encrypt Message'):
    if message and pubkey:
        encrypted_message = encrypt_message(message, pubkey)
        st.write("Encrypted Message: ", encrypted_message)
    else:
        st.write("Please generate keys and enter a message")

if st.button('Decrypt Message'):
    if encrypted_message and privkey:
        decrypted_message = decrypt_message(encrypted_message, privkey)
        st.write("Decrypted Message: ", decrypted_message)
    else:
        st.write("Please generate keys, enter a message and encrypt it")
