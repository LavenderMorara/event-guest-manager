from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    location = Column(String)
    date = Column(Date)

    rsvps = relationship("RSVP", back_populates="event", cascade="all, delete-orphan")
    guests = relationship("Guest", secondary="rsvps", back_populates="events")

    def __repr__(self):
        return f"<Event(id={self.id}, title='{self.title}', date={self.date})>"
