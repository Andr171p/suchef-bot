import logging

from typing import List, Optional

import aiohttp
from bs4 import BeautifulSoup

from ..core.entities import Promo
from ..core.interfaces import PromoGateway


logger = logging.getLogger(__name__)


class PromoCrawlerGateway(PromoGateway):
    def __init__(self, url: str) -> None:
        self.url = url

    async def get_promos(self) -> Optional[List[Promo]]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url) as response:
                    data = await response.text()
            soup = BeautifulSoup(data, "html.parser")
            promos = soup.find_all(
                "div",
                attrs={"class": "flex-grid__item flex-grid__item_max-width product-ajax-cont"}
            )
            return [
                Promo(url=image["data-src"], title=image["title"])
                for promo in promos
                if (image := promo.find("img"))
            ]
        except Exception as e:
            logger.error("Error while receiving promos: %s", e)
