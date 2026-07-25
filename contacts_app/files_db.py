import json
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FILE_NAME = SCRIPT_DIR / 'contacts.json'

# Створіть функцію save_contacts(contacts),
# яка зберігає список контактів у файл contacts.json


def save_contacts(contacts):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)


# Створіть функцію load_contacts(),
# яка читає контакти з файлу contacts.json

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        contacts = json.load(file)

    return contacts

#Функция make_contact_id(contacts),
#яка буде ств новий унікальний ID для контакту

def make_contact_id(contacts):
    max_id = 0

    for contact in contacts:
        contact_id = contact.get("id", 0)

        if contact_id > max_id:
            max_id = contact_id

    return max_id + 1