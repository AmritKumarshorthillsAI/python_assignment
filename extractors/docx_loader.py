import docx
from .base_file_loader import FileLoader

class DOCXLoader(FileLoader):
    def validate_file(self, file_path):
        return file_path.endswith('.docx')

    def load_file(self, file_path):
        doc = docx.Document(file_path)
        text = [paragraph.text for paragraph in doc.paragraphs]
        return text, doc.core_properties
