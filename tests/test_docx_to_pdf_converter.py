
import os
import pytest
from docx import Document
from src.docx_to_pdf_converter import DocxToPdfConverter

@pytest.fixture
def create_dummy_docx():
    """
    Creates a dummy .docx file for testing.
    """
    file_path = "dummy_test_document.docx"
    document = Document()
    document.add_paragraph("This is a test document.")
    document.save(file_path)
    yield file_path
    os.remove(file_path)
    if os.path.exists("dummy_test_document.pdf"):
        os.remove("dummy_test_document.pdf")

def test_convert_creates_pdf(create_dummy_docx):
    """
    Tests if the convert method creates a .pdf file.
    """
    converter = DocxToPdfConverter(create_dummy_docx)
    converter.convert()
    assert os.path.exists(converter.output_path)

def test_converter_raises_file_not_found():
    """
    Tests if the converter raises FileNotFoundError for a non-existent file.
    """
    with pytest.raises(FileNotFoundError):
        DocxToPdfConverter("non_existent_file.docx")


