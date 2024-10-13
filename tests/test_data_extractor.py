import unittest
from extractors.pdf_loader import PDFLoader
from extractors.docx_loader import DOCXLoader
from extractors.ppt_loader import PPTLoader
from data_extractors.data_extractor import DataExtractor

class TestDataExtractor(unittest.TestCase):
    def setUp(self):
        # Initialize loaders
        self.pdf_loader = PDFLoader()
        self.docx_loader = DOCXLoader()
        self.ppt_loader = PPTLoader()

    def test_extract_text_pdf(self):
        extractor = DataExtractor(self.pdf_loader)
        text, metadata = extractor.extract_text('resources/sample.pdf')
        self.assertIsInstance(text, list)
        self.assertIsInstance(metadata, dict)

    def test_extract_text_docx(self):
        extractor = DataExtractor(self.docx_loader)
        text, metadata = extractor.extract_text('resources/sample.docx')
        self.assertIsInstance(text, list)
        self.assertIsInstance(metadata, dict)

    def test_extract_text_ppt(self):
        extractor = DataExtractor(self.ppt_loader)
        text, metadata = extractor.extract_text('resources/sample.pptx')
        self.assertIsInstance(text, list)
        self.assertIsInstance(metadata, dict)

    def test_extract_links(self):
        extractor = DataExtractor(self.docx_loader)
        links = extractor.extract_links('resources/sample.docx')
        # Replace with actual expected links
        self.assertIsInstance(links, list)

    def test_extract_images(self):
        extractor = DataExtractor(self.pdf_loader)
        images = extractor.extract_images('resources/sample.pdf')
        # Replace with actual expected image metadata
        self.assertIsInstance(images, list)

    def test_extract_tables(self):
        extractor = DataExtractor(self.docx_loader)
        tables = extractor.extract_tables('resources/sample.docx')
        # Replace with actual expected table data
        self.assertIsInstance(tables, list)

if __name__ == '__main__':
    unittest.main()
