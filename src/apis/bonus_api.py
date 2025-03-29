from src.http import HTTPClient
from src.http.responses import JsonResponse
from src.core.entities import Bonus
from src.mappers import BonusMapper


class BonusAPI:
    def __init__(self, url: str) -> None:
        self._url = url

    async def get_by_phone_number(self, phone_number: str) -> Bonus:
        async with HTTPClient(JsonResponse()) as http_client:
            response = await http_client.post(
                url=self._url,
                json={
                    "command": "bonus",
                    "telefon": phone_number,
                    "project": "Сушеф.рф"
                },
                headers={"Content-Type": "application/json; charset=UTF-8"}
            )
        return BonusMapper.from_response(response)
