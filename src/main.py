import sys
from docx_to_pdf_converter import DocxToPdfConverter

class Main:
    """
    Main class to run the docx to pdf converter.
    """

    def __init__(self):
        """
        Initializes the Main class.
        """
        pass

    def run(self):
        """
        Runs the docx to pdf converter.
        """
        if len(sys.argv) != 2:
            print("Usage: python src/main.py <path_to_docx_file>")
            sys.exit(1)

        input_path = sys.argv[1]
        converter = DocxToPdfConverter(input_path)
        converter.convert()

if __name__ == "__main__":
    main = Main()
    main.run()


