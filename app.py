import streamlit as st
from about_page import show_about_page


st.set_page_config(
    page_title="Personal Project",
    layout="wide",
    initial_sidebar_state="expanded",
)

page = st.navigation({
        "": [st.Page(show_about_page, title="Про мене", default=True)],
    },
    position = "sidebar"
)

page.run()