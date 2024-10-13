import sqlite3
from .storage import Storage


class SQLStorage_pdf(Storage):
    def store(self, data):
        connection = sqlite3.connect('extracted_data_pdf.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS data (text TEXT)')
        cursor.executemany('INSERT INTO data (text) VALUES (?)', [(item,) for item in data])
        connection.commit()
        connection.close()

class SQLStorage_docx(Storage):
    def store(self, data):
        connection = sqlite3.connect('extracted_data_docx.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS data (text TEXT)')
        cursor.executemany('INSERT INTO data (text) VALUES (?)', [(item,) for item in data])
        connection.commit()
        connection.close()

class SQLStorage_ppt(Storage):
    def store(self, data):
        connection = sqlite3.connect('extracted_data_ppt.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS data (text TEXT)')
        cursor.executemany('INSERT INTO data (text) VALUES (?)', [(item,) for item in data])
        connection.commit()
        connection.close()