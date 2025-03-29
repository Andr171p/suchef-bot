from src.misc.file_readers import read_txt
from src.config import BASE_DIR


MESSAGE_PATH = BASE_DIR / "messages" / "Нет_заказов.txt"


class NoOrdersMessage:
    text: str = read_txt(MESSAGE_PATH)
