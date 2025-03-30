from typing import List

from src.core.entities import Promo
from src.services.web_parser import PromosWebParser


class PromosUseCase:

    def __init__(self, promos_web_parser: PromosWebParser) -> None:
        self._promos_web_parser = promos_web_parser

    async def get_promos(self) -> List[Promo]:
        return await self._promos_web_parser.parse_all()
