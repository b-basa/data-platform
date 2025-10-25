from .crud import generate_engine

from .schema import Base

def initialize_database(engine):
    Base.metadata.create_all(engine)
    print("Tables created successfully!")


# Create tables
if __name__ == "__main__":
    initialize_database(generate_engine())
