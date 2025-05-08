from typing import Any

from src.suchef_bot.core import Promo


class PromoMapper:
    @staticmethod
    def from_image(image: Any) -> Promo:
        return Promo(
            url=image["data-src"],
            title=image["title"]
        )
