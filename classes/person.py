import sqlite3

CONN = sqlite3.connect('resources.db')
CURSOR = CONN.cursor()

class Person:
    def __init__(self, id=None, name=None, dob=None):
        self.id = id
        self.name = name
        self.dob = dob

    @staticmethod
    def create_table():
        sql = '''
        CREATE TABLE IF NOT EXISTS Person (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dob TEXT
        )
        '''
        CURSOR.execute(sql)

    @staticmethod
    def add_person(name, dob=None):
        sql = '''
        INSERT INTO Person (name, dob)
        VALUES (?, ?)
        '''
        CURSOR.execute(sql, (name, dob))
        CONN.commit()

    @staticmethod
    def list_people():
        sql = 'SELECT * FROM Person'
        people = CURSOR.execute(sql).fetchall()

        return [Person(id=row[0], name=row[1], dob=row[2]) for row in people]


    @staticmethod
    def get_person(person_id):
        sql = 'SELECT * FROM Person WHERE id = ?'
        return CURSOR.execute(sql, (person_id,)).fetchone()

    @staticmethod
    def edit_name(person_id, new_name):
        sql = 'UPDATE Person SET name = ? WHERE id = ?'
        CURSOR.execute(sql, (new_name, person_id))
        CONN.commit()

    @staticmethod
    def edit_dob(person_id, new_dob):
        sql = 'UPDATE Person SET dob = ? WHERE id = ?'
        CURSOR.execute(sql, (new_dob, person_id))
        CONN.commit()

    @staticmethod
    def delete_person(person_id):
        sql = 'DELETE FROM Person WHERE id = ?'
        CURSOR.execute(sql, (person_id,))
        CONN.commit()
