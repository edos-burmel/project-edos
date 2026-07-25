#Створить функцию validate_email(email).
#Кожна з Ф-я повинная повертати кортеж з двох значень:
# True abo False
# Текст повидомлення

# from validation import validate_phone, validate_email

def validate_email(email):
    if "@" not in email:
        return False, "Email має містити @."

    if "." not in email:
        return False, "Email має містити крапку."

    return True, ""


def validate_phone(phone):
    if phone[0] == "+":
        digits = phone[1:]

    else:
        digits = phone

    if not digits.isdigit():
        return False, "Телефон має містити лише цифри та знак + на початку."

    if len(digits) != 12:
        return False, "Телефон має містити 12 цифр."

    return True, ""

