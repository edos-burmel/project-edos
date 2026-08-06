import streamlit as st

EMAIL = "edosburmel@gmail.com"
GITHUB_URL = "https://github.com/edos-burmel"

#
def show_about_page():
    st.title("Edos")
    st.info("Оновлено: тепер у застосунку є сторінка Контакти з пошуком, статистикою та навігацією.")

    st.subheader("Мої проєкти")

    with st.container(border=True):
        st.subheader("Список контактів")
        st.write(
            "Застосунок для збереження контактів. Користувач може додавати,"
            "видаляти, шукати і фільтрувати контакти."
        )
        st.write("Технології: Python, Streamlit, JSON, pandas")

    st.subheader("Мої Контакти")
    with st.container(border=True):
        st.write(f"Email: {EMAIL}")
        st.write(f"GitHub: {GITHUB_URL}")