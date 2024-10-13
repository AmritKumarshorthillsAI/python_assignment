import unittest
from extractors.pdf_loader import PDFLoader
from extractors.docx_loader import DOCXLoader
from extractors.ppt_loader import PPTLoader

class TestFileLoaders(unittest.TestCase):
    def test_pdf_loader(self):
        loader = PDFLoader()
        self.assertTrue(loader.validate_file('resources/sample.pdf'))
        text, metadata = loader.load_file('resources/sample.pdf')
        self.assertIsInstance(text, list)
        self.assertIsInstance(metadata, dict)

    def test_docx_loader(self):
        loader = DOCXLoader()
        self.assertTrue(loader.validate_file('resources/sample.docx'))
        text, metadata = loader.load_file('resources/sample.docx')
        self.assertIsInstance(text, list)
        self.assertIsInstance(metadata, dict)

    def test_ppt_loader(self):
        loader = PPTLoader()
        self.assertTrue(loader.validate_file('resources/sample.pptx'))
        text, metadata = loader.load_file('resources/sample.pptx')
        self.assertIsInstance(text, list)
        self.assertIsInstance(metadata, dict)

if __name__ == '__main__':
    unittest.main()
