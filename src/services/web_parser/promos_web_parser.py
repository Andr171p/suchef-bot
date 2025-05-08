from typing import List

from bs4 import BeautifulSoup

from src.http import HTTPClient
from src.http.responses import TextResponse
from src.suchef_bot.core import Promo
from src.mappers import PromoMapper


class PromosWebParser:
    def __init__(self, url: str) -> None:
        self._url = url

    async def parse_all(self) -> List[Promo]:
        async with HTTPClient(TextResponse()) as http_client:
            html = await http_client.get(self._url)
        soup = BeautifulSoup(html, "html.parser")
        blocks = soup.find_all("div", attrs={"class": "flex-grid__item flex-grid__item_max-width product-ajax-cont"})
        return [PromoMapper.from_image(image) for block in blocks if (image := block.find("img"))]
