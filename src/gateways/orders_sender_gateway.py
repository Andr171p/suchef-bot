from src.core.entities import Order
from src.presentation.bot.messages import OrderMessage
from src.services.sender import TelegramSenderService


class OrdersSenderGateway:
    def __init__(self, sender_service: TelegramSenderService) -> None:
        self._sender_service = sender_service
        
    async def send(self, user_id: int, order: Order) -> bool:
        order_message = OrderMessage(order)
        is_delivered = await self._sender_service.send_with_photo(
            user_id=user_id,
            photo=order_message.photo,
            text=order_message.text,
            keyboard=order_message.keyboard
        )
        return is_delivered
