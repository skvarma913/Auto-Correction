import streamlit as st
from streamlit_option_menu import option_menu
import uploadtextans

with st.sidebar:
    option = option_menu(
        menu_title="Auto Assess",
        options=["Home", "Login", "Signup", "upload papers", "About", "Help"],
    )

if option == "Home":
    uploadtextans.app()