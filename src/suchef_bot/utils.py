import re
from pathlib import Path
from typing import Union


def read_txt(file_path: Union[Path, str]) -> str:
    with open(file_path, encoding="utf-8") as file:
        return file.read()


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


def format_time(time: str) -> str:
    return str(time.split('T')[-1][:-3])


def format_date(date: str) -> str:
    parts = date.split('T')[0].split('-')
    return '.'.join(reversed(parts))


def format_address(address: str) -> str:
    parts = address.split(',')[3:]
    return ''.join(parts)
