from typing import List

from src.core.entities import Promo
from src.web_parsers import PromosWebParser


class PromosUseCase:

    def __init__(self, promos_web_parser: PromosWebParser) -> None:
        self._promos_web_parser = promos_web_parser

    async def get(self) -> List[Promo]:
        return await self._promos_web_parser.parse_all()
