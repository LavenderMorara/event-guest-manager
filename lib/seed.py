from lib.db import Session
from lib.models.guests import Guest
from lib.models.events import Event
from lib.models.rsvp import RSVP
import datetime


def seed_data():

    session = Session()
    
    session.query(RSVP).delete()
    session.query(Event).delete()
    session.query(Guest).delete()
    session.commit()

    
    guest1 = Guest(name="Alice", email="alice@example.com")
    guest2 = Guest(name="Bob", email="bob@example.com")

    event1 = Event(
        title="Tech Meetup",
        location="Nairobi",
        date=datetime.date(2025, 6, 5),
    )
    event2 = Event(
        title="Python Conference",
        location="Mombasa",
        date=datetime.date(2025, 7, 10),
    )

    session.add_all([guest1, guest2, event1, event2])
    session.commit()

    rsvp1 = RSVP(guest=guest1, event=event1, status="Yes")
    rsvp2 = RSVP(guest=guest2, event=event2, status="Maybe")
    session.add_all([rsvp1, rsvp2])
    session.commit()
    print("Seed data created.")
