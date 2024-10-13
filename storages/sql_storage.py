import sqlite3
from .storage import Storage


class SQLStorage(Storage):
    def store(self, data):
        connection = sqlite3.connect('extracted_data.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS data (text TEXT)')
        cursor.executemany('INSERT INTO data (text) VALUES (?)', [(item,) for item in data])
        connection.commit()
        connection.close()
