

class ChatBotUseCase:
    async def answer(self, user_id: int, user_question: str) -> str:
        ...
