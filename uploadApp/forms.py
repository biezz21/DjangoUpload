from django import forms

from .models import VCFUpload

class UploadForm(forms.ModelForm):
    class Meta:
        model = VCFUpload
        fields = {'title', 'vcf'}