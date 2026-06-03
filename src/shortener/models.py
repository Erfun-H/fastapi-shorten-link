from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from src.core.database import Base

from datetime import timedelta


class ShortLink(Base):
    __tablename__ = "short_links"

    id = Column(Integer, primary_key=True, index=True)
    original_link = Column(String(500))
    code = Column(String(6), unique=True, index=True)
    is_active = Column(Boolean, default=True)

    created = Column(DateTime, server_default=func.now())
    expired_at = Column(DateTime, default=func.now() + timedelta(days=7))
