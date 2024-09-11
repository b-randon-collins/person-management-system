#  person.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from db import Base, get_session



class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    dob = Column(String, nullable=True)
	# phone_numbers = relationship("PhoneNumber", back_populates="person", cascade="all, delete-orphan")
	# email_addresses = relationship("EmailAddress", back_populates="person", cascade="all, delete-orphan")

    @staticmethod
    def list_people():
        session = get_session()

        try:
            people_list = session.query(Person).all()

            if people_list:
                for id, person in enumerate(people_list, 1):
                    pass
            else:
                print("No people found.")
                
            return people_list

        except Exception as e:
            print(f"Error retrieving people: {str(e)}")
            return []

        finally:
            session.close()

    @staticmethod
    def add_person():
        print("add Person selected")