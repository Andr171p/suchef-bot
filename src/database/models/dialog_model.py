from datetime import datetime

from sqlalchemy import Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base_model import BaseModel
from src.database.models.user_relation_mixin import UserRelationMixin


class DialogModel(UserRelationMixin, BaseModel):
    __tablename__ = "dialogs"

    _user_back_populates = "dialogs"

    user_message: Mapped[str] = mapped_column(Text)
    chatbot_message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(user_id={self.user_id}, user_message={self.user_message}, chatbot_message={self.chatbot_message})"

    def __repr__(self) -> str:
        return str(self)
