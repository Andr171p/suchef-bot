from sqlalchemy import Index, BigInteger, Text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class UserOrm(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str]

    __table_args__ = (
        Index("user_index", "telegram_id", "phone_number"),
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n"
            f"telegram_id={self.telegram_id},\n"
            f"username={self.username},\n"
            f"phone_number={self.phone_number},\n"
            f"created_at={self.created_at}\n"
            f")"
        )

    def __repr__(self) -> str:
        return str(self)


class MessageOrm(Base):
    __tablename__ = "messages"

    role: Mapped[str]
    chat_id: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(Text)

    __table_args__ = (
        CheckConstraint(
            "role == 'user' OR role == 'assistant'",
            "check_available_roles"
        )
    )
