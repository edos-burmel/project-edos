import streamlit as st
from about_page import show_about_page
from contacts_app.app import show_contacts_page
from places_app.app import show_places_page

st.set_page_config(
    page_title="Personal Project",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Навігація")
page_name = st.sidebar.radio(
    "Оберіть сторінку:",
    ["Про мене", "Контакти", "Міста"],
    index=0,
)

if page_name == "Про мене":
    show_about_page()
elif page_name == "Контакти":
    show_contacts_page()
else:
    show_places_page()