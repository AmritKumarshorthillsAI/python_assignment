import os
from extractors.pdf_loader import PDFLoader
from extractors.docx_loader import DOCXLoader
from extractors.ppt_loader import PPTLoader
from data_extractors.data_extractor import DataExtractor
from storages.file_storage import FileStorage_pdf, FileStorage_docx, FileStorage_ppt
from storages.sql_storage import SQLStorage_pdf, SQLStorage_docx, SQLStorage_ppt

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


        # Extract and print links, tables and images from PDF
        links_pdf = pdf_extractor.extract_links(test_files['pdf'])
        images_pdf = pdf_extractor.extract_images(test_files['pdf'])
        tables_pdf = pdf_extractor.extract_tables(test_files['pdf'])
        print("PDF Links:", links_pdf)
        print("PDF Images:", images_pdf)
        print("PDF Tables:", tables_pdf)

        # Example of storing the extracted PDF text
        file_storage = FileStorage_pdf()
        file_storage.store(pdf_text)  # Store PDF text to CSV
        file_storage.store(pdf_metadata)
        file_storage.store(links_pdf)
        file_storage.store(images_pdf)
        file_storage.store(tables_pdf)

        # Example of storing the extracted DOCX text
        sql_storage = SQLStorage_pdf()
        sql_storage.store(pdf_text)  # Store DOCX text in SQL database
        sql_storage.store(pdf_metadata)
        sql_storage.store(links_pdf)

    # Extract and print text from DOCX
    if os.path.exists(test_files['docx']):
        docx_text, docx_metadata = docx_extractor.extract_text(test_files['docx'])
        print("DOCX Text:", docx_text)
        print("DOCX Metadata:", docx_metadata)

        
        # Extract and print images, tables and links from DOCX
        links_docx = docx_extractor.extract_links(test_files['docx'])
        images_docx = docx_extractor.extract_images(test_files['docx'])
        tables_docx = docx_extractor.extract_tables(test_files['docx'])
        print("DOCX Links:", links_docx)
        print("DOCX Images:", images_docx)
        print("DOCX Tables:", tables_docx)

        # Example of storing the extracted DOCX text
        sql_storage = SQLStorage_docx()
        sql_storage.store(docx_text)  # Store DOCX text in SQL database
        sql_storage.store(docx_metadata)
        sql_storage.store(links_docx)


        file_storage = FileStorage_docx()
        file_storage.store(docx_text)  # Store PDF text to CSV
        file_storage.store(docx_metadata)
        file_storage.store(links_docx)
        file_storage.store(images_docx)
        file_storage.store(tables_docx)

    # Extract and print text from PPT
    if os.path.exists(test_files['ppt']):
        ppt_text, ppt_metadata = ppt_extractor.extract_text(test_files['ppt'])
        print("PPT Text:", ppt_text)
        print("PPT Metadata:", ppt_metadata)

        
        # Extract and print links and images from PPT
        links_ppt = ppt_extractor.extract_links(test_files['ppt'])
        images_ppt = ppt_extractor.extract_images(test_files['ppt'])
        tables_ppt = ppt_extractor.extract_tables(test_files['ppt'])
        print("PPT Links:", links_ppt)
        print("PPT Images:", images_ppt)
        print("PPT Tables:", tables_ppt)

        file_storage = FileStorage_ppt()
        file_storage.store(ppt_text)  
        file_storage.store(ppt_metadata)
        file_storage.store(links_ppt)
        file_storage.store(images_ppt)
        file_storage.store(tables_ppt)

        sql_storage = SQLStorage_ppt()
        sql_storage.store(ppt_text)  # Store ppt text in SQL database
        sql_storage.store(ppt_metadata)
        sql_storage.store(links_ppt)


if __name__ == "__main__":
    main()
