from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    rsvps = relationship("RSVP", back_populates="guest", cascade="all, delete-orphan")
    events = relationship("Event", secondary="rsvps", back_populates="guests")

    def __repr__(self):
        return f"<Guest(id={self.id}, name='{self.name}', email='{self.email}')>"