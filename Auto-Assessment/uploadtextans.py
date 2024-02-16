import streamlit as st
from streamlit_option_menu import option_menu
import pyperclip

st.set_page_config(layout = "wide")

def app():
    with st.sidebar:
        selected = option_menu(
            menu_title="Question Numbers",
            options=[1, 2, 3, 4, 5],
        )


    for i in range(1,6):
        if selected == i:
            with st.sidebar:
                selected1 = option_menu(
                    menu_title="Sub Questions",
                    options=["a", "b"],
                )



    for i in range(1,6):
        if selected == i and selected1 == "a":
            cols1, cols2 = st.columns(2, gap = "large")
            img = cols1.file_uploader("Upload Answer Sheet", type = ["jpg", "png", "jpeg"], key = f"{selected}")
            if img is not None:
                cols1.image(img)
                container = cols2.container(border=True)
                if cols2.button("Upload"):
                    clipboard_text = pyperclip.paste()
                    # Optional: Check if clipboard content exists
                    if clipboard_text:
                        l=clipboard_text.split()
                        p=" ".join(l)
                        container.write(p)
                    else:
                        container.write("Clipboard is empty!")

                col1, col2, col3, col4 = st.columns(4)
                if col1.button("Save"):
                    col1.success("File Saved Successfully")
                if col2.button("Add one more file"):
                    img = cols1.file_uploader("Upload Answer Sheet", type = ["jpg", "png", "jpeg"])
                    if img is not None:
                        cols1.image(img)

        if selected == i and selected1 == "b":
            cols1, cols2 = st.columns(2, gap = "large")
            img = cols1.file_uploader("Upload Answer Sheet", type = ["jpg", "png", "jpeg"], key = f"{selected}")
            if img is not None:
                cols1.image(img)
                container = cols2.container(border=True)
                if cols2.button("Upload"):
                    clipboard_text = pyperclip.paste()
                    # Optional: Check if clipboard content exists
                    if clipboard_text:
                        l=clipboard_text.split()
                        p=" ".join(l)
                        container.write(p)
                    else:
                        container.write("Clipboard is empty!")
                col1, col2, col3, col4 = st.columns(4)
                if col1.button("Save"):
                    col1.success("File Saved Successfully")
                if col2.button("Add one more file"):
                    img = cols1.file_uploader("Upload Answer Sheet", type = ["jpg", "png", "jpeg"])
                    if img is not None:
                        cols1.image(img)