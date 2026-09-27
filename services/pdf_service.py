"""
Backend PDF processing service fallback for ToolHub using PyPDF.
"""
import io
from pypdf import PdfReader, PdfWriter

class PDFService:
    @staticmethod
    def get_metadata(pdf_bytes):
        reader = PdfReader(io.BytesIO(pdf_bytes))
        meta = reader.metadata or {}
        return {
            'num_pages': len(reader.pages),
            'title': meta.get('/Title', 'Unknown'),
            'author': meta.get('/Author', 'Unknown'),
            'subject': meta.get('/Subject', 'Unknown'),
            'creator': meta.get('/Creator', 'Unknown'),
            'producer': meta.get('/Producer', 'Unknown')
        }

    @staticmethod
    def merge_pdfs(list_of_pdf_bytes):
        writer = PdfWriter()
        for pdf_bytes in list_of_pdf_bytes:
            reader = PdfReader(io.BytesIO(pdf_bytes))
            for page in reader.pages:
                writer.add_page(page)
        
        output = io.BytesIO()
        writer.write(output)
        return output.getvalue()

    @staticmethod
    def extract_pages(pdf_bytes, page_numbers):
        reader = PdfReader(io.BytesIO(pdf_bytes))
        writer = PdfWriter()
        
        total_pages = len(reader.pages)
        for page_num in page_numbers:
            if 1 <= page_num <= total_pages:
                writer.add_page(reader.pages[page_num - 1])
                
        output = io.BytesIO()
        writer.write(output)
        return output.getvalue()
