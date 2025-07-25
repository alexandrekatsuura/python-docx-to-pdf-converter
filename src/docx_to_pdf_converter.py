import os
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

class DocxToPdfConverter:
    """
    A class to convert .docx files to .pdf files.
    """

    def __init__(self, input_path):
        """
        Initializes the DocxToPdfConverter with the input file path.

        Args:
            input_path (str): The path to the .docx file.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"The file was not found: {input_path}")
        self.input_path = input_path
        self.output_path = os.path.splitext(input_path)[0] + ".pdf"

    def convert(self):
        """
        Converts the .docx file to a .pdf file.
        """
        try:

            document = Document(self.input_path)
            c = canvas.Canvas(self.output_path, pagesize=letter)
            width, height = letter

            margin_x = 40
            margin_y = 40
            line_height = 15
            paragraph_spacing = 10
            max_width = width - 2 * margin_x
            y = height - margin_y

            for para in document.paragraphs:
                text = para.text
                lines = simpleSplit(text, 'Helvetica', 12, max_width)
                
                for line in lines:
                    if y < margin_y:
                        c.showPage()
                        y = height - margin_y
                    c.drawString(margin_x, y, line)
                    y -= line_height
                y -= paragraph_spacing

                

            c.save()
            print(f"Successfully converted {self.input_path} to {self.output_path}")
        except Exception as e:
            print(f"An error occurred during conversion: {e}")


