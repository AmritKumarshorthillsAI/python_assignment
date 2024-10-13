import unittest
import os
import sqlite3
from storages.file_storage import FileStorage
from storages.sql_storage import SQLStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.test_data = ["Sample text 1", "Sample text 2"]

    def test_store_file(self):
        self.file_storage.store(self.test_data)
        self.assertTrue(os.path.exists('extracted_data.csv'))
        # Clean up
        os.remove('extracted_data.csv')

class TestSQLStorage(unittest.TestCase):
    def setUp(self):
        self.sql_storage = SQLStorage()
        self.test_data = ["Sample text 1", "Sample text 2"]

    def test_store_sql(self):
        self.sql_storage.store(self.test_data)
        # Check if data is stored correctly
        connection = sqlite3.connect('extracted_data.db')
        cursor = connection.cursor()
        cursor.execute('SELECT text FROM data')
        results = cursor.fetchall()
        connection.close()

        self.assertEqual(len(results), 2)
        self.assertIn(("Sample text 1",), results)
        self.assertIn(("Sample text 2",), results)

        # Clean up
        connection = sqlite3.connect('extracted_data.db')
        cursor = connection.cursor()
        cursor.execute('DROP TABLE data')
        connection.commit()
        connection.close()

if __name__ == '__main__':
    unittest.main()
