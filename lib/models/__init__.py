from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.base import Base
from lib.models.events import Event
from lib.models.guests import Guest
from lib.models.rsvp import RSVP

engine = create_engine('sqlite:///event_guest_manager.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
