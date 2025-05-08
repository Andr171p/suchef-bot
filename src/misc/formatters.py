import re


def format_phone_number(phone: str) -> str:
    digits = re.sub(
        pattern='\D',
        repl='',
        string=phone
    )
    if len(digits) == 11 and digits.startswith('8'):
        digits = '7' + digits[1:]
    elif len(digits) == 10 and digits.startswith('9'):
        digits = '7' + digits
    return f"+{digits[0]}({digits[1:4]}){digits[4:7]}-{digits[7:9]}-{digits[9:11]}"


def format_order_number(number: str) -> str:
    return number.split(sep='-', maxsplit=1)[-1]


def format_address(address: str) -> str:
    parts = address.split(',')[3:]
    return ''.join(parts)
