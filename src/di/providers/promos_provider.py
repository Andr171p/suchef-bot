from dishka import Provider, provide, Scope

from src.services.web_parser import PromosWebParser
from src.core.use_cases import PromosUseCase
from src.config import settings


class PromosProvider(Provider):
    @provide(scope=Scope.APP)
    def get_promos_web_parser(self) -> PromosWebParser:
        return PromosWebParser(settings.project.url)

    @provide(scope=Scope.APP)
    def get_promos_use_case(self, promos_web_parser: PromosWebParser) -> PromosUseCase:
        return PromosUseCase(promos_web_parser)
