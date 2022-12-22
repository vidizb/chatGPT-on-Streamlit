import streamlit as st
from pyChatGPT import ChatGPT

session_token = st.secrets["pass"]
api = ChatGPT(session_token, proxy = 'https://hellochatgpt.streamlit.app')  # auth with session token
msg = st.text_area("Prompt:")
if st.button("Enter"): 
    resp = api.send_message(msg)
    st.write(resp['message'])
