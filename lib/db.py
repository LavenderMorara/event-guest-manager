from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///event_guest_manager.db')
Session = sessionmaker(bind=engine)
session = Session()
