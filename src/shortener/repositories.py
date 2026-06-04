from sqlalchemy import select, update
from sqlalchemy.orm import Session

from .models import ShortLink


class ShortLinkRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **short_link_data):
        short_link = ShortLink(**short_link_data)
        self.db.add(short_link)
        self.db.commit()
        return short_link

    def update_by_code(self, code: str, **updated_data):
        result = self.db.execute(
            update(ShortLink)
            .where(ShortLink.code == code)
            .values(**updated_data)
            .returning(ShortLink)
        )
        short_link_obj = result.scalar_one_or_none()
        self.db.commit()
        return short_link_obj

    def get_by_code(self, code: str):
        result = self.db.execute(select(ShortLink).where(ShortLink.code == code))
        short_link = result.scalar_one_or_none()
        return short_link

    def get_by_id(self, id: int):
        result = self.db.execute(select(ShortLink).where(ShortLink.id == id))
        short_link = result.scalar_one_or_none()
        return short_link
