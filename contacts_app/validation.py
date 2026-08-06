#Створить функцию validate_email(email).
#Кожна з Ф-я повинная повертати кортеж з двох значень:
# True abo False
# Текст повидомлення
from numpy.random.mtrand import normal


# from validation import validate_phone, validate_email

def validate_email(email):
    normalized_email = (email or "").strip()

    if not normalized_email:
        return False, "Email не може бути порожнім."

    if "@" not in normalized_email:
        return False, "Email має містити @."

    local_part, domain = normalized_email.split("@", 1)

    if not local_part or not domain:
        return False, "Email має містити ім'я користувача та домен."

    if "." not in domain:
        return False, "Email має містити крапку в домені."

    return True, ""


def validate_phone(phone):
    normalized_phone = (phone or "").strip()

    if not normalized_phone:
        return False, "Телефон не має бути порожнім."

    if normalized_phone[0] == "+":
        digits = normalized_phone[1:]
    else:
        digits = normalized_phone
        
    if not digits.isdigit():
        return False, "Телефон має містити лише цифри та знак + на початку."

    if len(digits) != 12:
        return False, "Телефон має містити 12 цифр."

    return True, ""

