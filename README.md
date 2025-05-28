# Event Guest Manager

## 📋 Project Description

**Event Guest Manager** is a console-based Python application that helps event organizers create events and manage guest RSVPs. Guests can RSVP to multiple events, and each event can have multiple guests, creating a many-to-many relationship. The app uses **SQLAlchemy (ORM)** with **SQLite** for data storage.

---

## 🏗️ Project Structure

├── Pipfile
├── Pipfile.lock
├── README.md
├── lily/
│ ├── models/
│ │ ├── init.py # ORM setup and DB connection
│ │ ├── guest.py # Guest model
│ │ ├── event.py # Event model
│ │ └── rsvp.py # RSVP join model
│ ├── seed.py # Populates the database with test data
│ ├── cli.py # Command-line interface for the user
│ ├── debug.py # Play with models while developing
│ └── helper.py # Contains helper functions (CRUD)

markdown
Copy
Edit

---

## 🧠 Models Used

### `Guest`
- `id`: Integer (Primary Key)
- `name`: String
- `email`: String

### `Event`
- `id`: Integer (Primary Key)
- `title`: String
- `location`: String
- `date`: Date

### `RSVP` (Join Table)
- `id`: Integer (Primary Key)
- `guest_id`: ForeignKey to `Guest`
- `event_id`: ForeignKey to `Event`
- `status`: RSVP status (`Yes`, `No`, or `Maybe`)

---

## ⚙️ Setup Instructions

1. **Install dependencies**
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
Create the database tables

bash
Copy
Edit
python lily/models/create_tables.py
Seed the database (optional)

bash
Copy
Edit
python lily/seed.py
Run the app

bash
Copy
Edit
python lily/cli.py
🧪 Sample CLI Features (To Be Built)
Add new guest or event

RSVP a guest to an event

View all guests for an event

View all events a guest is attending

Update RSVP status

✅ Requirements Met
Uses ORM (SQLAlchemy) ✔️

Has at least 3 models with a many-to-many relationship ✔️

Structured into appropriate files with folders ✔️

