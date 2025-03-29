from dishka import Provider, provide, Scope

from src.config import settings
from src.database import DatabaseManager


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_database_manager(self) -> DatabaseManager:
        return DatabaseManager(settings.db.url)
