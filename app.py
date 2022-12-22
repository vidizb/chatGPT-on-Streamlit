import streamlit as st
from pyChatGPT import ChatGPT

session_token = st.secrets["pass"]
api = ChatGPT(session_token)  # auth with session token
msg = st.text_area("Hello!")
if st.button("Start"): 
    resp = api.send_message(msg)
    st.write(resp['message'])
