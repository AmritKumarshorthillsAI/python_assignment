import os
from extractors.pdf_loader import PDFLoader
from extractors.docx_loader import DOCXLoader
from extractors.ppt_loader import PPTLoader
from data_extractors.data_extractor import DataExtractor
from storages.file_storage import FileStorage
from storages.sql_storage import SQLStorage

def main():
    # Specify the path to your test files
    test_files = {
        'pdf': 'resources/sample.pdf',
        'docx': 'resources/sample.docx',
        'ppt': 'resources/sample.pptx'
    }

    # Create instances of the loaders
    pdf_loader = PDFLoader()
    docx_loader = DOCXLoader()
    ppt_loader = PPTLoader()

    # Create instances of the data extractor for each file type
    pdf_extractor = DataExtractor(pdf_loader)
    docx_extractor = DataExtractor(docx_loader)
    ppt_extractor = DataExtractor(ppt_loader)

    # Extract and print text from PDF
    if os.path.exists(test_files['pdf']):
        pdf_text, pdf_metadata = pdf_extractor.extract_text(test_files['pdf'])
        print("PDF Text:", pdf_text)
        print("PDF Metadata:", pdf_metadata)

        # Example of storing the extracted PDF text
        file_storage = FileStorage()
        file_storage.store(pdf_text)  # Store PDF text to CSV

    # Extract and print text from DOCX
    if os.path.exists(test_files['docx']):
        docx_text, docx_metadata = docx_extractor.extract_text(test_files['docx'])
        print("DOCX Text:", docx_text)
        print("DOCX Metadata:", docx_metadata)

        # Example of storing the extracted DOCX text
        sql_storage = SQLStorage()
        sql_storage.store(docx_text)  # Store DOCX text in SQL database

    # Extract and print text from PPT
    if os.path.exists(test_files['ppt']):
        ppt_text, ppt_metadata = ppt_extractor.extract_text(test_files['ppt'])
        print("PPT Text:", ppt_text)
        print("PPT Metadata:", ppt_metadata)

        # Example of storing the extracted PPT text
        file_storage.store(ppt_text)  # Store PPT text to CSV

    # Extract links, images, and tables if implemented
    # Note: Implement these methods in DataExtractor for actual use
    # links_pdf = pdf_extractor.extract_links(test_files['pdf'])
    # images_pdf = pdf_extractor.extract_images(test_files['pdf'])
    # tables_docx = docx_extractor.extract_tables(test_files['docx'])
    
    # Print the extracted links, images, and tables
    # print("PDF Links:", links_pdf)
    # print("PDF Images:", images_pdf)
    # print("DOCX Tables:", tables_docx)

if __name__ == "__main__":
    main()
