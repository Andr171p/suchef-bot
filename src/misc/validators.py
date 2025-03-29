import re


def is_valid_phone_number(phone_number: str) -> bool:
    pattern = r'\+\d$\d{3}$\d{3}-\d{2}-\d{2}'
    return bool(re.fullmatch(
        pattern=pattern,
        string=phone_number
    ))
