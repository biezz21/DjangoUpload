from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import VCFUpload

# Create your views here.
def vcf_list(request):
    return render(request, 'list.html', {})

def upload_vcf(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vcf_list')
    
    else:
        form = UploadForm()
    return render(request, 'upload.html', {
        'form': form,
    })