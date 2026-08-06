import streamlit as st
from about_page import show_about_page
from contacts_app.app import show_contacts_page

st.set_page_config(
    page_title="Personal Project",
    layout="wide",
    initial_sidebar_state="expanded",
)
#
st.sidebar.title("Навігація")
selected_page = st.sidebar.radio(
    "Оберіть сторінку",
    ["Про мене", "Контакти"],
    index=0,
)

if selected_page == "Контакти":
    show_contacts_page()
else:
    show_about_page()