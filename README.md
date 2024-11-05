# Text-Extractor
# Text Extractor - PDF and Image OCR Application

A Django web application that extracts text from PDF documents and images using Tesseract OCR engine.

## Features

- Upload PDF documents and images (supports formats like PNG, JPEG, TIFF)
- Extract text from PDFs by converting them to images first
- Direct text extraction from image files
- Clean, responsive Bootstrap-based UI
- View and copy extracted text
- Stores upload history with extracted text

## Prerequisites

Before running this application, make sure you have the following installed:

1. Python 3.8 or higher
2. Tesseract OCR engine
   - Windows: Download and install from [GitHub Tesseract Release](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`
3. Poppler (for PDF processing)
   - Windows: Download and add to PATH from [Poppler Releases](http://blog.alivate.com.au/poppler-windows/)
   - Linux: `sudo apt-get install poppler-utils`
   - macOS: `brew install poppler`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd text-extractor
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create necessary directories:
   ```bash
   mkdir media
   mkdir media/documents
   ```

5. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000`

## Project Structure

```
text_extractor/
├── manage.py
├── requirements.txt
├── media/
│   └── documents/
├── text_extractor/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── extractor/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    └── templates/
        └── extractor/
            ├── base.html
            ├── upload.html
            └── result.html
```

## Usage

1. Start the application and navigate to `http://127.0.0.1:8000`
2. Click "Choose File" to select a PDF document or image
3. Click "Extract Text" to process the file
4. View the extracted text on the results page
5. Use "Upload Another File" to process more documents

## Supported File Types

- PDF documents (*.pdf)
- Images:
  - PNG (*.png)
  - JPEG (*.jpg, *.jpeg)
  - TIFF (*.tiff, *.tif)
  - BMP (*.bmp)
  - GIF (*.gif)

## Technical Details

- **Framework**: Django 5.0.1
- **OCR Engine**: Tesseract (via pytesseract 0.3.10)
- **PDF Processing**: pdf2image 1.16.3
- **Image Processing**: Pillow 10.2.0
- **Frontend**: Bootstrap 5.3
- **Database**: SQLite (default)

## Features in Detail

### Document Model
- Stores uploaded files in `media/documents/`
- Records upload timestamp
- Saves extracted text for future reference

### File Processing
- Automatic detection of file type (PDF vs Image)
- PDF files are converted to images using pdf2image
- Images are processed directly with Tesseract OCR
- Text extraction is handled by pytesseract

### User Interface
- Responsive design using Bootstrap
- Clean and intuitive upload form
- Formatted text output display
- Navigation between upload and results

## Error Handling

The application includes error handling for:
- Invalid file types
- Failed OCR processing
- File upload issues
- Database operations

## Security Considerations

- CSRF protection enabled
- File upload validation
- Secure file handling
- Django security middleware enabled

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Framework
- Tesseract OCR
- Bootstrap
- Python PDF and Image Processing Communities
