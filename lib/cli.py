from lib.models.guests import Guest
from lib.models.events import Event
from lib.models.rsvp import RSVP
from lib.seed import seed_data
from lib.helper import print_menu
from lib.db import session as session


def list_guests():
    print("\nGuests:")
    for guest in session.query(Guest).all():
        print(f"ID: {guest.id}, Name: {guest.name}, Email: {guest.email}")

def list_events():
    print("\n Events:")
    for event in session.query(Event).all():
        print(f"ID: {event.id}, Title: {event.title}, Location: {event.location}, Date: {event.date}")
        
def create_event():
    title = input("Enter event title: ")
    location = input("Enter event location: ")
    date_str = input("Enter event date (YYYY-MM-DD): ")
    try:
        from datetime import datetime
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return
    event = Event(title=title, location=location, date=date)
    session.add(event)
    session.commit()
    print(f"Event '{title}' created.")

def update_event():
    list_events()
    event_id = input("Enter event ID to update: ")
    event = session.query(Event).filter_by(id=event_id).first()
    if not event:
        print("Event not found.")
        return
    title = input(f"Enter new title (leave blank to keep '{event.title}'): ")
    location = input(f"Enter new location (leave blank to keep '{event.location}'): ")
    date_str = input(f"Enter new date (YYYY-MM-DD) (leave blank to keep '{event.date}'): ")
    if title:
        event.title = title
    if location:
        event.location = location
    if date_str:
        try:
            from datetime import datetime
            event.date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Date not updated.")
    session.commit()
    print("Event updated.")

def delete_event():
    list_events()
    event_id = input("Enter event ID to delete: ")
    event = session.query(Event).filter_by(id=event_id).first()
    if not event:
        print("Event not found.")
        return
    session.delete(event)
    session.commit()
    print("Event deleted.")

def add_guest_to_event():
    name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    guest = session.query(Guest).filter_by(email=email).first()
    if not guest:
        guest = Guest(name=name, email=email)
        session.add(guest)
        session.commit()
        print(f"Guest '{name}' added.")
    list_events()
    event_id = input("Enter event ID to add guest to: ")
    event = session.query(Event).filter_by(id=event_id).first()
    if not event:
        print("Event not found.")
        return
    # Check if RSVP already exists
    rsvp = session.query(RSVP).filter_by(guest_id=guest.id, event_id=event.id).first()
    if rsvp:
        print("Guest already added to this event.")
        return
    rsvp = RSVP(guest=guest, event=event, status="No RSVP")
    session.add(rsvp)
    session.commit()
    print(f"Guest '{guest.name}' added to event '{event.title}'.")

def update_guest_info():
    list_guests()
    guest_id = input("Enter guest ID to update: ")
    guest = session.query(Guest).filter_by(id=guest_id).first()
    if not guest:
        print("Guest not found.")
        return
    name = input(f"Enter new name (leave blank to keep '{guest.name}'): ")
    email = input(f"Enter new email (leave blank to keep '{guest.email}'): ")
    if name:
        guest.name = name
    if email:
        guest.email = email
    session.commit()
    print("Guest info updated.")

def delete_guest():
    list_guests()
    guest_id = input("Enter guest ID to delete: ")
    guest = session.query(Guest).filter_by(id=guest_id).first()
    if not guest:
        print("Guest not found.")
        return
    session.delete(guest)
    session.commit()
    print("Guest deleted.")

def rsvp_for_guest():
    list_guests()
    guest_id = input("Enter guest ID for RSVP: ")
    guest = session.query(Guest).filter_by(id=guest_id).first()
    if not guest:
        print("Guest not found.")
        return
    list_events()
    event_id = input("Enter event ID for RSVP: ")
    event = session.query(Event).filter_by(id=event_id).first()
    if not event:
        print("Event not found.")
        return
    rsvp = session.query(RSVP).filter_by(guest_id=guest.id, event_id=event.id).first()
    if not rsvp:
        rsvp = RSVP(guest=guest, event=event)
        session.add(rsvp)
    status = input("Enter RSVP status (Yes, No, Maybe): ")
    if status not in ["Yes", "No", "Maybe"]:
        print("Invalid RSVP status.")
        return
    rsvp.status = status
    session.commit()
    print(f"RSVP status for guest '{guest.name}' updated to '{status}'.")

def view_guests_by_rsvp_status():
    list_events()
    event_id = input("Enter event ID to filter guests by RSVP status: ")
    event = session.query(Event).filter_by(id=event_id).first()
    if not event:
        print("Event not found.")
        return
    status = input("Enter RSVP status to filter by (Yes, No, Maybe): ")
    if status not in ["Yes", "No", "Maybe"]:
        print("Invalid RSVP status.")
        return
    rsvps = session.query(RSVP).filter_by(event_id=event.id, status=status).all()
    print(f"\\nGuests with RSVP status '{status}' for event '{event.title}':")
    for rsvp in rsvps:
        print(rsvp.guest)

def main():
    print("\\n=== Event Guest Manager CLI ===")
    seed_data()
    while True:
        print_menu()
        choice = input("\\nEnter option: ")
        if choice == '1':
            list_guests()
        elif choice == '2':
            list_events()
        elif choice == '3':
            create_event()
        elif choice == '4':
            update_event()
        elif choice == '5':
            delete_event()
        elif choice == '6':
            add_guest_to_event()
        elif choice == '7':
            update_guest_info()
        elif choice == '8':
            delete_guest()
        elif choice == '9':
            rsvp_for_guest()
        elif choice == '10':
            view_guests_by_rsvp_status()
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
