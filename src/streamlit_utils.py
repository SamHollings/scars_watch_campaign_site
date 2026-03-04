import streamlit as st

def display_messages():
    """Display all messages in the chat history"""
    for msg in st.session_state.messages:
        if msg["role"] == "system":
            continue
        author = "user" if msg["role"] == "user" else "assistant"
        with st.chat_message(author):
            st.write(msg["content"])