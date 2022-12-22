import streamlit as st
from pyChatGPT import ChatGPT

session_token = st.secrets["pass"]
api = ChatGPT(session_token,verbose=True)  # auth with session token
msg = st.text_area("Prompt:")
if st.button("Enter"): 
    resp = api.send_message(msg)
    st.write(resp['message'])
    api.reset_conversation()  # reset the conversation
