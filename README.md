# 📝 Automatic DOCX to PDF File Converter

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-docx-to-pdf-converter?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-docx-to-pdf-converter?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-docx-to-pdf-converter?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-docx-to-pdf-converter?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-docx-to-pdf-converter?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created solely for learning purposes.
> It is not intended for production use.

## ℹ️ About

This project is a Python application designed to automatically convert `.docx` files to `.pdf`. It was developed to demonstrate the ability to automate office tasks using Python, focusing on simplicity and document conversion efficiency.

## 🚀 Features

* **Automatic Conversion**: Programmatically converts `.docx` files to `.pdf`.
* **Command-Line Interface (CLI)**: Enables conversion execution via terminal.
* **Clean Project Structure**: Organized into `src` and `tests` directories for better maintainability and scalability.

## 🛠️ Technologies Used

* **Python 3.x**
* **`python-docx`**: For handling `.docx` files.
* **`reportlab` or similar**: For generating `.pdf` files (to be defined).
* **`pytest`**: For unit testing.

## ⚙️ How to Run the Project

### Prerequisites

* Python 3.x installed on your system.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/alexandrekatsuura/python-docx-to-pdf-converter
   cd python-docx-to-pdf-converter
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # On Linux/macOS
   # .venv\\Scripts\\activate       # On Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

To convert a file, run the following command from the project root:

```bash
python src/main.py <path_to_file.docx>
```

The converted PDF file will be saved in the same directory as the original DOCX file, with the same name and a `.pdf` extension.

## ✅ Running Tests

To run the unit tests, execute the following command from the project root directory:

```bash
pytest -v
```

This command will discover and run all tests located in the `tests/` directory.

## 📁 Project Structure

```bash
python-docx-to-pdf-converter/
├── src/
│   ├── __init__.py
│   └── docx_to_pdf_converter.py  # Contains conversion logic
│   └── main.py                   # Contains the main execution logic
├── tests/
│   ├── __init__.py
│   └── test_docx_to_pdf_converter.py  # Unit tests for the converter class
├── .gitignore                    # Python .gitignore standard
├── README.md                     # This documentation file
└── requirements.txt              # Project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).
