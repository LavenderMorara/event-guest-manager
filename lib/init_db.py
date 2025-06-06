from lib.models import Base, engine


def init_db():
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    init_db()
