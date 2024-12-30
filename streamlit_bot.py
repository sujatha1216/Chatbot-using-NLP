import streamlit as st
from chatbot import chat_bot
import os
import csv
import datetime
from typing import Literal, TypeAlias
from dataclasses import dataclass
import streamlit.components.v1 as components

@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str

def load_css():
    try:
         with open("static/style.css", "r") as f:
            css = f"<style>{f.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError: st.error("CSS file not found.") 
    except Exception as e: st.error(f"An error occurred: {e}")

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    response = chat_bot(human_prompt)
    st.session_state.history.append(Message("human", human_prompt))
    st.session_state.history.append(Message("ai", response))

load_css()



    # creating side bar
menue=["Home","About"]
choice =st.sidebar.selectbox("Menue",menue)




 
if choice == "Home":
   
    
    initialize_session_state()
    st.title("Intents based Chatbot 🤖 ")

    chat_placeholder = st.container()
    prompt_placeholder = st.form("Chat-form")

 
    

    with chat_placeholder:
        for chat in st.session_state.history:
            div = f"""
    <div class="chat-row
        {'' if chat.origin =='ai' else 'row-reverse'}">
        <img class="chat-icon" src="app/static/{
            'ai_icon.png' if chat.origin == 'ai'
                        else 'user_icon.png'}
            "width=32 height=32>
        <div class="chat-bubble
        {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
            &#8203;{chat.message}
        </div>
    </div>
        """
            st.markdown(div, unsafe_allow_html=True)
            
            
        for _ in range(3):
            st.markdown("")

    with prompt_placeholder:
        st.markdown("Chat")
        cols = st.columns((6, 1))
        cols[0].text_input("chat", value="Hello bot", label_visibility="collapsed", key="human_prompt",)
        cols[1].form_submit_button("Submit", type="primary", on_click=on_click_callback,)