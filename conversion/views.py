import os
import pypandoc
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from .models import Files

def save_and_convert(request):
    if request.method == "POST":
        # Get the uploaded file from the request
        uploaded_file = request.FILES['document']

        # Save the original file to the media directory
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.read())

        # Convert the file to HTML using pypandoc
        html_output = pypandoc.convert_file(file_path, 'html', format='docx')

        # Save the HTML output to the media directory
        html_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name + '.html')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

        # Create a FileResponse object containing the HTML file
        download_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name + '.html')
        download_name = uploaded_file.name + '.html'
        response = FileResponse(open(download_path, 'rb'))
        response['content_type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=%s' % download_name

        return response
        
    return render(request, 'save_and_convert.html')
