from db import initialize_database, engine, get_session
from person import Person

print("Initializing database...")
initialize_database()

print("Getting session...")
session = get_session()

print("Clearing existing Person records...")
try:
    session.query(Person).filter(Person.id != 1).delete()
    print("Existing Person records cleared.")
except Exception as e:
    print(f"Error clearing existing Person records: {str(e)}")

print("Adding demo people...")
demo_people = [
    {"name": "Brandon Lee", "dob": "1991-07-05"},
    {"name": "Jane Smith", "dob": "1985-03-22"},
    {"name": "Michael Johnson", "dob": "1979-11-15"},
    {"name": "Emily Brown", "dob": "1993-08-28"},
    {"name": "David Wilson", "dob": "1987-04-12"}
]

for person_data in demo_people:
    try:
        print(f"Processing person: {person_data['name']}")
        new_person = Person(**person_data)
        session.add(new_person)
        print(f"Added person: {person_data['name']}")
    except Exception as e:
        print(f"Error adding person {person_data['name']}: {str(e)}")
        session.rollback()
    else:
        session.commit()
        print(f"Committed person {person_data['name']} successfully.")

print("Closing session...")
session.close()

print("Disposing engine...")
engine.dispose()

print("Script completed.")
