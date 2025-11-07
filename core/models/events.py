from datetime import datetime
from .base import Base, Column, Integer, String, DateTime


class Events(Base):
    __tablename__ = "events"
    from_attributes = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(String(255), index=True, nullable=False, unique=True)
    article_url = Column(String(500), nullable=False)

    registration_title = Column(String(255), default="无")
    registration_time = Column(String(100), default="即时")
    registration_method = Column(String(500))
    event_time = Column(String(255), default="无")
    event_fee = Column(String(100), default="无")
    audience = Column(String(255), default="无")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
