from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .base import Base

class RSVP(Base):
    __tablename__ = 'rsvps'

    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('guests.id'))
    event_id = Column(Integer, ForeignKey('events.id'))
    status = Column(String)

    guest = relationship("Guest", back_populates="rsvps")
    event = relationship("Event", back_populates="rsvps")

    def __repr__(self):
        return f"<RSVP(guest_id={self.guest_id}, event_id={self.event_id}, status='{self.status}')>"