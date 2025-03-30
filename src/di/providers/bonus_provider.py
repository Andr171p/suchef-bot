from dishka import Provider, provide, Scope

from src.apis import BonusAPI
from src.repository import UserRepository
from src.core.use_cases import BonusUseCase
from src.config import settings


class BonusProvider(Provider):
    @provide(scope=Scope.APP)
    def get_bonus_api(self) -> BonusAPI:
        return BonusAPI(settings.api.url)

    @provide(scope=Scope.APP)
    def get_bonus_use_case(
            self,
            bonus_api: BonusAPI,
            user_repository: UserRepository
    ) -> BonusUseCase:
        return BonusUseCase(bonus_api, user_repository)
