# # db.py
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# import os
# from db import initialize_database
# from person import Person


# DATABASE_URL = "sqlite:///resources.db"

# engine = create_engine(DATABASE_URL, echo=False)
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()

# def get_session():
#     return SessionLocal()

# def initialize_database():
#     try:
#         Base.metadata.create_all(engine)
#     except Exception as e:
#         print(f"Failed to create tables: {str(e)}")

# initialize_database()


from initialize import engine, SessionLocal

def get_session():
    return SessionLocal()
