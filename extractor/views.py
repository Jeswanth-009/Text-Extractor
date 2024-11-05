import os
from django.shortcuts import render
from django.conf import settings
from .models import Document
from .forms import DocumentForm
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

def extract_text(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.pdf':
        # Convert PDF to images
        images = convert_from_path(file_path)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        return text
    else:
        # Process image directly
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            
            # Extract text from the uploaded file
            file_path = os.path.join(settings.MEDIA_ROOT, document.file.name)
            extracted_text = extract_text(file_path)
            
            # Save the extracted text
            document.extracted_text = extracted_text
            document.save()
            
            return render(request, 'extractor/result.html', {
                'document': document,
                'extracted_text': extracted_text
            })
    else:
        form = DocumentForm()
    return render(request, 'extractor/upload.html', {'form': form})