from .base import Base, Column, Integer, String, DateTime

class Event(Base):
    from_attributes = True
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(String(255), index=True, nullable=False)

    registration_time = Column(String(100))
    registration_method = Column(String(500))
    event_time = Column(String(255))
    event_fee = Column(String(100))
    audience = Column(String(255))

    created_at = Column(DateTime)
    updated_at = Column(DateTime)