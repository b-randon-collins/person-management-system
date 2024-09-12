import sqlite3

CONN = sqlite3.connect('resource.db')
CURSOR = CONN.cursor()

class PhoneNumber:
    def __init__(self, id=None, person_id=None, phone_number=None):
        self.id = id
        self.person_id = person_id
        self.phone_number = phone_number

    @staticmethod
    def create_table():
        sql = '''
        CREATE TABLE IF NOT EXISTS PhoneNumbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            phone_number TEXT NOT NULL,
            FOREIGN KEY (person_id) REFERENCES Person(id) ON DELETE CASCADE
        )
        '''
        CURSOR.execute(sql)

    @staticmethod
    def add_phone_number(person_id, phone_number):
        sql = '''
        INSERT INTO PhoneNumbers (person_id, phone_number)
        VALUES (?, ?)
        '''
        CURSOR.execute(sql, (person_id, phone_number))
        CONN.commit()

    @staticmethod
    def get_phone_numbers(person_id):
        sql = 'SELECT * FROM PhoneNumbers WHERE person_id = ?'
        return CURSOR.execute(sql, (person_id,)).fetchall()

    @staticmethod
    def edit_phone_number(phone_id, new_phone_number):
        sql = 'UPDATE PhoneNumbers SET phone_number = ? WHERE id = ?'
        CURSOR.execute(sql, (new_phone_number, phone_id))
        CONN.commit()

    @staticmethod
    def delete_phone_number(phone_id):
        sql = 'DELETE FROM PhoneNumbers WHERE id = ?'
        CURSOR.execute(sql, (phone_id,))
        CONN.commit()
