import PyPDF2
from .base_file_loader import FileLoader

class PDFLoader(FileLoader):
    def validate_file(self, file_path):
        return file_path.endswith('.pdf')

    def load_file(self, file_path):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return [page.extract_text() for page in reader.pages], reader.metadata
