import streamlit as st
import pandas as pd
from .files_db import load_contacts, save_contacts, make_contact_id
from .validation import validate_email, validate_phone


CITIES = ('Київ', 'Полтава', 'Харків', 'Львів', 'Одеса', 'Дніпро')


def display_contacts_tabular(contacts):
    if not contacts:
        st.info("Поки що контактів немає.")
        return

    df = pd.DataFrame(contacts)
    st.dataframe(df, hide_index=True)


def get_contact_form_data(contacts):
    with st.form("contact_form"):
        st.subheader("Новий контакт")

        name = st.text_input("Ім'я:", placeholder="Введіть ваше ім'я").strip()
        phone = st.text_input("Телефон:", "+380").strip()
        email = st.text_input("Email:", placeholder="Введіть ваш email").strip()
        city = st.selectbox("Місто:", CITIES)

        submitted = st.form_submit_button("Додати й зберегти")

    if not submitted:
        return False, "", None

    if not name:
        return False, "Ім'я не має бути порожнім.", None

    phone_ok, phone_message = validate_phone(phone)
    if not phone_ok:
        return False, phone_message, None

    email_ok, email_message = validate_email(email)
    if not email_ok:
        return False, email_message, None

    contact = {
        "id": make_contact_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
    }

    return True, "", contact


def delete_contact_by_id(contacts, contact_id):
    return [contact for contact in contacts if contact.get("id") != contact_id]


def get_city_options(contacts):
    unique_cities = sorted({contact.get("city", "") for contact in contacts if contact.get("city")})
    return ["Усі міста"] + unique_cities


def filter_contacts(contacts, search_text, selected_city):
    clean_search = search_text.strip().lower()
    result = []

    for contact in contacts:
        clean_name = contact.get('name', '').strip().lower()
        clean_email = contact.get('email', '').strip().lower()
        clean_phone = contact.get('phone', '').strip().lower()

        matches_search = (
            not clean_search
            or clean_search in clean_name
            or clean_search in clean_email
            or clean_search in clean_phone
        )
        matches_city = selected_city == 'Усі міста' or contact.get('city') == selected_city

        if matches_search and matches_city:
            result.append(contact)

    return result


def show_contacts_list(contacts):
    st.subheader("Список контактів")

    if not contacts:
        st.info("Поки що контактів немає.")
        return

    search_text = st.text_input("Пошук", key="contacts_search")
    selected_city = st.selectbox("Місто:", get_city_options(contacts), key="contacts_city")
    filtered_contacts = filter_contacts(contacts, search_text, selected_city)

    st.write(f"Усього контактів: {len(contacts)}")
    st.write(f"Знайдено контактів: {len(filtered_contacts)}")
    display_contacts_tabular(filtered_contacts)


def show_add_contact(contacts):
    is_success, error_message, contact = get_contact_form_data(contacts)

    if is_success:
        contacts.append(contact)
        save_contacts(contacts)
        st.success("Контакт збережено.")
        st.experimental_rerun()

    if error_message:
        st.error(error_message)


def show_delete_contact(contacts):
    st.subheader("Видалення контакту")

    if not contacts:
        st.info("Поки що немає контактів для видалення.")
        return

    contact = st.selectbox(
        "Контакти",
        contacts,
        format_func=lambda contact: f"{contact.get('id')} - {contact.get('name')}",
        key="delete_contact_select",
    )

    if st.button("Видалити"):
        updated_contacts = delete_contact_by_id(contacts, contact["id"])
        save_contacts(updated_contacts)
        st.success("Контакт видалено.")
        st.experimental_rerun()


def show_contacts_page():
    st.title('Список контактів')

    contacts = load_contacts()
    tabs = st.tabs(["Мої Контакти", "Додати Контакт", "Видалити Контакт"])

    with tabs[0]:
        show_contacts_list(contacts)
    with tabs[1]:
        show_add_contact(contacts)
    with tabs[2]:
        show_delete_contact(contacts)