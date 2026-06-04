from .repositories import ShortLinkRepository
from .exceptions import CodeExistsError, RedirectError
from pydantic import HttpUrl
from datetime import datetime
import string
import random


class ShortLinkService:
    def __init__(self, repo: ShortLinkRepository):
        self.repo = repo

    @staticmethod
    def _generate_short_link_code(length: int = 6):
        characters = string.ascii_letters + string.digits
        code = "".join(random.choices(characters, k=length))
        return code

    def generate_unique_code(self):
        code = self._generate_short_link_code()

        while self.repo.get_by_code(code):
            code = self._generate_short_link_code()

        return code

    def create_short_link(
        self,
        url: HttpUrl,
        expire_time: datetime | None = None,
        custom_code: str | None = None,
    ):
        code = self.generate_unique_code() if not custom_code else custom_code

        if custom_code and self.repo.get_by_code(code):
            raise CodeExistsError("The code already exists.")

        return self.repo.create(
            code=code, original_link=str(url), expired_at=expire_time
        )

    def get_by_code(self, code: str):
        short_link_obj = self.repo.get_by_code(code)

        if (
            not short_link_obj
            or not short_link_obj.is_active
            or datetime.now() > short_link_obj.expired_at
        ):
            raise RedirectError("Page not found.")

        return short_link_obj

    def incr_visitor_count_by_code(self, code: str, visitor_count: int, value: int = 1):
        return self.repo.update_by_code(code, visitor_count=visitor_count + value)
