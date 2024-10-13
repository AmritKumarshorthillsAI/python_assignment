import csv
from .storage import Storage

class FileStorage(Storage):
    def store(self, data):
        with open('extracted_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow([item])
