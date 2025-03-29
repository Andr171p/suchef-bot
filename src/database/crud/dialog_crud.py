from typing import TYPE_CHECKING, Union, Sequence

if TYPE_CHECKING:
    from src.database.database_manager import DatabaseManager

from sqlalchemy import select

from src.database.crud.base_crud import BaseCRUD
from src.database.models import DialogModel


class DialogCRUD(BaseCRUD):
    def __init__(self, manager: "DatabaseManager") -> None:
        self._manager = manager

    async def create(self, dialog: DialogModel) -> int:
        async with self._manager.session() as session:
            session.add(dialog)
            id = dialog.id
            await session.commit()
            await session.refresh(dialog)
        return id

    async def read_by_user_id(self, user_id: int) -> Union[Sequence[DialogModel], None]:
        async with self._manager.session() as session:
            stmt = (
                select(DialogModel)
                .where(DialogModel.user_id == user_id)
            )
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()

    async def read_all(self) -> Union[Sequence[DialogModel], None]:
        async with self._manager.session() as session:
            stmt = select(DialogModel)
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()
