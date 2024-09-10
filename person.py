#  person.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dob = Column(String, nullable=True)
	# phone_numbers = relationship("PhoneNumber", back_populates="person", cascade="all, delete-orphan")
	# email_addresses = relationship("EmailAddress", back_populates="person", cascade="all, delete-orphan")