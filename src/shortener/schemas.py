from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime, timedelta


class ShortenLinkRequest(BaseModel):
    url: HttpUrl
    custom_code: str | None = Field(default=None, max_length=25)
    expire_time: datetime = Field(
        default=datetime.now() + timedelta(days=7),
    )


class ShortenLinkRespone(BaseModel):
    short_url: HttpUrl
    code: str
