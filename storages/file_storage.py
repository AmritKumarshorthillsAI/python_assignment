import csv
from .storage import Storage

class FileStorage_pdf(Storage):
    def store(self, data):
        with open('extracted_data_pdf.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow([item])

class FileStorage_docx(Storage):
    def store(self, data):
        with open('extracted_data_docx.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow([item])

class FileStorage_ppt(Storage):
    def store(self, data):
        with open('extracted_data_ppt.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow([item])
