import streamlit as st

styles = """"<style>
article {
    background: #f7f7f7;
    padding: 20px;
    border-radius: 12px;
    max-width: 700px;
}
article img {
    width: 100%;
    border-radius: 12px;
    margin-bottom: 16px;
}
article h3 {
    margin: 0 0 8px;
}
article p {
    margin: 0 0 12px;
}
article span {
    display: inline-block;
    margin-top: 12px;
    font-weight: 600;
}
"""

html = """
<article>
    <p>United Kingdom</p>
    <img src="https://images.unsplash.com/photo-1522098543979-ffc7f79d7418?auto=format&fit=crop&w=1200&q=80" alt="London image" />
    <h3>London</h3>
    <p>A historic city with famous landmarks, museums, and beautiful parks.</p>
    <span>Already visited</span>
</article>
"""


def show_places_page():
    st.title("Мої Міста")
    st.write(
        "Це сторінка для демонстрації улюблених місць. Тут можна додати карту, список міст, фільтри та описові картки."
    )
    st.markdown(styles + html, unsafe_allow_html=True)