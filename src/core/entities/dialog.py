from pydantic import BaseModel


class Dialog(BaseModel):
    user_id: int
    user_message: str
    chatbot_message: str

    class Config:
        from_attributes = True

