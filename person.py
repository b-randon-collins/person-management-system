# person.py
from sqlalchemy import text
from initialize import engine

class Person:
    @staticmethod
    def list_people():
        with engine.connect() as connection:
            try:
                sql = text("SELECT * FROM person")
                result = connection.execute(sql)
                people_list = result.fetchall()

                if people_list:
                    for id, person in enumerate(people_list, 1):
                        # print(f"Person {id}: {person}")
                        pass
                else:
                    print("No people found.")

                return people_list

            except Exception as e:
                print(f"Error retrieving people: {str(e)}")
                return []

    @staticmethod
    def add_person(name, dob):
        with engine.connect() as connection:
            try:
                sql = text("INSERT INTO person (name, dob) VALUES (:name, :dob)")
                connection.execute(sql, {'name': name, 'dob': dob})
                print(f"Added person: {name}, DOB: {dob}")

            except Exception as e:
                print(f"Error adding person: {str(e)}")