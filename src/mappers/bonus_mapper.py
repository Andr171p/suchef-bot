from src.core.entities import Bonus


class BonusMapper:
    @staticmethod
    def from_response(response: dict) -> Bonus:
        return Bonus(**response["data"])
