from pydantic import BaseModel, field_validator


class Promo(BaseModel):
    url: str
    title: str

    @field_validator("url")
    def validate_url(self, link: str) -> str:
        return f"https://imp72.ru{link}"
