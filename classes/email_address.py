import sqlite3

CONN = sqlite3.connect('resource.db')
CURSOR = CONN.cursor()

class EmailAddress:
    def __init__(self, id=None, person_id=None, email_address=None):
        self.id = id
        self.person_id = person_id
        self.email_address = email_address

    @staticmethod
    def create_table():
        sql = '''
        CREATE TABLE IF NOT EXISTS EmailAddresses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            email_address TEXT NOT NULL,
            FOREIGN KEY (person_id) REFERENCES Person(id) ON DELETE CASCADE
        )
        '''
        CURSOR.execute(sql)

    @staticmethod
    def add_email_address(person_id, email_address):
        sql = '''
        INSERT INTO EmailAddresses (person_id, email_address)
        VALUES (?, ?)
        '''
        CURSOR.execute(sql, (person_id, email_address))
        CONN.commit()

    @staticmethod
    def get_email_addresses(person_id):
        sql = 'SELECT * FROM EmailAddresses WHERE person_id = ?'
        return CURSOR.execute(sql, (person_id,)).fetchall()

    @staticmethod
    def edit_email_address(email_id, new_email_address):
        sql = 'UPDATE EmailAddresses SET email_address = ? WHERE id = ?'
        CURSOR.execute(sql, (new_email_address, email_id))
        CONN.commit()

    @staticmethod
    def delete_email_address(email_id):
        sql = 'DELETE FROM EmailAddresses WHERE id = ?'
        CURSOR.execute(sql, (email_id,))
        CONN.commit()
