from dishka import Provider, provide, Scope

from src.database.crud import UserCRUD, DialogCRUD
from src.repository import UserRepository, DialogRepository


class RepositoryProvider(Provider):
    @provide(scope=Scope.APP)
    def get_user_repository(self, crud: UserCRUD) -> UserRepository:
        return UserRepository(crud)

    @provide(scope=Scope.APP)
    def get_dialog_repository(self, crud: DialogCRUD) -> DialogRepository:
        return DialogRepository(crud)
